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


def create_git_repo(root: Path) -> Path:
    repo = root / "upstream"
    repo.mkdir()
    _git(["init", "-b", "main", str(repo)])
    _git(["config", "user.name", "Wiki Test"], cwd=repo)
    _git(["config", "user.email", "wiki@example.test"], cwd=repo)
    return repo


def commit_file(repo: Path, relative: str, content: str, message: str) -> str:
    path = repo / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    _git(["add", relative], cwd=repo)
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
