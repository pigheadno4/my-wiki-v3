# Campaign 46 final ten-question retrieval audit

Coordinator verdict: PASS, 10/10. All five selected raws were read fully by auditors. No extra full reads, retrieval repairs or wrong-object reruns. The coordinator checked each assigned object/action against the returned answer and accepted both groups. This is the single predetermined retrieval audit, not an extra source-quality review.

Group A's provider-catalog absence and line numbers reflect its pre-aggregation observation. Final aggregate validation independently confirmed all five provider/company entries and reciprocal routes after aggregation. Reports below are preserved verbatim.

# Campaign 46 final retrieval audit — Group A

## Timing and scope

- `started_at_utc`: `2026-09-13T09:23:47Z`
- `analysis_completed_at_utc`: `2026-09-13T09:27:13Z`
- `final_artifact_handoff_at_utc`: `2026-09-13T09:28:43Z`
- `analysis_elapsed`: `3m26s`
- Scope: the four frozen questions for **Get a contract v1** and **List all packages** only. This is retrieval audit, not a third semantic review.
- Repository and tracking state were read-only. The only write is this report at `/private/tmp/c46-audit-a.md`.
- Governing inputs read before audit: `CLAUDE.md`, `rules/query-and-synthesis.md`, full `rules/psp/metronome-ingest.md`, and `tracking/ingest/metronome/metronome-campaign-46/selection-review.md`.
- Final group verdict: **PASS — 4/4 questions retrieved through the required live wiki routes and verified against complete exact-raw reads.**
- Catalog timing: the two assigned sources are intentionally absent from the provider `## Sources` catalog pending aggregate close. This is nonblocking because both main-concept routes are live and purpose-fit; no direct provider-source-catalog shortcut was used.

## Page 1 — Get a contract v1

### Route and object/action match

`wiki/index.md:9` (`[[metronome-index]]`) → `wiki/metronome-index.md:285` (`[[metronome-customers-and-contracts]]`) → `wiki/concepts/metronome/metronome-customers-and-contracts.md:256` (`[[source-metronome-api-reference-contracts-get-a-contract-v1]]`) → `wiki/sources/metronome/source-metronome-api-reference-contracts-get-a-contract-v1.md` → `raw/metronome/api-reference/contracts/get-a-contract-v1-2026-08-28.md`.

**Requested object/action match:** yes. The reached source and raw are titled **Get a contract (v1)**, identify operation `getContract-v1`, and select one customer plus one contract. This is a single-contract read, not a customer-contract list or a v2 operation.

### Q1 — navigation

**Requested object/action:** retrieve one customer's specific contract through v1 rather than list that customer's contracts.

**Direct answer:** use bearer-authenticated `POST https://api.metronome.com/v1/contracts/get` (`getContract-v1`). Supply the customer and contract identities in the JSON payload.

**Exact evidence:** raw title/version boundary at lines 9–11; production server and bearer security at lines 23–27; operation, path and identity-purpose description at lines 88–98; source overview and route at lines 14–18 and 27–28.

**Verdict:** **PASS**.

### Q2 — version boundary and detail locators

**Requested object/action:** for that same v1 single-contract read, identify the version boundary and locate its contract selectors, optional expansions and returned contract detail.

**Direct answer:** this is explicitly the legacy **v1** get-contract endpoint; new clients are directed to implement the **v2** endpoint. Within a supplied JSON object, `customer_id` and `contract_id` are required UUID properties. Optional booleans `include_ledgers` and `include_balance` add commit-ledger and credit/commit-balance detail respectively; either may make the query slower. HTTP `200` places the selected object at `data`, which references `components.schemas.Contract` and its nested component schemas. The enclosing `requestBody` itself is not marked required, so omitted-body runtime behavior is not established by this page.

**Exact locators/evidence:**

- Version boundary: raw lines 9–11 and `paths./v1/contracts/get.post.description` at lines 92–96.
- Selectors and expansions: `paths./v1/contracts/get.post.requestBody.content.application/json.schema.required/properties`, raw lines 97–125.
- Success envelope: `paths./v1/contracts/get.post.responses.200.content.application/json.schema.properties.data`, raw lines 126–137.
- Returned detail entry point: `components.schemas.Contract`, raw lines 307–418; its `initial`, `current`, `amendments`, balance/ledger-bearing terms and other detail continue through referenced component schemas.
- Source coverage map: source lines 18–30.

**Verdict:** **PASS**.

## Page 2 — List all packages

### Route and object/action match

`wiki/index.md:9` (`[[metronome-index]]`) → `wiki/metronome-index.md:284` (`[[metronome-packages-and-aliases]]`) → `wiki/concepts/metronome/metronome-packages-and-aliases.md:38` (`[[source-metronome-api-reference-list-all-packages]]`) → `wiki/sources/metronome/source-metronome-api-reference-list-all-packages.md` → `raw/metronome/api-reference/list-all-packages-2026-08-28.md`.

**Requested object/action match:** yes. The reached source and raw identify `listPackages-v1` and enumerate reusable package definitions. Their purpose text explicitly sends package-associated contract lookup to the different `listContractsOnPackage` endpoint.

### Q3 — navigation

**Requested object/action:** list package definitions rather than contracts associated with one package.

**Direct answer:** use bearer-authenticated `POST https://api.metronome.com/v1/packages/list` (`listPackages-v1`). It returns package definitions and details; use the separate `listContractsOnPackage` operation only when the requested objects are the contracts associated with a specific package.

**Exact evidence:** raw purpose and object boundary at lines 9–11; production server and bearer security at lines 23–27; operation, path and repeated `listContractsOnPackage` distinction at lines 88–99; source overview at lines 14–19.

**Verdict:** **PASS**.

### Q4 — selection, pagination and returned-schema locators

**Requested object/action:** for that same package-definition list, locate package selection/pagination controls and the returned alias, duration and term schemas.

**Direct answer:**

- Package-state selection is optional body property `archive_filter` at `paths./v1/packages/list.post.requestBody.content.application/json.schema.properties.archive_filter`. It accepts archived, non-archived or all states (upper- and lowercase enum forms) and defaults to `NOT_ARCHIVED`; therefore the title “List all packages” does not mean archived packages are included by default.
- Pagination is in query parameters: `limit` references `components.parameters.PageLimit`, is bounded `1`–`100`, and the operation says it defaults to `10`; `next_page` references `components.parameters.NextPage` and is a string cursor.
- HTTP `200` requires `data` and nullable `next_page`; `data[]` references `components.schemas.Package`.
- Returned alias schedules are at `components.schemas.Package.properties.aliases` → `components.schemas.PackageAlias`; duration is at `components.schemas.Package.properties.duration` → `components.schemas.RelativeDate`. The returned reusable-term entry point is `components.schemas.Package`; follow its references to the named commit, credit, override, scheduled-charge, recurring commit/credit, threshold, spend-tracker and subscription component schemas rather than treating the source summary as a copied field inventory.

**Exact locators/evidence:**

- Operation, selection and default archive scope: raw lines 88–119.
- Response envelope: raw lines 120–137.
- Pagination definitions: `components.parameters.PageLimit` and `components.parameters.NextPage`, raw lines 220–235.
- Package entry point and term references: `components.schemas.Package`, raw lines 237–333.
- Alias and duration schemas: `components.schemas.PackageAlias`, raw lines 342–354; `components.schemas.RelativeDate`, raw lines 355–369.
- Principal term schema entry points: `CommitTemplate` at line 370, `CreditTemplate` at 450, `OverrideTemplate` at 505, `ScheduledChargeTemplate` at 563, `RecurringCommitTemplate` at 648, `RecurringCreditTemplate` at 677, `SpendThresholdConfiguration` at 689, `PrepaidBalanceThresholdConfiguration` at 718, `SpendTrackerTemplate` at 765 and `SubscriptionTemplate` at 787.
- Source coverage map and warning: source lines 18–29.

**Verdict:** **PASS**.

## Group gap sweep, complete reads and reverse links

- Complete exact raw reads: `raw/metronome/api-reference/contracts/get-a-contract-v1-2026-08-28.md` (3,458 lines) and `raw/metronome/api-reference/list-all-packages-2026-08-28.md` (1,684 lines).
- Gap sweep: content/filename searches across `raw/metronome` used the operation IDs, paths, page titles, expansion terms and `listContractsOnPackage`. Results included the selected raw files, their 2026-07-13 predecessors, aggregate OpenAPI/discovery artifacts, v2 and list-contract pages, the package-association page and the packages overview. No competing purpose-fit current raw or relevant conflict displaced either selected page.
- Extra full raw reads: **none**. The older same-canonical 2026-07-13 snapshots were not read because no question asks for historical differences and no relevant conflict required them. Distinct v2, contract-list, package-association, overview and aggregate artifacts were navigation/disambiguation results; the selected complete raw pages directly establish the requested object/action boundaries and answers.
- Reverse-link/route check: root index links `metronome-index` once; provider index links each selected main concept once; each main concept links its assigned source once in `## Sources`; each source reciprocally links its main concept once in `## Related`; and each `raw_files` value matches its one exact path-qualified `## Raw Sources` link. Both raw targets exist. No duplicate reciprocal route or wrong-object route was found.

## Final result

All four assigned questions pass. Retrieval failures: **none**. Wrong-object answers: **none**. Repairs or promotion requests: **none**. No repository file was edited and no semantic rereview was performed.


---

# Campaign 46 final retrieval audit — Group B (6 questions)

## Timing

- UTC analysis start: `2026-09-13T09:26:39Z`
- UTC analysis end: `2026-09-13T09:28:38Z`
- UTC artifact handoff: `2026-09-13T09:30:18Z`

## Create a package

**Route (Q1–Q2):** `wiki/index.md` -> `wiki/metronome-index.md` -> `wiki/concepts/metronome/metronome-packages-and-aliases.md` -> `wiki/sources/metronome/source-metronome-api-reference-contracts-create-a-package.md` -> `raw/metronome/api-reference/contracts/create-a-package-2026-08-28.md`.

### Q1 — Where create a reusable package of contract terms rather than provision a customer's contract?

- **Requested object/action:** create a reusable, customer-agnostic **Package** of contract terms, not provision a customer **Contract**. **Reached object/action:** exact match — `Create a package` (`createPackage-v1`), with custom negotiated customer terms explicitly directed to contract creation.
- **Direct answer:** Use bearer-authenticated `POST /v1/packages/create`. It creates reusable, time-relative terms layered on a rate card for consistent customer cohorts; use `createContract` instead for negotiated custom contract terms.
- **Exact evidence:** selected raw lines 9–16 define Package creation and reusable cohort terms; lines 24–29 distinguish packages from flexible customer-contract creation; lines 106–182 identify the POST path, purpose, operation ID, and request-schema route.
- **Verdict:** **PASS** — live retrieval reaches Package-template creation without confusing it with customer Contract provisioning.

### Q2 — How are relative dates and aliases used, and where are package inputs, restrictions and success details documented?

- **Requested object/action:** explain relative-date and alias behavior for **Package creation**, and locate creation inputs, restrictions, and success output. **Reached object/action:** exact match — the same create operation plus its `CreatePackagePayload` and supporting schemas.
- **Direct answer:** Package terms are relative to a future contract start: `starting_at_offset` generates a term's `starting_at`, `duration` generates its exclusive `ending_before` from that start, and `date_offset` represents a point-in-time date; supported units are days, weeks, months, and years. An alias is a human-readable substitute for package ID during contract provisioning. An alias belongs to only one package at a time; assigning it to a new package updates the original package's alias schedule and makes it resolve to the most recently assigned package. Inputs are under `components.schemas.CreatePackagePayload`; relative values and schedules are under `RelativeDate`, `RelativeScheduleDurationInput`, `RelativeSchedulePointInTimeInput`, and the relevant term-template schemas; alias fields are under `PackageAlias`. Restrictions are in `### Usage guidelines` and applicable nested schemas: packages are immutable, standard/self-serve rather than negotiated-custom terms, and configured billing-provider provisioning requires exactly one matching customer provider configuration. Success is at `paths./v1/packages/create.post.responses.200`, with created UUID at `data.id` via `components.schemas.Id`.
- **Exact evidence:** selected raw lines 18–29 state date, alias, provider-match, use-case, and immutability semantics; lines 188–202 document the `200` envelope/example; lines 213–304 locate package inputs; lines 328–355 define alias and relative-date schemas; lines 559–574, 830–840, and 871–948 show relative offsets, durations, and point-in-time schedule use.
- **Verdict:** **PASS** — semantics, consequential restrictions, exact schema locators, and success placement are all retrievable without copying the package's full field inventory.

## Get a package

**Route (Q3–Q4):** `wiki/index.md` -> `wiki/metronome-index.md` -> `wiki/concepts/metronome/metronome-packages-and-aliases.md` -> `wiki/sources/metronome/source-metronome-api-reference-packages-get-a-package.md` -> `raw/metronome/api-reference/packages/get-a-package-2026-08-28.md`.

### Q3 — Where inspect a specific package and its alias schedule rather than list packages?

- **Requested object/action:** retrieve one specific **Package** and inspect its alias schedule, not enumerate Package definitions. **Reached object/action:** exact match — `Get a package` (`getPackage-v1`) selected by Package UUID.
- **Direct answer:** Use bearer-authenticated `POST /v1/packages/get` with `package_id`. It returns one package's details and is explicitly intended for understanding that package's alias schedule or displaying its details.
- **Exact evidence:** selected raw lines 9–11 state the single-package purpose and alias-schedule use; lines 88–111 identify the POST path, operation ID, required-in-schema UUID selector, and example.
- **Verdict:** **PASS** — the route selects a single Package read, not the Package list operation.

### Q4 — Where are package selectors and returned alias, duration and term details documented, and what qualifications affect that read?

- **Requested object/action:** locate selector and returned-detail authority for the same single-**Package read**, including qualifications. **Reached object/action:** exact match — request schema plus `Package` response schema and its referenced term schemas.
- **Direct answer:** The selector is `paths./v1/packages/get.post.requestBody.content.application/json.schema`, where `package_id` is required within the JSON schema; the enclosing `requestBody` itself is not marked required. Success is `responses.200`, where required top-level `data` references `components.schemas.Package`; `404` routes through `components.responses.NotFound`. Returned alias and duration details are at `Package.aliases` -> `PackageAlias` and `Package.duration` -> `RelativeDate`; reusable terms branch from `Package` into commit, credit, override, scheduled-charge, recurring, threshold, spend-tracker, and subscription schemas. `aliases` and `duration` are optional Package properties and are absent from the success example, so this page does not guarantee either on every read; optional `Package.archived_at` is the archive-state timestamp locator when present.
- **Exact evidence:** selected raw lines 98–123 document selector and success placement; lines 124–193 show an example without aliases or duration; lines 194–195 document not-found; lines 198–294 define required versus optional Package properties and all term routes; lines 303–330 define alias schedule fields and duration units.
- **Verdict:** **PASS** — the requested detail is discoverable and the optionality/omitted-body/not-found qualifications are preserved.

## Update the rate card products order

**Route (Q5–Q6):** `wiki/index.md` -> `wiki/metronome-index.md` -> `wiki/concepts/metronome/metronome-products-and-rate-cards.md` -> `wiki/sources/metronome/source-metronome-api-reference-rate-cards-update-the-rate-card-products-order.md` -> `raw/metronome/api-reference/rate-cards/update-the-rate-card-products-order-2026-07-13.md`.

### Q5 — Where move selected rate-card products relative to current positions for invoice presentation?

- **Requested object/action:** move selected **Rate Card Products** relative to their current positions to control invoice presentation, not replace the entire Rate Card product order. **Reached object/action:** exact match — `Update the rate card products order` (`moveRateCardProducts-v1`).
- **Direct answer:** Use bearer-authenticated `POST /v1/contract-pricing/rate-cards/moveRateCardProducts`. The operation moves specific products relative to their current locations, and Rate Card ordering determines their order on customer invoices.
- **Exact evidence:** selected raw lines 9–11 state invoice-presentation effect and relative-move behavior; lines 88–111 identify the POST path, operation ID, and move example.
- **Verdict:** **PASS** — the route reaches the relative selected-product move operation rather than the separate full-order setter.

### Q6 — What movement/placement behavior is documented, and where are target, movement inputs and success response located?

- **Requested object/action:** explain placement behavior and locate the target Rate Card, per-product move inputs, and success response for the same relative move. **Reached object/action:** exact match — `MoveRateCardProductsPayload` and the operation's `200` response.
- **Direct answer:** Each requested product is moved to a zero-based new position relative to the current Rate Card ordering, which controls customer-invoice display. `components.schemas.MoveRateCardProductsPayload` requires `rate_card_id` and `product_moves`; each move item requires `product_id` and numeric `position`, with `position >= 0`. Success is `paths./v1/contract-pricing/rate-cards/moveRateCardProducts.post.responses.200.content.application/json.schema`: top-level `data` is required and references generic `components.schemas.Id`; the example repeats the Rate Card UUID at `data.id`, although the generic schema does not independently label the ID's object type. The enclosing `requestBody` is not marked required, so omitted-body runtime behavior is not established here.
- **Exact evidence:** selected raw lines 93–111 document relative movement and the zero-based example; lines 99–104 show the request-body/schema route without `required: true`; lines 112–126 document success placement; lines 137–162 define target and move-item requirements.
- **Verdict:** **PASS** — movement semantics, exact inputs, placement indexing, and success route are all retrievable.

## Shared group checks

- **Selected full reads:** `create-a-package-2026-08-28.md` (1,769 lines), `get-a-package-2026-08-28.md` (1,659 lines), and `update-the-rate-card-products-order-2026-07-13.md` (190 lines); all read completely.
- **Gap sweep:** filename and content searches under `raw/metronome/` covered create/get Package wording, aliases/alias schedules, relative package dates, `moveRateCardProducts`, and relative Rate Card product movement. The three promoted source pages contain no `## Related raw API references` section. The sweep found older same-canonical `create-a-package-2026-07-13.md` and `get-a-package-2026-07-13.md`, plus neighboring package overview/list/archive/association and full-order-set material. None was read: the questions do not ask for history/version differences, the selected current raws directly establish the requested Package behavior, the selected move raw directly distinguishes relative movement, and no relevant conflict requiring investigation was discovered. No external fetch, ingestion, or extra full read occurred.
- **Reciprocal/navigation checks:** root index links `metronome-index`; provider index links both main concepts and all three target sources; each main concept links its target source(s); every target source links back to its main concept and links the exact path-qualified selected raw named in `raw_files`. **PASS.**
- **Completeness:** Q1–Q6 only; three routes recorded once, six object/action checks, six direct answers, six exact-evidence blocks, and six verdicts present.

## Group result

**PASS — 6/6 questions.** No retrieval repair, wrong-object rerun, extra authority read, or material evidence uncertainty is required.
