"""Local Git repository fixtures for GitHub collection tests."""

from pathlib import Path
import subprocess


def _git(args, cwd=None):
    return subprocess.run(
        ["git"] + list(args),
        cwd=str(cwd) if cwd is not None else None,
        check=True,
        text=True,
        capture_output=True,
    )


def create_git_repo(root: Path, object_format=None) -> Path:
    repo = root / "upstream"
    repo.mkdir()
    init_args = ["init", "-b", "main"]
    if object_format is not None:
        init_args.append("--object-format=" + object_format)
    _git(init_args + [str(repo)])
    _git(["config", "user.name", "Wiki Test"], cwd=repo)
    _git(["config", "user.email", "wiki@example.test"], cwd=repo)
    return repo


def commit_file(repo: Path, relative: str, content: str, message: str) -> str:
    return commit_bytes(repo, relative, content.encode("utf-8"), message)


def commit_bytes(repo: Path, relative: str, content: bytes, message: str, executable: bool = False) -> str:
    path = repo / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    if executable:
        path.chmod(0o755)
    _git(["add", "--", relative], cwd=repo)
    _git(["commit", "-m", message], cwd=repo)
    return _git(["rev-parse", "HEAD"], cwd=repo).stdout.strip()


def commit_symlink(repo: Path, relative: str, target: str, message: str) -> str:
    path = repo / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.symlink_to(target)
    _git(["add", "--", relative], cwd=repo)
    _git(["commit", "-m", message], cwd=repo)
    return _git(["rev-parse", "HEAD"], cwd=repo).stdout.strip()


def tag(repo: Path, name: str) -> None:
    _git(["tag", name], cwd=repo)


def annotated_tag(repo: Path, name: str) -> None:
    _git(["tag", "-a", name, "-m", "annotated " + name], cwd=repo)


def add_submodule_marker(repo: Path, relative: str) -> None:
    marker = repo / ".gitmodules"
    marker.write_text(
        "[submodule \"" + relative + "\"]\n"
        "\tpath = " + relative + "\n"
        "\turl = ../dependency.git\n",
        encoding="utf-8",
    )
    _git(
        [
            "update-index",
            "--add",
            "--cacheinfo",
            "160000," + _git(["rev-parse", "HEAD"], cwd=repo).stdout.strip() + "," + relative,
        ],
        cwd=repo,
    )
    _git(["add", ".gitmodules"], cwd=repo)
    _git(["commit", "-m", "add submodule marker"], cwd=repo)
