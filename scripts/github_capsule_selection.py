"""Deterministic file selection and validation for GitHub source capsules."""

from dataclasses import dataclass, field
import hashlib
import re
from typing import AbstractSet, Dict, List, Mapping, NoReturn, Optional, Sequence, Set, Tuple

from github_canonical import safe_policy_path
from github_capsule_policy import (
    NPM_CAPSULE_ADAPTER,
    SECRET_DETECTOR,
    TAGGED_TREE_ADAPTER,
    CapsuleConfig,
    EffectivePolicy,
    PackageOverride,
    SecretAllowlist,
    build_effective_policy,
)
from github_git_tree import GitBlob, GitTree
from github_npm_workspace import (
    DeclaredTarget,
    WorkspacePackage,
    WorkspaceResolution,
    resolve_workspace,
)
from github_tagged_tree import resolve_tagged_workspace


_REGULAR_MODES = frozenset(("100644", "100755"))
_DETECTORS = (
    (
        "pem-private-key-header-v1",
        re.compile(
            r"(?m)^-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----[ \t]*\r?$",
            re.ASCII,
        ),
    ),
    (
        "aws-access-key-id-v1",
        re.compile(r"(?<![A-Z0-9])(?:AKIA|ASIA)[A-Z0-9]{16}(?![A-Z0-9])", re.ASCII),
    ),
    (
        "github-token-v1",
        re.compile(
            r"(?<![A-Za-z0-9_])(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{36,255}(?![A-Za-z0-9])",
            re.ASCII,
        ),
    ),
    (
        "github-fine-grained-token-v1",
        re.compile(
            r"(?<![A-Za-z0-9_])github_pat_[A-Za-z0-9_]{20,255}(?![A-Za-z0-9_])",
            re.ASCII,
        ),
    ),
    (
        "npm-access-token-v1",
        re.compile(
            r"(?<![A-Za-z0-9_])npm_[A-Za-z0-9]{36,255}(?![A-Za-z0-9])",
            re.ASCII,
        ),
    ),
    (
        "stripe-live-secret-key-v1",
        re.compile(
            r"(?<![A-Za-z0-9_])sk_live_[A-Za-z0-9]{16,255}(?![A-Za-z0-9])",
            re.ASCII,
        ),
    ),
    (
        "braintree-production-access-token-v1",
        re.compile(
            r"(?<![A-Za-z0-9_])access_token\$production\$"
            r"[A-Za-z0-9_-]+\$[A-Fa-f0-9]{32,128}(?![A-Za-z0-9])",
            re.ASCII,
        ),
    ),
)
_DETECTOR_CODES = tuple(item[0] for item in _DETECTORS)
_LFS_HEADER = b"version https://git-lfs.github.com/spec/v1"
_CATEGORY_ORDER = ("tests", "stories", "fixtures")
_CLASSIFICATION_ORDER = (
    "package-manifest",
    "required-root",
    "include-path",
    "changed-release-evidence",
    "tracked-main-target",
    "tracked-module-target",
    "tracked-bin-target",
    "tracked-export-target",
    "tracked-export-pattern",
    "tracked-types-target",
    "tracked-declaration-directory",
)
_CLASSIFICATION_PRIORITY = {
    reason: index for index, reason in enumerate(_CLASSIFICATION_ORDER)
}


@dataclass(frozen=True)
class CapsuleFile:
    path: str
    content: bytes = field(repr=False)
    sha256: str
    size: int
    purpose: str
    git_blob_oid: str
    git_mode: str
    package: str
    classification_reason: str


@dataclass(frozen=True)
class SecretFinding:
    path: str
    git_blob_oid: str
    detector_code: str
    file_sha256: str
    detector: str


@dataclass(frozen=True)
class _SecretFindingsEvidence:
    findings: Tuple[SecretFinding, ...]
    unallowlisted_findings: Tuple[SecretFinding, ...]


class SecretFindingsBlocked(ValueError):
    """Structured, bounded evidence for unallowlisted secret findings."""

    def __init__(
        self,
        findings: Sequence[SecretFinding],
        unallowlisted_findings: Sequence[SecretFinding],
    ) -> None:
        complete = _sorted_findings(findings)
        blocked = _sorted_findings(unallowlisted_findings)
        if not blocked:
            raise ValueError("unallowlisted_findings must not be empty")
        complete_by_identity = {_finding_identity(item): item for item in complete}
        for item in blocked:
            complete_item = complete_by_identity.get(_finding_identity(item))
            if complete_item is None:
                raise ValueError(
                    "unallowlisted_findings identity must be a subset of findings"
                )
            if complete_item != item:
                raise ValueError(
                    "unallowlisted_findings must contain exact finding records"
                )
        message = (
            "needs-policy-review:secret-finding: blocked="
            + str(len(blocked))
            + " findings="
            + str(len(complete))
            + " detector="
            + SECRET_DETECTOR
        )
        ValueError.__init__(self, message)
        object.__setattr__(self, "_evidence", _SecretFindingsEvidence(complete, blocked))
        object.__setattr__(self, "_sealed", True)

    def __setattr__(self, name: str, value: object) -> None:
        if getattr(self, "_sealed", False):
            raise AttributeError("SecretFindingsBlocked is immutable")
        object.__setattr__(self, name, value)

    def __delattr__(self, name: str) -> None:
        if getattr(self, "_sealed", False):
            raise AttributeError("SecretFindingsBlocked is immutable")
        object.__delattr__(self, name)

    @property
    def findings(self) -> Tuple[SecretFinding, ...]:
        return self._evidence.findings

    @property
    def unallowlisted_findings(self) -> Tuple[SecretFinding, ...]:
        return self._evidence.unallowlisted_findings


@dataclass(frozen=True)
class CapsuleResolution:
    workspace: WorkspaceResolution
    files: Tuple[CapsuleFile, ...]
    excluded: Tuple[Tuple[str, str], ...]
    required_roots: Tuple[Tuple[str, str, str], ...]
    generated_target_paths: Tuple[Tuple[str, str, str, str], ...]
    include_paths: Tuple[Tuple[str, str, str], ...]
    secret_findings: Tuple[SecretFinding, ...]
    effective_policy: EffectivePolicy

    @property
    def scanned_blob_count(self) -> int:
        return len(self.files)


def resolve_npm_capsule(
    tree: GitTree,
    capsule: CapsuleConfig,
    allowlist: Sequence[SecretAllowlist],
    changed_paths: Sequence[str] = (),
) -> CapsuleResolution:
    """Resolve, validate, scan, and budget one NPM source capsule."""
    if not isinstance(tree, GitTree):
        raise TypeError("tree must be a GitTree")
    if not isinstance(capsule, CapsuleConfig) or capsule.adapter != NPM_CAPSULE_ADAPTER:
        raise ValueError("capsule must use " + NPM_CAPSULE_ADAPTER)

    normalized = build_effective_policy(capsule, (), (), _DETECTOR_CODES).capsule
    workspace = resolve_workspace(tree, normalized)
    blobs_by_path = {blob.path: blob for blob in tree.blobs()}
    targets_by_package = _targets_by_package(workspace.declared_targets)
    overrides = {item.name: item for item in normalized.package_overrides}

    candidate_reasons: Dict[str, Tuple[str, str, Set[str]]] = {}
    excluded: Set[Tuple[str, str]] = set()
    required_rows: Set[Tuple[str, str, str]] = set()
    generated_rows: List[Tuple[str, str, str, str]] = []
    include_rows: Set[Tuple[str, str, str]] = set()

    for package in workspace.packages:
        override = overrides.get(package.name)
        roots, root_source = _required_roots(normalized, override)
        generated, generated_source = _generated_paths(normalized, override)
        configured_includes = _configured_includes(normalized, override)
        owned_paths = frozenset(package.owned_paths)

        for root in roots:
            required_rows.add((package.name, root, root_source))
        for root in package.tracked_declaration_roots:
            required_rows.add(
                (package.name, root, "tracked-declaration-target")
            )
        for path in generated:
            generated_rows.append(
                (
                    package.name,
                    path,
                    "directory" if path.endswith("/") else "file",
                    generated_source,
                )
            )
        for path, source in configured_includes:
            include_rows.add((package.name, path, source))

        _select(
            candidate_reasons,
            package,
            "package.json",
            "package-manifest",
            owned_paths,
            "missing-package-manifest",
        )
        for path, _ in configured_includes:
            _select(
                candidate_reasons,
                package,
                path,
                "include-path",
                owned_paths,
                "missing-required-include",
            )

        for target in targets_by_package.get(package.name, ()):
            if target.status not in ("tracked-required", "tracked-pattern-required"):
                continue
            reasons = _target_reasons(target)
            for path in target.matched_paths:
                include_rows.add((package.name, path, "declared-target"))
                for reason in reasons:
                    _select(
                        candidate_reasons,
                        package,
                        path,
                        reason,
                        owned_paths,
                        "invalid-workspace-resolution",
                    )

        for root in package.tracked_declaration_roots:
            for path in package.owned_paths:
                if _below_root(path, root):
                    repository_path = _join(package.path, path)
                    categories = _excluded_categories(
                        path,
                        normalized.excluded_categories,
                    )
                    if categories and repository_path not in candidate_reasons:
                        for category in categories:
                            excluded.add(
                                (repository_path, "excluded-category:" + category)
                            )
                        continue
                    _select(
                        candidate_reasons,
                        package,
                        path,
                        "tracked-declaration-directory",
                        owned_paths,
                        "invalid-workspace-resolution",
                    )

        for root in roots:
            matching = tuple(
                path for path in package.owned_paths if _below_root(path, root)
            )
            if not matching:
                _review(
                    "missing-required-root",
                    "package=" + package.name + " path=" + root,
                )
            for path in matching:
                repository_path = _join(package.path, path)
                categories = _excluded_categories(
                    path,
                    normalized.excluded_categories,
                )
                if categories and repository_path not in candidate_reasons:
                    if safe_policy_path(repository_path):
                        for category in categories:
                            excluded.add(
                                (repository_path, "excluded-category:" + category)
                            )
                    continue
                _select(
                    candidate_reasons,
                    package,
                    path,
                    "required-root",
                    owned_paths,
                    "invalid-workspace-resolution",
                )

    _select_changed_paths(
        candidate_reasons,
        workspace,
        changed_paths,
        normalized.changed_path_policy,
        normalized.excluded_categories,
        excluded,
    )
    excluded = {
        item for item in excluded if item[0] not in candidate_reasons
    }
    selected_blobs = _selected_blobs(candidate_reasons, blobs_by_path)
    effective_policy = build_effective_policy(
        normalized,
        allowlist,
        tuple((path, blob.oid) for path, blob in selected_blobs),
        _DETECTOR_CODES,
    )
    files, findings = _read_selected_files(
        tree,
        selected_blobs,
        candidate_reasons,
        effective_policy.capsule,
    )
    allowed = frozenset(
        (item.path, item.blob_oid, item.detector_code)
        for item in effective_policy.applicable_secret_allowlist
    )
    unallowlisted_findings = tuple(
        item
        for item in findings
        if (item.path, item.git_blob_oid, item.detector_code) not in allowed
    )
    if unallowlisted_findings:
        raise SecretFindingsBlocked(findings, unallowlisted_findings)

    return CapsuleResolution(
        workspace=workspace,
        files=files,
        excluded=tuple(sorted(excluded)),
        required_roots=tuple(sorted(required_rows)),
        generated_target_paths=tuple(sorted(set(generated_rows))),
        include_paths=tuple(sorted(include_rows)),
        secret_findings=findings,
        effective_policy=effective_policy,
    )


def resolve_capsule_workspace(
    tree: GitTree,
    capsule: CapsuleConfig,
    versions: Optional[Mapping[str, str]] = None,
) -> WorkspaceResolution:
    """Resolve the adapter-specific workspace contract for one exact tree."""
    if not isinstance(capsule, CapsuleConfig):
        raise TypeError("capsule must be a CapsuleConfig")
    if capsule.adapter == NPM_CAPSULE_ADAPTER:
        return resolve_workspace(tree, capsule)
    if capsule.adapter == TAGGED_TREE_ADAPTER:
        if versions is None:
            raise ValueError("tagged-tree-v1 requires package versions")
        return resolve_tagged_workspace(tree, capsule, versions)
    raise ValueError("unsupported capsule adapter " + capsule.adapter)


def resolve_capsule(
    tree: GitTree,
    capsule: CapsuleConfig,
    allowlist: Sequence[SecretAllowlist],
    changed_paths: Sequence[str] = (),
    versions: Optional[Mapping[str, str]] = None,
) -> CapsuleResolution:
    """Resolve one source capsule through its configured adapter."""
    if not isinstance(capsule, CapsuleConfig):
        raise TypeError("capsule must be a CapsuleConfig")
    if capsule.adapter == NPM_CAPSULE_ADAPTER:
        return resolve_npm_capsule(tree, capsule, allowlist, changed_paths)
    if capsule.adapter != TAGGED_TREE_ADAPTER:
        raise ValueError("unsupported capsule adapter " + capsule.adapter)
    if versions is None:
        raise ValueError("tagged-tree-v1 requires package versions")
    return _resolve_tagged_capsule(
        tree,
        capsule,
        allowlist,
        changed_paths,
        versions,
    )


def _resolve_tagged_capsule(
    tree: GitTree,
    capsule: CapsuleConfig,
    allowlist: Sequence[SecretAllowlist],
    changed_paths: Sequence[str],
    versions: Mapping[str, str],
) -> CapsuleResolution:
    normalized = build_effective_policy(capsule, (), (), _DETECTOR_CODES).capsule
    workspace = resolve_tagged_workspace(tree, normalized, versions)
    blobs_by_path = {blob.path: blob for blob in tree.blobs()}
    package = workspace.packages[0]
    owned_paths = frozenset(package.owned_paths)

    candidate_reasons: Dict[str, Tuple[str, str, Set[str]]] = {}
    excluded: Set[Tuple[str, str]] = set()
    required_rows: Set[Tuple[str, str, str]] = set()
    include_rows: Set[Tuple[str, str, str]] = set()

    for path in normalized.include_paths:
        include_rows.add((package.name, path, "capsule-policy"))
        _select(
            candidate_reasons,
            package,
            path,
            "include-path",
            owned_paths,
            "missing-required-include",
        )
    for root in normalized.default_required_roots:
        required_rows.add((package.name, root, "default"))
        matching = tuple(path for path in package.owned_paths if _below_root(path, root))
        if not matching:
            _review(
                "missing-required-root",
                "package=" + package.name + " path=" + root,
            )
        for path in matching:
            categories = _excluded_categories(
                path,
                normalized.excluded_categories,
            )
            if categories and path not in candidate_reasons:
                for category in categories:
                    excluded.add((path, "excluded-category:" + category))
                continue
            _select(
                candidate_reasons,
                package,
                path,
                "required-root",
                owned_paths,
                "invalid-workspace-resolution",
            )

    _select_changed_paths(
        candidate_reasons,
        workspace,
        changed_paths,
        normalized.changed_path_policy,
        normalized.excluded_categories,
        excluded,
    )
    excluded = {item for item in excluded if item[0] not in candidate_reasons}
    selected_blobs = _selected_blobs(candidate_reasons, blobs_by_path)
    effective_policy = build_effective_policy(
        normalized,
        allowlist,
        tuple((path, blob.oid) for path, blob in selected_blobs),
        _DETECTOR_CODES,
    )
    files, findings = _read_selected_files(
        tree,
        selected_blobs,
        candidate_reasons,
        effective_policy.capsule,
    )
    allowed = frozenset(
        (item.path, item.blob_oid, item.detector_code)
        for item in effective_policy.applicable_secret_allowlist
    )
    unallowlisted_findings = tuple(
        item
        for item in findings
        if (item.path, item.git_blob_oid, item.detector_code) not in allowed
    )
    if unallowlisted_findings:
        raise SecretFindingsBlocked(findings, unallowlisted_findings)

    return CapsuleResolution(
        workspace=workspace,
        files=files,
        excluded=tuple(sorted(excluded)),
        required_roots=tuple(sorted(required_rows)),
        generated_target_paths=(),
        include_paths=tuple(sorted(include_rows)),
        secret_findings=findings,
        effective_policy=effective_policy,
    )


def scan_evidence_files(
    files: Sequence[CapsuleFile],
    allowlist: Sequence[SecretAllowlist],
) -> Tuple[SecretFinding, ...]:
    """Scan already selected text evidence with the capsule detector contract."""
    findings: Set[SecretFinding] = set()
    paths = set()
    for item in files:
        if not isinstance(item, CapsuleFile):
            raise TypeError("files must contain CapsuleFile values")
        if item.path in paths:
            raise ValueError("evidence files contain duplicate paths")
        paths.add(item.path)
        if not safe_policy_path(item.path):
            _review("unsafe-required-file", "evidence path is not safe")
        if not isinstance(item.content, bytes):
            raise TypeError("evidence file content must be bytes")
        if item.size != len(item.content):
            _review("unsafe-required-file", "evidence size does not match content")
        digest = hashlib.sha256(item.content).hexdigest()
        if item.sha256 != digest:
            _review("unsafe-required-file", "evidence hash does not match content")
        if _is_lfs_pointer(item.content):
            _review("unsafe-required-file", "evidence is a Git LFS pointer")
        if b"\0" in item.content:
            _review("unsafe-required-file", "evidence contains NUL bytes")
        try:
            text = item.content.decode("utf-8", "strict")
        except UnicodeDecodeError:
            _review("unsafe-required-file", "evidence is not strict UTF-8")
        findings.update(
            _scan_secrets(item.path, item.git_blob_oid, item.sha256, text)
        )

    for item in allowlist:
        if not isinstance(item, SecretAllowlist):
            raise TypeError("allowlist must contain SecretAllowlist values")
    complete = _sorted_findings(findings)
    allowed = frozenset(
        (item.path, item.blob_oid, item.detector_code) for item in allowlist
    )
    blocked = tuple(
        item
        for item in complete
        if (item.path, item.git_blob_oid, item.detector_code) not in allowed
    )
    if blocked:
        raise SecretFindingsBlocked(complete, blocked)
    return complete


def _select_changed_paths(
    selected: Dict[str, Tuple[str, str, Set[str]]],
    workspace: WorkspaceResolution,
    changed_paths: Sequence[str],
    changed_path_policy: str,
    excluded_categories: Sequence[str],
    excluded: Set[Tuple[str, str]],
) -> None:
    if isinstance(changed_paths, (str, bytes)):
        raise TypeError("changed_paths must be a sequence of paths")
    for path in sorted(set(changed_paths)):
        if not isinstance(path, str) or not safe_policy_path(path):
            _review("unsafe-changed-path", "changed path is not safe")
        owners = []
        for package in workspace.packages:
            prefix = package.path + "/" if package.path else ""
            if path.startswith(prefix) and path[len(prefix):] in package.owned_paths:
                owners.append(package)
        if not owners:
            continue
        package = max(owners, key=lambda item: len(item.path))
        prefix = package.path + "/" if package.path else ""
        relative = path[len(prefix):]
        categories = _excluded_categories(relative, excluded_categories)
        if categories and path not in selected:
            for category in categories:
                excluded.add((path, "excluded-category:" + category))
            continue
        current = selected.get(path)
        if current is None:
            if changed_path_policy == "policy-bounded":
                continue
            selected[path] = (
                package.name,
                relative,
                {"changed-release-evidence"},
            )
            continue
        if current[0] != package.name or current[1] != relative:
            _review("ambiguous-package", "changed path has inconsistent ownership")
        current[2].add("changed-release-evidence")


def _targets_by_package(
    targets: Sequence[DeclaredTarget],
) -> Mapping[str, Tuple[DeclaredTarget, ...]]:
    result: Dict[str, List[DeclaredTarget]] = {}
    for target in targets:
        result.setdefault(target.package, []).append(target)
    return {name: tuple(values) for name, values in result.items()}


def _required_roots(
    capsule: CapsuleConfig,
    override: Optional[PackageOverride],
) -> Tuple[Tuple[str, ...], str]:
    if override is None:
        return capsule.default_required_roots, "default"
    return override.required_roots, "package-override"


def _generated_paths(
    capsule: CapsuleConfig,
    override: Optional[PackageOverride],
) -> Tuple[Tuple[str, ...], str]:
    if override is None:
        return capsule.default_generated_target_paths, "default"
    return override.generated_target_paths, "package-override"


def _configured_includes(
    capsule: CapsuleConfig,
    override: Optional[PackageOverride],
) -> Tuple[Tuple[str, str], ...]:
    values = {path: "capsule-policy" for path in capsule.include_paths}
    if override is not None:
        for path in override.include_paths:
            values.setdefault(path, "package-override")
    return tuple(sorted(values.items()))


def _select(
    selected: Dict[str, Tuple[str, str, Set[str]]],
    package: WorkspacePackage,
    relative_path: str,
    reason: str,
    owned_paths: AbstractSet[str],
    missing_code: str,
) -> None:
    if relative_path not in owned_paths:
        _review(
            missing_code,
            "package=" + package.name + " path=" + relative_path,
        )
    repository_path = _join(package.path, relative_path)
    current = selected.get(repository_path)
    if current is None:
        selected[repository_path] = (package.name, relative_path, {reason})
        return
    if current[0] != package.name or current[1] != relative_path:
        _review("ambiguous-package", "more than one package owns " + repository_path)
    current[2].add(reason)


def _selected_blobs(
    candidates: Mapping[str, Tuple[str, str, Set[str]]],
    blobs_by_path: Mapping[str, GitBlob],
) -> Tuple[Tuple[str, GitBlob], ...]:
    result = []
    for path in sorted(candidates):
        if not safe_policy_path(path):
            _review("unsafe-required-file", "unsafe selected path")
        blob = blobs_by_path.get(path)
        if blob is None:
            _review("unsafe-required-file", "selected path is not a Git tree entry: " + path)
        if blob.mode not in _REGULAR_MODES:
            _review(
                "unsafe-required-file",
                "selected path is not a regular Git blob: " + path,
            )
        result.append((path, blob))
    return tuple(result)


def _read_selected_files(
    tree: GitTree,
    selected_blobs: Sequence[Tuple[str, GitBlob]],
    candidates: Mapping[str, Tuple[str, str, Set[str]]],
    capsule: CapsuleConfig,
) -> Tuple[Tuple[CapsuleFile, ...], Tuple[SecretFinding, ...]]:
    if len(selected_blobs) > capsule.max_capsule_files:
        _review(
            "capsule-budget-exceeded",
            "selected file count "
            + str(len(selected_blobs))
            + " exceeds max_capsule_files "
            + str(capsule.max_capsule_files),
        )

    files: List[CapsuleFile] = []
    findings: Set[SecretFinding] = set()
    total_bytes = 0
    for path, blob in selected_blobs:
        if tree.blob_size(path) > capsule.max_file_bytes:
            _review(
                "capsule-budget-exceeded",
                "path=" + path + " exceeds max_file_bytes",
            )
        content = tree.read_blob(path, max_bytes=capsule.max_file_bytes)
        if _is_lfs_pointer(content):
            _review("unsafe-required-file", "selected path is a Git LFS pointer: " + path)
        if b"\0" in content:
            _review("unsafe-required-file", "selected path contains NUL bytes: " + path)
        try:
            text = content.decode("utf-8", "strict")
        except UnicodeDecodeError:
            _review("unsafe-required-file", "selected path is not strict UTF-8: " + path)
        digest = hashlib.sha256(content).hexdigest()
        package, _, reasons = candidates[path]
        reason = min(reasons, key=lambda value: _CLASSIFICATION_PRIORITY[value])
        files.append(
            CapsuleFile(
                path=path,
                content=content,
                sha256=digest,
                size=len(content),
                purpose="source-capsule",
                git_blob_oid=blob.oid,
                git_mode=blob.mode,
                package=package,
                classification_reason=reason,
            )
        )
        findings.update(_scan_secrets(path, blob.oid, digest, text))
        total_bytes += len(content)
        if total_bytes > capsule.max_capsule_utf8_bytes:
            _review(
                "capsule-budget-exceeded",
                "selected UTF-8 bytes exceed max_capsule_utf8_bytes",
            )
    return tuple(files), tuple(
        sorted(
            findings,
            key=lambda item: (item.path, item.git_blob_oid, item.detector_code),
        )
    )


def _scan_secrets(
    path: str,
    blob_oid: str,
    file_sha256: str,
    text: str,
) -> Tuple[SecretFinding, ...]:
    return tuple(
        SecretFinding(path, blob_oid, detector_code, file_sha256, SECRET_DETECTOR)
        for detector_code, pattern in _DETECTORS
        if pattern.search(text) is not None
    )


def _sorted_findings(
    findings: Sequence[SecretFinding],
) -> Tuple[SecretFinding, ...]:
    if any(not isinstance(item, SecretFinding) for item in findings):
        raise ValueError("findings must contain SecretFinding records")
    result = tuple(
        sorted(
            findings,
            key=_finding_identity,
        )
    )
    identities = tuple(_finding_identity(item) for item in result)
    if len(identities) != len(set(identities)):
        raise ValueError("finding identity must be unique")
    return result


def _finding_identity(value: SecretFinding) -> Tuple[str, str, str]:
    return (value.path, value.git_blob_oid, value.detector_code)


def _is_lfs_pointer(content: bytes) -> bool:
    return (
        content == _LFS_HEADER
        or content.startswith(_LFS_HEADER + b"\n")
        or content.startswith(_LFS_HEADER + b"\r\n")
    )


def classify_excluded_categories(
    path: str, enabled: Sequence[str]
) -> Tuple[str, ...]:
    """Return approved evidence categories matched by one package-relative path."""
    if not isinstance(path, str) or not safe_policy_path(path):
        raise ValueError("category classifier path must be safe")
    return _classify_excluded_categories(path, enabled)


def _classify_excluded_categories(
    path: str, enabled: Sequence[str]
) -> Tuple[str, ...]:
    enabled_set = frozenset(enabled)
    if any(category not in _CATEGORY_ORDER for category in enabled_set):
        raise ValueError("category classifier contains an unknown category")
    segments = tuple(segment.lower() for segment in path.split("/"))
    filename = segments[-1]
    matches = {
        "tests": (
            ".test." in filename
            or ".spec." in filename
            or any(
                segment in (
                    "test",
                    "tests",
                    "__tests__",
                    "__mocks__",
                    "bundle-tests",
                )
                for segment in segments
            )
        ),
        "stories": (
            ".stories." in filename
            or any(
                segment in (".storybook", "storybook", "stories")
                for segment in segments
            )
        ),
        "fixtures": any(
            segment in ("fixture", "fixtures", "__fixtures__", "snapshots")
            for segment in segments
        ),
    }
    return tuple(
        category
        for category in _CATEGORY_ORDER
        if category in enabled_set and matches[category]
    )


def _excluded_categories(path: str, enabled: Sequence[str]) -> Tuple[str, ...]:
    return _classify_excluded_categories(path, enabled)


def _target_reasons(target: DeclaredTarget) -> Tuple[str, ...]:
    if target.field in ("types", "typings"):
        return ("tracked-types-target",)
    if target.field == "main":
        return ("tracked-main-target",)
    if target.field == "module":
        return ("tracked-module-target",)
    if target.field == "bin":
        return ("tracked-bin-target",)
    if target.field == "exports":
        primary = (
            "tracked-export-pattern"
            if target.status == "tracked-pattern-required"
            else "tracked-export-target"
        )
        if "types" in target.condition_chain:
            return (primary, "tracked-types-target")
        return (primary,)
    _review("invalid-workspace-resolution", "unknown declared target field")


def _below_root(path: str, root: str) -> bool:
    return not root or path.startswith(root + "/")


def _join(left: str, right: str) -> str:
    return left + "/" + right if left else right


def _review(code: str, detail: str) -> NoReturn:
    raise ValueError("needs-policy-review:" + code + ": " + detail[:500])


__all__ = [
    "CapsuleFile",
    "CapsuleResolution",
    "SecretFinding",
    "SecretFindingsBlocked",
    "classify_excluded_categories",
    "resolve_capsule",
    "resolve_capsule_workspace",
    "resolve_npm_capsule",
    "scan_evidence_files",
]
