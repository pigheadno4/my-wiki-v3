"""Deterministic validation for focused GitHub collection artifacts."""

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
from typing import Any, Dict, List, Optional, Sequence, Tuple

from github_canonical import canonical_json_bytes, safe_policy_path
from github_registry import RepoConfig, load_registry, validate_enabled_policy
from github_versions import parse_package_tag, parse_semver
from github_work_items import WorkItem, load_work_items, render_status


_OBJECT_ID = re.compile(r"^(?:[0-9a-f]{40}|[0-9a-f]{64})$")
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_SNAPSHOT_FIELDS = {
    "collected_date",
    "excluded",
    "files",
    "format_version",
    "repository",
    "sha",
    "triggering_refs",
}
_SNAPSHOT_V2_FIELDS = _SNAPSHOT_FIELDS | {"author_date", "commit_date"}
_SNAPSHOT_FILE_FIELDS = {
    "classification_reason",
    "git_blob_oid",
    "git_mode",
    "package",
    "path",
    "purpose",
    "sha256",
    "size",
}
_RELEASE_FIELDS = {
    "collected_date",
    "format_version",
    "notes_available",
    "notes_sha256",
    "package",
    "release_date",
    "repository",
    "sha",
    "source_url",
    "tag",
    "version",
}
_SUPPLEMENT_FIELDS = {
    "collected_date",
    "files",
    "format_version",
    "identity_sha256",
    "repository",
    "sha",
}
_COMPARISON_FIELDS = {
    "changed_paths",
    "format_version",
    "from_sha",
    "from_version",
    "markdown_sha256",
    "package",
    "patch_sha256",
    "pathspecs",
    "repository",
    "to_sha",
    "to_version",
}


@dataclass(frozen=True)
class RepositoryInspection:
    path: Path
    repositories: Tuple[RepoConfig, ...]
    error: str = ""


@dataclass(frozen=True)
class ManifestInspection:
    path: Path
    relative_path: str
    document: Optional[dict]
    error: str = ""


@dataclass(frozen=True)
class WorkItemInspection:
    path: Path
    items: Tuple[WorkItem, ...]
    exists: bool
    error: str = ""


@dataclass(frozen=True)
class PageInspection:
    path: Path
    relative_path: str
    text: str
    error: str = ""


@dataclass(frozen=True)
class StatusInspection:
    path: Path
    text: str
    exists: bool
    error: str = ""


@dataclass(frozen=True)
class GitHubReport:
    repositories: RepositoryInspection
    snapshots: Tuple[ManifestInspection, ...]
    supplements: Tuple[ManifestInspection, ...]
    release_records: Tuple[ManifestInspection, ...]
    comparisons: Tuple[ManifestInspection, ...]
    work_items: WorkItemInspection
    source_pages: Tuple[PageInspection, ...]
    changelog_pages: Tuple[PageInspection, ...]
    status_text: StatusInspection


def inspect_github(root: Path) -> GitHubReport:
    """Inspect focused GitHub authorities without raising on malformed artifacts."""
    root = Path(root).resolve()
    registry_path = root / "tracking/github/repo-registry.toml"
    try:
        repositories = RepositoryInspection(
            registry_path, load_registry(registry_path), ""
        )
    except (OSError, ValueError) as error:
        repositories = RepositoryInspection(registry_path, (), _bounded(error))

    snapshots = _inspect_manifests(
        root, root.glob("raw/github/*/*/snapshots/*/manifest.json")
    )
    supplements = _inspect_manifests(
        root, root.glob("raw/github/*/*/supplements/*/manifest.json")
    )
    release_records = _inspect_manifests(
        root, root.glob("raw/github/*/*/releases/*/*/*/manifest.json")
    )
    comparisons = _inspect_manifests(
        root,
        root.glob("tracking/github/repos/*/*/comparisons/*/*/comparison.json"),
    )
    queue_path = root / "tracking/github/work-items.json"
    if queue_path.exists():
        try:
            work_items = WorkItemInspection(
                queue_path, load_work_items(queue_path), True, ""
            )
        except (OSError, ValueError, TypeError) as error:
            work_items = WorkItemInspection(queue_path, (), True, _bounded(error))
    else:
        work_items = WorkItemInspection(queue_path, (), False, "")
    source_pages = _inspect_pages(
        root, root.glob("wiki/sources/*/github/source-github-*.md")
    )
    changelog_pages = _inspect_pages(
        root, root.glob("wiki/sources/*/github/changelog-github-*.md")
    )
    status_path = root / "tracking/github/status.md"
    if status_path.exists():
        try:
            status = StatusInspection(
                status_path, status_path.read_text(encoding="utf-8"), True, ""
            )
        except (OSError, UnicodeError) as error:
            status = StatusInspection(status_path, "", True, _bounded(error))
    else:
        status = StatusInspection(status_path, "", False, "")
    return GitHubReport(
        repositories,
        snapshots,
        supplements,
        release_records,
        comparisons,
        work_items,
        source_pages,
        changelog_pages,
        status,
    )


def validate_github(report: GitHubReport) -> List[str]:
    """Validate registry, immutable evidence, queue/status, and ingested pages."""
    if not isinstance(report, GitHubReport):
        raise TypeError("report must be GitHubReport")
    errors: List[str] = []
    errors.extend(_validate_repositories(report.repositories))
    snapshot_index, snapshot_paths = _validate_snapshots(report.snapshots, errors)
    _validate_supplements(report.supplements, snapshot_index, errors)
    release_index = _validate_releases(
        report.release_records, snapshot_index, errors
    )
    comparison_paths = _validate_comparisons(
        report.comparisons, snapshot_index, errors
    )
    _validate_work_items(
        report,
        snapshot_paths,
        release_index,
        comparison_paths,
        errors,
    )
    return _deduplicated(errors)


def _validate_repositories(inspection: RepositoryInspection) -> List[str]:
    if inspection.error:
        return ["repository registry is invalid: " + inspection.error]
    errors = []
    for repo in inspection.repositories:
        errors.extend(repo.id + ": " + error for error in validate_enabled_policy(repo))
        if not repo.version_tracks:
            continue
        if len(repo.capsules) != 1:
            errors.append(repo.id + ": package release tracks require one capsule policy")
        for track in repo.version_tracks:
            if not track.selector.startswith("package:"):
                errors.append(repo.id + ": release selector must be package-qualified")
                continue
            parsed = parse_package_tag(track.selector[8:])
            if parsed is None:
                errors.append(repo.id + ": package release selector is invalid")
    return errors


def _validate_snapshots(
    inspections: Sequence[ManifestInspection], errors: List[str]
) -> Tuple[Dict[Tuple[str, str], ManifestInspection], set]:
    index: Dict[Tuple[str, str], ManifestInspection] = {}
    paths = set()
    for artifact in inspections:
        label = artifact.relative_path
        if artifact.error or artifact.document is None:
            errors.append(label + ": snapshot manifest is invalid: " + artifact.error)
            continue
        document = artifact.document
        version = document.get("format_version")
        expected_fields = _SNAPSHOT_V2_FIELDS if version == 2 else _SNAPSHOT_FIELDS
        if set(document) != expected_fields or version not in (1, 2):
            errors.append(label + ": snapshot manifest has unknown or missing fields")
            continue
        if version == 2 and (
            not isinstance(document.get("author_date"), str)
            or not document.get("author_date")
            or not isinstance(document.get("commit_date"), str)
            or not document.get("commit_date")
        ):
            errors.append(label + ": snapshot commit dates are invalid")
        repo_id = document.get("repository")
        sha = document.get("sha")
        files = document.get("files")
        if not isinstance(repo_id, str) or not isinstance(sha, str) or not _OBJECT_ID.fullmatch(sha):
            errors.append(label + ": snapshot identity is invalid")
            continue
        if not isinstance(files, list):
            errors.append(label + ": snapshot files must be an array")
            continue
        key = (repo_id, sha)
        if key in index:
            errors.append(label + ": duplicate SHA snapshot for " + repo_id)
        index[key] = artifact
        paths.add(label)
        seen = set()
        for row in files:
            if not isinstance(row, dict) or set(row) != _SNAPSHOT_FILE_FIELDS:
                errors.append(label + ": snapshot file row is invalid")
                continue
            path = row.get("path")
            if not isinstance(path, str) or not safe_policy_path(path):
                errors.append(label + ": unsafe snapshot file path")
                continue
            if path in seen:
                errors.append(label + ": duplicate snapshot file path " + path)
                continue
            seen.add(path)
            expected_hash = row.get("sha256")
            expected_size = row.get("size")
            if not isinstance(expected_hash, str) or not _SHA256.fullmatch(expected_hash):
                errors.append(label + ": snapshot file hash is invalid")
                continue
            if not isinstance(expected_size, int) or expected_size < 0:
                errors.append(label + ": snapshot file size is invalid")
                continue
            saved = artifact.path.parent / "files" / Path(path)
            if not saved.is_file() or saved.is_symlink():
                errors.append(label + ": snapshot file is missing " + path)
                continue
            try:
                content = saved.read_bytes()
            except OSError as error:
                errors.append(label + ": snapshot file is unreadable " + path + ": " + _bounded(error))
                continue
            if len(content) != expected_size:
                errors.append(label + ": snapshot file size mismatch " + path)
            if hashlib.sha256(content).hexdigest() != expected_hash:
                errors.append(label + ": snapshot file hash mismatch " + path)
    return index, paths


def _validate_supplements(
    inspections: Sequence[ManifestInspection],
    snapshots: Dict[Tuple[str, str], ManifestInspection],
    errors: List[str],
) -> None:
    identities = set()
    for artifact in inspections:
        label = artifact.relative_path
        if artifact.error or artifact.document is None:
            errors.append(label + ": supplement manifest is invalid: " + artifact.error)
            continue
        document = artifact.document
        if set(document) != _SUPPLEMENT_FIELDS or document.get("format_version") != 1:
            errors.append(label + ": supplement manifest has unknown or missing fields")
            continue
        repo_id = document.get("repository")
        sha = document.get("sha")
        identity = document.get("identity_sha256")
        files = document.get("files")
        if (
            not isinstance(repo_id, str)
            or not isinstance(sha, str)
            or not _OBJECT_ID.fullmatch(sha)
            or not isinstance(identity, str)
            or not _SHA256.fullmatch(identity)
            or not isinstance(files, list)
        ):
            errors.append(label + ": supplement identity is invalid")
            continue
        if (repo_id, sha) not in snapshots:
            errors.append(label + ": supplement links missing SHA snapshot")
        identity_key = (repo_id, sha, identity)
        if identity_key in identities:
            errors.append(label + ": duplicate source supplement")
        identities.add(identity_key)
        identity_rows = []
        seen = set()
        for row in files:
            if not isinstance(row, dict) or set(row) != _SNAPSHOT_FILE_FIELDS:
                errors.append(label + ": supplement file row is invalid")
                continue
            path = row.get("path")
            digest = row.get("sha256")
            size = row.get("size")
            if (
                not isinstance(path, str)
                or not safe_policy_path(path)
                or not isinstance(digest, str)
                or not _SHA256.fullmatch(digest)
                or not isinstance(size, int)
                or size < 0
            ):
                errors.append(label + ": supplement file row is invalid")
                continue
            if path in seen:
                errors.append(label + ": duplicate supplement file path " + path)
                continue
            seen.add(path)
            identity_rows.append({"path": path, "sha256": digest})
            saved = artifact.path.parent / "files" / Path(path)
            if not saved.is_file() or saved.is_symlink():
                errors.append(label + ": supplement file is missing " + path)
                continue
            try:
                content = saved.read_bytes()
            except OSError as error:
                errors.append(label + ": supplement file is unreadable " + path + ": " + _bounded(error))
                continue
            if len(content) != size:
                errors.append(label + ": supplement file size mismatch " + path)
            if hashlib.sha256(content).hexdigest() != digest:
                errors.append(label + ": supplement file hash mismatch " + path)
        expected_identity = hashlib.sha256(
            canonical_json_bytes(
                {
                    "files": identity_rows,
                    "repository": repo_id,
                    "sha": sha,
                }
            )
        ).hexdigest()
        if identity != expected_identity:
            errors.append(label + ": supplement identity hash mismatch")


def _validate_releases(
    inspections: Sequence[ManifestInspection],
    snapshots: Dict[Tuple[str, str], ManifestInspection],
    errors: List[str],
) -> Dict[str, ManifestInspection]:
    paths: Dict[str, ManifestInspection] = {}
    identities: Dict[Tuple[str, str, str, str, str], List[ManifestInspection]] = {}
    for artifact in inspections:
        label = artifact.relative_path
        paths[label] = artifact
        if artifact.error or artifact.document is None:
            errors.append(label + ": release manifest is invalid: " + artifact.error)
            continue
        document = artifact.document
        if set(document) != _RELEASE_FIELDS or document.get("format_version") != 1:
            errors.append(label + ": release manifest has unknown or missing fields")
            continue
        values = tuple(
            document.get(key) for key in ("repository", "package", "version", "tag", "sha")
        )
        if any(not isinstance(value, str) or not value for value in values):
            errors.append(label + ": release identity is invalid")
            continue
        repo_id, package, version, tag, sha = values
        if parse_package_tag(package + "@" + version) != (package, version):
            errors.append(label + ": release identity is not package-qualified")
        elif not _release_tag_matches(tag, package, version):
            errors.append(label + ": release tag does not match package version")
        if not _OBJECT_ID.fullmatch(sha):
            errors.append(label + ": release SHA is invalid")
        elif (repo_id, sha) not in snapshots:
            errors.append(label + ": release record links missing SHA snapshot")
        notes_hash = document.get("notes_sha256")
        notes_path = artifact.path.parent / "release-notes.md"
        if not isinstance(notes_hash, str) or not _SHA256.fullmatch(notes_hash):
            errors.append(label + ": release notes hash is invalid")
        elif not notes_path.is_file() or notes_path.is_symlink():
            errors.append(label + ": release notes file is missing")
        else:
            try:
                actual_notes_hash = hashlib.sha256(notes_path.read_bytes()).hexdigest()
            except OSError as error:
                errors.append(label + ": release notes file is unreadable: " + _bounded(error))
            else:
                if actual_notes_hash != notes_hash:
                    errors.append(label + ": release notes hash mismatch")
        identities.setdefault((repo_id, package, version, tag, sha), []).append(artifact)
    for rows in identities.values():
        if len(rows) < 2:
            continue
        hashes = [str(row.document.get("notes_sha256")) for row in rows if row.document]
        directory_names_valid = all(
            row.path.parent.name.startswith(str(row.document.get("collected_date")))
            for row in rows
            if row.document
        )
        if len(set(hashes)) != len(hashes) or not directory_names_valid:
            errors.append(
                rows[-1].relative_path + ": duplicate release identity without revision"
            )
    return paths


def _release_tag_matches(tag: str, package: str, version: str) -> bool:
    package_tag = parse_package_tag(tag)
    if package_tag is not None:
        return package_tag == (package, version)
    plain_version = tag[1:] if tag.startswith("v") else tag
    return plain_version == version and parse_semver(tag) is not None


def _validate_comparisons(
    inspections: Sequence[ManifestInspection],
    snapshots: Dict[Tuple[str, str], ManifestInspection],
    errors: List[str],
) -> set:
    paths = set()
    for artifact in inspections:
        label = artifact.relative_path
        paths.add(label)
        if artifact.error or artifact.document is None:
            errors.append(label + ": comparison manifest is invalid: " + artifact.error)
            continue
        document = artifact.document
        if set(document) != _COMPARISON_FIELDS or document.get("format_version") != 1:
            errors.append(label + ": comparison manifest has unknown or missing fields")
            continue
        repo_id = document.get("repository")
        from_sha = document.get("from_sha")
        to_sha = document.get("to_sha")
        if (
            not isinstance(repo_id, str)
            or not isinstance(from_sha, str)
            or not _OBJECT_ID.fullmatch(from_sha)
            or not isinstance(to_sha, str)
            or not _OBJECT_ID.fullmatch(to_sha)
        ):
            errors.append(label + ": comparison identity is invalid")
        elif (repo_id, from_sha) not in snapshots or (repo_id, to_sha) not in snapshots:
            errors.append(label + ": comparison links missing SHA snapshot")
        for field in ("changed_paths", "pathspecs"):
            values = document.get(field)
            if not isinstance(values, list) or any(
                not isinstance(value, str) or not safe_policy_path(value)
                for value in values
            ):
                errors.append(label + ": comparison contains unsafe " + field)
        for name in ("diff.patch", "comparison.md"):
            path = artifact.path.parent / name
            if not path.is_file() or path.is_symlink():
                errors.append(label + ": comparison file is missing " + name)
        for name, field, message in (
            ("diff.patch", "patch_sha256", "comparison patch hash mismatch"),
            ("comparison.md", "markdown_sha256", "comparison Markdown hash mismatch"),
        ):
            expected_hash = document.get(field)
            path = artifact.path.parent / name
            if not isinstance(expected_hash, str) or not _SHA256.fullmatch(expected_hash):
                errors.append(label + ": comparison file hash is invalid")
            elif path.is_file() and not path.is_symlink():
                try:
                    actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
                except OSError as error:
                    errors.append(label + ": comparison file is unreadable: " + _bounded(error))
                else:
                    if actual_hash != expected_hash:
                        errors.append(label + ": " + message)
    return paths


def _validate_work_items(
    report: GitHubReport,
    snapshot_paths: set,
    release_paths: Dict[str, ManifestInspection],
    comparison_paths: set,
    errors: List[str],
) -> None:
    inspection = report.work_items
    if inspection.error:
        errors.append("work-item queue is invalid: " + inspection.error)
        return
    if inspection.exists:
        status = report.status_text
        if status.error:
            errors.append("tracking/github/status.md is unreadable: " + status.error)
        elif not status.exists or status.text != render_status(inspection.items):
            errors.append("tracking/github/status.md is stale")
    elif report.status_text.exists:
        errors.append("tracking/github/status.md exists without work-items.json")

    source_pages = {page.relative_path: page for page in report.source_pages}
    changelog_pages = {page.relative_path: page for page in report.changelog_pages}
    snapshots = {artifact.relative_path: artifact for artifact in report.snapshots}
    comparisons = {artifact.relative_path: artifact for artifact in report.comparisons}
    for page in tuple(report.source_pages) + tuple(report.changelog_pages):
        if page.error:
            errors.append(page.relative_path + ": page is unreadable: " + page.error)
    repos = {repo.id: repo for repo in report.repositories.repositories}
    for item in inspection.items:
        if item.snapshot_manifest and item.snapshot_manifest not in snapshot_paths:
            errors.append(item.work_item_id + ": missing snapshot manifest")
        elif item.snapshot_manifest:
            snapshot = snapshots.get(item.snapshot_manifest)
            document = snapshot.document if snapshot is not None else None
            if document is not None and (
                document.get("repository") != item.repo_id
                or document.get("sha") != item.sha
            ):
                errors.append(item.work_item_id + ": work-item snapshot identity mismatch")
        for change in item.package_changes:
            release = release_paths.get(change.release_manifest)
            if change.release_manifest and release is None:
                errors.append(item.work_item_id + ": missing release manifest " + change.release_id)
            elif release is not None and release.document is not None:
                package = release.document.get("package")
                version = release.document.get("version")
                if not isinstance(package, str) or not isinstance(version, str):
                    errors.append(item.work_item_id + ": release manifest identity is invalid")
                elif package + "@" + version != change.release_id:
                    errors.append(item.work_item_id + ": release manifest identity mismatch")
                if release.document.get("repository") != item.repo_id:
                    errors.append(item.work_item_id + ": work-item release repository mismatch")
                if release.document.get("sha") != item.sha:
                    errors.append(item.work_item_id + ": work-item release SHA mismatch")
            if change.comparison_manifest and change.comparison_manifest not in comparison_paths:
                errors.append(item.work_item_id + ": missing comparison manifest " + change.release_id)
            elif change.comparison_manifest:
                comparison = comparisons.get(change.comparison_manifest)
                document = comparison.document if comparison is not None else None
                if document is not None and (
                    document.get("repository") != item.repo_id
                    or document.get("package") != change.package
                    or document.get("from_version") != change.from_version
                    or document.get("to_version") != change.to_version
                    or document.get("to_sha") != item.sha
                ):
                    errors.append(item.work_item_id + ": work-item comparison identity mismatch")
        if item.state != "ingested":
            continue
        repo = repos.get(item.repo_id)
        if repo is None:
            errors.append(item.work_item_id + ": repository is absent from registry")
            continue
        name = item.repo_id.split("/", 1)[1]
        source_path = "wiki/sources/" + repo.company + "/github/source-github-" + name + ".md"
        changelog_path = "wiki/sources/" + repo.company + "/github/changelog-github-" + name + ".md"
        source = source_pages.get(source_path)
        changelog = changelog_pages.get(changelog_path)
        if source is None:
            errors.append(item.work_item_id + ": missing " + source_path)
        elif item.snapshot_manifest not in source.text:
            errors.append(item.work_item_id + ": source page omits raw snapshot link")
        if changelog is None:
            errors.append(item.work_item_id + ": missing " + changelog_path)
            continue
        for change in item.package_changes:
            if change.release_id not in changelog.text:
                errors.append(
                    item.work_item_id
                    + ": changelog omits package-qualified release "
                    + change.release_id
                )
            required = tuple(
                path
                for path in (
                    item.snapshot_manifest,
                    change.release_manifest,
                    change.comparison_manifest,
                )
                if path
            )
            if any(path not in changelog.text for path in required):
                errors.append(
                    item.work_item_id
                    + ": changelog omits raw evidence link for "
                    + change.release_id
                )


def _inspect_manifests(
    root: Path, paths: Sequence[Path]
) -> Tuple[ManifestInspection, ...]:
    return tuple(_inspect_manifest(root, path) for path in sorted(paths))


def _inspect_manifest(root: Path, path: Path) -> ManifestInspection:
    relative = path.relative_to(root).as_posix()
    try:
        document = json.loads(
            path.read_text(encoding="utf-8"), object_pairs_hook=_reject_duplicates
        )
        if not isinstance(document, dict):
            raise ValueError("JSON root must be an object")
        return ManifestInspection(path, relative, document, "")
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as error:
        return ManifestInspection(path, relative, None, _bounded(error))


def _inspect_pages(root: Path, paths: Sequence[Path]) -> Tuple[PageInspection, ...]:
    result = []
    for path in sorted(paths):
        relative = path.relative_to(root).as_posix()
        try:
            result.append(PageInspection(path, relative, path.read_text(encoding="utf-8"), ""))
        except (OSError, UnicodeError) as error:
            result.append(PageInspection(path, relative, "", _bounded(error)))
    return tuple(result)


def _reject_duplicates(pairs: Sequence[Tuple[str, Any]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key " + key)
        result[key] = value
    return result


def _bounded(error: Exception) -> str:
    text = str(error).strip() or error.__class__.__name__
    return text[:1000] + ("..." if len(text) > 1000 else "")


def _deduplicated(values: Sequence[str]) -> List[str]:
    result = []
    seen = set()
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


__all__ = [
    "GitHubReport",
    "ManifestInspection",
    "PageInspection",
    "RepositoryInspection",
    "StatusInspection",
    "WorkItemInspection",
    "inspect_github",
    "validate_github",
]
