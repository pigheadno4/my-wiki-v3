# Braintree C06 final query audit

Overall: 10/10 PASS; no extra selected raw reads or post-audit repairs.
Coordinator mechanical close check separately passed; Audit A pending-catalog observation was resolved by final aggregation.

# Braintree C06 final query audit — group A

Timing (UTC): actual_start `2026-09-20T13:56:42Z`; analysis_end `2026-09-20T13:58:32Z`; handoff `2026-09-20T13:59:28Z`.

## `customer-update-node`

Actual route: `wiki/index.md` (`## PSP Indexes` → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-server-sdk]]`) → `wiki/concepts/braintree-server-sdk.md` (`## Related` → `[[source-braintree-customer-update-node]]`) → `wiki/sources/braintree/source-braintree-customer-update-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/request/customer/update/node-2026-09-16.md`.

1. **Navigation question — Where is Node customer updating by ID documented?**
   - **Object/action match:** Yes — the route reaches Node `Customer: Update` and `gateway.customer.update(customerId, attributes)`; this is customer mutation by ID, not customer lookup or standalone payment-method update.
   - **Direct answer:** `[[source-braintree-customer-update-node]]` routes to the collected Node customer-update guide. Its opening states that the customer's ID is supplied with new attributes and shows the callback invocation.
   - **Exact raw locator:** `# Customer: Update`, lines 13–27; operation statement at line 17 and invocation at lines 20–27.
   - **Verdict:** **PASS**.

2. **Detail question — Where are omitted-attribute behavior, existing versus new payment-method updates, default selection and verification qualifications documented?**
   - **Object/action match:** Yes — these are customer-update semantics and nested payment-method/card options on the same Node operation; existing-card mutation is kept distinct from associating a new method.
   - **Direct answer:** Omitted customer attributes remain unchanged. Updating an existing method through customer update is limited here to credit cards and uses the existing card token in `creditCard.options.updateExistingToken`; the collected note's route for updating other existing payment-method types is incomplete and is not reconstructed. Omitting `update_existing_token` creates and associates a new credit card, while a payment-method nonce can associate a new payment method of any type. For nested billing addresses, `updateExisting: true` updates the address; omitting it creates a new address, associates it with the card, and leaves the old address attached to the customer but no longer as that card's billing address. Default selection passes the payment-method token as `defaultPaymentMethodToken`. Card validation runs by default but verification does not; Braintree recommends account-wide verification, the manual example sets `verifyCard: true`, and Premium Fraud Management Tools users are strongly advised to pass `device_data` each time a card is verified.
   - **Exact raw locator:** unchanged omissions at `# Customer: Update`, line 17; existing-card scope, incomplete non-card route and token option at `## Examples > ### Update customer and existing credit card`, lines 32–63; nested billing-address update/omission behavior at `### Update customer, credit card, and billing address`, lines 88–135; new-credit-card and any-payment-method association at `### Update customer and create new payment method`, lines 136–181; default selection at `### Update default payment method`, lines 184–203; verification qualifications at `### Card verification`, lines 206–240.
   - **Verdict:** **PASS**.

## `transaction-find-node`

Actual route: `wiki/index.md` (`## PSP Indexes` → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-server-sdk]]`) → `wiki/concepts/braintree-server-sdk.md` (`## Related` → `[[source-braintree-transaction-find-node]]`) → `wiki/sources/braintree/source-braintree-transaction-find-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/request/transaction/find/node-2026-09-16.md`.

3. **Navigation question — Where is Node transaction lookup by ID documented?**
   - **Object/action match:** Yes — the route reaches Node `Transaction: Find` and `gateway.transaction.find(transactionId)`; this is lookup of one transaction by ID, not transaction search, creation or settlement.
   - **Direct answer:** `[[source-braintree-transaction-find-node]]` routes to the collected Node transaction-find reference, which shows callback and Promise forms passing a transaction ID; a missing transaction routes to `notFoundError`.
   - **Exact raw locator:** `# Transaction: Find > ### Callback`, lines 20–23; `### Promise`, lines 25–28; missing-transaction route at line 29.
   - **Verdict:** **PASS**.

4. **Detail question — What result-limitation notice is stated and where is the Marketplace escrow-status example?**
   - **Object/action match:** Yes — the notice applies to transaction-find results, and the requested example is explicitly for escrow status on Braintree Marketplace transactions.
   - **Direct answer:** The page states only that results are limited according to the linked PayPal Data Protection Addendum for Card Processing Products policy. That external policy was not selected or read, so this audit does not infer which fields are limited or why. The Braintree Marketplace section uses a transaction ID to find the transaction and reads `escrowStatus` in callback and Promise examples; the shown `"held"` value is an example, not a universal Marketplace status.
   - **Exact raw locator:** result-limitation notice at `# Transaction: Find`, lines 16–17; `### Escrow status on Braintree Marketplace transactions`, lines 30–45 (scope/purpose at lines 30–32, callback at lines 33–38, Promise at lines 40–45).
   - **Verdict:** **PASS**.

## Shared checks

- **Gap sweep / extra reads:** Filename and action-text sweeps surfaced adjacent customer find/update authorities, credit-card and payment-method update pages, transaction search/response material, and transaction-line-item lookup. Neither promoted source has a `## Related raw API references` section. The two exact selected raws directly answer all four fixed object/actions; no neighboring raw or external policy was needed or selected for full reading, and no relevant conflict was found. No historical equivalence was inferred.
- **Reciprocal routes:** **PASS** — all links in both actual routes resolve. Each source links back to `[[braintree-server-sdk]]`; the concept contains each source link exactly once; each source contains the exact path-qualified raw link. Direct provider-source catalog entries and other shared aggregates are still pending, but both required concept-led routes are live.
- **Raw identity:** **PASS** — source `canonical_url`, `raw_files` and `## Raw Sources` match the manifest. Computed SHA-256 values match: customer update `e9082439e7ae5b1bf2c6714c25ef5f2c086308e749084a0ef2b5e556b4cfa3e0`; transaction find `5e3101952dfe03bea32c8f766d396c9da4999b7fe58e7a679a783b40dde1b768`.
- **Completeness:** 2 pages; exactly 4/4 predetermined questions; 4 PASS, 0 FAIL, 0 unresolved; no repair required.

**Group verdict: PASS (4/4).**

# Braintree C06 final query audit — group B

Timing (UTC): actual start `2026-09-20T14:04:07Z`; analysis end `2026-09-20T14:06:00Z`; handoff `2026-09-20T14:06:47Z`.

## `subscription-cancel-node`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-server-sdk]]` → `[[source-braintree-subscription-cancel-node]]` → `[[raw/braintree/docs/reference/request/subscription/cancel/node-2026-09-16]]`.

1. **Where is Node subscription cancellation documented?** Object/action match: PASS — the reached page is the Node subscription-cancel operation, not customer or payment-method deletion. Answer: the source routes to the pinned `Subscription: Cancel` reference and its callback/Promise calls to `gateway.subscription.cancel("theSubscriptionId")`. Exact locator: raw lines 13–25 (purpose at line 15; callback lines 16–20; Promise lines 22–25). Verdict: **PASS**.
2. **What billing effect and result or error guidance does this page state?** Object/action match: PASS — this is the page-stated effect/result boundary for canceling one subscription, not refund, proration, paid-term, deletion, or timing behavior. Answer: cancellation stops billing a credit card; callback and Promise forms return `result`; a missing subscription returns `notFoundError`; after cancellation the subscription cannot be edited or reactivated and a new subscription is required. Exact locator: raw line 15, lines 18–25, and lines 27–29. Verdict: **PASS**.

## `webhooks-subscription-node`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-webhooks]]` → `[[source-braintree-webhooks-subscription-node]]` → `[[raw/braintree/docs/reference/general/webhooks/subscription/node-2026-09-16]]`.

3. **Where are subscription notification kinds and payload routes documented?** Object/action match: PASS — the reached Node page is the subscription webhook event reference, not general webhook delivery or subscription billing behavior. Answer: **Notification kinds** defines `kind` and the eight subscription-event rows; **Attributes** routes the notification kind, UTC trigger time, and `Subscription` object. Exact locator: raw lines 17–32 and 35–37. Verdict: **PASS**.
4. **Where are event-trigger qualifications and payload-content limits documented?** Object/action match: PASS — the answer uses the event-specific rows and payload statement, not universal delivery or payment-finality claims. Answer: the table qualifies skipped billing by a covering zero/negative balance; successful charge includes mid-cycle upgrade proration; unsuccessful charge requires an existing subscription and excludes manual retries and failed creation attempts; active means first authorized transaction or successful Past Due→Active recovery and excludes trial→first-cycle; past due requires the billing cycle's initial transaction decline and fires only once that cycle after transition. The payload's `Subscription` object contains only the 20 most recent associated transactions. Exact locator: raw lines 21–32 (especially 25, 27–28, 31–32) and lines 35–37. Verdict: **PASS**.

## `subscription-find-node`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-server-sdk]]` → `[[source-braintree-subscription-find-node]]` → `[[raw/braintree/docs/reference/request/subscription/find/node-2026-09-16]]`.

5. **Where is lookup of a single subscription by ID documented?** Object/action match: PASS — the reached page retrieves one existing subscription by ID, not subscription search, creation, or cancellation. Answer: the `Subscription: Find` raw states the single-ID lookup purpose; although its prose omits the method name, the displayed Node examples document `gateway.subscription.find("aSubscriptionId")`. Exact locator: raw line 21 and lines 22–31. Verdict: **PASS**.
6. **Where are callback and Promise invocation forms, result handling and the result-limitation notice documented?** Object/action match: PASS — this is invocation/result evidence for subscription Find; no missing method or policy meaning is reconstructed. Answer: the callback receives `(err, result)` and the Promise resolves to `result`; the page links the `Subscription` response object, returns `notFoundError` when absent, and says results are limited according to the linked PayPal Data Protection Addendum without specifying or explaining that external policy. The incomplete `Otherwise, use.` sentence establishes no alternative action. Exact locator: raw lines 16–19, callback lines 22–26, Promise lines 28–31, and lines 33–35. Verdict: **PASS**.

## Completeness check

All three selected raws were read completely through their final numbered lines (37, 37, and 35); extra full reads: none. Topic/filename/content and exact-canonical-URL sweeps found no second snapshot or competing owner for the three selected pages; adjacent subscription operations, the subscription response page, and broader webhook pages were not selected because the fixed questions are answered directly by the pinned raws and no selected-evidence conflict required expansion. SHA-256: **PASS 3/3** (`12bca1403d0fe59bad5ea5ab592af80c33d0e08042b85f1fbef3085eee22096a`, `e5de3f19807dbabd6e771d6b23f57205dd74cd1cf2b7e0dc921b03ab5b7d55d4`, `83abc3c9f551511da1db3d156533e841bdff5a4f30e6d0a9842b517488e2dd40`). Manifest, raw Source URL, source `canonical_url`, and `raw_files` owner agree **3/3**. Root→provider index, provider index→concept, concept→source, source→concept, and source→exact raw links resolve reciprocally **3/3**, with one source owner per raw. Material meaning/warnings are preserved **3/3**. Result: **6/6 PASS; no retrieval repair required**.
