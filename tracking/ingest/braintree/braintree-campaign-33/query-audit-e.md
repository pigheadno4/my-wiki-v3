# Braintree C33 fixed query audit — Group E — 8/8 PASS

- Prompt artifact: `/root/c33_audit_e`
- Analysis end UTC: `2026-10-04T04:21:12Z`
- Artifact handoff UTC: `2026-10-04T04:22:31Z`
- Scope: `reference-forward-api-transformation-errors`, `reference-forward-api-config`, `reference-forward-api-vault-errors`, `reference-forward-api-server-errors`; two fixed questions each.
- Authority rule: concepts were navigation only. Every direct answer was checked against the complete canonical source page and complete pinned raw snapshot. Error/config references do not prove downstream success, payment execution, Orchestration behavior, retry policy, or current production enablement.

## reference-forward-api-transformation-errors

**Object/action matched:** unversioned Braintree Forward API transformation-error reference / report and classify pre-execution transformation failures returned in the caller application's response body.

**Actual route:** `wiki/index.md:11` → `wiki/braintree-index.md:58` → `wiki/concepts/braintree-forward-api.md:27` → `wiki/sources/braintree/source-braintree-reference-forward-api-transformation-errors.md:1-56` → `raw/braintree/docs/reference/forward-api/transformation-errors-2026-09-16.md`.

1. **Q1 — PASS.** This is the collected, unversioned **Transformation Errors** reference for Braintree Forward API. It names no SDK, language, SDK version, endpoint, or sandbox environment. The only environment qualification on this page is that production Forward API use is subject to eligibility, with Account Manager/Business Development inquiry routes. The documented object is a response-body transformation failure, and its JSON is explicitly only a format-resembling example, not a complete required schema. Identity/metadata: raw `5-14`; production eligibility: `17-20`; illustrative response: `22-34`.
2. **Q2 — PASS.** Forward API type-checks a transformation before performing it. The common type-check failure is `Received invalid transformation. Does not type check`; its `message` includes the transformation flag, triggering expression, and `type_errors`. Results must serialize as boolean, nil, number, or string; the catalog also covers invalid expiration inputs, unsupported encoding, non-numeric integer conversion, and out-of-bounds slicing. The type-error categories are invalid arity, invalid argument type, and invalid function name, and one transformation can return multiple type errors. This failure reference defines no retry, destination receipt/success, or payment lifecycle. Locators: raw `35-45`, `48-60`.

## reference-forward-api-config

**Object/action matched:** unversioned Braintree Forward API config reference / describe the third-party destination request template used to encode, method-select, and inject payment data into an outbound request.

**Actual route:** `wiki/index.md:11` → `wiki/braintree-index.md:58` → `wiki/concepts/braintree-forward-api.md:26` → `wiki/sources/braintree/source-braintree-reference-forward-api-config.md:1-38` → `raw/braintree/docs/reference/forward-api/config-2026-09-16.md`.

1. **Q1 — PASS.** This is the collected, unversioned **Config** reference for Forward API, not an SDK guide or an Orchestration processor-connection flow. It names no language, SDK version, or endpoint. It documents both environments: production use is eligibility-gated and production configs are submitted as JSON for Braintree review, approval, and loading; sandbox permits an inline config with the forwarding request or a submitted JSON file. Identity/availability: raw `5-22`; environment handling: `25-28`.
2. **Q2 — PASS.** The config's central purpose is to describe the destination request's encoding, HTTP method, and payment-data injection. After a config has been loaded, both sandbox and production can identify it by name. The JSON block is one illustrative config with method, name, request-format, transformation, payment-type, and URL-pattern values; it is not a universal schema. This page does not establish credential exchange, destination authorization/acceptance, payment execution, authorization, capture, settlement, or current eligibility. Locators: raw `22-28`, `36-55`.

## reference-forward-api-vault-errors

**Object/action matched:** unversioned Braintree Forward API Vault-error reference / report Vault access, payment-method lookup/export, binding, and PayPal-account forwarding prerequisite failures in the caller application's response body.

**Actual route:** `wiki/index.md:11` → `wiki/braintree-index.md:58` → `wiki/concepts/braintree-forward-api.md:25` → `wiki/sources/braintree/source-braintree-reference-forward-api-vault-errors.md:1-59` → `raw/braintree/docs/reference/forward-api/vault-errors-2026-09-16.md`.

1. **Q1 — PASS.** This is the collected, unversioned **Vault Errors** reference for Forward API. It names no SDK, language, SDK version, endpoint, or sandbox environment; production use alone is identified and remains subject to eligibility. The documented object is a Vault failure returned in the response body. The shown `error`/nested `message`/`request-uuid` JSON only resembles the response format and is not a guaranteed exhaustive schema. Identity/availability: raw `5-20`; illustrative body: `22-34`.
2. **Q2 — PASS.** The catalog maps `401` to invalid credentials or an IP allowlist violation and `403` to credentials lacking the Forward API right, with a contact route to confirm that the user's credentials are allowlisted. It distinguishes invalid merchant, nonce, and token `404`s from `422` malformed/insufficient data, non-exportable methods, and payment-method or `cse_data` binding failures. For a PayPal account specifically, the nonce must come from the Vault flow, and the additional text requires a Pre-Approved Payment enabled PayPal account for exporting. These are access/export/binding failure conditions, not credential provisioning, automatic retry, destination processing, or payment-lifecycle evidence. Locators: raw `35-45`.

## reference-forward-api-server-errors

**Object/action matched:** unversioned Braintree Forward API server-error reference / report Forward API inability to complete a request, including timeout/TLS failures and relay of a destination-originated 5xx.

**Actual route:** `wiki/index.md:11` → `wiki/braintree-index.md:58` → `wiki/concepts/braintree-forward-api.md:24` → `wiki/sources/braintree/source-braintree-reference-forward-api-server-errors.md:1-50` → `raw/braintree/docs/reference/forward-api/server-errors-2026-09-16.md`.

1. **Q1 — PASS.** This is the collected, unversioned **Server Errors** reference for Forward API. It names no SDK, language, SDK version, endpoint, or sandbox environment; production use is eligibility-gated. The object is a server failure returned when Forward API cannot complete the request. Its `error`/nested `message`/`request-uuid` JSON only resembles the response format and is illustrative, not a required schema. Identity/availability: raw `5-19`; example: `19-30`.
2. **Q2 — PASS.** The catalog maps TCP connect timeout, request-processing timeout, and between-packet socket timeout to HTTP 504, and a failed destination TLS handshake to HTTP 502. A destination-originated 5xx is materially different: Forward API returns HTTP 200 while the body carries the destination response error in its `status` field. Forward API HTTP 200 therefore does not prove destination success or a payment outcome. The page defines no retry/remediation policy, downstream success, or payment lifecycle. Locators: raw `32-40`.

## Shared provenance, gaps, sweep, and link checks

- **Manifest/hash PASS:** transformation errors `2e4d07769683941e70c78d3922be5ce2a4380820a5261e5da31b335457225451`; config `c211b92b4d4838cf2f9367756506e6dbbccf10c99f4b9d6c15f10313c734a69e`; Vault errors `881881f5ef887f46661c66844d8bf28039fae377a76c93b78c215da214fc9191`; server errors `e981e4287cfff545f575c99dc3de01bf6e69565b635d49b0795b820dfdddf014`. Recomputed bytes match `manifest.json`.
- **Canonical/source/raw PASS:** every source canonical URL and sole `raw_files` entry match its manifest job; every exact dated `## Raw Sources` link exists; every pinned raw source comment matches the canonical URL. Reverse `raw_files` lookup maps each primary raw to exactly its assigned canonical source. Exact source-comment searches found one retained raw per canonical URL and no older same-canonical snapshot, so no historical conflict read was required.
- **Factual/navigation PASS:** every retained claim above is directly supported by the selected raw locators. Each source links `braintree-forward-api`, and that concept links back to all four sources. Root → Braintree index → concept → source → raw is live for all four; provider-index and company-catalog direct rows also exist. Campaign-wide aggregate close remains coordinator-owned and is not inferred from this audit.
- **Sweep / extra reads:** filename, exact-canonical, distinctive-content, and declared-related-reference sweeps found the adjacent Forward API overview, forward request, functions, transformations, configuration, examples, validation-errors, payment-method, and IP-allowlisting material. The selected raws already supply the exact identities, purposes, access/config/environment/security qualifications, and status behavior needed here; no discovered conflict or missing selected authority required promoting an adjacent page to factual authority or full-reading an older history. No raw promotion is recommended.
- **Concrete failures:** none. All eight fixed questions are answered from successfully retrieved, complete, hash-matched selected evidence. Illustrative JSON is not treated as schema; transformation failures remain pre-execution type-checking evidence; config production review/load remains distinct from sandbox inline use; Vault access and PayPal Vault-flow scope stay narrow; destination 5xx carried inside Forward API HTTP 200 is not downstream success. No retry, destination success, payment, Orchestration, or current-enablement claim is invented.
