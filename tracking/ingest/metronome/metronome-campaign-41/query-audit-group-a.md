# Campaign 41 final retrieval audit — Group A

- Scope: retrieval audit only; not a third semantic approval.
- Repository: `/Users/tengtao/Development/wiki-v2`
- UTC start: `2026-09-09T13:06:54Z`
- UTC end: `2026-09-09T13:11:37Z`
- Overall verdict: **PASS (6/6)**
- Repository/tracking writes by this auditor: **none**. The only write is this report.
- Governing files read before auditing: `CLAUDE.md`, `rules/query-and-synthesis.md`, `rules/psp/metronome.md`, and `rules/psp/metronome-ingest.md`.
- Navigation method: every question began at `wiki/index.md`, followed `[[metronome-index]]`, selected the purpose-fit promoted concept, followed its source link, then followed the source page's exact path-qualified `## Raw Sources` link. No manifest, campaign attempt, receipt, or tracking shortcut was used.
- Catalog timing: the three assigned source pages are not yet in the aggregate `wiki/metronome-index.md` source list. This is nonblocking for this audit because the assigned state says aggregate cataloging happens later and the concept routes are already promoted.
- Route integrity: `wiki/index.md` contains one Metronome-index route; `wiki/metronome-index.md` contains one route each to `[[metronome-credits-and-commits]]` and `[[metronome-alerts-and-notifications]]`; each assigned source link occurs once in the intended concept `## Sources` section; and each assigned source has one reciprocal link back to the purpose-fit concept in `## Related`.

## Q1 — LEGACY CREDIT GRANTS / LIST

**Requested object/action:** list legacy **credit grants**, and identify the recommended API family for new clients.

**Route with object/action verification:** `wiki/index.md` (`[[metronome-index]]`) → `wiki/metronome-index.md` (`[[metronome-credits-and-commits]]`) → `wiki/concepts/metronome/metronome-credits-and-commits.md` (`## Sources`, `[[source-metronome-api-reference-credit-grants-list-credit-grants]]`) → `wiki/sources/metronome/source-metronome-api-reference-credit-grants-list-credit-grants.md` → `raw/metronome/api-reference/credit-grants/list-credit-grants-2026-07-13.md`. **Verified beside route:** the selected source and raw are titled “List credit grants,” document `listGrants`, and are explicitly the deprecated Plans surface—not current credit listing, credit archival, a commit operation, or a ledger listing.

**Answer:** Use bearer-authenticated `POST https://api.metronome.com/v1/credits/listGrants`. It is a deprecated **Plans** endpoint. The page directs new clients to the **Contracts** family, but it does not name a one-to-one Contracts replacement or migration mapping.

**Evidence:** exact raw heading and warning at lines 9–11; operation/server at `paths./credits/listGrants.post` plus the `/v1` server; source summary lines 14–20; raw-detail locator in source line 24.

**Required gap sweep:** `rg -l -i "listGrants|list credit grants|voided grants" raw/metronome`. Results were the exact page plus aggregate versioned Plans OpenAPI artifacts; no competing purpose-fit raw page was found. No extra raw read was needed.

**Verdict:** **PASS**.

**Concrete failures:** none.

## Q2 — LEGACY CREDIT GRANTS / LIST DETAILS

**Requested object/action:** for that same legacy credit-grant list, determine voided-grant inclusion, customer selection, pagination, and returned grant detail.

**Route with object/action verification:** `wiki/index.md` → `wiki/metronome-index.md` → `[[metronome-credits-and-commits]]` → `[[source-metronome-api-reference-credit-grants-list-credit-grants]]` → `raw/metronome/api-reference/credit-grants/list-credit-grants-2026-07-13.md`. **Verified beside route:** the raw operation is the same `POST /v1/credits/listGrants` list object from Q1, not the separate credit-ledger endpoint or current Contracts credit list.

**Answer:**

- Voided grants are explicitly excluded, so the result is not a complete grant inventory/history.
- Customer selection uses optional JSON-body `customer_ids` (UUID array). It cannot be supplied with `credit_grant_ids`; when `credit_grant_ids` is supplied, neither `customer_ids` nor `credit_type_ids` may be supplied. Other optional body filters are `credit_type_ids`, `not_expiring_before` (expire at or after), and `effective_before` (exclusive).
- Pagination uses optional query `limit` (`1`–`100`) and query `next_page`. HTTP `200` requires `data` and nullable `next_page`; continue with the returned cursor until it is null.
- Each returned `CreditGrant` requires `id`, `name`, `customer_id`, `effective_at`, `expires_at`, `priority`, `grant_amount`, `paid_amount`, `balance`, `deductions`, `pending_deductions`, and `custom_fields`. Optional detail includes `invoice_id`, `uniqueness_key`, `reason`, `credit_grant_type`, and `products`. Grant/paid amounts embed amount plus credit type; balance includes posted-only and posted-plus-pending values with an effective time; deduction arrays contain ledger-entry detail.

**Evidence:** void exclusion at raw lines 9–11 and 96–101; pagination parameter definitions at lines 175–192 and success envelope at lines 122–174; payload filters at lines 193–240; `CreditGrant` schema at lines 241–367; ledger and nested type schemas at lines 376–428.

**Required gap sweep:** same legacy-list filename/content sweep as Q1. The aggregate OpenAPI copies did not reveal a different routed object, and the selected raw completely answered the query. No extra raw read was needed.

**Verdict:** **PASS**.

**Concrete failures:** none.

## Q3 — CREDIT / EDIT

**Requested object/action:** modify an existing customer-level or contract-level **credit**, specifically excluding archive and commit operations.

**Route with object/action verification:** `wiki/index.md` (`[[metronome-index]]`) → `wiki/metronome-index.md` (`[[metronome-credits-and-commits]]`) → `wiki/concepts/metronome/metronome-credits-and-commits.md` (`## Sources`, `[[source-metronome-api-reference-credits-and-commits-edit-a-credit]]`) → `wiki/sources/metronome/source-metronome-api-reference-credits-and-commits-edit-a-credit.md` → `raw/metronome/api-reference/credits-and-commits/edit-a-credit-2026-08-28.md`. **Verified beside route:** title, purpose text, operation ID `editCredit-v2`, and path all identify credit editing. The route did not select the nearby archive-credit, edit-commit, or general contract-edit sources.

**Answer:** Use bearer-authenticated `POST https://api.metronome.com/v2/contracts/credits/edit`. A supplied payload requires `customer_id` and `credit_id`. Documented editable surfaces are `name`, `description`, `access_schedule` (add/update/remove schedule items), `applicable_product_ids`, `applicable_product_tags`, customer-credit `applicable_contract_ids`, `specifiers`, `product_id`, `priority`, `rate_type`, and `hierarchy_configuration`. `specifiers` cannot be combined with the direct product-ID/tag selectors, and `applicable_contract_ids` cannot be set on a contract-level credit.

**Evidence:** raw purpose and use cases at lines 9–19; operation at `paths./v2/contracts/credits/edit.post` beginning line 96; required identity and editable properties under `components.schemas.EditCreditPayload` lines 170–256; access-schedule shapes under `UpdateAccessScheduleInput`; source overview and coverage map lines 14–36.

**Required gap sweep:** `rg -l -i "/v2/contracts/credits/edit|Edit a credit|access schedule segment that was applied to a finalized invoice" raw/metronome`. It found the exact 2026-08-28 page, its 2026-07-13 predecessor, related commit/edit-contract pages, discovery indexes, and aggregate OpenAPI artifacts. The promoted source selects the newer exact snapshot, which completely answers the current query; no historical comparison or conflict required reading the predecessor or adjacent-object pages.

**Verdict:** **PASS**.

**Concrete failures:** none.

## Q4 — CREDIT / EDIT INVOICE AND SCHEDULE EFFECTS

**Requested object/action:** for that same existing-credit edit, determine draft-versus-finalized invoice effects and the restriction on removing an access-schedule segment.

**Route with object/action verification:** `wiki/index.md` → `wiki/metronome-index.md` → `[[metronome-credits-and-commits]]` → `[[source-metronome-api-reference-credits-and-commits-edit-a-credit]]` → `raw/metronome/api-reference/credits-and-commits/edit-a-credit-2026-08-28.md`. **Verified beside route:** the selected operation is the same credit edit from Q3; it is not credit archive, commit edit, or invoice-issue-date mutation.

**Answer:** Draft invoices reflect an edit immediately. Finalized invoices remain untouched unless voided and regenerated. The `rate_type` description likewise says changes affect current and future invoices, while earlier finalized invoices must be voided and regenerated to reflect the change. An access-schedule segment already applied to a finalized invoice cannot be removed; void the invoice first, then remove the segment.

**Evidence:** raw usage guidelines at lines 18–19 and repeated in the operation description at lines 116–123; `rate_type` qualification at lines 243–253; schedule removal shape under `UpdateAccessScheduleInput`; source summary lines 18–26.

**Required gap sweep:** same current credit-edit sweep as Q3. The exact raw states both requested effects directly, so no extra authority was needed.

**Verdict:** **PASS**.

**Concrete failures:** none.

## Q5 — OFFSET NOTIFICATION CONFIGURATION / EDIT

**Requested object/action:** edit an existing **offset lifecycle-event notification configuration**, not a threshold alert and not an emitted/delivered notification event.

**Route with object/action verification:** `wiki/index.md` (`[[metronome-index]]`) → `wiki/metronome-index.md` (`[[metronome-alerts-and-notifications]]`) → `wiki/concepts/metronome/metronome-alerts-and-notifications.md` (`## Sources`, `[[source-metronome-api-reference-notifications-edit-an-offset-lifecycle-event-notification-configuration]]`) → `wiki/sources/metronome/source-metronome-api-reference-notifications-edit-an-offset-lifecycle-event-notification-configuration.md` → `raw/metronome/api-reference/notifications/edit-an-offset-lifecycle-event-notification-configuration-2026-07-13.md`. **Verified beside route:** the source/raw title, operation summary, and `editNotificationConfig-v2` identify stored offset-configuration mutation. The source explicitly says success is not evidence of lifecycle-event occurrence, emitted notification, or webhook delivery; it is not a threshold-alert endpoint.

**Answer:** Use bearer-authenticated `POST https://api.metronome.com/v2/notifications/edit` to edit the existing offset lifecycle-event notification configuration.

**Evidence:** raw title/purpose at lines 9–11; operation at `paths./v2/notifications/edit.post` beginning line 87; source overview and scope boundary at lines 14–26.

**Required gap sweep:** `rg -l -i "/v2/notifications/edit|Edit an existing offset lifecycle event notification configuration|policy.type must match" raw/metronome`. It found the exact page plus aggregate OpenAPI/discovery copies and a system-notification guide. The exact operation fully answers the requested mutation and preserves the threshold/event-delivery boundary, so no extra raw read was needed.

**Verdict:** **PASS**.

**Concrete failures:** none.

## Q6 — OFFSET NOTIFICATION CONFIGURATION / EDIT DETAILS

**Requested object/action:** for that same offset-configuration edit, identify the configuration ID, editable settings, response structure, and explicit edit restrictions.

**Route with object/action verification:** `wiki/index.md` → `wiki/metronome-index.md` → `[[metronome-alerts-and-notifications]]` → `[[source-metronome-api-reference-notifications-edit-an-offset-lifecycle-event-notification-configuration]]` → `raw/metronome/api-reference/notifications/edit-an-offset-lifecycle-event-notification-configuration-2026-07-13.md`. **Verified beside route:** this remains the stored offset-configuration edit operation. Threshold configuration, system-event emission, offset occurrence, and webhook delivery are outside the selected object's action.

**Answer:**

- The configuration identifier is payload `id` (UUID). The offset-edit example supplies it. However, `EditNotificationConfigPayload.required` contains only `policy`; the `id` description says it is omitted for system-event configuration updates, and the page does not explicitly resolve omitted-ID behavior for offset edits.
- The updated `policy` is required within a supplied payload and is one of an offset or system policy. For the assigned offset object, `LifecycleEventOffsetPolicy` requires lifecycle-event `type` and signed ISO-8601 `offset`; positive means after the base event and negative means before it.
- Explicit restrictions: updated `policy.type` must match the existing lifecycle-event type, so this edit does not change the configuration to a different event basis. Shared payload `is_enabled` is supported only for system lifecycle events, so it is not an offset-configuration enable/disable control. The payload exposes no offset-configuration `name` update field; absence alone does not establish unknown-field rejection.
- HTTP `200` requires top-level `data`, whose schema is `oneOf` `LifecycleEventSystemNotificationConfig` or `LifecycleEventOffsetNotificationConfig`. The offset form requires `id`, `name`, configuration `type`, `policy`, `environment_type`, `created_at`, `created_by`, and nullable `archived_at`. Its policy separately requires lifecycle-event `type` and `offset`. Documented `400` codes are `NotificationConfigNotFound` and `BadRequest`.

**Evidence:** request example at raw lines 97–105; response envelope/example at lines 107–132; error codes at lines 134–148; edit payload at lines 151–176; system/offset response schemas at lines 177–235; offset policy at lines 236–254; source material boundaries and coverage map at lines 18–30.

**Required gap sweep:** same offset-edit sweep as Q5. The exact raw provides every requested schema boundary, including its unresolved offset-ID requiredness; no extra raw was needed.

**Verdict:** **PASS**.

**Concrete failures:** none.

## Final audit result

All six assigned retrieval questions pass. The promoted concept routes are purpose-fit, reciprocal, unique within their intended navigation sections, and lead to exact raw evidence that answers the requested details. No retrieval failure, wrong-object answer, repair, repository edit, or promotion recommendation was found.
