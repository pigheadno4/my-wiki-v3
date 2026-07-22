"""Exact, bounded reads from one immutable Git commit tree."""

from dataclasses import dataclass
import json
import os
from pathlib import Path
import subprocess
from typing import Any, Dict, Optional, Sequence, Tuple

from github_canonical import safe_policy_path


DEFAULT_MAX_BLOB_BYTES = 512000
_OBJECT_ID_LENGTHS = (40, 64)
_HEX = frozenset("0123456789abcdef")


class GitObjectReadError(ValueError):
    """A bounded infrastructure failure while reading immutable Git objects."""


class GitCommandRejectedError(GitObjectReadError):
    """A deterministic rejection from a Git command that launched successfully."""


@dataclass(frozen=True)
class GitBlob:
    path: str
    oid: str
    mode: str
    size: Optional[int]


class GitTree:
    """Enumerate and read blobs belonging to one exact commit object."""

    def __init__(self, repo_root: Path, sha: str, max_blob_bytes: int = DEFAULT_MAX_BLOB_BYTES):
        if not _is_object_id(sha):
            raise ValueError("sha must be a full lowercase hexadecimal object ID")
        if not isinstance(max_blob_bytes, int) or isinstance(max_blob_bytes, bool) or max_blob_bytes <= 0:
            raise ValueError("max_blob_bytes must be a positive integer")
        self._repo_root = Path(repo_root)
        self._sha = sha
        self._max_blob_bytes = max_blob_bytes
        self._blobs: Optional[Tuple[GitBlob, ...]] = None
        self._sizes: Dict[str, int] = {}
        self._is_exact_commit: Optional[bool] = None

    @property
    def sha(self) -> str:
        """Return the exact commit object ID owned by this reader."""
        return self._sha

    def blobs(self) -> Tuple[GitBlob, ...]:
        """Return every recursive entry in the exact commit tree, sorted by path."""
        if self._blobs is None:
            self._require_exact_commit()
            output = _run_git_bytes(
                ["ls-tree", "-r", "-z", self._sha], self._repo_root
            )
            entries = tuple(_parse_ls_tree_entry(item) for item in output.split(b"\0") if item)
            paths = tuple(entry.path for entry in entries)
            if len(paths) != len(set(paths)):
                raise ValueError("Git tree contains duplicate paths")
            self._blobs = tuple(sorted(entries, key=lambda entry: entry.path))
        return self._blobs

    def blob_size(self, path: str) -> int:
        """Resolve the size of one selected blob without sizing the entire tree."""
        blob = self._blob(path)
        if blob.mode == "160000":
            raise ValueError("path is not tracked as a blob: " + path)
        if path not in self._sizes:
            raw_size = _run_git_bytes(
                ["cat-file", "-s", self._sha + ":" + path], self._repo_root
            ).strip()
            try:
                size = int(raw_size)
            except ValueError as error:
                raise GitObjectReadError("Git blob size is invalid") from error
            if size < 0:
                raise GitObjectReadError("Git blob size is invalid")
            self._sizes[path] = size
        return self._sizes[path]

    def read_blob(self, path: str, max_bytes: Optional[int] = None) -> bytes:
        """Read one bounded tracked blob by its safe repository-relative path."""
        limit = self._max_blob_bytes if max_bytes is None else _read_limit(max_bytes)
        self._blob(path)
        size = self.blob_size(path)
        if size > limit:
            raise ValueError("Git blob exceeds byte limit: " + path)

        content = _run_git_bytes(
            ["cat-file", "blob", self._sha + ":" + path], self._repo_root
        )
        if len(content) != size:
            raise GitObjectReadError("Git blob read size did not match tree metadata")
        return content

    def read_json(self, path: str, max_bytes: Optional[int] = None) -> Any:
        """Read a JSON blob without accepting duplicate object keys."""
        try:
            text = self.read_blob(path, max_bytes=max_bytes).decode("utf-8")
        except UnicodeDecodeError as error:
            raise ValueError("JSON blob is not valid UTF-8") from error
        return json.loads(
            text,
            object_pairs_hook=_no_duplicate_keys,
            parse_constant=_reject_json_constant,
        )

    def _require_exact_commit(self) -> None:
        if self._is_exact_commit is None:
            try:
                resolved = _run_git_bytes(
                    ["rev-parse", "--verify", self._sha + "^{commit}"], self._repo_root
                ).strip().decode("ascii")
            except GitCommandRejectedError:
                raise ValueError("sha must name an exact commit") from None
            self._is_exact_commit = resolved == self._sha
        if not self._is_exact_commit:
            raise ValueError("sha must name an exact commit")

    def _blob(self, path: str) -> GitBlob:
        if not safe_policy_path(path):
            raise ValueError("path must be a safe repository-relative POSIX path")
        blob = next((entry for entry in self.blobs() if entry.path == path), None)
        if blob is None:
            raise ValueError("path is not tracked by the exact Git tree: " + path)
        return blob


def _parse_ls_tree_entry(value: bytes) -> GitBlob:
    metadata, separator, raw_path = value.partition(b"\t")
    if not separator or not raw_path:
        raise ValueError("malformed git ls-tree entry")
    fields = metadata.split()
    if len(fields) != 3:
        raise ValueError("malformed git ls-tree metadata")
    raw_mode, object_type, raw_oid = fields
    try:
        mode = raw_mode.decode("ascii")
        oid = raw_oid.decode("ascii")
        path = raw_path.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ValueError("git ls-tree entry is not valid UTF-8") from error
    if len(mode) != 6 or not mode.isdigit() or not _is_object_id(oid):
        raise ValueError("malformed git ls-tree metadata")
    if object_type == b"blob":
        return GitBlob(path=path, oid=oid, mode=mode, size=None)
    if object_type == b"commit" and mode == "160000":
        return GitBlob(path=path, oid=oid, mode=mode, size=None)
    raise ValueError("unsupported Git tree entry: " + path)


def _run_git_bytes(args: Sequence[str], cwd: Path) -> bytes:
    command = ["git"] + list(args)
    try:
        result = subprocess.run(
            command,
            cwd=str(cwd),
            check=True,
            capture_output=True,
            env=_git_environment(),
        )
    except subprocess.CalledProcessError:
        raise GitCommandRejectedError("Git object command was rejected") from None
    except (subprocess.SubprocessError, OSError):
        raise GitObjectReadError("Git object command failed") from None
    return result.stdout


def _git_environment() -> dict:
    environment = os.environ.copy()
    environment["GIT_NO_REPLACE_OBJECTS"] = "1"
    return environment


def _is_object_id(value: object) -> bool:
    return (
        isinstance(value, str)
        and len(value) in _OBJECT_ID_LENGTHS
        and all(character in _HEX for character in value)
    )


def _read_limit(value: object) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
        raise ValueError("max_bytes must be a positive integer")
    return value


def _no_duplicate_keys(pairs: Sequence[Tuple[str, Any]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key: " + key)
        result[key] = value
    return result


def _reject_json_constant(value: str) -> None:
    raise ValueError("invalid JSON constant: " + value)


__all__ = [
    "DEFAULT_MAX_BLOB_BYTES",
    "GitBlob",
    "GitCommandRejectedError",
    "GitObjectReadError",
    "GitTree",
]
