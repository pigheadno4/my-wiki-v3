# Braintree C15 fixed query audit — Group A

- Scope: Result Objects (Node.js) + Exceptions (Node.js)
- UTC start: 2026-09-23T11:31:20Z
- UTC analysis end: 2026-09-23T11:32:11Z
- Evidence: both selected raw pages read completely

## Braintree Result Objects (Node.js)

Actual route: `[[index]]` → `[[braintree-index]]` → `[[braintree-server-sdk]]` → `[[source-braintree-result-objects-node]]` → `[[raw/braintree/docs/reference/general/result-objects/node-2026-09-16]]`.

### 1. Where is Braintree Result Objects (Node.js) documented?

- Object/action match: Braintree's Node.js result-wrapper reference and its retrieval location; the route reaches the general result-object page, not a transaction- or Ruby-specific response page.
- Direct answer: use `[[source-braintree-result-objects-node]]`; its factual evidence is `raw/braintree/docs/reference/general/result-objects/node-2026-09-16.md`.
- Raw locator: source URL at line 1; `# Result Objects` at line 14.
- Verdict: **PASS**.

### 2. What does a result object establish, which calls return other shapes, and where are success versus validation-error details?

- Object/action match: API result-wrapper semantics, the documented non-wrapper boundary, and success/validation-detail locations; this does not assume every SDK call has one result shape.
- Direct answer: a result object reports whether the API call succeeded and, on success, contains the requested target object; `result.success` is true in the success case (lines 14–27). Calls without validations—searches are the example—return a collection of requested objects instead of a result object (lines 16–18). An unsuccessful result has `success=false` and may reflect invalid-parameter validation errors, processor declines, gateway rejections or exceptional conditions (lines 29–40). `result.errors` is populated only for failed validation, so false success alone does not establish that `deepErrors()` is available (lines 37–42). Exact callback/Promise nested validation traversal is at lines 43–113; the human-readable message and damaged unresolved SDK-version template are at lines 115–124; submitted params and the credit-card-number/CVV omission are at lines 127–134.
- Raw locator: `# Result Objects`, lines 14–18; `## Success results`, lines 21–27; `## Error results`, lines 29–114; `### Message`, lines 115–124; `### Params`, lines 127–134.
- Verdict: **PASS**.

## Braintree Exceptions (Node.js)

Actual route: `[[index]]` → `[[braintree-index]]` → `[[braintree-server-sdk]]` → `[[source-braintree-exceptions-node]]` → `[[raw/braintree/docs/reference/general/exceptions/node-2026-09-16]]`.

### 3. Where is Braintree Exceptions (Node.js) documented?

- Object/action match: Braintree's Node.js server-SDK exception reference and its retrieval location; the route reaches that exact page rather than a status or validation-errors page.
- Direct answer: use `[[source-braintree-exceptions-node]]`; its factual evidence is `raw/braintree/docs/reference/general/exceptions/node-2026-09-16.md`.
- Raw locator: source URL at line 1; `# Exceptions` at line 14.
- Verdict: **PASS**.

### 4. How are exception handling and timeout/error categories distinguished without inferring transaction outcome or safe retry?

- Object/action match: Node.js exception consumption and category boundaries, especially timeout meaning; this does not ask for transaction success status or a universal retry policy.
- Direct answer: callback error branches and Promise `catch` expose the exception's `type`, `name` and `message`, and older SDK integrations are directed to the migration guide (lines 23–57). Authentication means incorrect API keys; authorization means the key owner's role cannot perform the action and can also cover malformed parameter placement; invalid webhook challenge/signature, not-found, server, unexpected-library, unsafe request-volume, unsupported-version and service-unavailable cases have separate documented meanings (lines 60–124 and 151–155). The timeout headings describe three different boundaries: a request exceeding a custom server-SDK timeout, Braintree servers timing out while delivering a response, and Braintree servers timing out while waiting for the merchant server's complete request (lines 127–148). A custom timeout exception can still precede successful processing within Braintree's stated 60-second gateway timeout, so it does not prove failure or authorize a blind retry. The only action stated here is that a search-call gateway timeout usually suggests splitting a large search into smaller batches (lines 137–141); the page gives no general retry rule for mutations or the other exception classes.
- Raw locator: `## Handling exceptions`, lines 23–57; `## Authentication Error` through `## Upgrade Required Error`, lines 60–124; `## Timeouts`, lines 127–148; `## Service Unavailable Error`, lines 151–155.
- Verdict: **PASS**.

## Bounded group gap sweep and completeness

- Searched Braintree raw filenames for result objects, search results, validation errors, statuses, exceptions, best practices and server-SDK migration; inspected every outbound route in both selected raws.
- Search Results, validation-error catalogs, transaction response objects, Statuses, Best Practices and the migration guide are separate detail authorities. The four fixed questions are fully answered by the two selected raws; no facts were imported from unread related pages and no promotion gap was found.
- Reciprocal routes pass: root index links `braintree-index`; provider index links `braintree-server-sdk`; that concept links both selected sources; each source links the concept and its exact path-qualified raw evidence.
- The campaign's company/provider source aggregates are not yet closed. Direct provider-index/company catalog entries for these new sources remain a **pending coordinator-close item**, not a source or retrieval-route failure; the concept-led routes above already resolve.
- Completeness: exactly four fixed questions answered, two per page; both selected raws read fully; requested objects/actions and precise locators recorded; **4/4 PASS**.

- UTC handoff: 2026-09-23T11:33:12Z
