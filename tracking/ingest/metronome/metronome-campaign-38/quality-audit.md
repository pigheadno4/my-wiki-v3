# Campaign 38 — final retrieval audit

Overall verdict: **PASS — 10/10 predetermined questions**, with zero extra searches, retrieval misses, or route repairs. One audit was divided into two disjoint groups (6 + 4); no question was repeated by the coordinator. Detail-task auditors read their assigned raw snapshots in full.

All five index → main concept → source → exact raw routes worked. Reciprocal navigation was unique within its intended sections. A supported concept-body citation is not counted as a duplicate navigation entry.

Three non-blocking index-description improvements were applied during normal close aggregation: contract lifecycle/change/end, offset configuration lookup, and usage targeting. These improve discoverability without expanding source facts or concept synthesis. Evidence line numbers below reflect the audit-time snapshot and may shift after aggregation.

# Campaign 38 retrieval audit — Group A

Scope: exactly six predetermined tasks for Contract lifecycle, Offset notification get, and List rate cards. The route for every task began at `wiki/index.md` and followed actual wiki links; no manifest or historical-attempt path was used as retrieval evidence. Selected detail raw files were read in full.

## Six task results

1. **Contract lifecycle — navigation — PASS**
   - **Answer:** Workflows for changing and ending customer contracts are under `[[metronome-customers-and-contracts]]`, which routes to `[[source-metronome-guides-customers-billing-manage-customers-manage-customer-lifecycle]]` for existing-contract edits, linked renewals, early conclusion, and merchant-owned access enforcement.
   - **Route:** `wiki/index.md:9` → `wiki/metronome-index.md:241` → `wiki/concepts/metronome/metronome-customers-and-contracts.md:255` → `wiki/sources/metronome/source-metronome-guides-customers-billing-manage-customers-manage-customer-lifecycle.md:14-24`.
   - **Extra-search count:** 0.

2. **Contract lifecycle — detail — PASS**
   - **Answer:** A mid-term update edits the existing contract to add or change terms; the worked renewal instead creates a linked successor contract. Concluding early schedules a new end date with `/v1/contracts/updateEndDate`. The guide separates financial handling from application access: the merchant must configure an alert/webhook and make its entitlement system listen and gate product access.
   - **Route:** same index/concept/source route as task 1 → source raw backlink at `wiki/sources/metronome/source-metronome-guides-customers-billing-manage-customers-manage-customer-lifecycle.md:40-42` → `raw/metronome/guides/customers-billing/manage-customers/manage-customer-lifecycle-2026-07-13.md:98-117,168-180,232-259`.
   - **Extra-search count:** 0.

3. **Offset notification get — navigation — PASS**
   - **Answer:** Inspect one offset-notification configuration by identity through `[[metronome-alerts-and-notifications]]` and its targeted-get source, `[[source-metronome-api-reference-notifications-get-an-offset-lifecycle-event-notification-configuration]]`, documenting `POST /v2/notifications/get`.
   - **Route:** `wiki/index.md:9` → `wiki/metronome-index.md:247` → `wiki/concepts/metronome/metronome-alerts-and-notifications.md:93` → `wiki/sources/metronome/source-metronome-api-reference-notifications-get-an-offset-lifecycle-event-notification-configuration.md:14-20`.
   - **Extra-search count:** 0.

4. **Offset notification get — detail — PASS**
   - **Answer:** Required UUID property `id` within the supplied JSON payload schema selects the configuration. The `200` response places the configuration in top-level `data`; its required `policy.type` is the base lifecycle-event type and `policy.offset` is the signed ISO 8601 offset. Positive offsets mean after the base event and negative offsets mean before it.
   - **Route:** same index/concept/source route as task 3 → source raw backlink at `wiki/sources/metronome/source-metronome-api-reference-notifications-get-an-offset-lifecycle-event-notification-configuration.md:36-38` → `raw/metronome/api-reference/notifications/get-an-offset-lifecycle-event-notification-configuration-2026-07-13.md:96-124,163-171,215-233`.
   - **Extra-search count:** 0.

5. **List rate cards — navigation — PASS**
   - **Answer:** Discover cards through `[[metronome-products-and-rate-cards]]` and `[[source-metronome-api-reference-rate-cards-list-rate-cards]]`. The list operation returns card metadata, not rates; the reference directs actual-rate inspection to the separate `getRates` or `getRateSchedule` endpoints.
   - **Route:** `wiki/index.md:9` → `wiki/metronome-index.md:239` → `wiki/concepts/metronome/metronome-products-and-rate-cards.md:148` → `wiki/sources/metronome/source-metronome-api-reference-rate-cards-list-rate-cards.md:14-21`.
   - **Extra-search count:** 0.

6. **List rate cards — detail — PASS**
   - **Answer:** Optional query `limit` accepts 1–100 results and optional query `next_page` is the cursor for the next page. A successful response requires sibling fields `data` (an array of `RateCard`) and `next_page` (nullable string).
   - **Route:** same index/concept/source route as task 5 → source raw backlink at `wiki/sources/metronome/source-metronome-api-reference-rate-cards-list-rate-cards.md:35-37` → `raw/metronome/api-reference/rate-cards/list-rate-cards-2026-07-13.md:88-125,141-157`.
   - **Extra-search count:** 0.

## Reciprocal navigation

- **Contract lifecycle:** exactly one intended concept → source entry (`metronome-customers-and-contracts.md:255`) and exactly one source → main-concept return link (`source-...manage-customer-lifecycle.md:38`).
- **Offset notification get:** exactly one intended concept → source entry (`metronome-alerts-and-notifications.md:93`) and exactly one source → main-concept return link (`source-...get-an-offset-lifecycle-event-notification-configuration.md:33`).
- **List rate cards:** exactly one intended concept → source entry (`metronome-products-and-rate-cards.md:148`) and exactly one source → main-concept return link (`source-...list-rate-cards.md:33`).
- All three source targets, three main concepts, and three raw backlink targets exist. No missing, duplicate, or wrong-topic reciprocal route was found.

## Concrete optimization opportunity

At provider-index aggregation/close, enrich the existing concept descriptions at `wiki/metronome-index.md:241` and `:247` with the query vocabulary **contract lifecycle/change/end** and **offset configuration lookup**. The current concepts are correct and the six tasks pass, but those two catalog descriptions are broad enough that a future evaluator could hesitate before selecting the right concept. This is navigation enrichment only; it does not require concept prose or source-scope expansion.

# Campaign 38 retrieval audit — group B

Status: 4/4 assigned tasks complete. Both approved sources and their promoted main-concept routes were audited; no candidate or attempt artifact was used as evidence.

## 1. Contract usage filter — navigation

- **Answer:** Use `[[metronome-customers-and-contracts]]`, then its Sources entry for `[[source-metronome-api-reference-contracts-set-a-contract-usage-filter]]`. That source is specifically described as contract-level routing for overlapping rates and leads to the exact raw snapshot.
- **Evidence:** `wiki/index.md:5-10` selects the Metronome provider index; `wiki/metronome-index.md:230-242` exposes the main contracts concept; `wiki/concepts/metronome/metronome-customers-and-contracts.md:251-253` has the purpose-fit source entry; the source identifies the operation and overlapping-contract purpose at `wiki/sources/metronome/source-metronome-api-reference-contracts-set-a-contract-usage-filter.md:12-18`, and its exact raw link is at line 37.
- **Route:** `wiki/index.md` → `wiki/metronome-index.md` → `wiki/concepts/metronome/metronome-customers-and-contracts.md` → `wiki/sources/metronome/source-metronome-api-reference-contracts-set-a-contract-usage-filter.md` → `raw/metronome/api-reference/contracts/set-a-contract-usage-filter-2026-07-13.md`.
- **Extra search:** None needed after following the prescribed route. I read the complete 200-line raw file for the paired detail task. Exact-link checks found one intended concept→source entry in the concept Sources section, one source→concept return link, one `raw_files` entry, and one matching path-qualified Raw Sources link.
- **Verdict:** **PASS.** `metronome-customers-and-contracts` semantically fits customer-contract selection when rates overlap; the reciprocal navigation is present and unique in its intended sections, and the raw route is exact rather than manifest/attempt based.

## 2. Contract usage filter — detail

- **Answer:** The filter's `group_key` must already be defined on the billable metrics underlying the contracts' rate card. The payload requires `customer_id`, `contract_id`, `group_key`, `group_values`, and `starting_at`; `group_values` is an array whose items are strings. The reference states no minimum/maximum array size, uniqueness rule, or behavior for unmatched or multiply matched usage, so none should be inferred.
- **Evidence:** The prerequisite is explicit in `raw/metronome/api-reference/contracts/set-a-contract-usage-filter-2026-07-13.md:20-21` and repeated in the OpenAPI description at lines 127-128. `SetUsageFilterPayload` requires all five fields at lines 157-164; `group_key` is a string at lines 172-173 and `group_values` is an array of strings at lines 174-177. The concise source preserves both the prerequisite and the documented schema/absence boundary at `wiki/sources/metronome/source-metronome-api-reference-contracts-set-a-contract-usage-filter.md:20-27`.
- **Route:** Same prescribed index → main concept → source → exact raw route as task 1; raw detail locator: `POST /v1/contracts/setUsageFilter`, schema key `SetUsageFilterPayload`.
- **Extra search:** None. The exact raw operation and schema fully answer the declared question; no adjacent concept or unrelated authority was necessary.
- **Verdict:** **PASS.** The source retains the consequential prerequisite, accurately routes schema detail to raw, and does not invent constraints absent from the reference.

## 3. Target credits/commits — navigation

- **Answer:** Use `[[metronome-credits-and-commits]]`, then its Sources entry for `[[source-metronome-guides-pricing-packaging-apply-credits-and-commits-target-credit-and-commits]]`. The concept's reviewed Drawdown and invoice attribution paragraph also directly describes the source's selector purpose.
- **Evidence:** `wiki/index.md:5-10` selects the Metronome provider index; `wiki/metronome-index.md:236-247` exposes the credits-and-commits main concept; `wiki/concepts/metronome/metronome-credits-and-commits.md:37-39` gives the purpose-fit selector summary and source citation; its intended Sources section has the matching navigation entry at lines 263-265. The source identifies selected-usage targeting at `wiki/sources/metronome/source-metronome-guides-pricing-packaging-apply-credits-and-commits-target-credit-and-commits.md:12-20` and links the exact raw snapshot at line 35.
- **Route:** `wiki/index.md` → `wiki/metronome-index.md` → `wiki/concepts/metronome/metronome-credits-and-commits.md` → `wiki/sources/metronome/source-metronome-guides-pricing-packaging-apply-credits-and-commits-target-credit-and-commits.md` → `raw/metronome/guides/pricing-packaging/apply-credits-and-commits/target-credit-and-commits-2026-07-13.md`.
- **Extra search:** None needed after following the prescribed route. I read the complete 176-line raw file for the paired detail task. Exact-link checks found one concept→source entry in the intended Sources section and one source→concept return link; the concept also has one supported semantic citation to the source. The source has one `raw_files` entry and one matching path-qualified Raw Sources link.
- **Verdict:** **PASS.** `metronome-credits-and-commits` directly represents restricting balance drawdown to selected usage; reciprocal navigation is present and unique in its intended sections, and the raw route is exact rather than manifest/attempt based.

## 4. Target credits/commits — detail

- **Answer:** Use `applicable_product_ids` or `applicable_product_tags` for simple product-ID or product-family filtering when complex AND/OR logic is unnecessary; usage matching any listed product ID or tag is eligible. Use `specifiers` for pricing-group values, presentation-group values, or advanced boolean logic. All fields inside one specifier are ANDed, while matching any separate specifier object makes the line item eligible (OR across objects). A pricing/presentation-group condition cannot match a product without the corresponding group key; subscriptions and composite products never have those group values and therefore do not draw down under such a specifier.
- **Evidence:** The exact selector choice is stated at `raw/metronome/guides/pricing-packaging/apply-credits-and-commits/target-credit-and-commits-2026-07-13.md:13-22`; specifier purpose and AND-within/OR-across matching are at lines 24-28; missing-group-key, subscription, and composite-product boundaries are at line 30. The source retains these behaviors at `wiki/sources/metronome/source-metronome-guides-pricing-packaging-apply-credits-and-commits-target-credit-and-commits.md:16-26`, and the reviewed concept paragraph preserves them at `wiki/concepts/metronome/metronome-credits-and-commits.md:37-39`.
- **Route:** Same prescribed index → main concept → source → exact raw route as task 3; raw detail locators: `Target with applicable_product_ids and applicable_product_tags` and `Target with specifiers`.
- **Extra search:** None. The exact raw guide fully answers the declared question; example payloads were read as part of the full raw read but were not expanded into cross-API claims.
- **Verdict:** **PASS.** Selector choice, boolean matching, and the consequential missing-dimension boundary are accurate and appropriately scoped.

## Four-task final verdict

**PASS — 4/4.** Both pages were retrievable through the required root index → Metronome index → purpose-fit main concept → approved source → exact raw path. All four answers are evidence-backed; both reciprocal concept/source routes are present and unique within their intended navigation sections; raw provenance is intact; no extra search or route repair was required.

## Concrete optimization observation

The provider-index description for `[[metronome-credits-and-commits]]` (`wiki/metronome-index.md:242`) mentions access schedules, rollover, and lifecycle but not usage applicability. Adding a short phrase such as “usage targeting” during the coordinator's normal catalog close would make the declared navigation question less dependent on already knowing that applicability belongs under credits and commits. This is a non-blocking discoverability improvement, not a failed route. For review efficiency, the promoted change also demonstrates that a bounded concept check can focus on the one new matching-logic paragraph plus the one Sources entry and reciprocal source link; rereading the unrelated remainder of the 357-line concept is unnecessary for this audit.
