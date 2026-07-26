#!/usr/bin/env python3
"""Validate focused GitHub evidence, work items, pages, and generated status."""

from pathlib import Path
import sys
from typing import Optional, Sequence

from github_validation import inspect_github, validate_github


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def main(argv: Optional[Sequence[str]] = None) -> int:
    arguments = tuple(sys.argv[1:] if argv is None else argv)
    if arguments:
        print(
            "usage: python3 scripts/validate_github_collection.py",
            file=sys.stderr,
        )
        return 2
    report = inspect_github(PROJECT_ROOT)
    errors = validate_github(report)
    if errors:
        print(
            "validate_github_collection: "
            + str(len(errors))
            + " structural error(s)"
        )
        for error in errors:
            print("  - " + error)
        pending = sum(
            item.state != "ingested" for item in report.work_items.items
        )
        print("pending work items: " + str(pending) + " (informational)")
        return 1
    print(
        "validate_github_collection: OK ("
        + str(len(report.snapshots))
        + " snapshots, "
        + str(len(report.release_records))
        + " release records, "
        + str(len(report.comparisons))
        + " comparisons, "
        + str(len(report.work_items.items))
        + " work items, no structural errors)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
