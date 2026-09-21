# Braintree C10 quality audit

Final result: 20/20 fixed questions PASS across ten pages. Five disjoint groups
form one audit; no extra three-page audit, retrieval repair or selected extra raw
read during the query audit. Coordinator checked all assigned object/action
matches, direct answers, evidence routes and group completeness before acceptance.
The Transaction initial reviewer separately read the existing overview raw for
scope comparison; that authority read is not a query-audit read or retry.

Mechanical close: PASS on 2026-09-21. All10 final canonical pages equal their
approved candidates/receipts; exact hashes, canonical identities, unique raw
owners, path-qualified raw links, approved snippets and reciprocal routes agree.
Company/provider index catalogs are unique;71 sources=55 website+16 GitHub,
excluding changelogs. All14 touched typed pages pass validate_wiki checks;
git diff --check passed. No code unit suite was run for this documentation-only
campaign. Earlier groups' pending-catalog notes describe their audit-time state;
aggregate catalogs were subsequently checked at the single mechanical close.


# Braintree C10 query audit — Group A (Payment Method Create/Update)

Scope: `payment-method-create-node` and `payment-method-update-node`; exactly four fixed questions from `tracking/ingest/braintree/braintree-campaign-10/selection-review.md`. This is Group A of the single 20-question C10 audit.

Timing (UTC): actual_start `2026-09-21T11:31:27Z`; analysis_end `2026-09-21T11:32:52Z`; handoff `2026-09-21T11:32:57Z`.

## `payment-method-create-node`

Actual route: `wiki/index.md` (`## PSP Indexes` → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-server-sdk]]`) → `wiki/concepts/braintree-server-sdk.md` (`## Related` → `[[source-braintree-payment-method-create-node]]`) → `wiki/sources/braintree/source-braintree-payment-method-create-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/request/payment-method/create/node-2026-09-16.md`.

1. **Navigation question — Where is Node payment-method creation for an existing customer documented?**
   - **Object/action match:** Yes — the route reaches Node `Payment Method: Create` for adding a payment method to an existing customer, not customer creation, credit-card creation, nonce creation, or payment-method update.
   - **Direct answer:** `[[source-braintree-payment-method-create-node]]` routes to the pinned Node request reference. The raw states the existing-customer creation purpose and shows `gateway.paymentMethod.create({ customerId, paymentMethodNonce }, callback)`.
   - **Exact raw locator:** `# Payment Method: Create`, lines 13–19; `### Node`, lines 22–30, with the invocation at lines 24–29.
   - **Verdict:** **PASS**.

2. **Detail question — What prerequisites and payment-type qualifications are stated, and where are duplicate prevention, verification and nonce/raw-data rules?**
   - **Object/action match:** Yes — these are the create page's existing-customer inputs and creation-time default, address, duplicate, verification, and nonce/raw-card rules; no sibling customer, credit-card, or nonce endpoint behavior is imported.
   - **Direct answer:** For the documented existing-customer route, the page calls customer ID and payment-method nonce the only required attributes and separately links customer creation as another route. When a customer has multiple payment methods, the first created becomes default; `makeDefault: true` selects the new one, and the default is used for transactions created with customer ID. A supplied billing address is ignored for a PayPal account and overrides an address supplied during nonce creation; an existing customer address can instead be supplied by ID. Duplicate rejection uses `failOnDuplicatePaymentMethod`, but that option is ignored for PayPal, Pay with Venmo, Apple Pay, Google Pay, and ACH payment methods. Credit-card validations run by default while verification does not; Braintree recommends account-wide verification, manual verification uses `verifyCard: true`, and Premium Fraud Management Tools carry the recommendation to pass `device_data` each time a card is verified. The page recommends passing only a nonce; when raw card data and a nonce are both supplied, explicit fields take precedence and remaining attributes come from the nonce.
   - **Exact raw locator:** prerequisite and alternate customer-creation route at lines 17–19; default behavior at `### New default payment method`, lines 60–87; new-address PayPal/precedence qualification at lines 89–116 and existing-address-ID form at lines 118–141; duplicate option and payment-type exclusions at lines 143–170; validation, verification and `device_data` guidance at lines 172–202; nonce/raw-card recommendation and precedence at lines 205–209.
   - **Verdict:** **PASS**.

## `payment-method-update-node`

Actual route: `wiki/index.md` (`## PSP Indexes` → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-server-sdk]]`) → `wiki/concepts/braintree-server-sdk.md` (`## Related` → `[[source-braintree-payment-method-update-node]]`) → `wiki/sources/braintree/source-braintree-payment-method-update-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/request/payment-method/update/node-2026-09-16.md`.

3. **Navigation question — Where is Node updating of a stored payment method documented?**
   - **Object/action match:** Yes — the route reaches Node `Payment Method: Update` for a stored payment-method token, not payment-method creation, credit-card-only update, customer update, or PayPal checkout.
   - **Direct answer:** `[[source-braintree-payment-method-update-node]]` routes to the pinned Node request reference. Its base example invokes `gateway.paymentMethod.update("theToken", attributes)`.
   - **Exact raw locator:** `# Payment Method: Update`, lines 13–19; `### Node`, lines 22–32, with the invocation at lines 24–31.
   - **Verdict:** **PASS**.

4. **Detail question — Where are billing-address, PayPal-token, default-selection and verification qualifications; what omission or nonce behavior is explicitly stated?**
   - **Object/action match:** Yes — every qualification comes from the stored-payment-method update page, with credit-card-only and PayPal-only behavior kept distinct and the damaged non-card destination left unreconstructed.
   - **Direct answer:** `billingAddress.options.updateExisting: true` mutates the existing address and therefore affects other payment methods sharing it; omitting `updateExisting` creates a new address while leaving the old one in the customer's Vault, and `billingAddressId` selects an existing customer address. A PayPal account can update only its associated token or default status. This call can make only a credit card or PayPal account default; the collected destination for other types is damaged after `default_payment_method_token`, and the page recommends customer update instead. Credit-card validations run by default while verification does not; enabled AVS/CVV checks run on update and `verifyCard: false` skips them, while manual verification uses `verifyCard: true`. Premium Fraud Management Tools carry the `device_data` recommendation for each verification. Specifically for verifying AVS information on an existing payment method with `verifyCard: true`, the page says the update creates a transaction; if processing options reject transactions without CVV, include CVV or disable that rule. For credit-card updates using a nonce, client-supplied fields already inside nonce data should not also be explicit; the nonce must not be associated with a customer, and a nonce authorized with customer ID raises the linked cannot-update-card error. When raw data and nonce are both supplied, the page recommends nonce only; explicit fields take precedence and remaining attributes come from the nonce.
   - **Exact raw locator:** enabled card-verification qualification at lines 18–19; shared-address mutation at lines 37–63, omission behavior at lines 64–91, and existing-address reuse at lines 93–108; PayPal-token restriction at lines 110–125; default-type boundary, damaged destination and customer-update recommendation at lines 127–149; validation, AVS/CVV, `verifyCard` and `device_data` guidance at lines 152–178; duplicate-field warning at lines 181–187; customer-unassociated nonce restriction at lines 216–217; AVS transaction/CVV action at line 223; raw-card/nonce recommendation and precedence at lines 235–239.
   - **Verdict:** **PASS**.

## Shared gap sweep and completeness check

- Both selected raws were read completely. Filename and exact-claim sweeps surfaced the payment-method nonce guide and endpoints, payment-method response/guide pages, credit-card and customer create/update pages, credit-card-verification creation, validation errors, and card-verification/fraud guides. No extra raw was selected: the two exact Node operation raws directly answer all four fixed questions, the Create source's related API references remain navigation-only, and sibling-operation or global-guide behavior is not needed to resolve an evidence gap or conflict. No historical raw was selected because no question asks about history and no relevant conflict was discovered.
- Reciprocal routes: **PASS** — root index → Braintree index → `[[braintree-server-sdk]]` resolves; the concept contains each audited source exactly once; each source links back to that concept and contains its exact path-qualified raw link. Aggregate direct source catalog entries in `wiki/braintree-index.md` are still pending, but both required concept-led routes are live.
- Raw identity: **PASS 2/2** — source `canonical_url`, `raw_files`, path-qualified Raw Sources link, raw Source URL, manifest identity and computed SHA-256 agree for Create (`826fd4507841c645de8ef9e3255b862acaf12730ca88c62925e61c5a20423660`) and Update (`93d912a7f1aa11b05dc2f2d869e1c7c71388a24b168f780271a052cba96ecce0`).
- Completeness: **PASS** — 2 routes; exactly 4/4 predetermined questions; 4/4 object/action matches, direct answers, exact locators and PASS verdicts; no retrieval repair, extra full read, promotion recommendation, contradiction, or unresolved answer.

**Group verdict: PASS (4/4).**

# Braintree C10 query audit — Group B

- Scope: four of 20 fixed questions; Subscription Search + Subscription Retry Charge.
- `start_utc`: `2026-09-21T11:24:30Z`
- `analysis_end_utc`: `2026-09-21T11:25:39Z`
- `handoff_utc`: `2026-09-21T11:25:47Z`
- Aggregate company/provider-index/log/count work: pending; not part of this audit.

## Subscription Search (Node.js)

Route: [[index]] → [[braintree-index]] → [[braintree-server-sdk]] → [[source-braintree-subscription-search-node]] → [[raw/braintree/docs/reference/request/subscription/search/node-2026-09-16]].

1. **Navigation question — Where is searching subscriptions using Node documented?**
   - Object/action match: Node.js search of subscriptions, not single-subscription ID lookup.
   - Direct answer: `[[source-braintree-subscription-search-node]]`, backed by `[[raw/braintree/docs/reference/request/subscription/search/node-2026-09-16]]`, documents `gateway.subscription.search()`.
   - Exact locator: raw `# Subscription: Search`, lines 13–30.
   - Verdict: **PASS**.

2. **Detail question — How are results consumed and filters located, and what result-limitation notice must be retained?**
   - Object/action match: consumption of Node subscription-search results, filter-documentation routes, and the page's explicit limitation notice.
   - Direct answer: the page says the operation returns Subscription response objects. Its callback form iterates with `response.each()`; its stream forms use `pipe()` or `data`/`end` handlers followed by `resume()`. Operators are routed to the linked Search fields page, while this raw's `## Examples` section contains qualified examples for range fields, multiple-value fields, active subscriptions with or without a trial period, days past due, merchant account ID, billing cycles remaining, next billing date, created-at time, and combined fields. Retain the notice that results are limited according to the linked PayPal Data Protection Addendum for Card Processing Products policy, without interpreting the unread policy or claiming which results or fields are limited. Do not reconstruct the missing SDK version values in `versionor greater` / `versioncan`, or the method missing from `useinstead` for single-ID lookup.
   - Exact locator: result objects and Search fields route at lines 16–21; callback iteration at lines 23–30; damaged single-ID prose at line 32; stream consumption and damaged version prose at lines 33–61; filter examples at lines 62–180; Search fields/results links at lines 182–187.
   - Verdict: **PASS**.

## Subscription Retry Charge (Node.js)

Route: [[index]] → [[braintree-index]] → [[braintree-server-sdk]] → [[source-braintree-subscription-retry-charge-node]] → [[raw/braintree/docs/reference/request/subscription/retry-charge/node-2026-09-16]].

3. **Navigation question — Where is manually retrying a past-due subscription charge documented?**
   - Object/action match: manual retry of a charge for a past-due subscription, not automatic retry scheduling or generic transaction settlement.
   - Direct answer: `[[source-braintree-subscription-retry-charge-node]]`, backed by `[[raw/braintree/docs/reference/request/subscription/retry-charge/node-2026-09-16]]`, documents `gateway.subscription.retryCharge()` for manually retrying past-due subscriptions.
   - Exact locator: raw `# Subscription: Retry Charge`, lines 13–27.
   - Verdict: **PASS**.

4. **Detail question — What amount, result, and settlement behavior do the displayed examples and qualifications establish?**
   - Object/action match: only the inputs, result access, and settlement sequence shown on the Node retry-charge page.
   - Direct answer: every displayed retry passes `subscription.id` and the explicit string amount `"24.00"`; the page does not establish currency, a default or omitted amount, whether other amounts are permitted, or whether this is the whole past-due balance. The opening callback and Promise examples also pass an unlabeled third argument `true` and display `result.success` as `true`; this does not establish the argument's semantics, payment finality, or settlement completion. In the section titled **Manually submit transaction for settlement**, retry calls omit the third argument; only when `retryResult.success` is true do the examples pass `retryResult.transaction.id` to `gateway.transaction.submitForSettlement()`, whose nested result again displays `success` as true. This is the displayed conditional submission sequence, not proof of eventual settlement or a later subscription lifecycle effect.
   - Exact locator: callback retry example at lines 20–27; Promise retry example at lines 32–38; callback manual-settlement sequence at lines 44–62; Promise sequence at lines 65–78.
   - Verdict: **PASS**.

## Shared gap sweep and route check

- Both selected evidence files were read completely. Neither promoted source has a `## Related raw API references` section.
- Filename sweep found adjacent Search fields, Search results, Subscription response, Transaction response/navigation, recurring-billing, and other subscription-operation raws. No extra full read was selected: the direct endpoint raws completely answer these four questions. The adjacent pages would be needed for exhaustive operator semantics, legacy iterable behavior, response-field inventory, automatic retry policy/cadence, or actual settlement-state semantics, none of which is established or requested here.
- The external PayPal policy was not read. Its result-limitation notice is retained without legal or field-level interpretation.
- No older snapshot of either exact canonical endpoint appeared in the sweep.
- Reciprocal links resolve from `[[braintree-server-sdk]]` to both promoted sources; each source resolves to its exact path-qualified raw. `[[braintree-index]]` routes to the concept. Direct provider-index source entries remain part of pending aggregate work and are not required for these actual routes.

## One shared completeness check

All four fixed questions include object/action match, direct answer, exact raw locator, and verdict. Each page has one actual route. Full selected evidence reads, filename/related-reference gap sweep, reciprocal-link check, the search policy and damaged-rendering boundaries, and retry example-only amount/result/settlement qualifications are present. Result: **4/4 PASS; no repair or promotion recommendation from this group.**


# Braintree C10 query audit — Group C

- Scope: four of 20 fixed questions; Payment Method Grant + Payment Method Revoke.
- `start_utc`: `2026-09-21T11:38:37Z`
- `analysis_end_utc`: `2026-09-21T11:39:14Z`
- `handoff_utc`: `2026-09-21T11:39:19Z`
- Aggregate company/provider-index/log/count work: pending; not part of this audit.

## Payment Method Grant (Node.js)

Route: [[index]] → [[braintree-index]] → [[braintree-server-sdk]] → [[source-braintree-payment-method-grant-node]] → [[raw/braintree/docs/reference/request/payment-method/grant/node-2026-09-16]].

1. **Navigation question — Where is granting a payment method using Node documented?**
   - Object/action match: Node.js payment-method grant through the Grant API, not payment-method creation, transfer, deletion, or revocation.
   - Direct answer: `[[source-braintree-payment-method-grant-node]]`, backed by `[[raw/braintree/docs/reference/request/payment-method/grant/node-2026-09-16]]`, documents `gateway.paymentMethod.grant()`.
   - Exact locator: raw `# Payment Method: Grant`, lines 13–21, and `### Node`, lines 22–37.
   - Verdict: **PASS**.

2. **Detail question — What availability restriction, participating identities, and scope are explicitly established?**
   - Object/action match: availability and parties/scope of the Node Grant API operation shown on this page.
   - Direct answer: the Grant API is currently in limited release; Braintree directs merchants to contact it to assess fit and request API access, so the page does not establish general availability. The grant gives another Braintree merchant controlled access to one payment method belonging to the granting merchant's customer. The displayed Node example initializes `BraintreeGateway` with `accessTokenForRecipient`, passes `the_payment_method_token`, shows `allow_vaulting: false` and `include_billing_postal_code: true`, and reads `grantResult.paymentMethodNonce.nonce` into `nonceToSendToRecipient`. Those values establish the displayed handoff only; the page does not establish account-wide/customer-wide access, ownership transfer, option defaults, nonce lifetime/reuse, transaction success, authorization, or settlement.
   - Exact locator: limited-release/access notice at lines 17–18; participating merchants, customer, and one-payment-method scope at lines 20–21; recipient access token, token/options, and returned nonce at lines 22–37.
   - Verdict: **PASS**.

## Payment Method Revoke (Node.js)

Route: [[index]] → [[braintree-index]] → [[braintree-server-sdk]] → [[source-braintree-payment-method-revoke-node]] → [[raw/braintree/docs/reference/request/payment-method/revoke/node-2026-09-16]].

3. **Navigation question — Where is revoking a payment-method grant documented?**
   - Object/action match: Node.js revocation of a Grant API payment-method grant, not general `paymentMethod.delete()`.
   - Direct answer: `[[source-braintree-payment-method-revoke-node]]`, backed by `[[raw/braintree/docs/reference/request/payment-method/revoke/node-2026-09-16]]`, documents `gateway.paymentMethod.revoke()`.
   - Exact locator: raw `# Payment Method: Revoke`, lines 13–23, and `### Node`, lines 24–30.
   - Verdict: **PASS**.

4. **Detail question — What access limitation and revocation effect or result guidance does this page state, distinct from deleting a payment method?**
   - Object/action match: limited-release grant revocation, its exact receiving-Vault effect, and only the result guidance present on the revoke page.
   - Direct answer: the same Grant API remains in limited release with contact/request-access guidance, and its surrounding scope is controlled access by another Braintree merchant to one of the granting merchant's customer's payment methods. Revocation deletes the granted version of that payment method from the receiving merchant's Vault. This raw does not say it deletes the granting merchant's original payment method or establish subscription, transaction, nonce, or other cascade effects, so none should be imported from general payment-method deletion. For results, the page links the Payment Method response object and the Node callback exposes `err` and `result`, but it supplies no result fields, success condition, failure behavior, or timing.
   - Exact locator: Payment Method response-object route at line 15; limited-release/access notice at lines 18–19; grant scope at line 21; receiving-Vault deletion effect at line 23; token invocation and callback shape at lines 24–30.
   - Verdict: **PASS**.

## Shared gap sweep and route check

- Both selected evidence files were read completely. Neither promoted source has a `## Related raw API references` section.
- Filename/content sweep found the Grant API report, Grant API webhook reference, general payment-method deletion, OAuth/access-token guides, and webhook overview pages. No extra full read was selected: these four questions are completely answered by the direct Grant and Revoke raws. Adjacent pages would expand into reporting, event notifications, general OAuth policy, or the separate deletion operation's cascade rather than clarify the retained claims.
- The linked Payment Method response object was not read because the question asks what result guidance this page provides; the verified line-15 route and callback shape answer that without importing an unread response schema.
- No older snapshot of either exact canonical endpoint appeared in the sweep.
- Reciprocal links resolve from `[[braintree-server-sdk]]` to both promoted sources; each source resolves to its exact path-qualified raw. `[[braintree-index]]` routes to the concept. Direct provider-index source entries remain pending aggregate work and are not required for these actual routes.

## One shared completeness check

All four fixed questions include object/action match, direct answer, exact raw locator, and verdict. Each page has one actual route. Full selected evidence reads, filename/content gap sweep, reciprocal-link checks, limited-release status, participating-identity scope, receiving-Vault revocation effect, result-navigation boundary, and revocation-versus-deletion distinction are present. Result: **4/4 PASS; no repair or promotion recommendation from this group.**


# Braintree C10 query audit — Group D

- Scope: four of 20 fixed questions; Transaction Webhooks + Account Updater Webhooks.
- `start_utc`: `2026-09-21T11:39:21Z`
- `analysis_end_utc`: `2026-09-21T11:39:58Z`
- `handoff_utc`: `2026-09-21T11:40:45Z`
- Aggregate company/provider-index/log/count work: pending; not part of this audit.

## Transaction Webhooks (Node.js)

Route: [[index]] → [[braintree-index]] → [[braintree-webhooks]] → [[source-braintree-webhooks-transaction-node]] → [[raw/braintree/docs/reference/general/webhooks/transaction/node-2026-09-16]].

1. **Navigation question — Where are Node transaction webhook kinds documented?**
   - Object/action match: Node.js transaction webhook notification kinds, not general transaction lifecycle, transaction lookup, or webhook parsing/setup.
   - Direct answer: `[[source-braintree-webhooks-transaction-node]]`, backed by `[[raw/braintree/docs/reference/general/webhooks/transaction/node-2026-09-16]]`, documents the dedicated Node transaction-webhook kinds.
   - Exact locator: raw `# Transaction`, lines 14–18; `### Notification kinds`, lines 21–39.
   - Verdict: **PASS**.

2. **Detail question — What payment-method availability and event/payload qualifications are stated, and which rendered details remain missing?**
   - Object/action match: payment-method scope, trigger conditions, and payload categories on the dedicated Node transaction-webhook page; no universal transaction or adjacent webhook behavior is imported.
   - Direct answer: the availability line unambiguously names ACH and SEPA Direct Debit requests, but its trailing `Direct Debitandrequests` text is malformed; it does not support reconstructing another payment method, operation, link, qualification, or universal transaction-webhook availability. `transaction_settlement_declined` means settlement for the transaction was declined and may occur after `transaction_settled` if the customer's bank “returns the refund after it has appeared to settle”; that unusual page-specific wording is not generalized into a return, reversal, ordering, or finality rule. `transaction_settled` means the transaction successfully settled. The concatenated Attributes section provides only the categories notification kind, UTC trigger date/time, and an associated Braintree Transaction object; visible attribute names and the object's field inventory are missing.
   - Exact locator: availability and damaged trailing prose at lines 17–18; trigger-role text at lines 21–25; both kinds and their conditions at lines 27–39; concatenated payload categories at lines 42–44.
   - Verdict: **PASS**.

## Account Updater Webhooks (Node.js)

Route: [[index]] → [[braintree-index]] → [[braintree-webhooks]] → [[source-braintree-webhooks-account-updater-node]] → [[raw/braintree/docs/reference/general/webhooks/account-updater/node-2026-09-16]].

3. **Navigation question — Where is the Account Updater notification reference?**
   - Object/action match: Braintree's Node.js Account Updater webhook notification reference, not Account Updater enrollment, update processing, or generic webhook setup.
   - Direct answer: `[[source-braintree-webhooks-account-updater-node]]`, backed by `[[raw/braintree/docs/reference/general/webhooks/account-updater/node-2026-09-16]]`, documents the Account Updater webhook notification kind and attributes route.
   - Exact locator: raw `# Account Updater`, lines 14–18; `### Notification kinds`, lines 23–31; `### Attributes`, lines 34–36.
   - Verdict: **PASS**.

4. **Detail question — Which merchants can receive it, and where are the trigger and payload attributes documented?**
   - Object/action match: feature eligibility, report-level trigger, and payload categories for the Account Updater webhook; not universal merchant access or per-payment-method delivery.
   - Direct answer: only merchants using Braintree's Account Updater feature can receive this webhook; the page does not establish feature enrollment, pricing, configuration, or regional availability. Under **Notification kinds**, `webhook_notification.kind` identifies the trigger and the sole listed value, `account_updater_daily_report`, represents a daily report containing all vaulted payment methods updated in the last 24 hours; when there are no updates, the webhook is not triggered. Under **Attributes**, the damaged concatenated rendering exposes categories rather than visible attribute names: notification kind, UTC trigger time, report-generation date, and an assigned report-download URL whose link expires after one week. It does not establish per-method webhook delivery, report format, download authentication, retries, ordering, or duplicate handling.
   - Exact locator: merchant restriction at lines 17–18; trigger role at lines 23–27; report kind, 24-hour scope, and no-update suppression at lines 29–31; payload categories and one-week expiry at lines 34–36.
   - Verdict: **PASS**.

## Shared gap sweep and route check

- Both selected raws were read completely. Neither promoted source has a `## Related raw API references` section.
- Canonical-path, filename, and exact-claim sweeps found the linked Account Updater guide and many generic transaction/request/response pages, but the two dedicated webhook raws were the only raw matches for their exact notification kinds and stated availability sentences. No extra full read was selected: these exact pages answer all four questions, while the Account Updater guide concerns the feature rather than this notification contract and generic transaction pages do not resolve the damaged webhook rendering. No older snapshot of either exact canonical page was found, and no actual contradiction requiring neighbor evidence was discovered.
- Reciprocal routes resolve from `[[braintree-webhooks]]` to both promoted sources; each source links back to that concept and resolves to its exact path-qualified raw. `[[index]]` routes to `[[braintree-index]]`, and `[[braintree-index]]` routes to the webhook concept. Direct provider-index source entries remain pending aggregate work and are not required for these live concept-led routes.

## One shared completeness check

All four fixed questions include object/action match, direct answer, exact raw locator, and verdict. Each page has one actual route. Full selected-evidence reads, one group gap sweep, reciprocal-link checks, feature/payment-method scope, event conditions, payload-category locators, and both damaged-rendering boundaries are present. Result: **4/4 PASS; no retrieval repair, extra full read, promotion recommendation, contradiction, or unresolved answer.**


# Braintree C10 query audit — Group E (Fraud Protection Webhooks / Address Find)

Scope: `webhooks-fraud-protection-node` and `address-find-node`; exactly four fixed questions from `tracking/ingest/braintree/braintree-campaign-10/selection-review.md`. This is Group E of the single 20-question C10 audit.

Timing (UTC): actual_start `2026-09-21T11:39:59Z`; analysis_end `2026-09-21T11:40:39Z`; handoff `2026-09-21T11:40:43Z`.

## `webhooks-fraud-protection-node`

Actual route: `wiki/index.md` (`## PSP Indexes` → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-webhooks]]`) → `wiki/concepts/braintree-webhooks.md` (`## Sources` → `[[source-braintree-webhooks-fraud-protection-node]]`) → `wiki/sources/braintree/source-braintree-webhooks-fraud-protection-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/general/webhooks/fraud-protection/node-2026-09-16.md`.

1. **Navigation question — Where are Fraud Protection webhook notifications documented?**
   - **Object/action match:** Yes — the route reaches the Node Fraud Protection webhook event reference, not general webhook delivery/parsing, transaction fraud screening, or a fraud-product eligibility guide.
   - **Direct answer:** `[[source-braintree-webhooks-fraud-protection-node]]` routes to the pinned Node reference. Its `Notification kinds` section identifies `webhook_notification.kind` as the trigger discriminator and lists the page's single kind, `transaction_reviewed`.
   - **Exact raw locator:** `# Fraud Protection`, line 14; `### Notification kinds`, lines 17–25, with the event row at line 25.
   - **Verdict:** **PASS**.

2. **Detail question — What event conditions and payload scope does this page establish without inferring universal fraud coverage?**
   - **Object/action match:** Yes — the answer is limited to the page's Fraud Protection Dashboard review event and category-level payload prose; it does not generalize to all transactions, fraud decisions, products, payment methods, or merchants.
   - **Direct answer:** `transaction_reviewed` applies when a transaction cited for Review in the Fraud Protection Dashboard has been accepted or rejected. If rejected, a void or refund of the transaction amount **has been requested**; the page does not establish completion, success, settlement, or finality. The concatenated Attributes line exposes no visible field names but describes the categories: notification kind, reviewed transaction identifier, resulting risk decision, reviewer email, reviewer notes, UTC review time, and UTC webhook-trigger time, then links to a separate Fraud Protection guide. It establishes no universal fraud-screening or webhook eligibility, review automation, delivery timing, retry, ordering, or duplicate behavior.
   - **Exact raw locator:** trigger and requested void/refund qualification at the `transaction_reviewed` table row, line 25; category-only payload prose and further-guide route at `### Attributes`, lines 28–30.
   - **Verdict:** **PASS**.

## `address-find-node`

Actual route: `wiki/index.md` (`## PSP Indexes` → `[[braintree-index]]`) → `wiki/braintree-index.md` (`## Concepts` → `[[braintree-server-sdk]]`) → `wiki/concepts/braintree-server-sdk.md` (`## Related` → `[[source-braintree-address-find-node]]`) → `wiki/sources/braintree/source-braintree-address-find-node.md` (`## Raw Sources`) → `raw/braintree/docs/reference/request/address/find/node-2026-09-16.md`.

3. **Navigation question — Where is Node lookup of a customer address documented?**
   - **Object/action match:** Yes — the route reaches Node `Address: Find` for one customer address, not address creation/update/deletion, customer lookup, or an address-only search.
   - **Direct answer:** `[[source-braintree-address-find-node]]` routes to the pinned Node request reference, whose example invokes `gateway.address.find("aCustomerId", "anAddressId", callback)`.
   - **Exact raw locator:** `# Address: Find`, line 13; `### Node`, lines 16–20, with the lookup at lines 18–19.
   - **Verdict:** **PASS**.

4. **Detail question — What identifiers and callback arguments are shown, and what response details are not supplied by this page?**
   - **Object/action match:** Yes — the identifiers and callback belong to the direct Node address-find operation; response-object and exception links remain separate navigation rather than imported evidence.
   - **Direct answer:** The example passes customer ID first (`"aCustomerId"`) and address ID second (`"anAddressId"`), then exposes callback arguments `(err, address)`. The page does not display fields on `address`, a success flag, a Promise form, uniqueness rules, or any other response shape; it links to a separate Address response-object reference. If either the address or customer cannot be found, it routes to the same linked `notFoundError` and does not define distinct outcomes or error fields.
   - **Exact raw locator:** separate Address response-object route at line 15; identifiers and callback arguments at lines 16–20; shared address-or-customer not-found route at line 21.
   - **Verdict:** **PASS**.

## Shared gap sweep and completeness check

- Both selected raws were read completely. Filename and exact-claim sweeps surfaced broader Fraud Protection/Premium Fraud Management Tools guides, general exceptions, the Address response object, adjacent address create/update/delete operations, and unrelated client-token/transaction pages containing similar example identifiers. No extra raw was selected: the exact event and lookup raws directly answer all four fixed questions; the Fraud Protection guide, Address response object and exceptions page remain navigation-only because no requested answer is missing or conflicted. No historical raw was needed.
- Reciprocal routes: **PASS** — both root → provider-index → concept → source → exact raw routes resolve; each concept contains its audited source exactly once; each source links back to its main concept and contains one exact path-qualified raw link. `wiki/braintree-index.md` also contains one direct catalog entry for each source.
- Raw identity: **PASS 2/2** — source `canonical_url`, `raw_files`, Raw Sources link, raw Source URL, manifest identity and computed SHA-256 agree for Fraud Protection (`563ae85f2b8e23f9639ca098b75b32a587fa76f6c54b7cc8f5ef870ac775a0eb`) and Address Find (`56498cb401e04c9f336bc9be9af2748bd3e8d96e5bc45a69175dd7f8ce65055a`).
- Completeness: **PASS** — 2 routes; exactly 4/4 predetermined questions; 4/4 object/action matches, direct answers, exact locators and PASS verdicts; no retrieval repair, extra full read, promotion recommendation, contradiction, or unresolved answer.

**Group verdict: PASS (4/4).**
