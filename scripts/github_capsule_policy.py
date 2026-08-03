"""Frozen GitHub source-capsule policy records and registry parsing."""

import re
from dataclasses import dataclass
from typing import Dict, Iterable, Sequence, Tuple

from github_canonical import canonical_json_bytes, canonical_sha256, safe_policy_path, validate_npm_package_name


NPM_CAPSULE_ADAPTER = "npm-tracked-source-v1"
TAGGED_TREE_ADAPTER = "tagged-tree-v1"
COMMIT_TREE_ADAPTER = "commit-tree-v1"
CAPSULE_ADAPTERS = frozenset((NPM_CAPSULE_ADAPTER, TAGGED_TREE_ADAPTER, COMMIT_TREE_ADAPTER))
CAPSULE_ADAPTER = NPM_CAPSULE_ADAPTER
NPM_DEPENDENCY_SCOPE = "internal-runtime-closure"
TAGGED_TREE_DEPENDENCY_SCOPE = "configured-repository-paths"
COMMIT_TREE_DEPENDENCY_SCOPE = "configured-repository-paths"
DEPENDENCY_SCOPES = {
    NPM_CAPSULE_ADAPTER: NPM_DEPENDENCY_SCOPE,
    TAGGED_TREE_ADAPTER: TAGGED_TREE_DEPENDENCY_SCOPE,
    COMMIT_TREE_ADAPTER: COMMIT_TREE_DEPENDENCY_SCOPE,
}
DEPENDENCY_SCOPE = NPM_DEPENDENCY_SCOPE
DEFAULT_CHANGED_PATH_POLICY = "package-owned"
CHANGED_PATH_POLICIES = frozenset((DEFAULT_CHANGED_PATH_POLICY, "policy-bounded"))
SECRET_DETECTOR = "text-secrets-v1"
CATEGORY_CLASSIFIER = "excluded-categories-v1"
WORKSPACE_RESOLVERS = {
    NPM_CAPSULE_ADAPTER: "npm-workspaces-v1",
    TAGGED_TREE_ADAPTER: "single-tagged-tree-v1",
    COMMIT_TREE_ADAPTER: "exact-commit-tree-v1",
}
WORKSPACE_RESOLVER = WORKSPACE_RESOLVERS[NPM_CAPSULE_ADAPTER]
DEFAULT_REQUIRED_ROOTS = ("src",)
DEFAULT_EXCLUDED_CATEGORIES = ("fixtures", "stories", "tests")
EXCLUDED_CATEGORIES = frozenset(DEFAULT_EXCLUDED_CATEGORIES)
_CAPSULE_ID = re.compile(r"[a-z0-9][a-z0-9-]{0,62}\Z")
_BLOB_OID = re.compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})\Z")
_SHA256 = re.compile(r"[0-9a-f]{64}\Z")

_CAPSULE_REQUIRED_KEYS = {"id", "adapter"}
_CAPSULE_OPTIONAL_KEYS = {
    "focus_packages",
    "source_id",
    "dependency_scope",
    "changed_path_policy",
    "default_required_roots",
    "default_generated_target_paths",
    "include_paths",
    "excluded_categories",
    "secret_detector",
    "max_file_bytes",
    "max_capsule_files",
    "max_capsule_utf8_bytes",
    "max_packet_files",
    "max_packet_utf8_bytes",
    "package_overrides",
    "historical_policy_hashes",
}
_OVERRIDE_KEYS = {"name", "required_roots", "generated_target_paths", "include_paths"}
_ALLOWLIST_KEYS = {"path", "blob_oid", "detector_code"}


@dataclass(frozen=True)
class PackageOverride:
    name: str
    required_roots: Tuple[str, ...]
    generated_target_paths: Tuple[str, ...]
    include_paths: Tuple[str, ...]


@dataclass(frozen=True)
class SecretAllowlist:
    path: str
    blob_oid: str
    detector_code: str


@dataclass(frozen=True)
class CapsuleConfig:
    id: str
    adapter: str
    focus_packages: Tuple[str, ...] = ()
    source_id: str = ""
    dependency_scope: str = DEPENDENCY_SCOPE
    changed_path_policy: str = DEFAULT_CHANGED_PATH_POLICY
    default_required_roots: Tuple[str, ...] = DEFAULT_REQUIRED_ROOTS
    default_generated_target_paths: Tuple[str, ...] = ()
    include_paths: Tuple[str, ...] = ()
    excluded_categories: Tuple[str, ...] = DEFAULT_EXCLUDED_CATEGORIES
    secret_detector: str = SECRET_DETECTOR
    max_file_bytes: int = 512000
    max_capsule_files: int = 120
    max_capsule_utf8_bytes: int = 750000
    max_packet_files: int = 160
    max_packet_utf8_bytes: int = 1000000
    package_overrides: Tuple[PackageOverride, ...] = ()
    historical_policy_hashes: Tuple[str, ...] = ()


@dataclass(frozen=True)
class EffectivePolicy:
    capsule: CapsuleConfig
    applicable_secret_allowlist: Tuple[SecretAllowlist, ...]
    canonical_bytes: bytes
    policy_hash: str


def parse_capsules(value: object, repository_index: int) -> Tuple[CapsuleConfig, ...]:
    """Parse and validate repository-local capsule policy tables."""
    if not isinstance(value, list):
        raise ValueError(_prefix(repository_index) + " capsules must be an array of tables")
    capsules = []
    ids = set()
    for capsule_index, row in enumerate(value, 1):
        prefix = _prefix(repository_index) + " capsule " + str(capsule_index)
        if not isinstance(row, dict):
            raise ValueError(prefix + " must be a table")
        _exact_keys(row, _CAPSULE_REQUIRED_KEYS, _CAPSULE_OPTIONAL_KEYS, prefix)
        capsule = _parse_capsule(row, prefix)
        if capsule.id in ids:
            raise ValueError(prefix + " has duplicate capsule id " + capsule.id)
        ids.add(capsule.id)
        capsules.append(capsule)
    return tuple(capsules)


def parse_secret_allowlist(value: object, repository_index: int) -> Tuple[SecretAllowlist, ...]:
    """Parse and validate repository-level immutable secret exceptions."""
    if not isinstance(value, list):
        raise ValueError(_prefix(repository_index) + " secret_allowlist must be an array of tables")
    rows = []
    triples = set()
    for allowlist_index, row in enumerate(value, 1):
        prefix = _prefix(repository_index) + " secret allowlist " + str(allowlist_index)
        if not isinstance(row, dict):
            raise ValueError(prefix + " must be a table")
        _exact_keys(row, _ALLOWLIST_KEYS, set(), prefix)
        item = _normalize_allowlist(
            SecretAllowlist(
                _required_string(row, "path", prefix),
                _required_string(row, "blob_oid", prefix),
                _required_string(row, "detector_code", prefix),
            ),
            prefix,
        )
        triple = (item.path, item.blob_oid, item.detector_code)
        if triple in triples:
            raise ValueError(prefix + " has duplicate secret allowlist row")
        triples.add(triple)
        rows.append(item)
    return tuple(sorted(rows, key=lambda item: (item.path, item.blob_oid, item.detector_code)))


def build_effective_policy(
    capsule: CapsuleConfig,
    secret_allowlist: Sequence[SecretAllowlist],
    selected_candidate_blobs: Sequence[Tuple[str, str]],
    detector_codes: Sequence[str],
) -> EffectivePolicy:
    """Return the immutable policy applicable to the selected candidate blobs."""
    normalized_capsule = _normalize_capsule(capsule, "capsule")
    candidates = _candidate_blob_keys(selected_candidate_blobs)
    selected_codes = _unique_strings(detector_codes, "detector_codes", allow_empty=True)
    applicable = []
    applicable_triples = set()
    for index, item in enumerate(secret_allowlist, 1):
        normalized = _normalize_allowlist(item, "secret allowlist " + str(index))
        if (normalized.path, normalized.blob_oid) in candidates and normalized.detector_code in selected_codes:
            triple = (normalized.path, normalized.blob_oid, normalized.detector_code)
            if triple in applicable_triples:
                raise ValueError("duplicate applicable secret allowlist row")
            applicable_triples.add(triple)
            applicable.append(normalized)
    applicable_rows = tuple(sorted(applicable, key=lambda item: (item.path, item.blob_oid, item.detector_code)))
    payload = _policy_payload(normalized_capsule, applicable_rows)
    bytes_value = canonical_json_bytes(payload)
    return EffectivePolicy(normalized_capsule, applicable_rows, bytes_value, canonical_sha256(payload))


def _parse_capsule(row: Dict[str, object], prefix: str) -> CapsuleConfig:
    adapter = _required_string(row, "adapter", prefix)
    return _normalize_capsule(
        CapsuleConfig(
            id=_required_string(row, "id", prefix),
            adapter=adapter,
            focus_packages=_strings(row, "focus_packages", prefix),
            source_id=_optional_string(row, "source_id", "", prefix, allow_empty=True),
            dependency_scope=_optional_string(
                row,
                "dependency_scope",
                DEPENDENCY_SCOPES.get(adapter, DEPENDENCY_SCOPE),
                prefix,
            ),
            changed_path_policy=_optional_string(
                row,
                "changed_path_policy",
                DEFAULT_CHANGED_PATH_POLICY,
                prefix,
            ),
            default_required_roots=_strings(row, "default_required_roots", prefix, default=DEFAULT_REQUIRED_ROOTS),
            default_generated_target_paths=_strings(row, "default_generated_target_paths", prefix, default=()),
            include_paths=_strings(row, "include_paths", prefix, default=()),
            excluded_categories=_strings(row, "excluded_categories", prefix, default=DEFAULT_EXCLUDED_CATEGORIES),
            secret_detector=_optional_string(row, "secret_detector", SECRET_DETECTOR, prefix),
            max_file_bytes=_positive_int(row, "max_file_bytes", 512000, prefix),
            max_capsule_files=_positive_int(row, "max_capsule_files", 120, prefix),
            max_capsule_utf8_bytes=_positive_int(row, "max_capsule_utf8_bytes", 750000, prefix),
            max_packet_files=_positive_int(row, "max_packet_files", 160, prefix),
            max_packet_utf8_bytes=_positive_int(row, "max_packet_utf8_bytes", 1000000, prefix),
            package_overrides=_parse_overrides(row.get("package_overrides", []), prefix),
            historical_policy_hashes=_policy_hashes(row.get("historical_policy_hashes", ()), prefix),
        ),
        prefix,
    )


def _parse_overrides(value: object, capsule_prefix: str) -> Tuple[PackageOverride, ...]:
    if not isinstance(value, list):
        raise ValueError(capsule_prefix + " package_overrides must be an array of tables")
    overrides = []
    names = set()
    for override_index, row in enumerate(value, 1):
        prefix = capsule_prefix + " package override " + str(override_index)
        if not isinstance(row, dict):
            raise ValueError(prefix + " must be a table")
        _exact_keys(row, _OVERRIDE_KEYS, set(), prefix)
        override = _normalize_override(
            PackageOverride(
                _required_string(row, "name", prefix),
                _strings(row, "required_roots", prefix, required=True),
                _strings(row, "generated_target_paths", prefix),
                _strings(row, "include_paths", prefix),
            ),
            prefix,
        )
        if override.name in names:
            raise ValueError(prefix + " has duplicate package override " + override.name)
        names.add(override.name)
        overrides.append(override)
    return tuple(sorted(overrides, key=lambda item: item.name))


def _normalize_capsule(capsule: CapsuleConfig, prefix: str) -> CapsuleConfig:
    if not isinstance(capsule, CapsuleConfig):
        raise ValueError(prefix + " must be a CapsuleConfig")
    if _CAPSULE_ID.fullmatch(capsule.id) is None:
        raise ValueError(prefix + " id must be a lowercase ASCII slug")
    if capsule.adapter not in CAPSULE_ADAPTERS:
        raise ValueError(
            prefix
            + " adapter must be one of "
            + ", ".join(sorted(CAPSULE_ADAPTERS))
        )
    focus_packages = _package_names(
        capsule.focus_packages,
        prefix + " focus_packages",
        required=capsule.adapter != COMMIT_TREE_ADAPTER,
    )
    source_id = capsule.source_id
    if capsule.adapter == COMMIT_TREE_ADAPTER:
        if focus_packages:
            raise ValueError(prefix + " commit-tree-v1 forbids focus_packages")
        if not isinstance(source_id, str) or not safe_policy_path(source_id):
            raise ValueError(prefix + " commit-tree-v1 requires a safe source_id")
        if capsule.default_generated_target_paths:
            raise ValueError(prefix + " commit-tree-v1 forbids generated target paths")
        if capsule.package_overrides:
            raise ValueError(prefix + " commit-tree-v1 forbids package overrides")
    elif source_id:
        raise ValueError(prefix + " " + capsule.adapter + " forbids source_id")
    if capsule.adapter == TAGGED_TREE_ADAPTER and len(focus_packages) != 1:
        raise ValueError(prefix + " tagged-tree-v1 requires exactly one focus package")
    dependency_scope = DEPENDENCY_SCOPES[capsule.adapter]
    if capsule.dependency_scope != dependency_scope:
        raise ValueError(prefix + " dependency_scope must equal " + dependency_scope)
    if capsule.changed_path_policy not in CHANGED_PATH_POLICIES:
        raise ValueError(
            prefix
            + " changed_path_policy must be package-owned or policy-bounded"
        )
    required_roots = _paths(capsule.default_required_roots, prefix + " default_required_roots", required=True)
    generated_targets = _generated_paths(
        capsule.default_generated_target_paths, prefix + " default_generated_target_paths"
    )
    include_paths = _paths(capsule.include_paths, prefix + " include_paths")
    _reject_generated_overlap(generated_targets, required_roots, include_paths, prefix)
    excluded_categories = _excluded_categories(capsule.excluded_categories, prefix)
    if capsule.secret_detector != SECRET_DETECTOR:
        raise ValueError(prefix + " secret_detector must equal " + SECRET_DETECTOR)
    limits = (
        capsule.max_file_bytes,
        capsule.max_capsule_files,
        capsule.max_capsule_utf8_bytes,
        capsule.max_packet_files,
        capsule.max_packet_utf8_bytes,
    )
    if any(not isinstance(value, int) or isinstance(value, bool) or value <= 0 for value in limits):
        raise ValueError(prefix + " limits must be positive integers")
    overrides = []
    names = set()
    for index, override in enumerate(capsule.package_overrides, 1):
        normalized = _normalize_override(override, prefix + " package override " + str(index))
        if normalized.name in names:
            raise ValueError(prefix + " has duplicate package override " + normalized.name)
        names.add(normalized.name)
        _reject_generated_overlap(
            normalized.generated_target_paths,
            normalized.required_roots,
            tuple(sorted(set(include_paths).union(normalized.include_paths))),
            prefix + " package override " + str(index),
        )
        overrides.append(normalized)
    historical_policy_hashes = _policy_hashes(
        capsule.historical_policy_hashes, prefix
    )
    return CapsuleConfig(
        id=capsule.id,
        adapter=capsule.adapter,
        focus_packages=focus_packages,
        source_id=source_id,
        dependency_scope=dependency_scope,
        changed_path_policy=capsule.changed_path_policy,
        default_required_roots=required_roots,
        default_generated_target_paths=generated_targets,
        include_paths=include_paths,
        excluded_categories=excluded_categories,
        secret_detector=capsule.secret_detector,
        max_file_bytes=limits[0],
        max_capsule_files=limits[1],
        max_capsule_utf8_bytes=limits[2],
        max_packet_files=limits[3],
        max_packet_utf8_bytes=limits[4],
        package_overrides=tuple(sorted(overrides, key=lambda item: item.name)),
        historical_policy_hashes=historical_policy_hashes,
    )


def _normalize_override(override: PackageOverride, prefix: str) -> PackageOverride:
    if not isinstance(override, PackageOverride):
        raise ValueError(prefix + " must be a PackageOverride")
    if not validate_npm_package_name(override.name):
        raise ValueError(prefix + " name must be an npm-package-name-v1 value")
    required_roots = _paths(override.required_roots, prefix + " required_roots", required=True)
    generated_targets = _generated_paths(override.generated_target_paths, prefix + " generated_target_paths")
    include_paths = _paths(override.include_paths, prefix + " include_paths")
    _reject_generated_overlap(generated_targets, required_roots, include_paths, prefix)
    return PackageOverride(override.name, required_roots, generated_targets, include_paths)


def _normalize_allowlist(item: SecretAllowlist, prefix: str) -> SecretAllowlist:
    if not isinstance(item, SecretAllowlist):
        raise ValueError(prefix + " must be a SecretAllowlist")
    if not safe_policy_path(item.path):
        raise ValueError(prefix + " path must be a safe repository-relative POSIX path")
    if not isinstance(item.blob_oid, str) or _BLOB_OID.fullmatch(item.blob_oid) is None:
        raise ValueError(prefix + " blob_oid must be 40 or 64 lowercase hexadecimal characters")
    if not isinstance(item.detector_code, str) or not item.detector_code:
        raise ValueError(prefix + " detector_code must be a non-empty string")
    return item


def _policy_payload(capsule: CapsuleConfig, allowlist: Tuple[SecretAllowlist, ...]) -> Dict[str, object]:
    payload = {
        "adapter": capsule.adapter,
        "category_classifier": CATEGORY_CLASSIFIER,
        "changed_path_policy": capsule.changed_path_policy,
        "id": capsule.id,
        "dependency_scope": capsule.dependency_scope,
        "default_required_roots": list(capsule.default_required_roots),
        "default_generated_target_paths": list(capsule.default_generated_target_paths),
        "include_paths": list(capsule.include_paths),
        "excluded_categories": list(capsule.excluded_categories),
        "secret_detector": capsule.secret_detector,
        "workspace_resolver": WORKSPACE_RESOLVERS[capsule.adapter],
        "max_file_bytes": capsule.max_file_bytes,
        "max_capsule_files": capsule.max_capsule_files,
        "max_capsule_utf8_bytes": capsule.max_capsule_utf8_bytes,
        "max_packet_files": capsule.max_packet_files,
        "max_packet_utf8_bytes": capsule.max_packet_utf8_bytes,
        "package_overrides": [
            {
                "name": override.name,
                "required_roots": list(override.required_roots),
                "generated_target_paths": list(override.generated_target_paths),
                "include_paths": list(override.include_paths),
            }
            for override in capsule.package_overrides
        ],
        "secret_allowlist": [
            {"path": item.path, "blob_oid": item.blob_oid, "detector_code": item.detector_code}
            for item in allowlist
        ],
    }
    if capsule.adapter == COMMIT_TREE_ADAPTER:
        payload["source_id"] = capsule.source_id
    else:
        payload["focus_packages"] = list(capsule.focus_packages)
    return payload


def _candidate_blob_keys(value: Sequence[Tuple[str, str]]) -> set:
    candidates = set()
    for index, item in enumerate(value, 1):
        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("selected_candidate_blobs item " + str(index) + " must be a (path, blob_oid) tuple")
        path, blob_oid = item
        if not safe_policy_path(path) or not isinstance(blob_oid, str) or _BLOB_OID.fullmatch(blob_oid) is None:
            raise ValueError("selected_candidate_blobs item " + str(index) + " is invalid")
        candidates.add((path, blob_oid))
    return candidates


def _package_names(value: object, prefix: str, required: bool = False) -> Tuple[str, ...]:
    names = _unique_strings(value, prefix, allow_empty=not required)
    if any(not validate_npm_package_name(name) for name in names):
        raise ValueError(prefix + " must contain npm-package-name-v1 values")
    return names


def _paths(value: object, prefix: str, required: bool = False) -> Tuple[str, ...]:
    paths = _unique_strings(value, prefix, allow_empty=not required)
    if any(not safe_policy_path(path) for path in paths):
        raise ValueError(prefix + " must contain safe package-relative POSIX paths")
    return paths


def _generated_paths(value: object, prefix: str) -> Tuple[str, ...]:
    paths = _unique_strings(value, prefix, allow_empty=True)
    for path in paths:
        bare_path = path[:-1] if path.endswith("/") else path
        if path.endswith("//") or not bare_path or not safe_policy_path(bare_path):
            raise ValueError(prefix + " must contain safe generated file paths or directory prefixes")
    return paths


def _excluded_categories(value: object, prefix: str) -> Tuple[str, ...]:
    categories = _unique_strings(value, prefix + " excluded_categories", allow_empty=True)
    if any(category not in EXCLUDED_CATEGORIES for category in categories):
        raise ValueError(prefix + " excluded_categories contains an unknown category")
    return categories


def _policy_hashes(value: object, prefix: str) -> Tuple[str, ...]:
    hashes = _unique_strings(value, prefix + " historical_policy_hashes", allow_empty=True)
    if any(_SHA256.fullmatch(value) is None for value in hashes):
        raise ValueError(prefix + " historical_policy_hashes must contain SHA-256 values")
    return hashes


def _unique_strings(value: object, prefix: str, allow_empty: bool) -> Tuple[str, ...]:
    if not isinstance(value, (tuple, list)) or not all(isinstance(item, str) for item in value):
        raise ValueError(prefix + " must be an array of strings")
    values = tuple(value)
    if not allow_empty and not values:
        raise ValueError(prefix + " must not be empty")
    if len(set(values)) != len(values):
        raise ValueError(prefix + " contains duplicate values")
    return tuple(sorted(values))


def _reject_generated_overlap(
    generated_paths: Sequence[str], required_roots: Sequence[str], include_paths: Sequence[str], prefix: str
) -> None:
    for generated in generated_paths:
        candidate = generated[:-1] if generated.endswith("/") else generated
        for selected in tuple(required_roots) + tuple(include_paths):
            if _paths_overlap(candidate, selected):
                raise ValueError(prefix + " generated target overlaps required root or include path")


def _paths_overlap(left: str, right: str) -> bool:
    return left == right or left.startswith(right + "/") or right.startswith(left + "/")


def _exact_keys(row: Dict[str, object], required: set, optional: set, prefix: str) -> None:
    missing = sorted(required - set(row))
    if missing:
        raise ValueError(prefix + " missing required key " + missing[0])
    unexpected = sorted(set(row) - required - optional)
    if unexpected:
        raise ValueError(prefix + " contains unknown key " + unexpected[0])


def _required_string(row: Dict[str, object], key: str, prefix: str) -> str:
    value = row[key]
    if not isinstance(value, str) or not value:
        raise ValueError(prefix + " " + key + " must be a non-empty string")
    return value


def _optional_string(
    row: Dict[str, object], key: str, default: str, prefix: str, allow_empty: bool = False
) -> str:
    value = row.get(key, default)
    if not isinstance(value, str) or (not allow_empty and not value):
        qualifier = "a string" if allow_empty else "a non-empty string"
        raise ValueError(prefix + " " + key + " must be " + qualifier)
    return value


def _strings(
    row: Dict[str, object], key: str, prefix: str, required: bool = False, default: Iterable[str] = ()
) -> Tuple[str, ...]:
    value = tuple(default) if key not in row else row[key]
    return _unique_strings(value, prefix + " " + key, allow_empty=not required)


def _positive_int(row: Dict[str, object], key: str, default: int, prefix: str) -> int:
    value = row.get(key, default)
    if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
        raise ValueError(prefix + " " + key + " must be a positive integer")
    return value


def _prefix(repository_index: int) -> str:
    return "registry row " + str(repository_index)


__all__ = [
    "COMMIT_TREE_ADAPTER",
    "CapsuleConfig",
    "EffectivePolicy",
    "PackageOverride",
    "SecretAllowlist",
    "build_effective_policy",
    "parse_capsules",
    "parse_secret_allowlist",
]
