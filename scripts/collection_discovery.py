from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass
from typing import Dict, List, Optional
from urllib.parse import urlsplit, urlunsplit

LLMS_LINK_RE = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)")
DOC_HOST = "docs.metronome.com"


@dataclass(frozen=True)
class DiscoveryRecord:
    canonical_url: str
    fetch_url: str
    in_llms: bool
    in_sitemap: bool
    language: str
    selected: bool
    kind: str
    section: str
    exclusion_reason: Optional[str] = None

    def to_dict(self) -> Dict[str, object]:
        return asdict(self)


def canonicalize_url(url: str) -> str:
    parts = urlsplit(url.strip())
    path = parts.path.rstrip("/") or "/"
    if path.endswith(".md"):
        path = path[:-3]
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, "", ""))


def parse_llms(text: str) -> List[str]:
    return sorted(set(LLMS_LINK_RE.findall(text)))


def parse_sitemap(text: str) -> List[str]:
    root = ET.fromstring(text)
    return sorted(
        set(
            element.text.strip()
            for element in root.iter()
            if element.tag.endswith("loc") and element.text
        )
    )


def _section(path: str) -> str:
    segments = [part for part in path.split("/") if part]
    return "/".join(segments[:2]) if segments else "root"


def reconcile_metronome(llms_text: str, sitemap_text: str) -> List[DiscoveryRecord]:
    llms_urls = parse_llms(llms_text)
    sitemap_urls = parse_sitemap(sitemap_text)
    llms_by_canonical = {canonicalize_url(url): url for url in llms_urls}
    sitemap_by_canonical = {canonicalize_url(url): url for url in sitemap_urls}
    records = []
    for canonical in sorted(set(llms_by_canonical) | set(sitemap_by_canonical)):
        parts = urlsplit(canonical)
        in_llms = canonical in llms_by_canonical
        in_sitemap = canonical in sitemap_by_canonical
        language = "fr" if parts.path.startswith("/fr/") else "en"
        kind = "artifact" if parts.path.endswith(".json") else "page"
        reason = None
        if parts.netloc != DOC_HOST:
            reason = "external-host"
        elif language == "fr":
            reason = "localized-fr"
        selected = reason is None
        original = llms_by_canonical.get(canonical) or sitemap_by_canonical[canonical]
        if kind == "artifact":
            fetch_url = original
        elif original.endswith(".md"):
            fetch_url = original
        else:
            fetch_url = original.rstrip("/") + ".md"
        records.append(
            DiscoveryRecord(
                canonical_url=canonical,
                fetch_url=fetch_url,
                in_llms=in_llms,
                in_sitemap=in_sitemap,
                language=language,
                selected=selected,
                kind=kind,
                section=_section(parts.path),
                exclusion_reason=reason,
            )
        )
    return records
