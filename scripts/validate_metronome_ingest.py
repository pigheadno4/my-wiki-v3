#!/usr/bin/env python3
"""Validate a Metronome ingest pilot job and optional completed receipt."""
import argparse
from pathlib import Path

from metronome_ingest_pilot import (
    load_json,
    validate_final_receipt,
    validate_job,
    validate_luna_output,
    validate_receipt,
    validate_worker_receipt,
)


ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--job", required=True)
    parser.add_argument("--receipt")
    parser.add_argument("--luna-output")
    parser.add_argument("--worker-receipt")
    parser.add_argument("--final-receipt")
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

    for path, validator, label in (
        (args.luna_output, validate_luna_output, "luna output"),
        (args.worker_receipt, validate_worker_receipt, "worker receipt"),
        (args.final_receipt, validate_final_receipt, "final receipt"),
    ):
        if not path:
            continue
        artifact = load_json(ROOT / path)
        errors = validator(ROOT, job, artifact)
        if errors:
            for error in errors:
                print(error)
            return 1
        print(f"{label}: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
