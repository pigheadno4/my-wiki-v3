# Metronome Campaign 07 Independent Query-Quality Audit

Date: 2026-07-30
Repository: `/Users/tengtao/Development/wiki-v2`
Repository writes: none

## Outcome

Campaign recommendation: **approve**.

The three immutable manifest samples all passed. There are no material partials or failures, so the audit stops after the predetermined pages and does **not** expand to all ten Campaign 07 jobs.

| Result | Pages | Queries |
| --- | ---: | ---: |
| Pass | 3 | 9 |
| Partial | 0 | 0 |
| Fail | 0 | 0 |

All three raw hashes match the manifest, all three promoted sources are byte-for-byte identical to their final approved candidates, all three canonical URLs and path-qualified raw links are correct, and all ten required fact-bearing concept backlinks are present. No unsupported synthesis or required repair was found.

Materiality rule: a partial or fail is material when an answer-critical fact, boundary, contradiction, raw link, or required reciprocal fact citation is absent or incorrect. Cosmetic wording is not material.

## Expansion decision

**No expansion.** The manifest-selected standard page, longest/schema-heavy page, and ordinary sample each passed all three future-query tests. The ingest rule expands only when a selected page has a material partial or fail.

## 1. `subscription-overview` — pass

Final approved attempt: 2

Traceability:

- Raw SHA-256 matches: `cfb7010e563190d094f33fbdebcc41acd11fc87d1311d33d2074bdb2317b47d5`.
- Approved candidate and promoted source both hash to `9527682ee131913a947693adc188d30819ccaf7b5d74a748ecd44bd8fa8b8bbc`.
- Canonical URL matches the manifest.
- Frontmatter raw path and path-qualified Raw Sources link are correct.
- Fact-bearing backlinks are present in `metronome-subscriptions`, `metronome-products-and-rate-cards`, `metronome-customers-and-contracts`, and `metronome-credits-and-commits`.
- The company catalog and provider index both list the source.

| Future query | Type | Result | Evidence and assessment |
| --- | --- | --- | --- |
| How does Metronome model a subscription across products, rates, contracts, quantities, collection timing, and optional credits? | Core retrieval | Pass | Raw lines 11 and 23–39 are retained in source lines 18–36: recurring schedule, per-offering products, quantity-one rates, frequency variants, contract quantity/proration/collection direction, seats, and pooled or per-seat credits. |
| Can I treat `entitlement` as the exact API field, and does this overview define proration calculations, credit drawdown, seat rules, or lifecycle and invoice behavior? | Boundary/unknown | Pass | Source lines 38–40 and 51–53 preserve the `entitlement` versus `entitled` uncertainty and enumerate every excluded mechanic. The subscription concept repeats the terminology warning at lines 19–20. |
| Where should I go next for subscription pricing, customer provisioning, seat management, and lifecycle transitions? | Cross-link/deep dive | Pass | Source lines 42–58 retain all four route descriptions and link the subscription concept. That concept links the promoted pricing and lifecycle sources and adjacent concepts at lines 32–43; the exact raw page preserves the uninvented provisioning and seat routes. |

Specific defects: none.

## 2. `get-billable-metrics-for-customer` — pass

Final approved attempt: 1

Traceability:

- Raw SHA-256 matches: `c47a27686ec65742e9b341dd2e7b7cb6d4324e9541eafb2df12a468237a4954f`.
- Approved candidate and promoted source both hash to `337db051ca22d29f770507018bd87956ccefbae4e7deede57544bb5fb3b1d47a`.
- Canonical URL matches the manifest.
- Frontmatter raw path and path-qualified Raw Sources link are correct.
- Fact-bearing backlinks are present in `metronome-billable-metrics` and `metronome-customers-and-contracts`.
- The company catalog and provider index both list the source.

| Future query | Type | Result | Evidence and assessment |
| --- | --- | --- | --- |
| How do I list a customer's billable metrics, paginate the result, filter to the current plan or include archived metrics, and interpret the current versus deprecated response fields? | Core retrieval | Pass | Raw lines 90–134 and 225–310 are represented in source lines 14–82: bearer-authenticated endpoint, UUID scope, optional filters, `1`–`100` limit, cursor, required `data` and nullable `next_page`, required item fields, current fields, and all four deprecated fields. |
| What does `on_current_plan` mean with multiple or scheduled contracts, can I combine it safely with archived metrics and pagination, and should I trust the response example or `UNIQUE` for streaming distinct counts? | Boundary/contradiction | Pass | Source lines 34–36, 51–59, and 86–110 preserve plan, filter, cursor, error, archive, discriminator, and precedence unknowns. It flags the exclusion-list contradiction, unresolved `UNIQUE`, conflicting legacy/current grouping, and both `aggregation_key: bytes` example defects. The promoted create and metric-guide references independently support the `UNIQUE` conflict. |
| Where can I continue for generic cursor traversal, metric creation semantics, authentication, status-code behavior, and the broader customer/contract and billable-metric models? | Cross-link/deep dive | Pass | Source lines 112–120 directly link pagination, create, authentication, status codes, both concepts, and the raw snapshot. The billable-metrics concept integrates the retrieval API and cites this source at lines 51–73. |

Specific defects: none.

## 3. `pay-as-you-go` — pass

Final approved attempt: 2

Traceability:

- Raw SHA-256 matches: `388557d7e71ecfacc738b7cd9f19a35bc57e684b3e8760d4f0d73dd530f18232`.
- Approved candidate and promoted source both hash to `6aa57a60c5a8b7f4b813578bad7401a97f1acddd1b5d1341e382ca84e56c3084`.
- Canonical URL matches the manifest.
- Frontmatter raw path and path-qualified Raw Sources link are correct.
- Fact-bearing backlinks are present in `metronome-usage-based-billing`, `metronome-products-and-rate-cards`, `metronome-customers-and-contracts`, and `metronome-invoicing`.
- `metronome-integrations` is navigation-only; it retains no PayGo fact, so no reciprocal fact citation is required.
- The company catalog and provider index both list the source.

| Future query | Type | Result | Evidence and assessment |
| --- | --- | --- | --- |
| What building blocks and provisioning sequence does Metronome's PayGo example use for Basic, and how does it illustrate the Best upgrade? | Core retrieval | Pass | Raw lines 11, 43–50, 70–131, and 135–187 are represented in source lines 18–30: arrears definition, usage products plus monthly fee, premium tag, rate card, Basic override, monthly default, Stripe/Metronome mapping, and the bounded six-month Best sequence. |
| Does `send_invoice` automatically charge the preferred card, does `entitled` prove application access control, and can I copy the Best contract's top-level `ending_at` field as valid API schema? | Boundary/contradiction | Pass | Source lines 28–43 reject all three unsafe inferences. The promoted Stripe integration says `send_invoice` emails instructions and the default-payment-method requirement applies to `charge_automatically`; the promoted create-contract reference documents optional exclusive top-level `ending_before`. |
| Where can I deep-dive into Stripe invoice behavior, authoritative customer and contract schemas, contract provisioning, and the usage-billing, rate-card, customer-contract, and invoicing concepts? | Cross-link/deep dive | Pass | Source lines 45–53 link four source deep dives, five concepts, the company page, and the exact raw snapshot. Four fact-bearing concepts cite it reciprocally; the integrations concept is correctly navigation-only. |

Specific defects: none.

## Campaign recommendation

Approve Campaign 07 from the independent query-quality perspective. No repair is required, and the material-failure expansion rule is not triggered.

This recommendation is limited to the current promoted working-tree snapshot and the manifest-defined three-page content-quality sample. It does not replace campaign-wide mechanical validation of all ten jobs.
