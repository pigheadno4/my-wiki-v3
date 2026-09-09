# Campaign 42 final query quality audit

Verdict: PASS — 10/10 predetermined questions. Coordinator checked requested versus reached objects and actions for all answers. No query-driven source repair, wrong-object rerun, or additional audit round was required. Reports below are the independent handoffs, preserved verbatim under a common cover.

The single audit was split into disjoint groups (Q1–Q6 and Q7–Q10). Both followed live index/concept/source/raw routes, read selected evidence fully and performed the required gap sweep. Group A made two extra historical-snapshot reads; Group B made three extra related-authority reads. These were query evidence reads, not ingestion retries.

---

# Campaign 42 final query audit — Group A (Q1–Q6)

## Timing

- UTC analysis start: `2026-09-09T14:04:46Z`
- UTC analysis end: `2026-09-09T14:08:37Z`
- UTC final handoff: `2026-09-09T14:10:24Z`

## Q1 — Product/update: Where update an existing product rather than create a replacement?

- **Requested object/action:** mutate an existing **Product**. **Reached object/action:** the `Update a product` operation for a Product, not Product creation or Rate Card pricing.
- **Route:** `wiki/index.md` -> `wiki/metronome-index.md` -> `wiki/concepts/metronome/metronome-products-and-rate-cards.md` -> `wiki/sources/metronome/source-metronome-api-reference-products-update-a-product.md` -> `raw/metronome/api-reference/products/update-a-product-2026-08-28.md`.
- **Answer:** Use bearer-authenticated `POST /v1/contract-pricing/products/update`, identifying the existing Product with `product_id`. Create-and-archive replacement is only the documented path when the Product type itself is wrong.
- **Exact evidence:** selected raw lines 91–110 identify the Product update path/operation and immutable-type replacement exception; lines 128–133 route the payload and example to `UpdateProductListItemPayload` with an existing `product_id`.
- **Verdict:** **PASS** — the live index/concept/source/raw route reaches the requested existing-Product update operation and answers it directly.

## Q2 — Product/update: What effective-time and product-type restrictions apply, and where are editable properties documented?

- **Requested object/action:** constraints and property authority for the same existing-**Product update**. **Reached object/action:** the same `Update a product` operation and its payload schema.
- **Route:** Same as Q1.
- **Answer:** `starting_at` is required, must be a date-time on an hour boundary, and may be future-dated for scheduling or past-dated for a retroactive change. Product type cannot be changed; an incorrect type requires a new Product and archival of the original. The authoritative editable-property list and all field-specific qualifications are under `components.schemas.UpdateProductListItemPayload` (with nested schemas for referenced structures), not the prose phrase “pricing rules.”
- **Exact evidence:** selected raw lines 11–14 state future/past effective timing and immutable type; lines 159–179 require `product_id` and `starting_at` and define the hour-boundary constraint; lines 180–264 contain the editable properties and product/configuration qualifications.
- **Verdict:** **PASS** — restrictions and the exact detail locator are discoverable without copying an optional field inventory into the source or concept.

## Q3 — Customer credit/commit net balance/read: Where retrieve a customer's combined matching credit and commit balance?

- **Requested object/action:** read one customer's **combined matching credit-and-commit net balance**, not individual balance ledgers. **Reached object/action:** `Get the net balance of a customer`.
- **Route:** `wiki/index.md` -> `wiki/metronome-index.md` -> `wiki/concepts/metronome/metronome-credits-and-commits.md` -> `wiki/sources/metronome/source-metronome-api-reference-credits-and-commits-get-the-net-balance-of-a-customer.md` -> `raw/metronome/api-reference/credits-and-commits/get-the-net-balance-of-a-customer-2026-08-28.md`.
- **Answer:** Use bearer-authenticated `POST /v1/contracts/customerBalances/getNetBalance` with required `customer_id`; it returns the combined current balance across all matching commits and credits. Use `listBalances` instead only when per-balance ledger detail is required.
- **Exact evidence:** selected raw lines 11–18 define the combined result; lines 29–33 distinguish `listBalances`; lines 109–117 identify the exact operation; lines 193–204 define customer and denomination request fields.
- **Verdict:** **PASS** — route and endpoint match the requested customer-level combined read rather than an individual-credit, individual-commit, or detailed-ledger object.

## Q4 — Customer net balance: How are filter groups combined, what is the denomination, and where are filtering/response details defined?

- **Requested object/action:** filtering, denomination, and response-detail authority for the same combined **customer net-balance read**. **Reached object/action:** the same `getNetBalance` request and response schemas.
- **Route:** Same as Q3.
- **Answer:** Multiple filter objects are ORed; conditions inside one filter object are ANDed. A filter can select balance types, exact IDs, and custom-field pairs. `credit_type_id` selects the fiat or custom pricing unit and defaults to USD cents when omitted; current quantity-access filtering is the exception, because `access_type: QUANTITY` forbids `credit_type_id`. The returned `data` requires numeric `balance` and `credit_type_id`. Full filtering is defined at the operation request schema plus `components.schemas.BalanceFilter`; response placement is defined at `responses -> 200 -> application/json -> schema`.
- **Exact evidence:** selected raw lines 20–26 state OR-between/AND-within composition and selectors; lines 193–227 define `credit_type_id`, the quantity-access boundary, and filter-array schema; lines 252–283 require `data.balance` and `data.credit_type_id`; lines 290–313 define `BalanceFilter` details.
- **Verdict:** **PASS** — combination rules, denomination, current qualification, and exact request/response locators are all reachable.

## Q5 — Rate card/create: Where create a rate card rather than add rates to an existing card?

- **Requested object/action:** create a new **Rate Card**, not add rates to an existing Rate Card. **Reached object/action:** `Create a rate card`.
- **Route:** `wiki/index.md` -> `wiki/metronome-index.md` -> `wiki/concepts/metronome/metronome-products-and-rate-cards.md` -> `wiki/sources/metronome/source-metronome-api-reference-rate-cards-create-a-rate-card.md` -> `raw/metronome/api-reference/rate-cards/create-a-rate-card-2026-07-13.md`.
- **Answer:** Use bearer-authenticated `POST /v1/contract-pricing/rate-cards/create`; the create payload requires `name`, and success returns the created ID at `data.id`. Product/rate addition is a subsequent operation, not part of this create endpoint.
- **Exact evidence:** selected raw lines 13–22 distinguish creation from later product/rate addition; lines 99–104 identify the create path; lines 228–246 define the create payload and required `name`; lines 216–221 show `data.id`.
- **Verdict:** **PASS** — the route reaches Rate Card creation and preserves the boundary from rate addition.

## Q6 — Rate card/create: What currency and alias boundaries are documented, and where is subsequent product/rate addition directed?

- **Requested object/action:** setup boundaries on the same new **Rate Card** plus the next action for adding products/rates. **Reached object/action:** the same Rate Card create operation and its usage guidance.
- **Route:** Same as Q5.
- **Answer:** A Rate Card has one underlying fiat currency; omitting `fiat_credit_type_id` defaults it to USD cents. Any number of custom-pricing-unit conversions may be supplied, and a conversion is required for custom units used by rates. An alias can belong to only one Rate Card at a time; reusing it updates the original card's alias schedule and resolves the alias to the most recently assigned card. After creation, use `addRate` or `addRates` to add products and their prices.
- **Exact evidence:** selected raw lines 15–16 state the single-fiat, conversion, and alias purposes; lines 22–23 state the next endpoints and consequential alias reassignment; lines 240–260 define fiat default, conversion requirement, and latest-assignment alias resolution.
- **Verdict:** **PASS** — currency, alias, and next-operation boundaries are directly supported and correctly routed.

## Shared Group A checks

- **Gap sweep:** searched `raw/metronome/` filenames and content for Product update/create, Rate Card create/add/update, combined/net/list balances, alias, currency, and `addRate`/`addRates`. No three source pages contain a `## Related raw API references` section. The sweep found older same-canonical snapshots `products/update-a-product-2026-07-13.md` and `credits-and-commits/get-the-net-balance-of-a-customer-2026-07-13.md`; both were read fully. The Product delta only removes feature/SDK annotations from `include_composite_spend`; the net-balance delta adds the current `access_type` request field and its `QUANTITY`/`credit_type_id` exclusion. Neither contradicts Q1–Q6; the latter current qualification is included in Q4. Adjacent `list-balances`, `get-remaining-balance`, `addRate`/`addRates`, and pricing-guide hits were not needed to establish the requested operations because the selected canonical raw pages explicitly state those boundaries and next routes.
- **Extra full reads:** the two older same-canonical snapshots above; no external fetch and no new ingestion.
- **Reciprocal checks:** `wiki/metronome-index.md` links all three source pages (lines 25–27) and both concepts (lines 265 and 268); `metronome-products-and-rate-cards.md` links the Rate Card create and Product update sources (lines 147–148); `metronome-credits-and-commits.md` links the net-balance source (line 269); every source links back to its expected primary/main concept. **PASS.**
- **Group result:** **6/6 PASS; no retrieval failure, wrong-object answer, broken reciprocal route, or material evidence uncertainty found.**

---

# C42 final query audit — Group B (Q7-Q10)

## Timing

- UTC analysis start: `2026-09-09T14:05:18Z`
- UTC analysis end: `2026-09-09T14:09:13Z`
- UTC artifact handoff: `2026-09-09T14:10:29Z`

## Q7 — Offset notification configuration creation

- **Requested object/action:** create and store an **offset lifecycle event notification configuration**, not edit a configuration and not send an event. **Reached object/action:** exact match — the routed source and raw page are titled `Create an offset lifecycle event notification configuration` and define `POST /v2/notifications/create`.
- **Actual route:** `wiki/index.md` -> `wiki/metronome-index.md` -> `wiki/concepts/metronome/metronome-alerts-and-notifications.md` -> `wiki/sources/metronome/source-metronome-api-reference-notifications-create-an-offset-lifecycle-event-notification-configuration.md` -> `raw/metronome/api-reference/notifications/create-an-offset-lifecycle-event-notification-configuration-2026-07-13.md`.
- **Direct answer:** Create it with bearer-authenticated `POST /v2/notifications/create`. The operation stores a notification configuration; success is configuration creation, not proof that a lifecycle event occurred, an offset notification was emitted, or a webhook was delivered.
- **Exact evidence:** raw lines 9-11 (object and action); 18 and 88-108 (method/path, operation identity, and creation example); 109-133 (`200` returns the stored configuration under `data`). The offset guide independently gives the same API setup route at lines 62-66.
- **Verdict:** **PASS**.

## Q8 — Lifecycle-event selection, policy, creation fields, and returned configuration

- **Requested object/action:** select the base lifecycle-event type for a newly created offset configuration and locate its policy, creation payload, and stored response. **Reached object/action:** exact match — these schemas belong to the Q7 create operation, not the edit operation or an emitted-event payload.
- **Actual route:** same as Q7.
- **Direct answer:** Select the lifecycle event through `policy.type`; the operation says the event type is inferred from that field. `components.schemas.LifecycleEventOffsetPolicy` requires `type` and `offset`; `offset` is a signed ISO 8601 duration (positive = after the base event, negative = before). Creation fields are documented by `components.schemas.CreateNotificationConfigPayload`: required `name` and `policy`, plus optional `uniqueness_key`. The `200` response is documented at `paths./v2/notifications/create.post.responses.200.content.application/json`; top-level `data` references `components.schemas.LifecycleEventOffsetNotificationConfig`, whose required stored fields are `id`, `name`, `type`, `policy`, `environment_type`, `created_at`, `created_by`, and nullable `archived_at`.
- **Exact evidence:** raw lines 92-108 (type inference and example); 109-133 (response placement/example); 152-172 (creation payload); 173-215 (stored-configuration schema); 216-234 (policy and signed-offset semantics). The offset guide lines 52-66 confirms UI selection and API policy/name setup without replacing the OpenAPI schemas.
- **Verdict:** **PASS**.

## Q9 — Shorten a customer credit end date

- **Requested object/action:** shorten the end of a customer **CREDIT**, not a **COMMIT**, and not extend the credit. **Reached object/action:** exact match — `POST /v1/contracts/customerCredits/updateEndDate`, operation ID `updateCreditEndDate-v1`, with `customer_id`, `credit_id`, and `access_ending_before`. The separate commit operation is `/v1/contracts/customerCommits/updateEndDate` and uses `commit_id`.
- **Actual route:** `wiki/index.md` -> `wiki/metronome-index.md` -> `wiki/concepts/metronome/metronome-credits-and-commits.md` -> `wiki/sources/metronome/source-metronome-api-reference-credits-and-commits-update-the-credit-end-date.md` -> `raw/metronome/api-reference/credits-and-commits/update-the-credit-end-date-2026-07-13.md`.
- **Direct answer:** Use bearer-authenticated `POST /v1/contracts/customerCredits/updateEndDate` with the customer ID, intended customer-credit ID, and the earlier exclusive `access_ending_before` timestamp.
- **Exact evidence:** credit raw lines 9-13 (credit shortening and no-extension scope); 20 and 90-113 (credit endpoint, operation ID, request example); 139-159 (required identifiers and cutoff). The neighboring commit raw lines 91-119 and 145-172 proves the distinct commit route, `commit_id`, prepaid-only scope, and separate access/invoice cutoffs.
- **Material caveat:** credit raw line 153 incorrectly describes `credit_id` as the "ID of the commit to update." The title, endpoint path, summary/description, operation ID, request description, `customer_id` description, and distinct commit endpoint all contradict that one sentence. Treat it as an upstream documentation inconsistency and verify the supplied ID is the intended customer credit.
- **Verdict:** **PASS** (retrieval succeeds; upstream field-description inconsistency is preserved).

## Q10 — Date direction, changed cutoff, and extension/broader-edit route

- **Requested object/action:** state the date-direction restriction for the customer-credit shortening operation, identify which cutoff changes, and identify the route for extension or broader credit edits. **Reached object/action:** exact match — the credit operation changes the credit's access cutoff only; commit-only invoice-cutoff behavior was not imported.
- **Actual route:** same as Q9.
- **Direct answer:** The new end must move earlier; this operation cannot extend the credit. `access_ending_before` is an exclusive RFC 3339 cutoff: at that timestamp access ends and the credit can no longer be drawn down. For extension or comprehensive credit edits, use the separate edit-credit operation, bearer-authenticated `POST /v2/contracts/credits/edit`. That broader operation can extend a free credit's duration or amount and modify access schedules, applicable products, priority, and other documented credit fields.
- **Exact evidence:** update-credit raw lines 11-13 and 96-102 (earlier-only and edit-credit direction); 104-113 and 139-159 (the sole required credit cutoff and its exclusive meaning). Latest edit-credit raw lines 9-19 and 96-122 documents credit scope, extension/broader edits, endpoint, and invoice/schedule cautions. Commit raw lines 159-172 separately documents access and invoice cutoffs, confirming `invoices_ending_before` is commit-specific and not part of this credit payload.
- **Verdict:** **PASS**.

## Shared group checks

- **Gap sweep:** filename/content searches under `raw/metronome/` found the offset guide plus create/get/list/edit/archive offset-configuration references, and the update-credit, update-commit, and edit-credit references. No external fetch or ingestion was performed. The only material neighboring authorities for these questions were fully read: the offset-notifications guide, the distinct commit end-date operation, and the latest edit-credit operation. No relevant unlinked raw gap changed an answer.
- **Full raw reads:** primary create-offset raw (248 lines) and primary update-credit-end-date raw (187 lines); extra offset guide (86 lines), update-commit-end-date raw (200 lines), and latest edit-credit raw (416 lines).
- **Reciprocal/navigation checks:** root index links `metronome-index`; provider index links both main concepts and both target sources; each concept links its target source; each target source links back to its main concept and links the exact path-qualified raw named in `raw_files`. All checks passed.
- **Completeness:** Q7-Q10 only; four object/action checks, four direct answers, four exact-evidence blocks, and four verdicts present. One completeness check passed after evidence review.

## Group result

**PASS — 4/4 questions.** No retrieval repair is required. Preserve the Q9 upstream `credit_id` description inconsistency as a warning; it does not redirect the operation to the commit endpoint.
