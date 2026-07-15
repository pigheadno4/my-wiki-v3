"""Shared semantic-version and package-tag parsing for GitHub collection."""

from dataclasses import dataclass
import re
from typing import Optional, Tuple


_SEMVER = re.compile(
    r"^v?(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:-([0-9A-Za-z][0-9A-Za-z.-]*))?$"
)
_SCOPED_PACKAGE = re.compile(r"^@[^/@]+/[^@/]+$")


@dataclass(frozen=True)
class SemanticVersion:
    major: int
    minor: Optional[int]
    patch: Optional[int]
    prerelease: Optional[Tuple[str, ...]]
    is_exact: bool


def parse_semver(value: str) -> Optional[SemanticVersion]:
    """Parse the supported exact, major, or minor semantic-version selector."""
    match = _SEMVER.fullmatch(value)
    if match is None:
        return None
    prerelease = match.group(4)
    minor = int(match.group(2)) if match.group(2) is not None else None
    patch = int(match.group(3)) if match.group(3) is not None else None
    return SemanticVersion(
        major=int(match.group(1)),
        minor=minor,
        patch=patch,
        prerelease=tuple(prerelease.split(".")) if prerelease is not None else None,
        is_exact=minor is not None and patch is not None,
    )


def compare_semver(left: SemanticVersion, right: SemanticVersion) -> int:
    """Compare semantic versions using SemVer precedence rules."""
    left_numbers = (left.major, left.minor or 0, left.patch or 0)
    right_numbers = (right.major, right.minor or 0, right.patch or 0)
    if left_numbers < right_numbers:
        return -1
    if left_numbers > right_numbers:
        return 1
    if left.prerelease is None and right.prerelease is None:
        return 0
    if left.prerelease is None:
        return 1
    if right.prerelease is None:
        return -1
    for left_identifier, right_identifier in zip(left.prerelease, right.prerelease):
        if left_identifier == right_identifier:
            continue
        left_numeric = left_identifier.isdigit()
        right_numeric = right_identifier.isdigit()
        if left_numeric and right_numeric:
            return -1 if int(left_identifier) < int(right_identifier) else 1
        if left_numeric:
            return -1
        if right_numeric:
            return 1
        return -1 if left_identifier < right_identifier else 1
    if len(left.prerelease) < len(right.prerelease):
        return -1
    if len(left.prerelease) > len(right.prerelease):
        return 1
    return 0


def matches_semver(
    candidate: SemanticVersion, target: SemanticVersion, include_prerelease: bool = False
) -> bool:
    """Return whether a candidate matches a selector's version line."""
    if candidate.major != target.major:
        return False
    if target.minor is not None and (candidate.minor or 0) != target.minor:
        return False
    if target.patch is not None and (candidate.patch or 0) != target.patch:
        return False
    if target.prerelease is not None:
        return candidate.prerelease == target.prerelease
    if target.is_exact:
        return candidate.prerelease is None
    return include_prerelease or candidate.prerelease is None


def parse_package_tag(tag: str) -> Optional[Tuple[str, str]]:
    """Return a scoped package name and semantic version from a package tag."""
    if not tag.startswith("@"):
        return None
    package_name, separator, version = tag.rpartition("@")
    if not separator or not _SCOPED_PACKAGE.fullmatch(package_name) or parse_semver(version) is None:
        return None
    return package_name, version
