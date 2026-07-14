#!/usr/bin/env python3
"""Validate a Metronome ingest pilot job and optional completed receipt."""
import argparse
from pathlib import Path

from metronome_ingest_pilot import load_json, validate_job, validate_receipt


ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--job", required=True)
    parser.add_argument("--receipt")
    args = parser.parse_args()

    job_path = ROOT / args.job
    job = load_json(job_path)
    errors = validate_job(ROOT, job)
    if errors:
        for error in errors:
            print(error)
        return 1
    print("job: valid")

    if args.receipt:
        receipt = load_json(ROOT / args.receipt)
        errors = validate_receipt(ROOT, job, receipt)
        if errors:
            for error in errors:
                print(error)
            return 1
        print("receipt: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
