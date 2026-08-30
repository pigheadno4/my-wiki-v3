"""Deterministic validation for focused GitHub collection artifacts."""

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
from typing import Any, Dict, List, Optional, Sequence, Tuple

from github_canonical import canonical_json_bytes, safe_policy_path, wiki_slug
from github_capsule_policy import build_effective_policy
from github_registry import RepoConfig, load_registry, validate_enabled_policy
from github_ingest_packets import (
    PackagePacketInput,
    PacketBuildError,
    RefPacketInput,
    build_ingest_packet,
    build_ref_ingest_packet,
    load_packet_summary,
)
from github_collection_index import validate_collection_index
from github_pilot_store import UpstreamChange
from github_versions import parse_package_tag, parse_semver
from github_work_items import (
    PacketStatusSummary,
    WorkItem,
    evidence_attachment_required_reading,
    load_work_items,
    render_status,
)


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
_COMPARISON_V2_FIELDS = _COMPARISON_FIELDS | {"upstream_changes"}
_REF_COMPARISON_FIELDS = {
    "changed_paths",
    "format_version",
    "from_sha",
    "markdown_sha256",
    "patch_sha256",
    "pathspecs",
    "ref_kind",
    "ref_name",
    "repository",
    "to_sha",
    "upstream_changes",
}
_UPSTREAM_CHANGE_FIELDS = {"new_path", "old_path", "status"}


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
    queued_packets: Tuple[ManifestInspection, ...]
    review_packets: Tuple[ManifestInspection, ...]
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
    queued_packets = _inspect_manifests(
        root,
        root.glob("tracking/github/repos/*/*/ingest-packets/*/packet.json"),
    )
    review_packets = _inspect_manifests(
        root,
        root.glob(
            "tracking/github/repos/*/*/comparisons/*/*/review-packet.json"
        ),
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
        queued_packets,
        review_packets,
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
    queued_packets = _validate_packets(report, errors)
    _validate_work_items(
        report,
        snapshot_paths,
        release_index,
        comparison_paths,
        queued_packets,
        errors,
    )
    root = report.repositories.path.parents[2]
    if (
        (root / "tracking/github/collection-index.json").exists()
        or (root / "tracking/github/collection-index.md").exists()
    ):
        errors.extend(
            validate_collection_index(
                root,
                report.repositories.repositories,
                report.work_items.items,
            )
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
        version = document.get("format_version")
        is_ref = "ref_kind" in document
        expected_fields = (
            _REF_COMPARISON_FIELDS
            if is_ref
            else _COMPARISON_V2_FIELDS
            if version == 2
            else _COMPARISON_FIELDS
        )
        if set(document) != expected_fields or version not in (1, 2):
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
        if version == 2:
            _validate_upstream_changes(document, label, errors)
        if is_ref and (
            document.get("ref_kind") != "default-branch"
            or not isinstance(document.get("ref_name"), str)
            or not document.get("ref_name")
        ):
            errors.append(label + ": comparison ref identity is invalid")
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


def _validate_upstream_changes(
    document: dict,
    label: str,
    errors: List[str],
) -> None:
    rows = document.get("upstream_changes")
    if not isinstance(rows, list):
        errors.append(label + ": comparison upstream changes must be an array")
        return
    normalized = []
    seen = set()
    invalid = False
    for row in rows:
        if not isinstance(row, dict) or set(row) != _UPSTREAM_CHANGE_FIELDS:
            invalid = True
            continue
        status = row.get("status")
        old_path = row.get("old_path")
        new_path = row.get("new_path")
        if not all(isinstance(value, str) for value in (status, old_path, new_path)):
            invalid = True
            continue
        valid_shape = (
            status == "added"
            and not old_path
            and bool(new_path)
            or status == "deleted"
            and bool(old_path)
            and not new_path
            or status == "modified"
            and bool(old_path)
            and old_path == new_path
            or status == "renamed"
            and bool(old_path)
            and bool(new_path)
            and old_path != new_path
        )
        paths = tuple(path for path in (old_path, new_path) if path)
        identity = (status, old_path, new_path)
        if (
            not valid_shape
            or any(not safe_policy_path(path) for path in paths)
            or identity in seen
        ):
            invalid = True
            continue
        seen.add(identity)
        normalized.append(identity)
    if invalid:
        errors.append(label + ": comparison upstream change row is invalid")
    expected_paths = sorted(
        {
            path
            for _, old_path, new_path in normalized
            for path in (old_path, new_path)
            if path
        }
    )
    if document.get("changed_paths") != expected_paths:
        errors.append(label + ": comparison changed path union mismatch")


def _validate_packets(
    report: GitHubReport,
    errors: List[str],
) -> Dict[str, dict]:
    root = report.repositories.path.parents[2]
    repos = {repo.id: repo for repo in report.repositories.repositories}
    queued = {}
    for kind, artifacts in (
        ("queued", report.queued_packets),
        ("ad-hoc", report.review_packets),
    ):
        for artifact in artifacts:
            label = artifact.relative_path
            if artifact.error or artifact.document is None:
                errors.append(
                    label + ": packet JSON is invalid: " + artifact.error
                )
                continue
            document = artifact.document
            try:
                content = artifact.path.read_bytes()
            except OSError as error:
                errors.append(label + ": packet JSON is unreadable: " + _bounded(error))
                continue
            if canonical_json_bytes(document) + b"\n" != content:
                errors.append(label + ": packet JSON is not canonical")
            if document.get("packet_kind") != kind:
                errors.append(label + ": packet kind/path mismatch")
                continue
            repo_id = document.get("repository")
            config = repos.get(repo_id) if isinstance(repo_id, str) else None
            if config is None:
                errors.append(label + ": packet repository is absent from registry")
                continue
            work_item_id = document.get("work_item_id")
            if kind == "queued":
                expected_path = (
                    "tracking/github/repos/"
                    + config.company
                    + "/"
                    + config.id.split("/", 1)[1]
                    + "/ingest-packets/"
                    + str(work_item_id)
                    + "/packet.json"
                )
                if label != expected_path:
                    errors.append(label + ": packet path/work-item identity mismatch")
            elif work_item_id:
                errors.append(label + ": ad-hoc packet carries work-item identity")
            markdown_name = "packet.md" if kind == "queued" else "review-packet.md"
            markdown_path = artifact.path.parent / markdown_name
            if not markdown_path.is_file() or markdown_path.is_symlink():
                errors.append(label + ": packet Markdown is missing")
                continue
            try:
                markdown = markdown_path.read_bytes()
            except OSError as error:
                errors.append(label + ": packet Markdown is unreadable: " + _bounded(error))
                continue
            if hashlib.sha256(markdown).hexdigest() != document.get("markdown_sha256"):
                errors.append(label + ": packet Markdown hash mismatch")
            try:
                is_ref_packet = isinstance(document.get("ref"), dict)
                inputs = () if is_ref_packet else _packet_inputs(document)
                stored_policy_hash = document.get("capsule_policy_sha256")
                current_policy_hash = build_effective_policy(
                    config.capsules[0], (), (), ()
                ).policy_hash
                allowed_policy_hashes = {
                    current_policy_hash,
                    *config.capsules[0].historical_policy_hashes,
                }
                if (
                    not isinstance(stored_policy_hash, str)
                    or _SHA256.fullmatch(stored_policy_hash) is None
                    or stored_policy_hash not in allowed_policy_hashes
                ):
                    raise PacketBuildError(
                        "packet policy hash is not current or registered historical policy"
                    )
                if kind == "ad-hoc":
                    comparison_manifest = (
                        str(document["ref"].get("comparison_manifest", ""))
                        if is_ref_packet
                        else inputs[0].comparison_manifest
                        if len(inputs) == 1
                        else ""
                    )
                    if not comparison_manifest:
                        raise PacketBuildError(
                            "ad-hoc packet requires one comparison"
                        )
                    comparison_path = (
                        root / comparison_manifest
                    ).parent.resolve()
                    if comparison_path != artifact.path.parent.resolve():
                        raise PacketBuildError(
                            "ad-hoc packet comparison path mismatch"
                        )
                if is_ref_packet:
                    rebuilt = build_ref_ingest_packet(
                        root,
                        config,
                        str(work_item_id),
                        str(document.get("snapshot_manifest", "")),
                        _ref_packet_input(root, document),
                        kind,
                        document.get("wiki_context"),
                        document.get("expected_wiki_targets"),
                        stored_policy_hash,
                    )
                else:
                    rebuilt = build_ingest_packet(
                        root,
                        config,
                        str(work_item_id),
                        str(document.get("snapshot_manifest", "")),
                        inputs,
                        kind,
                        document.get("wiki_context"),
                        document.get("expected_wiki_targets"),
                        stored_policy_hash,
                    )
            except (OSError, TypeError, ValueError) as error:
                errors.append(label + ": packet rebuild failed: " + _bounded(error))
                continue
            if rebuilt.document != document:
                errors.append(label + ": packet deterministic content mismatch")
            if rebuilt.markdown != markdown:
                errors.append(label + ": packet Markdown content mismatch")
            if kind == "queued":
                queued[label] = document
    return queued


def _packet_inputs(document: dict) -> Tuple[PackagePacketInput, ...]:
    rows = document.get("packages")
    if not isinstance(rows, list):
        raise PacketBuildError("packet packages must be an array")
    inputs = []
    for row in rows:
        if not isinstance(row, dict):
            raise PacketBuildError("packet package row is invalid")
        upstream_rows = row.get("upstream_changes")
        if not isinstance(upstream_rows, list):
            raise PacketBuildError("packet upstream changes must be an array")
        upstream = []
        for change in upstream_rows:
            if not isinstance(change, dict):
                raise PacketBuildError("packet upstream change row is invalid")
            status = change.get("status")
            old_path = change.get("old_path")
            new_path = change.get("new_path")
            if not all(
                isinstance(value, str)
                for value in (status, old_path, new_path)
            ):
                raise PacketBuildError("packet upstream change row is invalid")
            upstream.append(UpstreamChange(status, old_path, new_path))
        recommendation = row.get("recommendation")
        reasons = (
            recommendation.get("reasons")
            if isinstance(recommendation, dict)
            else ()
        )
        inputs.append(
            PackagePacketInput(
                package=str(row.get("package", "")),
                from_version=str(row.get("from_version", "")),
                to_version=str(row.get("to_version", "")),
                from_sha=str(row.get("from_sha", "")),
                to_sha=str(row.get("to_sha", "")),
                release_manifest=str(row.get("release_manifest", "")),
                comparison_manifest=str(row.get("comparison_manifest", "")),
                prior_snapshot_manifest=str(
                    row.get("prior_snapshot_manifest", "")
                ),
                upstream_changes=tuple(upstream),
                release_notes_revision=(
                    isinstance(reasons, list)
                    and "release-notes-revision" in reasons
                ),
            )
        )
    return tuple(inputs)


def _ref_packet_input(root: Path, document: dict) -> RefPacketInput:
    ref = document.get("ref")
    if not isinstance(ref, dict):
        raise PacketBuildError("packet ref is invalid")
    comparison_manifest = str(ref.get("comparison_manifest", ""))
    upstream = ()
    if comparison_manifest:
        comparison_path = root / comparison_manifest
        try:
            comparison = json.loads(comparison_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as error:
            raise PacketBuildError("ref comparison is unreadable") from error
        upstream = _upstream_rows(comparison.get("upstream_changes"))
    excluded_rows = document.get("excluded_changes", [])
    if not isinstance(excluded_rows, list):
        raise PacketBuildError("packet excluded changes must be an array")
    excluded = _upstream_rows(excluded_rows)
    return RefPacketInput(
        str(ref.get("ref_kind", "")),
        str(ref.get("ref_name", "")),
        str(ref.get("from_sha", "")),
        str(ref.get("to_sha", "")),
        comparison_manifest,
        str(ref.get("prior_snapshot_manifest", "")),
        upstream,
        excluded,
    )


def _upstream_rows(rows: object) -> Tuple[UpstreamChange, ...]:
    if not isinstance(rows, list):
        raise PacketBuildError("packet upstream changes must be an array")
    changes = []
    for row in rows:
        if not isinstance(row, dict):
            raise PacketBuildError("packet upstream change row is invalid")
        values = tuple(row.get(key) for key in ("status", "old_path", "new_path"))
        if not all(isinstance(value, str) for value in values):
            raise PacketBuildError("packet upstream change row is invalid")
        changes.append(UpstreamChange(*values))
    return tuple(changes)


def _validate_work_items(
    report: GitHubReport,
    snapshot_paths: set,
    release_paths: Dict[str, ManifestInspection],
    comparison_paths: set,
    queued_packets: Dict[str, dict],
    errors: List[str],
) -> None:
    inspection = report.work_items
    if inspection.error:
        errors.append("work-item queue is invalid: " + inspection.error)
        return
    if inspection.exists:
        status = report.status_text
        packet_summaries = {}
        attachment_reading_counts = {}
        root = report.repositories.path.parents[2]
        for item in inspection.items:
            try:
                attachment_reading_counts[item.work_item_id] = len(
                    evidence_attachment_required_reading(root, item)
                )
            except (OSError, TypeError, ValueError) as error:
                attachment_reading_counts[item.work_item_id] = 0
                errors.append(
                    item.work_item_id
                    + ": invalid evidence attachment: "
                    + _bounded(error)
                )
            if not item.ingest_packet:
                continue
            try:
                summary = load_packet_summary(root, item.ingest_packet)
            except (OSError, ValueError):
                continue
            packet_summaries[item.work_item_id] = PacketStatusSummary(
                summary.packet_path,
                summary.priority,
                summary.required_reading_count
                + attachment_reading_counts[item.work_item_id],
                summary.unclassified_count,
                summary.evidence_gap_count,
            )
        if status.error:
            errors.append("tracking/github/status.md is unreadable: " + status.error)
        elif not status.exists or status.text != render_status(
            inspection.items, packet_summaries
        ):
            errors.append("tracking/github/status.md is stale")
    elif report.status_text.exists:
        errors.append("tracking/github/status.md exists without work-items.json")

    source_pages = {page.relative_path: page for page in report.source_pages}
    changelog_pages = {page.relative_path: page for page in report.changelog_pages}
    snapshots = {artifact.relative_path: artifact for artifact in report.snapshots}
    comparisons = {artifact.relative_path: artifact for artifact in report.comparisons}
    referenced_packets = set()
    referenced_attachments = set()
    for page in tuple(report.source_pages) + tuple(report.changelog_pages):
        if page.error:
            errors.append(page.relative_path + ": page is unreadable: " + page.error)
    repos = {repo.id: repo for repo in report.repositories.repositories}
    for item in inspection.items:
        referenced_attachments.update(item.evidence_attachments)
        if item.ingest_packet:
            referenced_packets.add(item.ingest_packet)
            packet = queued_packets.get(item.ingest_packet)
            if packet is None:
                errors.append(
                    item.work_item_id + ": missing or invalid ingest packet"
                )
            elif (
                packet.get("work_item_id") != item.work_item_id
                or packet.get("repository") != item.repo_id
                or packet.get("to_sha") != item.sha
            ):
                errors.append(
                    item.work_item_id + ": packet/work-item identity mismatch"
                )
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
        for change in item.ref_changes:
            if change.comparison_manifest and change.comparison_manifest not in comparison_paths:
                errors.append(
                    item.work_item_id
                    + ": missing comparison manifest "
                    + change.display_identity
                )
            elif change.comparison_manifest:
                comparison = comparisons.get(change.comparison_manifest)
                document = comparison.document if comparison is not None else None
                if document is not None and (
                    document.get("repository") != item.repo_id
                    or document.get("ref_kind") != change.ref_kind
                    or document.get("ref_name") != change.ref_name
                    or document.get("from_sha") != change.from_sha
                    or document.get("to_sha") != change.to_sha
                    or document.get("to_sha") != item.sha
                ):
                    errors.append(
                        item.work_item_id
                        + ": work-item ref comparison identity mismatch"
                    )
        if item.state != "ingested":
            continue
        repo = repos.get(item.repo_id)
        if repo is None:
            errors.append(item.work_item_id + ": repository is absent from registry")
            continue
        name = wiki_slug(item.repo_id.split("/", 1)[1])
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
        for change in item.ref_changes:
            if change.display_identity not in changelog.text:
                errors.append(
                    item.work_item_id
                    + ": changelog omits ref identity "
                    + change.display_identity
                )
            required = tuple(
                path
                for path in (
                    item.snapshot_manifest,
                    change.comparison_manifest,
                )
                if path
            )
            if any(path not in changelog.text for path in required):
                errors.append(
                    item.work_item_id
                    + ": changelog omits raw evidence link for "
                    + change.display_identity
                )
    for path in sorted(set(queued_packets) - referenced_packets):
        errors.append(path + ": queued packet has no work item")
    attachment_paths = {
        path.relative_to(root).as_posix()
        for path in root.glob(
            "tracking/github/repos/*/*/evidence-attachments/*/attachment.json"
        )
    }
    for path in sorted(attachment_paths - referenced_attachments):
        errors.append(path + ": evidence attachment has no work item")


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
