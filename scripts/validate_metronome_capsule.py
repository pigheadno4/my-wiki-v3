#!/usr/bin/env python3
"""Validate and report the Metronome provider capsule."""
from pathlib import Path

from metronome_capsule import inspect_capsule, validate_capsule


ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    report = inspect_capsule(ROOT)
    errors = validate_capsule(report)
    print(
        f"Metronome capsule: {len(report.raw_files)} raw, "
        f"{len(report.source_page_stems)} sources, "
        f"{len(report.orphan_raw_files)} raw pages without source summaries"
    )
    if errors:
        print("\nStructural errors:")
        for error in errors:
            print(f"- {error}")
        return 1
    if report.orphan_raw_files:
        print("\nRaw pages without source summaries:")
        for path in report.orphan_raw_files:
            print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
