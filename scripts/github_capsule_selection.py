"""Deterministic file selection and validation for NPM source capsules."""

from dataclasses import dataclass, field
import hashlib
import re
from typing import AbstractSet, Dict, List, Mapping, NoReturn, Optional, Sequence, Set, Tuple

from github_canonical import safe_policy_path
from github_capsule_policy import (
    CAPSULE_ADAPTER,
    SECRET_DETECTOR,
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
)
_DETECTOR_CODES = tuple(item[0] for item in _DETECTORS)
_LFS_HEADER = b"version https://git-lfs.github.com/spec/v1"
_CATEGORY_ORDER = ("tests", "stories", "fixtures")
_CLASSIFICATION_ORDER = (
    "package-manifest",
    "required-root",
    "include-path",
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
) -> CapsuleResolution:
    """Resolve, validate, scan, and budget one NPM source capsule."""
    if not isinstance(tree, GitTree):
        raise TypeError("tree must be a GitTree")
    if not isinstance(capsule, CapsuleConfig) or capsule.adapter != CAPSULE_ADAPTER:
        raise ValueError("capsule must use " + CAPSULE_ADAPTER)

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
        if blob.mode not in _REGULAR_MODES or blob.size is None:
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
            "selected file count exceeds max_capsule_files",
        )

    files: List[CapsuleFile] = []
    findings: Set[SecretFinding] = set()
    total_bytes = 0
    for path, blob in selected_blobs:
        if blob.size is None or blob.size > capsule.max_file_bytes:
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


def _excluded_categories(path: str, enabled: Sequence[str]) -> Tuple[str, ...]:
    enabled_set = frozenset(enabled)
    segments = path.split("/")
    filename = segments[-1]
    matches = {
        "tests": (
            ".test." in filename
            or ".spec." in filename
            or any(
                segment in ("test", "tests", "__tests__", "bundle-tests")
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
    "resolve_npm_capsule",
]
