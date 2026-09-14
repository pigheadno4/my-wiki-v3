# Campaign 45 final quality audit

Coordinator verdict: PASS, ten predetermined questions answered with correct object/action matches. Read both complete reports and checked against assigned questions; no retrieval repair. One justified extra 190-line adjacent-operation read, not a new ingestion or inferred equivalence. Reports preserve read-time route line numbers and role timestamps.

# Campaign 45 final query audit A — Q1–Q4

## Timing

- Started (UTC, captured before repository reads): `2026-09-13T08:22:36Z`
- Analysis ended (UTC): `2026-09-13T08:25:55Z`
- Handoff (UTC, after one completeness check): `2026-09-13T08:26:00Z`

## Actual retrieval routes

1. **Legacy v1 customer-contract list page:** `wiki/index.md:9` (`[[metronome-index]]`) -> `wiki/metronome-index.md:280` (`[[metronome-customers-and-contracts]]`) -> `wiki/concepts/metronome/metronome-customers-and-contracts.md:258` (`[[source-metronome-api-reference-contracts-list-customer-contracts-v1]]`) -> `wiki/sources/metronome/source-metronome-api-reference-contracts-list-customer-contracts-v1.md` -> `raw/metronome/api-reference/contracts/list-customer-contracts-v1-2026-08-28.md`.
2. **v2 customer-contract list page:** `wiki/index.md:9` (`[[metronome-index]]`) -> `wiki/metronome-index.md:280` (`[[metronome-customers-and-contracts]]`) -> `wiki/concepts/metronome/metronome-customers-and-contracts.md:257` (`[[source-metronome-api-reference-contracts-list-customer-contracts-v2]]`) -> `wiki/sources/metronome/source-metronome-api-reference-contracts-list-customer-contracts-v2.md` -> `raw/metronome/api-reference/contracts/list-customer-contracts-v2-2026-08-28.md`.

The promoted source pages are reached through the live concept routes; provider-source catalog aggregation is intentionally later and was not used as a shortcut.

## Answers

### Q1 — Where can I list a customer's contracts using legacy v1 rather than read a single contract?

- **Object/action match:** Requested object is one customer's **contract collection** and requested action is **list/read**, not a single-contract lookup. Reached evidence is the `List customer contracts (v1)` collection-read operation.
- **Asked answer:** Use bearer-authenticated `POST /v1/contracts/list`. It retrieves all contracts for a specific customer for contract-history and current-agreement views.
- **Exact raw evidence:** `raw/metronome/api-reference/contracts/list-customer-contracts-v1-2026-08-28.md:9-13` (identity, purpose, legacy qualification); OpenAPI `paths./v1/contracts/list.post` at lines `90-104` (summary, description, `operationId: listContracts-v1`).
- **Verdict:** **PASS** — the actual route selects the correct customer-contract collection action and the raw identifies the legacy v1 list endpoint without diverting to a single-contract read.

### Q2 — What version boundary applies, and where are customer/filter selectors, optional ledger/balance controls and returned contract schemas documented?

- **Object/action match:** Requested details belong to the legacy v1 **customer-contract list request and response**, not to v2 field comparison or a contract mutation.
- **Asked answer:** This is the **legacy v1** endpoint; Metronome says new integrations should use v2 for enhanced features. The v1 list request's JSON schema requires `customer_id`; it locates archive/time selection and the mutually exclusive `starting_at`/`covering_date` filters alongside optional `include_ledgers` and `include_balance` controls, both warned as potentially slower. The success envelope returns a `data` array of `Contract` objects.
- **Where to find it:**
  - Version boundary: raw lines `9-13` and OpenAPI `paths./v1/contracts/list.post.description`, lines `94-104`.
  - Customer/filter and ledger/balance controls: `paths./v1/contracts/list.post.requestBody.content.application/json.schema`, raw lines `105-146`.
  - Success envelope: `paths./v1/contracts/list.post.responses.200.content.application/json.schema`, raw lines `147-160`.
  - Returned contract schemas: `components.schemas.Contract` (starts line `330`), `ContractWithoutAmendments` (line `450`), and `ContractAmendment` (line `636`); optional balance detail routes through `Commit` (line `886`), `Credit` (line `1082`), `CommitLedger` (line `2081`), `BalanceForCommitsAndCredits` (line `2105`), and `CreditLedger` (line `2146`).
- **Verdict:** **PASS** — the source gives a discoverable version warning and exact request, response, and component-schema locators without requiring a copied field inventory or historical/cross-version comparison.

### Q3 — Where can I list a customer's contracts with v2 for contract history rather than change a contract?

- **Object/action match:** Requested object is one customer's **contract collection/history** and requested action is **list/read**, not `editContract` or another mutation. Reached evidence is the v2 list operation.
- **Asked answer:** Use bearer-authenticated `POST /v2/contracts/list`. It lists the customer's contracts for provisioning checks, the current agreement, and the customer's history of contract tiers.
- **Exact raw evidence:** `raw/metronome/api-reference/contracts/list-customer-contracts-v2-2026-08-28.md:9-19` (collection purpose, current-contract and tier-history use cases); OpenAPI `paths./v2/contracts/list.post`, lines `96-124` (`operationId: listContracts-v2`).
- **Verdict:** **PASS** — the route and raw select the v2 contract-history collection read, not the contract-change operation.

### Q4 — What ordering/current-history scope is documented, and where are request selection and contract response details located?

- **Object/action match:** Requested facts are the v2 **customer-contract list** ordering, current/history selection, and response-detail routes.
- **Asked answer:** The result is documented as being in **chronological order**; no ascending/descending direction is stated. The endpoint supports contract-tier history and current-agreement views. To list only contracts active now, pass `covering_date` equal to the current time. `starting_at`, `covering_date`, and `include_archived` select the returned history; `starting_at` and `covering_date` cannot be combined. HTTP `200` places `ContractV2` items in top-level `data`. A returned contract's embedded commits or credits can be incomplete when the corresponding `has_more` flag is true.
- **Where to find it:**
  - Ordering and current/history scope: raw lines `9-19`; duplicated in `paths./v2/contracts/list.post.description`, lines `100-123`.
  - Request selection: `paths./v2/contracts/list.post.requestBody.content.application/json.schema`, raw lines `125-165`.
  - Response placement: `paths./v2/contracts/list.post.responses.200.content.application/json.schema`, raw lines `166-179`.
  - Contract response details: `components.schemas.ContractV2` (starts line `275`); embedded collection completeness: `components.schemas.HasMore` (starts line `838`).
- **Verdict:** **PASS** — the direct answer and exact locators are retrievable through the promoted route; the answer avoids inventing an ordering direction or complete embedded collections.

## Shared gap sweep, reciprocal routes, and completeness

- **Selected raw reads completed in full:** v1, `3,481/3,481` lines; v2, `3,210/3,210` lines.
- **Query-relevant filename sweep:** found the selected 2026-08-28 v1/v2 list snapshots; older 2026-07-13 snapshots of the same canonical pages; and adjacent package-list, single-contract get, and contract-edit pages. The older snapshots were not selected because no question asks for historical version differences and no relevant conflict was discovered. The adjacent pages were not selected because their object/action is package projection, single-object lookup, or mutation rather than customer-contract collection history.
- **Extra full reads:** none. Reason: the two selected full raws directly answer all four questions; no retained claim required adjacent authority, and the sweep exposed no conflict or evidence gap. No cross-version field comparison was performed.
- **Reciprocal route check (once):** concept -> v2 source at `wiki/concepts/metronome/metronome-customers-and-contracts.md:257` and concept -> v1 source at line `258`; v2 source -> concept at `wiki/sources/metronome/source-metronome-api-reference-contracts-list-customer-contracts-v2.md:38`; v1 source -> concept at `wiki/sources/metronome/source-metronome-api-reference-contracts-list-customer-contracts-v1.md:36`. Both reciprocal routes are intact.
- **Repairs:** none.
- **Failures/material uncertainty:** none. All four questions pass.
- **Completeness check:** performed once after analysis; confirmed two actual routes, four separately scored object/action answers, exact raw locators, complete selected-raw reads, one shared gap sweep, one reciprocal check, extra-read reasons, timings, and failure status.


---

# Campaign 45 final retrieval audit — Group B

## Timing and scope

- `started_at_utc`: `2026-09-13T08:25:16Z`
- `analysis_completed_at_utc`: `2026-09-13T08:28:28Z`
- `final_artifact_handoff_at_utc`: `2026-09-13T08:30:02Z`
- `analysis_elapsed`: `3m12s`
- `start_to_final_handoff_elapsed`: `4m46s` (includes the single completeness check)
- Scope: Q5–Q10 only. Repository and tracking remained read-only; the only write is this report. No manifest, attempt, receipt, or historical-version shortcut was used.
- Rules/contracts read before audit: `CLAUDE.md`, `rules/query-and-synthesis.md`, `rules/psp/metronome-ingest.md`, and `tracking/ingest/metronome/metronome-campaign-45/dispatch-contract.md`.
- Final group verdict: **PASS — 6/6 questions reached the correct promoted object/action through the required live route and were verified against complete exact-raw reads.**

## Page A — list customer commits

### Route (used once for Q5 and Q6)

`wiki/index.md:9` → `wiki/metronome-index.md:280` (`metronome-credits-and-commits`) → `wiki/concepts/metronome/metronome-credits-and-commits.md:268` → `wiki/sources/metronome/source-metronome-api-reference-credits-and-commits-list-commits.md` → `raw/metronome/api-reference/credits-and-commits/list-commits-2026-08-28.md` (1,115 lines, SHA-256 `3b760a1808648eff75b1551225be9a91e4fcc57362a46d7ab28a51cd2a0a1342`).

The provider catalog also directly lists the promoted source at `wiki/metronome-index.md:27`.

### Q5 — list prepaid/postpaid commits rather than credits

- Requested object/action: list one customer's **commit agreements**, both prepaid and postpaid; do not select the distinct credit-list operation.
- Reached object/action match: **yes**. The raw is titled `List commits`, says it retrieves both prepaid and postpaid commitments, and exposes operation `POST /v1/contracts/customerCommits/list` (`raw` lines 9–11 and 120–130).
- Direct answer: use bearer-authenticated `POST /v1/contracts/customerCommits/list`; in a supplied JSON object, `customer_id` is the required customer selector (`paths./v1/contracts/customerCommits/list.post.requestBody.content.application/json.schema`, `raw` lines 188–200). The returned `Commit.type` distinguishes `PREPAID` and `POSTPAID` (`components.schemas.Commit.type`, `raw` lines 334–359).
- Verdict: **PASS**. The route selects commits, not credits, and gives the exact operation and customer selector.

### Q6 — selection, balance/ledger controls, returned details, and qualifications

- Requested object/action: on that same customer-commit list operation, locate selection and expansion controls, the returned commit schema, and the qualifications needed to interpret ledger and balance views.
- Reached object/action match: **yes**. All requested controls and returned views are under the same `customerCommits/list` operation and its referenced `Commit` components, not a credit or aggregate-balance endpoint.
- Direct answer and exact raw locators:
  - Selection/pagination controls are at `paths./v1/contracts/customerCommits/list.post.requestBody.content.application/json.schema`: required-within-a-supplied-object `customer_id`, plus optional `commit_id`, feature-annotated `access_type`, `covering_date`, `starting_at`, exclusive `effective_before`, `include_contract_commits`, `include_archived`, `next_page`, and `limit` (`raw` lines 188–263). `include_contract_commits` expands beyond customer-level commits; `include_archived` also includes archived commits and commits from archived contracts (`raw` lines 237–244).
  - Ledger/balance expansion controls are `include_ledgers` and `include_balance` at that same request-schema locator; both are documented as potentially slower (`raw` lines 245–254).
  - The response envelope is `paths./v1/contracts/customerCommits/list.post.responses.200.content.application/json.schema`, with `data[]` referencing `components.schemas.Commit` and nullable `next_page` (`raw` lines 268–285). Returned commit detail is at `components.schemas.Commit` (`raw` lines 334–531), schedule detail at `ScheduleDuration` and `SchedulePointInTime` (`raw` lines 532–609), ledger variants at `CommitLedger` (`raw` lines 658–681), and current balance meaning at `BalanceForCommitsAndCredits` (`raw` lines 682–693).
  - Interpretation qualifications: `ledger` is an ordered event list affecting the commit balance (`raw` lines 485–493). The calculated balance is value accessible **now**: expired and upcoming segments contribute zero; excessive negative manual entries cannot reduce the calculated value below zero; future-dated manual entries associated with active segments are included (`raw` lines 682–693). The selection `access_type` is marked with an `x-mint` feature group and `x-stainless-skip`, so its presence must not be generalized as unqualified client availability (`raw` lines 204–218).
- Verdict: **PASS**. The source routes users to exact controls and components, and the raw supplies the requested performance, feature, ledger, and calculated-balance qualifications.

## Page B — change a legacy customer Plan end date

### Route (used once for Q7 and Q8)

`wiki/index.md:9` → `wiki/metronome-index.md:285` (`metronome-customers-and-contracts`) → `wiki/concepts/metronome/metronome-customers-and-contracts.md:256` → `wiki/sources/metronome/source-metronome-api-reference-plans-end-a-customer-plan.md` → `raw/metronome/api-reference/plans/end-a-customer-plan-2026-07-13.md` (167 lines, SHA-256 `940e1e26b6b745487ab64795f243bb60c01c6b3466ba9db36960eabea1d4598f`).

The provider catalog also directly lists the promoted source at `wiki/metronome-index.md:28`.

### Q7 — change a legacy Plan end date rather than end a Contract

- Requested object/action: change the end date on one legacy **customer-Plan relationship**; do not select a Contract-ending operation.
- Reached object/action match: **yes**. The reached operation is tagged Plans, targets `customer_id` plus `customer_plan_id`, and defines the latter as the ID of a customer-Plan relationship (`raw` lines 91–109 and 121–138).
- Direct answer: use bearer-authenticated `POST /v1/customers/{customer_id}/plans/{customer_plan_id}/end` (the document server contributes `/v1`; the path is at `paths./customers/{customer_id}/plans/{customer_plan_id}/end.post`, `raw` lines 18, 91–109). Supply `ending_before` in `components.schemas.EndCustomerPlanPayload` to change the relationship's end boundary (`raw` lines 140–149).
- Verdict: **PASS**. The selected page mutates a customer Plan, not a Contract.

### Q8 — deprecation/time boundaries and target/date inputs

- Requested object/action: for that same legacy Plan mutation, identify deprecation and time semantics, then locate target and date inputs.
- Reached object/action match: **yes**. The evidence is explicitly Plans-only and documents the relationship selectors and end-date payload.
- Direct answer and exact raw locators:
  - Deprecation boundary: the endpoint is **Plans (deprecated)** and says new clients should implement using Contracts (`raw` lines 9–11 and 96–100). The complete page does **not** identify a Contract replacement operation, Plan-to-Contract identity mapping, compatibility period, or removal date; no such boundary is inferred.
  - Time boundary: `ending_before` is an exclusive RFC 3339 timestamp and must be midnight (`0:00`) UTC. If omitted from a supplied payload, it clears the Plan end date (`components.schemas.EndCustomerPlanPayload.ending_before`, `raw` lines 140–149).
  - Target inputs: `components.parameters.CustomerId` and `CustomerPlanId`, both required UUID path parameters; `CustomerPlanId` is specifically the customer-Plan relationship ID (`raw` lines 121–138). Date and invoice controls are under `components.schemas.EndCustomerPlanPayload` (`raw` lines 140–161).
  - Consequential qualifications: `void_invoices: true` permits an end date before the last finalized invoice date and voids invoices generated after the Plan end date (`raw` lines 150–154). `void_stripe_invoices` applies only with `void_invoices: true` and documents an **attempt** to void finalized Stripe invoices or delete drafts, not guaranteed Stripe success (`raw` lines 155–160). Neither the enclosing `requestBody` nor payload properties are schema-marked required; only the explicit `ending_before` description establishes omission behavior.
- Verdict: **PASS**. Deprecation, exclusive midnight-UTC semantics, omission behavior, targets, and conditional invoice effects are all retrievable without importing Contract behavior.

## Page C — set rate-card product presentation order

### Route (used once for Q9 and Q10)

`wiki/index.md:9` → `wiki/metronome-index.md:283` (`metronome-products-and-rate-cards`) → `wiki/concepts/metronome/metronome-products-and-rate-cards.md:151` → `wiki/sources/metronome/source-metronome-api-reference-rate-cards-set-the-rate-card-products-order.md` → `raw/metronome/api-reference/rate-cards/set-the-rate-card-products-order-2026-07-13.md` (176 lines, SHA-256 `b9d878039d37ce932dac23c5ac7ec1a36b1f2eec113c96d96f92c1b30fa35c45`).

The provider catalog also directly lists the promoted source at `wiki/metronome-index.md:29`.

### Q9 — control invoice presentation order rather than prices

- Requested object/action: set product sequence on a **rate card** to control customer-invoice presentation; do not select a rate or price mutation.
- Reached object/action match: **yes**. The operation explicitly says rate-card product ordering determines customer-invoice appearance and does not describe changing product prices or rate schedules (`raw` lines 9–11 and 90–97).
- Direct answer: use bearer-authenticated `POST /v1/contract-pricing/rate-cards/setRateCardProductsOrder` (`raw` lines 18 and 88–103). In a supplied payload, identify the target with required UUID `rate_card_id` and provide the required ordered array of product UUIDs in `product_order` (`components.schemas.SetRateCardProductsOrderPayload`, `raw` lines 134–148).
- Verdict: **PASS**. The route selects presentation ordering on a rate card, not pricing mutation.

### Q10 — ordering/omission behavior and request/response schemas

- Requested object/action: for the same set-order operation, determine documented order behavior, omitted-product behavior, and exact request-target/response locations.
- Reached object/action match: **yes**. The route remains on `setRateCardProductsOrder`, not the separate relative-move operation found during the sweep.
- Direct answer and exact raw locators:
  - Documented behavior: `product_order` is the ordered product-UUID array for the target `rate_card_id`; that ordering determines how products appear on customer invoices (`raw` lines 90–108 and 134–148).
  - Omitted-product behavior is **genuinely undocumented** in the complete 176-line raw. `components.schemas.SetRateCardProductsOrderPayload.product_order` contains only an array of UUIDs and states no all-products requirement, `minItems`, missing-product placement, preservation, removal, append, or rejection rule (`raw` lines 134–148). No such behavior is inferred.
  - Request target/order schema: `components.schemas.SetRateCardProductsOrderPayload` (`raw` lines 134–148); operation placement is `paths./v1/contract-pricing/rate-cards/setRateCardProductsOrder.post.requestBody` (`raw` lines 88–108). The enclosing `requestBody` itself is not marked required, so omitted-body runtime behavior is also not inferred.
  - Response schema: `paths./v1/contract-pricing/rate-cards/setRateCardProductsOrder.post.responses.200.content.application/json.schema` requires top-level `data`, which references generic `components.schemas.Id`; `Id` requires UUID `id` (`raw` lines 109–123 and 149–156).
- Verdict: **PASS**. The documented ordering and schema routes are precise, and the answer preserves the real omitted-product evidence gap.

## Shared reciprocal, gap-sweep, and provenance check

- Reciprocal check performed once for all three routes: root links `metronome-index` once; the provider index links each promoted source once and each main concept once; each main concept links its promoted source once; each source links its main concept once and has one path-qualified `Raw Sources` link resolving to the exact raw read. No duplicate or wrong-purpose reciprocal route was found.
- Query-relevant sweeps searched `raw/metronome` and `wiki` for `customerCommits/list`, commit/credit list terms, ledger/balance flags, customer-Plan end payload/Stripe void terms, and rate-card product-order endpoints/fields.
- The commit sweep found the historical 2026-07-13 snapshot of the same canonical `list-commits` page plus separate credit, aggregate-balance, seat-balance, and contract surfaces. None was required to answer Q5/Q6 or resolve a conflict, so they were not read and no equivalence was assumed.
- The Plan sweep found other legacy Plan endpoints and both OpenAPI artifacts, but no separate query-bearing page or discovered conflict. They were not used as factual evidence.
- Extra full read: `raw/metronome/api-reference/rate-cards/update-the-rate-card-products-order-2026-07-13.md` (190 lines). Reason: its exact related title and `moveRateCardProducts` operation could have resolved the omitted-product question. It documents moving selected products relative to current positions, but it is a distinct operation (`raw` lines 88–111 and `MoveRateCardProductsPayload` lines 137–162). Per the audit contract, that adjacent operation was **not** used to infer omission behavior for `setRateCardProductsOrder`.
- Historical JSON artifacts, discovery files, and older same-canonical snapshots were not read merely because the sweep found them.

## Completeness disposition

- Retrieval failures: **none**.
- Wrong-object answers: **none**.
- Material unresolved uncertainty: **none beyond the explicitly documented/retained omitted-product gap in Q10 and unspecified Contract migration/removal details in Q8**.
- Repairs requested: **none**.
