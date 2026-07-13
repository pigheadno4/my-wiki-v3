from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Dict, Iterable, List

TERMINAL = {
    "collected-new",
    "collected-changed",
    "unchanged",
    "retry-pending",
    "failed",
}


def write_jsonl(path: Path, events: Iterable[Dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(event, sort_keys=True) + "\n" for event in events),
        encoding="utf-8",
    )


def validate_terminal_counts(events: List[Dict[str, object]]) -> int:
    selected = [event for event in events if event.get("selected")]
    bad = [event for event in selected if event.get("state") not in TERMINAL]
    if bad:
        raise ValueError("selected run contains non-terminal states")
    return len(selected)


def render_status(
    provider: str,
    records: List[Dict[str, object]],
    events: List[Dict[str, object]],
) -> str:
    counts = Counter(str(event.get("state")) for event in events)
    title = provider.replace("-", " ").title()
    lines = ["# " + title + " Collection Status", "", "## Current summary", ""]
    lines += ["| State | Count |", "| --- | ---: |"]
    for state in sorted(counts):
        lines.append("| " + state + " | " + str(counts[state]) + " |")
    lines += ["", "## Discovery reconciliation", ""]
    membership = Counter(
        "both"
        if record.get("in_llms") and record.get("in_sitemap")
        else "llms-only"
        if record.get("in_llms")
        else "sitemap-only"
        for record in records
        if record.get("selected") and record.get("kind") == "page"
    )
    lines += ["| Membership | Count |", "| --- | ---: |"]
    for name in ("both", "llms-only", "sitemap-only"):
        lines.append("| " + name + " | " + str(membership[name]) + " |")
    lines += ["", "## Failed and retry queue", ""]
    for event in events:
        if event.get("state") in {"failed", "retry-pending"}:
            lines.append(
                "- " + str(event.get("url")) + " - " + str(event.get("last_error", ""))
            )
    return "\n".join(lines).rstrip() + "\n"
