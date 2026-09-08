# Campaign 40 final retrieval audit — Group A

- Scope: one final retrieval audit of exactly six predetermined questions; read-only repository review
- Started (UTC): `2026-09-08T13:38:22Z`
- Initial audit completion (UTC, before correction): `2026-09-08T13:46:58Z`
- Wrong-object correction started (UTC): `2026-09-08T13:48:09Z`
- Corrected completion (UTC): `2026-09-08T13:52:08Z`
- Correction elapsed: `00:03:59`
- Overall verdict: **PASS (6/6) after correcting an audit-execution error in Q3-Q4**
- Concrete retrieval failures: **none**
- Repairs required: **none**
- Audit-execution correction: the first pass incorrectly substituted **credit** for the assigned **commit** in Q3-Q4. Those two initial verdicts were invalidated and rerun below. This was an auditor object-selection error, not a source, route, or wiki failure.

## Audit boundary and method

I followed the live retrieval route, not campaign manifests, receipts, attempts, or supplied raw-path shortcuts:

`wiki/index.md` → `wiki/metronome-index.md` → relevant promoted concept route → source summary → exact raw snapshot.

The root Metronome route is visible at `wiki/index.md:5-10`. At corrected verification, the provider concept routes are `wiki/metronome-index.md:254` (credits and commits), `wiki/metronome-index.md:257` (products and rate cards), and `wiki/metronome-index.md:265` (alerts and notifications). Company/provider source catalogs are aggregation surfaces and were not treated as required audit hops.

The three selected raw snapshots were read completely:

1. `raw/metronome/api-reference/rate-cards/get-rates-2026-07-13.md` (492 lines; SHA-256 `671370310f26605f6daabc770a111a24461738b9efe9dee54eee46d05c7900b2`)
2. `raw/metronome/api-reference/credits-and-commits/archive-a-commit-2026-07-13.md` (210 lines; SHA-256 `d41b201f720705d7f66b1791fadcdde0d8ce3ab922ba49e1cc0aa63a651b7c93`)
3. `raw/metronome/guides/customers-billing/set-up-notifications/threshold-notifications-2026-07-13.md` (244 lines; SHA-256 `23b06ecf3425aa23644658a81d5f2e5fc258777842ccbc44f5586b760c265102`)

One related raw API reference was also needed and read completely for the customer-contract branch of Q1:

- `raw/metronome/api-reference/contracts/get-the-rate-schedule-for-a-contract-2026-07-13.md` (504 lines; SHA-256 `9d9c8ef4ef07560fa2ea396bc25497c5c247f5de337014956985e6018c4104ea`)

## Navigation and reciprocity checks

| Question group | Actual concept → source route | Source → concept backlink | Uniqueness in intended concept section | Result |
| --- | --- | --- | --- | --- |
| Rates | `wiki/concepts/metronome/metronome-products-and-rate-cards.md:146-148` → `source-metronome-api-reference-rate-cards-get-rates` | `wiki/sources/metronome/source-metronome-api-reference-rate-cards-get-rates.md:34-39` | Exact source link occurs once, in `## Sources` | PASS |
| Commit archive | `wiki/concepts/metronome/metronome-credits-and-commits.md:24-26,267-269` → `source-metronome-api-reference-credits-and-commits-archive-a-commit` | `wiki/sources/metronome/source-metronome-api-reference-credits-and-commits-archive-a-commit.md:31-34` | One route in `## Sources`; the supported lifecycle citation is not a duplicate catalog entry | PASS |
| Threshold | `wiki/concepts/metronome/metronome-alerts-and-notifications.md:91-93` → `source-metronome-guides-customers-billing-set-up-notifications-threshold-notifications` | `wiki/sources/metronome/source-metronome-guides-customers-billing-set-up-notifications-threshold-notifications.md:32-35` | Exact source link occurs once, in `## Sources` | PASS |

Each source's `raw_files` entry and `## Raw Sources` link resolve to the same exact existing raw path: rates at source lines 7-8 and 41-43; archive at lines 7-8 and 36-38; threshold at lines 7-8 and 37-39. A supported inline citation elsewhere is not counted as a duplicate Sources-catalog route. No duplicate exists for these three concept routes.

At corrected verification, the provider Sources catalog also lists the three selected sources once each at `wiki/metronome-index.md:26-28`. Those aggregate entries do not duplicate the purposeful concept routes and were not used as a source-path shortcut.

## Six-question audit

### Rates

#### Q1 — Where find a product rate-card price at a particular time, and customer-contract overrides?

**Verdict: PASS.**

Actual route:

`wiki/index.md:9` → `wiki/metronome-index.md:257` → `wiki/concepts/metronome/metronome-products-and-rate-cards.md:146-148` → `wiki/sources/metronome/source-metronome-api-reference-rate-cards-get-rates.md:12-23` → exact raw `raw/metronome/api-reference/rate-cards/get-rates-2026-07-13.md`.

Retrieved answer:

- Use bearer-authenticated `POST /v1/contract-pricing/rate-cards/getRates` to retrieve a rate card's schedule and display the product price at a given timestamp (`raw/.../rate-cards/get-rates-2026-07-13.md:9-13`, `:90-106`).
- For a specific customer's contract, inclusive of contract-level overrides, use `getContractRateSchedule`; the rate-card raw states this boundary directly (`raw/.../rate-cards/get-rates-2026-07-13.md:13`, `:103-105`).
- Following the source's `## Related raw API references` route (`wiki/sources/metronome/source-metronome-api-reference-rate-cards-get-rates.md:45-47`) and fully reading it confirms `POST /v1/contracts/getContractRateSchedule` considers the contract's rate card, scheduled changes, and contract overrides and returns entitled rates (`raw/metronome/api-reference/contracts/get-the-rate-schedule-for-a-contract-2026-07-13.md:9-13`, `:99-105`).

No repair needed.

#### Q2 — What timestamp and product/pricing-group selectors are documented, and where are returned rate details?

**Verdict: PASS.**

Actual route: same route as Q1, with source detail locators at `wiki/sources/metronome/source-metronome-api-reference-rate-cards-get-rates.md:25-32` and full raw verification.

Retrieved answer:

- Payload requires `rate_card_id` and date-time `at`; `at` is the inclusive starting point for the rate schedule (`raw/metronome/api-reference/rate-cards/get-rates-2026-07-13.md:160-173`).
- `selectors` are ORed across selector objects; passing none returns all rates (`:174-181`). An individual selector can use subscription `billing_frequency`, exact `product_id`, `product_tags` (matching any supplied tag), exact `pricing_group_values` (all key/value pairs), or `partial_pricing_group_values` (returned rate contains the supplied pairs) (`:227-272`).
- Success returns `data[]` of `RateSchedule`. Required entry fields are product ID/name/tags/custom fields, `starting_at`, `entitled`, and `rate`; optional details include `pricing_group_values`, `ending_before`, `commit_rate`, and `billing_frequency` (`:182-226`). The nested details are under `Rate`, `CommitRate`, `Tier`, `MinimumConfig`, and `CreditType`, as accurately routed by source line 32.

No repair needed.

### Commit archive

#### Q3 — Where deactivate an erroneous commit while keeping history?

**Verdict: PASS.**

Actual route:

`wiki/index.md:9` → `wiki/metronome-index.md:254` → `wiki/concepts/metronome/metronome-credits-and-commits.md:24-26` (purposeful lifecycle route; also cataloged once at `:267-269`) → `wiki/sources/metronome/source-metronome-api-reference-credits-and-commits-archive-a-commit.md:12-23` → exact raw `raw/metronome/api-reference/credits-and-commits/archive-a-commit-2026-07-13.md`.

Retrieved answer: use bearer-authenticated `POST /v2/contracts/commits/archive` to deactivate a customer- or contract-level commit while preserving historical records (`raw/.../archive-a-commit-2026-07-13.md:9-17`, `:99-109`).

No repair needed.

#### Q4 — What finalized-invoice prerequisites, then balance/ledger/access-schedule/default-list effects?

**Verdict: PASS.**

Actual route: same route as Q3; the source surfaces both finalized-invoice prerequisite classes and the consequential full-deactivation warning before routing to raw (`wiki/sources/metronome/source-metronome-api-reference-credits-and-commits-archive-a-commit.md:14-23`).

Retrieved answer:

- Every finalized **usage invoice** to which the commit was applied and every finalized **commit-payment invoice** must first be voided. The documented correction flow is: void the affected finalized usage invoice and associated finalized commit-payment invoice → archive the commit → regenerate the voided usage invoice without that commit (`raw/metronome/api-reference/credits-and-commits/archive-a-commit-2026-07-13.md:11-17`).
- After archival, the commit is omitted by default from `listCustomerCommits` and `listCustomerBalances`; pass `include_archived` to retrieve it (`:19-20`).
- It has a null ledger and zero remaining balance (`:21`).
- Its entire access schedule is deactivated; use commit editing or a manual ledger entry when only reducing the amount (`:22`).

No repair needed.

### Threshold

#### Q5 — Where compare balance, spend/usage, and invoice thresholds?

**Verdict: PASS.**

Actual route:

`wiki/index.md:9` → `wiki/metronome-index.md:265` → `wiki/concepts/metronome/metronome-alerts-and-notifications.md:91-93` → `wiki/sources/metronome/source-metronome-guides-customers-billing-set-up-notifications-threshold-notifications.md:12-30` → exact raw `raw/metronome/guides/customers-billing/set-up-notifications/threshold-notifications-2026-07-13.md`.

Retrieved answer: use the `Threshold notifications` guide, especially `## Threshold notification types`, which places Commit & Credit, Spend & Usage, and Invoice notifications side by side (`raw/.../threshold-notifications-2026-07-13.md:9-26`, `:28-112`). The source summary correctly advertises that section and its detailed locators (`wiki/sources/metronome/source-metronome-guides-customers-billing-set-up-notifications-threshold-notifications.md:14-19`, `:25-30`).

No repair needed.

#### Q6 — What does each category measure, and what is the explicit individual-seat-credit exclusion?

**Verdict: PASS.**

Retrieved answer:

- Commit & Credit thresholds measure remaining customer- or contract-level commit/credit balances. Individual seat-scoped credits are explicitly excluded from these calculations; seat monitoring has the separate `low_remaining_seat_balance_reached` type and `seat_filter` (`raw/metronome/guides/customers-billing/set-up-notifications/threshold-notifications-2026-07-13.md:15-24`, `:29-76`).
- Spend thresholds measure usage-based spend in the current billing period before commit/credit drawdown; usage drawdowns count, but commit purchases do not. Billable-metric usage thresholds measure the chosen metric's usage in the current billing period, defined from the earliest start through latest end across active invoices (`:79-100`).
- Invoice thresholds evaluate each active invoice independently against its net total after credits, commits, and other adjustments, limited to the specified currency (`:103-110`).

No repair needed.

## Existing query gap sweep

Commands run against `raw/metronome/**/*.md`:

1. Filename sweep for `(rate.*schedule|schedule.*rate|archive.*credit|credit.*archive|threshold.*notification|notification.*threshold)`.
2. Content sweep for rate timestamp/contract-override phrases.
3. Content sweep for finalized usage-invoice/commit-payment-invoice/null-ledger/full-access-schedule phrases.
4. Content sweep for category/seat-exclusion/invoice-after-drawdown phrases.
5. Check the three selected source pages for `## Related raw API references`.

Results and adjudication:

- The exact three selected raws were found.
- The rate sweep also found `raw/metronome/api-reference/rate-cards/get-a-rate-schedule-2026-07-13.md`. Its header/intro was inspected but it was not used as evidence: the promoted `get-rates` source has a different exact raw path and fully answers the current rate-card query. No equivalence or supersession was inferred.
- The selected get-rates source has one related raw route, the contract rate schedule. Because Q1 explicitly asks about customer-contract overrides, that related raw was needed and was read completely. It confirmed the route and boundary; no additional promotion or repair is needed.
- The corrected commit-specific filename sweep found the exact `archive-a-commit` raw; the directory-name pattern also surfaced `archive-a-credit`, which is the wrong object and was excluded. The content sweep additionally surfaced `edit-contract` and the credit archive because of shared lifecycle language. The exact commit-archive raw completely answers Q3-Q4, so no extra raw was needed.
- Threshold-adjacent hits included threshold-alert CRUD references and the prepaid-balance-thresholds guide. They cover configuration/status or automatic recharge rather than the requested side-by-side notification taxonomy. The selected threshold-notifications raw completely answers Q5-Q6, so no extra raw was needed.
- The archive and threshold selected source pages have no `## Related raw API references` section. The get-rates related reference was handled as above.

## Consolidated failures and repairs

- Retrieval failures: none.
- Final corrected answers wrong: none.
- Broken raw routes: none.
- Missing concept reciprocity: none.
- Duplicate navigation in intended concept sections: none.
- Repairs: none.

Audit correction record: the initial Q3-Q4 credit audit was a wrong-object execution error by this auditor. It was not counted as a source retrieval failure. Q1-Q2 and Q5-Q6 were preserved without reread; only Q3-Q4 were rerun from the live commit route, with the exact commit raw read completely and the commit-specific gap sweep repeated.

Repository note: no repository file was changed by this audit. The only audit output is `/private/tmp/c40-audit-a.md`; pre-existing modified/untracked repository state was left untouched.
