# Adyen response handling overview retrieval checks

## Q1 — Purpose, scope, and non-inference

**Query:** What response layers does this Adyen overview explain, and does HTTP 200 prove that a payment succeeded or a later webhook was delivered?

**Expected route:** `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-development-resources-overview-response-handling]]`; pinned raw `# Response handling` lines 15–25, `### HTTP status codes` lines 27–31, and `### Raw acquirer responses` lines 39–45.

**Expected answer:** The page explains API request status, raw acquirer response, refusal reason, and result code. HTTP status reports API request processing. A `200/OK` payment request can still correspond to a refused or cancelled transaction, so it is not payment-success proof. This overview gives API-response meaning; it neither documents webhook delivery nor proves final capture or settlement. Use the separate lifecycle and webhook routes for later asynchronous state.

## Q2 — Central capability, prerequisites, warnings

**Query:** How should an integration distinguish transport errors, issuer/acquirer response, refusal reason, and result code in the API response?

**Expected route:** Same source; raw `### Error codes and messages` lines 33–37, `### Raw acquirer responses` lines 39–45, `## How Adyen handles responses` and `### Refusal reasons` lines 47–55, and `### Result codes` lines 57–72. For detailed HTTP interpretation, route to `[[source-adyen-docs-development-resources-response-handling]]`.

**Expected answer:** Non-200 API responses may include `errorCode` and `message` for diagnosis. For a submitted payment, the raw acquirer response reflects the financial institution's authorization/rejection decision and possible reason; Adyen maps it to a refusal reason and result code. The listed result codes summarize payment-level outcomes or communication state: `Authorised`, `Refused`, `Error`, and `Cancelled`. They are not HTTP codes. The mapping and exact result remain transaction- and responder-dependent.
