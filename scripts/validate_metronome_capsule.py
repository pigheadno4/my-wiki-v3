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
        f"{len(report.sources)} sources, "
        f"{len(report.orphan_raw_files)} pending ingest"
    )
    if errors:
        print("\nStructural errors:")
        for error in errors:
            print(f"- {error}")
        return 1
    if report.orphan_raw_files:
        print("\nPending ingest:")
        for path in report.orphan_raw_files:
            print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
