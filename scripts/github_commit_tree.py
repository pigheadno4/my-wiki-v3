"""Deterministic workspace resolution for one exact repository commit tree."""

from typing import NoReturn

from github_capsule_policy import (
    COMMIT_TREE_ADAPTER,
    CapsuleConfig,
    build_effective_policy,
)
from github_git_tree import GitTree
from github_npm_workspace import WorkspacePackage, WorkspaceResolution


_REGULAR_MODES = frozenset(("100644", "100755"))


def resolve_commit_workspace(
    tree: GitTree,
    capsule: CapsuleConfig,
) -> WorkspaceResolution:
    """Resolve configured repository paths as one unversioned source identity."""
    if not isinstance(tree, GitTree):
        raise TypeError("tree must be a GitTree")
    if not isinstance(capsule, CapsuleConfig) or capsule.adapter != COMMIT_TREE_ADAPTER:
        raise ValueError("capsule must use " + COMMIT_TREE_ADAPTER)

    normalized = build_effective_policy(capsule, (), (), ()).capsule
    regular_paths = frozenset(
        blob.path for blob in tree.blobs() if blob.mode in _REGULAR_MODES
    )
    owned_paths = set()
    for root in normalized.default_required_roots:
        matches = {path for path in regular_paths if path.startswith(root + "/")}
        if not matches:
            _review(
                "missing-required-root",
                "source=" + normalized.source_id + " path=" + root,
            )
        owned_paths.update(matches)
    for path in normalized.include_paths:
        if path not in regular_paths:
            _review(
                "missing-required-include",
                "source=" + normalized.source_id + " path=" + path,
            )
        owned_paths.add(path)

    package = WorkspacePackage(
        name=normalized.source_id,
        path="",
        version="",
        reason="repository-source",
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


__all__ = ["resolve_commit_workspace"]
