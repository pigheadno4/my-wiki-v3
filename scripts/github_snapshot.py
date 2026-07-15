"""Immutable, curated raw snapshots for checked-out GitHub repositories."""

from dataclasses import dataclass
import fnmatch
import hashlib
from pathlib import Path
import re
import shutil
import tempfile
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

from github_git import ResolvedRef
from github_registry import RepoConfig


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


def select_key_files(
    config: RepoConfig, repo_root: Path, changed_paths: Sequence[str] = ()
) -> SelectionResult:
    """Select readable evidence files in a deterministic, bounded order."""
    repo_root = repo_root.resolve()
    candidates, missing = _candidate_groups(config, repo_root, changed_paths)
    selected: List[Path] = []
    excluded: Dict[str, str] = dict(missing)
    total_bytes = 0

    for paths in candidates:
        for path in paths:
            relative = path.relative_to(repo_root).as_posix()
            if relative in {item.relative_to(repo_root).as_posix() for item in selected}:
                continue
            reason = _exclusion_reason(config, path, relative)
            if reason is not None:
                excluded[relative] = reason
                continue
            size = path.stat().st_size
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
) -> SnapshotRecord:
    """Stage an immutable snapshot below ``raw/github/.staging``."""
    if ref.repo_id != config.id:
        raise SnapshotError("resolved reference repository does not match configuration")
    if capture_kind not in ("canonical", "supplement"):
        raise SnapshotError("capture_kind must be canonical or supplement")

    raw_root = raw_root.resolve()
    staging_root = staging_root.resolve()
    required_staging_root = raw_root / ".staging"
    try:
        staging_root.relative_to(required_staging_root)
    except ValueError as error:
        raise SnapshotError("staging must live under raw/github/.staging") from error

    repo_root = repo_root.resolve()
    selection = select_key_files(config, repo_root)
    revision, target_path = _target_path(config, ref, raw_root, collection_date, capture_kind)
    staging_root.mkdir(parents=True, exist_ok=True)
    staging_path = Path(tempfile.mkdtemp(prefix="snapshot-", dir=str(staging_root)))
    files_root = staging_path / "files"
    snapshot_files: List[SnapshotFile] = []

    try:
        for source in selection.selected:
            relative = source.relative_to(repo_root).as_posix()
            destination = files_root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(str(source), str(destination))
            content = destination.read_bytes()
            snapshot_files.append(
                SnapshotFile(
                    path=relative,
                    sha256=hashlib.sha256(content).hexdigest(),
                    size=len(content),
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
        )
        (staging_path / "snapshot.md").write_text(
            _render_manifest(config, record, prior_snapshot, selection.excluded), encoding="utf-8"
        )
        return record
    except Exception:
        shutil.rmtree(str(staging_path), ignore_errors=True)
        raise


def validate_staged_snapshot(record: SnapshotRecord) -> List[str]:
    """Return deterministic integrity failures for a staged snapshot."""
    errors: List[str] = []
    manifest_path = record.staging_path / "snapshot.md"
    files_root = record.staging_path / "files"
    if not manifest_path.is_file():
        return ["snapshot.md is missing"]
    if not files_root.is_dir():
        return ["files directory is missing"]

    try:
        manifest = manifest_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return ["snapshot.md is not UTF-8"]

    metadata = _read_table(manifest, "Snapshot", ("Field", "Value"))
    saved = _read_table(manifest, "Saved files", ("Path", "SHA-256", "Bytes", "Purpose"))
    excluded = _read_table(manifest, "Excluded files", ("Path", "Reason"))
    if metadata is None:
        errors.append("snapshot metadata table is missing or malformed")
        metadata = []
    if saved is None:
        errors.append("saved file table is missing or malformed")
        saved = []
    if excluded is None:
        errors.append("excluded file table is missing or malformed")

    expected_metadata = {
        "Repository ID": record.repo_id,
        "Ref kind": record.ref.ref_kind,
        "Ref name": record.ref.ref_name,
        "Full SHA": record.ref.sha,
        "Capture kind": record.capture_kind,
        "Capture revision": str(record.capture_revision),
        "Collection date": record.collection_date,
    }
    metadata_values = {row[0]: row[1] for row in metadata if len(row) == 2}
    required_metadata = (
        "Repository URL",
        "Repository ID",
        "Company",
        "Repository type",
        "Ref kind",
        "Ref name",
        "Full SHA",
        "Aliases",
        "Capture kind",
        "Capture revision",
        "Collection date",
        "Upstream commit date",
        "Release published date",
        "Prior snapshot",
    )
    for field in required_metadata:
        if field not in metadata_values:
            errors.append("missing required metadata: " + field)
    for field, value in expected_metadata.items():
        if metadata_values.get(field) != value:
            errors.append("metadata mismatch for " + field)

    manifest_files: Dict[str, Tuple[str, int, str]] = {}
    for row in saved:
        if len(row) != 4:
            errors.append("malformed saved file row")
            continue
        path, sha256, size_text, purpose = row
        if path in manifest_files:
            errors.append("saved file listed more than once: " + path)
            continue
        try:
            size = int(size_text)
        except ValueError:
            errors.append("invalid saved file size: " + path)
            continue
        manifest_files[path] = (sha256, size, purpose)

    record_files = {item.path: item for item in record.files}
    for path, item in record_files.items():
        if manifest_files.get(path) != (item.sha256, item.size, item.purpose):
            errors.append("manifest metadata mismatch: " + path)
    for path in manifest_files:
        if path not in record_files:
            errors.append("manifest lists unknown file: " + path)

    actual_files = {}
    for path in sorted(item for item in files_root.rglob("*") if item.is_file()):
        relative = path.relative_to(files_root).as_posix()
        actual_files[relative] = path
        if path.suffix == ".patch":
            errors.append("generated patch is not allowed in raw snapshot: " + relative)
    for path, item in record_files.items():
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
        if path not in record_files:
            errors.append("copied file is not listed: " + path)
    return errors


def promote_snapshot(record: SnapshotRecord) -> Path:
    """Validate and atomically promote a staged snapshot without overwriting raw evidence."""
    errors = validate_staged_snapshot(record)
    if errors:
        raise SnapshotError("invalid staged snapshot:\n- " + "\n- ".join(errors))

    existing = _existing_canonical(record)
    if existing is not None:
        shutil.rmtree(str(record.staging_path), ignore_errors=True)
        return existing
    if record.target_path.exists():
        raise SnapshotError("snapshot target already exists: " + str(record.target_path))

    record.target_path.parent.mkdir(parents=True, exist_ok=True)
    if record.staging_path.parent.stat().st_dev != record.target_path.parent.stat().st_dev:
        raise SnapshotError("staging and target must share a filesystem")
    record.staging_path.replace(record.target_path)
    return record.target_path


def _candidate_groups(
    config: RepoConfig, repo_root: Path, changed_paths: Sequence[str]
) -> Tuple[Tuple[Tuple[Path, ...], ...], Tuple[Tuple[str, str], ...]]:
    missing: List[Tuple[str, str]] = []
    explicit = []
    for key_path in sorted(set(config.key_paths)):
        path = repo_root / key_path
        if not path.exists():
            missing.append((key_path, "configured key path is missing"))
            continue
        explicit.extend(_expand_path(path))

    all_files = tuple(sorted((path for path in repo_root.rglob("*") if path.is_file()), key=lambda item: item.as_posix()))
    defaults = [path for path in all_files if _is_default_path(path.relative_to(repo_root))]
    changed = []
    for changed_path in sorted(set(changed_paths)):
        path = repo_root / changed_path
        if path.is_file() and _is_changed_public_path(path.relative_to(repo_root)):
            changed.append(path)
    return (
        tuple(sorted(set(explicit), key=lambda item: item.relative_to(repo_root).as_posix())),
        tuple(sorted(set(defaults), key=lambda item: item.relative_to(repo_root).as_posix())),
        tuple(sorted(set(changed), key=lambda item: item.relative_to(repo_root).as_posix())),
    ), tuple(missing)


def _expand_path(path: Path) -> Iterable[Path]:
    if path.is_file():
        return (path,)
    return tuple(item for item in path.rglob("*") if item.is_file())


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
    with path.open("rb") as source:
        return b"\0" in source.read(8192)


def _purpose_for_path(config: RepoConfig, repo_root: Path, path: Path) -> str:
    relative = path.relative_to(repo_root).as_posix()
    if any(relative == key.strip("/") or relative.startswith(key.strip("/") + "/") for key in config.key_paths):
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


def _render_manifest(
    config: RepoConfig,
    record: SnapshotRecord,
    prior_snapshot: Optional[str],
    excluded: Sequence[Tuple[str, str]],
) -> str:
    aliases = ", ".join(record.ref.aliases) if record.ref.aliases else "-"
    release_date = record.ref.release_published_at or "-"
    prior = prior_snapshot or "-"
    lines = [
        "# GitHub snapshot",
        "",
        "## Snapshot",
        "| Field | Value |",
        "| --- | --- |",
        "| Repository URL | " + config.url + " |",
        "| Repository ID | " + record.repo_id + " |",
        "| Company | " + config.company + " |",
        "| Repository type | " + config.repo_type + " |",
        "| Ref kind | " + record.ref.ref_kind + " |",
        "| Ref name | " + record.ref.ref_name + " |",
        "| Full SHA | " + record.ref.sha + " |",
        "| Aliases | " + aliases + " |",
        "| Capture kind | " + record.capture_kind + " |",
        "| Capture revision | " + str(record.capture_revision) + " |",
        "| Collection date | " + record.collection_date + " |",
        "| Upstream commit date | " + record.ref.upstream_commit_time + " |",
        "| Release published date | " + release_date + " |",
        "| Prior snapshot | " + prior + " |",
        "",
        "## Saved files",
        "| Path | SHA-256 | Bytes | Purpose |",
        "| --- | --- | ---: | --- |",
    ]
    lines.extend(
        "| " + item.path + " | " + item.sha256 + " | " + str(item.size) + " | " + item.purpose + " |"
        for item in record.files
    )
    lines.extend(["", "## Excluded files", "| Path | Reason |", "| --- | --- |"])
    lines.extend("| " + path + " | " + reason + " |" for path, reason in excluded)
    lines.append("")
    return "\n".join(lines)


def _read_table(
    manifest: str, heading: str, headers: Tuple[str, ...]
) -> Optional[List[Tuple[str, ...]]]:
    lines = manifest.splitlines()
    try:
        start = lines.index("## " + heading)
    except ValueError:
        return None
    if start + 2 >= len(lines):
        return None
    header = _table_cells(lines[start + 1])
    separator = _table_cells(lines[start + 2])
    if tuple(header) != headers or len(separator) != len(headers):
        return None
    rows = []
    for line in lines[start + 3 :]:
        if not line.strip() or line.startswith("## "):
            break
        cells = _table_cells(line)
        if len(cells) != len(headers):
            return None
        rows.append(tuple(cells))
    return rows


def _table_cells(line: str) -> List[str]:
    if not line.startswith("|") or not line.endswith("|"):
        return []
    return [cell.strip() for cell in line[1:-1].split("|")]


def _existing_canonical(record: SnapshotRecord) -> Optional[Path]:
    if record.capture_kind != "canonical":
        return None
    snapshot_root = record.target_path.parent
    if not snapshot_root.is_dir():
        return None
    for manifest_path in sorted(snapshot_root.glob("*/snapshot.md")):
        try:
            manifest = manifest_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        metadata = _read_table(manifest, "Snapshot", ("Field", "Value"))
        values = {row[0]: row[1] for row in metadata or [] if len(row) == 2}
        if (
            values.get("Repository ID") == record.repo_id
            and values.get("Full SHA") == record.ref.sha
            and values.get("Capture kind") == "canonical"
        ):
            return manifest_path.parent
    return None
