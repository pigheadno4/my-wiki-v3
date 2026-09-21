# Braintree C13 close audit

Result: PASS.10/10 sources promoted;20/20 fixed queries passed.
First-pass worker format10/10; first content approval9/10.10 full initial
reviews plus1 targeted correction review; zero full retry reviews.

## Mechanical close

All10 approved candidate/receipt pairs, raw SHA-256/canonical URL/primary
quotes, unique primary owners, full supporting-evidence paths, approved
concept snippets, required/reciprocal links, duplicate-free new catalogs and
counts passed.101 sources=85 website+16 GitHub, excluding changelogs.
Generic typed-page validation passed15 files; git diff whitespace check passed.

Two bounded coordinator repairs: exact independently reviewed reciprocal
conflict warning on existing ordinary-settlement source; one mechanical
Line Item warning substitution from `Do not fill in the missing words` to
`Do not reconstruct the missing words` to avoid placeholder-regex false
positive. Candidate/receipt remain unchanged; equality check permits only
this exact recorded substitution. No code/rule/validator changes, no default
third coordinator full read, no additional three-page audit or unit suite.

Partial Settlement primary and ordinary Settlement supporting raw differ on
payment-method availability. Both source routes preserve the unresolved
conflict. Supporting raw is factual evidence, not a second primary source
owner; primary reverse ownership remains unique. The exact reviewed warning
is saved in attempts/transaction-submit-for-partial-settlement-node/attempt-2/
reciprocal-warning.md and approved in that attempt's review reason.

## Fixed query evidence

# C13 query audit — Group A

- Scope: the four fixed Group A questions from `selection-review.md` (4 of 20 campaign questions).
- Start UTC: `2026-09-21T13:27:49Z`
- Analysis end UTC: `2026-09-21T13:28:45Z`
- Handoff UTC: `2026-09-21T13:29:20Z`
- Aggregate note: campaign aggregate files remain pending; both promoted concept-to-source routes are live.

## Route: Subscription Create

`wiki/index.md:11` → `wiki/braintree-index.md:134` → `wiki/concepts/braintree-server-sdk.md:41` → `wiki/sources/braintree/source-braintree-subscription-create-node.md:51-53` → `raw/braintree/docs/reference/request/subscription/create/node-2026-09-16.md`

### 1. Where is Node Subscription Create documented?

- Object/action match: Braintree Node.js creation of a subscription through `gateway.subscription.create()`.
- Direct answer: It is documented in the Node.js **Subscription: Create** request reference, reached through the Braintree Server SDK concept and the promoted Subscription Create source.
- Exact locator: raw `# Subscription: Create`, lines 13-39; source raw backlink at lines 51-53.
- Verdict: **PASS**

### 2. What payment-method prerequisites, creation scope and consequential qualifications are stated, and where are input details routed?

- Object/action match: payment-method conditions and creation-time behavior, not later subscription updates.
- Direct answer: The page says the payment method must be vaulted before association with a subscription and permits a token or, under certain conditions, a nonce; if 3DS must apply to the first transaction, creation must use a 3DS-enriched nonce because tokens do not carry 3DS data. Creation can select a merchant account, override plan add-ons/discounts, trial details, start date and descriptors. The selected merchant account must match the plan currency; an add-on or discount can be added only once (use `quantity` for repeated application); and `first_billing_date`, `billing_day_of_month`, and `start_immediately` are mutually exclusive. Exact input shapes remain routed to the raw sections rather than treated as a complete schema.
- Exact locator: raw prerequisite and 3DS scope at lines 17-19 and 39, with nonce calls at lines 72-93; merchant-account currency at lines 43-70; plan modifications and single-add rule at lines 95-307; trials at lines 310-343; start-date choices and validation warning at lines 346-408; descriptors at lines 410-449.
- Verdict: **PASS**

## Route: Subscription Update

`wiki/index.md:11` → `wiki/braintree-index.md:134` → `wiki/concepts/braintree-server-sdk.md:43` → `wiki/sources/braintree/source-braintree-subscription-update-node.md:45-47` → `raw/braintree/docs/reference/request/subscription/update/node-2026-09-16.md`

### 3. Where is Node Subscription Update documented?

- Object/action match: Braintree Node.js update of an existing subscription through `gateway.subscription.update()`.
- Direct answer: It is documented in the Node.js **Subscription: Update** request reference, reached through the Braintree Server SDK concept and the promoted Subscription Update source.
- Exact locator: raw `# Subscription: Update`, lines 13-39; source raw backlink at lines 45-47.
- Verdict: **PASS**

### 4. What update scope and material billing or payment-method qualifications are stated without importing creation behavior?

- Object/action match: changes to an existing subscription, with update-specific payment-method and add-on/discount qualifications.
- Direct answer: The examples update an existing subscription identifier with illustrative subscription fields and route a missing subscription to `notFoundError`. Updates can add, update or remove add-ons and discounts, including multiple changes at once; an item can be added only once, with `quantity` used to apply it several times. If 3DS must apply to the existing subscription's **next transaction**, the update must use a 3DS-enriched nonce; this is not a requirement for every update. `replaceAllAddOnsAndDiscounts` removes all existing add-ons and discounts. The page does not establish creation prerequisites, proration, immediate charging or when an update affects billing, so none is imported.
- Exact locator: raw invocation and not-found route at lines 13-39; add/update/remove and single-add rule at lines 43-127; qualified next-transaction 3DS nonce at lines 129-148; multiple changes at lines 150-215; inheritance/override route at lines 217-273; remove-all option at lines 275-296.
- Verdict: **PASS**

## Shared route and gap checks

- Both routes resolve through the actual root index, Braintree provider index, Braintree Server SDK concept, promoted source and source-owned raw backlink. The supporting `recurring-payments` concept also has reciprocal links, but was not needed as a second route.
- The filename/content sweep found the exact create and update raws plus response, guide, search, find, cancel, retry and webhook pages. Related response, exception, validation, 3DS and management/creation guides were navigation-only because the selected raws directly answer the fixed questions; no adjacent authority or creation/update behavior was imported.
- Create and update remain distinct: first-transaction 3DS creation scope is not substituted for the update page's next-transaction condition, and update examples do not establish creation prerequisites or billing outcomes.

## Completeness

All four fixed questions contain one route/page context, object/action match, direct answer, exact locator and verdict. Result: **4/4 PASS**. No repair or additional promotion is required from this audit.

# C13 query audit — Group B

- Scope: the four fixed Group B questions from `selection-review.md` (4 of 20 campaign questions).
- Start UTC: `2026-09-21T13:38:18Z`
- Analysis end UTC: `2026-09-21T13:40:22Z`
- Handoff UTC: `2026-09-21T13:41:05Z`
- Aggregate note: campaign aggregate files remain pending; both promoted concept-to-source routes are live.

## Route: Transaction Search

`wiki/index.md:11` → `wiki/braintree-index.md:134` → `wiki/concepts/braintree-server-sdk.md:49` → `wiki/sources/braintree/source-braintree-transaction-search-node.md:47-49` → `raw/braintree/docs/reference/request/transaction/search/node-2026-09-16.md`

### 1. Where is Node Transaction Search documented?

- Object/action match: Braintree Node.js search of the Transaction collection through `gateway.transaction.search()`, not single-transaction lookup or reporting.
- Direct answer: It is documented in the Node.js **Transaction: Search** request reference, reached through the Braintree Server SDK concept and the promoted Transaction Search source.
- Exact locator: raw `# Transaction: Search`, lines 13-29; source raw backlink at lines 47-49.
- Verdict: **PASS**

### 2. How are transaction criteria and result consumption documented, including policy limits and scope qualifications?

- Object/action match: transaction-search criteria, callback collection consumption, and search-specific qualifications.
- Direct answer: The opening example applies a customer-ID criterion and consumes returned Transaction objects with callback `response.each()`. The page provides grouped criterion examples and routes operator semantics to the separate Search fields authority rather than claiming an exhaustive schema. It preserves a policy-based results-limit notice without inventing a number. Credits include refunds and standalone credits unless the additional refund criterion narrows them. Status-change and dispute-date criteria are date/time searches; supplied time zones are respected, omission defaults to the gateway-account time zone, and returned time values are UTC.
- Exact locator: raw limitation and operator routes at lines 16-19; search call and `response.each()` at lines 20-29; grouped criteria at lines 31-221; credit/refund scope at lines 223-254; amount and status-change criteria at lines 256-316; dispute-date and timezone qualifications at lines 318-332.
- Verdict: **PASS**

## Route: Transaction Submit For Partial Settlement

`wiki/index.md:11` → `wiki/braintree-index.md:134` → `wiki/concepts/braintree-server-sdk.md:41` → `wiki/sources/braintree/source-braintree-transaction-submit-for-partial-settlement-node.md:45-48` → `raw/braintree/docs/reference/request/transaction/submit-for-partial-settlement/node-2026-09-16.md`

### 3. Where is Node Transaction Submit For Partial Settlement documented?

- Object/action match: Braintree Node.js creation of multiple partial settlements against one parent authorization through `gateway.transaction.submitForPartialSettlement()`, not ordinary settlement submission.
- Direct answer: It is documented in the Node.js **Transaction: Submit For Partial Settlement** request reference, reached through the Braintree Server SDK concept and the promoted Partial Settlement source.
- Exact locator: raw `# Transaction: Submit For Partial Settlement`, lines 13-25, with callback and Promise calls at lines 30-63; source primary-raw backlink at lines 45-47.
- Verdict: **PASS**

### 4. What payment-method availability, parent/child settlement behavior and consequential restrictions are documented?

- Object/action match: multiple partial settlement availability, parent/child behavior and resulting restrictions; it does not collapse this operation into ordinary settlement.
- Direct answer: The primary page says multiple partial settlements are only for PayPal and Venmo, while the fully read ordinary Submit For Settlement page additionally says some credit-card transactions for select merchants are eligible. The sources therefore preserve an unresolved availability conflict and direct readers to verify current payment-method and merchant eligibility with Braintree; they do not synthesize a universal rule. The workflow keeps the order authorization as the parent, prohibits ordinary settlement submission of that parent, and makes one partial-settlement call per portion; each creates a child with the original details and specified amount. The collected lifecycle/status text is damaged, so missing states are not reconstructed, though the page says no further settlements are possible after the unidentified later transition. Refunds are child-only, capped at the amount settled on that child, and require full settlement, but the required state name is missing.
- Exact locator: primary raw availability and procedure at lines 15-25; child creation and damaged lifecycle/no-further-settlement section at lines 65-76; refund restrictions at lines 79-84; parent/child Control Panel links at lines 87-91. Conflicting supporting authority: ordinary Submit For Settlement raw, `## Examples > ### Specifying settlement amount`, line 32. Reciprocal unresolved-conflict warnings: Partial Settlement source lines 25-26 and ordinary Submit For Settlement source lines 24-25.
- Verdict: **PASS**

## Shared route and gap checks

- Both routes resolve through the actual root index, Braintree provider index, Braintree Server SDK concept, promoted source and source-owned raw backlink. The Partial Settlement source separately identifies the fully read ordinary-settlement raw as supporting conflict evidence rather than primary ownership.
- Full evidence read: Transaction Search raw SHA-256 `2af4c7f62a0dd0463beff6d1ffa40d0ea4572f45a70da3e26201f944b4905612`; primary Partial Settlement raw `ee0e96a52e0f5b846c2aedb3bdcd9104abaddcf7ebc9b5472aa789da8e10de41`; supporting ordinary Submit For Settlement raw `83ed4cc7250f0a35cb0a3879b1d2c1d05d12f2d263f051ff7a4156ac69f13d98`.
- The filename/content sweep found the exact selected raws, the separate Search fields/results references, two payment-method-specific partial-settlement guides, and adjacent reporting examples. The selected Search raw directly answers the fixed questions and routes general operator/result details; the primary plus supporting settlement raws directly expose the availability conflict. No adjacent guide was needed as additional factual authority.
- Reciprocal conflict disclosure is live on both promoted settlement sources. The audit preserves the primary PayPal/Venmo statement, the supporting select-merchant credit-card statement, and unresolved eligibility without choosing between them.

## Completeness

All four fixed questions contain one route/page context, object/action match, direct answer, exact locator and verdict. Result: **4/4 PASS**. No repair or additional promotion is required from this audit.

# C13 query audit — Group C

- Scope: the four fixed Group C questions from `selection-review.md` (4 of 20 campaign questions).
- Start UTC: `2026-09-21T13:35:03Z`
- Analysis end UTC: `2026-09-21T13:35:10Z`
- Handoff UTC: `2026-09-21T13:35:43Z`
- Aggregate note: campaign aggregate files remain pending; both promoted concept-to-source routes are live.

## Route: Transaction Adjust Authorization

`wiki/index.md:11` → `wiki/braintree-index.md:134` → `wiki/concepts/braintree-server-sdk.md:43` → `wiki/sources/braintree/source-braintree-transaction-adjust-authorization-node.md:40-42` → `raw/braintree/docs/reference/request/transaction/adjust-authorization/node-2026-09-16.md`

### 1. Where is Node Transaction Adjust Authorization documented?

- Object/action match: Braintree Node.js adjustment of an existing transaction's authorized amount through `gateway.transaction.adjustAuthorization()`.
- Direct answer: It is documented in the Node.js **Transaction: Adjust Authorization** request reference, reached through the Braintree Server SDK concept and the promoted Adjust Authorization source.
- Exact locator: raw `# Transaction: Adjust Authorization`, lines 13-25, with the Node call at lines 26-40; source raw backlink at lines 40-42.
- Verdict: **PASS**

### 2. What authorization-adjustment scope, availability and fee qualifications are documented, distinct from capture?

- Object/action match: authorization-amount adjustment eligibility and effects, not capture or settlement submission.
- Direct answer: The page limits adjustment to transactions in `authorized` status and requires the transaction ID and amount. A lower new amount causes an **attempted** partial reversal of the difference to the cardholder; a higher amount causes an **attempted** incremental authorization. It does not state broader payment-method, merchant or processor availability. The fee note says authorization and capture **can** incur merchant fees in some markets and points to the Braintree User Agreement; it does not specify markets or guarantee a fee for every adjustment. The operation changes authorized amount and is not documented as capture, settlement submission or a transaction-status transition.
- Exact locator: raw fee qualification at lines 16-17; post-creation purpose, `authorized` status and required inputs at lines 21-23; partial-reversal and incremental-authorization attempt wording at line 25; callback result handling at lines 26-40.
- Verdict: **PASS**

## Route: Transaction Clone

`wiki/index.md:11` → `wiki/braintree-index.md:134` → `wiki/concepts/braintree-server-sdk.md:41` → `wiki/sources/braintree/source-braintree-transaction-clone-transaction-node.md:47-49` → `raw/braintree/docs/reference/request/transaction/clone_transaction/node-2026-09-16.md`

### 3. Where is Node Transaction Clone documented?

- Object/action match: Braintree Node.js creation of a new transaction through `gateway.transaction.cloneTransaction()`.
- Direct answer: It is documented in the Node.js **Transaction: Clone Transaction** request reference, reached through the Braintree Server SDK concept and the promoted Clone Transaction source.
- Exact locator: raw `# Transaction: Clone Transaction`, lines 13-20, with callback and Promise calls at lines 23-51; source raw backlink at lines 47-49.
- Verdict: **PASS**

### 4. What is copied into a new transaction, what inputs or restrictions matter, and what alternative is recommended?

- Object/action match: clone-created new transaction, copied scope, required inputs, failure route and recommended alternative.
- Direct answer: Cloning creates a **new** transaction and copies all attributes of the original except `amount`; the page does not enumerate those attributes. It requires an amount and an option flag to submit the new transaction for settlement. The examples also pass the original transaction ID and show `options.submitForSettlement: true`; if the original transaction cannot be found, the page routes to `notFoundError`. Braintree recommends saving and reusing payment-method or customer information in the Vault instead of cloning in most cases, as a recommendation rather than a prohibition.
- Exact locator: raw new-transaction/copied-scope and Vault recommendation at lines 15-18; required amount and settlement option at lines 19-20; callback and Promise examples at lines 23-51; not-found route at line 52.
- Verdict: **PASS**

## Shared route and gap checks

- Both routes resolve through the actual root index, Braintree provider index, Braintree Server SDK concept, promoted source and source-owned raw backlink.
- The filename/content sweep found the two exact Node request raws, the distinct submit-for-settlement raw and a Control Panel cloning article. Related transaction-response, status, Vault/payment-method, customer and exception references are navigation-only; the selected raws directly answer the fixed questions, so no adjacent factual authority was imported.
- Attempt modality, the some-market fee qualification, clone-created new-transaction scope and the distinction between authorization adjustment, capture and settlement submission remain explicit.

## Completeness

All four fixed questions contain one route/page context, object/action match, direct answer, exact locator and verdict. Result: **4/4 PASS**. No repair or additional promotion is required from this audit.

# C13 query audit — Group D

- Scope: the four fixed Group D questions from `selection-review.md` (4 of 20 campaign questions).
- Start UTC: `2026-09-21T13:41:48Z`
- Analysis end UTC: `2026-09-21T13:42:13Z`
- Handoff UTC: `2026-09-21T13:42:48Z`
- Aggregate note: campaign aggregate files remain pending; both promoted concept-to-source routes are live.

## Route: Transaction Hold In Escrow

`wiki/index.md:11` → `wiki/braintree-index.md:134` → `wiki/concepts/braintree-server-sdk.md:47` → `wiki/sources/braintree/source-braintree-transaction-hold-in-escrow-node.md:46-48` → `raw/braintree/docs/reference/request/transaction/hold-in-escrow/node-2026-09-16.md`

### 1. Where is Node Transaction Hold In Escrow documented?

- Object/action match: Braintree Node.js placement of an eligible transaction into escrow through `gateway.transaction.holdInEscrow()`, not escrow release or cancellation.
- Direct answer: It is documented in the Node.js **Transaction: Hold In Escrow** request reference, reached through the Braintree Server SDK concept and the promoted Hold In Escrow source.
- Exact locator: raw `# Transaction: Hold In Escrow`, lines 13-29; source raw backlink at lines 46-48.
- Verdict: **PASS**

### 2. What Marketplace qualification, invocation and result guidance is shown without inventing lifecycle details?

- Object/action match: hold invocation and prerequisites for a Braintree Marketplace transaction, bounded by the displayed empty result handlers.
- Direct answer: The page makes the functionality specific to Braintree Marketplace merchants. Both callback and Promise forms pass a transaction ID to `holdInEscrow()`, but their handlers are empty; they establish the invocation shape only, not success, a returned property, a resulting status, release, settlement, disbursement or timing. The transaction must have status `authorized` or `submitted_for_settlement`; the page does not establish how it reached either state or what later lifecycle transition occurs. A missing transaction is routed to `notFoundError`.
- Exact locator: raw Marketplace qualification at line 17; callback and Promise calls with empty handlers at lines 18-26; missing-transaction route and the two eligible statuses at lines 27-29.
- Verdict: **PASS**

## Route: Transaction Release From Escrow

`wiki/index.md:11` → `wiki/braintree-index.md:134` → `wiki/concepts/braintree-server-sdk.md:43` → `wiki/sources/braintree/source-braintree-transaction-release-from-escrow-node.md:46-48` → `raw/braintree/docs/reference/request/transaction/release-from-escrow/node-2026-09-16.md`

### 3. Where is Node Transaction Release From Escrow documented?

- Object/action match: Braintree Node.js release of funds from an eligible Marketplace transaction's escrow through `gateway.transaction.releaseFromEscrow()`, not holding funds or cancelling a release.
- Direct answer: It is documented in the Node.js **Transaction: Release From Escrow** request reference, reached through the Braintree Server SDK concept and the promoted Release From Escrow source.
- Exact locator: raw `# Transaction: Release From Escrow`, lines 13-34; source raw backlink at lines 46-48.
- Verdict: **PASS**

### 4. What Marketplace qualification and release invocation are shown, distinct from holding or cancelling release?

- Object/action match: release invocation, prerequisite, distribution and timing for a Braintree Marketplace transaction, kept distinct from hold and cancel-release operations.
- Direct answer: The page makes the functionality specific to Braintree Marketplace merchants and calls `releaseFromEscrow()` with a transaction ID in callback and Promise forms. The handlers are empty, so they do not establish success, a result shape or a resulting escrow status. The transaction's `escrow_status` must already be `held`. After a release request, Braintree says the service fee less processing fees is disbursed to the master merchant account and the remaining funds to the sub-merchant on the following business day. The page does not document how funds were held or how release cancellation works; those are separate operations. A missing transaction is routed to `notFoundError`.
- Exact locator: raw Marketplace qualification at line 17; release calls and empty handlers at lines 18-29; missing-transaction route at line 30; master/sub-merchant distribution and next-business-day timing at line 32; required `held` escrow status at line 34.
- Verdict: **PASS**

## Shared route and gap checks

- Both routes resolve through the actual root index, Braintree provider index, Braintree Server SDK concept, promoted source and source-owned raw backlink.
- Full selected evidence read: Hold In Escrow raw SHA-256 `e9f4ae0fb60c83a3596ee5bf7a85c0b2bb932f2a221fd28ac720b81bab0ad41d`; Release From Escrow raw `0a13b6d9849cd891bdfa8fda382ee92aea193a5e26ba40ccc3385ff295dd12c6`.
- The filename/content sweep found the exact selected raws plus the distinct Cancel Release page, Marketplace sale-time hold option and transaction-find escrow-status route. Those adjacent pages were navigation-only because the selected raws directly answer the fixed questions; no facts from another operation were imported.
- Marketplace scope, hold-state prerequisites, release timing and distribution remain operation-specific. Empty callback/Promise handlers are treated only as invocation evidence, not completed lifecycle proof.

## Completeness

All four fixed questions contain one route/page context, object/action match, direct answer, exact locator and verdict. Result: **4/4 PASS**. No repair or additional promotion is required from this audit.

# C13 query audit — Group E

- Scope: the four fixed Group E questions from `selection-review.md` (4 of 20 campaign questions).
- Start UTC: `2026-09-21T13:42:35Z`
- Analysis end UTC: `2026-09-21T13:42:49Z`
- Handoff UTC: `2026-09-21T13:43:19Z`
- Aggregate note: campaign aggregate files remain pending; both promoted concept-to-source routes are live.

## Route: Transaction Cancel Release

`wiki/index.md:11` → `wiki/braintree-index.md:134` → `wiki/concepts/braintree-server-sdk.md:43` → `wiki/sources/braintree/source-braintree-transaction-cancel-release-node.md:50-52` → `raw/braintree/docs/reference/request/transaction/cancel-release/node-2026-09-16.md`

### 1. Where is Node Transaction Cancel Release documented?

- Object/action match: Braintree Node.js cancellation of a previously requested Marketplace escrow release through `gateway.transaction.cancelRelease()`.
- Direct answer: It is documented in the Node.js **Transaction: Cancel Release** request reference, reached through the Braintree Server SDK concept and the promoted Cancel Release source.
- Exact locator: raw `# Transaction: Cancel Release`, lines 13-17, with callback and Promise invocations at lines 18-31; source raw backlink at lines 50-52.
- Verdict: **PASS**

### 2. What Marketplace qualification and cancellation invocation are shown, without equating cancellation with a refund?

- Object/action match: cancel-release eligibility and invocation, not transaction refund or cancellation.
- Direct answer: The functionality is specific to Braintree Marketplace merchants. Callback and Promise examples pass a transaction ID to `gateway.transaction.cancelRelease()` and show only generic result handling; a missing transaction routes to `notFoundError`. Eligibility requires an escrowed Marketplace transaction whose release was previously requested and whose `escrow_status` is still `release_pending`. The page does not state a refund, transaction cancellation, buyer-funds effect, resulting escrow status or completed downstream outcome.
- Exact locator: raw Marketplace qualification at line 17; callback and Promise calls at lines 18-31; not-found route and prior-release plus `release_pending` conditions at lines 32-34.
- Verdict: **PASS**

## Route: Transaction Line Item Find All

`wiki/index.md:11` → `wiki/braintree-index.md:134` → `wiki/concepts/braintree-server-sdk.md:41` → `wiki/sources/braintree/source-braintree-transaction-line-item-find-all-node.md:43-45` → `raw/braintree/docs/reference/request/transaction-line-item/find-all/node-2026-09-16.md`

### 3. Where is Node Transaction Line Item Find All documented?

- Object/action match: Braintree Node.js retrieval of a transaction's line-item collection through `gateway.transactionLineItem.findAll()`.
- Direct answer: It is documented in the Node.js **Transaction Line Item: Find All** request reference, reached through the Braintree Server SDK concept and the promoted Line Item Find All source.
- Exact locator: raw `# Transaction Line Item: Find All`, lines 13-21, with callback and Promise calls at lines 22-38; source raw backlink at lines 43-45.
- Verdict: **PASS**

### 4. What collection and result guidance, policy notice and missing-rendering limitations are documented?

- Object/action match: transaction-ID collection retrieval, displayed result variables, policy limitation and damaged prose boundary.
- Direct answer: The page states that the operation returns a collection of Transaction Line Item objects and links their details to a separate response reference. The callback passes `theTransactionId` and receives `transactionLineItems`; the Promise passes the same displayed ID and resolves `transactionLineItems`. Empty handlers do not establish fields, ordering, count, pagination, completeness or failure behavior. The page preserves a notice that results are limited according to the linked PayPal Data Protection Addendum for Card Processing Products, without interpreting that unread policy. Its sentence before the examples is incomplete—`To retrieve a list of transaction line items that were provided when a transaction was created with, use.`—so the missing qualifier and method text are not reconstructed; the code independently establishes `findAll()`.
- Exact locator: raw policy notice at lines 16-17; collection/response route at line 19; damaged sentence at line 21; callback at lines 22-30; Promise at lines 32-38.
- Verdict: **PASS**

## Shared route and gap checks

- Both routes resolve through the actual root index, Braintree provider index, Braintree Server SDK concept, promoted source and source-owned raw backlink.
- The filename/content sweep found the exact cancel-release and transaction-line-item Find All raws plus the separate Transaction Line Item response reference. Cancel Release also exposes response, Marketplace, status and exception navigation. The selected raws directly answer the fixed questions, so those adjacent pages and the external policy were not read as factual authority.
- Marketplace and `release_pending` scope, the non-refund boundary, the policy notice and the damaged Line Item prose remain explicit; no missing schema or lifecycle behavior was reconstructed.

## Completeness

All four fixed questions contain one route/page context, object/action match, direct answer, exact locator and verdict. Result: **4/4 PASS**. No repair or additional promotion is required from this audit.
