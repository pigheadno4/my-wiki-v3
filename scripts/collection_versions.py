from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Optional, Tuple

HEADER_RE = re.compile(
    r"^\s*<!--\s*(Source URL|Fetched|Discovery):.*-->\s*$",
    re.MULTILINE,
)
DATED_RE = re.compile(r"-(\d{4}-\d{2}-\d{2})(?:-r(\d+))?\.md$")


def source_body(content: str) -> str:
    return HEADER_RE.sub("", content).strip()


def body_sha256(content: str) -> str:
    return hashlib.sha256(source_body(content).encode("utf-8")).hexdigest()


def classify_candidate(previous: Optional[str], candidate: str) -> str:
    if previous is None:
        return "new"
    return "unchanged" if body_sha256(previous) == body_sha256(candidate) else "changed"


def _version_key(path: Path) -> Tuple[str, int]:
    match = DATED_RE.search(path.name)
    if match is None:
        raise ValueError("not a dated raw Markdown path: " + str(path))
    return match.group(1), int(match.group(2) or "1")


def latest_prior(raw_root: Path, relative_path: Path) -> Optional[Path]:
    parent = raw_root / relative_path.parent
    stem = relative_path.stem
    candidates = [path for path in parent.glob(stem + "-*.md") if DATED_RE.search(path.name)]
    return sorted(candidates, key=_version_key)[-1] if candidates else None


def next_target(raw_root: Path, relative_path: Path, collection_date: str) -> Path:
    parent = raw_root / relative_path.parent
    base = parent / (relative_path.stem + "-" + collection_date + ".md")
    if not base.exists():
        return base
    revision = 2
    while True:
        candidate = parent / (
            relative_path.stem + "-" + collection_date + "-r" + str(revision) + ".md"
        )
        if not candidate.exists():
            return candidate
        revision += 1
