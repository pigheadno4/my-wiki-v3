# Braintree C14 query audit — Group C

Scope: exactly the four fixed Group C questions for Recurring Billing Testing and Go Live and the Transactions Guide. Both selected raws were read completely; no additional factual evidence was needed.

Timing (UTC): actual start `2026-09-22T13:37:13Z`; analysis end `2026-09-22T13:38:38Z`; handoff `2026-09-22T13:38:44Z`.

## `recurring-billing-testing-go-live-node`

Actual route: `wiki/index.md` (`## PSP Indexes` → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-server-sdk]]`) → `wiki/concepts/braintree-server-sdk.md` (`## Related` → `[[source-braintree-recurring-billing-testing-go-live-node]]`) → `wiki/sources/braintree/source-braintree-recurring-billing-testing-go-live-node.md` (`raw_files` and `## Raw Sources`) → `raw/braintree/docs/guides/recurring-billing/testing-go-live/node-2026-09-16.md`.

1. **Where is Braintree Recurring Billing Testing and Go Live documented?**
   - **Object/action match:** Braintree's Node.js guide for sandbox recurring-billing testing and the transition to production, not the general testing reference or proof of live processing.
   - **Direct answer:** `source-braintree-recurring-billing-testing-go-live-node.md` is the promoted retrieval entry and routes to the complete collected **Testing and Go Live** guide at the exact raw path above.
   - **Exact locator:** selected raw provenance and page identity at lines 1 and 6–7; `# Testing and Go Live`, lines 14–24; `## Go live`, lines 186–190.
   - **Verdict:** PASS — the live provider/concept route reaches the requested guide and its owned raw evidence.

2. **What sandbox testing and production-transition steps or warnings are stated, without treating test data as live behavior?**
   - **Object/action match:** sandbox recurring-billing simulation and production configuration/testing boundaries, not a test-value inventory or a claim that sandbox success proves live availability, settlement or receipt.
   - **Direct answer:** Sandbox recurring-billing testing begins by storing a sandbox payment method with test values, creating a plan and creating a subscription. For card tests, transaction success is controlled by the test amount while verification success is controlled by the test nonce; the listed nonces and Node.js nonce objects simulate sandbox outcomes. A sandbox account is not linked to production: created objects, processing options and recurring-billing settings do not transfer, and login information, merchant ID and API keys differ. For production, the guide recommends a dedicated API user rather than an individual's credentials, then uses that user's production merchant ID, public key and private key; public and private keys are environment- and user-specific. The production account must mirror tested settings, including recreated recurring-billing plans/settings. Server configuration switches to `braintree.Environment.Production` and production credentials; the stated client-token flow needs no client-side configuration change. Production testing uses a limited number of low-value sales for each intended payment-method type, submission for settlement and confirmation of bank deposit. Real payment methods are required, sandbox values do not work, and settled tests debit the associated method and incur fees; use reasonable amounts and few transactions. None of this turns simulated sandbox success or a successful request into proof of production availability or final settlement.
   - **Exact locator:** sandbox setup at lines 16–21; transaction-amount versus verification-nonce control at lines 27–35; test-value categories and Node.js nonce objects at lines 39–183; sandbox/production isolation at lines 186–190; API-user and credential qualifications at lines 193–211; account and Node.js environment transition plus client-token boundary at lines 214–235; low-value live sales, settlement/deposit check and real-method/debit/fee warning at lines 238–244.
   - **Verdict:** PASS — the source/raw pair answers the testing and transition question while preserving the test-versus-production and real-funds boundaries.

## `transactions-guide-node`

Actual route: `wiki/index.md` (`## PSP Indexes` → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-server-sdk]]`) → `wiki/concepts/braintree-server-sdk.md` (`## Related` → `[[source-braintree-transactions-guide-node]]`) → `wiki/sources/braintree/source-braintree-transactions-guide-node.md` (`raw_files` and `## Raw Sources`) → `raw/braintree/docs/guides/transactions/node-2026-09-16.md`.

3. **Where is Braintree Transactions Guide documented?**
   - **Object/action match:** Braintree's Node.js guide that organizes the transaction lifecycle and routes its operations, not a single sale, settlement, validation or dispute endpoint reference.
   - **Direct answer:** `source-braintree-transactions-guide-node.md` is the promoted retrieval entry and routes to the complete collected **Transactions** guide at the exact raw path above.
   - **Exact locator:** selected raw provenance and page identity at lines 1 and 6–7; `# Transactions`, lines 14–20.
   - **Verdict:** PASS — the live provider/concept route reaches the requested Transactions guide and its owned raw evidence.

4. **How are authorization, settlement, validation and dispute routes distinguished, with what material qualifications?**
   - **Object/action match:** transaction lifecycle actions and retrieval routes, not an exhaustive request schema, status catalog, processor-response table or dispute-management specification.
   - **Direct answer:** Creating a sale gets authorization to collect money; collecting it is a separate settlement-submission action. Before settlement a transaction can be voided, while a refund returns previously collected money. Settlement can be requested during `gateway.transaction.sale()` with the Node.js `options.submitForSettlement` field or later with `gateway.transaction.submitForSettlement(transactionId)`; the latter requires an authorized transaction and returns `notFoundError` when the transaction cannot be found. The examples expose `result.transaction` on request success, but do not establish final settlement. Transaction `status` identifies the lifecycle stage, while exact meanings remain in a separate reference. Invalid or malformed transaction details produce transaction validation errors, and associated payment-method, customer or address data can have separate validation errors; duplicate address error codes must be interpreted by parameter scope. Billing-address collection, including at least postal code, is only recommended for certain account setups and can improve authorization likelihood rather than guarantee it. Depending on account setup, bank/card-network disputes can be retrieved through the transaction response's zero-or-more `disputes` array and searched by dispute date; handling after retrieval depends on the banking partner. The guide does not define dispute lifecycle, eligibility, evidence actions or outcomes.
   - **Exact locator:** action distinctions at lines 20–28; lifecycle-status route at lines 31–35; sale-time settlement examples at lines 36–78; separate settlement submission, not-found route and authorization prerequisite at lines 80–106; validation, account-qualified billing guidance and parameter-scoped address errors at lines 107–115; account-qualified dispute retrieval, array/search routes and banking-partner boundary at lines 116–122; deeper processor, rejection, currency, refund/void/credit, 3DS and sandbox navigation at lines 123–134.
   - **Verdict:** PASS — the source/raw pair cleanly distinguishes the requested operations and preserves the material submission, validation, account and dispute qualifications.

## Shared gap sweep and completeness

- **Full selected evidence:** both raws were read from provenance through their final sections. SHA-256 identities match the campaign pins: Testing and Go Live `33bf03a89de049f2ce331d69402f11fa06f0986ec172662228ffdb9b223dd519`; Transactions Guide `98ff39704d69ce9e42d183df0fc7f513cbad07b321adb5fa5495fec270ea53ae`.
- **Bounded gap sweep:** filename and source-reference checks surfaced the two selected guides and their already-linked payment-method, plan, subscription, testing, credential, transaction-operation, status, validation and dispute authorities. The selected raws directly answer all four fixed questions, so adjacent pages remain navigation-only and no extra factual read was needed.
- **Route integrity:** the root index links the Braintree provider index; the provider index links `braintree-server-sdk`; that concept lists each promoted source once; each source reciprocally links the concept and its exact raw. Both routes are live and object-correct.
- **Completeness:** 4/4 fixed questions include object/action match, direct answer, exact locator and verdict. No retrieval repair, additional promotion or extra question is required.

**Group verdict: PASS (4/4).**
