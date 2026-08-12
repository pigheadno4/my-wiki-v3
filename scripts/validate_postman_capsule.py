"""Validate Postman JSON and version sentinels in a collected snapshot."""

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Sequence


POSTMAN_V21_SCHEMA = (
    "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
)


@dataclass(frozen=True)
class ValidationResult:
    postman_file_count: int
    sentinel_reference_count: int


class PostmanCapsuleValidationError(ValueError):
    pass


def validate_postman_capsule(
    snapshot_dir: Path,
    postman_paths: Sequence[str],
    sentinel_path: str,
    sentinel_references: Sequence[str],
) -> ValidationResult:
    files_root = snapshot_dir / "files"
    for relative_path in postman_paths:
        path = files_root / relative_path
        if not path.is_file():
            raise PostmanCapsuleValidationError(
                "missing-postman-file: " + relative_path
            )
        try:
            payload = json.loads(path.read_text(encoding="utf-8", errors="strict"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise PostmanCapsuleValidationError(
                "invalid-postman-json: " + relative_path
            ) from error
        if not isinstance(payload, dict) or not isinstance(payload.get("info"), dict):
            raise PostmanCapsuleValidationError(
                "wrong-postman-schema: " + relative_path
            )
        if payload["info"].get("schema") != POSTMAN_V21_SCHEMA:
            raise PostmanCapsuleValidationError(
                "wrong-postman-schema: " + relative_path
            )

    sentinel = files_root / sentinel_path
    if not sentinel.is_file():
        raise PostmanCapsuleValidationError(
            "missing-sentinel-file: " + sentinel_path
        )
    try:
        sentinel_text = sentinel.read_text(encoding="utf-8", errors="strict")
    except UnicodeDecodeError as error:
        raise PostmanCapsuleValidationError(
            "invalid-sentinel-utf8: " + sentinel_path
        ) from error
    for reference in sentinel_references:
        if reference not in sentinel_text:
            raise PostmanCapsuleValidationError(
                "missing-sentinel-reference: " + reference
            )
    return ValidationResult(len(postman_paths), len(sentinel_references))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("snapshot_dir", type=Path)
    parser.add_argument("--postman-path", action="append", required=True)
    parser.add_argument("--sentinel-path", required=True)
    parser.add_argument("--sentinel-reference", action="append", required=True)
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        result = validate_postman_capsule(
            args.snapshot_dir,
            tuple(args.postman_path),
            args.sentinel_path,
            tuple(args.sentinel_reference),
        )
    except (PostmanCapsuleValidationError, UnicodeDecodeError) as error:
        print(str(error), file=sys.stderr)
        return 1
    print(
        json.dumps(
            {
                "postman_file_count": result.postman_file_count,
                "sentinel_reference_count": result.sentinel_reference_count,
                "status": "ok",
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
