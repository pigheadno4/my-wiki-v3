"""Immutable evidence storage for the focused GitHub collection pilot."""

from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from typing import Dict, List, Optional, Sequence, Tuple

from github_canonical import canonical_json_bytes, safe_policy_path
from github_capsule_selection import (
    CapsuleFile,
    CapsuleResolution,
    scan_evidence_files,
)
from github_git_tree import GitTree
from github_registry import RepoConfig
from github_releases import ReleaseCandidate, ReleaseNotesEvidence


_DATE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
_OBJECT_ID = re.compile(r"^(?:[0-9a-f]{40}|[0-9a-f]{64})$")
_ROOT_CONTEXT = ("LICENSE", "LICENSE.md", "README.md", "package-lock.json", "package.json")


class PilotStoreError(ValueError):
    """A focused pilot artifact is invalid or cannot be published safely."""


@dataclass(frozen=True)
class SourceSnapshot:
    repo_id: str
    sha: str
    collected_date: str
    directory: Path
    manifest_path: Path
    files: Tuple[str, ...]


@dataclass(frozen=True)
class PackageReleaseRecord:
    release_id: str
    package: str
    version: str
    tag: str
    sha: str
    release_date: str
    collected_date: str
    directory: Path
    manifest_path: Path
    notes_path: Path
    notes_sha256: str


@dataclass(frozen=True)
class ComparisonRecord:
    package: str
    from_version: str
    to_version: str
    from_sha: str
    to_sha: str
    changed_paths: Tuple[str, ...]
    patch_path: Path
    metadata_path: Path
    markdown_path: Path


def package_slug(package: str) -> str:
    """Return the unscoped package path component."""
    if not isinstance(package, str) or not package:
        raise PilotStoreError("package name is required")
    value = package.lower().rsplit("/", 1)[-1]
    if not re.fullmatch(r"[a-z0-9][a-z0-9._~-]*", value):
        raise PilotStoreError("package name cannot form a safe path")
    return value


def publish_source_snapshot(
    root: Path,
    config: RepoConfig,
    tree: GitTree,
    resolution: CapsuleResolution,
    collected_date: str,
    triggering_refs: Sequence[str],
) -> SourceSnapshot:
    """Publish or reuse one immutable source snapshot for an exact SHA."""
    root = Path(root).resolve()
    _require_date(collected_date)
    if not isinstance(tree, GitTree):
        raise TypeError("tree must be a GitTree")
    if not isinstance(resolution, CapsuleResolution):
        raise TypeError("resolution must be a CapsuleResolution")
    sha = tree.sha
    if not _OBJECT_ID.fullmatch(sha):
        raise PilotStoreError("snapshot SHA is invalid")
    repository_root = _raw_repository_root(root, config)
    snapshot_root = repository_root / "snapshots"
    existing = _find_snapshot(snapshot_root, config.id, sha)
    if existing is not None:
        return existing

    files = _snapshot_files(tree, resolution, config)
    total = sum(item.size for item in files)
    if total > config.max_snapshot_bytes:
        raise PilotStoreError("snapshot exceeds max_snapshot_bytes")
    manifest = {
        "collected_date": collected_date,
        "excluded": [
            {"path": path, "reason": reason}
            for path, reason in resolution.excluded
        ],
        "files": [_file_manifest(item) for item in files],
        "format_version": 1,
        "repository": config.id,
        "sha": sha,
        "triggering_refs": sorted(set(triggering_refs)),
    }
    destination = snapshot_root / (collected_date + "-" + sha[:7])
    staging = _new_staging(repository_root)
    try:
        for item in files:
            target = staging / "files" / item.path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(item.content)
        _write_json(staging / "manifest.json", manifest)
        snapshot_root.mkdir(parents=True, exist_ok=True)
        try:
            os.replace(str(staging), str(destination))
        except FileExistsError:
            winner = _find_snapshot(snapshot_root, config.id, sha)
            if winner is None:
                raise PilotStoreError("snapshot destination collision")
            return winner
    except Exception:
        _clean_owned(staging)
        raise
    return SourceSnapshot(
        config.id,
        sha,
        collected_date,
        destination,
        destination / "manifest.json",
        tuple(item.path for item in files),
    )


def publish_release_record(
    root: Path,
    config: RepoConfig,
    candidate: ReleaseCandidate,
    release_date: str,
    evidence: Optional[ReleaseNotesEvidence],
    collected_date: str,
) -> PackageReleaseRecord:
    """Publish or reuse one immutable package release record."""
    root = Path(root).resolve()
    _require_date(collected_date)
    if not isinstance(candidate, ReleaseCandidate):
        raise TypeError("candidate must be a ReleaseCandidate")
    if not release_date:
        raise PilotStoreError("release date is required")
    if not _OBJECT_ID.fullmatch(candidate.commit_sha):
        raise PilotStoreError("release SHA is invalid")
    slug = package_slug(candidate.package)
    if not safe_policy_path(candidate.version):
        raise PilotStoreError("release version is not path safe")
    notes = evidence.content if evidence is not None else b""
    if not isinstance(notes, bytes):
        raise TypeError("release notes must be bytes")
    notes_sha256 = hashlib.sha256(notes).hexdigest()
    release_id = candidate.package + "@" + candidate.version
    release_root = (
        _raw_repository_root(root, config)
        / "releases"
        / slug
        / candidate.version
    )
    existing = _find_release_record(
        release_root,
        config.id,
        candidate,
        notes_sha256,
    )
    if existing is not None:
        return existing

    destination = _next_revision_path(release_root, collected_date)
    manifest = {
        "collected_date": collected_date,
        "format_version": 1,
        "notes_available": evidence is not None,
        "notes_sha256": notes_sha256,
        "package": candidate.package,
        "release_date": release_date,
        "repository": config.id,
        "sha": candidate.commit_sha,
        "source_url": evidence.source_url if evidence is not None else "",
        "tag": candidate.tag,
        "version": candidate.version,
    }
    staging = _new_staging(_raw_repository_root(root, config))
    try:
        (staging / "release-notes.md").write_bytes(notes)
        _write_json(staging / "manifest.json", manifest)
        release_root.mkdir(parents=True, exist_ok=True)
        os.replace(str(staging), str(destination))
    except Exception:
        _clean_owned(staging)
        raise
    return _release_from_manifest(destination, manifest)


def write_package_comparison(
    root: Path,
    config: RepoConfig,
    repo_root: Path,
    package: str,
    from_version: str,
    from_sha: str,
    from_paths: Sequence[str],
    to_version: str,
    to_sha: str,
    to_paths: Sequence[str],
) -> ComparisonRecord:
    """Write one generated comparison scoped to a package's repository paths."""
    if not _OBJECT_ID.fullmatch(from_sha) or not _OBJECT_ID.fullmatch(to_sha):
        raise PilotStoreError("comparison SHA is invalid")
    pathspecs = tuple(sorted(set(from_paths) | set(to_paths)))
    if not pathspecs or any(not safe_policy_path(path) for path in pathspecs):
        raise PilotStoreError("comparison paths are invalid")
    changed = _run_git(
        repo_root,
        ("diff", "--name-only", from_sha, to_sha, "--") + pathspecs,
    )
    patch = _run_git_bytes(
        repo_root,
        ("diff", "--no-ext-diff", "--unified=3", from_sha, to_sha, "--")
        + pathspecs,
    )
    changed_paths = tuple(sorted(line for line in changed.splitlines() if line))
    comparison_root = (
        Path(root).resolve()
        / "tracking"
        / "github"
        / "repos"
        / config.company
        / config.id.split("/", 1)[1]
        / "comparisons"
        / package_slug(package)
        / (_version_slug(from_version) + "--" + _version_slug(to_version))
    )
    metadata = {
        "changed_paths": list(changed_paths),
        "format_version": 1,
        "from_sha": from_sha,
        "from_version": from_version,
        "package": package,
        "pathspecs": list(pathspecs),
        "repository": config.id,
        "to_sha": to_sha,
        "to_version": to_version,
    }
    markdown = _comparison_markdown(metadata)
    comparison_root.mkdir(parents=True, exist_ok=True)
    _write_bytes_atomic(comparison_root / "diff.patch", patch)
    _write_bytes_atomic(
        comparison_root / "comparison.json", canonical_json_bytes(metadata) + b"\n"
    )
    _write_bytes_atomic(comparison_root / "comparison.md", markdown.encode("utf-8"))
    return ComparisonRecord(
        package,
        from_version,
        to_version,
        from_sha,
        to_sha,
        changed_paths,
        comparison_root / "diff.patch",
        comparison_root / "comparison.json",
        comparison_root / "comparison.md",
    )


def _snapshot_files(
    tree: GitTree,
    resolution: CapsuleResolution,
    config: RepoConfig,
) -> Tuple[CapsuleFile, ...]:
    selected: Dict[str, CapsuleFile] = {item.path: item for item in resolution.files}
    blobs = {item.path: item for item in tree.blobs()}
    context: List[CapsuleFile] = []
    for path in _ROOT_CONTEXT:
        if path in selected or path not in blobs:
            continue
        blob = blobs[path]
        if blob.size is None or blob.size > config.max_file_bytes:
            raise PilotStoreError("repository context file exceeds max_file_bytes")
        content = tree.read_blob(path, max_bytes=config.max_file_bytes)
        item = CapsuleFile(
            path=path,
            content=content,
            sha256=hashlib.sha256(content).hexdigest(),
            size=len(content),
            purpose="repository-context",
            git_blob_oid=blob.oid,
            git_mode=blob.mode,
            package="",
            classification_reason="repository-context",
        )
        context.append(item)
    scan_evidence_files(context, config.secret_allowlist)
    for item in context:
        selected[item.path] = item
    for item in selected.values():
        if item.size != len(item.content):
            raise PilotStoreError("selected file size mismatch")
        if item.sha256 != hashlib.sha256(item.content).hexdigest():
            raise PilotStoreError("selected file hash mismatch")
    return tuple(selected[path] for path in sorted(selected))


def _find_snapshot(
    snapshot_root: Path,
    repo_id: str,
    sha: str,
) -> Optional[SourceSnapshot]:
    if not snapshot_root.is_dir():
        return None
    matches = []
    for directory in sorted(snapshot_root.iterdir()):
        if not directory.is_dir() or directory.is_symlink():
            continue
        manifest_path = directory / "manifest.json"
        if not manifest_path.is_file():
            continue
        manifest = _read_json(manifest_path)
        if manifest.get("sha") == sha:
            if manifest.get("repository") != repo_id:
                raise PilotStoreError("snapshot repository identity mismatch")
            files = manifest.get("files")
            if not isinstance(files, list):
                raise PilotStoreError("snapshot files are invalid")
            matches.append(
                SourceSnapshot(
                    repo_id,
                    sha,
                    str(manifest.get("collected_date", "")),
                    directory,
                    manifest_path,
                    tuple(str(item["path"]) for item in files),
                )
            )
    if len(matches) > 1:
        raise PilotStoreError("more than one source snapshot exists for SHA")
    return matches[0] if matches else None


def _find_release_record(
    release_root: Path,
    repo_id: str,
    candidate: ReleaseCandidate,
    notes_sha256: str,
) -> Optional[PackageReleaseRecord]:
    if not release_root.is_dir():
        return None
    for directory in sorted(release_root.iterdir()):
        manifest_path = directory / "manifest.json"
        if not directory.is_dir() or not manifest_path.is_file():
            continue
        manifest = _read_json(manifest_path)
        identity = (
            manifest.get("repository"),
            manifest.get("package"),
            manifest.get("version"),
            manifest.get("tag"),
            manifest.get("sha"),
            manifest.get("notes_sha256"),
        )
        expected = (
            repo_id,
            candidate.package,
            candidate.version,
            candidate.tag,
            candidate.commit_sha,
            notes_sha256,
        )
        if identity == expected:
            return _release_from_manifest(directory, manifest)
    return None


def _release_from_manifest(directory: Path, manifest: dict) -> PackageReleaseRecord:
    package = str(manifest["package"])
    version = str(manifest["version"])
    return PackageReleaseRecord(
        package + "@" + version,
        package,
        version,
        str(manifest["tag"]),
        str(manifest["sha"]),
        str(manifest["release_date"]),
        str(manifest["collected_date"]),
        directory,
        directory / "manifest.json",
        directory / "release-notes.md",
        str(manifest["notes_sha256"]),
    )


def _raw_repository_root(root: Path, config: RepoConfig) -> Path:
    name = config.id.split("/", 1)[1]
    return root / "raw" / "github" / config.company / name


def _new_staging(repository_root: Path) -> Path:
    staging_root = repository_root / ".staging"
    staging_root.mkdir(parents=True, exist_ok=True)
    return Path(tempfile.mkdtemp(prefix="pilot-", dir=str(staging_root)))


def _next_revision_path(root: Path, collected_date: str) -> Path:
    candidate = root / collected_date
    revision = 1
    while candidate.exists() or candidate.is_symlink():
        revision += 1
        candidate = root / (collected_date + "-r" + str(revision))
    return candidate


def _file_manifest(item: CapsuleFile) -> dict:
    return {
        "classification_reason": item.classification_reason,
        "git_blob_oid": item.git_blob_oid,
        "git_mode": item.git_mode,
        "package": item.package,
        "path": item.path,
        "purpose": item.purpose,
        "sha256": item.sha256,
        "size": item.size,
    }


def _comparison_markdown(metadata: dict) -> str:
    lines = [
        "# GitHub package comparison",
        "",
        "- Repository: `" + str(metadata["repository"]) + "`",
        "- Package: `" + str(metadata["package"]) + "`",
        "- From: `" + str(metadata["from_version"]) + "` (`" + str(metadata["from_sha"]) + "`)",
        "- To: `" + str(metadata["to_version"]) + "` (`" + str(metadata["to_sha"]) + "`)",
        "- Patch: [diff.patch](diff.patch)",
        "",
        "## Changed paths",
        "",
    ]
    changed = metadata["changed_paths"]
    lines.extend("- `" + str(path) + "`" for path in changed)
    if not changed:
        lines.append("- None")
    return "\n".join(lines) + "\n"


def _run_git(repo_root: Path, args: Sequence[str]) -> str:
    return _run_git_bytes(repo_root, args).decode("utf-8")


def _run_git_bytes(repo_root: Path, args: Sequence[str]) -> bytes:
    try:
        return subprocess.run(
            ["git"] + list(args),
            cwd=str(repo_root),
            check=True,
            capture_output=True,
        ).stdout
    except (OSError, subprocess.SubprocessError):
        raise PilotStoreError("Git comparison command failed") from None


def _write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(canonical_json_bytes(value) + b"\n")


def _write_bytes_atomic(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=".tmp-", dir=str(path.parent))
    try:
        with os.fdopen(descriptor, "wb") as output:
            output.write(content)
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary, str(path))
    except Exception:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def _read_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        raise PilotStoreError("artifact manifest is unreadable") from None
    if not isinstance(value, dict):
        raise PilotStoreError("artifact manifest must be an object")
    return value


def _require_date(value: str) -> None:
    if not isinstance(value, str) or not _DATE.fullmatch(value):
        raise PilotStoreError("collected date must use YYYY-MM-DD")


def _version_slug(value: str) -> str:
    if not isinstance(value, str) or not safe_policy_path(value):
        raise PilotStoreError("version is not path safe")
    return value


def _clean_owned(path: Path) -> None:
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path)


__all__ = [
    "ComparisonRecord",
    "PackageReleaseRecord",
    "PilotStoreError",
    "SourceSnapshot",
    "package_slug",
    "publish_release_record",
    "publish_source_snapshot",
    "write_package_comparison",
]
