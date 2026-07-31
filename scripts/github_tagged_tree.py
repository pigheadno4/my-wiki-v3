"""Deterministic synthetic workspace resolution for one tagged repository tree."""

from typing import Mapping, NoReturn

from github_capsule_policy import (
    TAGGED_TREE_ADAPTER,
    CapsuleConfig,
    build_effective_policy,
)
from github_git_tree import GitTree
from github_npm_workspace import WorkspacePackage, WorkspaceResolution


_REGULAR_MODES = frozenset(("100644", "100755"))


def resolve_tagged_workspace(
    tree: GitTree,
    capsule: CapsuleConfig,
    versions: Mapping[str, str],
) -> WorkspaceResolution:
    """Resolve configured repository paths as one synthetic release package."""
    if not isinstance(tree, GitTree):
        raise TypeError("tree must be a GitTree")
    if not isinstance(capsule, CapsuleConfig) or capsule.adapter != TAGGED_TREE_ADAPTER:
        raise ValueError("capsule must use " + TAGGED_TREE_ADAPTER)
    if not isinstance(versions, Mapping):
        raise TypeError("versions must be a mapping")

    normalized = build_effective_policy(capsule, (), (), ()).capsule
    if normalized.default_generated_target_paths:
        _review(
            "unsupported-tagged-policy",
            "tagged-tree-v1 does not use generated target paths",
        )
    if normalized.package_overrides:
        _review(
            "unsupported-tagged-policy",
            "tagged-tree-v1 does not use package overrides",
        )
    package_name = normalized.focus_packages[0]
    if set(versions) != {package_name}:
        raise ValueError("versions must contain exactly the focus package")
    version = versions[package_name]
    if not isinstance(version, str) or not version:
        raise ValueError("focus package version must be a non-empty string")

    regular_paths = frozenset(
        blob.path for blob in tree.blobs() if blob.mode in _REGULAR_MODES
    )
    owned_paths = set()
    for root in normalized.default_required_roots:
        matches = {
            path for path in regular_paths if path.startswith(root + "/")
        }
        if not matches:
            _review(
                "missing-required-root",
                "package=" + package_name + " path=" + root,
            )
        owned_paths.update(matches)
    for path in normalized.include_paths:
        if path not in regular_paths:
            _review(
                "missing-required-include",
                "package=" + package_name + " path=" + path,
            )
        owned_paths.add(path)

    package = WorkspacePackage(
        name=package_name,
        path="",
        version=version,
        reason="focus",
        owned_paths=tuple(sorted(owned_paths)),
    )
    return WorkspaceResolution(
        packages=(package,),
        dependency_edges=(),
        external_dependencies=(),
        declared_targets=(),
    )


def _review(code: str, detail: str) -> NoReturn:
    raise ValueError("needs-policy-review:" + code + ": " + detail[:500])


__all__ = ["resolve_tagged_workspace"]
