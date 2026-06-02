#!/usr/bin/env python3
"""
validate_wiki.py — deterministic, model-independent guardrail for the wiki.

Checks (no LLM judgment involved):
  1. Frontmatter present and has the required fields for its `type`.
  2. Every raw_files: entry points to a file that exists in raw/.
  3. Every [[wikilink]] resolves to a real page (wiki/ or raw/ basename, Obsidian-style).
  4. No leftover placeholder text ([TODO], TBD, FIXME, <placeholder>, FILL IN).
  5. Filenames are lowercase-hyphenated slugs.

Run on the whole wiki, or on specific files (e.g. right after an ingest):
  python scripts/validate_wiki.py
  python scripts/validate_wiki.py wiki/sources/source-stripe-payment-intents.md

Exit code is non-zero if any error is found. See rules/lint.md and rules/ingest.md.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"

REQUIRED = {
    "source": ["title", "type", "date_ingested", "original_format", "raw_files", "tags"],
    "company": ["title", "type", "tags", "source_count"],
    "concept": ["title", "type", "category", "tags"],
    "comparison": ["title", "type", "dimension", "date_created", "tags"],
    "analysis": ["title", "type", "date_created", "tags"],
}
PLACEHOLDER_RE = re.compile(r"\[TODO\]|\bTBD\b|\bFIXME\b|<placeholder>|FILL IN", re.IGNORECASE)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FM_LIST_ITEM = re.compile(r'^\s*-\s*"?([^"]+?)"?\s*$')


def split_frontmatter(text: str):
    if not text.startswith("---"):
        return None, text
    lines = text.splitlines()
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return None, text
    return "\n".join(lines[1:end]), "\n".join(lines[end + 1:])


def parse_frontmatter(fm: str) -> dict:
    """Minimal flat-YAML parser: scalars, `[a, b]` inline lists, and block lists."""
    data: dict = {}
    key = None
    for line in fm.splitlines():
        if not line.strip():
            continue
        m = FM_LIST_ITEM.match(line)
        if m and key is not None:
            data.setdefault(key, [])
            if isinstance(data[key], list):
                data[key].append(m.group(1).strip())
            continue
        if ":" in line and not line.startswith(" "):
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            if val.startswith("[") and val.endswith("]"):
                data[key] = [v.strip().strip('"') for v in val[1:-1].split(",") if v.strip()]
            elif val:
                data[key] = val.strip().strip('"')
                key = None  # scalar, not a block-list header
            else:
                data[key] = []  # may be filled by following block-list items
    return data


def build_link_index() -> set[str]:
    names: set[str] = set()
    for p in WIKI.rglob("*.md"):
        names.add(p.stem)
    for p in RAW.glob("*.md"):
        names.add(p.stem)
    for p in RAW.glob("*/"):  # repo detail dirs are valid link targets too
        names.add(p.name.rstrip("/"))
    return names


def check_file(path: Path, link_index: set[str], errors: list[str]) -> None:
    rel = path.relative_to(ROOT)
    if not SLUG_RE.match(path.stem):
        errors.append(f"{rel}: filename '{path.stem}' is not a lowercase-hyphenated slug")
    text = path.read_text(encoding="utf-8")

    fm_raw, body = split_frontmatter(text)
    if fm_raw is None:
        errors.append(f"{rel}: missing YAML frontmatter")
        return
    fm = parse_frontmatter(fm_raw)
    ptype = fm.get("type")
    if ptype not in REQUIRED:
        errors.append(f"{rel}: unknown or missing type: {ptype!r}")
    else:
        for field in REQUIRED[ptype]:
            if field not in fm or fm[field] in ("", [], None):
                errors.append(f"{rel}: missing required frontmatter field '{field}'")

    # raw_files existence
    for rf in fm.get("raw_files", []) if isinstance(fm.get("raw_files"), list) else []:
        if not (RAW / rf).exists():
            errors.append(f"{rel}: raw_files entry '{rf}' does not exist in raw/")

    # placeholders
    for i, line in enumerate(text.splitlines(), 1):
        if PLACEHOLDER_RE.search(line):
            errors.append(f"{rel}:{i}: leftover placeholder text")

    # wikilinks resolve (strip escaped-bracket / whitespace artifacts)
    for target in WIKILINK_RE.findall(body):
        t = target.strip().rstrip("\\").strip()
        if t and t not in link_index:
            errors.append(f"{rel}: unresolved wikilink [[{t}]]")


def main() -> int:
    args = sys.argv[1:]
    if args:
        files = [Path(a) if Path(a).is_absolute() else ROOT / a for a in args]
    else:
        files = sorted(WIKI.rglob("*.md"))
        files = [f for f in files if f.name not in ("index.md", "log.md", "overview.md")
                 and not f.name.endswith("-index.md")]

    link_index = build_link_index()
    errors: list[str] = []
    for f in files:
        if f.exists():
            check_file(f, link_index, errors)
        else:
            errors.append(f"{f}: file not found")

    if errors:
        print(f"validate_wiki: {len(errors)} issue(s) found:\n")
        for e in errors:
            print("  - " + e)
        return 1
    print(f"validate_wiki: OK ({len(files)} file(s) checked, no issues)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
