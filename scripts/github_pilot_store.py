"""Immutable evidence storage for the focused GitHub collection pilot."""

from dataclasses import dataclass
from contextlib import contextmanager
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import threading
from typing import Dict, List, Optional, Sequence, Tuple

from github_canonical import canonical_json_bytes, safe_policy_path
from github_capsule_policy import (
    COMMIT_TREE_ADAPTER,
    TAGGED_TREE_ADAPTER,
    CapsuleConfig,
)
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
_ROOT_CONTEXT = ("LICENSE", "LICENSE.md", "README.md", "package.json")
_ARTIFACT_THREAD_LOCK = threading.RLock()


class PilotStoreError(ValueError):
    """A focused pilot artifact is invalid or cannot be published safely."""


def _ref_evidence_owner(capsule: CapsuleConfig) -> str:
    if capsule.adapter == COMMIT_TREE_ADAPTER:
        return capsule.source_id
    if capsule.adapter == TAGGED_TREE_ADAPTER and len(capsule.focus_packages) == 1:
        return capsule.focus_packages[0]
    raise PilotStoreError(
        "ref comparison requires commit-tree-v1 or tagged-tree-v1"
    )


@dataclass(frozen=True)
class SourceSnapshot:
    repo_id: str
    sha: str
    collected_date: str
    directory: Path
    manifest_path: Path
    files: Tuple[str, ...]


@dataclass(frozen=True)
class SourceSupplement:
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
    upstream_changes: Tuple["UpstreamChange", ...]
    patch_path: Path
    metadata_path: Path
    markdown_path: Path
    ref_kind: str = ""
    ref_name: str = ""


@dataclass(frozen=True)
class UpstreamChange:
    status: str
    old_path: str
    new_path: str


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
    with _artifact_lock(root):
        return _publish_source_snapshot_unlocked(
            root,
            config,
            tree,
            resolution,
            collected_date,
            triggering_refs,
        )


def _publish_source_snapshot_unlocked(
    root: Path,
    config: RepoConfig,
    tree: GitTree,
    resolution: CapsuleResolution,
    collected_date: str,
    triggering_refs: Sequence[str],
) -> SourceSnapshot:
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
    capsule = resolution.effective_policy.capsule
    if len(files) > capsule.max_capsule_files:
        raise PilotStoreError(
            "needs-policy-review:capsule-budget-exceeded: published file count "
            + str(len(files))
            + " exceeds max_capsule_files "
            + str(capsule.max_capsule_files)
        )
    if total > capsule.max_capsule_utf8_bytes:
        raise PilotStoreError(
            "needs-policy-review:capsule-budget-exceeded: published UTF-8 bytes "
            + str(total)
            + " exceeds max_capsule_utf8_bytes "
            + str(capsule.max_capsule_utf8_bytes)
        )
    if total > config.max_snapshot_bytes:
        raise PilotStoreError("snapshot exceeds max_snapshot_bytes")
    author_date, commit_date = tree.commit_dates()
    manifest = {
        "author_date": author_date,
        "collected_date": collected_date,
        "commit_date": commit_date,
        "excluded": [
            {"path": path, "reason": reason}
            for path, reason in resolution.excluded
        ],
        "files": [_file_manifest(item) for item in files],
        "format_version": 2,
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


def publish_source_supplement(
    root: Path,
    config: RepoConfig,
    tree: GitTree,
    paths: Sequence[str],
    collected_date: str,
) -> SourceSupplement:
    """Publish a bounded immutable exact-SHA supplement without changing a snapshot."""
    root = Path(root).resolve()
    with _artifact_lock(root):
        return _publish_source_supplement_unlocked(
            root, config, tree, paths, collected_date
        )


def _publish_source_supplement_unlocked(
    root: Path,
    config: RepoConfig,
    tree: GitTree,
    paths: Sequence[str],
    collected_date: str,
) -> SourceSupplement:
    _require_date(collected_date)
    requested = tuple(sorted(set(paths)))
    if not requested or any(not safe_policy_path(path) for path in requested):
        raise PilotStoreError("supplement paths must be safe repository-relative paths")
    blobs = {blob.path: blob for blob in tree.blobs()}
    files = []
    total = 0
    for path in requested:
        blob = blobs.get(path)
        if blob is None or blob.mode not in ("100644", "100755"):
            raise PilotStoreError("supplement path must be a regular tracked file: " + path)
        content = tree.read_blob(path, max_bytes=config.max_file_bytes)
        total += len(content)
        if total > config.max_snapshot_bytes:
            raise PilotStoreError("supplement exceeds max_snapshot_bytes")
        files.append(
            CapsuleFile(
                path=path,
                content=content,
                sha256=hashlib.sha256(content).hexdigest(),
                size=len(content),
                purpose="query-supplement",
                git_blob_oid=blob.oid,
                git_mode=blob.mode,
                package="",
                classification_reason="explicit-query-path",
            )
        )
    scan_evidence_files(files, config.secret_allowlist)
    identity = hashlib.sha256(
        canonical_json_bytes(
            {
                "files": [
                    {"path": item.path, "sha256": item.sha256}
                    for item in files
                ],
                "repository": config.id,
                "sha": tree.sha,
            }
        )
    ).hexdigest()
    repository_root = _raw_repository_root(root, config)
    supplement_root = repository_root / "supplements"
    for manifest_path in sorted(supplement_root.glob("*/manifest.json")):
        manifest = _read_json(manifest_path)
        if manifest.get("identity_sha256") == identity:
            return _supplement_from_manifest(manifest_path.parent, manifest)
    manifest = {
        "collected_date": collected_date,
        "files": [_file_manifest(item) for item in files],
        "format_version": 1,
        "identity_sha256": identity,
        "repository": config.id,
        "sha": tree.sha,
    }
    destination = supplement_root / (
        collected_date + "-" + tree.sha[:7] + "-" + identity[:8]
    )
    staging = _new_staging(repository_root)
    try:
        for item in files:
            target = staging / "files" / item.path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(item.content)
        _write_json(staging / "manifest.json", manifest)
        supplement_root.mkdir(parents=True, exist_ok=True)
        os.replace(str(staging), str(destination))
    except Exception:
        _clean_owned(staging)
        raise
    return _supplement_from_manifest(destination, manifest)


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
    with _artifact_lock(root):
        return _publish_release_record_unlocked(
            root,
            config,
            candidate,
            release_date,
            evidence,
            collected_date,
        )


def _publish_release_record_unlocked(
    root: Path,
    config: RepoConfig,
    candidate: ReleaseCandidate,
    release_date: str,
    evidence: Optional[ReleaseNotesEvidence],
    collected_date: str,
) -> PackageReleaseRecord:
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
    scan_evidence_files(
        (
            CapsuleFile(
                path="release-notes.md",
                content=notes,
                sha256=notes_sha256,
                size=len(notes),
                purpose="release-notes",
                git_blob_oid=notes_sha256,
                git_mode="100644",
                package=candidate.package,
                classification_reason="release-notes",
            ),
        ),
        config.secret_allowlist,
    )
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
    upstream_changes = read_upstream_changes(
        repo_root,
        from_sha,
        to_sha,
        pathspecs,
    )
    patch = _run_git_bytes(
        repo_root,
        ("diff", "--no-ext-diff", "--unified=3", from_sha, to_sha, "--")
        + pathspecs,
    )
    changed_paths = _changed_path_union(upstream_changes)
    if len(config.capsules) != 1:
        raise PilotStoreError("comparison requires exactly one capsule policy")
    capsule = config.capsules[0]
    if len(changed_paths) > capsule.max_packet_files:
        raise PilotStoreError("comparison exceeds max_packet_files")
    if len(patch) > capsule.max_packet_utf8_bytes:
        raise PilotStoreError("comparison exceeds max_packet_utf8_bytes")
    comparison_root = (
        _tracking_repository_root(Path(root).resolve(), config)
        / "comparisons"
        / package_slug(package)
        / (_version_slug(from_version) + "--" + _version_slug(to_version))
    )
    metadata = {
        "changed_paths": list(changed_paths),
        "format_version": 2,
        "from_sha": from_sha,
        "from_version": from_version,
        "package": package,
        "pathspecs": list(pathspecs),
        "repository": config.id,
        "to_sha": to_sha,
        "to_version": to_version,
        "upstream_changes": [
            {
                "new_path": item.new_path,
                "old_path": item.old_path,
                "status": item.status,
            }
            for item in upstream_changes
        ],
    }
    markdown = _comparison_markdown(metadata)
    markdown_bytes = markdown.encode("utf-8")
    metadata["markdown_sha256"] = hashlib.sha256(markdown_bytes).hexdigest()
    metadata["patch_sha256"] = hashlib.sha256(patch).hexdigest()
    comparison_evidence = tuple(
        CapsuleFile(
            path=path,
            content=content,
            sha256=hashlib.sha256(content).hexdigest(),
            size=len(content),
            purpose="package-comparison",
            git_blob_oid=hashlib.sha256(content).hexdigest(),
            git_mode="100644",
            package=package,
            classification_reason="generated-comparison",
        )
        for path, content in (
            ("diff.patch", patch),
            ("comparison.md", markdown_bytes),
        )
    )
    scan_evidence_files(comparison_evidence, config.secret_allowlist)
    existing = _existing_comparison(comparison_root, metadata)
    if existing is not None:
        return existing
    comparison_root.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(
        tempfile.mkdtemp(prefix=".comparison-", dir=str(comparison_root.parent))
    )
    try:
        _write_bytes_atomic(staging / "diff.patch", patch)
        _write_bytes_atomic(
            staging / "comparison.json", canonical_json_bytes(metadata) + b"\n"
        )
        _write_bytes_atomic(staging / "comparison.md", markdown_bytes)
        os.replace(str(staging), str(comparison_root))
    except Exception:
        _clean_owned(staging)
        winner = _existing_comparison(comparison_root, metadata)
        if winner is not None:
            return winner
        raise
    return ComparisonRecord(
        package,
        from_version,
        to_version,
        from_sha,
        to_sha,
        changed_paths,
        upstream_changes,
        comparison_root / "diff.patch",
        comparison_root / "comparison.json",
        comparison_root / "comparison.md",
    )


def write_ref_comparison(
    root: Path,
    config: RepoConfig,
    repo_root: Path,
    ref_name: str,
    from_sha: str,
    from_paths: Sequence[str],
    to_sha: str,
    to_paths: Sequence[str],
) -> ComparisonRecord:
    """Write one generated comparison for selected default-branch evidence."""
    if not _OBJECT_ID.fullmatch(from_sha) or not _OBJECT_ID.fullmatch(to_sha):
        raise PilotStoreError("comparison SHA is invalid")
    if (
        not isinstance(ref_name, str)
        or not ref_name
        or any(character.isspace() for character in ref_name)
    ):
        raise PilotStoreError("comparison ref name is invalid")
    pathspecs = tuple(sorted(set(from_paths) | set(to_paths)))
    if not pathspecs or any(not safe_policy_path(path) for path in pathspecs):
        raise PilotStoreError("comparison paths are invalid")
    upstream_changes = read_upstream_changes(repo_root, from_sha, to_sha, pathspecs)
    patch = _run_git_bytes(
        repo_root,
        ("diff", "--no-ext-diff", "--unified=3", from_sha, to_sha, "--")
        + pathspecs,
    )
    changed_paths = _changed_path_union(upstream_changes)
    if len(config.capsules) != 1:
        raise PilotStoreError("comparison requires exactly one capsule policy")
    capsule = config.capsules[0]
    if len(changed_paths) > capsule.max_packet_files:
        raise PilotStoreError("comparison exceeds max_packet_files")
    if len(patch) > capsule.max_packet_utf8_bytes:
        raise PilotStoreError("comparison exceeds max_packet_utf8_bytes")
    comparison_root = (
        _tracking_repository_root(Path(root).resolve(), config)
        / "comparisons"
        / "default-branch"
        / (from_sha[:7] + "--" + to_sha[:7])
    )
    metadata = {
        "changed_paths": list(changed_paths),
        "format_version": 2,
        "from_sha": from_sha,
        "pathspecs": list(pathspecs),
        "ref_kind": "default-branch",
        "ref_name": ref_name,
        "repository": config.id,
        "to_sha": to_sha,
        "upstream_changes": [
            {
                "new_path": item.new_path,
                "old_path": item.old_path,
                "status": item.status,
            }
            for item in upstream_changes
        ],
    }
    markdown = _ref_comparison_markdown(metadata)
    markdown_bytes = markdown.encode("utf-8")
    metadata["markdown_sha256"] = hashlib.sha256(markdown_bytes).hexdigest()
    metadata["patch_sha256"] = hashlib.sha256(patch).hexdigest()
    comparison_evidence = tuple(
        CapsuleFile(
            path=path,
            content=content,
            sha256=hashlib.sha256(content).hexdigest(),
            size=len(content),
            purpose="repository-comparison",
            git_blob_oid=hashlib.sha256(content).hexdigest(),
            git_mode="100644",
            package=_ref_evidence_owner(capsule),
            classification_reason="generated-comparison",
        )
        for path, content in (("diff.patch", patch), ("comparison.md", markdown_bytes))
    )
    scan_evidence_files(comparison_evidence, config.secret_allowlist)
    existing = _existing_ref_comparison(comparison_root, metadata)
    if existing is not None:
        return existing
    comparison_root.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".comparison-", dir=str(comparison_root.parent)))
    try:
        _write_bytes_atomic(staging / "diff.patch", patch)
        _write_bytes_atomic(staging / "comparison.json", canonical_json_bytes(metadata) + b"\n")
        _write_bytes_atomic(staging / "comparison.md", markdown_bytes)
        os.replace(str(staging), str(comparison_root))
    except Exception:
        _clean_owned(staging)
        winner = _existing_ref_comparison(comparison_root, metadata)
        if winner is not None:
            return winner
        raise
    return ComparisonRecord(
        "",
        "",
        "",
        from_sha,
        to_sha,
        changed_paths,
        upstream_changes,
        comparison_root / "diff.patch",
        comparison_root / "comparison.json",
        comparison_root / "comparison.md",
        "default-branch",
        ref_name,
    )


def _existing_ref_comparison(
    comparison_root: Path,
    expected: dict,
) -> Optional[ComparisonRecord]:
    if not comparison_root.exists():
        return None
    if comparison_root.is_symlink() or not comparison_root.is_dir():
        raise PilotStoreError("comparison destination is unsafe")
    manifest_path = comparison_root / "comparison.json"
    patch_path = comparison_root / "diff.patch"
    markdown_path = comparison_root / "comparison.md"
    if any(
        not path.is_file() or path.is_symlink()
        for path in (manifest_path, patch_path, markdown_path)
    ):
        raise PilotStoreError("comparison destination is incomplete")
    manifest = _read_json(manifest_path)
    if (
        manifest != expected
        or hashlib.sha256(patch_path.read_bytes()).hexdigest() != manifest.get("patch_sha256")
        or hashlib.sha256(markdown_path.read_bytes()).hexdigest() != manifest.get("markdown_sha256")
    ):
        raise PilotStoreError("comparison destination conflicts with generated evidence")
    return ComparisonRecord(
        "",
        "",
        "",
        str(manifest["from_sha"]),
        str(manifest["to_sha"]),
        tuple(str(path) for path in manifest["changed_paths"]),
        _upstream_changes_from_manifest(manifest),
        patch_path,
        manifest_path,
        markdown_path,
        str(manifest["ref_kind"]),
        str(manifest["ref_name"]),
    )


def _existing_comparison(
    comparison_root: Path, expected: dict
) -> Optional[ComparisonRecord]:
    if not comparison_root.exists():
        return None
    if comparison_root.is_symlink() or not comparison_root.is_dir():
        raise PilotStoreError("comparison destination is unsafe")
    manifest_path = comparison_root / "comparison.json"
    patch_path = comparison_root / "diff.patch"
    markdown_path = comparison_root / "comparison.md"
    if any(
        not path.is_file() or path.is_symlink()
        for path in (manifest_path, patch_path, markdown_path)
    ):
        raise PilotStoreError("comparison destination is incomplete")
    manifest = _read_json(manifest_path)
    if manifest == expected:
        upstream_changes = _upstream_changes_from_manifest(manifest)
    elif _matches_legacy_comparison(
        manifest,
        expected,
        patch_path,
        markdown_path,
    ):
        upstream_changes = _upstream_changes_from_manifest(expected)
    else:
        raise PilotStoreError("comparison destination conflicts with generated evidence")
    return ComparisonRecord(
        str(manifest["package"]),
        str(manifest["from_version"]),
        str(manifest["to_version"]),
        str(manifest["from_sha"]),
        str(manifest["to_sha"]),
        tuple(str(path) for path in manifest["changed_paths"]),
        upstream_changes,
        patch_path,
        manifest_path,
        markdown_path,
    )


def _matches_legacy_comparison(
    manifest: dict,
    expected: dict,
    patch_path: Path,
    markdown_path: Path,
) -> bool:
    legacy_fields = set(expected) - {"upstream_changes"}
    if (
        manifest.get("format_version") != 1
        or set(manifest) != legacy_fields
    ):
        return False
    comparable = set(legacy_fields) - {"format_version", "markdown_sha256"}
    if any(manifest.get(field) != expected.get(field) for field in comparable):
        return False
    return (
        hashlib.sha256(patch_path.read_bytes()).hexdigest()
        == manifest.get("patch_sha256")
        and hashlib.sha256(markdown_path.read_bytes()).hexdigest()
        == manifest.get("markdown_sha256")
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
        if blob.mode not in ("100644", "100755") or tree.blob_size(path) > config.max_file_bytes:
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


def _supplement_from_manifest(directory: Path, manifest: dict) -> SourceSupplement:
    return SourceSupplement(
        str(manifest["repository"]),
        str(manifest["sha"]),
        str(manifest["collected_date"]),
        directory,
        directory / "manifest.json",
        tuple(str(item["path"]) for item in manifest["files"]),
    )


def _raw_repository_root(root: Path, config: RepoConfig) -> Path:
    name = config.id.split("/", 1)[1]
    base = root / "raw" / "github"
    candidate = base / config.company / name
    _require_contained_storage_path(root, candidate)
    return candidate


def _tracking_repository_root(root: Path, config: RepoConfig) -> Path:
    name = config.id.split("/", 1)[1]
    candidate = root / "tracking" / "github" / "repos" / config.company / name
    _require_contained_storage_path(root, candidate)
    return candidate


def _require_contained_storage_path(root: Path, candidate: Path) -> None:
    root = root.resolve()
    try:
        relative = candidate.relative_to(root)
    except ValueError as error:
        raise PilotStoreError("repository storage path escapes wiki root") from error
    current = root
    for component in relative.parts:
        current = current / component
        if current.is_symlink():
            raise PilotStoreError("repository storage path contains a symlink")
    resolved = candidate.resolve(strict=False)
    if resolved != root and root not in resolved.parents:
        raise PilotStoreError("repository storage path escapes wiki root")


@contextmanager
def _artifact_lock(root: Path):
    lock_path = root / "tracking" / "github" / "artifacts.lock"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with _ARTIFACT_THREAD_LOCK:
        with lock_path.open("a+b") as lock:
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
            try:
                yield
            finally:
                fcntl.flock(lock.fileno(), fcntl.LOCK_UN)


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
    if metadata.get("format_version") == 2:
        lines.extend(["", "## Upstream changes", ""])
        rows = metadata["upstream_changes"]
        for row in rows:
            old_path = str(row["old_path"])
            new_path = str(row["new_path"])
            status = str(row["status"])
            if status == "renamed":
                label = "`" + old_path + "` -> `" + new_path + "`"
            else:
                label = "`" + (new_path or old_path) + "`"
            lines.append("- `" + status + "`: " + label)
        if not rows:
            lines.append("- None")
    return "\n".join(lines) + "\n"


def _ref_comparison_markdown(metadata: dict) -> str:
    lines = [
        "# GitHub repository ref comparison",
        "",
        "- Repository: `" + str(metadata["repository"]) + "`",
        "- Ref: `" + str(metadata["ref_kind"]) + "/" + str(metadata["ref_name"]) + "`",
        "- From SHA: `" + str(metadata["from_sha"]) + "`",
        "- To SHA: `" + str(metadata["to_sha"]) + "`",
        "- Patch: [diff.patch](diff.patch)",
        "",
        "## Changed paths",
        "",
    ]
    changed = metadata["changed_paths"]
    lines.extend("- `" + str(path) + "`" for path in changed)
    if not changed:
        lines.append("- None")
    lines.extend(["", "## Upstream changes", ""])
    for row in metadata["upstream_changes"]:
        old_path = str(row["old_path"])
        new_path = str(row["new_path"])
        status = str(row["status"])
        label = (
            "`" + old_path + "` -> `" + new_path + "`"
            if status == "renamed"
            else "`" + (new_path or old_path) + "`"
        )
        lines.append("- `" + status + "`: " + label)
    if not metadata["upstream_changes"]:
        lines.append("- None")
    return "\n".join(lines) + "\n"


def read_upstream_changes(
    repo_root: Path,
    from_sha: str,
    to_sha: str,
    pathspecs: Sequence[str] = (),
) -> Tuple[UpstreamChange, ...]:
    """Return strict rename-aware changes between two local Git objects."""
    if not _OBJECT_ID.fullmatch(from_sha) or not _OBJECT_ID.fullmatch(to_sha):
        raise PilotStoreError("comparison SHA is invalid")
    normalized_paths = tuple(sorted(set(pathspecs)))
    if any(not safe_policy_path(path) for path in normalized_paths):
        raise PilotStoreError("comparison paths are invalid")
    args = (
        "diff",
        "--name-status",
        "-z",
        "-M",
        "--find-renames=50%",
        from_sha,
        to_sha,
    )
    if normalized_paths:
        args += ("--",) + normalized_paths
    output = _run_git_bytes(repo_root, args)
    values = output.split(b"\0")
    if values and values[-1] == b"":
        values.pop()
    changes = []
    index = 0
    while index < len(values):
        status = _decode_git_field(values[index], "status")
        index += 1
        if status in ("A", "M", "D"):
            if index >= len(values):
                raise PilotStoreError("Git comparison status row is malformed")
            path = _decode_git_field(values[index], "path")
            index += 1
            if status == "A":
                item = UpstreamChange("added", "", path)
            elif status == "D":
                item = UpstreamChange("deleted", path, "")
            else:
                item = UpstreamChange("modified", path, path)
        elif re.fullmatch(r"R(?:100|0[0-9]{2})", status):
            if index + 1 >= len(values):
                raise PilotStoreError("Git comparison rename row is malformed")
            old_path = _decode_git_field(values[index], "old path")
            new_path = _decode_git_field(values[index + 1], "new path")
            index += 2
            item = UpstreamChange("renamed", old_path, new_path)
        else:
            raise PilotStoreError("Git comparison status is unsupported")
        _validate_upstream_change(item, normalized_paths)
        changes.append(item)
    if len(changes) != len(set(changes)):
        raise PilotStoreError("Git comparison contains duplicate status rows")
    return tuple(
        sorted(
            changes,
            key=lambda item: (
                item.new_path or item.old_path,
                item.old_path,
                item.status,
            ),
        )
    )


def _decode_git_field(value: bytes, label: str) -> str:
    try:
        decoded = value.decode("utf-8")
    except UnicodeDecodeError:
        raise PilotStoreError("Git comparison " + label + " is not UTF-8") from None
    if not safe_policy_path(decoded):
        raise PilotStoreError("Git comparison " + label + " is unsafe")
    return decoded


def _validate_upstream_change(
    item: UpstreamChange, pathspecs: Sequence[str] = ()
) -> None:
    if not isinstance(item, UpstreamChange):
        raise TypeError("upstream change must be UpstreamChange")
    valid_shape = (
        item.status == "added"
        and not item.old_path
        and bool(item.new_path)
        or item.status == "deleted"
        and bool(item.old_path)
        and not item.new_path
        or item.status == "modified"
        and bool(item.old_path)
        and item.old_path == item.new_path
        or item.status == "renamed"
        and bool(item.old_path)
        and bool(item.new_path)
        and item.old_path != item.new_path
    )
    if not valid_shape:
        raise PilotStoreError("Git comparison status row is invalid")
    paths = tuple(path for path in (item.old_path, item.new_path) if path)
    if any(not safe_policy_path(path) for path in paths):
        raise PilotStoreError("Git comparison path is unsafe")
    if pathspecs and any(
        not any(path == root or path.startswith(root + "/") for root in pathspecs)
        for path in paths
    ):
        raise PilotStoreError("Git comparison path escapes requested scope")


def _changed_path_union(
    changes: Sequence[UpstreamChange],
) -> Tuple[str, ...]:
    return tuple(
        sorted(
            {
                path
                for item in changes
                for path in (item.old_path, item.new_path)
                if path
            }
        )
    )


def _upstream_changes_from_manifest(manifest: dict) -> Tuple[UpstreamChange, ...]:
    if manifest.get("format_version") == 1:
        return tuple(
            UpstreamChange("modified", str(path), str(path))
            for path in manifest["changed_paths"]
        )
    rows = manifest.get("upstream_changes")
    if not isinstance(rows, list):
        raise PilotStoreError("comparison upstream changes are invalid")
    changes = tuple(
        UpstreamChange(
            str(row.get("status", "")),
            str(row.get("old_path", "")),
            str(row.get("new_path", "")),
        )
        for row in rows
        if isinstance(row, dict)
    )
    if len(changes) != len(rows):
        raise PilotStoreError("comparison upstream changes are invalid")
    for item in changes:
        _validate_upstream_change(item)
    if _changed_path_union(changes) != tuple(manifest["changed_paths"]):
        raise PilotStoreError("comparison changed path union mismatch")
    return changes


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
    "SourceSupplement",
    "package_slug",
    "publish_release_record",
    "publish_source_snapshot",
    "publish_source_supplement",
    "write_package_comparison",
    "write_ref_comparison",
]
