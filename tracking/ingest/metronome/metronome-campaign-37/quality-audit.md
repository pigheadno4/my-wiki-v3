# Campaign 37 single retrieval audit

Date: 2026-09-07

Scope: the ten predetermined retrieval tasks in `selection-review.md`; query navigation and evidence evaluation only.
Method: each route began at `wiki/index.md`, followed `[[metronome-index]]`, then a provider concept reciprocal link, then the source page and its actual path-qualified `## Raw Sources` link. No manifest path was used as a retrieval shortcut. All five linked raw snapshots were read completely (236, 839, 208, 389, and 317 lines respectively). A bounded filename/topic sweep required by the query workflow surfaced only related or older raw pages; none was needed to answer these ten questions, so no supplemental raw was read.

## Verdict

**PASS — 10/10 tasks passed; 0 retrieval misses; 0 answer-seeking extra searches beyond the intended routes.** The source routes were sufficient for every answer. The central consequential-warning test passed: the Archive a credit route makes the finalized-invoice prerequisite and correction sequence visible before schema detail.

## Results

### 1. Get a rate card — navigation question — PASS

- **Starting route:** `wiki/index.md:9` -> `[[metronome-index]]` -> `wiki/metronome-index.md:239` `[[metronome-products-and-rate-cards]]` -> `wiki/concepts/metronome/metronome-products-and-rate-cards.md:148` `[[source-metronome-api-reference-rate-cards-get-a-rate-card]]` -> source `## Raw Sources` link at `wiki/sources/metronome/source-metronome-api-reference-rate-cards-get-a-rate-card.md:38`.
- **Answer:** Inspect the card's identifying and creation metadata, description, fiat credit type/conversions, aliases, and custom fields through **Get a rate card** (`POST /v1/contract-pricing/rate-cards/get`). If rates are needed, follow the page's dedicated `getRates` or `getRateSchedule` routes; those are navigation-only here, not evidence read for this question.
- **Evidence:** source overview/boundary at `wiki/sources/metronome/source-metronome-api-reference-rate-cards-get-a-rate-card.md:14-21`; raw purpose and no-rates warning at `raw/metronome/api-reference/rate-cards/get-a-rate-card-2026-07-13.md:9-11` and operation description at lines 88-97.
- **Extra search:** none; the reciprocal concept link and source raw link were sufficient.

### 2. Get a rate card — detail question — PASS

- **Starting route:** same concept -> source -> raw route as task 1.
- **Answer:** The JSON request identifier is `id`; `components.schemas.Id` requires it and formats it as a UUID. The response carries aliases at `data.aliases`, an array of `RateCardAlias`; every alias requires `name`, with optional `starting_at` and `ending_before` timestamps.
- **Evidence:** request and `id` schema at `raw/metronome/api-reference/rate-cards/get-a-rate-card-2026-07-13.md:99-106,137-144`; response example at lines 107-132; `RateCard.aliases` and `RateCardAlias` at lines 145-174 and 199-211.
- **Extra search:** none; the source's request/alias schema locators led directly to the answer.

### 3. List credits — navigation question — PASS

- **Starting route:** `wiki/index.md:9` -> `[[metronome-index]]` -> `wiki/metronome-index.md:236` `[[metronome-credits-and-commits]]` -> `wiki/concepts/metronome/metronome-credits-and-commits.md:265` `[[source-metronome-api-reference-credits-and-commits-list-credits]]` -> source `## Raw Sources` link at `wiki/sources/metronome/source-metronome-api-reference-credits-and-commits-list-credits.md:48`.
- **Answer:** Use **List credits** (`POST /v1/contracts/customerCredits/list`) to inspect promotional and contract-specific customer credits, access schedules, applicability, optional ledgers, and calculated balances. Ledger documentation is routed from the source to `components.schemas.Credit.ledger`, the `CreditLedger` union, and its referenced entry schemas in raw.
- **Evidence:** source purpose and ledger route at `wiki/sources/metronome/source-metronome-api-reference-credits-and-commits-list-credits.md:14-23,33-39`; raw purpose at `raw/metronome/api-reference/credits-and-commits/list-credits-2026-08-28.md:9-28`; ledger field/union at lines 404-410 and 531-546.
- **Extra search:** none; the main concept exposed the source and its raw schema map.

### 4. List credits — detail question — PASS

- **Starting route:** same concept -> source -> raw route as task 3.
- **Answer:** In a supplied JSON object, `customer_id` is required. Set `include_ledgers: true` to include each credit's ordered balance-impacting events; `credit_id` narrows to one credit, while date, contract, archive, cursor, and limit fields scope the returned credit set rather than defining a separate ledger time window. `include_balance` is a separate, potentially slower current-balance calculation. `include_ledgers` may also slow the query. `limit` is 1-25 and defaults to 25, with `next_page` for continuation. The page mistakenly says “commits” in the limit and `credit_id` prose, but the operation, path, response items, and schema are credits; no commit-list conclusion is supported.
- **Evidence:** exact request controls and performance note at `raw/metronome/api-reference/credits-and-commits/list-credits-2026-08-28.md:185-248`; success `Credit[]` plus nullable cursor at lines 249-266; ordered-event definition and union at lines 404-410 and 531-546; wording cautions at lines 30-42. Source preserves the same qualification at `wiki/sources/metronome/source-metronome-api-reference-credits-and-commits-list-credits.md:20-28`.
- **Extra search:** none; the routed request schema and ledger union answered the question.

### 5. Archive a credit — navigation question — PASS

- **Starting route:** `wiki/index.md:9` -> `[[metronome-index]]` -> `wiki/metronome-index.md:236` `[[metronome-credits-and-commits]]` -> `wiki/concepts/metronome/metronome-credits-and-commits.md:263` `[[source-metronome-api-reference-credits-and-commits-archive-a-credit]]` -> source `## Raw Sources` link at `wiki/sources/metronome/source-metronome-api-reference-credits-and-commits-archive-a-credit.md:38`.
- **Answer:** The source is the route for deactivating either a contract-level or customer-level credit with `POST /v2/contracts/credits/archive` while preserving its history. Its prerequisite is prominent: every finalized invoice to which the credit was applied must first be voided.
- **Evidence:** source purpose and warning at `wiki/sources/metronome/source-metronome-api-reference-credits-and-commits-archive-a-credit.md:14-21`; raw purpose/prerequisite at `raw/metronome/api-reference/credits-and-commits/archive-a-credit-2026-07-13.md:9-17`.
- **Extra search:** none; the concept summary exposed the prerequisite before entering raw.

### 6. Archive a credit — detail question — PASS

- **Starting route:** same concept -> source -> raw route as task 5.
- **Answer:** Void all finalized invoices that used the credit, archive the credit, then regenerate the voided invoice so it is recalculated without the credit. Archival deactivates the **entire** access schedule; it is not a partial grant reduction. The archived credit disappears by default from `listCustomerCredits` and `listCustomerBalances` but can be requested with `include_archived`; it then has a null ledger and zero remaining balance.
- **Evidence:** correction sequence at `raw/metronome/api-reference/credits-and-commits/archive-a-credit-2026-07-13.md:11-17` (repeated in the OpenAPI description at lines 103-122); visibility, null-ledger/zero-balance, and full-schedule effect at lines 19-22 and 125-137.
- **Extra search:** none; the consequential behavior is directly available in both the source warning and linked raw.

### 7. Hybrid business models — navigation question — PASS

- **Starting route:** `wiki/index.md:9` -> `[[metronome-index]]` -> `wiki/metronome-index.md:232` `[[metronome-usage-based-billing]]` -> `wiki/concepts/metronome/metronome-usage-based-billing.md:79` `[[source-metronome-guides-pricing-packaging-billing-model-guides-hybrid-business-models]]` -> source `## Raw Sources` link at `wiki/sources/metronome/source-metronome-guides-pricing-packaging-billing-model-guides-hybrid-business-models.md:43`.
- **Answer:** **Launch a hybrid business model** is the guide for combining an existing per-seat subscription with usage-based AI products and pooled AI credits. It routes catalog setup, contract/subscription-linked recurring credits, seat changes, balance notifications, paid top-ups, and customer balance controls.
- **Evidence:** source overview and raw map at `wiki/sources/metronome/source-metronome-guides-pricing-packaging-billing-model-guides-hybrid-business-models.md:14-34`; raw guide purpose and SeatsCo model at `raw/metronome/guides/pricing-packaging/billing-model-guides/hybrid-business-models-2026-07-13.md:9-31`.
- **Extra search:** none; provider concept reciprocal navigation selected the intended guide.

### 8. Hybrid business models — detail question — PASS

- **Starting route:** same concept -> source -> raw route as task 7.
- **Answer:** Feature cutoff is merchant-implemented from Metronome alert webhooks: configure low-credit/depletion threshold notifications, then the merchant gates AI access until a top-up is purchased or the monthly balance resets. For per-user controls, include `user_id` in events, define it as a billable-metric group key, and create a spend alert; the merchant chooses to cut off the user or notify the user/admin. The end-user billing experience is likewise merchant-facing: use `listCustomerBalances` to display the aggregate AI-credit balance and the group-key/spend-alert pattern for per-seat controls. Metronome owns automatic recurring-credit provisioning and proration when subscription seats change; the merchant owns UI, webhook handling, cutoff, notification, and initiating top-up contract edits/payment gating.
- **Evidence:** Metronome provisioning/proration responsibility at `raw/metronome/guides/pricing-packaging/billing-model-guides/hybrid-business-models-2026-07-13.md:23-31` and seat-change behavior at lines 229-233; webhook-driven cutoff at lines 279-297; top-up/payment-gate workflow at lines 300-306; customer balance and per-user controls at lines 350-368. Source correctly narrows alerts to merchant-actionable signals, not automatic enforcement, at `wiki/sources/metronome/source-metronome-guides-pricing-packaging-billing-model-guides-hybrid-business-models.md:18-22`.
- **Extra search:** none; the source's `Implement...` and `Optimize...` locators led directly to the complete raw sections.

### 9. Provision a customer — navigation question — PASS

- **Starting route:** `wiki/index.md:9` -> `[[metronome-index]]` -> `wiki/metronome-index.md:241` `[[metronome-customers-and-contracts]]` -> `wiki/concepts/metronome/metronome-customers-and-contracts.md:253` `[[source-metronome-guides-customers-billing-manage-customers-provision-a-customer]]` -> source `## Raw Sources` link at `wiki/sources/metronome/source-metronome-guides-customers-billing-manage-customers-provision-a-customer.md:57`.
- **Answer:** **Metronome Provision a Customer and Contract** is the end-to-end route for creating the billing recipient and configuring the contract that governs rating and billing. It covers customer identity/ingest aliases, billing-destination setup, contract terms, invoice consolidation, discounts, usage filters, and custom fields.
- **Evidence:** source overview/flow at `wiki/sources/metronome/source-metronome-guides-customers-billing-manage-customers-provision-a-customer.md:14-22` and detail map at lines 36-46; raw introduction at `raw/metronome/guides/customers-billing/manage-customers/provision-a-customer-2026-08-28.md:9-22`.
- **Extra search:** none; the main concept source entry and raw link were sufficient.

### 10. Provision a customer — detail question — PASS

- **Starting route:** same concept -> source -> raw route as task 9.
- **Answer:** Before provisioning, the guide lists four prerequisites: usage events connected to Metronome, a billable metric, a product, and a rate card. A scoped additional prerequisite applies when adding a billing-provider configuration: Metronome must already be connected to that destination. Creating the customer object alone does not start billing usage; the customer needs at least one contract before metering and rating for billing begin. The contract encodes product access, rates, access duration, and other commercial terms, and it selects the billing configuration when routing to a provider.
- **Evidence:** prerequisites and start boundary at `raw/metronome/guides/customers-billing/manage-customers/provision-a-customer-2026-08-28.md:13-22`; provider-connection prerequisite at lines 87-91; provider routing requires contract selection at lines 121-126; contract purpose at lines 129-133.
- **Extra search:** none; the source's `Create a customer`, billing-configuration, and contract locators covered the question.

## Pilot interpretation

All ten questions were answerable through the intended layered navigation. Detailed values and behavioral qualifications required raw reads, while the source summaries successfully selected and localized that evidence. No source needed broader scope to pre-answer ordinary schema detail, and no unlinked or related-raw sweep contributed evidence to these answers.
