"""Local Git inspection and exact reference resolution for repository collection."""

from dataclasses import dataclass
import json
from pathlib import Path
import re
import subprocess
from typing import Dict, Iterable, Optional, Sequence, Tuple

from github_registry import RepoConfig


_ERROR_STDERR_LIMIT = 1000
_SEMVER = re.compile(
    r"^v?(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:-([0-9A-Za-z][0-9A-Za-z.-]*))?$"
)
_SCOPED_PACKAGE = re.compile(r"^@[^/@]+/[^@/]+$")
_LFS_FILTER = re.compile(r"(?:^|\s)filter\s*=\s*lfs(?:\s|$)", re.IGNORECASE)


class GitCommandError(RuntimeError):
    """A bounded, actionable failure from a Git subprocess."""

    def __init__(self, args: Sequence[str], returncode: int, stderr: Optional[str]):
        command = "git " + " ".join(args)
        detail = (stderr or "").strip()
        if len(detail) > _ERROR_STDERR_LIMIT:
            detail = detail[:_ERROR_STDERR_LIMIT] + "..."
        message = command + " failed with exit " + str(returncode)
        if detail:
            message += ": " + detail
        super().__init__(message)


class RefResolutionError(ValueError):
    """A selector did not identify exactly one inspected Git reference."""


@dataclass(frozen=True)
class ResolvedRef:
    repo_id: str
    ref_kind: str
    ref_name: str
    sha: str
    version: str
    aliases: Tuple[str, ...]
    upstream_commit_time: str
    release_published_at: Optional[str]


@dataclass(frozen=True)
class RepoInspection:
    default_branch: str
    refs: Tuple[ResolvedRef, ...]
    packages: Tuple[str, ...]
    has_submodules: bool
    has_lfs: bool


def run_git(args: Sequence[str], cwd: Optional[Path] = None) -> str:
    """Run Git without a shell and return its stripped standard output."""
    command = ["git"] + list(args)
    try:
        result = subprocess.run(
            command,
            cwd=str(cwd) if cwd is not None else None,
            check=True,
            text=True,
            capture_output=True,
        )
    except subprocess.CalledProcessError as error:
        raise GitCommandError(list(args), error.returncode, error.stderr) from error
    return result.stdout.strip()


def clone_repository(config: RepoConfig, destination: Path) -> None:
    """Create the required partial no-checkout clone for later exact resolution."""
    run_git(["clone", "--filter=blob:none", "--no-checkout", config.url, str(destination)])


def inspect_repository(config: RepoConfig, clone_path: Path) -> RepoInspection:
    """Discover locally available refs and repository capabilities without network access."""
    default_branch = run_git(["symbolic-ref", "--short", "HEAD"], clone_path)
    if not default_branch:
        raise GitCommandError(["symbolic-ref", "--short", "HEAD"], 1, "repository HEAD has no branch")

    tracked_paths = tuple(
        path for path in run_git(["ls-files", "-z"], clone_path).split("\0") if path
    )
    packages = _discover_packages(clone_path, tracked_paths)
    has_submodules = _has_submodules(clone_path, tracked_paths)
    has_lfs = _has_lfs_declarations(clone_path, tracked_paths)

    tag_names = tuple(
        name
        for name in run_git(
            ["for-each-ref", "--format=%(refname:strip=2)", "refs/tags"], clone_path
        ).splitlines()
        if name
    )
    tag_shas = {
        name: run_git(["rev-list", "-n", "1", "refs/tags/" + name], clone_path)
        for name in tag_names
    }
    aliases_by_sha = _aliases_by_sha(tag_shas)
    commit_times: Dict[str, str] = {}

    def commit_time(sha: str) -> str:
        if sha not in commit_times:
            commit_times[sha] = run_git(["show", "-s", "--format=%cI", sha], clone_path)
        return commit_times[sha]

    default_sha = run_git(["rev-parse", default_branch + "^{commit}"], clone_path)
    branch_ref = ResolvedRef(
        repo_id=config.id,
        ref_kind="branch",
        ref_name=default_branch,
        sha=default_sha,
        version=default_branch,
        aliases=aliases_by_sha.get(default_sha, ()),
        upstream_commit_time=commit_time(default_sha),
        release_published_at=None,
    )
    tag_refs = tuple(
        _tag_ref(config.id, name, tag_shas[name], aliases_by_sha[tag_shas[name]], commit_time(tag_shas[name]))
        for name in sorted(tag_names)
    )
    commit_refs = tuple(
        ResolvedRef(
            repo_id=config.id,
            ref_kind="commit",
            ref_name=sha,
            sha=sha,
            version=sha,
            aliases=aliases_by_sha.get(sha, ()),
            upstream_commit_time=commit_time(sha),
            release_published_at=None,
        )
        for sha in sorted(
            sha
            for sha in run_git(["rev-list", "--all"], clone_path).splitlines()
            if sha != default_sha
        )
    )
    return RepoInspection(
        default_branch=default_branch,
        refs=(branch_ref,) + tag_refs + commit_refs,
        packages=packages,
        has_submodules=has_submodules,
        has_lfs=has_lfs,
    )


def resolve_ref(config: RepoConfig, inspection: RepoInspection, selector: str) -> ResolvedRef:
    """Resolve one explicit selector, never falling back to another reference."""
    if selector == "default-branch":
        return _one(
            (ref for ref in inspection.refs if ref.ref_kind == "branch" and ref.ref_name == inspection.default_branch),
            selector,
        )
    if selector.startswith("tag:"):
        name = selector[4:]
        return _one(
            (ref for ref in inspection.refs if ref.ref_kind != "branch" and ref.ref_name == name),
            selector,
        )
    if selector.startswith("commit:"):
        return _resolve_commit(config, inspection, selector[7:])
    if selector.startswith("package:"):
        package_name, version = _package_selector(selector[8:])
        target = _semver_parts(version)
        return _one(
            (
                ref
                for ref in inspection.refs
                if ref.ref_kind == "package-version"
                and ref.ref_name.startswith(package_name + "@")
                and _semver_parts(ref.version) == target
            ),
            selector,
        )

    target = _semver_parts(selector)
    if target is None:
        raise RefResolutionError("missing selector " + selector)
    return _one(
        (
            ref
            for ref in inspection.refs
            if ref.ref_kind in ("tag", "package-version") and _semver_parts(ref.version) == target
        ),
        selector,
    )


def _resolve_commit(config: RepoConfig, inspection: RepoInspection, value: str) -> ResolvedRef:
    if not _is_full_object_id(value):
        raise RefResolutionError("commit selector must use an exact full SHA")
    matches = [ref for ref in inspection.refs if ref.sha.lower() == value.lower()]
    if not matches:
        raise RefResolutionError("missing selector commit:" + value)
    sha = matches[0].sha
    aliases = tuple(sorted({alias for ref in matches for alias in ref.aliases}))
    return ResolvedRef(
        repo_id=config.id,
        ref_kind="commit",
        ref_name=sha,
        sha=sha,
        version=sha,
        aliases=aliases,
        upstream_commit_time=matches[0].upstream_commit_time,
        release_published_at=None,
    )


def _discover_packages(clone_path: Path, tracked_paths: Iterable[str]) -> Tuple[str, ...]:
    names = set()
    for path in tracked_paths:
        if Path(path).name != "package.json":
            continue
        try:
            data = json.loads(run_git(["show", "HEAD:" + path], clone_path))
        except (GitCommandError, ValueError):
            continue
        name = data.get("name") if isinstance(data, dict) else None
        if isinstance(name, str) and name:
            names.add(name)
    return tuple(sorted(names))


def _has_submodules(clone_path: Path, tracked_paths: Iterable[str]) -> bool:
    if ".gitmodules" in tracked_paths:
        return True
    entries = run_git(["ls-files", "--stage", "-z"], clone_path).split("\0")
    return any(entry.startswith("160000 ") for entry in entries if entry)


def _has_lfs_declarations(clone_path: Path, tracked_paths: Iterable[str]) -> bool:
    for path in tracked_paths:
        if Path(path).name != ".gitattributes":
            continue
        attributes = run_git(["show", "HEAD:" + path], clone_path)
        if _LFS_FILTER.search(attributes):
            return True
    return False


def _tag_ref(repo_id: str, name: str, sha: str, aliases: Tuple[str, ...], commit_time: str) -> ResolvedRef:
    package = _package_tag(name)
    if package is not None:
        _, version = package
        return ResolvedRef(
            repo_id=repo_id,
            ref_kind="package-version",
            ref_name=name,
            sha=sha,
            version=version,
            aliases=aliases,
            upstream_commit_time=commit_time,
            release_published_at=None,
        )
    parsed = _semver_parts(name)
    version = name[1:] if parsed is not None and name.startswith("v") else name
    return ResolvedRef(
        repo_id=repo_id,
        ref_kind="tag",
        ref_name=name,
        sha=sha,
        version=version,
        aliases=aliases,
        upstream_commit_time=commit_time,
        release_published_at=None,
    )


def _aliases_by_sha(tag_shas: Dict[str, str]) -> Dict[str, Tuple[str, ...]]:
    aliases: Dict[str, list] = {}
    for name, sha in tag_shas.items():
        aliases.setdefault(sha, []).append(name)
    return {sha: tuple(sorted(names)) for sha, names in aliases.items()}


def _package_tag(name: str) -> Optional[Tuple[str, str]]:
    if not name.startswith("@"):
        return None
    package_name, separator, version = name.rpartition("@")
    if not separator or not _SCOPED_PACKAGE.fullmatch(package_name) or _semver_parts(version) is None:
        return None
    return package_name, version


def _package_selector(value: str) -> Tuple[str, str]:
    package = _package_tag(value)
    if package is None:
        raise RefResolutionError("package selector must include a scoped package namespace")
    return package


def _semver_parts(value: str) -> Optional[Tuple[int, int, int]]:
    match = _SEMVER.fullmatch(value)
    if match is None:
        return None
    return int(match.group(1)), int(match.group(2) or 0), int(match.group(3) or 0)


def _is_full_object_id(value: str) -> bool:
    return len(value) in (40, 64) and all(character in "0123456789abcdefABCDEF" for character in value)


def _one(candidates: Iterable[ResolvedRef], selector: str) -> ResolvedRef:
    matches = tuple(candidates)
    if not matches:
        raise RefResolutionError("missing selector " + selector)
    if len(matches) != 1:
        raise RefResolutionError("ambiguous selector " + selector)
    return matches[0]
