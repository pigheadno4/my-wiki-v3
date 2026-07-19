"""Deterministic NPM workspace and package-export resolution at one Git SHA."""

from dataclasses import dataclass
import posixpath
import re
from typing import Dict, List, Mapping, NoReturn, Sequence, Set, Tuple

from github_canonical import safe_policy_path, validate_npm_package_name
from github_capsule_policy import CAPSULE_ADAPTER, CapsuleConfig
from github_git_tree import GitBlob, GitTree


_REGULAR_MODES = frozenset(("100644", "100755"))
_DEPENDENCY_FIELDS = (
    ("dependencies", "dependency", False),
    ("optionalDependencies", "optional-dependency", True),
    ("peerDependencies", "peer-dependency", False),
)
_REASON_FOR_KIND = {
    "dependency": "internal-dependency",
    "optional-dependency": "internal-optional-dependency",
    "peer-dependency": "internal-peer-dependency",
}
_REASON_PRIORITY = {
    "focus": 0,
    "internal-dependency": 1,
    "internal-optional-dependency": 2,
    "internal-peer-dependency": 3,
}
_PERCENT_SEPARATOR = re.compile(r"%(?:2f|5c)", re.IGNORECASE)


@dataclass(frozen=True)
class WorkspacePackage:
    name: str
    path: str
    version: str
    reason: str
    files: Tuple[str, ...] = ()
    tracked_declaration_roots: Tuple[str, ...] = ()


@dataclass(frozen=True)
class DependencyEdge:
    from_package: str
    to_package: str
    dependency_kind: str
    specification: str
    optional: bool


@dataclass(frozen=True)
class DeclaredTarget:
    package: str
    field: str
    json_pointer: str
    condition_chain: Tuple[str, ...]
    array_indices: Tuple[int, ...]
    target: str
    status: str
    generated_policy_path: str
    matched_paths: Tuple[str, ...]


@dataclass(frozen=True)
class WorkspaceResolution:
    packages: Tuple[WorkspacePackage, ...]
    dependency_edges: Tuple[DependencyEdge, ...]
    external_dependencies: Tuple[DependencyEdge, ...]
    declared_targets: Tuple[DeclaredTarget, ...]


@dataclass(frozen=True)
class _DiscoveredPackage:
    name: str
    path: str
    version: str
    manifest: Mapping[str, object]
    files: Tuple[str, ...]
    blobs: Mapping[str, GitBlob]
    foreign_blobs: Mapping[str, GitBlob]


@dataclass(frozen=True)
class _ExportMatch:
    public_path: str
    path: str
    blob: GitBlob
    foreign: bool


@dataclass(frozen=True)
class _ExportLeaf:
    target: DeclaredTarget
    public_matches: Tuple[_ExportMatch, ...]


def resolve_workspace(tree: GitTree, capsule: CapsuleConfig) -> WorkspaceResolution:
    """Resolve one capsule's package closure and statically enumerable targets."""
    if not isinstance(tree, GitTree):
        raise TypeError("tree must be a GitTree")
    if not isinstance(capsule, CapsuleConfig) or capsule.adapter != CAPSULE_ADAPTER:
        raise ValueError("capsule must use " + CAPSULE_ADAPTER)

    all_blobs = tree.blobs()
    blobs_by_path = {blob.path: blob for blob in all_blobs}
    root_manifest = _read_manifest(tree, blobs_by_path, "")
    package_paths = _discover_package_paths(root_manifest, all_blobs)
    owned_blobs, foreign_blobs = _assign_package_blobs(package_paths, blobs_by_path)
    packages = tuple(
        _read_package(
            tree,
            blobs_by_path,
            path,
            owned_blobs[path],
            foreign_blobs[path],
        )
        for path in package_paths
    )
    packages_by_name = _index_packages(packages)
    packages_by_path = {package.path: package for package in packages}

    reasons: Dict[str, str] = {}
    for name in capsule.focus_packages:
        if name not in packages_by_name:
            _review("ambiguous-package", "focus package is not uniquely discovered: " + name)
        reasons[name] = "focus"

    normalized_by_name = {
        package.name: _normalized_dependencies(package.manifest, package.name)
        for package in packages
    }
    internal_edges: Set[DependencyEdge] = set()
    external_edges: Set[DependencyEdge] = set()
    pending = set(reasons)
    visited: Set[str] = set()
    while pending:
        package_name = min(pending)
        pending.remove(package_name)
        if package_name in visited:
            continue
        visited.add(package_name)
        package = packages_by_name[package_name]
        for edge in normalized_by_name[package_name]:
            if edge.specification.startswith(("file:", "link:")):
                _validate_local_dependency(edge, package, packages_by_path)
            if edge.to_package in packages_by_name:
                if edge in internal_edges:
                    _review("duplicate-dependency-edge", "duplicate normalized dependency edge")
                internal_edges.add(edge)
                reason = _REASON_FOR_KIND[edge.dependency_kind]
                current = reasons.get(edge.to_package)
                if current is None or _REASON_PRIORITY[reason] < _REASON_PRIORITY[current]:
                    reasons[edge.to_package] = reason
                if edge.to_package not in visited:
                    pending.add(edge.to_package)
            else:
                if edge in external_edges:
                    _review("duplicate-dependency-edge", "duplicate normalized external dependency edge")
                external_edges.add(edge)

    declared_targets: List[DeclaredTarget] = []
    output_packages: List[WorkspacePackage] = []
    for name in sorted(reasons):
        package = packages_by_name[name]
        generated_paths = _generated_paths_for(package.name, capsule)
        package_targets, declaration_roots = _resolve_declarations(package, generated_paths)
        declared_targets.extend(package_targets)
        output_packages.append(
            WorkspacePackage(
                package.name,
                package.path,
                package.version,
                reasons[name],
                package.files,
                tuple(sorted(declaration_roots)),
            )
        )

    return WorkspaceResolution(
        tuple(output_packages),
        tuple(sorted(internal_edges, key=_edge_key)),
        tuple(sorted(external_edges, key=_edge_key)),
        tuple(sorted(declared_targets, key=_declared_target_key)),
    )


def _read_manifest(tree: GitTree, blobs_by_path: Mapping[str, GitBlob], package_path: str) -> Mapping[str, object]:
    manifest_path = _join(package_path, "package.json")
    blob = blobs_by_path.get(manifest_path)
    if blob is None:
        _review("missing-package-manifest", "workspace directory has no package.json: " + (package_path or "."))
    if blob.mode not in _REGULAR_MODES:
        _review("missing-package-manifest", "package.json is not a regular tracked blob: " + manifest_path)
    try:
        value = tree.read_json(manifest_path)
    except ValueError as error:
        if str(error).startswith("duplicate JSON key:"):
            raise
        _review("malformed-package-manifest", "cannot parse " + manifest_path)
    if not isinstance(value, dict):
        _review("malformed-package-manifest", "package manifest must be an object: " + manifest_path)
    return value


def _read_package(
    tree: GitTree,
    blobs_by_path: Mapping[str, GitBlob],
    package_path: str,
    package_blobs: Mapping[str, GitBlob],
    foreign_blobs: Mapping[str, GitBlob],
) -> _DiscoveredPackage:
    value = _read_manifest(tree, blobs_by_path, package_path)
    name = value.get("name")
    version = value.get("version")
    if not validate_npm_package_name(name) or not isinstance(version, str) or not version:
        _review("invalid-package-identity", "package name and version must be valid strings: " + (package_path or "."))
    files = _package_files(value, name)
    return _DiscoveredPackage(
        name,
        package_path,
        version,
        value,
        files,
        dict(package_blobs),
        dict(foreign_blobs),
    )


def _discover_package_paths(root_manifest: Mapping[str, object], blobs: Sequence[GitBlob]) -> Tuple[str, ...]:
    patterns = _workspace_patterns(root_manifest)
    directories: Set[str] = set()
    for blob in blobs:
        parts = blob.path.split("/")[:-1]
        for index in range(1, len(parts) + 1):
            directories.add("/".join(parts[:index]))
    discovered = {""}
    for pattern in patterns:
        pattern_parts = pattern.split("/")
        for directory in directories:
            parts = directory.split("/")
            if len(parts) != len(pattern_parts):
                continue
            if all(expected == "*" or expected == actual for expected, actual in zip(pattern_parts, parts)):
                discovered.add(directory)
    return tuple(sorted(discovered))


def _assign_package_blobs(
    package_paths: Sequence[str],
    blobs_by_path: Mapping[str, GitBlob],
) -> Tuple[Dict[str, Dict[str, GitBlob]], Dict[str, Dict[str, GitBlob]]]:
    owned: Dict[str, Dict[str, GitBlob]] = {path: {} for path in package_paths}
    foreign: Dict[str, Dict[str, GitBlob]] = {path: {} for path in package_paths}
    deepest_first = tuple(
        sorted(
            package_paths,
            key=lambda path: (-(path.count("/") + 1 if path else 0), path),
        )
    )
    for repository_path, blob in blobs_by_path.items():
        owner = next(
            path
            for path in deepest_first
            if not path or repository_path.startswith(path + "/")
        )
        relative_path = repository_path[len(owner) + 1 :] if owner else repository_path
        owned[owner][relative_path] = blob
        for ancestor in package_paths:
            if ancestor == owner:
                continue
            if not ancestor or repository_path.startswith(ancestor + "/"):
                ancestor_relative = (
                    repository_path[len(ancestor) + 1 :]
                    if ancestor
                    else repository_path
                )
                foreign[ancestor][ancestor_relative] = blob
    return owned, foreign


def _workspace_patterns(root_manifest: Mapping[str, object]) -> Tuple[str, ...]:
    if "workspaces" not in root_manifest:
        return ()
    value = root_manifest["workspaces"]
    if isinstance(value, list):
        patterns = value
    elif isinstance(value, dict):
        if set(value) not in ({"packages"}, {"packages", "nohoist"}):
            _review("unsupported-workspace", "workspace object has unsupported keys")
        patterns = value.get("packages")
        nohoist = value.get("nohoist", [])
        if not _nonempty_string_list(nohoist, allow_empty=True):
            _review("unsupported-workspace", "nohoist must be a list of strings")
    else:
        _review("unsupported-workspace", "workspaces must be a list or object")
    if not _nonempty_string_list(patterns, allow_empty=False):
        _review("unsupported-workspace", "workspace packages must be a non-empty string list")
    if len(set(patterns)) != len(patterns):
        _review("unsupported-workspace", "workspace patterns must be unique")
    for pattern in patterns:
        _validate_workspace_pattern(pattern)
    return tuple(patterns)


def _validate_workspace_pattern(pattern: str) -> None:
    if (
        not pattern
        or pattern.startswith(("/", "!"))
        or "\\" in pattern
        or "**" in pattern
        or any(character in pattern for character in "{}[]")
    ):
        _review("unsupported-workspace", "unsupported workspace pattern: " + repr(pattern))
    parts = pattern.split("/")
    if any(part in ("", ".", "..") or ("*" in part and part != "*") for part in parts):
        _review("unsupported-workspace", "unsupported workspace pattern: " + repr(pattern))


def _index_packages(packages: Sequence[_DiscoveredPackage]) -> Dict[str, _DiscoveredPackage]:
    result: Dict[str, _DiscoveredPackage] = {}
    for package in packages:
        if package.name in result:
            _review("duplicate-package-name", "duplicate workspace package name: " + package.name)
        result[package.name] = package
    return result


def _package_files(manifest: Mapping[str, object], package_name: str) -> Tuple[str, ...]:
    if "files" not in manifest:
        return ()
    value = manifest["files"]
    if not isinstance(value, list) or not all(isinstance(item, str) and item for item in value):
        _review("invalid-declaration", "files must be a list of non-empty strings in " + package_name)
    if len(set(value)) != len(value):
        _review("invalid-declaration", "files contains duplicate values in " + package_name)
    return tuple(sorted(value))


def _normalized_dependencies(manifest: Mapping[str, object], package_name: str) -> Tuple[DependencyEdge, ...]:
    mappings: Dict[str, Mapping[str, str]] = {}
    for field, _, _ in _DEPENDENCY_FIELDS:
        value = manifest.get(field, {})
        if not isinstance(value, dict) or not all(
            isinstance(name, str)
            and validate_npm_package_name(name)
            and isinstance(specification, str)
            for name, specification in value.items()
        ):
            _review("malformed-dependency-metadata", field + " must map package names to strings in " + package_name)
        mappings[field] = value

    peer_meta = manifest.get("peerDependenciesMeta", {})
    peers = mappings["peerDependencies"]
    if not isinstance(peer_meta, dict):
        _review("malformed-dependency-metadata", "peerDependenciesMeta must be an object in " + package_name)
    for name, metadata in peer_meta.items():
        if name not in peers or not isinstance(metadata, dict) or set(metadata) != {"optional"}:
            _review("malformed-dependency-metadata", "invalid peer dependency metadata in " + package_name)
        if not isinstance(metadata["optional"], bool):
            _review("malformed-dependency-metadata", "peer optional metadata must be Boolean in " + package_name)

    edges: List[DependencyEdge] = []
    optional_names = set(mappings["optionalDependencies"])
    for name, specification in mappings["dependencies"].items():
        if name not in optional_names:
            edges.append(DependencyEdge(package_name, name, "dependency", specification, False))
    for name, specification in mappings["optionalDependencies"].items():
        edges.append(DependencyEdge(package_name, name, "optional-dependency", specification, True))
    for name, specification in peers.items():
        optional = bool(peer_meta.get(name, {}).get("optional", False))
        edges.append(DependencyEdge(package_name, name, "peer-dependency", specification, optional))
    if len(edges) != len(set(edges)):
        _review("duplicate-dependency-edge", "duplicate normalized dependency edge in " + package_name)
    return tuple(sorted(edges, key=_edge_key))


def _validate_local_dependency(
    edge: DependencyEdge,
    source: _DiscoveredPackage,
    packages_by_path: Mapping[str, _DiscoveredPackage],
) -> None:
    target = edge.specification.split(":", 1)[1]
    if not target or target.startswith("/") or "\\" in target or "\x00" in target:
        _review("unsafe-local-dependency", "unsafe local dependency from " + source.name)
    resolved = posixpath.normpath(posixpath.join(source.path, target))
    if resolved == ".":
        resolved = ""
    if resolved == ".." or resolved.startswith("../") or "/../" in resolved:
        _review("unsafe-local-dependency", "local dependency escapes repository from " + source.name)
    package = packages_by_path.get(resolved)
    if package is None or package.name != edge.to_package:
        _review("unsafe-local-dependency", "local dependency does not identify its named workspace package")


def _generated_paths_for(package_name: str, capsule: CapsuleConfig) -> Tuple[str, ...]:
    override = next((item for item in capsule.package_overrides if item.name == package_name), None)
    return tuple(capsule.default_generated_target_paths if override is None else override.generated_target_paths)


def _resolve_declarations(
    package: _DiscoveredPackage,
    generated_paths: Sequence[str],
) -> Tuple[Tuple[DeclaredTarget, ...], Set[str]]:
    targets: List[DeclaredTarget] = []
    declaration_roots: Set[str] = set()
    for field in ("main", "module", "types", "typings"):
        if field not in package.manifest:
            continue
        value = package.manifest[field]
        if not isinstance(value, str):
            _review("invalid-declaration", field + " must be a string in " + package.name)
        target = _literal_declared_target(package, field, "/" + field, value, generated_paths)
        targets.append(target)
        if field in ("types", "typings") and target.status == "tracked-required":
            declaration_roots.add(_declaration_root(target.matched_paths[0]))

    if "bin" in package.manifest:
        value = package.manifest["bin"]
        if isinstance(value, str):
            targets.append(_literal_declared_target(package, "bin", "/bin", value, generated_paths))
        elif isinstance(value, dict) and all(
            isinstance(name, str) and isinstance(target, str)
            for name, target in value.items()
        ):
            for name, target_value in value.items():
                targets.append(
                    _literal_declared_target(
                        package,
                        "bin",
                        "/bin/" + _pointer_segment(name),
                        target_value,
                        generated_paths,
                    )
                )
        else:
            _review("invalid-declaration", "bin must be a string or string map in " + package.name)

    if "exports" in package.manifest:
        walker = _ExportWalker(package, generated_paths)
        export_targets, export_roots = walker.resolve(package.manifest["exports"])
        targets.extend(export_targets)
        declaration_roots.update(export_roots)
    return tuple(targets), declaration_roots


def _literal_declared_target(
    package: _DiscoveredPackage,
    field: str,
    pointer: str,
    declared: str,
    generated_paths: Sequence[str],
) -> DeclaredTarget:
    normalized = declared[2:] if declared.startswith("./") else declared
    if "*" in normalized or not safe_policy_path(normalized):
        _review("invalid-declaration", "unsafe " + field + " target in " + package.name)
    status, policy, matches = _literal_status(package, normalized, generated_paths)
    return DeclaredTarget(package.name, field, pointer, (), (), declared, status, policy, matches)


class _ExportWalker:
    def __init__(self, package: _DiscoveredPackage, generated_paths: Sequence[str]):
        self.package = package
        self.generated_paths = tuple(generated_paths)
        self.declaration_roots: Set[str] = set()

    def resolve(self, value: object) -> Tuple[Tuple[DeclaredTarget, ...], Set[str]]:
        if isinstance(value, dict) and self._object_kind(value) == "subpath":
            leaves = self._subpath_map(value, "/exports")
        else:
            leaves = self._walk(".", value, "/exports", (), ())
        targets = tuple(self._finalize_leaf(leaf) for leaf in leaves)
        return targets, self.declaration_roots

    def _finalize_leaf(self, leaf: _ExportLeaf) -> DeclaredTarget:
        target = leaf.target
        if target.status == "tracked-pattern-required":
            foreign_matches = tuple(match for match in leaf.public_matches if match.foreign)
            if foreign_matches:
                selected = next(
                    (
                        match
                        for match in foreign_matches
                        if not safe_policy_path(match.path)
                        or match.blob.mode not in _REGULAR_MODES
                    ),
                    foreign_matches[0],
                )
                _reject_foreign_target(self.package, selected.path, selected.blob)
            matched_paths = tuple(sorted({match.path for match in leaf.public_matches}))
            for path in matched_paths:
                blob = self.package.blobs[path]
                if not safe_policy_path(path):
                    _review("unsafe-declared-target", "export pattern selects an unsafe tracked path")
                if blob.mode not in _REGULAR_MODES:
                    _review("unsafe-declared-target", "export pattern selects a non-regular tracked entry")
            target = DeclaredTarget(
                target.package,
                target.field,
                target.json_pointer,
                target.condition_chain,
                target.array_indices,
                target.target,
                target.status,
                target.generated_policy_path,
                matched_paths,
            )
        if target.status.startswith("tracked") and "types" in target.condition_chain:
            for path in target.matched_paths:
                self.declaration_roots.add(_declaration_root(path))
        return target

    def _subpath_map(self, value: Mapping[str, object], pointer: str) -> Tuple[_ExportLeaf, ...]:
        keys = tuple(value)
        for key in keys:
            _validate_subpath_key(key)
        leaves: List[_ExportLeaf] = []
        claimed: Set[str] = set()
        blocking_patterns: List[str] = []
        for key in sorted(keys, key=_subpath_precedence):
            child_pointer = pointer + "/" + _pointer_segment(key)
            child = self._walk(key, value[key], child_pointer, (), ())
            filtered: List[_ExportLeaf] = []
            public_for_key: Set[str] = set()
            for leaf in child:
                matches = tuple(
                    match
                    for match in leaf.public_matches
                    if match.public_path not in claimed
                    and not any(
                        _subpath_pattern_matches(pattern, match.public_path)
                        for pattern in blocking_patterns
                    )
                )
                public_for_key.update(match.public_path for match in matches)
                target = leaf.target
                if matches != leaf.public_matches:
                    target = DeclaredTarget(
                        target.package,
                        target.field,
                        target.json_pointer,
                        target.condition_chain,
                        target.array_indices,
                        target.target,
                        target.status,
                        target.generated_policy_path,
                        tuple(sorted({match.path for match in matches})),
                    )
                filtered.append(_ExportLeaf(target, matches))
            leaves.extend(filtered)
            if "*" not in key:
                claimed.add(key)
            else:
                claimed.update(public_for_key)
                blocking_patterns.append(key)
        return tuple(leaves)

    def _walk(
        self,
        subpath: str,
        value: object,
        pointer: str,
        conditions: Tuple[str, ...],
        array_indices: Tuple[int, ...],
    ) -> Tuple[_ExportLeaf, ...]:
        if value is None:
            target = DeclaredTarget(
                self.package.name,
                "exports",
                pointer,
                conditions,
                array_indices,
                "",
                "blocked-export",
                "",
                (),
            )
            return (_ExportLeaf(target, ()),)
        if isinstance(value, str):
            return (self._string_leaf(subpath, value, pointer, conditions, array_indices),)
        if isinstance(value, list):
            result: List[_ExportLeaf] = []
            for index, child in enumerate(value):
                result.extend(
                    self._walk(
                        subpath,
                        child,
                        pointer + "/" + str(index),
                        conditions,
                        array_indices + (index,),
                    )
                )
            return tuple(result)
        if isinstance(value, dict):
            kind = self._object_kind(value)
            if kind == "subpath":
                _review("invalid-exports", "nested subpath map is not supported")
            result = []
            for condition, child in value.items():
                result.extend(
                    self._walk(
                        subpath,
                        child,
                        pointer + "/" + _pointer_segment(condition),
                        conditions + (condition,),
                        array_indices,
                    )
                )
            return tuple(result)
        _review("invalid-exports", "unsupported exports scalar")

    def _object_kind(self, value: Mapping[str, object]) -> str:
        if not value:
            _review("invalid-exports", "exports objects must not be empty")
        keys = tuple(value)
        if any(not isinstance(key, str) or not key or key.isdigit() for key in keys):
            _review("invalid-exports", "exports keys must be non-empty non-numeric strings")
        subpath = tuple(key.startswith(".") for key in keys)
        if any(subpath) and not all(subpath):
            _review("invalid-exports", "exports objects cannot mix subpaths and conditions")
        if all(subpath):
            for key in keys:
                _validate_subpath_key(key)
            return "subpath"
        return "condition"

    def _string_leaf(
        self,
        subpath: str,
        declared: str,
        pointer: str,
        conditions: Tuple[str, ...],
        array_indices: Tuple[int, ...],
    ) -> _ExportLeaf:
        normalized = _normalize_export_target(declared)
        key_stars = subpath.count("*")
        target_stars = normalized.count("*")
        if key_stars != target_stars or key_stars not in (0, 1):
            _review("invalid-exports", "export patterns require one star in key and target")
        if key_stars == 0:
            status, policy, matched = _literal_status(self.package, normalized, self.generated_paths)
            public_matches = tuple(
                _ExportMatch(subpath, path, self.package.blobs[path], False)
                for path in matched
            )
        else:
            status, policy, public_matches = _pattern_status(
                self.package,
                subpath,
                normalized,
                self.generated_paths,
            )
            matched = tuple(sorted({match.path for match in public_matches}))
        target = DeclaredTarget(
            self.package.name,
            "exports",
            pointer,
            conditions,
            array_indices,
            declared,
            status,
            policy,
            matched,
        )
        return _ExportLeaf(target, public_matches)


def _normalize_export_target(value: str) -> str:
    if not value.startswith("./") or value.startswith("././"):
        _review("invalid-exports", "export target must begin with exactly ./")
    normalized = value[2:]
    if (
        not normalized
        or "\\" in normalized
        or "\x00" in normalized
        or _PERCENT_SEPARATOR.search(normalized)
        or any(part in ("", ".", "..", "node_modules") for part in normalized.split("/"))
    ):
        _review("invalid-exports", "unsafe export target")
    if "*" in normalized and any(character in normalized for character in "{}[]"):
        _review("invalid-exports", "export patterns do not support braces or character classes")
    return normalized


def _validate_subpath_key(key: str) -> None:
    if key == ".":
        return
    if not key.startswith("./"):
        _review("invalid-exports", "invalid export subpath key")
    remainder = key[2:]
    if (
        not remainder
        or key.endswith("/")
        or "\\" in remainder
        or _PERCENT_SEPARATOR.search(remainder)
        or any(part in ("", ".", "..", "node_modules") for part in remainder.split("/"))
        or remainder.count("*") not in (0, 1)
        or ("*" in remainder and any(character in remainder for character in "{}[]"))
    ):
        _review("invalid-exports", "unsafe export subpath key")


def _literal_status(
    package: _DiscoveredPackage,
    normalized: str,
    generated_paths: Sequence[str],
) -> Tuple[str, str, Tuple[str, ...]]:
    foreign_blob = package.foreign_blobs.get(normalized)
    if foreign_blob is not None:
        _reject_foreign_target(package, normalized, foreign_blob)
    blob = package.blobs.get(normalized)
    if blob is not None:
        if blob.mode not in _REGULAR_MODES:
            _review("unsafe-declared-target", "declared target is not a regular tracked blob")
        return "tracked-required", "", (normalized,)
    policy = _matching_generated_literal(normalized, generated_paths)
    if policy:
        return "generated-target-not-tracked", policy, ()
    _review("untracked-declared-target", "declared target is not tracked or reviewed generated output")


def _pattern_status(
    package: _DiscoveredPackage,
    subpath: str,
    normalized: str,
    generated_paths: Sequence[str],
) -> Tuple[str, str, Tuple[_ExportMatch, ...]]:
    prefix, suffix = normalized.split("*", 1)
    candidates = tuple(
        sorted(
            (
                (path, blob, False)
                for path, blob in package.blobs.items()
            ),
            key=lambda item: item[0],
        )
    ) + tuple(
        sorted(
            (
                (path, blob, True)
                for path, blob in package.foreign_blobs.items()
            ),
            key=lambda item: item[0],
        )
    )
    matches: List[_ExportMatch] = []
    for path, blob, foreign in sorted(candidates, key=lambda item: item[0]):
        if not path.startswith(prefix) or not path.endswith(suffix):
            continue
        stop = len(path) - len(suffix) if suffix else len(path)
        substitution = path[len(prefix) : stop]
        if not substitution:
            continue
        public = subpath.replace("*", substitution)
        matches.append(_ExportMatch(public, path, blob, foreign))
    if matches:
        return "tracked-pattern-required", "", tuple(matches)
    policy = _matching_generated_pattern(prefix, generated_paths)
    if policy:
        return "generated-pattern-not-tracked", policy, ()
    _review("untracked-declared-target", "export pattern has no tracked or reviewed generated match")


def _reject_foreign_target(
    package: _DiscoveredPackage,
    path: str,
    blob: GitBlob,
) -> NoReturn:
    repository_path = _join(package.path, path)
    _review(
        "foreign-package-target",
        "declared target belongs to a deeper package: path="
        + repository_path
        + " mode="
        + blob.mode,
    )


def _matching_generated_literal(path: str, generated_paths: Sequence[str]) -> str:
    for policy in generated_paths:
        if policy.endswith("/"):
            directory = policy[:-1]
            if path.startswith(directory + "/"):
                return policy
        elif path == policy:
            return policy
    return ""


def _matching_generated_pattern(prefix: str, generated_paths: Sequence[str]) -> str:
    for policy in generated_paths:
        if not policy.endswith("/"):
            continue
        directory = policy[:-1]
        if prefix.startswith(directory + "/"):
            return policy
    return ""


def _subpath_precedence(key: str) -> Tuple[int, int, int, str]:
    if "*" not in key:
        return (0, -len(key), 0, key)
    prefix, suffix = key.split("*", 1)
    return (1, -len(prefix), -len(suffix), key)


def _subpath_pattern_matches(pattern: str, value: str) -> bool:
    if "*" not in pattern:
        return pattern == value
    prefix, suffix = pattern.split("*", 1)
    return value.startswith(prefix) and value.endswith(suffix)


def _declaration_root(path: str) -> str:
    return path.split("/", 1)[0] if "/" in path else ""


def _pointer_segment(value: str) -> str:
    return value.replace("~", "~0").replace("/", "~1")


def _declared_target_key(value: DeclaredTarget) -> Tuple[object, ...]:
    return (
        value.package,
        value.field,
        value.json_pointer,
        value.condition_chain,
        value.array_indices,
        value.target,
    )


def _edge_key(value: DependencyEdge) -> Tuple[object, ...]:
    return (
        value.from_package,
        value.to_package,
        value.dependency_kind,
        value.specification,
        value.optional,
    )


def _nonempty_string_list(value: object, allow_empty: bool) -> bool:
    return (
        isinstance(value, list)
        and (allow_empty or bool(value))
        and all(isinstance(item, str) and bool(item) for item in value)
    )


def _join(left: str, right: str) -> str:
    return left + "/" + right if left else right


def _review(code: str, detail: str) -> NoReturn:
    raise ValueError("needs-policy-review:" + code + ": " + detail[:500])


__all__ = [
    "DeclaredTarget",
    "DependencyEdge",
    "WorkspacePackage",
    "WorkspaceResolution",
    "resolve_workspace",
]
