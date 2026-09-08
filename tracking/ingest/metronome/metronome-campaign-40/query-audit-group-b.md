# Campaign 40 final retrieval audit — Group B

## Timing and gate

- Audit start (UTC, explicitly observed): `2026-09-08T13:45:05Z`
- Avalara promotion wait: yes. Plans Q7–Q8 were completed first and readiness was reported to the coordinator. Avalara navigation did not begin until the coordinator confirmed approved concept/source promotion at `2026-09-08T13:49:35Z`. The readiness instant was not separately sampled, so no wait duration is claimed.
- Audit end (UTC, explicitly observed after report verification): `2026-09-08T13:53:52Z`

This was one final retrieval audit, not a new source-approval review. Repository content was treated as read-only. No manifest, selection, order, receipt, or prior attempt was used as a retrieval shortcut.

## Q7 — Where can a caller inspect customers attached to a legacy Plan, and what is recommended for new clients?

**Actual route**

`wiki/index.md` → `wiki/metronome-index.md` → `wiki/concepts/metronome/metronome-customers-and-contracts.md` (`Deprecated Plans listing boundary`) → `wiki/sources/metronome/source-metronome-api-reference-plans-list-customers-on-a-plan.md` → `raw/metronome/api-reference/plans/list-customers-on-a-plan-2026-07-13.md`

**Evidence and answer**

- Use bearer-authenticated `GET https://api.metronome.com/v1/planDetails/{plan_id}/customers` to list customers associated with one legacy Plan.
- The operation is explicitly a deprecated Plans endpoint. New clients are directed to implement using Contracts.
- Neither the exact raw nor its promoted source identifies a replacement Contracts operation, Plan-to-Contract identity or field mapping, migration procedure, compatibility period, or removal date; no replacement should be inferred.
- Exact raw locators: `paths./planDetails/{plan_id}/customers.get` for operation/deprecation wording and `components.parameters.PlanId` for the Plan identifier.

**Search/gap sweep**

- Exact endpoint/title/schema sweep terms: `planDetails/{plan_id}/customers`, `list customers on a plan`, `past customers of the plan`, and `CustomerAndPlanDetail`.
- The only matching raw for those exact endpoint/response terms was the selected raw snapshot. A broader legacy-Plans deprecation sweep found adjacent reverse-direction customer-plan history and other Plans operations, but none was needed to answer this Plan-to-customers question.

**Verdict: PASS.** The index-led route selects the correct source and exact raw, and the answer preserves the deprecated/current-authority boundary.

## Q8 — Which identifier, active/past scope, and pagination controls apply, and where is the returned customer structure defined?

**Actual route**

Same route and exact raw as Q7.

**Evidence and answer**

- Identifier: required path parameter `plan_id`, schema type string with `format: uuid`.
- Scope filter: optional query `status`, default `active`. The description defines `active` as current customers, `ended` as past customers, `upcoming` as upcoming customers, and `all` as current, past, and upcoming customers.
- The description permits comma-OR values such as `active,ended`, but says `ended,upcoming` is not yet supported. The published scalar enum lists only `all`, `active`, `ended`, and `upcoming`, so combined strings conflict with the schema and should be reported as a documentation conflict rather than normalized away.
- Pagination: optional query `limit` from 1 through 100 and optional query cursor `next_page`; HTTP 200 requires a top-level `data` array and nullable sibling `next_page`.
- Returned structure: each `data[]` item references `components.schemas.CustomerAndPlanDetail`, which requires `customer_details` and `plan_details`. Field detail is under `CustomerDetail` and `CustomerPlanDetail`; nested customer configuration/custom fields/status are under `CustomerConfig`, `CustomField`, and `BillableStatus`. The worked placement is also visible at `paths./planDetails/{plan_id}/customers.get.responses.200`.
- `CustomerDetail` requires `external_id`, `id`, `name`, `created_at`, `updated_at`, `customer_config`, `ingest_aliases`, and `custom_fields`; `archived_at` and configuration-dependent `current_billable_status` are optional. `CustomerPlanDetail` requires `id`, `name`, `custom_fields`, `starting_on`, and `customer_plan_id`, with nullable optional `ending_before`.

**Search/gap sweep**

- The same exact-topic sweep as Q7 located no additional raw authority needed for the identifier, status, pagination, envelope, or component-schema answer.

**Verdict: PASS.** Specific values and schema placement were verified in the fully read raw, including the status-description/schema conflict.

## Q9 — Where is the Avalara credential-setting operation, and which invoicing workflow does it support?

**Actual route**

`wiki/index.md` → `wiki/metronome-index.md` → `wiki/concepts/metronome/metronome-integrations.md` (`Avalara tax-app boundary`) → `wiki/sources/metronome/source-metronome-api-reference-settings-upsert-avalara-credentials.md` → `raw/metronome/api-reference/settings/upsert-avalara-credentials-2026-07-13.md`

The provider source catalog appeared during the coordinator's aggregate close work, but the route was selected through the provider index's main `metronome-integrations` concept as required.

**Evidence and answer**

- Use bearer-authenticated `POST https://api.metronome.com/v1/upsertAvalaraCredentials` (`operationId: upsertAvalaraCredentials-v1`).
- The request object requires `delivery_method_ids`, `avalara_environment`, `avalara_username`, and `avalara_password`; `avalara_environment` is `PRODUCTION` or `SANDBOX`. Optional `commit_transactions` controls whether Metronome tax calculations are committed for reporting and tax filings.
- At this snapshot, these credentials are documented as being used only for **PLG Invoicing**.
- This source does not establish that the credential flow is the same as the separate Stripe-hosted Avalara tax-app workflow.
- The corrected error locator is accurate: HTTP 400 references `#/components/schemas/Error`, whose body schema is defined under `components.schemas.Error`; HTTP 404 uses the `NotFound` response reference.

**Search/gap sweep**

- Exact-topic sweep terms: `upsertAvalaraCredentials`, `Avalara credentials`, and `PLG Invoicing`.
- Only the selected Avalara credential raw matched those exact terms. The separate Avalara integration guide concerns the Stripe-hosted tax-app workflow and was not substituted for this credential-operation authority.

**Verdict: PASS.** The main concept and source route directly retrieve the operation and its qualified PLG Invoicing scope without conflating Avalara workflows.

## Q10 — How do the credentials associate billing entities, and where are delivery-method IDs obtained?

**Actual route**

Primary route: same route and exact Avalara raw as Q9.

Targeted supporting route for the ID-producing operation: `wiki/concepts/metronome/metronome-integrations.md` (`Account-level provider enumeration`) → `wiki/sources/metronome/source-metronome-api-reference-settings-list-account-level-billing-providers.md` → `raw/metronome/api-reference/settings/list-account-level-billing-providers-2026-07-13.md` (fully read).

**Evidence and answer**

- The Avalara request supplies `delivery_method_ids`; Metronome maps the supplied credentials to the appropriate billing entities through those selected billing-provider delivery methods.
- Obtain the IDs from the response of bearer-authenticated `POST /v1/listConfiguredBillingProviders`.
- The provider-list response requires `data`; every `data[]` item requires `billing_provider`, UUID `delivery_method_id`, `delivery_method`, and `delivery_method_configuration`. The operation enumerates account-level provider delivery methods; enumeration alone does not prove a customer or contract currently selects the returned configuration or that downstream delivery will succeed.

**Search/gap sweep**

- A `listConfiguredBillingProviders` raw sweep found the account-level provider-list raw plus cross-references from the Avalara raw, Anrok raw, and two dated Stripe-integration raws.
- The account-level provider-list raw was read completely because Q10 asks where the IDs are obtained and the Avalara raw names the response but does not itself define that operation's method or response schema. The Anrok and Stripe pages were not needed for the Avalara mapping answer.

**Verdict: PASS.** The answer is reachable from the promoted source and its exact raw; the targeted extra raw closes the method/response-detail gap without broadening the claim.

## Route integrity and concrete failures

- Plans reciprocal route: the source links once to `[[metronome-customers-and-contracts]]`; the concept's intended `Deprecated Plans listing boundary` section has one supported inline citation back to the source. That inline citation is the reciprocal route and is not a duplicate catalog entry.
- Avalara reciprocal route: the source links once to main concept `[[metronome-integrations]]`; that concept's intended `Avalara tax-app boundary` section has one supported inline citation back to the source. The source also links once to supporting route `[[metronome-invoicing]]`, whose Sources section contains one reciprocal source entry.
- Both source pages' `raw_files` entries and `## Raw Sources` links resolve to the exact fully read raw snapshots.
- Provider and company source catalogs contain one entry per audited promoted source after aggregate close updates; no duplicate entry was found.
- Concrete retrieval failures: none.
- Repairs required by this final audit: none.
- Final verdict: **4/4 PASS**.
