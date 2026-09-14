# Campaign 43 final query quality audit

Verdict: PASS — 10/10 predetermined questions, no query-driven source repair. Coordinator checked requested versus reached object/action for each answer. One disjoint audit, Q1–Q6 and Q7–Q10, followed actual root/provider/concept/source/raw routes. All five selected raw pages were read fully; the gap sweep required no extra historical or adjacent full reads. This does not establish equivalence of unread versions.

Independent reports follow verbatim. Each page records its route once with two separately scored answers; no additional full-content audit was run.

---

# Campaign 43 final query audit — Group A (Q1–Q6)

- Analysis started (UTC): `2026-09-10T10:17:38Z`
- Analysis ended (UTC): `2026-09-10T10:21:04Z`
- Handoff (UTC): `2026-09-10T10:22:34Z`
- Scope: three promoted pages; six predetermined questions; repository and tracking remained read-only.

## Route block 1 — Add a rate

Actual route: `wiki/index.md:9` → `wiki/metronome-index.md:273` (`[[metronome-products-and-rate-cards]]`) → `wiki/concepts/metronome/metronome-products-and-rate-cards.md:150` → `wiki/sources/metronome/source-metronome-api-reference-rate-cards-add-a-rate.md` → `raw/metronome/api-reference/rate-cards/add-a-rate-2026-07-13.md`.

### Q1 — Where add one rate to a rate card rather than create a rate card?

- Object/action match: **one product rate / add to an identified existing rate card**; this is not rate-card creation.
- Direct requested answer: use bearer-authenticated `POST /v1/contract-pricing/rate-cards/addRate`. The page identity is “Add a rate,” and `AddRatePayload` identifies both the rate card to update and the product whose rate is added.
- Exact evidence: raw lines `9–13` (page purpose and warning), `20`, `90–103` (operation path, method, summary, and operation ID), and `144–160` (payload target meanings).
- Verdict: **PASS** — the prescribed route selects the correct single-rate action and reaches complete exact raw evidence.

### Q2 — What warning affects single vs bulk addition, and where are rate configuration fields and the success response documented?

- Object/action match: **single-versus-bulk rate addition / operation-selection warning plus detail locators**; this is not a request for a field inventory.
- Direct requested answer: the singular endpoint is **heavily rate limited**; for multiple rates, Metronome strongly encourages the bulk `addRates` endpoint. Rate configuration fields are documented at `components.schemas.AddRatePayload` (with specialized minimum behavior at `components.schemas.MinimumConfig`). The success response is documented at `paths./v1/contract-pricing/rate-cards/addRate.post.responses.200.content.application/json`; its required `data` routes to `components.schemas.RateWithCommitRate`.
- Exact evidence: raw lines `13` and `99–102` (warning and bulk route), `118–130` (success response placement), `144–152` (payload schema), `289–293` (returned rate schema), and `410–420` (minimum configuration behavior).
- Verdict: **PASS** — the warning and both requested locators are directly recoverable without expanding into unrelated schema detail.

## Route block 2 — Update a rate card

Actual route: `wiki/index.md:9` → `wiki/metronome-index.md:273` (`[[metronome-products-and-rate-cards]]`) → `wiki/concepts/metronome/metronome-products-and-rate-cards.md:71` → `wiki/sources/metronome/source-metronome-api-reference-rate-cards-update-a-rate-card.md` → `raw/metronome/api-reference/rate-cards/update-a-rate-card-2026-08-28.md`.

### Q3 — Where update rate-card configuration rather than underlying pricing rates?

- Object/action match: **rate-card configuration / update**; this is not an underlying product-price or rate-schedule mutation.
- Direct requested answer: use bearer-authenticated `POST /v1/contract-pricing/rate-cards/update`. The page expressly says the endpoint updates rate-card configuration and does not affect underlying pricing rates or schedules.
- Exact evidence: raw lines `9–17` (purpose and supported configuration categories), `42`, and `112–120` (operation and explicit underlying-pricing boundary).
- Verdict: **PASS** — the route clearly separates rate-card configuration from pricing-rate changes.

### Q4 — How do alias changes affect existing vs newly provisioned contracts, and where are editable fields documented?

- Object/action match: **rate-card alias change / contract-selection effect plus update-field locator**; this is not a contract migration or rate edit.
- Direct requested answer: already-created contracts remain on their originally assigned rate cards. New contracts that use `rate_card_alias` resolve the alias at provisioning time; after a scheduled alias transition, newly provisioned contracts using that alias reference the new card. Editable fields are documented at `paths./v1/contract-pricing/rate-cards/update.post.requestBody` → `components.schemas.UpdateRateCardPayload`; alias effective-date detail is under `components.schemas.RateCardAlias`.
- Exact evidence: raw lines `19–35` (existing-contract continuity and new-contract resolution/cutover), `138–181` (same behavior in the operation description), `183–190` (request-body locator), `220–249` (update schema), and `265–277` (alias schema locator).
- Verdict: **PASS** — both contract cohorts and the requested editable-field locator are explicit.

## Route block 3 — Archive an offset notification configuration

Actual route: `wiki/index.md:9` → `wiki/metronome-index.md:281` (`[[metronome-alerts-and-notifications]]`) → `wiki/concepts/metronome/metronome-alerts-and-notifications.md:92` → `wiki/sources/metronome/source-metronome-api-reference-notifications-archive-an-offset-lifecycle-event-notification-configuration.md` → `raw/metronome/api-reference/notifications/archive-an-offset-lifecycle-event-notification-configuration-2026-07-13.md`.

### Q5 — Where archive offset configuration rather than edit it or send an event?

- Object/action match: **offset lifecycle-event notification configuration / archive**; this is neither configuration editing nor event generation or sending.
- Direct requested answer: use bearer-authenticated `POST /v2/notifications/archive`, operation `archiveNotificationConfig-v2`.
- Exact evidence: raw lines `9–18` (page identity, archive purpose, and operation), `88–102` (method, summary, operation ID, and request-body route).
- Verdict: **PASS** — the route lands on the configuration-archive operation with the correct object and action.

### Q6 — What processing effect is documented, and where are target identification and returned state defined?

- Object/action match: **archived offset-notification configuration / processing effect, selector, and returned configuration state**; this is not proof of canceling an already-generated delivery.
- Direct requested answer: the documented effect is that archived notifications are **not processed**. The target configuration is identified at `components.schemas.ArchiveNotificationConfigPayload.id`. Returned state is defined at `paths./v2/notifications/archive.post.responses.200.content.application/json.data` → `components.schemas.LifecycleEventOffsetNotificationConfig`. Boundary: the page does not define effect timing or treatment of already-generated, queued, in-flight, retried, or delivered work; moreover, the success example shows `archived_at: null` while the schema permits a nullable archive timestamp, so the returned archive timestamp remains a documentation tension.
- Exact evidence: raw lines `11`, `92–117` (effect and success schema route), `118–129` (success example), `164–175` (target ID), and `175–217` (returned configuration schema and nullable `archived_at`).
- Verdict: **PASS** — the requested effect and locators are recoverable, with the material delivery/timestamp uncertainty preserved rather than overclaimed.

## Shared gap sweep, extra full reads, and reciprocal checks

- Gap sweep: searched the Metronome raw rate-card and notification paths by topic and operation text. It surfaced the bulk `add-rates` page, adjacent create/edit/get/list/system-notification pages, and the older `update-a-rate-card-2026-07-13.md` same-canonical snapshot. The three selected source summaries contain no `## Related raw API references` section.
- Extra full reads: **none**. The selected exact raw pages directly answered all six questions. The bulk page was not needed because Q2 asks for the single-page warning and destination, both explicit in the selected raw; adjacent notification pages were not needed because the archive page itself defines archive identity, processing effect, selector, and returned schema; the older update snapshot was not read because no question asks for history/version comparison and no relevant conflict required it. No historical equivalence or absence of change was inferred.
- Fully read selected evidence: `raw/metronome/api-reference/rate-cards/add-a-rate-2026-07-13.md` (513 lines), `raw/metronome/api-reference/rate-cards/update-a-rate-card-2026-08-28.md` (301 lines), and `raw/metronome/api-reference/notifications/archive-an-offset-lifecycle-event-notification-configuration-2026-07-13.md` (242 lines).
- Reciprocal/navigation checks: **PASS**. Root index → Metronome index; Metronome index → both concept hubs; concept → each promoted source (supported inline citation or Sources entry); each source → its concept; and each source → its exact raw path are all present. The provider catalog's direct per-source aggregation is not required for these actual concept-led routes and was not used as a shortcut.

## Group result

`Q1 PASS · Q2 PASS · Q3 PASS · Q4 PASS · Q5 PASS · Q6 PASS`

Completeness: three route blocks, six distinct object/action checks, six direct answers, exact raw evidence for every answer, one shared gap/extra-read/reciprocal section, and no repository or tracking writes.

---

# Campaign 43 final query audit — Group B (Q7–Q10)

## Timing (UTC)

- audit_started_at: `2026-09-10T10:18:06Z`
- analysis_ended_at: `2026-09-10T10:20:07Z`
- handoff_at: `2026-09-10T10:21:26Z`

## Page route 1 — Customer Plan price adjustments

`wiki/index.md` → `wiki/metronome-index.md` → `wiki/concepts/metronome/metronome-customers-and-contracts.md` → `wiki/sources/metronome/source-metronome-api-reference-plans-get-the-plan-adjustments-for-a-customer.md` → `raw/metronome/api-reference/plans/get-the-plan-adjustments-for-a-customer-2026-07-13.md`

- Selected raw read completely: 236 lines.
- SHA-256: `2b5252b77e27cf2d1a541fa945fd32927f7c226a488a02ae1d2aff869864ae1c`.

### Q7 — Where retrieve a specific customer Plan's price adjustments rather than Contract pricing?

- Object/action match: **MATCH** — this is a read of price adjustments for one legacy customer–Plan relationship, not a Contract or rate-card pricing read.
- Requested answer: Use bearer-authenticated `GET https://api.metronome.com/v1/customers/{customer_id}/plans/{customer_plan_id}/priceAdjustments`. The `customer_plan_id` selects the customer–Plan relationship, not the catalog Plan.
- Exact evidence: raw lines 9–11 name the operation, its Plans-deprecated scope, and Contracts direction; lines 18 and 23–27 establish the OpenAPI path, `/v1` production server, and bearer authentication; lines 92–107 define the GET and its parameter references; lines 148–164 define required UUID `customer_id` and required UUID `customer_plan_id`, explicitly describing the latter as “the ID of a customer-plan relationship.”
- Verdict: **PASS** — the promoted route reaches the exact raw and answers the requested locator without substituting Contract pricing.

### Q8 — What deprecation boundary applies, and where are request selectors and adjustment response details documented?

- Object/action match: **MATCH** — this asks about the same legacy customer-Plan adjustment-read operation, its migration boundary, and its request/response documentation, not a current Contract mutation.
- Requested answer: It is a deprecated Plans endpoint; new clients are directed to Contracts, but this page names no replacement Contract operation or Plan/customer-plan mapping. Request selectors are documented at `## OpenAPI` → `/customers/{customer_id}/plans/{customer_plan_id}/priceAdjustments` → `get.parameters`, with definitions in `components.parameters.CustomerId` and `components.parameters.CustomerPlanId` (pagination in `PageLimit` and `NextPage`). Adjustment response details are documented at the GET operation's `responses.200.content.application/json.schema`, then `components.schemas.PriceAdjustment` and `components.schemas.ChargeType`.
- Exact evidence: raw lines 11 and 97–102 state the deprecation and Contracts direction; lines 103–107 and 148–180 locate the request selectors and pagination parameters; lines 108–145 locate the `200` envelope/example; lines 182–230 contain the `PriceAdjustment` and `ChargeType` schemas. Neither the page introduction nor the full OpenAPI operation identifies a replacement Contract route or migration mapping.
- Verdict: **PASS** — the source preserves the deprecation boundary and supplies exact raw schema locators without copying an unrelated schema inventory.

## Page route 2 — Delete selected custom-field values

`wiki/index.md` → `wiki/metronome-index.md` → `wiki/concepts/metronome/metronome-custom-fields.md` → `wiki/sources/metronome/source-metronome-api-reference-custom-fields-delete-custom-fields.md` → `raw/metronome/api-reference/custom-fields/delete-custom-fields-2026-07-13.md`

- Selected raw read completely: 160 lines.
- SHA-256: `994543f4191b3314347139ee1a83c3f60208bca242219b43850a95143e831a9b`.

### Q9 — Where remove selected custom-field values from an entity rather than delete field definitions?

- Object/action match: **MATCH** — this is deletion of selected values on one entity instance, not removal of custom-field key definitions from the entity-type allowlist.
- Requested answer: Use bearer-authenticated `POST https://api.metronome.com/v1/customFields/deleteValues`. It removes values for specified keys from one entity instance while preserving that instance's other custom fields.
- Exact evidence: raw lines 9–11 state selected-value removal and preservation of other fields; lines 18 and 23–27 establish the POST path, production server, and bearer authentication; lines 88–99 define the operation and repeat its entity-instance/selected-key effect.
- Verdict: **PASS** — the promoted route selects the value-level operation and makes the object/action boundary discoverable.

### Q10 — What identifies the deletion target and selected keys, what is preserved, and where is the request schema documented?

- Object/action match: **MATCH** — the target is one entity instance plus selected field keys; this is neither entity deletion nor key-definition removal.
- Requested answer: Required payload properties `entity` and UUID `entity_id` identify the target entity instance; required array `keys` identifies the values to remove. Other custom fields on the same entity are preserved. The request contract is at `## OpenAPI` → `/v1/customFields/deleteValues` → `post` → `requestBody` → `content.application/json.schema`; exact entity choices are at `components.schemas.ManagedEntity`.
- Exact evidence: raw lines 93–99 state the target, selected-key action, and preservation; lines 100–124 document the request body, required selectors, property shapes, and example; lines 128–154 locate the managed-entity enum.
- Verdict: **PASS** — the route answers the requested target/key semantics and gives the exact request-schema locator.

## Shared gap sweep, extra reads, and reciprocal checks

- Gap sweep: searched `raw/metronome/` filenames and content for Plan/price-adjustment terms, the exact adjustment path/operation ID, custom-field deletion terms, `deleteValues`, and its operation ID. The two selected canonical raw pages were the only page-level exact-operation matches. Broad custom-field overview/key-management pages and OpenAPI/discovery artifacts were navigation or adjacent authority, not necessary evidence for these four questions. No material conflict was discovered.
- Extra full reads: none. Q7–Q10 ask current contents and locators from the selected snapshots, not history or version differences; the fully read exact raws answered every requested point, and no relevant conflict required an older same-canonical snapshot or adjacent page.
- Reciprocal checks: `wiki/metronome-index.md` contains both promoted source entries and both concept routes. `metronome-customers-and-contracts.md` links the Plan-adjustments source in its Sources section, and that source links back to the concept as Primary concept. `metronome-custom-fields.md` links the delete-values source in its entity-scope section, and that source links back as Main concept. Each source's `raw_files` and `## Raw Sources` route resolves to the exact fully read raw above.
- Group verdict: **PASS (Q7–Q10 all PASS; no repair required).**
