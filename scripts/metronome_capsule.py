#!/usr/bin/env python3
"""Deterministic inspection and validation for the Metronome wiki capsule."""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Tuple

from validate_wiki import WIKILINK_RE, parse_frontmatter, split_frontmatter


METRONOME_SOURCE = "https://docs.metronome.com/"
RAW_SOURCES_HEADING = re.compile(r"^## Raw Sources\s*$", re.MULTILINE)
NEXT_HEADING = re.compile(r"^##\s+", re.MULTILINE)


@dataclass(frozen=True)
class SourceRecord:
    path: str
    stem: str
    canonical_url: str
    raw_files: Tuple[str, ...]
    raw_source_files: Tuple[str, ...]


@dataclass(frozen=True)
class CapsuleReport:
    raw_files: Tuple[str, ...]
    sources: Tuple[SourceRecord, ...]
    index_source_stems: Tuple[str, ...]
    company_source_count: Optional[int]
    orphan_raw_files: Tuple[str, ...]
    inspection_errors: Tuple[str, ...]


def _raw_source_files(body: str) -> Tuple[str, ...]:
    heading = RAW_SOURCES_HEADING.search(body)
    if heading is None:
        return ()
    section_start = heading.end()
    next_heading = NEXT_HEADING.search(body, section_start)
    section = body[section_start:next_heading.start() if next_heading else len(body)]
    paths = []
    for target in WIKILINK_RE.findall(section):
        target = target.strip().rstrip("\\").strip()
        if target.startswith("raw/"):
            target = target[len("raw/"):]
        paths.append(target + ("" if target.endswith(".md") else ".md"))
    return tuple(paths)


def _source_record(root: Path, path: Path, errors: List[str]) -> SourceRecord:
    rel = path.relative_to(root).as_posix()
    text = path.read_text(encoding="utf-8")
    fm_raw, body = split_frontmatter(text)
    if fm_raw is None:
        errors.append(f"{rel}: missing YAML frontmatter")
        fm = {}
    else:
        fm = parse_frontmatter(fm_raw)
    canonical_url = str(fm.get("canonical_url", ""))
    raw_value = fm.get("raw_files", [])
    raw_files = tuple(raw_value) if isinstance(raw_value, list) else ()
    return SourceRecord(
        path=rel,
        stem=path.stem,
        canonical_url=canonical_url,
        raw_files=raw_files,
        raw_source_files=_raw_source_files(body),
    )


def _index_source_stems(path: Path, errors: List[str], root: Path) -> Tuple[str, ...]:
    if not path.exists():
        errors.append(f"{path.relative_to(root).as_posix()}: file not found")
        return ()
    stems = []
    for target in WIKILINK_RE.findall(path.read_text(encoding="utf-8")):
        stem = Path(target.strip()).name
        if stem.startswith("source-"):
            stems.append(stem)
    return tuple(sorted(stems))


def _company_source_count(path: Path, errors: List[str], root: Path) -> Optional[int]:
    if not path.exists():
        errors.append(f"{path.relative_to(root).as_posix()}: file not found")
        return None
    fm_raw, _ = split_frontmatter(path.read_text(encoding="utf-8"))
    if fm_raw is None:
        errors.append(f"{path.relative_to(root).as_posix()}: missing YAML frontmatter")
        return None
    value = parse_frontmatter(fm_raw).get("source_count")
    try:
        return int(value)
    except (TypeError, ValueError):
        errors.append(
            f"{path.relative_to(root).as_posix()}: source_count must be an integer"
        )
        return None


def inspect_capsule(root: Path) -> CapsuleReport:
    """Derive Metronome capsule state from raw and wiki files."""
    raw_root = root / "raw" / "metronome"
    source_root = root / "wiki" / "sources" / "metronome"
    errors: List[str] = []

    raw_files = []
    if raw_root.exists():
        for path in sorted(raw_root.rglob("*.md")):
            relative = path.relative_to(raw_root)
            if relative.parts and relative.parts[0] in {"_artifacts", "_discovery"}:
                continue
            raw_files.append("metronome/" + relative.as_posix())

    sources = tuple(
        _source_record(root, path, errors)
        for path in sorted(source_root.glob("*.md"))
    ) if source_root.exists() else ()
    referenced = {raw_file for source in sources for raw_file in source.raw_files}
    orphans = tuple(sorted(set(raw_files) - referenced))

    index_sources = _index_source_stems(
        root / "wiki" / "metronome-index.md", errors, root
    )
    company_count = _company_source_count(
        root / "wiki" / "companies" / "metronome.md", errors, root
    )
    return CapsuleReport(
        raw_files=tuple(raw_files),
        sources=sources,
        index_source_stems=index_sources,
        company_source_count=company_count,
        orphan_raw_files=orphans,
        inspection_errors=tuple(errors),
    )


def validate_capsule(report: CapsuleReport) -> List[str]:
    """Return structural capsule errors; pending ingest orphans are informational."""
    errors = list(report.inspection_errors)
    by_url = {}
    source_stems = {source.stem for source in report.sources}
    raw_files = set(report.raw_files)

    for source in report.sources:
        if not source.canonical_url.startswith(METRONOME_SOURCE):
            errors.append(f"{source.path}: missing or invalid Metronome canonical_url")
        elif source.canonical_url in by_url:
            errors.append(
                f"{source.path}: duplicate canonical_url also owned by "
                f"{by_url[source.canonical_url]}"
            )
        else:
            by_url[source.canonical_url] = source.path

        outside = [path for path in source.raw_files if not path.startswith("metronome/")]
        if outside:
            errors.append(f"{source.path}: raw_files entries must stay inside metronome/")
        missing = [path for path in source.raw_files if path not in raw_files]
        if missing:
            errors.append(f"{source.path}: raw_files entries do not exist: {missing}")
        if source.raw_files != source.raw_source_files:
            errors.append(f"{source.path}: raw_files and Raw Sources differ or are out of order")

    indexed = set(report.index_source_stems)
    for stem in sorted(source_stems - indexed):
        errors.append(f"{stem}: missing from metronome-index")
    for stem in sorted(indexed - source_stems):
        errors.append(f"{stem}: indexed source does not exist")

    if (
        report.company_source_count is not None
        and report.company_source_count != len(report.sources)
    ):
        errors.append(
            "wiki/companies/metronome.md: source_count is "
            f"{report.company_source_count} but found {len(report.sources)} source pages"
        )
    return errors
