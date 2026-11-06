# Adyen C70: API Explorer discovery refresh proposal

**PREPARED ONLY — awaiting discovery-refresh approval.**

C69 completed the captured catalog: **670 URLs = 643 ingested API Explorer sources + 27 excluded title-only stubs**. There are zero uncollected URLs or substantive raw pages pending. Total Adyen sources: 3206 (2547 General Docs + 643 API Explorer + 16 GitHub). These are captured-catalog counts, not an upstream completeness claim.

The next useful step is one documentation discovery URL: `GET https://docs.adyen.com/api-explorer/llms.txt` (maximum three attempts). Capture immutable response evidence and reconcile it with the pinned catalog. Preserve official casing and required duplicated-segment fixup. Keep all 27 stubs excluded.

After discovery approval, prepare an exact proposal of up to 50 newly discovered eligible page URLs if any exist. Stop for separate page-collection approval, then separate ingestion approval. No endpoint-page fetching, raw refresh, API/account/device/payment operation, worker runtime or ingestion is authorized by this proposal. No requests have run.

Review [the machine-readable scope](collection-proposal.json), [baseline](baseline-reconciliation.json), and [preflight](preflight-validation.json).
