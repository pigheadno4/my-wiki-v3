# Campaign 44 final quality audit

Coordinator verdict: PASS, 10/10 predetermined query answers. Both reports were read and checked against the assigned object/action questions; no query repair or extra full raw reads. Group A routes used promoted concept/source links before final catalog aggregation; group B observed final catalogs. Reports below preserve auditor evidence and timing; reported handoff may precede coordinator receipt.

# Campaign 44 final retrieval audit — group A

## Timing

- UTC start: `2026-09-11T14:02:25Z`
- UTC analysis end: `2026-09-11T14:05:53Z`
- UTC final handoff: `2026-09-11T14:05:57Z`

## Page 1 — Add Rates

Route (used for both questions): `wiki/index.md` → `wiki/metronome-index.md` → `wiki/concepts/metronome/metronome-products-and-rate-cards.md` → `wiki/sources/metronome/source-metronome-api-reference-rate-cards-add-rates.md` → `raw/metronome/api-reference/rate-cards/add-rates-2026-07-13.md`.

1. **Where can I add multiple rates to a rate card rather than add only one rate? — PASS**
   - Object/action match: yes — bulk addition of product rates to one rate card, not single-rate addition.
   - Answer: use bearer-authenticated `POST /v1/contract-pricing/rate-cards/addRates`. Its JSON object requires `rate_card_id` and a `rates` array; the example contains two rate entries.
   - Raw evidence: `raw/metronome/api-reference/rate-cards/add-rates-2026-07-13.md`, `paths./v1/contract-pricing/rate-cards/addRates.post` and its `requestBody` (`lines 87–131`, especially `88–112`).

2. **Where are batch request constraints, rate configuration and success response documented? — PASS**
   - Object/action match: yes — locations belong to the bulk `addRates` request, its per-rate configuration, and that operation's success response.
   - Answer: batch payload constraints are at `paths./v1/contract-pricing/rate-cards/addRates.post.requestBody.content.application/json.schema`; per-rate configuration is at `components.schemas.RatePayload`, with specialized nested configuration at `Tier`, `MinimumConfig`, and `CommitRate`; success is at the same operation's `responses.200`, whose required `data` resolves to `components.schemas.Id` and is described as the rate-card ID.
   - Raw evidence: `raw/metronome/api-reference/rate-cards/add-rates-2026-07-13.md`, request `lines 96–112`, success response `lines 132–147`, `RatePayload` beginning at `line 158`, `Id` at `line 292`, `Tier` at `line 307`, `MinimumConfig` at `line 316`, and `CommitRate` at `line 327`.

## Page 2 — Get a Rate Schedule

Route (used for both questions): `wiki/index.md` → `wiki/metronome-index.md` → `wiki/concepts/metronome/metronome-products-and-rate-cards.md` → `wiki/sources/metronome/source-metronome-api-reference-rate-cards-get-a-rate-schedule.md` → `raw/metronome/api-reference/rate-cards/get-a-rate-schedule-2026-07-13.md`.

3. **Where can I retrieve a rate-card schedule rather than contract-specific overridden prices? — PASS**
   - Object/action match: yes — rate-card catalog schedule retrieval, not a customer's contract schedule with overrides.
   - Answer: use bearer-authenticated `POST /v1/contract-pricing/rate-cards/getRateSchedule`. For a specific customer's rates inclusive of contract-level overrides, the page instead directs callers to `getContractRateSchedule`.
   - Raw evidence: `raw/metronome/api-reference/rate-cards/get-a-rate-schedule-2026-07-13.md`, page purpose and boundary `lines 9–13`; operation `paths./v1/contract-pricing/rate-cards/getRateSchedule.post`, including the repeated contract-override boundary, `lines 89–110`.

4. **What starting-date/filter scope is documented, and where are request and scheduled-rate response schemas? — PASS**
   - Object/action match: yes — temporal/filter scope and schemas for rate-card schedule retrieval.
   - Answer: `starting_at` is required and inclusive; `ending_before` is optional and exclusive, and omitting it returns all future schedule segments. Selector objects match with ANY semantics; omitting selectors returns all rates. Selector fields cover product ID, billing frequency, and exact or partial pricing-group values. The request schema is `components.schemas.GetRateSchedulePayload`; selector rules are in `components.schemas.RateSelector`. The success envelope is `paths./v1/contract-pricing/rate-cards/getRateSchedule.post.responses.200`, whose `data` items resolve to `components.schemas.RateSchedule`; nested pricing schemas are `Rate`, `CommitRate`, `Tier`, `MinimumConfig`, and `CreditType`.
   - Raw evidence: `raw/metronome/api-reference/rate-cards/get-a-rate-schedule-2026-07-13.md`, success envelope `lines 128–144`, request/date/filter scope `GetRateSchedulePayload` at `lines 164–191`, scheduled-rate response `RateSchedule` at `lines 192–236`, selector schema at `line 237`, and nested schemas at `Rate` line `281`, `CommitRate` line `390`, `Tier` line `459`, `MinimumConfig` line `468`, and `CreditType` line `479`.

## Page 3 — Update a Credit Grant

Route (used for both questions): `wiki/index.md` → `wiki/metronome-index.md` → `wiki/concepts/metronome/metronome-credits-and-commits.md` → `wiki/sources/metronome/source-metronome-api-reference-credit-grants-update-a-credit-grant.md` → `raw/metronome/api-reference/credit-grants/update-a-credit-grant-2026-07-13.md`.

5. **Where can I edit a legacy credit grant rather than a Contracts credit? — PASS**
   - Object/action match: yes — editing an existing legacy Plans credit grant, not editing a current Contracts credit.
   - Answer: use bearer-authenticated `POST /v1/credits/editGrant` (OpenAPI server `https://api.metronome.com/v1` plus path `/credits/editGrant`).
   - Raw evidence: `raw/metronome/api-reference/credit-grants/update-a-credit-grant-2026-07-13.md`, title/deprecation statement `lines 9–11`, server `lines 23–25`, and `paths./credits/editGrant.post` at `lines 91–100`.

6. **What deprecation boundary applies, and where are grant identification and editable fields documented? — PASS**
   - Object/action match: yes — deprecation and request semantics for the legacy Plans credit-grant edit.
   - Answer: this is a deprecated Plans endpoint, and new clients are directed to Contracts. Grant identification and editable-field prose are under `paths./credits/editGrant.post.requestBody`; it requires the grant `id` and says only `name` and `expires_at` are currently editable. `components.schemas.EditCreditGrantPayload` is the payload schema. That schema also exposes optional `credit_grant_type`, which conflicts with the narrower request description, so its editability must not be assumed without further authority.
   - Raw evidence: `raw/metronome/api-reference/credit-grants/update-a-credit-grant-2026-07-13.md`, deprecation boundary `lines 97–100`, request description/example `lines 101–112`, and `EditCreditGrantPayload` at `lines 136–154`.

## Shared gap sweep, extra reads, and reciprocal routes

- Query-relevant filename sweep found adjacent raw pages for single-rate addition, the separate `getRates` surface, contract rate schedules, and current Contracts credit editing. None was needed to answer these six questions: each selected raw directly establishes its requested operation, object boundary, and requested schema locator. No source summary has a `## Related raw API references` section.
- Historical presence alone did not trigger a read. In particular, the two dated snapshots of the adjacent current Contracts `edit-a-credit` page were not opened because the questions ask for the legacy Plans grant endpoint and its selected raw directly states the Contracts migration boundary.
- Extra full raw reads: none. Reasons: no unresolved query-relevant conflict, version/history question, or missing detail remained after the three selected complete raw reads.
- Reciprocal route check: PASS once per page. Each source links back to its main concept, and the corresponding concept links to the source: Add Rates at `metronome-products-and-rate-cards.md:151`; Get a Rate Schedule at `metronome-products-and-rate-cards.md:58`; Update a Credit Grant at `metronome-credits-and-commits.md:268`.
- Concrete retrieval failures: none. Overall: **6/6 PASS**.


---

# Campaign 44 final query audit — Group B (Q7–Q10)

## Timing (UTC)

- audit_started_at: `2026-09-11T14:06:32Z`
- analysis_ended_at: `2026-09-11T14:08:39Z`
- final_handoff_at: `2026-09-11T14:09:38Z`

## Page route 1 — Add a Plan to an existing customer

`wiki/index.md` → `wiki/metronome-index.md` → `wiki/concepts/metronome/metronome-customers-and-contracts.md` → `wiki/sources/metronome/source-metronome-api-reference-plans-add-a-plan-to-a-customer.md` → `raw/metronome/api-reference/plans/add-a-plan-to-a-customer-2026-07-13.md`

- Selected raw read completely: 275 lines.
- SHA-256: `6b030d2918e8d6b72a5eef7d87eb1c599f0102afc562a05d34a02941a31983fe`.

### Q7 — Where can I associate an existing customer with a Plan rather than create a Contract?

- Object/action match: **MATCH** — this is association of one existing customer with one existing legacy Plan, not customer creation and not Contract creation.
- Requested answer: Use bearer-authenticated `POST https://api.metronome.com/v1/customers/{customer_id}/plans/add`. The operation adds a Plan to an existing customer for a specified date range; it is explicitly a deprecated Plans operation rather than a Contract-creation route.
- Exact evidence: raw lines 9–11 state the existing-customer/Plan association and deprecated-Plans boundary; lines 18 and 23–27 establish the POST path, `/v1` production server, and bearer authentication; lines 92–105 identify the operation and required customer path selector.
- Verdict: **PASS** — the promoted concept/source route reaches the exact legacy Plan-association operation without substituting Contract creation.

### Q8 — What deprecation/date-range boundaries apply, and where are selectors and adjustment schemas documented?

- Object/action match: **MATCH** — this asks about the same legacy customer-to-Plan association request, its time bounds, selectors, and adjustment-schema locations; it is not a request for a current Contract schema or a copied field inventory.
- Requested answer: The operation is on the deprecated Plans surface, and new clients are directed to Contracts; the page provides no replacement Contract operation, Plan-to-Contract mapping, compatibility period, or removal date. `starting_on` is required; optional `ending_before` is exclusive; both must be RFC 3339 timestamps at midnight UTC. Request selectors are documented at `## OpenAPI` → `/customers/{customer_id}/plans/add` → `post.parameters` / `components.parameters.CustomerId` and `components.schemas.AddPlanToCustomerPayload.required` / `properties.plan_id`. Adjustment details are documented at `components.schemas.AddPlanToCustomerPayload.properties.price_adjustments`; optional trial and overage configuration are adjacent at `properties.trial_spec` and `properties.overage_rate_adjustments`.
- Exact evidence: raw lines 97–103 state deprecation and the direction to Contracts; the complete 275-line raw names no replacement, mapping, compatibility period, or removal date. Lines 104–115 locate the parameter, payload, and example; lines 133–160 define the customer/Plan selectors and inclusive-start/exclusive-end midnight-UTC boundaries; lines 168–210 locate the price-adjustment schema; lines 211–261 locate the optional trial and overage structures.
- Verdict: **PASS** — the route preserves the deprecation and date qualifications and gives verified selector/schema locators rather than an unnecessary inventory.

## Page route 2 — Archive a package

`wiki/index.md` → `wiki/metronome-index.md` → `wiki/concepts/metronome/metronome-packages-and-aliases.md` → `wiki/sources/metronome/source-metronome-api-reference-packages-archive-a-package.md` → `raw/metronome/api-reference/packages/archive-a-package-2026-07-13.md`

- Selected raw read completely: 166 lines.
- SHA-256: `ce29df756ed66814cb647ab2d6fc4fb374e2f532e9a24ba53ed642ff3a96f567`.

### Q9 — Where can I archive a package rather than end its existing contracts?

- Object/action match: **MATCH** — this is archival of a package object, not archival or termination of the contracts already associated with it.
- Requested answer: Use bearer-authenticated `POST https://api.metronome.com/v1/packages/archive`. Archiving the package prevents its use for new contracts but does not end its existing associated contracts; those continue to function normally.
- Exact evidence: raw lines 9–11 state the package-archive action and existing-contract continuity; lines 18 and 23–27 establish the POST path, production server, and bearer authentication; lines 88–98 define the exact archive operation and repeat the new-versus-existing-contract effects.
- Verdict: **PASS** — the promoted route distinguishes package archival from ending existing contracts.

### Q10 — What happens to new/existing contracts, retrieval and reversibility, and where is target identification documented?

- Object/action match: **MATCH** — the target is one package selected for archival; the requested effects concern later package use and already-associated contracts, not contract archival or package deletion.
- Requested answer: An archived package cannot be used to create new contracts; existing associated contracts continue normally. The package remains retrievable through both the UI and API, and it cannot be unarchived, so the operation is irreversible. Target identification is documented at `## OpenAPI` → `paths./v1/packages/archive.post.requestBody.content.application/json.schema.properties.package_id`; within the supplied JSON schema, `package_id` is a required UUID and additional properties are disallowed. The enclosing `requestBody` is not itself marked required, so omitted-body runtime behavior is not established.
- Exact evidence: raw lines 93–98 state the new-contract restriction, existing-contract continuity, UI/API retrieval, and inability to unarchive; lines 99–113 locate the request schema and required UUID `package_id` target; lines 114–128 locate the success response.
- Verdict: **PASS** — every requested lifecycle effect and the target locator is discoverable through the promoted route.

## Shared gap sweep, extra reads, and reciprocal checks

- Gap sweep: searched `raw/metronome/` filenames and page content for the exact customer-Plan association language, `plans/add`, `price_adjustments`, package-archive language, `packages/archive`, and `cannot unarchive`. The two selected raws were the only exact page-level operation matches. `raw/metronome/api-reference/products/archive-a-product-2026-07-13.md` was a search hit but is the wrong object (product, not package), so it was not selected. Discovery/current-inventory records identify the same canonical pages, and an August collection run records each as unchanged; those metadata/history records were not treated as factual evidence or as a reason to claim equivalence.
- Extra full raw reads: none. Q7–Q10 ask the selected operations' current documented behavior and exact locators, not history or version differences. Both selected raws answered every requested point, and no relevant unlinked or related conflict required another authority. Neither source contains a `## Related raw API references` section.
- Reciprocal checks: `wiki/index.md` routes to `wiki/metronome-index.md`; the provider index contains both main concept routes and both promoted source entries. `metronome-customers-and-contracts.md` links the Plan-association source in `## Sources`, and that source links back under `Primary concept`. `metronome-packages-and-aliases.md` cites the package-archive source in `### Package archival`, and that source links back under `Primary concept`; the inline supported citation is the reciprocal concept route. Each source's `raw_files` and `## Raw Sources` link resolves to the exact fully read raw above.
- Group verdict: **PASS (Q7–Q10 all PASS; no retrieval repair required).**

## Completeness

- One scoped completeness check passed: exactly four object/action matches, four requested answers, four exact-evidence blocks, four verdicts, two actual routes, the shared gap sweep, extra-read reasons, reciprocal checks, and distinct analysis/handoff timestamps are present.
