# Braintree C24 fixed query audit — Group C

Scope: Billing Cycles + Trial Periods; four fixed questions from `selection-review.md`. Verdict: **4/4 PASS**.

## Evidence integrity

- Billing Cycles pinned raw: `raw/braintree/articles/guides/recurring-billing/billing-cycles-2026-09-16.md`; computed SHA-256 `36d4a0ad2b8ba52dc7b3ccd06bb175c24a455df0768f4a38aef6874c81b9def9` = manifest.
- Trial Periods pinned raw: `raw/braintree/articles/guides/recurring-billing/trial-periods-2026-09-16.md`; computed SHA-256 `4de9ff59d3ad3f03c8dbb63264065b20eeed7af90e21c2454d22c50a2127fa3e` = manifest.
- Both pinned raws and both exact source pages were read completely.

## Billing Cycles

Actual route: `[[index]]` → `[[braintree-index]]` → `[[braintree-recurring-billing]]` § Billing cycles → `[[source-braintree-recurring-article-billing-cycles]]` → `[[raw/braintree/articles/guides/recurring-billing/billing-cycles-2026-09-16]]`.

1. **Navigation — requested object/action:** locate the article-level recurring-billing **Billing Cycles** article, not a Node guide or subscription API reference. **Direct answer:** the route above reaches the dedicated Billing Cycles source page and its exact pinned raw. **Raw locator:** `# Billing Cycles`, line 14 (identity), with purpose at lines 16–20. **PASS**.
2. **Detail — requested object/action:** report the timing and lifecycle qualifications stated by this article itself. **Direct answer:** cycle length is in monthly increments and is shared by subscriptions in a plan. Charging begins at 9am UTC on the billing date, but runs occur a couple of times daily, so processing is not simultaneous; transactions are submitted for settlement on the chosen date and the article says funds are collected immediately even on weekends/holidays, with declined-payment retry logic configured separately. Billing can start immediately or on a future date; immediate starts anchor to the signup calendar date, while starts on the 29th–31st fall on the last day of the first month in a cycle, so the article recommends a future date present in every month. On the final cycle, `Next Bill Date` is the subscription's final date. A new subscription may override the plan billing date, but its billing date cannot change after creation; cancellation and recreation are recommended. A finite cycle count determines expiry, `Never expires` is available, and a new subscription may override the plan's cycle count. **Raw locator:** `# Billing Cycles`, lines 16–20; `## How it works > ### Billing cycle length`, lines 25–35; `### Billing date`, lines 40–44; `#### Identifying the next billing date`, lines 49–60; `#### Changing the billing date`, lines 67–69; `### Number of billing cycles`, lines 74–76. **PASS**.

## Trial Periods

Actual route: `[[index]]` → `[[braintree-index]]` → `[[braintree-recurring-billing]]` § Trial periods → `[[source-braintree-recurring-article-trial-periods]]` → `[[raw/braintree/articles/guides/recurring-billing/trial-periods-2026-09-16]]`.

3. **Navigation — requested object/action:** locate the article-level recurring-billing **Trial Periods** article, not a creation guide or plan/API reference. **Direct answer:** the route above reaches the dedicated Trial Periods source page and its exact pinned raw. **Raw locator:** `# Trial Periods`, line 14 (identity), with purpose at lines 17–24. **PASS**.
4. **Detail — requested object/action:** report the trial timing and billing consequences stated by this article itself. **Direct answer:** a trial delays the first billing date and may be applied case by case or attached to a plan for new subscriptions. Trial time does not consume billing cycles (the article's three-month-trial plus twelve-month-plan example lasts fifteen months). A payment method is still required when the subscription starts, and the customer is charged automatically the day after the trial ends. Braintree does not alert customers by default when they enter the first billing cycle; the merchant must provide advance notice and an opt-out. The article calls failure to do so negative-option billing, says it increases chargeback risk and is generally prohibited among banking partners, and strongly recommends notifying the customer of the first billing date near trial end. **Raw locator:** `# Trial Periods`, lines 17–24; `## Risks and requirements`, lines 27–33. **PASS**.

## Shared bounded checks

- **Gap sweep:** one bounded filename/path sweep for recurring-billing, billing-cycle and trial-period raws plus a content/ownership sweep for `billing cycle`, `Next Bill Date`, `trial period`, and `negative option billing` found adjacent article, Node/API, account-updater, chargeback and navigation-only routes. The fixed questions explicitly ask what each selected article itself says, and both pinned raws answer them directly; no extra raw was needed or fully read. No conflicting evidence affecting these four answers was found.
- **Reciprocal/navigation links:** root index → Braintree index passes; Braintree index → recurring-billing concept and both selected sources passes; concept → both sources passes; each source → concept and exact raw passes. Each pinned raw is owned through `raw_files` by its exact source page; the other occurrence in the subscriptions source is explicitly navigation-only, not duplicate evidence ownership. **PASS**.
