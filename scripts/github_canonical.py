"""Canonical values and validation helpers for GitHub source capsules."""

import hashlib
import json
import re
from typing import Any


_NPM_COMPONENT = r"[a-z0-9._~-]+"
_NPM_UNSCOPED = re.compile(r"[a-z0-9][a-z0-9._~-]*\Z")
_NPM_SCOPED = re.compile(r"@[a-z0-9][a-z0-9._~-]*/" + _NPM_COMPONENT + r"\Z")
_LABEL_UNSAFE = re.compile(r"[^a-z0-9._-]+")


def canonical_json_bytes(value: Any) -> bytes:
    """Serialize JSON with the source-capsule canonicalization rules."""
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def canonical_sha256(value: Any) -> str:
    """Return the SHA-256 digest of canonical JSON bytes."""
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def validate_npm_package_name(name: str) -> bool:
    """Return whether *name* matches the npm-package-name-v1 grammar."""
    if not isinstance(name, str) or not name.isascii() or len(name) > 214:
        return False
    if name.startswith("@"):
        return _NPM_SCOPED.fullmatch(name) is not None
    return _NPM_UNSCOPED.fullmatch(name) is not None


def safe_policy_path(path: str) -> bool:
    """Return whether *path* is a non-empty, relative POSIX policy path."""
    if not isinstance(path, str) or not path or path.startswith("/"):
        return False
    if "\\" in path or "\x00" in path:
        return False
    parts = path.split("/")
    return all(part not in ("", ".", "..") for part in parts)


def readable_label(value: str, max_bytes: int = 40) -> str:
    """Normalize an identity label to a bounded ASCII filesystem component."""
    if not isinstance(value, str):
        raise TypeError("label must be a string")
    if max_bytes <= 0:
        raise ValueError("max_bytes must be positive")

    ascii_lower = "".join(
        chr(ord(character) + (ord("a") - ord("A")))
        if "A" <= character <= "Z"
        else character
        for character in value
    )
    label = _LABEL_UNSAFE.sub("-", ascii_lower).strip("-")
    label = label or "capsule"
    label = label.encode("ascii")[:max_bytes].decode("ascii")
    return label or "capsule"[:max_bytes]


__all__ = [
    "canonical_json_bytes",
    "canonical_sha256",
    "readable_label",
    "safe_policy_path",
    "validate_npm_package_name",
]
