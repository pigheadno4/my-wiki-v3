"""Worker-result checks for the minimum Metronome dry-run pilot."""

import hashlib
from pathlib import Path
from typing import Any, Dict


class ValidationError(Exception):
    """Raised when a worker result cannot become a candidate."""


RESULT_KEYS = {
    "job_id",
    "attempt",
    "source_page",
    "quotes",
    "suggestions",
    "raw_path",
    "raw_sha256",
    "status",
}
SUGGESTION_KEYS = {"company", "concepts", "index", "log"}


def _ensure_utf8(value: Any) -> None:
    if isinstance(value, str):
        try:
            value.encode("utf-8")
        except UnicodeEncodeError as error:
            raise ValidationError("worker result contains non-UTF-8 text") from error
    elif isinstance(value, dict):
        for key, item in value.items():
            _ensure_utf8(key)
            _ensure_utf8(item)
    elif isinstance(value, list):
        for item in value:
            _ensure_utf8(item)


def sha256_file(path: Path) -> str:
    """Return the SHA-256 digest of one raw file."""
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def _raw_entry(source_page: str, raw_path: str, canonical_url: str) -> str:
    if not source_page.startswith("---\n"):
        raise ValidationError("source page must start with frontmatter")
    closing = source_page.find("\n---\n", 4)
    if closing == -1:
        raise ValidationError("source page frontmatter is incomplete")
    frontmatter = source_page[4:closing].splitlines()
    expected = raw_path.removeprefix("raw/")
    if f'canonical_url: "{canonical_url}"' not in frontmatter:
        raise ValidationError("source page canonical_url does not match the job")
    try:
        raw_files = frontmatter.index("raw_files:")
    except ValueError as error:
        raise ValidationError("source page is missing raw_files") from error
    raw_entries = []
    for line in frontmatter[raw_files + 1:]:
        if line.startswith("  - "):
            raw_entries.append(line)
        elif line and not line.startswith(" "):
            break
    if f'  - "{expected}"' not in raw_entries:
        raise ValidationError("source page raw_files entry does not match raw path")
    return expected


def validate_worker_result(root: Path, job: dict, result: dict) -> Dict[str, Any]:
    """Validate a candidate against its trusted job and immutable raw source."""
    if not isinstance(result, dict):
        raise ValidationError("worker result must use the fixed schema")
    _ensure_utf8(result)
    if set(result) != RESULT_KEYS:
        raise ValidationError("worker result must use the fixed schema")
    if result["job_id"] != job["job_id"] or result["attempt"] != job["attempt"]:
        raise ValidationError("worker result does not match the job attempt")
    if result["status"] != "candidate_ready":
        raise ValidationError("worker result status must be candidate_ready")
    if result["raw_path"] != job["raw_path"]:
        raise ValidationError("worker result raw path does not match the job")

    raw_file = root / job["raw_path"]
    raw_sha256 = sha256_file(raw_file)
    if result["raw_sha256"] != job["raw_sha256"] or raw_sha256 != job["raw_sha256"]:
        raise ValidationError("worker result raw hash does not match the job")

    suggestions = result["suggestions"]
    if not isinstance(suggestions, dict) or set(suggestions) != SUGGESTION_KEYS:
        raise ValidationError("suggestions must use the fixed schema")
    if not all(isinstance(suggestions[key], list) for key in SUGGESTION_KEYS):
        raise ValidationError("suggestions values must be arrays")

    quotes = result["quotes"]
    if not isinstance(quotes, list) or not 3 <= len(quotes) <= 5:
        raise ValidationError("worker result must contain three to five quotes")
    raw_bytes = raw_file.read_bytes()
    for quote in quotes:
        if not isinstance(quote, dict):
            raise ValidationError("quote must be an object")
        text = quote.get("text")
        location = quote.get("location")
        if not isinstance(text, str) or not text or not isinstance(location, str) or not location:
            raise ValidationError("quote text and location are required")
        if text.encode("utf-8") not in raw_bytes:
            raise ValidationError("quote is absent from the raw file")

    source_page = result["source_page"]
    if not isinstance(source_page, str):
        raise ValidationError("source page must be text")
    canonical_url = job.get("canonical_url")
    if not isinstance(canonical_url, str) or not canonical_url:
        raise ValidationError("job is missing canonical_url")
    raw_entry = _raw_entry(source_page, job["raw_path"], canonical_url)
    lines = source_page.splitlines()
    try:
        heading = lines.index("## Raw Sources")
    except ValueError as error:
        raise ValidationError("source page is missing Raw Sources") from error
    section_end = next(
        (index for index, line in enumerate(lines[heading + 1:], start=heading + 1) if line.startswith("## ")),
        len(lines),
    )
    raw_target = f"raw/{raw_entry.removesuffix('.md')}"
    raw_sources = "\n".join(lines[heading + 1:section_end])
    if f"[[{raw_target}|" not in raw_sources and f"[[{raw_target}]]" not in raw_sources:
        raise ValidationError("source page raw link does not match raw path")

    return result
