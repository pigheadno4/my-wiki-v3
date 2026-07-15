"""Immutable, curated raw snapshots for checked-out GitHub repositories."""

from dataclasses import dataclass, replace
import fnmatch
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import tempfile
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

from github_git import ResolvedRef
from github_registry import RepoConfig
from github_releases import ReleaseNotesEvidence


_DEFAULT_EXCLUDED_PARTS = {
    ".git",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "vendor",
}
_LOCK_FILENAMES = {
    "cargo.lock",
    "composer.lock",
    "gemfile.lock",
    "package-lock.json",
    "pnpm-lock.yaml",
    "podfile.lock",
    "yarn.lock",
}
_DEFAULT_FILENAMES = {"package.json", "package.swift"}
_PUBLIC_EXAMPLE_PARTS = {"demo", "demos", "example", "examples", "sample", "samples"}
_PUBLIC_ENTRYPOINTS = {"index", "main", "public"}
_SAFE_CAPTURE_PART = re.compile(r"[^A-Za-z0-9._-]+")
_SUPPLEMENT_SUFFIX = re.compile(r"-r[0-9]+$")
_METADATA_MARKER = "<!-- github-snapshot-metadata-v1 -->"
_MANIFEST_VERSION = 1
_LOCK_NAME = ".promotion.lock"


class SnapshotError(ValueError):
    """A snapshot cannot be selected, validated, or promoted safely."""


@dataclass(frozen=True)
class SnapshotFile:
    path: str
    sha256: str
    size: int
    purpose: str


@dataclass(frozen=True)
class SelectionResult:
    selected: Tuple[Path, ...]
    excluded: Tuple[Tuple[str, str], ...]
    total_bytes: int


@dataclass(frozen=True)
class SnapshotRecord:
    repo_id: str
    ref: ResolvedRef
    capture_kind: str
    capture_revision: int
    collection_date: str
    staging_path: Path
    target_path: Path
    files: Tuple[SnapshotFile, ...]
    repository_url: str = ""
    company: str = ""
    repo_type: str = ""
    release_notes_source_url: Optional[str] = None
    release_notes_published_at: Optional[str] = None
    staging_device: Optional[int] = None
    staging_inode: Optional[int] = None


def select_key_files(
    config: RepoConfig, repo_root: Path, changed_paths: Sequence[str] = ()
) -> SelectionResult:
    """Select readable evidence files in a deterministic, bounded order."""
    repo_root = repo_root.resolve()
    candidates, excluded_items = _candidate_groups(config, repo_root, changed_paths)
    selected: List[Path] = []
    excluded: Dict[str, str] = dict(excluded_items)
    selected_paths = set()
    total_bytes = 0

    for paths in candidates:
        for path in paths:
            relative, reason = _candidate_relative(path, repo_root)
            label = relative or path.as_posix()
            if reason is not None:
                excluded[label] = reason
                continue
            if relative in selected_paths:
                continue
            reason = _exclusion_reason(config, path, relative)
            if reason is not None:
                excluded[relative] = reason
                continue
            try:
                size = path.stat().st_size
            except OSError:
                excluded[relative] = "candidate could not be read"
                continue
            if size > config.max_file_bytes:
                excluded[relative] = "exceeds per-file byte limit"
                continue
            if _is_binary(path):
                excluded[relative] = "binary content detected"
                continue
            if total_bytes + size > config.max_snapshot_bytes:
                excluded[relative] = "exceeds total snapshot byte limit"
                continue
            selected.append(path)
            selected_paths.add(relative)
            total_bytes += size

    return SelectionResult(
        selected=tuple(sorted(selected, key=lambda item: item.relative_to(repo_root).as_posix())),
        excluded=tuple(sorted(excluded.items())),
        total_bytes=total_bytes,
    )


def build_snapshot(
    config: RepoConfig,
    ref: ResolvedRef,
    repo_root: Path,
    raw_root: Path,
    staging_root: Path,
    collection_date: str,
    prior_snapshot: Optional[str] = None,
    capture_kind: str = "canonical",
    release_notes: Optional[ReleaseNotesEvidence] = None,
    changed_paths: Sequence[str] = (),
) -> SnapshotRecord:
    """Stage an immutable snapshot below ``raw/github/.staging``."""
    if ref.repo_id != config.id:
        raise SnapshotError("resolved reference repository does not match configuration")
    if capture_kind not in ("canonical", "supplement"):
        raise SnapshotError("capture_kind must be canonical or supplement")
    if release_notes is not None and not isinstance(release_notes.content, bytes):
        raise SnapshotError("release notes content must be bytes")

    raw_root = raw_root.resolve()
    staging_root = staging_root.resolve()
    required_staging_root = raw_root / ".staging"
    try:
        staging_root.relative_to(required_staging_root)
    except ValueError as error:
        raise SnapshotError("staging must live under raw/github/.staging") from error

    repo_root = repo_root.resolve()
    selection = select_key_files(config, repo_root, changed_paths)
    revision, target_path = _target_path(config, ref, raw_root, collection_date, capture_kind)
    staging_root.mkdir(parents=True, exist_ok=True)
    staging_path = Path(tempfile.mkdtemp(prefix="snapshot-", dir=str(staging_root)))
    staging_stat = _staging_stat(staging_path)
    files_root = staging_path / "files"
    snapshot_files: List[SnapshotFile] = []
    copied_total = 0

    try:
        for source in selection.selected:
            try:
                relative = source.relative_to(repo_root).as_posix()
            except ValueError as error:
                raise SnapshotError("selected file is no longer contained in checkout") from error
            if not _is_safe_relative_path(relative):
                raise SnapshotError("selected file is no longer contained in checkout")
            destination = files_root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            _require_contained(destination, files_root, "snapshot destination")
            sha256, size, is_binary = _copy_checkout_file(
                repo_root,
                relative,
                destination,
                config.max_file_bytes,
                config.max_snapshot_bytes - copied_total,
            )
            if is_binary:
                raise SnapshotError("copied file has binary content: " + relative)
            copied_total += size
            snapshot_files.append(
                SnapshotFile(
                    path=relative,
                    sha256=sha256,
                    size=size,
                    purpose=_purpose_for_path(config, repo_root, source),
                )
            )

        record = SnapshotRecord(
            repo_id=config.id,
            ref=ref,
            capture_kind=capture_kind,
            capture_revision=revision,
            collection_date=collection_date,
            staging_path=staging_path,
            target_path=target_path,
            files=tuple(sorted(snapshot_files, key=lambda item: item.path)),
            repository_url=config.url,
            company=config.company,
            repo_type=config.repo_type,
            release_notes_source_url=(release_notes.source_url if release_notes is not None else None),
            release_notes_published_at=(release_notes.published_at if release_notes is not None else None),
            staging_device=staging_stat.st_dev,
            staging_inode=staging_stat.st_ino,
        )
        metadata = _snapshot_metadata(config, record, prior_snapshot, selection.excluded, release_notes)
        if release_notes is not None:
            (staging_path / "release-notes.md").write_bytes(release_notes.content)
        _write_manifest(staging_path, metadata)
        return record
    except Exception:
        _clean_staging_path(staging_path, staging_stat)
        raise


def validate_staged_snapshot(record: SnapshotRecord) -> List[str]:
    """Return deterministic integrity failures for a staged snapshot."""
    errors: List[str] = []
    staging_error = _staging_identity_error(record)
    if staging_error is not None:
        return [staging_error]
    staging_path = record.staging_path
    manifest_path = staging_path / "snapshot.md"
    files_root = staging_path / "files"
    if not manifest_path.is_file() or manifest_path.is_symlink():
        return ["snapshot.md is missing"]
    if not files_root.is_dir() or files_root.is_symlink():
        return ["files directory is missing"]

    try:
        manifest = manifest_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return ["snapshot.md is not UTF-8"]
    metadata, metadata_error = _read_metadata(manifest)
    if metadata_error is not None:
        return [metadata_error]

    _validate_top_level(staging_path, metadata, errors)
    _validate_no_symlinks_or_diffs(staging_path, errors)
    _validate_identity(metadata, record, errors)
    manifest_files = _validate_manifest_files(metadata, record, errors)
    _validate_copied_files(files_root, manifest_files, errors)
    _validate_release_notes(staging_path, metadata, record, errors)
    return errors


def promote_snapshot(record: SnapshotRecord) -> Path:
    """Validate and atomically promote a staged snapshot without overwriting evidence."""
    snapshot_root = record.target_path.parent
    lock_path = snapshot_root / _LOCK_NAME
    lock_identity: Optional[Tuple[int, int]] = None
    try:
        snapshot_root.mkdir(parents=True, exist_ok=True)
        try:
            descriptor = os.open(str(lock_path), os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        except FileExistsError as error:
            _clean_staging(record)
            raise SnapshotError("promotion lock already exists: " + str(lock_path)) from error
        try:
            lock_stat = os.fstat(descriptor)
            lock_identity = (lock_stat.st_dev, lock_stat.st_ino)
            os.write(descriptor, str(os.getpid()).encode("ascii"))
        finally:
            os.close(descriptor)

        existing = _existing_canonical(record)
        if existing is not None:
            _clean_staging(record)
            return existing

        active_record = record
        if active_record.capture_kind == "supplement":
            active_record = _allocate_supplement(active_record)
        if _path_exists_or_is_symlink(active_record.target_path):
            raise SnapshotError("snapshot target already exists: " + str(active_record.target_path))

        errors = validate_staged_snapshot(active_record)
        if errors:
            raise SnapshotError("invalid staged snapshot:\n- " + "\n- ".join(errors))
        staging_error = _staging_identity_error(active_record)
        if staging_error is not None:
            raise SnapshotError(staging_error)
        active_record.target_path.parent.mkdir(parents=True, exist_ok=True)
        if active_record.staging_path.parent.stat().st_dev != active_record.target_path.parent.stat().st_dev:
            raise SnapshotError("staging and target must share a filesystem")
        try:
            active_record.staging_path.replace(active_record.target_path)
        except OSError as error:
            raise SnapshotError("could not promote snapshot: " + str(error)) from error
        return active_record.target_path
    except Exception:
        _clean_staging(record)
        raise
    finally:
        if lock_identity is not None:
            _remove_owned_lock(lock_path, lock_identity)


def _candidate_groups(
    config: RepoConfig, repo_root: Path, changed_paths: Sequence[str]
) -> Tuple[Tuple[Tuple[Path, ...], ...], Tuple[Tuple[str, str], ...]]:
    excluded: List[Tuple[str, str]] = []
    explicit = []
    for key_path in sorted(set(config.key_paths)):
        candidate, reason = _requested_path(repo_root, key_path)
        if reason is not None:
            excluded.append((key_path, reason))
            continue
        if not candidate.exists() and not candidate.is_symlink():
            excluded.append((key_path, "configured key path is missing"))
            continue
        explicit.extend(_expand_path(candidate))

    all_files = tuple(
        sorted(
            (path for path in repo_root.rglob("*") if path.is_file() or path.is_symlink()),
            key=lambda item: item.as_posix(),
        )
    )
    defaults = [
        path
        for path in all_files
        if _candidate_relative(path, repo_root)[0]
        and _is_default_path(Path(_candidate_relative(path, repo_root)[0]))
    ]
    changed = []
    for changed_path in sorted(set(changed_paths)):
        candidate, reason = _requested_path(repo_root, changed_path)
        if reason is not None:
            excluded.append((changed_path, reason))
            continue
        if not candidate.exists() and not candidate.is_symlink():
            excluded.append((changed_path, "changed path is missing"))
            continue
        relative, containment_reason = _candidate_relative(candidate, repo_root)
        if containment_reason is not None:
            changed.append(candidate)
        elif candidate.is_file() and _is_changed_public_path(Path(relative)):
            changed.append(candidate)
    return (
        tuple(sorted(set(explicit), key=lambda item: item.as_posix())),
        tuple(sorted(set(defaults), key=lambda item: item.as_posix())),
        tuple(sorted(set(changed), key=lambda item: item.as_posix())),
    ), tuple(excluded)


def _requested_path(repo_root: Path, requested: str) -> Tuple[Path, Optional[str]]:
    raw = Path(requested)
    if raw.is_absolute() or ".." in raw.parts:
        return repo_root / raw.name, "outside-checkout"
    return repo_root / raw, None


def _expand_path(path: Path) -> Iterable[Path]:
    if path.is_file() or path.is_symlink():
        return (path,)
    return tuple(item for item in path.rglob("*") if item.is_file() or item.is_symlink())


def _candidate_relative(path: Path, repo_root: Path) -> Tuple[Optional[str], Optional[str]]:
    try:
        lexical_relative = path.relative_to(repo_root)
    except ValueError:
        return None, "outside-checkout"
    if _has_symlink_component(path, repo_root):
        return lexical_relative.as_posix(), "symlink is not allowed"
    try:
        resolved_relative = path.resolve().relative_to(repo_root)
    except ValueError:
        return lexical_relative.as_posix(), "outside-checkout"
    return resolved_relative.as_posix(), None


def _has_symlink_component(path: Path, root: Path) -> bool:
    try:
        relative = path.relative_to(root)
    except ValueError:
        return False
    current = root
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            return True
    return False


def _is_default_path(relative: Path) -> bool:
    name = relative.name.lower()
    parts = {part.lower() for part in relative.parts}
    stem = relative.stem.lower()
    if name.startswith("readme") or name.startswith("changelog"):
        return True
    if "migration" in parts or "migrations" in parts or "migration" in stem:
        return True
    if name in _DEFAULT_FILENAMES or name.endswith(".podspec") or name.endswith(".gemspec"):
        return True
    return ("openapi" in stem or "swagger" in stem or "api-spec" in stem) and relative.suffix.lower() in {
        ".json",
        ".yaml",
        ".yml",
    }


def _is_changed_public_path(relative: Path) -> bool:
    parts = {part.lower() for part in relative.parts[:-1]}
    return bool(parts & _PUBLIC_EXAMPLE_PARTS) or relative.stem.lower() in _PUBLIC_ENTRYPOINTS


def _exclusion_reason(config: RepoConfig, path: Path, relative: str) -> Optional[str]:
    parts = {part.lower() for part in Path(relative).parts}
    if parts & _DEFAULT_EXCLUDED_PARTS:
        return "default build, dependency, or vendor exclusion"
    name = path.name.lower()
    if name in _LOCK_FILENAMES or name.endswith(".lock"):
        return "lock file exclusion"
    for pattern in config.exclude_paths:
        normalized = pattern.strip("/")
        if (
            fnmatch.fnmatch(relative, normalized)
            or fnmatch.fnmatch(name, normalized)
            or relative == normalized
            or relative.startswith(normalized + "/")
        ):
            return "registry exclusion: " + pattern
    return None


def _is_binary(path: Path) -> bool:
    try:
        with path.open("rb") as source:
            return b"\0" in source.read(8192)
    except OSError:
        return True


def _purpose_for_path(config: RepoConfig, repo_root: Path, path: Path) -> str:
    relative = path.relative_to(repo_root).as_posix()
    for key_path in config.key_paths:
        requested = Path(key_path)
        if requested.is_absolute() or ".." in requested.parts:
            continue
        key = requested.as_posix().strip("/")
        if relative == key or relative.startswith(key + "/"):
            return "registry key path"
    if _is_default_path(path.relative_to(repo_root)):
        return "default repository documentation"
    return "changed public entrypoint or example"


def _target_path(
    config: RepoConfig,
    ref: ResolvedRef,
    raw_root: Path,
    collection_date: str,
    capture_kind: str,
) -> Tuple[int, Path]:
    repository = config.id.rsplit("/", 1)[-1]
    snapshot_root = raw_root / config.company / repository / "snapshots"
    base = collection_date + "-" + _safe_capture_part(ref.version or ref.ref_name) + "-" + ref.sha[:7]
    if capture_kind == "canonical":
        return 0, snapshot_root / base
    revision = 1
    while (snapshot_root / (base + "-r" + str(revision))).exists():
        revision += 1
    return revision, snapshot_root / (base + "-r" + str(revision))


def _safe_capture_part(value: str) -> str:
    cleaned = _SAFE_CAPTURE_PART.sub("-", value).strip("-.")
    return cleaned or "ref"


def _snapshot_metadata(
    config: RepoConfig,
    record: SnapshotRecord,
    prior_snapshot: Optional[str],
    excluded: Sequence[Tuple[str, str]],
    release_notes: Optional[ReleaseNotesEvidence],
) -> dict:
    release_metadata = None
    if release_notes is not None:
        release_metadata = {
            "path": "release-notes.md",
            "source_url": record.release_notes_source_url,
            "published_at": record.release_notes_published_at,
            "sha256": hashlib.sha256(release_notes.content).hexdigest(),
            "size": len(release_notes.content),
        }
    return {
        "format_version": _MANIFEST_VERSION,
        "repository": {
            "url": record.repository_url,
            "id": record.repo_id,
            "company": record.company,
            "type": record.repo_type,
        },
        "ref": {
            "kind": record.ref.ref_kind,
            "name": record.ref.ref_name,
            "sha": record.ref.sha,
            "version": record.ref.version,
            "aliases": list(record.ref.aliases),
            "upstream_commit_time": record.ref.upstream_commit_time,
            "release_published_at": record.ref.release_published_at,
        },
        "capture_kind": record.capture_kind,
        "capture_revision": record.capture_revision,
        "collection_date": record.collection_date,
        "prior_snapshot": prior_snapshot,
        "files": [
            {
                "path": item.path,
                "sha256": item.sha256,
                "size": item.size,
                "purpose": item.purpose,
            }
            for item in record.files
        ],
        "excluded": [{"path": path, "reason": reason} for path, reason in excluded],
        "release_notes": release_metadata,
    }


def _write_manifest(staging_path: Path, metadata: dict) -> None:
    lines = [
        "# GitHub snapshot",
        "",
        _METADATA_MARKER,
        "```json",
        json.dumps(metadata, indent=2, sort_keys=True),
        "```",
        "",
        "## Snapshot",
        "| Field | Value |",
        "| --- | --- |",
    ]
    repository = metadata["repository"]
    ref = metadata["ref"]
    lines.extend(
        "| " + _markdown_cell(field) + " | " + _markdown_cell(value) + " |"
        for field, value in (
            ("Repository URL", repository["url"]),
            ("Repository ID", repository["id"]),
            ("Company", repository["company"]),
            ("Repository type", repository["type"]),
            ("Ref kind", ref["kind"]),
            ("Ref name", ref["name"]),
            ("Full SHA", ref["sha"]),
            ("Aliases", ", ".join(ref["aliases"]) if ref["aliases"] else "-"),
            ("Capture kind", metadata["capture_kind"]),
            ("Capture revision", metadata["capture_revision"]),
            ("Collection date", metadata["collection_date"]),
            ("Upstream commit date", ref["upstream_commit_time"]),
            ("Release published date", ref["release_published_at"] or "-"),
            ("Prior snapshot", metadata["prior_snapshot"] or "-"),
        )
    )
    lines.extend(["", "## Saved files", "| Path | SHA-256 | Bytes | Purpose |", "| --- | --- | ---: | --- |"])
    lines.extend(
        "| "
        + _markdown_cell(item["path"])
        + " | "
        + _markdown_cell(item["sha256"])
        + " | "
        + _markdown_cell(item["size"])
        + " | "
        + _markdown_cell(item["purpose"])
        + " |"
        for item in metadata["files"]
    )
    lines.extend(["", "## Excluded files", "| Path | Reason |", "| --- | --- |"])
    lines.extend(
        "| " + _markdown_cell(item["path"]) + " | " + _markdown_cell(item["reason"]) + " |"
        for item in metadata["excluded"]
    )
    lines.append("")
    (staging_path / "snapshot.md").write_text("\n".join(lines), encoding="utf-8")


def _markdown_cell(value: object) -> str:
    return str(value).replace("\\", "\\\\").replace("|", "\\|").replace("\n", "<br>")


def _read_metadata(manifest: str) -> Tuple[Optional[dict], Optional[str]]:
    if manifest.count(_METADATA_MARKER) != 1:
        return None, "snapshot metadata block is missing, duplicated, or malformed"
    expected_start = _METADATA_MARKER + "\n```json\n"
    start = manifest.find(expected_start)
    if start < 0:
        return None, "snapshot metadata block is missing, duplicated, or malformed"
    payload_start = start + len(expected_start)
    payload_end = manifest.find("\n```", payload_start)
    if payload_end < 0:
        return None, "snapshot metadata block is missing, duplicated, or malformed"
    try:
        metadata = json.loads(manifest[payload_start:payload_end], object_pairs_hook=_no_duplicate_keys)
    except (TypeError, ValueError, json.JSONDecodeError):
        return None, "snapshot metadata JSON is malformed"
    if not isinstance(metadata, dict):
        return None, "snapshot metadata JSON must be an object"
    return metadata, None


def _no_duplicate_keys(pairs: Sequence[Tuple[str, object]]) -> dict:
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError("duplicate JSON key " + key)
        value[key] = item
    return value


def _validate_top_level(staging_path: Path, metadata: dict, errors: List[str]) -> None:
    release_metadata = metadata.get("release_notes")
    allowed = {"snapshot.md", "files"}
    if release_metadata is not None:
        allowed.add("release-notes.md")
    for entry in sorted(staging_path.iterdir(), key=lambda item: item.name):
        if entry.name not in allowed:
            errors.append("unexpected top-level entry: " + entry.name)


def _validate_no_symlinks_or_diffs(staging_path: Path, errors: List[str]) -> None:
    for parent, directories, filenames in os.walk(str(staging_path), followlinks=False):
        for name in sorted(directories + filenames):
            path = Path(parent) / name
            relative = path.relative_to(staging_path).as_posix()
            if path.is_symlink():
                errors.append("symlink is not allowed in staged snapshot: " + relative)
            if path.suffix.lower() in (".patch", ".diff"):
                errors.append("generated " + path.suffix.lower() + " is not allowed in raw snapshot: " + relative)


def _validate_identity(metadata: dict, record: SnapshotRecord, errors: List[str]) -> None:
    expected = {
        "format_version": _MANIFEST_VERSION,
        "repository.url": record.repository_url,
        "repository.id": record.repo_id,
        "repository.company": record.company,
        "repository.type": record.repo_type,
        "ref.kind": record.ref.ref_kind,
        "ref.name": record.ref.ref_name,
        "ref.sha": record.ref.sha,
        "ref.version": record.ref.version,
        "ref.aliases": list(record.ref.aliases),
        "ref.upstream_commit_time": record.ref.upstream_commit_time,
        "ref.release_published_at": record.ref.release_published_at,
        "capture_kind": record.capture_kind,
        "capture_revision": record.capture_revision,
        "collection_date": record.collection_date,
    }
    required = (
        "repository.url",
        "repository.id",
        "repository.company",
        "repository.type",
        "ref.kind",
        "ref.name",
        "ref.sha",
        "ref.version",
        "ref.aliases",
        "ref.upstream_commit_time",
        "ref.release_published_at",
        "capture_kind",
        "capture_revision",
        "collection_date",
        "prior_snapshot",
        "files",
        "excluded",
        "release_notes",
    )
    for field in required:
        actual, found = _metadata_value(metadata, field)
        if not found:
            errors.append("missing required metadata: " + field)
    for field, value in expected.items():
        actual, found = _metadata_value(metadata, field)
        if found and actual != value:
            errors.append("metadata mismatch for " + field)
    for field in ("repository.url", "repository.company", "repository.type"):
        actual, found = _metadata_value(metadata, field)
        if found and (not isinstance(actual, str) or not actual):
            errors.append("metadata mismatch for " + field)


def _metadata_value(metadata: dict, field: str) -> Tuple[object, bool]:
    current: object = metadata
    for part in field.split("."):
        if not isinstance(current, dict) or part not in current:
            return None, False
        current = current[part]
    return current, True


def _validate_manifest_files(
    metadata: dict, record: SnapshotRecord, errors: List[str]
) -> Dict[str, SnapshotFile]:
    entries = metadata.get("files")
    manifest_files: Dict[str, SnapshotFile] = {}
    if not isinstance(entries, list):
        errors.append("saved files metadata is malformed")
        return manifest_files
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append("malformed saved file metadata")
            continue
        path = entry.get("path")
        sha256 = entry.get("sha256")
        size = entry.get("size")
        purpose = entry.get("purpose")
        if not isinstance(path, str) or not _is_safe_relative_path(path):
            errors.append("invalid saved file path")
            continue
        if path in manifest_files:
            errors.append("saved file listed more than once: " + path)
            continue
        if not isinstance(sha256, str) or not isinstance(size, int) or not isinstance(purpose, str):
            errors.append("malformed saved file metadata: " + path)
            continue
        manifest_files[path] = SnapshotFile(path, sha256, size, purpose)

    record_files = {item.path: item for item in record.files}
    if len(record_files) != len(record.files):
        errors.append("record lists a file more than once")
    for path, item in record_files.items():
        if manifest_files.get(path) != item:
            errors.append("manifest metadata mismatch: " + path)
    for path in manifest_files:
        if path not in record_files:
            errors.append("manifest lists unknown file: " + path)
    return manifest_files


def _validate_copied_files(
    files_root: Path, manifest_files: Dict[str, SnapshotFile], errors: List[str]
) -> None:
    actual_files: Dict[str, Path] = {}
    for parent, _, filenames in os.walk(str(files_root), followlinks=False):
        for name in sorted(filenames):
            path = Path(parent) / name
            if path.is_symlink():
                continue
            relative = path.relative_to(files_root).as_posix()
            actual_files[relative] = path
    for path, item in manifest_files.items():
        copied = actual_files.get(path)
        if copied is None:
            errors.append("listed file is missing: " + path)
            continue
        content = copied.read_bytes()
        if len(content) != item.size:
            errors.append("size mismatch: " + path)
        if hashlib.sha256(content).hexdigest() != item.sha256:
            errors.append("hash mismatch: " + path)
    for path in actual_files:
        if path not in manifest_files:
            errors.append("copied file is not listed: " + path)


def _validate_release_notes(
    staging_path: Path, metadata: dict, record: SnapshotRecord, errors: List[str]
) -> None:
    release_metadata = metadata.get("release_notes")
    release_path = staging_path / "release-notes.md"
    if release_metadata is None:
        if (
            record.release_notes_source_url is not None
            or record.release_notes_published_at is not None
        ):
            errors.append("metadata mismatch for release_notes")
        if release_path.exists() or release_path.is_symlink():
            errors.append("release notes are present without manifest metadata")
        return
    if not isinstance(release_metadata, dict):
        errors.append("release notes metadata is malformed")
        return
    required = ("path", "source_url", "published_at", "sha256", "size")
    if any(field not in release_metadata for field in required):
        errors.append("release notes metadata is incomplete")
        return
    if release_metadata.get("path") != "release-notes.md":
        errors.append("release notes metadata path is invalid")
    if not isinstance(release_metadata.get("source_url"), str) or not isinstance(
        release_metadata.get("published_at"), str
    ):
        errors.append("release notes source metadata is malformed")
    if release_metadata.get("source_url") != record.release_notes_source_url:
        errors.append("metadata mismatch for release_notes.source_url")
    if release_metadata.get("published_at") != record.release_notes_published_at:
        errors.append("metadata mismatch for release_notes.published_at")
    if not release_path.is_file() or release_path.is_symlink():
        errors.append("release-notes.md is missing")
        return
    content = release_path.read_bytes()
    if release_metadata.get("size") != len(content):
        errors.append("release notes size mismatch")
    if release_metadata.get("sha256") != hashlib.sha256(content).hexdigest():
        errors.append("release notes hash mismatch")


def _is_safe_relative_path(path: str) -> bool:
    candidate = Path(path)
    return bool(path) and not candidate.is_absolute() and ".." not in candidate.parts and candidate.as_posix() == path


def _existing_canonical(record: SnapshotRecord) -> Optional[Path]:
    if record.capture_kind != "canonical":
        return None
    snapshot_root = record.target_path.parent
    if not snapshot_root.is_dir():
        return None
    for manifest_path in sorted(snapshot_root.glob("*/snapshot.md")):
        try:
            metadata, error = _read_metadata(manifest_path.read_text(encoding="utf-8"))
        except UnicodeDecodeError:
            continue
        if error is not None or metadata is None:
            continue
        repository, repository_found = _metadata_value(metadata, "repository.id")
        sha, sha_found = _metadata_value(metadata, "ref.sha")
        capture_kind, kind_found = _metadata_value(metadata, "capture_kind")
        if (
            repository_found
            and sha_found
            and kind_found
            and repository == record.repo_id
            and sha == record.ref.sha
            and capture_kind == "canonical"
        ):
            return manifest_path.parent
    return None


def _allocate_supplement(record: SnapshotRecord) -> SnapshotRecord:
    snapshot_root = record.target_path.parent
    base = _SUPPLEMENT_SUFFIX.sub("", record.target_path.name)
    revision = 1
    while (snapshot_root / (base + "-r" + str(revision))).exists():
        revision += 1
    updated = replace(
        record,
        capture_revision=revision,
        target_path=snapshot_root / (base + "-r" + str(revision)),
    )
    manifest_path = updated.staging_path / "snapshot.md"
    try:
        metadata, error = _read_metadata(manifest_path.read_text(encoding="utf-8"))
    except UnicodeDecodeError:
        return updated
    if metadata is not None and error is None:
        metadata["capture_kind"] = "supplement"
        metadata["capture_revision"] = revision
        _write_manifest(updated.staging_path, metadata)
    return updated


def _require_contained(path: Path, root: Path, label: str) -> None:
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError as error:
        raise SnapshotError(label + " escapes its root") from error


def _copy_checkout_file(
    repo_root: Path,
    relative: str,
    destination: Path,
    max_file_bytes: int,
    remaining_total_bytes: int,
) -> Tuple[str, int, bool]:
    """Copy one regular checkout file through no-follow descriptors only."""
    source_descriptor = _open_checkout_regular_file(repo_root, relative)
    destination_descriptor = None
    digest = hashlib.sha256()
    copied = 0
    preview = b""
    try:
        destination_descriptor = os.open(
            str(destination),
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | _no_follow_flag(),
            0o600,
        )
        while True:
            chunk = os.read(source_descriptor, 64 * 1024)
            if not chunk:
                break
            copied += len(chunk)
            if copied > max_file_bytes:
                raise SnapshotError("copied file exceeds per-file byte limit: " + relative)
            if copied > remaining_total_bytes:
                raise SnapshotError("copied files exceed total snapshot byte limit: " + relative)
            if len(preview) < 8192:
                preview += chunk[: 8192 - len(preview)]
            _write_all(destination_descriptor, chunk)
            digest.update(chunk)
        source_stat = os.fstat(source_descriptor)
        if not stat.S_ISREG(source_stat.st_mode):
            raise SnapshotError("selected file is not a regular file: " + relative)
        return digest.hexdigest(), copied, b"\0" in preview
    finally:
        if destination_descriptor is not None:
            os.close(destination_descriptor)
        os.close(source_descriptor)


def _open_checkout_regular_file(repo_root: Path, relative: str) -> int:
    if not _is_safe_relative_path(relative):
        raise SnapshotError("selected file is not a safe checkout path")
    if os.open not in os.supports_dir_fd:
        raise SnapshotError("descriptor-relative checkout traversal is unavailable")
    directory_flag = getattr(os, "O_DIRECTORY", None)
    if directory_flag is None:
        raise SnapshotError("no-follow directory traversal is unavailable")

    root_descriptor = os.open(str(repo_root), os.O_RDONLY | directory_flag | _no_follow_flag())
    current_descriptor = root_descriptor
    try:
        root_stat = os.fstat(root_descriptor)
        if not stat.S_ISDIR(root_stat.st_mode):
            raise SnapshotError("checkout root is not a directory")
        parts = Path(relative).parts
        for index, part in enumerate(parts):
            flags = os.O_RDONLY | _no_follow_flag()
            if index < len(parts) - 1:
                flags |= directory_flag
            next_descriptor = os.open(part, flags, dir_fd=current_descriptor)
            os.close(current_descriptor)
            current_descriptor = next_descriptor
        source_stat = os.fstat(current_descriptor)
        if not stat.S_ISREG(source_stat.st_mode):
            raise SnapshotError("selected file is not a regular file: " + relative)
        return current_descriptor
    except OSError as error:
        os.close(current_descriptor)
        raise SnapshotError("no-follow checkout traversal rejected selected file: " + relative) from error
    except Exception:
        os.close(current_descriptor)
        raise


def _no_follow_flag() -> int:
    flag = getattr(os, "O_NOFOLLOW", None)
    if flag is None:
        raise SnapshotError("no-follow file opening is unavailable")
    return flag


def _write_all(descriptor: int, content: bytes) -> None:
    offset = 0
    while offset < len(content):
        written = os.write(descriptor, content[offset:])
        if written <= 0:
            raise OSError("could not write snapshot file")
        offset += written


def _staging_stat(staging_path: Path) -> os.stat_result:
    try:
        staging_stat = os.lstat(str(staging_path))
    except OSError as error:
        raise SnapshotError("staged directory is missing") from error
    if not stat.S_ISDIR(staging_stat.st_mode) or stat.S_ISLNK(staging_stat.st_mode):
        raise SnapshotError("staged directory is not a real directory")
    return staging_stat


def _staging_identity_error(record: SnapshotRecord) -> Optional[str]:
    if record.staging_device is None or record.staging_inode is None:
        return "staged directory identity is unavailable"
    try:
        directory_flag = getattr(os, "O_DIRECTORY", None)
        if directory_flag is None:
            return "no-follow staged directory validation is unavailable"
        descriptor = os.open(
            str(record.staging_path), os.O_RDONLY | directory_flag | _no_follow_flag()
        )
    except (OSError, SnapshotError):
        return "staged directory is missing or no longer original"
    try:
        staging_stat = os.fstat(descriptor)
        if (
            not stat.S_ISDIR(staging_stat.st_mode)
            or (staging_stat.st_dev, staging_stat.st_ino)
            != (record.staging_device, record.staging_inode)
        ):
            return "staged directory is a symlink or no longer original"
        return None
    finally:
        os.close(descriptor)


def _path_exists_or_is_symlink(path: Path) -> bool:
    return path.exists() or path.is_symlink()


def _remove_owned_lock(lock_path: Path, identity: Tuple[int, int]) -> None:
    try:
        lock_stat = os.lstat(str(lock_path))
    except FileNotFoundError:
        return
    if (lock_stat.st_dev, lock_stat.st_ino) != identity:
        return
    try:
        os.unlink(str(lock_path))
    except FileNotFoundError:
        pass


def _clean_staging(record: SnapshotRecord) -> None:
    if record.staging_device is None or record.staging_inode is None:
        return
    _clean_staging_path(record.staging_path, (record.staging_device, record.staging_inode))


def _clean_staging_path(staging_path: Path, expected: object) -> None:
    try:
        staging_stat = os.lstat(str(staging_path))
    except FileNotFoundError:
        return
    if hasattr(expected, "st_dev") and hasattr(expected, "st_ino"):
        expected_identity = (expected.st_dev, expected.st_ino)
    else:
        expected_identity = expected
    if (
        not stat.S_ISDIR(staging_stat.st_mode)
        or stat.S_ISLNK(staging_stat.st_mode)
        or (staging_stat.st_dev, staging_stat.st_ino) != expected_identity
    ):
        return
    shutil.rmtree(str(staging_path), ignore_errors=True)
