"""Deterministic review packets derived from accepted GitHub evidence."""

from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import tempfile
import threading
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

from github_canonical import canonical_json_bytes, safe_policy_path
from github_capsule_policy import (
    CAPSULE_ADAPTER,
    CapsuleConfig,
    build_effective_policy,
)
from github_capsule_selection import classify_excluded_categories
from github_pilot_store import UpstreamChange, _require_contained_storage_path
from github_registry import RepoConfig
from github_versions import parse_semver


_WORK_ITEM_ID = re.compile(r"^github-[0-9a-f]{20}$")
_OBJECT_ID = re.compile(r"^(?:[0-9a-f]{40}|[0-9a-f]{64})$")
_SOURCE_SUFFIXES = (
    ".c",
    ".cc",
    ".cpp",
    ".cs",
    ".go",
    ".h",
    ".hpp",
    ".java",
    ".js",
    ".jsx",
    ".kt",
    ".kts",
    ".mjs",
    ".cjs",
    ".m",
    ".mm",
    ".php",
    ".py",
    ".rb",
    ".rs",
    ".swift",
    ".ts",
    ".mts",
    ".cts",
    ".tsx",
)
_DOCUMENT_SUFFIXES = (".md", ".mdx", ".rst", ".txt")
_DEPENDENCY_FIELDS = (
    "dependencies",
    "optionalDependencies",
    "peerDependencies",
)
_PUBLIC_FIELDS = ("exports", "main", "module", "types", "typings", "bin")
_ROOT_CONTEXT = ("LICENSE", "LICENSE.md", "README.md", "package.json")
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
_REASON_ORDER = (
    "initial-package-baseline",
    "major-version-transition",
    "missing-prior-snapshot",
    "capsule-policy-changed",
    "public-api-incompatible-change",
    "unbounded-security-impact",
    "release-notes-revision",
    "contained-patch-release",
    "contained-minor-release",
    "public-api-addition",
    "dependency-change",
    "security-review-signal",
    "payment-review-signal",
    "policy-history-bootstrap",
)
_PACKET_THREAD_LOCK = threading.RLock()


class PacketBuildError(ValueError):
    """Packet inputs cannot establish a bounded review scope."""


@dataclass(frozen=True)
class PackagePacketInput:
    package: str
    from_version: str
    to_version: str
    from_sha: str
    to_sha: str
    release_manifest: str
    comparison_manifest: str
    prior_snapshot_manifest: str
    upstream_changes: Tuple[UpstreamChange, ...]
    release_notes_revision: bool = False


@dataclass(frozen=True)
class PacketRecommendation:
    mode: str
    priority: str
    reasons: Tuple[str, ...]


@dataclass(frozen=True)
class IngestPacket:
    document: dict
    markdown: bytes


@dataclass(frozen=True)
class PacketSummary:
    packet_path: str
    priority: str
    required_reading_count: int
    unclassified_count: int
    evidence_gap_count: int


@dataclass(frozen=True)
class _LoadedSnapshot:
    relative_path: str
    manifest: dict
    manifest_sha256: str
    files: Mapping[str, dict]
    excluded: Mapping[str, str]


def build_ingest_packet(
    root: Path,
    config: RepoConfig,
    work_item_id: str,
    snapshot_manifest: str,
    package_inputs: Sequence[PackagePacketInput],
    packet_kind: str,
    wiki_context_override: Optional[Sequence[str]] = None,
    expected_wiki_targets_override: Optional[Sequence[str]] = None,
) -> IngestPacket:
    """Build one canonical packet without publishing or changing queue state."""
    root = Path(root).resolve()
    _validate_config(config)
    if packet_kind not in ("queued", "ad-hoc"):
        raise PacketBuildError("packet kind must be queued or ad-hoc")
    if packet_kind == "queued":
        if _WORK_ITEM_ID.fullmatch(work_item_id) is None:
            raise PacketBuildError("queued packet work-item ID is invalid")
    elif work_item_id:
        raise PacketBuildError("ad-hoc packet must not carry a work-item ID")
    inputs = tuple(sorted(package_inputs, key=lambda item: item.package))
    if not inputs or any(not isinstance(item, PackagePacketInput) for item in inputs):
        raise PacketBuildError("packet requires package inputs")
    if len({item.package for item in inputs}) != len(inputs):
        raise PacketBuildError("packet package inputs must be unique")

    current = _load_snapshot(root, snapshot_manifest, config.id)
    capsule = config.capsules[0]
    policy_hash = build_effective_policy(capsule, (), (), ()).policy_hash
    package_documents = []
    all_required = set()
    all_unclassified = []
    all_gaps = []
    for item in inputs:
        package_document = _build_package(
            root,
            config,
            capsule,
            current,
            item,
            policy_hash,
        )
        package_documents.append(package_document)
        all_required.update(package_document["required_reading"])
        all_unclassified.extend(
            item["path"] for item in package_document["unclassified_changes"]
        )
        all_gaps.extend(item["path"] for item in package_document["evidence_gaps"])

    if all_gaps:
        raise PacketBuildError(
            "blocking evidence gap: " + sorted(set(all_gaps))[0]
        )
    if all_unclassified:
        raise PacketBuildError(
            "unclassified retained evidence: " + sorted(set(all_unclassified))[0]
        )

    recommendation = _aggregate_recommendation(package_documents)
    if (wiki_context_override is None) != (
        expected_wiki_targets_override is None
    ):
        raise PacketBuildError("wiki generation context override is incomplete")
    if wiki_context_override is None:
        wiki_context, expected_targets = _wiki_paths(root, config)
    else:
        wiki_context, expected_targets = _validate_wiki_paths(
            root,
            config,
            wiki_context_override,
            expected_wiki_targets_override or (),
        )
    all_required.update(wiki_context)
    required = tuple(sorted(all_required))
    _enforce_packet_budget(root, capsule, required)
    unchanged_count = sum(
        package["retained_evidence"]["counts"]["unchanged"]
        for package in package_documents
    )
    document = {
        "capsule_policy_sha256": policy_hash,
        "collection_date": str(current.manifest["collected_date"]),
        "evidence_gaps": [],
        "expected_wiki_targets": list(expected_targets),
        "format_version": 1,
        "markdown_sha256": "",
        "packet_kind": packet_kind,
        "packages": package_documents,
        "recommendation": _recommendation_dict(recommendation),
        "repository": config.id,
        "required_reading": list(required),
        "snapshot_manifest": current.relative_path,
        "snapshot_sha256": current.manifest_sha256,
        "to_sha": str(current.manifest["sha"]),
        "unchanged_evidence_count": unchanged_count,
        "unclassified_changes": [],
        "wiki_context": list(wiki_context),
        "work_item_id": work_item_id,
    }
    markdown = _render_markdown(document)
    document["markdown_sha256"] = hashlib.sha256(markdown).hexdigest()
    return IngestPacket(document, markdown)


def publish_queued_packet(
    root: Path,
    config: RepoConfig,
    packet: IngestPacket,
) -> Path:
    """Publish one queued packet directory as an atomic evidence unit."""
    root = Path(root).resolve()
    _validate_config(config)
    json_bytes, markdown_bytes = _packet_bytes(packet, "queued")
    work_item_id = str(packet.document["work_item_id"])
    repository_name = config.id.split("/", 1)[1]
    repository_root = (
        root
        / "tracking"
        / "github"
        / "repos"
        / config.company
        / repository_name
    )
    _require_packet_storage(root, repository_root)
    destination = repository_root / "ingest-packets" / work_item_id
    with _PACKET_THREAD_LOCK:
        existing = _existing_packet_pair(
            destination / "packet.json",
            destination / "packet.md",
            json_bytes,
            markdown_bytes,
        )
        if existing:
            return destination / "packet.json"
        destination.parent.mkdir(parents=True, exist_ok=True)
        staging = Path(
            tempfile.mkdtemp(prefix=".packet-", dir=str(destination.parent))
        )
        try:
            _write_atomic(staging / "packet.md", markdown_bytes)
            _write_atomic(staging / "packet.json", json_bytes)
            os.replace(str(staging), str(destination))
        except Exception:
            shutil.rmtree(staging, ignore_errors=True)
            if _existing_packet_pair(
                destination / "packet.json",
                destination / "packet.md",
                json_bytes,
                markdown_bytes,
            ):
                return destination / "packet.json"
            raise
    return destination / "packet.json"


def publish_review_packet(
    comparison_directory: Path,
    packet: IngestPacket,
) -> Path:
    """Publish an ad hoc review pair beside an accepted comparison."""
    comparison_directory = Path(comparison_directory)
    if (
        not comparison_directory.is_dir()
        or comparison_directory.is_symlink()
        or not (comparison_directory / "comparison.json").is_file()
        or (comparison_directory / "comparison.json").is_symlink()
    ):
        raise PacketBuildError("comparison directory is unsafe")
    json_bytes, markdown_bytes = _packet_bytes(packet, "ad-hoc")
    json_path = comparison_directory / "review-packet.json"
    markdown_path = comparison_directory / "review-packet.md"
    with _PACKET_THREAD_LOCK:
        if _existing_packet_pair(
            json_path, markdown_path, json_bytes, markdown_bytes
        ):
            return json_path
        created = []
        try:
            _write_atomic(markdown_path, markdown_bytes)
            created.append(markdown_path)
            _write_atomic(json_path, json_bytes)
            created.append(json_path)
        except Exception:
            for path in reversed(created):
                try:
                    path.unlink()
                except FileNotFoundError:
                    pass
            raise
    return json_path


def load_packet_summary(root: Path, packet_path: str) -> PacketSummary:
    """Load the bounded operator summary from one canonical packet."""
    _, document, content = _load_json(Path(root).resolve(), packet_path)
    if canonical_json_bytes(document) + b"\n" != content:
        raise PacketBuildError("packet JSON is not canonical")
    recommendation = document.get("recommendation")
    required = document.get("required_reading")
    unclassified = document.get("unclassified_changes")
    gaps = document.get("evidence_gaps")
    if (
        not isinstance(recommendation, dict)
        or recommendation.get("priority") not in ("normal", "high")
        or not isinstance(required, list)
        or not isinstance(unclassified, list)
        or not isinstance(gaps, list)
    ):
        raise PacketBuildError("packet status summary is invalid")
    return PacketSummary(
        packet_path,
        str(recommendation["priority"]),
        len(required),
        len(unclassified),
        len(gaps),
    )


def _packet_bytes(
    packet: IngestPacket, expected_kind: str
) -> Tuple[bytes, bytes]:
    if not isinstance(packet, IngestPacket):
        raise TypeError("packet must be IngestPacket")
    document = packet.document
    if not isinstance(document, dict) or document.get("packet_kind") != expected_kind:
        raise PacketBuildError("packet kind does not match publication target")
    if document.get("repository") is None:
        raise PacketBuildError("packet repository identity is missing")
    markdown = packet.markdown
    if not isinstance(markdown, bytes):
        raise PacketBuildError("packet Markdown must be bytes")
    if hashlib.sha256(markdown).hexdigest() != document.get("markdown_sha256"):
        raise PacketBuildError("packet Markdown hash mismatch")
    return canonical_json_bytes(document) + b"\n", markdown


def _existing_packet_pair(
    json_path: Path,
    markdown_path: Path,
    expected_json: bytes,
    expected_markdown: bytes,
) -> bool:
    exists = (json_path.exists(), markdown_path.exists())
    if not any(exists):
        return False
    if (
        not all(exists)
        or json_path.is_symlink()
        or markdown_path.is_symlink()
        or not json_path.is_file()
        or not markdown_path.is_file()
    ):
        raise PacketBuildError("packet destination is incomplete or unsafe")
    if (
        json_path.read_bytes() != expected_json
        or markdown_path.read_bytes() != expected_markdown
    ):
        raise PacketBuildError("packet destination conflicts with generated evidence")
    return True


def _require_packet_storage(root: Path, candidate: Path) -> None:
    try:
        _require_contained_storage_path(root, candidate)
    except ValueError as error:
        raise PacketBuildError("repository storage path is unsafe") from error


def _write_atomic(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=".tmp-", dir=str(path.parent))
    try:
        with os.fdopen(descriptor, "wb") as output:
            output.write(content)
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary, path)
    except Exception:
        try:
            os.close(descriptor)
        except OSError:
            pass
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def _build_package(
    root: Path,
    config: RepoConfig,
    capsule: CapsuleConfig,
    current: _LoadedSnapshot,
    item: PackagePacketInput,
    policy_hash: str,
) -> dict:
    _validate_package_input(item, config.id, current.manifest["sha"])
    release = _load_release(root, item.release_manifest, config.id, item)
    prior = (
        _load_snapshot(root, item.prior_snapshot_manifest, config.id)
        if item.prior_snapshot_manifest
        else None
    )
    if prior is not None and prior.manifest["sha"] != item.from_sha:
        raise PacketBuildError("prior snapshot SHA mismatch")
    comparison = (
        _load_comparison(root, item.comparison_manifest, config.id, item)
        if item.comparison_manifest
        else None
    )
    if item.from_version and prior is not None and comparison is None and not item.release_notes_revision:
        raise PacketBuildError("non-baseline packet requires comparison evidence")

    retained = _retained_diff(prior, current, item.upstream_changes)
    package_paths = _package_roots(item.package, prior, current)
    upstream, gaps = _upstream_dispositions(
        item.upstream_changes,
        prior,
        current,
        capsule,
        package_paths,
        item.package,
    )
    changed_rows = [
        row for row in retained["files"] if row["status"] != "unchanged"
    ]
    unclassified = [
        {"path": row["path"], "status": row["status"]}
        for row in changed_rows
        if row["classification"] == "unclassified"
    ]
    prior_manifest = _package_manifest(root, prior, item.package) if prior else {}
    current_manifest = _package_manifest(root, current, item.package)
    if prior_manifest and prior_manifest.get("version") != item.from_version:
        raise PacketBuildError("prior package manifest version mismatch")
    if current_manifest.get("version") != item.to_version:
        raise PacketBuildError("current package manifest version mismatch")
    dependency_changes = _dependency_changes(prior_manifest, current_manifest)
    public_api_changes = _public_api_changes(prior_manifest, current_manifest)
    notes_path = str(PurePosixPath(item.release_manifest).parent / "release-notes.md")
    required = _required_reading(
        root,
        item,
        current,
        prior,
        retained,
        notes_path,
    )
    recommendation = _recommend(
        root,
        config,
        item,
        release["notes"],
        public_api_changes,
        dependency_changes,
        upstream,
        policy_hash,
        prior is not None,
    )
    return {
        "comparison_manifest": item.comparison_manifest,
        "dependency_changes": dependency_changes,
        "evidence_gaps": gaps,
        "from_sha": item.from_sha,
        "from_version": item.from_version,
        "package": item.package,
        "prior_snapshot_manifest": item.prior_snapshot_manifest,
        "public_api_changes": public_api_changes,
        "recommendation": _recommendation_dict(recommendation),
        "release_manifest": item.release_manifest,
        "release_notes_path": notes_path,
        "required_reading": list(required),
        "retained_evidence": retained,
        "to_sha": item.to_sha,
        "to_version": item.to_version,
        "unclassified_changes": unclassified,
        "upstream_changes": upstream,
    }


def _load_snapshot(root: Path, relative: str, repository: str) -> _LoadedSnapshot:
    path, document, content = _load_json(root, relative)
    required = {
        "collected_date",
        "excluded",
        "files",
        "format_version",
        "repository",
        "sha",
        "triggering_refs",
    }
    if document.get("format_version") == 2:
        required |= {"author_date", "commit_date"}
    if set(document) != required or document.get("format_version") not in (1, 2):
        raise PacketBuildError("snapshot manifest shape is invalid")
    if document.get("repository") != repository or not _valid_sha(document.get("sha")):
        raise PacketBuildError("snapshot identity is invalid")
    rows = document.get("files")
    excluded_rows = document.get("excluded")
    if not isinstance(rows, list) or not isinstance(excluded_rows, list):
        raise PacketBuildError("snapshot evidence rows are invalid")
    files: Dict[str, dict] = {}
    for row in rows:
        if not isinstance(row, dict) or set(row) != _SNAPSHOT_FILE_FIELDS:
            raise PacketBuildError("snapshot file row is invalid")
        file_path = row.get("path")
        digest = row.get("sha256")
        size = row.get("size")
        if (
            not isinstance(file_path, str)
            or not safe_policy_path(file_path)
            or not isinstance(digest, str)
            or re.fullmatch(r"[0-9a-f]{64}", digest) is None
            or not isinstance(size, int)
            or size < 0
            or file_path in files
        ):
            raise PacketBuildError("snapshot file row is invalid")
        saved = _resolve_file(root, str(PurePosixPath(relative).parent / "files" / file_path))
        payload = saved.read_bytes()
        if len(payload) != size or hashlib.sha256(payload).hexdigest() != digest:
            raise PacketBuildError("snapshot file hash mismatch: " + file_path)
        files[file_path] = row
    excluded: Dict[str, str] = {}
    excluded_pairs = set()
    for row in excluded_rows:
        pair = (
            row.get("path"),
            row.get("reason"),
        ) if isinstance(row, dict) else None
        if (
            not isinstance(row, dict)
            or set(row) != {"path", "reason"}
            or not isinstance(row.get("path"), str)
            or not safe_policy_path(row["path"])
            or not isinstance(row.get("reason"), str)
            or not row["reason"]
            or pair in excluded_pairs
        ):
            raise PacketBuildError("snapshot exclusion row is invalid")
        excluded_pairs.add(pair)
        excluded.setdefault(row["path"], row["reason"])
    return _LoadedSnapshot(
        relative,
        document,
        hashlib.sha256(content).hexdigest(),
        files,
        excluded,
    )


def _load_release(
    root: Path,
    relative: str,
    repository: str,
    item: PackagePacketInput,
) -> dict:
    path, document, _ = _load_json(root, relative)
    if set(document) != _RELEASE_FIELDS or document.get("format_version") != 1:
        raise PacketBuildError("release manifest shape is invalid")
    identity = (
        document.get("repository"),
        document.get("package"),
        document.get("version"),
        document.get("sha"),
    )
    expected = (repository, item.package, item.to_version, item.to_sha)
    if identity != expected:
        raise PacketBuildError("release manifest identity mismatch")
    notes_path = path.parent / "release-notes.md"
    if not notes_path.is_file() or notes_path.is_symlink():
        raise PacketBuildError("release notes are missing")
    notes_bytes = notes_path.read_bytes()
    if hashlib.sha256(notes_bytes).hexdigest() != document.get("notes_sha256"):
        raise PacketBuildError("release notes hash mismatch")
    try:
        notes = notes_bytes.decode("utf-8")
    except UnicodeDecodeError:
        raise PacketBuildError("release notes are not UTF-8") from None
    return {"manifest": document, "notes": notes}


def _load_comparison(
    root: Path,
    relative: str,
    repository: str,
    item: PackagePacketInput,
) -> dict:
    path, document, _ = _load_json(root, relative)
    version = document.get("format_version")
    fields = _COMPARISON_FIELDS | ({"upstream_changes"} if version == 2 else set())
    if set(document) != fields or version not in (1, 2):
        raise PacketBuildError("comparison manifest shape is invalid")
    identity = (
        document.get("repository"),
        document.get("package"),
        document.get("from_version"),
        document.get("to_version"),
        document.get("from_sha"),
        document.get("to_sha"),
    )
    expected = (
        repository,
        item.package,
        item.from_version,
        item.to_version,
        item.from_sha,
        item.to_sha,
    )
    if identity != expected:
        raise PacketBuildError("comparison manifest identity mismatch")
    for name, field in (
        ("comparison.md", "markdown_sha256"),
        ("diff.patch", "patch_sha256"),
    ):
        evidence = path.parent / name
        if not evidence.is_file() or evidence.is_symlink():
            raise PacketBuildError("comparison evidence is missing")
        if hashlib.sha256(evidence.read_bytes()).hexdigest() != document.get(field):
            raise PacketBuildError("comparison evidence hash mismatch")
    return document


def _load_json(root: Path, relative: str) -> Tuple[Path, dict, bytes]:
    path = _resolve_file(root, relative)
    content = path.read_bytes()
    try:
        value = json.loads(
            content.decode("utf-8"),
            object_pairs_hook=_reject_duplicates,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as error:
        raise PacketBuildError("JSON evidence is invalid: " + str(error)) from None
    if not isinstance(value, dict):
        raise PacketBuildError("JSON evidence root must be an object")
    return path, value, content


def _resolve_file(root: Path, relative: str) -> Path:
    if not isinstance(relative, str) or not safe_policy_path(relative):
        raise PacketBuildError("evidence path is unsafe")
    candidate = root / PurePosixPath(relative)
    try:
        resolved = candidate.resolve(strict=True)
    except OSError:
        raise PacketBuildError("evidence path is missing: " + relative) from None
    try:
        resolved.relative_to(root)
    except ValueError:
        raise PacketBuildError("evidence path escapes repository root") from None
    if not resolved.is_file() or candidate.is_symlink():
        raise PacketBuildError("evidence path is not a regular file")
    return resolved


def _retained_diff(
    prior: Optional[_LoadedSnapshot],
    current: _LoadedSnapshot,
    upstream_changes: Sequence[UpstreamChange],
) -> dict:
    if prior is None:
        files = [
            _retained_row(path, "added", None, row, _classify_file(path, row))
            for path, row in sorted(current.files.items())
        ]
        return {
            "counts": {
                "added": len(files),
                "modified": 0,
                "removed": 0,
                "renamed": 0,
                "unchanged": 0,
            },
            "files": files,
        }
    prior_remaining = set(prior.files)
    current_remaining = set(current.files)
    rows = []
    for change in sorted(
        upstream_changes,
        key=lambda value: (value.new_path or value.old_path, value.old_path),
    ):
        if change.status != "renamed":
            continue
        old = prior.files.get(change.old_path)
        new = current.files.get(change.new_path)
        if old is None or new is None or old["sha256"] != new["sha256"]:
            continue
        rows.append(
            _retained_row(
                change.new_path,
                "renamed",
                old,
                new,
                _classify_file(change.new_path, new),
                old_path=change.old_path,
            )
        )
        prior_remaining.discard(change.old_path)
        current_remaining.discard(change.new_path)
    for path in sorted(prior_remaining | current_remaining):
        old = prior.files.get(path)
        new = current.files.get(path)
        if old is None:
            status = "added"
            classification = _classify_file(path, new)
        elif new is None:
            status = "removed"
            classification = _classify_file(path, old)
        elif old["sha256"] == new["sha256"]:
            status = "unchanged"
            classification = _classify_file(path, new)
        else:
            status = "modified"
            classification = _classify_file(path, new)
        rows.append(_retained_row(path, status, old, new, classification))
    rows.sort(key=lambda row: row["path"])
    counts = {
        status: sum(row["status"] == status for row in rows)
        for status in ("added", "modified", "removed", "renamed", "unchanged")
    }
    return {"counts": counts, "files": rows}


def _retained_row(
    path: str,
    status: str,
    old: Optional[dict],
    new: Optional[dict],
    classification: str,
    old_path: str = "",
) -> dict:
    return {
        "affected_areas": list(_affected_areas(path)),
        "classification": classification,
        "from_sha256": old["sha256"] if old else "",
        "old_path": old_path,
        "path": path,
        "status": status,
        "to_sha256": new["sha256"] if new else "",
    }


def _classify_file(path: str, row: Mapping[str, Any]) -> str:
    lowered = path.lower()
    filename = lowered.rsplit("/", 1)[-1]
    if filename == "package.json":
        return "package-manifest"
    if filename == "tsconfig.json" or (
        filename.startswith("tsconfig.") and filename.endswith(".json")
    ):
        return "build-configuration"
    if filename in ("build.gradle", "gradle.properties") or filename.endswith(
        (".podspec", ".pbxproj", ".xcscheme", ".xml")
    ):
        return "build-configuration"
    if (
        filename == ".eslintrc"
        or filename.startswith(".eslintrc.")
        or filename.startswith("eslint.config.")
    ):
        return "build-configuration"
    if filename.startswith(("changelog", "history", "releases")):
        return "release-history"
    if row.get("purpose") == "repository-context" or row.get(
        "classification_reason"
    ) == "repository-context":
        return "repository-context"
    if classify_excluded_categories(path, ("stories",)):
        return "story"
    segments = lowered.split("/")
    if any(segment in ("example", "examples", "demo", "demos", "sample", "samples") for segment in segments):
        return "example"
    if any(segment in ("locale", "locales", "i18n", "translations") for segment in segments):
        return "translation"
    if lowered.endswith(_DOCUMENT_SUFFIXES):
        return "documentation"
    if lowered.endswith(_SOURCE_SUFFIXES):
        return "public-source"
    return "unclassified"


def _upstream_dispositions(
    changes: Sequence[UpstreamChange],
    prior: Optional[_LoadedSnapshot],
    current: _LoadedSnapshot,
    capsule: CapsuleConfig,
    package_roots: Sequence[str],
    package: str,
) -> Tuple[List[dict], List[dict]]:
    prior_files = prior.files if prior else {}
    prior_excluded = prior.excluded if prior else {}
    excluded = dict(prior_excluded)
    excluded.update(current.excluded)
    rows = []
    gaps = []
    for change in sorted(
        set(changes),
        key=lambda item: (item.new_path or item.old_path, item.old_path, item.status),
    ):
        paths = tuple(path for path in (change.old_path, change.new_path) if path)
        retained = any(path in prior_files or path in current.files for path in paths)
        exclusion = next((excluded[path] for path in paths if path in excluded), "")
        if retained:
            disposition = "retained-evidence"
            reason = "snapshot-file"
        elif exclusion:
            disposition = "intentional-policy-exclusion"
            reason = exclusion
        elif any(
            _required_by_policy(path, package_roots, capsule, package)
            for path in paths
        ):
            disposition = "blocking-evidence-gap"
            reason = "required-path-missing-from-snapshot"
            gaps.append({"path": change.new_path or change.old_path, "reason": reason})
        else:
            disposition = "intentional-policy-exclusion"
            reason = "outside-capsule-policy"
        rows.append(
            {
                "affected_areas": list(
                    _affected_areas(change.new_path or change.old_path)
                ),
                "disposition": disposition,
                "new_path": change.new_path,
                "old_path": change.old_path,
                "reason": reason,
                "status": change.status,
            }
        )
    return rows, gaps


def _required_by_policy(
    path: str,
    package_roots: Sequence[str],
    capsule: CapsuleConfig,
    package: str,
) -> bool:
    for package_root in package_roots:
        relative = (
            path[len(package_root) + 1 :]
            if package_root and path.startswith(package_root + "/")
            else path
            if not package_root
            else ""
        )
        if not relative:
            continue
        if relative == "package.json":
            return True
        roots = capsule.default_required_roots
        includes = capsule.include_paths
        override = next(
            (row for row in capsule.package_overrides if row.name == package),
            None,
        )
        if override is not None:
            roots = override.required_roots
            includes = override.include_paths
        if any(_within(relative, selected) for selected in tuple(roots) + tuple(includes)):
            categories = classify_excluded_categories(
                relative, capsule.excluded_categories
            )
            return not categories
    return False


def _package_roots(
    package: str,
    prior: Optional[_LoadedSnapshot],
    current: _LoadedSnapshot,
) -> Tuple[str, ...]:
    paths = []
    for snapshot in tuple(row for row in (prior, current) if row is not None):
        for path, metadata in snapshot.files.items():
            if metadata.get("package") == package and path.endswith("package.json"):
                root = path[: -len("/package.json")] if path != "package.json" else ""
                paths.append(root)
    return tuple(sorted(set(paths)))


def _package_manifest(
    root: Path, snapshot: _LoadedSnapshot, package: str
) -> dict:
    matches = [
        path
        for path, row in snapshot.files.items()
        if row.get("package") == package and path.endswith("package.json")
    ]
    if len(matches) != 1:
        raise PacketBuildError("package snapshot must contain one package manifest")
    relative = str(
        PurePosixPath(snapshot.relative_path).parent / "files" / matches[0]
    )
    path = _resolve_file(root, relative)
    try:
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_reject_duplicates)
    except (UnicodeError, json.JSONDecodeError, ValueError) as error:
        raise PacketBuildError("package manifest is invalid: " + str(error)) from None
    if not isinstance(value, dict) or value.get("name") != package:
        raise PacketBuildError("package manifest identity mismatch")
    return value


def _dependency_changes(prior: Mapping[str, Any], current: Mapping[str, Any]) -> List[dict]:
    rows = []
    for field in _DEPENDENCY_FIELDS:
        old = _string_map(prior.get(field, {}), field)
        new = _string_map(current.get(field, {}), field)
        for name in sorted(set(old) | set(new)):
            if old.get(name) == new.get(name):
                continue
            status = "added" if name not in old else "removed" if name not in new else "changed"
            rows.append(
                {
                    "field": field,
                    "from": old.get(name, ""),
                    "name": name,
                    "status": status,
                    "to": new.get(name, ""),
                }
            )
    return rows


def _public_api_changes(prior: Mapping[str, Any], current: Mapping[str, Any]) -> List[dict]:
    rows = []
    for field in _PUBLIC_FIELDS:
        old = _flatten_public_field(field, prior.get(field))
        new = _flatten_public_field(field, current.get(field))
        for pointer in sorted(set(old) | set(new)):
            if old.get(pointer) == new.get(pointer):
                continue
            status = "added" if pointer not in old else "removed" if pointer not in new else "retargeted"
            rows.append(
                {
                    "compatibility": "compatible" if status == "added" else "incompatible",
                    "field": field,
                    "from": old.get(pointer, ""),
                    "path": pointer,
                    "status": status,
                    "to": new.get(pointer, ""),
                }
            )
    return rows


def _flatten_public_field(field: str, value: Any) -> Dict[str, str]:
    if value is None:
        return {}
    if field in ("main", "module", "types", "typings"):
        if not isinstance(value, str):
            raise PacketBuildError("unsupported public API structure: " + field)
        return {"/" + field: value}
    if field == "bin" and isinstance(value, str):
        return {"/bin": value}
    if not isinstance(value, dict):
        raise PacketBuildError("unsupported public API structure: " + field)
    result: Dict[str, str] = {}

    def visit(node: Any, pointer: str) -> None:
        if isinstance(node, str):
            result[pointer] = node
            return
        if not isinstance(node, dict) or not node:
            raise PacketBuildError("unsupported public API structure: " + field)
        for key in sorted(node):
            if not isinstance(key, str) or not key:
                raise PacketBuildError("unsupported public API structure: " + field)
            escaped = key.replace("~", "~0").replace("/", "~1")
            visit(node[key], pointer + "/" + escaped)

    visit(value, "/" + field)
    return result


def _required_reading(
    root: Path,
    item: PackagePacketInput,
    current: _LoadedSnapshot,
    prior: Optional[_LoadedSnapshot],
    retained: dict,
    notes_path: str,
) -> Tuple[str, ...]:
    required = {item.release_manifest, notes_path, current.relative_path}
    if item.comparison_manifest:
        comparison_root = PurePosixPath(item.comparison_manifest).parent
        required.update(
            (
                item.comparison_manifest,
                str(comparison_root / "comparison.md"),
                str(comparison_root / "diff.patch"),
            )
        )
    if prior is not None:
        required.add(prior.relative_path)
    rows = retained["files"]
    for row in rows:
        if prior is None or row["status"] != "unchanged":
            snapshot = prior if row["status"] == "removed" else current
            path = row["path"]
            required.add(
                str(PurePosixPath(snapshot.relative_path).parent / "files" / path)
            )
    for value in required:
        _resolve_file(root, value)
    return tuple(sorted(required))


def _recommend(
    root: Path,
    config: RepoConfig,
    item: PackagePacketInput,
    notes: str,
    public_api_changes: Sequence[dict],
    dependency_changes: Sequence[dict],
    upstream_changes: Sequence[dict],
    policy_hash: str,
    has_prior: bool,
) -> PacketRecommendation:
    current = parse_semver(item.to_version)
    prior = parse_semver(item.from_version) if item.from_version else None
    if current is None or not current.is_exact or item.from_version and (
        prior is None or not prior.is_exact
    ):
        raise PacketBuildError("packet versions must be exact semantic versions")
    reasons = []
    mode = "delta"
    priority = "normal"
    if prior is None:
        mode = "full"
        reasons.append("initial-package-baseline")
    elif prior.major != current.major:
        mode = "full"
        reasons.append("major-version-transition")
    if item.from_version and not has_prior:
        mode = "full"
        reasons.append("missing-prior-snapshot")
    prior_policy = _prior_packet_policy(root, config, item)
    if prior_policy and prior_policy != policy_hash:
        mode = "full"
        reasons.append("capsule-policy-changed")
    elif item.from_version and not prior_policy:
        priority = "high"
        reasons.append("policy-history-bootstrap")
    if any(row["compatibility"] == "incompatible" for row in public_api_changes):
        mode = "full"
        reasons.append("public-api-incompatible-change")
    elif public_api_changes:
        priority = "high"
        reasons.append("public-api-addition")
    if dependency_changes:
        reasons.append("dependency-change")
    lowered = notes.lower()
    security = "security" in lowered or "cve-" in lowered
    if security:
        priority = "high"
        reasons.append("security-review-signal")
        if any(
            row["disposition"] == "intentional-policy-exclusion"
            and row["reason"] == "outside-capsule-policy"
            for row in upstream_changes
        ):
            mode = "full"
            reasons.append("unbounded-security-impact")
    if any(word in lowered for word in ("payment", "checkout", "vault", "venmo", "3d secure")):
        priority = "high"
        reasons.append("payment-review-signal")
    if item.release_notes_revision:
        reasons.append("release-notes-revision")
    elif prior is not None and prior.major == current.major:
        reasons.append(
            "contained-patch-release"
            if prior.minor == current.minor
            else "contained-minor-release"
        )
    ordered = tuple(code for code in _REASON_ORDER if code in reasons)
    return PacketRecommendation(mode, priority, ordered)


def _prior_packet_policy(
    root: Path, config: RepoConfig, item: PackagePacketInput
) -> str:
    packet_root = (
        root
        / "tracking/github/repos"
        / config.company
        / config.id.split("/", 1)[1]
        / "ingest-packets"
    )
    if not packet_root.is_dir():
        return ""
    matches = []
    for path in sorted(packet_root.glob("*/packet.json")):
        try:
            document = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError):
            continue
        if document.get("repository") != config.id:
            continue
        for package in document.get("packages", []):
            if (
                isinstance(package, dict)
                and package.get("package") == item.package
                and package.get("to_version") == item.from_version
                and package.get("to_sha") == item.from_sha
            ):
                value = document.get("capsule_policy_sha256")
                if isinstance(value, str):
                    matches.append(value)
    if len(set(matches)) > 1:
        raise PacketBuildError("prior packet policy identity is ambiguous")
    return matches[0] if matches else ""


def _aggregate_recommendation(packages: Sequence[dict]) -> PacketRecommendation:
    modes = [row["recommendation"]["mode"] for row in packages]
    priorities = [row["recommendation"]["priority"] for row in packages]
    reasons = {
        reason
        for row in packages
        for reason in row["recommendation"]["reasons"]
    }
    return PacketRecommendation(
        "full" if "full" in modes else "delta",
        "high" if "high" in priorities else "normal",
        tuple(reason for reason in _REASON_ORDER if reason in reasons),
    )


def _wiki_paths(root: Path, config: RepoConfig) -> Tuple[Tuple[str, ...], Tuple[str, ...]]:
    repo = config.id.split("/", 1)[1]
    paths = (
        "wiki/sources/"
        + config.company
        + "/github/source-github-"
        + repo
        + ".md",
        "wiki/sources/"
        + config.company
        + "/github/changelog-github-"
        + repo
        + ".md",
    )
    context = tuple(path for path in paths if (root / path).is_file())
    expected = tuple(path for path in paths if path not in context)
    return context, expected


def _validate_wiki_paths(
    root: Path,
    config: RepoConfig,
    context: Sequence[str],
    expected: Sequence[str],
) -> Tuple[Tuple[str, ...], Tuple[str, ...]]:
    stored_context = tuple(context)
    stored_expected = tuple(expected)
    current_context, current_expected = _wiki_paths(root, config)
    canonical = set(current_context) | set(current_expected)
    if (
        len(stored_context) != len(set(stored_context))
        or len(stored_expected) != len(set(stored_expected))
        or set(stored_context) & set(stored_expected)
        or set(stored_context) | set(stored_expected) != canonical
    ):
        raise PacketBuildError("wiki generation context is invalid")
    for path in stored_context:
        _resolve_file(root, path)
    return stored_context, stored_expected


def _enforce_packet_budget(
    root: Path, capsule: CapsuleConfig, required: Sequence[str]
) -> None:
    if len(required) > capsule.max_packet_files:
        raise PacketBuildError("packet budget exceeds max_packet_files")
    size = sum(_resolve_file(root, path).stat().st_size for path in required)
    if size > capsule.max_packet_utf8_bytes:
        raise PacketBuildError("packet budget exceeds max_packet_utf8_bytes")


def _render_markdown(document: dict) -> bytes:
    recommendation = document["recommendation"]
    lines = [
        "# GitHub ingest packet",
        "",
        "- Repository: `" + document["repository"] + "`",
        "- Work item: `" + (document["work_item_id"] or "ad-hoc") + "`",
        "- Snapshot: `" + document["snapshot_manifest"] + "`",
        "- Recommended mode: `" + recommendation["mode"] + "`",
        "- Review priority: `" + recommendation["priority"] + "`",
        "",
    ]
    for package in document["packages"]:
        lines.extend(
            [
                "## `" + package["package"] + "`",
                "",
                "- Version: `"
                + (package["from_version"] or "baseline")
                + "` -> `"
                + package["to_version"]
                + "`",
                "- Recommendation: `"
                + package["recommendation"]["mode"]
                + "` / `"
                + package["recommendation"]["priority"]
                + "`",
                "- Unchanged retained files: `"
                + str(package["retained_evidence"]["counts"]["unchanged"])
                + "`",
                "",
                "### Required reading",
                "",
            ]
        )
        lines.extend("- `" + path + "`" for path in package["required_reading"])
        lines.extend(["", "### Upstream changes", ""])
        if package["upstream_changes"]:
            for row in package["upstream_changes"]:
                path = row["new_path"] or row["old_path"]
                lines.append(
                    "- `"
                    + row["status"]
                    + "` `"
                    + path
                    + "`: `"
                    + row["disposition"]
                    + "`"
                )
        else:
            lines.append("- None")
        lines.append("")
    return ("\n".join(lines).rstrip() + "\n").encode("utf-8")


def _validate_config(config: RepoConfig) -> None:
    if not isinstance(config, RepoConfig) or len(config.capsules) != 1:
        raise PacketBuildError("packet requires one repository capsule")
    if config.capsules[0].adapter != CAPSULE_ADAPTER:
        raise PacketBuildError("packet adapter is unsupported")


def _validate_package_input(
    item: PackagePacketInput, repository: str, current_sha: Any
) -> None:
    if not _valid_sha(item.to_sha) or item.to_sha != current_sha:
        raise PacketBuildError("package target SHA is invalid")
    if item.from_sha and not _valid_sha(item.from_sha):
        raise PacketBuildError("package prior SHA is invalid")
    if bool(item.from_version) != bool(item.from_sha):
        raise PacketBuildError("package prior identity is incomplete")
    for change in item.upstream_changes:
        if not isinstance(change, UpstreamChange):
            raise PacketBuildError("package upstream changes are invalid")
        valid_shape = (
            change.status == "added"
            and not change.old_path
            and bool(change.new_path)
            or change.status == "deleted"
            and bool(change.old_path)
            and not change.new_path
            or change.status == "modified"
            and bool(change.old_path)
            and change.old_path == change.new_path
            or change.status == "renamed"
            and bool(change.old_path)
            and bool(change.new_path)
            and change.old_path != change.new_path
        )
        if not valid_shape or any(
            not safe_policy_path(path)
            for path in (change.old_path, change.new_path)
            if path
        ):
            raise PacketBuildError("package upstream change shape is invalid")


def _valid_sha(value: Any) -> bool:
    return isinstance(value, str) and _OBJECT_ID.fullmatch(value) is not None


def _string_map(value: Any, field: str) -> Dict[str, str]:
    if not isinstance(value, dict) or any(
        not isinstance(key, str) or not isinstance(item, str)
        for key, item in value.items()
    ):
        raise PacketBuildError("package " + field + " must map strings to strings")
    return dict(value)


def _affected_areas(path: str) -> Tuple[str, ...]:
    lowered = path.lower()
    areas = []
    for marker, label in (
        ("venmo", "Venmo"),
        ("paypal-checkout", "PayPal Checkout"),
        ("three-d-secure", "3D Secure"),
        ("3d-secure", "3D Secure"),
        ("hosted-fields", "Hosted Fields"),
    ):
        if marker in lowered:
            areas.append(label)
    if ".stories." in lowered or "/stories/" in lowered:
        areas.append("Integration scenarios")
    if lowered.endswith("package.json"):
        areas.append("Dependencies")
    return tuple(dict.fromkeys(areas))


def _within(path: str, selected: str) -> bool:
    return path == selected or path.startswith(selected.rstrip("/") + "/")


def _recommendation_dict(value: PacketRecommendation) -> dict:
    return {
        "mode": value.mode,
        "priority": value.priority,
        "reasons": list(value.reasons),
    }


def _reject_duplicates(pairs: Iterable[Tuple[str, Any]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key " + key)
        result[key] = value
    return result


__all__ = [
    "IngestPacket",
    "PackagePacketInput",
    "PacketBuildError",
    "PacketRecommendation",
    "PacketSummary",
    "build_ingest_packet",
    "load_packet_summary",
    "publish_queued_packet",
    "publish_review_packet",
]
