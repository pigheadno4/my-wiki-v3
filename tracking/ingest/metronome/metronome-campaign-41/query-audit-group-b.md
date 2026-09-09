# Campaign 41 final retrieval audit — Group B

## Timing and scope

- `started_at_utc`: `2026-09-09T13:08:23Z`
- `audit_completed_at_utc`: `2026-09-09T13:17:45Z`
- `final_artifact_handoff_at_utc`: `2026-09-09T13:20:38Z`
- `audit_elapsed`: `9m22s`
- `start_to_final_handoff_elapsed`: `12m15s` (includes report verification and coordinator handoff)
- `field_promotion_wait`: `2026-09-09T13:09:45Z`–`2026-09-09T13:14:57Z` (`5m12s` observed). At `2026-09-09T13:11:03Z`, the coordinator reported that semantic review had approved the candidate/shared meaning but a bounded receipt-only quote-line correction was still running. Q9/Q10 were not scored before promotion.
- Scope: Q7–Q10 only. Repository and tracking were read-only. No manifest, attempt, receipt, or tracking shortcut was used. The only write is this report.
- Rules read before audit: `CLAUDE.md`, `rules/query-and-synthesis.md`, `rules/psp/metronome.md`, `rules/psp/metronome-ingest.md`.
- Final group verdict: **PASS — 4/4 questions retrieved through the required live wiki route and verified against complete exact-raw reads.**

## Q7 — prepaid commit: shorten its end date

### Requested object/action and match check

- Requested object: one existing **prepaid commit**.
- Requested action: shorten its end boundary, rather than change a credit, extend a commit, or change the enclosing contract's end date.
- Reached source/raw match: **yes**. Both are titled `Update the commit end date`; the operation is tagged `Credits and commits`, selects `customer_id` plus `commit_id`, and the raw explicitly limits `commit_id` to `PREPAID`. This is not the separate credit or contract end-date operation.

### Route

`wiki/index.md:9` → `wiki/metronome-index.md:260` (`metronome-credits-and-commits`) → `wiki/concepts/metronome/metronome-credits-and-commits.md:269` → `wiki/sources/metronome/source-metronome-api-reference-credits-and-commits-update-the-commit-end-date.md` → `raw/metronome/api-reference/credits-and-commits/update-the-commit-end-date-2026-07-13.md`.

The provider index also directly catalogs the reached source at `wiki/metronome-index.md:29`; this was confirmed after aggregate catalog close.

### Answer and evidence

Use bearer-authenticated `POST /v1/contracts/customerCommits/updateEndDate` (`raw` lines 91–114). In a supplied payload, identify the customer and commit with required UUIDs `customer_id` and `commit_id` (`raw` lines 145–158). Supply either or both of:

- `access_ending_before`: exclusive RFC 3339 cutoff after which the commit cannot be drawn down; omission leaves access unchanged (`raw` lines 159–165).
- `invoices_ending_before`: exclusive RFC 3339 cutoff after which the commit stops being invoiced; omission leaves the invoice schedule unchanged (`raw` lines 166–173).

Verdict: **PASS**. The intended targeted shortening operation is directly retrievable and the reached evidence matches the requested object/action.

## Q8 — same prepaid commit: type/date restrictions and extension route

### Requested object/action and match check

- Requested object: the same existing commit selected in Q7.
- Requested action: determine its commit-type/date-direction restrictions and where extension or comprehensive edits go.
- Reached source/raw match: **yes**. The source/raw remain commit-specific and explicitly distinguish shortening from extension.

### Route

Same route as Q7, ending in the complete 200-line exact raw `raw/metronome/api-reference/credits-and-commits/update-the-commit-end-date-2026-07-13.md`.

### Answer and evidence

- Commit type: **PREPAID only** (`raw` lines 97–101 and 155–158).
- Date direction: the endpoint can move an end boundary **earlier only**; it cannot extend the commit. The raw uses the phrase “move the end date forward (earlier),” so “earlier” is the operative direction (`raw` lines 97–101).
- Extension/comprehensive edit route: use the separate **edit commit** endpoint (`raw` lines 104–107), represented in the wiki by `wiki/sources/metronome/source-metronome-api-reference-credits-and-commits-edit-a-commit.md` (`POST /v2/contracts/commits/edit`).

Verdict: **PASS**. The type, direction, and handoff route are explicit in the exact raw.

## Q9 — one entity instance: set custom-field values

### Requested object/action and match check

- Requested object: one identified Metronome entity instance.
- Requested action: set custom-field values on that instance, rather than delete selected values or remove a key definition.
- Reached source/raw match: **yes**. The reached operation selects `entity` plus UUID `entity_id` and accepts a `custom_fields` map; it is not `deleteValues` and not `removeKey`.

### Route

After coordinator-confirmed promotion at `2026-09-09T13:14:57Z`: `wiki/index.md:9` → `wiki/metronome-index.md:275` (`metronome-custom-fields`) → `wiki/concepts/metronome/metronome-custom-fields.md:84` → `wiki/sources/metronome/source-metronome-api-reference-custom-fields-set-custom-field-values.md` → `raw/metronome/api-reference/custom-fields/set-custom-field-values-2026-07-13.md`.

The provider index also directly catalogs the reached source at `wiki/metronome-index.md:30`.

### Answer and evidence

Use bearer-authenticated `POST /v1/customFields/setValues` (`raw` lines 88–100). Within a supplied JSON object, the schema requires `entity`, `entity_id`, and `custom_fields`; `entity_id` is a UUID and `custom_fields` routes to the `CustomField` string-valued map schema (`raw` lines 101–121 and 152–156).

Action-boundary sweep:

- `POST /v1/customFields/deleteValues` removes named field values from one selected entity instance while preserving other fields (`raw/metronome/api-reference/custom-fields/delete-custom-fields-2026-07-13.md`, lines 88–124).
- `POST /v1/customFields/removeKey` removes an entity/key pair from the allowlist across all instances of that entity type, making existing values inaccessible (`raw/metronome/api-reference/custom-fields/delete-a-custom-field-key-2026-07-13.md`, lines 88–115).

Verdict: **PASS**. The promoted route selects the correct object and mutation rather than either deletion operation.

## Q10 — same entity value mutation: overwrite, preservation, transaction, limits, selectors

### Requested object/action and match check

- Requested object: the same one entity instance selected by `entity` and `entity_id` in Q9.
- Requested action: determine matching-key behavior, other-key preservation, transaction guarantee, value limit, and entity selectors.
- Reached source/raw match: **yes**. The operation description and schemas describe exactly that entity-instance value mutation.

### Route

Same route as Q9, ending in the complete 162-line exact raw `raw/metronome/api-reference/custom-fields/set-custom-field-values-2026-07-13.md`.

### Answer and evidence

- Submitted matching keys overwrite their existing values; other custom fields on the entity are preserved (`raw` lines 93–97).
- The submitted update is documented as transactional: all submitted values are set or none are (`raw` lines 95–97).
- Each value is documented as limited to **200 characters** in the operation description (`raw` line 97). The `CustomField` schema itself defines arbitrary string-valued properties but does not encode `maxLength`; the limit is therefore narrative documentation, not a schema keyword (`raw` lines 152–156).
- Endpoint `entity` selectors are the 19 `ManagedEntity` enum values (`raw` lines 127–148): `alert`, `billable_metric`, `charge`, `commit`, `contract_credit`, `contract_product`, `contract`, `customer`, `discount`, `invoice`, `professional_service`, `product`, `rate_card`, `scheduled_charge`, `subscription`, `package_commit`, `package_credit`, `package_subscription`, and `package_scheduled_charge`.
- The supplied-object required properties are at `paths./v1/customFields/setValues.post.requestBody...schema.required`; selector choices are at `components.schemas.ManagedEntity`; the value-map shape is at `components.schemas.CustomField`; bearer authentication is at the root `security` declaration and `components.securitySchemes.bearerAuth`.

Verdict: **PASS**. The requested behaviors, limit, selectors, and their raw locations are discoverable without pre-expanding source-level schema detail.

## Route integrity, reciprocal uniqueness, and provenance

- Root `wiki/index.md` links `metronome-index` once.
- Commit route: provider index links the source once and main concept once; the main concept links the source once; the source reciprocally links the main concept once. Its `raw_files` path and path-qualified `Raw Sources` backlink resolve to the exact 200-line raw read.
- Custom-field route: provider index links the source once and main concept once; the main concept links the source once; the source reciprocally links the main concept once. Its `raw_files` path and path-qualified `Raw Sources` backlink resolve to the exact 162-line raw read.
- Purpose fit: both reciprocal routes describe the question-bearing operation and its selection boundary, not incidental fields.
- No duplicate catalog or reciprocal entries were observed in the checked navigation surfaces.

## Searches and complete reads

Complete reads used as evidence or necessary object/action disambiguation:

- `wiki/index.md`
- `wiki/metronome-index.md`
- `wiki/concepts/metronome/metronome-credits-and-commits.md`
- `wiki/sources/metronome/source-metronome-api-reference-credits-and-commits-update-the-commit-end-date.md`
- `raw/metronome/api-reference/credits-and-commits/update-the-commit-end-date-2026-07-13.md` (200 lines)
- `wiki/concepts/metronome/metronome-custom-fields.md`
- `wiki/sources/metronome/source-metronome-api-reference-custom-fields-set-custom-field-values.md`
- `raw/metronome/api-reference/custom-fields/set-custom-field-values-2026-07-13.md` (162 lines)
- `raw/metronome/api-reference/custom-fields-2026-08-28.md` (144 lines; related overview gap check)
- `raw/metronome/api-reference/custom-fields/delete-custom-fields-2026-07-13.md` (160 lines; one-instance delete-values disambiguation)
- `raw/metronome/api-reference/custom-fields/delete-a-custom-field-key-2026-07-13.md` (151 lines; entity-type key-removal disambiguation)

Gap sweeps used filename and content searches across `raw/metronome` and `wiki` for commit/end/edit/credit/contract and custom-field/setValues/deleteValues/removeKey/matching/transaction/limit terms. The sweeps found the distinct credit-end-date, contract-end-date, edit-commit, delete-values, and remove-key routes and did not displace either selected operation.

## Nonblocking gaps and failures

- Nonblocking gap: the latest custom-fields overview raw says `custom_fields` “accepts an array of key-value pairs,” but its own example uses an object and the dedicated endpoint OpenAPI defines an arbitrary-key string-valued object. For Q9/Q10, the dedicated endpoint schema is the exact authority. This wording conflict does not change the selected operation or requested behavior.
- Nonblocking scope tension: the custom-fields overview names a narrower eight-entity prose set, whereas the exact `setValues` endpoint exposes 19 `ManagedEntity` enum selectors. The answer reports the endpoint-specific enum without claiming it reconciles platform-wide applicability labels.
- Nonblocking schema qualification: the enclosing OpenAPI `requestBody` is not marked required even though `entity`, `entity_id`, and `custom_fields` are required within a supplied payload. No omitted-body behavior is inferred.
- Retrieval failures: **none**.
- Wrong-object answers: **none**.
- Repairs requested by this audit: **none**. No third semantic approval was performed or requested.
