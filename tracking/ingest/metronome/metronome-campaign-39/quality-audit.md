# Campaign 39 — final retrieval audit

Overall verdict: **PASS — 10/10** predetermined questions. Group A covered six questions; Group B covered the other four in two non-overlapping pairs as sources became available. No task was repeated by the coordinator. All five detail raws were read completely by their assigned auditor.

All intended index → concept → source → exact raw routes passed, including reciprocal navigation and purpose fit. Auditors performed supplementary filename/phrase gap sweeps under the existing query rules; these are not zero-search results. No extra raw was needed as factual evidence and no broken route required repair. The self-timed audit intervals below exclude some startup, report verification and delivery latency.

Group A's suggestion to move a secondary Plan migration link is nonblocking. Keep the already approved, purpose-labelled route in this campaign; no extra content rewrite is required. Provider-index descriptions were enriched during normal close aggregation for discounts, billing-configuration lookup, legacy Plan charges, and Anrok configuration. Index descriptions remain navigation, not factual authority. Evidence line numbers are audit-time snapshots and may shift after aggregation.

# Campaign 39 Final Retrieval Audit — Group A

- Started (UTC): 2026-09-08T10:18:48Z
- Completed (UTC): 2026-09-08T10:21:53Z
- Scope: six retrieval tasks in three page pairs; retrieval audit only, not a second semantic review.
- Evidence policy followed: began at `wiki/index.md`, used the Metronome provider index and purpose-fit concept, then the promoted source and its exact current raw; did not use manifests, attempts, tracking, logs, or historical raw versions as evidence. All three selected raw files were read in full (426 + 297 + 275 lines).

## Overall verdict

**PASS — 6/6 tasks.** Each intended route exists, is semantically appropriate, and occurs once in its intended section; each promoted source links back once to its intended main concept. Secondary supporting/migration-context links are role-labelled and do not duplicate the intended section route.

## 1. Where can I compare ways to offer discounts on a commitment?

**Verdict: PASS**

- Route: `wiki/index.md` `## PSP Indexes` → `[[metronome-index]]` (line 9) → `wiki/metronome-index.md` `## Concepts` → `[[metronome-credits-and-commits]]` (line 242) → `wiki/concepts/metronome/metronome-credits-and-commits.md` `## Enterprise commitment structure` → `[[source-metronome-guides-pricing-packaging-apply-credits-and-commits-discounting-on-commits]]` (line 14) → `raw/metronome/guides/pricing-packaging/apply-credits-and-commits/discounting-on-commits-2026-07-13.md`.
- Answer evidence: the raw guide `# Offer discounts on commits` names two primary methods—reduce commit cost basis and create commit-specific contract overrides—and an advanced third method, encode commit rates on a rate card (raw lines 9–18). The promoted source summarizes this comparison at lines 12–20 and links the exact raw at line 39.
- Route integrity: the intended concept-to-source link occurs once in `## Enterprise commitment structure`; the source-to-main-concept backlink `[[metronome-credits-and-commits]]` occurs once in `## Related` (source line 34). The separate `metronome-products-and-rate-cards` supporting link is semantically appropriate to the third method and is explicitly labelled supporting, not the intended route for this question.
- Extra searches: exact source-link search across `wiki/metronome-index.md` and `wiki/concepts/metronome/` found the intended credits-and-commits route plus one purpose-specific rate-card supporting route; filename sweep found exactly the promoted current raw for this guide. A narrow raw phrase sweep found related implementation references, but none is a better comparison guide.

## 2. How does the guide distinguish reduced cost basis, commit-specific overrides, and commit rates?

**Verdict: PASS**

- Route: same complete route as task 1.
- Answer evidence:
  - Reduced cost basis grants more accessible spend than is invoiced (example: $10,000 access for an $8,000 invoice). It is for prepaid commits with a uniform percentage discount; usage-statement prices do not show the discount, and it is unsuitable for postpaid commits because their invoice and access amounts must match (raw lines 20–69).
  - Commit-specific overrides change rates while a balance is being consumed. They can be multiplier, overwrite, or tiered; can target all commits/credits or selected commit/credit IDs; can select line items by product IDs, tags, pricing groups, or presentation groups; and commit-specific overwrite/multiplier classes precede the corresponding non-commit-specific classes (raw lines 71–93).
  - Commit rates are reusable rate-card pricing for customers who commit, avoiding per-customer override setup. They are usage-product-only, must accompany a list rate in the same pricing unit, can be tiered without resetting tier quantity when switching rates, and fall back to the list rate plus list-rate-targeting overrides when a product lacks a commit rate. A contract can further discount a commit rate with a commit-specific override (raw lines 231–268).
- Route integrity: source summary locators at lines 27–29 point to all three raw sections without replacing the raw evidence; the main concept backlink is unique as recorded in task 1.
- Extra searches: scoped searches for `cost basis`, `commit-specific override`, and `commit rate` surfaced neighboring create/edit/rate-card documents, but the assigned guide is the only promoted page that directly compares all three methods; no unrelated concept was needed.

## 3. Where can I retrieve an existing customer billing-provider configuration for contract provisioning?

**Verdict: PASS**

- Route: `wiki/index.md` → `[[metronome-index]]` (line 9) → `wiki/metronome-index.md` `## Concepts` → `[[metronome-customers-and-contracts]]` (line 247) → `wiki/concepts/metronome/metronome-customers-and-contracts.md` `## Sources` → `[[source-metronome-api-reference-customers-fetch-billing-provider-configurations-for-a-customer]]` (line 253) → `raw/metronome/api-reference/customers/fetch-billing-provider-configurations-for-a-customer-2026-08-28.md`.
- Answer evidence: use bearer-authenticated `POST /v1/getCustomerBillingProviderConfigurations`. The page expressly says it returns previously set customer billing configurations for contract provisioning (raw lines 9–18 and 87–98). The promoted source states the same retrieval boundary at lines 12–18 and links the exact 2026-08-28 raw at line 38.
- Route integrity: the concept-to-source link appears once in the intended `## Sources` section; the source-to-main-concept backlink `[[metronome-customers-and-contracts]]` appears once in `## Related` (source line 34).
- Extra searches: endpoint/field search across current Metronome guide and API raw files also found create-contract and edit-contract consumers plus an older 2026-07-13 capture of this endpoint. Per audit rules, those were not used as answer evidence; the promoted source selects the exact 2026-08-28 raw.

## 4. Which request identifier selects customer, and where does response expose configuration identity used for contract billing?

**Verdict: PASS**

- Route: same complete route as task 3.
- Answer evidence: within a supplied JSON object, required `customer_id` is the UUID selecting the customer; optional `include_archived` is also documented (raw lines 99–114). HTTP 200 returns required top-level `data`, an array of `CustomerBillingProviderConfiguration` objects (raw lines 115–148). Each object’s required UUID `id` is explicitly the configuration identity that can be passed as `billing_provider_configuration_id` when creating a contract (raw lines 155–174). `archived_at` is required but nullable, so callers should inspect it rather than assume every result is active (raw lines 159–167 and 200–203).
- Route integrity: request and response locators are correctly surfaced by the promoted source at lines 25–29; the source/raw and reciprocal main-concept routes are unique as recorded in task 3.
- Extra searches: a scoped search for `getCustomerBillingProviderConfigurations` and `billing_provider_configuration_id` found downstream contract consumers but no competing customer-configuration lookup route. The separate account-level `delivery_method_id` and provider-specific IDs were not substituted for the returned customer configuration `id`.

## 5. Where can I inspect charges on a legacy plan, and is this recommended API family for new clients?

**Verdict: PASS**

- Route: `wiki/index.md` → `[[metronome-index]]` (line 9) → `wiki/metronome-index.md` `## Concepts` → `[[metronome-products-and-rate-cards]]` (line 245) → `wiki/concepts/metronome/metronome-products-and-rate-cards.md` `## Sources` → `[[source-metronome-api-reference-plans-list-plan-charges]]` (line 148) → `raw/metronome/api-reference/plans/list-plan-charges-2026-07-13.md`.
- Answer evidence: use bearer-authenticated `GET /v1/planDetails/{plan_id}/charges` (the raw OpenAPI server is `https://api.metronome.com/v1` and path is `/planDetails/{plan_id}/charges`). This is a deprecated Plans endpoint; new clients should implement with Contracts. The page does not name a replacement Contract operation or establish a Plan-to-Contract mapping (raw lines 9–18 and 91–104; promoted source lines 14–21).
- Route integrity: the intended source occurs once in `metronome-products-and-rate-cards.md` `## Sources`; the source links once to that main concept (source line 33). Its separately labelled migration-context backlink and the customers/contracts source-list route are semantically appropriate to the deprecation boundary rather than a second intended product/charge route.
- Extra searches: exact path/title/deprecation search across current Metronome raw found this Plan-charge operation; the broader Plans-folder sweep found adjacent Plan APIs but no competing endpoint for listing a Plan’s charges.

## 6. Which path identifier and result structure does the operation document, and what charge details can be inspected in raw?

**Verdict: PASS**

- Route: same complete route as task 5.
- Answer evidence:
  - Required path identifier: UUID `plan_id`; optional query controls are `limit` (1–100) and `next_page` (raw lines 142–166).
  - Result: HTTP 200 object with required `data: PlanCharge[]` and required nullable sibling `next_page: string | null` (raw lines 105–140).
  - Inspectable charge details: required ID, name, product ID/name, prices, charge type, credit type, and custom fields; optional quantity, price-ramp `start_period`, tier-reset frequency, and unit conversion (raw lines 168–221). Price items expose value and tier plus optional quantity, collection schedule, and collection interval (raw lines 222–242). Charge types are `usage`, `fixed`, `composite`, `minimum`, and `seat`; credit type has name and UUID; custom fields are string-valued (raw lines 243–269). Unit conversion supplies `division_factor` and optional `rounding_behavior` of `floor` or `ceiling`; null rounding is described as 20-decimal-place rounding (raw lines 205–221).
- Route integrity: the promoted source’s raw-detail locators at lines 25–28 accurately identify the endpoint, parameters, response, and schemas; reciprocal navigation is unique as recorded in task 5.
- Extra searches: a narrow raw search for the exact route and operation title returned the assigned raw; adjacent legacy Plan and credit-grant sources mention charges in other contexts but do not document this operation’s `PlanCharge` result structure.

## Nonblocking optimization observation

`source-metronome-api-reference-plans-list-plan-charges` is correctly primary-routed from `metronome-products-and-rate-cards`, but it is also listed as a source under `metronome-customers-and-contracts` solely for migration context. Moving that secondary occurrence from the generic `## Sources` list into the nearby legacy Plan/Contract migration prose (as a supporting citation) would make the single primary browse route more visually obvious while preserving the useful deprecation context. This does not block retrieval or change the PASS verdict.

# Campaign 39 final retrieval audit - Group B partial report (Anrok pair)

## Run metadata

- UTC start: `2026-09-08T10:25:56Z`
- UTC completion: `2026-09-08T10:28:11Z`
- Scope: 2 of 2 currently assigned Anrok questions; no end-date work attempted.
- Repository/tracking posture: read-only. Only this report was written.
- Governing files read in full before audit: `CLAUDE.md`; `rules/query-and-synthesis.md`.

## Canonical retrieval route

Both questions resolve through the same intended route:

1. `wiki/index.md:5-10` -> `[[metronome-index]]`
2. `wiki/metronome-index.md:236-242` -> purpose-fit `[[metronome-integrations]]`
3. `wiki/concepts/metronome/metronome-integrations.md:61-63` -> Anrok credential-setting fact and citation; `:151-153` -> the promoted source navigation entry
4. `wiki/sources/metronome/source-metronome-api-reference-settings-upsert-anrok-api-token.md:12-27` -> operation summary and raw detail map; `:35-37` -> exact raw backlink
5. `raw/metronome/api-reference/settings/upsert-anrok-api-token-2026-07-13.md` -> exact source of truth, read fully (175/175 lines)

This route begins at the root catalog and traverses the provider catalog and purpose-fit concept. No manifest, attempt, history, tracking, or direct raw shortcut was used.

## Question 1

### Prompt

Where can I find the Anrok credential-setting operation and its supported workflow?

### Answer

Find it at `[[source-metronome-api-reference-settings-upsert-anrok-api-token]]`, reached from `[[metronome-integrations]]`. The operation is the bearer-authenticated Settings request `POST /v1/upsertAnrokApiToken` (`operationId: upsertAnrokApiToken-v1`). The snapshot explicitly limits these API tokens to **Threshold Billing workflows**; it is not evidence for a general-purpose Anrok integration.

### Evidence

- Raw title and summary: `raw/metronome/api-reference/settings/upsert-anrok-api-token-2026-07-13.md:9-11`
- OpenAPI route, method, Settings tag, description, operation ID: raw `:88-98`
- Document-level bearer authentication and bearer scheme: raw `:26-27`, `:170-173`
- Source-summary qualification against overclaiming: `wiki/sources/metronome/source-metronome-api-reference-settings-upsert-anrok-api-token.md:14-21`

### Semantic-fit verdict

**PASS.** The promoted source is exact-purpose evidence: its title, endpoint, operation description, and stated workflow boundary directly match the question. The broader Anrok integration guide is not required to identify this credential-setting operation or its expressly supported workflow.

## Question 2

### Prompt

How are tokens associated with billing entities, and where does the reference tell me to obtain delivery-method identifiers?

### Answer

The caller submits the Anrok token in `anrok_api_token` together with an array of billing-provider configuration UUIDs in `delivery_method_ids`. Metronome maps that Anrok key to the billing entities represented by those IDs. The same reference says to obtain the IDs from the response of `/listConfiguredBillingProviders`.

Payload/detail boundaries: the JSON object schema requires both `delivery_method_ids` and `anrok_api_token`, but the enclosing OpenAPI `requestBody` is not marked required. A successful HTTP 200 returns only `data.success: boolean`; there is no per-ID outcome in this schema.

### Evidence

- Direct association and identifier-discovery statement: raw `:11`
- Repeated operation description: raw `:93-97`
- Required object properties and UUID-array schema: raw `:99-120`
- Example pairing an ID array with one token: raw `:121-124`
- Aggregate success response: raw `:125-145`
- Source-summary route to discovery context: `wiki/sources/metronome/source-metronome-api-reference-settings-upsert-anrok-api-token.md:29-33`

### Semantic-fit verdict

**PASS.** The exact raw page answers both halves without inference: it names the association semantics and explicitly routes identifier discovery to `/listConfiguredBillingProviders`.

## Reciprocal navigation audit

- Provider catalog -> concept: one purpose-fit `[[metronome-integrations]]` entry at `wiki/metronome-index.md:241`.
- Concept `## Sources` -> promoted source: exactly one navigation entry at `wiki/concepts/metronome/metronome-integrations.md:153`.
- Source -> main concept: exactly one `Main concept: [[metronome-integrations]]` backlink at `wiki/sources/metronome/source-metronome-api-reference-settings-upsert-anrok-api-token.md:32`.
- The same source link also appears in the concept's Anrok fact paragraph at `wiki/concepts/metronome/metronome-integrations.md:63`. This is an inline supporting citation, not a duplicate `## Sources` navigation entry.
- Source -> exact raw: one `## Raw Sources` backlink at the source page's line 37, matching its sole `raw_files` entry at line 8.

**Navigation verdict: PASS.** Reciprocal source/concept navigation is present and unique in its intended navigation sections. The inline concept citation correctly supports the fact and does not create a duplicate Sources entry.

## Extra searches and gap sweep

- Filename sweep: `rg --files raw | rg -i 'anrok|configured-billing-provider|billing-provider'` surfaced the selected Anrok token raw, the Anrok integration-guide snapshots, configured-provider reference raws, customer-provider configuration raws, and adjacent provider-transition material.
- Focused raw-text sweep: `rg -n -i 'upsertAnrokApiToken|anrok_api_token|delivery_method_ids|listConfiguredBillingProviders' raw/metronome --glob '*.md'` confirmed the selected raw is the direct Anrok credential source. It also surfaced adjacent Stripe/Avalara and provider-list context but no conflicting Anrok token-to-entity rule.
- No additional raw was used as evidence. The selected raw itself states where to obtain the identifiers and was sufficient for both questions; reading adjacent pages would repeat source review rather than close an answer gap.
- The source page has no `## Related raw API references` section to inspect. Its `## Related` link to the promoted configured-provider source is useful context, but the present question asks where the Anrok reference directs the reader, which the selected raw answers explicitly.

## Interim verdict after Anrok pair

**PASS - 2/2.** Both Anrok questions are retrievable through the required root -> provider index -> purpose-fit concept -> promoted source -> exact raw path. The promoted page is semantically precise, the exact raw substantiates every answer detail, and reciprocal navigation is correctly unique once fact citations are distinguished from `## Sources` navigation.

---

# End-date pair

## Pair timing and scope

- UTC start: `2026-09-08T10:29:29Z`
- UTC completion: `2026-09-08T10:31:10Z`
- Scope: questions 3-4 only; the Anrok pair was not repeated.
- Repository/tracking posture: read-only. No manifest, attempt, history, or tracking shortcut was used.

## Canonical retrieval route

The primary route for both end-date questions is:

1. `wiki/index.md:5-10` -> `[[metronome-index]]`
2. `wiki/metronome-index.md:242-253` -> purpose-fit primary concept `[[metronome-customers-and-contracts]]`
3. `wiki/concepts/metronome/metronome-customers-and-contracts.md:167-169` -> exact contract-end-date fact and promoted source citation
4. `wiki/sources/metronome/source-metronome-api-reference-contracts-update-the-contract-end-date.md:12-33` -> operation, retained behavior, boundaries, and raw-detail map; `:42-44` -> exact raw backlink
5. `raw/metronome/api-reference/contracts/update-the-contract-end-date-2026-07-13.md` -> exact source of truth, read fully (191/191 lines)

The provider index also exposes the promoted source directly at `wiki/metronome-index.md:24-30`, but the audit used the required purpose-fit concept route rather than jumping from that direct catalog entry to the source.

## Question 3

### Prompt

Where can I find how to end a contract early or move its end date?

### Answer

Use `[[source-metronome-api-reference-contracts-update-the-contract-end-date]]`, reached through `[[metronome-customers-and-contracts]]`. It documents the bearer-authenticated Contracts operation `POST /v1/contracts/updateEndDate` (`operationId: updateContractEndDate-v1`) for adding, changing, or removing a contract's end boundary. The optional `ending_before` is an exclusive RFC 3339 timestamp; if omitted, the contract is made open-ended.

### Evidence

- Raw title and complete lifecycle summary: `raw/metronome/api-reference/contracts/update-the-contract-end-date-2026-07-13.md:9-11`
- OpenAPI path, method, Contracts tag, description, and operation ID: raw `:88-100`
- Request example: raw `:101-110`
- Required customer/contract UUIDs and exclusive/open-ended `ending_before` semantics: raw `:136-156`
- Bearer authentication: raw `:26-27`, `:186-189`

### Semantic-fit verdict

**PASS.** The source is the exact operation-level authority for both ending early and moving/removing the end date. It does not require inference from a general lifecycle guide.

## Question 4

### Prompt

What does ending early affect, and what does moving end date later explicitly not extend?

### Answer

Ending the contract early:

- impacts draft usage statements;
- truncates any terms; and
- removes upcoming scheduled invoices.

Moving the end date later extends only the contract length. It explicitly does **not** extend terms, scheduled invoices, or in-advance subscriptions.

A related finalized-invoice boundary is also explicit: `allow_ending_before_finalized_invoice` defaults to `true`; when used, existing finalized invoices remain unchanged. To incorporate the new end date into finalized usage invoices, the reference says they can be voided and regenerated.

### Evidence

- Complete earlier-versus-later effect statement: raw `:11`
- OpenAPI operation description repeating each effect and non-extension: raw `:93-99`
- Finalized-invoice option, unchanged-invoice boundary, and remediation: raw `:157-163`
- Source summary's retained behavior and material non-renewal boundary: `wiki/sources/metronome/source-metronome-api-reference-contracts-update-the-contract-end-date.md:16-25`

### Semantic-fit verdict

**PASS.** The raw operation description states every requested effect and non-extension directly. The source summary preserves the distinctions without converting an end-date extension into a renewal claim.

## Reciprocal and supporting navigation audit

- Primary provider-catalog route: one `[[metronome-customers-and-contracts]]` entry at `wiki/metronome-index.md:253`.
- Primary concept -> promoted source: exactly one occurrence at `wiki/concepts/metronome/metronome-customers-and-contracts.md:169`. It is a fact-paragraph citation under `## Contract edit history`, not a `## Sources` list entry; that remains a valid purpose-fit source route.
- Promoted source -> primary concept: exactly one `Primary concept: [[metronome-customers-and-contracts]]` backlink at `wiki/sources/metronome/source-metronome-api-reference-contracts-update-the-contract-end-date.md:38`.
- Purpose-fit supporting source routes are present once each: `[[metronome-invoicing]]` lists the source at `wiki/concepts/metronome/metronome-invoicing.md:277`, and `[[metronome-subscriptions]]` lists it at `wiki/concepts/metronome/metronome-subscriptions.md:54`.
- The source identifies those same supporting concepts once in `Purpose-fit navigation` at its line 39.
- Source -> exact raw: one `## Raw Sources` backlink at the source page's line 44, matching its sole `raw_files` entry at line 8.

**Navigation verdict: PASS.** The primary reciprocal route is unique and semantically appropriate even though the primary concept uses an inline fact citation rather than duplicating the source in its `## Sources` list. The invoicing and subscription routes are distinct, purpose-fit supporting navigation, not duplicate primary routes.

## Extra searches and gap sweep

- Filename sweep for contract-ending topics surfaced the selected operation raw, the customer-lifecycle guide, and contract-amendment raws.
- Focused raw-text sweep for `updateEndDate` and the explicit earlier/later behavior surfaced lifecycle, pricing, and marketplace pages that point to the same endpoint, plus separate credit/commit end-date operations. No conflicting contract-end-date effect statement was found.
- The selected operation raw directly and completely answers both questions, so no adjacent raw was used as evidence. Separate credit or commit end-date operations are different resources and would be semantically wrong substitutes.
- The promoted source has no `## Related raw API references` section to inspect. Its API-wide idempotency link is retry context, not needed for this retrieval pair.

## Final Group B verdict

**PASS - 4/4.** The two Anrok questions and the two contract-end-date questions are all retrievable through their required root -> provider index -> purpose-fit concept -> promoted source -> exact raw routes. Both selected raws were read fully. Each promoted source is semantically exact for its pair, retains the material workflow and lifecycle boundaries, and has valid reciprocal navigation with intended uniqueness. Supporting concept routes add purpose-fit discovery without duplicating the primary relationship.
