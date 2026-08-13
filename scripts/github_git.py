"""Local Git inspection and exact reference resolution for repository collection."""

from dataclasses import dataclass
import json
from pathlib import Path
import re
import subprocess
from typing import Dict, Iterable, Optional, Sequence, Tuple

from github_registry import RepoConfig
from github_versions import SemanticVersion, compare_semver, matches_semver, parse_package_tag, parse_semver


_ERROR_STDERR_LIMIT = 1000
_GIT_COMMAND_TIMEOUT_SECONDS = 120
_LFS_FILTER = re.compile(r"(?:^|\s)filter\s*=\s*lfs(?:\s|$)", re.IGNORECASE)


class GitCommandError(RuntimeError):
    """A bounded, actionable failure from a Git subprocess."""

    def __init__(self, args: Sequence[str], returncode: int, stderr: Optional[str]):
        self.args = tuple(args)
        self.returncode = returncode
        self.stderr = stderr
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
            timeout=_GIT_COMMAND_TIMEOUT_SECONDS,
        )
    except subprocess.CalledProcessError as error:
        raise GitCommandError(list(args), error.returncode, error.stderr) from error
    except subprocess.TimeoutExpired as error:
        detail = "timed out after " + str(_GIT_COMMAND_TIMEOUT_SECONDS) + " seconds"
        raise GitCommandError(list(args), 124, detail) from error
    return result.stdout.strip()


def clone_repository(config: RepoConfig, destination: Path) -> None:
    """Create the required partial no-checkout clone for later exact resolution."""
    run_git(
        ["clone", "--filter=blob:none", "--no-checkout", "--no-tags", config.url, str(destination)]
    )


def fetch_required_refs(config: RepoConfig, clone_path: Path, selectors: Sequence[str]) -> None:
    """Fetch only the remote refs and objects required to resolve selectors."""
    tag_names = None
    fetched = set()
    for selector in selectors:
        if tag_names is None and _selector_needs_tag_metadata(selector):
            tag_names = _remote_tag_names(clone_path)
        source, destination = _fetch_refspec(selector, tag_names)
        if source == "":
            continue
        refspec = source + ":" + destination
        if refspec not in fetched:
            run_git(["fetch", "--depth=1", "--no-tags", "origin", refspec], clone_path)
            fetched.add(refspec)


def fetch_commit_history(clone_path: Path, sha: str) -> None:
    """Fetch the ancestry required to validate and compare an exact commit boundary."""
    if run_git(["rev-parse", "--is-shallow-repository"], clone_path) != "true":
        return
    destination = "refs/github-collection/commits/" + sha.lower()
    run_git(
        ["fetch", "--unshallow", "--no-tags", "origin", sha + ":" + destination],
        clone_path,
    )


def inspect_repository(config: RepoConfig, clone_path: Path) -> RepoInspection:
    """Discover locally available refs and repository capabilities without network access."""
    default_branch = run_git(["symbolic-ref", "--short", "HEAD"], clone_path)
    if not default_branch:
        raise GitCommandError(["symbolic-ref", "--short", "HEAD"], 1, "repository HEAD has no branch")

    default_sha = run_git(["rev-parse", default_branch + "^{commit}"], clone_path)
    tracked_paths = tuple(
        path
        for path in run_git(["ls-tree", "-r", "-z", "--name-only", default_sha], clone_path).split("\0")
        if path
    )
    packages = _discover_packages(clone_path, default_sha, tracked_paths)
    has_submodules = _has_submodules(clone_path, default_sha, tracked_paths)
    has_lfs = _has_lfs_declarations(clone_path, default_sha, tracked_paths)

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
        return _select_semver_ref(
            (
                ref
                for ref in inspection.refs
                if ref.ref_kind == "package-version" and ref.ref_name.startswith(package_name + "@")
            ),
            parse_semver(version),
            selector,
        )

    target = parse_semver(selector)
    if target is None:
        raise RefResolutionError("missing selector " + selector)
    candidates = tuple(
        ref
        for ref in inspection.refs
        if ref.ref_kind in ("tag", "package-version")
        and _matches_semver(parse_semver(ref.version), target)
    )
    package_names = {
        parse_package_tag(ref.ref_name)[0]
        for ref in candidates
        if ref.ref_kind == "package-version" and parse_package_tag(ref.ref_name) is not None
    }
    if len(package_names) > 1:
        raise RefResolutionError("ambiguous selector " + selector)
    return _select_semver_ref(candidates, target, selector)


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


def _discover_packages(clone_path: Path, treeish: str, tracked_paths: Iterable[str]) -> Tuple[str, ...]:
    names = set()
    for path in tracked_paths:
        if Path(path).name != "package.json":
            continue
        try:
            data = json.loads(run_git(["show", treeish + ":" + path], clone_path))
        except (GitCommandError, ValueError):
            continue
        name = data.get("name") if isinstance(data, dict) else None
        if isinstance(name, str) and name:
            names.add(name)
    return tuple(sorted(names))


def _has_submodules(clone_path: Path, treeish: str, tracked_paths: Iterable[str]) -> bool:
    if ".gitmodules" in tracked_paths:
        return True
    entries = run_git(["ls-tree", "-r", "-z", treeish], clone_path).split("\0")
    return any(entry.startswith("160000 ") for entry in entries if entry)


def _has_lfs_declarations(clone_path: Path, treeish: str, tracked_paths: Iterable[str]) -> bool:
    for path in tracked_paths:
        if Path(path).name != ".gitattributes":
            continue
        attributes = run_git(["show", treeish + ":" + path], clone_path)
        if _LFS_FILTER.search(attributes):
            return True
    return False


def _tag_ref(repo_id: str, name: str, sha: str, aliases: Tuple[str, ...], commit_time: str) -> ResolvedRef:
    package = parse_package_tag(name)
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
    parsed = parse_semver(name)
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


def _package_selector(value: str) -> Tuple[str, str]:
    package = parse_package_tag(value)
    if package is None:
        raise RefResolutionError("package selector must include a scoped package namespace")
    return package


def _is_full_object_id(value: str) -> bool:
    return len(value) in (40, 64) and all(character in "0123456789abcdefABCDEF" for character in value)


def _one(candidates: Iterable[ResolvedRef], selector: str) -> ResolvedRef:
    matches = tuple(candidates)
    if not matches:
        raise RefResolutionError("missing selector " + selector)
    if len(matches) != 1:
        raise RefResolutionError("ambiguous selector " + selector)
    return matches[0]


def _fetch_refspec(selector: str, tag_names: Optional[Tuple[str, ...]]) -> Tuple[str, str]:
    if selector == "default-branch":
        return "", ""
    if selector.startswith("tag:"):
        name = selector[4:]
        if not name:
            raise RefResolutionError("missing selector " + selector)
        return "refs/tags/" + name, "refs/tags/" + name
    if selector.startswith("commit:"):
        sha = selector[7:]
        if not _is_full_object_id(sha):
            raise RefResolutionError("commit selector must use an exact full SHA")
        return sha, "refs/github-collection/commits/" + sha.lower()
    if tag_names is None:
        return "", ""
    if selector.startswith("package:"):
        package_name, version = _package_selector(selector[8:])
        name = _select_remote_tag_name(tag_names, parse_semver(version), selector, package_name)
    else:
        target = parse_semver(selector)
        if target is None:
            raise RefResolutionError("missing selector " + selector)
        name = _select_remote_tag_name(tag_names, target, selector, None)
    return "refs/tags/" + name, "refs/tags/" + name


def _selector_needs_tag_metadata(selector: str) -> bool:
    return selector.startswith("package:") or parse_semver(selector) is not None


def _remote_tag_names(clone_path: Path) -> Tuple[str, ...]:
    names = set()
    for line in run_git(["ls-remote", "--tags", "origin"], clone_path).splitlines():
        _, separator, ref_name = line.partition("\t")
        if separator and ref_name.startswith("refs/tags/") and not ref_name.endswith("^{}"):
            names.add(ref_name[len("refs/tags/"):])
    return tuple(sorted(names))


def _select_remote_tag_name(
    tag_names: Sequence[str],
    target: Optional[SemanticVersion],
    selector: str,
    package_name: Optional[str],
) -> str:
    if target is None:
        raise RefResolutionError("missing selector " + selector)
    candidates = []
    package_names = set()
    for name in tag_names:
        package = parse_package_tag(name)
        if package_name is not None:
            if package is None or package[0] != package_name:
                continue
            version = parse_semver(package[1])
        elif package is not None:
            version = parse_semver(package[1])
        else:
            version = parse_semver(name)
        if _matches_semver(version, target):
            candidates.append((name, version))
            if package_name is None and package is not None:
                package_names.add(package[0])
    if package_name is None and len(package_names) > 1:
        raise RefResolutionError("ambiguous selector " + selector)
    return _select_semver_name(candidates, target, selector)


def _matches_semver(
    candidate: Optional[SemanticVersion], target: SemanticVersion
) -> bool:
    return candidate is not None and matches_semver(candidate, target)


def _select_semver_ref(
    candidates: Iterable[ResolvedRef], target: Optional[SemanticVersion], selector: str
) -> ResolvedRef:
    if target is None:
        raise RefResolutionError("missing selector " + selector)
    matches = [
        (ref, parse_semver(ref.version))
        for ref in candidates
        if _matches_semver(parse_semver(ref.version), target)
    ]
    if target.is_exact:
        return _one((ref for ref, _ in matches), selector)
    selected = _select_semver_name([(ref.ref_name, version) for ref, version in matches], target, selector)
    return _one((ref for ref, _ in matches if ref.ref_name == selected), selector)


def _select_semver_name(
    candidates: Sequence[Tuple[str, Optional[SemanticVersion]]],
    target: SemanticVersion,
    selector: str,
) -> str:
    matches = [(name, version) for name, version in candidates if _matches_semver(version, target)]
    if not matches:
        raise RefResolutionError("missing selector " + selector)
    if target.is_exact:
        return _one_name(matches, selector)
    best_version = matches[0][1]
    for _, version in matches[1:]:
        if _compare_semver(version, best_version) > 0:
            best_version = version
    return _one_name([(name, version) for name, version in matches if version == best_version], selector)


def _one_name(candidates: Sequence[Tuple[str, Optional[SemanticVersion]]], selector: str) -> str:
    if not candidates:
        raise RefResolutionError("missing selector " + selector)
    if len(candidates) != 1:
        raise RefResolutionError("ambiguous selector " + selector)
    return candidates[0][0]


def _compare_semver(
    left: Optional[SemanticVersion], right: Optional[SemanticVersion]
) -> int:
    if left is None or right is None:
        raise ValueError("semantic version comparison requires parsed versions")
    return compare_semver(left, right)
