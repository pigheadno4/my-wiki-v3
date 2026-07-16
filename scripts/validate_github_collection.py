#!/usr/bin/env python3
"""Validate GitHub snapshots, packets, sources, and generated status."""

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
        print(
            "pending packets: "
            + str(len(report.pending_packets))
            + " (informational)"
        )
        return 1
    print(
        "validate_github_collection: OK ("
        + str(len(report.snapshot_paths))
        + " snapshots, "
        + str(len(report.pending_packets))
        + " pending packets, no structural errors)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
