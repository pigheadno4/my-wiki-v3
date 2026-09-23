# Braintree C15 query audit — Group C

Scope: exactly the four fixed Group C questions for AVS and CVV Responses and Settlement Responses. Both selected raws were read completely; no additional factual evidence was needed.

Timing (UTC): start `2026-09-23T11:33:42Z`; analysis end `2026-09-23T11:36:34Z`; handoff `2026-09-23T11:36:45Z`.

## `avs-cvv-responses`

Actual route: `wiki/index.md` (`## PSP Indexes` → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-server-sdk]]`) → `wiki/concepts/braintree-server-sdk.md` (`## Related` → `[[source-braintree-avs-cvv-responses]]`) → `wiki/sources/braintree/source-braintree-avs-cvv-responses.md` (`raw_files` and `## Raw Sources`) → `raw/braintree/docs/reference/general/processor-responses/avs-cvv-responses-2026-09-16.md`.

1. **Where is Braintree AVS and CVV Responses documented?**
   - **Object/action match:** response-category semantics for AVS postal/street checks and CVV checks, not a complete transaction-response object, an SDK field-placement reference, or a fraud-decision rule.
   - **Direct answer:** `source-braintree-avs-cvv-responses.md` is the promoted retrieval entry and routes to the complete collected `# AVS and CVV Response Codes` raw at the path above.
   - **Exact locator:** raw provenance and canonical path at lines 1 and 6–7; page identity at line 14; damaged response-object introduction at line 16; AVS and CVV tables at lines 17–45.
   - **Verdict:** PASS.

2. **Which AVS and CVV result categories are documented, and what cannot be inferred from the damaged response-object introduction?**
   - **Object/action match:** category meanings only, not transaction approval, decline, fraud disposition, retry behavior, object names, or SDK field placement.
   - **Direct answer:** AVS reports postal code and street address separately: `M` means match, `N` mismatch, `U` received but not verified, and `I` not provided. For both postal and street `U`, the page says the processor typically declined authorization before the bank evaluated the value, so `U` is not `N`. AVS also documents issuing-bank non-support `S` (typically a bank outside the US, Canada and UK), system error `E`, not applicable `A`, and skipped `B`. CVV documents match `M`, mismatch `N`, not verified `U`, not provided `I`, issuer nonparticipation `S`, not applicable `A`, and skipped `B`; CVV `U` likewise may follow an authorization decline before evaluation, while CVV `I` also occurs for a transaction made with a vaulted payment method. The introduction is damaged as `Available on theandresponse objects.` It cannot establish response-object names, field placement, or any transaction/fraud/retry outcome, and none should be reconstructed from the tables.
   - **Exact locator:** damaged introduction at line 16; AVS postal categories at lines 19–24; AVS street and remaining categories at lines 25–32; CVV categories and vaulted-`I` qualification at lines 35–45.
   - **Verdict:** PASS.

## `settlement-responses`

Actual route: `wiki/index.md` (`## PSP Indexes` → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-server-sdk]]`) → `wiki/concepts/braintree-server-sdk.md` (`## Related` → `[[source-braintree-settlement-responses]]`) → `wiki/sources/braintree/source-braintree-settlement-responses.md` (`raw_files` and `## Raw Sources`) → `raw/braintree/docs/reference/general/processor-responses/settlement-responses-2026-09-16.md`.

3. **Where is Braintree Settlement Responses documented?**
   - **Object/action match:** 4000-class processor responses for capture-funds requests, not the settlement-submission operation, authorization approval, or final funds-movement ledger.
   - **Direct answer:** `source-braintree-settlement-responses.md` is the promoted retrieval entry and routes to the complete collected `# Settlement` response table at the path above.
   - **Exact locator:** raw provenance and canonical path at lines 1 and 6–7; page identity and capture-request scope at lines 14–17; approval, pending and decline sections at lines 18–49.
   - **Verdict:** PASS.

4. **How are settlement approval, pending and decline responses distinguished without turning a pending request into final settlement?**
   - **Object/action match:** capture-request processor-response classes and their transaction-status consequence, not a guarantee of funds movement, eventual settlement, fulfillment safety, or retry safety.
   - **Direct answer:** The page says 4000-class codes indicate success or failure of the request to capture funds and that Braintree updates transaction status from the processor response. `4000 Settled` is the sole approval row. `4002 Settlement Pending` is a separate pending-request row; it is not `4000`, does not itself establish final settlement or confirmed funds movement, and supplies no eventual-outcome or general retry rule. Declines begin with `4001 Settlement Declined` for a processor-refused sale or refund settlement request and continue with already-captured, already-refunded, risk, capture-limit, and PayPal refund/account cases. `4018 PayPal Pending Payments Not Supported` is itself a decline for a PayPal pending sale/refund response disallowed by Braintree, with likely account misconfiguration and a transaction-details route; it must not be collapsed into `4002`.
   - **Exact locator:** capture-request scope and status update at lines 16–17; `4000 Settled` at lines 18–22; `4002 Settlement Pending` at lines 25–29; settlement declines at lines 32–49; distinct `4018` decline at line 41.
   - **Verdict:** PASS.

## Shared gap sweep and completeness

- **Full selected evidence:** both raws were read from provenance through their final rows. SHA-256 identities match the campaign pins: AVS/CVV `8c85badbe6e42704ebc46e26ed8ee85e3ee143c9bc00035d3ab6cdc33f9aca41`; Settlement `3ef08acd765c4b6186e120349fd5ca6dd328166d20203005d5fc324c51218665`.
- **Bounded gap sweep:** filename and source-reference checks surfaced the two selected response tables, AVS/CVV's linked Vault-rules raw, and Settlement's linked transaction-status and operation routes. The selected raws directly answer all four questions, including vaulted CVV `I` and pending-versus-settled semantics, so adjacent pages remain navigation-only.
- **Route and catalog integrity:** the root index links the Braintree provider index; the provider index links `braintree-server-sdk`; that concept lists each promoted source once; each source reciprocally links the concept and exact raw. The provider index directly catalogs AVS/CVV and Settlement once each, and `wiki/companies/braintree.md` also directly catalogs each once with the correct evidence boundary.
- **Completeness:** 4/4 fixed questions include object/action match, direct answer, exact locator and verdict. AVS/CVV categories are not turned into transaction outcomes; damaged object names remain unreconstructed; `4002 Settlement Pending` remains distinct from `4000 Settled` and `4018` decline. No repair or extra question is required.

**Group verdict: PASS (4/4).**
