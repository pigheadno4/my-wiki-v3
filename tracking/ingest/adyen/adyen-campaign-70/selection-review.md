# Adyen C70 selection review

**COMPLETE — no new page targets.**

- Approved discovery URL fetched successfully: HTTP 200, one attempt; exact body, safe headers, timestamps and SHA-256 retained.
- Pinned catalog: 670 URLs. Refreshed catalog: **669 URLs = 642 already ingested + 27 excluded title-only stubs**.
- **0 added URLs; 1 removed listing**: `POST /cardreaderapdu` under `terminal-api/latest`. Existing raw and source are retained; disappearance from discovery does not establish deprecation or endpoint unavailability.
- Historical coverage remains **670 local raw URLs = 643 ingested API Explorer sources + 27 excluded stubs**. There are zero new eligible page targets and zero substantive pages pending in the refreshed catalog. Existing endpoint content was not re-fetched, so no content-freshness claim is made.
- No endpoint Markdown pages fetched, no stub retries, no ingestion runtime or provider operations. All baseline raw hashes verified unchanged; exact count in discovery-reconciliation.json.
- No further page-collection or ingestion approval packet is needed for this catalog: page-collection-proposal.json records an empty target set. No commit/push performed.

Evidence: [reconciliation](discovery-reconciliation.json), [empty page proposal](page-collection-proposal.json), [capture](../../../collections/adyen/c70-discovery-2026-11-07/capture-summary.json).
