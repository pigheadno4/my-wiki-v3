# Braintree Campaign 39 query audit — group A

## Identity and timing

- Provider: **Braintree**
- Campaign: **braintree-campaign-39**
- Manifest: `/Users/tengtao/Development/wiki-v2/tracking/ingest/braintree/braintree-campaign-39/manifest.json`
- Exact jobs / queue positions: **1** `articles-nab-chargebacks-retrievals-prearbs`; **2** `articles-risk-and-security-chargebacks-retrievals-chargeback-reason-codes`; **3** `articles-risk-and-security-chargebacks-retrievals-disputing-chargebacks`; **4** `articles-nab-statements-reconciliation`
- Verified objects/actions before answering: NAB-labelled credit-card dispute management; Braintree-surfaced credit-card reason-code lookup; general bank-chargeback acceptance/dispute/evidence handling; NAB-labelled statement access and settlement/fee reconciliation.
- Analysis end UTC: `2026-10-04T15:01:01Z`
- Final handoff UTC: `2026-10-04T15:02:46Z`

## Shared checks

- **PASS — identity and integrity.** Provider/campaign/job paths, canonical URLs, source targets, and raw objects match the manifest. All four raw SHA-256 values match: `833f7ef...3147`, `a39b30f...52b`, `8169d647...f817`, `d62e921f...6bfe`.
- **PASS — retrieval path.** The root index routes to `[[braintree-index]]`; the Braintree index routes to `[[disputes]]` or `[[payment-reconciliation-reporting]]`; each concept routes to its promoted source; each source pins the manifest raw. Direct aggregate source catalog entries are deferred to close, so no nonexistent direct index-to-source hop is claimed.
- **PASS — bounded gap/conflict sweep.** Exact-topic filenames and distinctive claims were swept in existing `raw/braintree/`. The only additional authority required for a retained qualification was the fully read general Braintree chargeback overview source/raw. Navigation-only ACH and dispute-response references were not used as evidence.
- **PASS — NAB fee outcome qualification.** The generic Braintree overview says fee amount and debit point depend on merchant-account type (`raw/.../chargebacks-retrievals/overview-2026-09-16.md:45-47`). The NAB page is more specific: a merchant-favorable ruling returns the amount with no fee; loss or acceptance incurs the agreement-defined fee (`raw/.../nab/chargebacks-retrievals-prearbs-2026-09-16.md:94-106`). `[[disputes]]` retains this account-specific exception immediately after its generic “typically charged” statement; no universal fee outcome is asserted.

## Position 1 — `articles-nab-chargebacks-retrievals-prearbs`

**Actual route:** `wiki/index.md` → `[[braintree-index]]` → `[[disputes]]` → `[[source-braintree-articles-nab-chargebacks-retrievals-prearbs]]` → `raw/braintree/articles/nab/chargebacks-retrievals-prearbs-2026-09-16.md`

1. **PASS — exact scope.** This is a Braintree-hosted, NAB-labelled account/processor snapshot for **credit-card** chargebacks, retrievals, re-opens and pre-arbitrations; it excludes PayPal disputes to a separate guide. It was fetched `2026-09-16`, with page metadata dated `2025-04-01`; no region, jurisdiction, currency, pricing model or merchant-eligibility rule is stated. Raw locators: lines `1-18`, `90-101`, `130-150`.
2. **PASS — purpose/action and consequences.** It routes notifications and Control Panel/API handling, evidence or acceptance, reply-by cutoffs, fund/fee outcomes, retrieval response, NAB continuous-dispute treatment, statuses and reporting. Material limits: expiry at 12am in the account time zone sends acceptance and ends the evidence opportunity; the original amount is debited within seven days and held pending resolution; retrievals have 11 days, no fund removal and no processing fee; exact standard chargeback fee is in the pricing agreement. Raw locators: `25-46`, `49-85`, `90-127`, `130-150`, `153-175`.

## Position 2 — `articles-risk-and-security-chargebacks-retrievals-chargeback-reason-codes`

**Actual route:** `wiki/index.md` → `[[braintree-index]]` → `[[disputes]]` → `[[source-braintree-articles-risk-and-security-chargebacks-retrievals-chargeback-reason-codes]]` → `raw/braintree/articles/risk-and-security/chargebacks-retrievals/chargeback-reason-codes-2026-09-16.md`

1. **PASS — exact scope.** This is a general Braintree merchant-surfacing lookup for **received credit-card dispute** reason codes, organized by American Express, Diners, Discover, Elo, Hipercard, JCB, Maestro, Mastercard, UnionPay and Visa; JCB separately includes retrieval codes. The list was generated `2025-09-22`, may vary by processing region/payment network, may change, and may omit known codes. ACH return codes are expressly outside scope; no merchant-account or jurisdiction scope is stated. Raw locators: `1-23`, headings `## American Express` through `## Visa` (`26-401`).
2. **PASS — purpose/action and consequences.** Use the tables to interpret a surfaced code as the captured normalized reason/description, not as independent current network authority or an exhaustive eligibility/ruleset. Preserve the Visa representation rule: decimal codes are stored as four characters with a zero, e.g. `10.4` → `1040`. Exact values remain in the brand tables, including JCB retrieval `170-200`, JCB chargeback `203-293`, Mastercard `304-337`, and Visa `348-401`.

## Position 3 — `articles-risk-and-security-chargebacks-retrievals-disputing-chargebacks`

**Actual route:** `wiki/index.md` → `[[braintree-index]]` → `[[disputes]]` → `[[source-braintree-articles-risk-and-security-chargebacks-retrievals-disputing-chargebacks]]` → `raw/braintree/articles/risk-and-security/chargebacks-retrievals/disputing-chargebacks-2026-09-16.md`

1. **PASS — exact scope.** This is a general Braintree guide for accepting or disputing a customer’s **bank chargeback**; actual notifications, actions and evidence procedures depend on account setup and bank-specific articles. PayPal disputes use a separate route. The snapshot was fetched `2026-09-16`; its narrow body statement dated `2025-08-27` applies only to U.S. flat-rate merchants’ pre-arbitrations, not other regions/accounts or current universal policy. Raw locators: `1-18`, `102-104`, `122-134`.
2. **PASS — purpose/action and consequences.** It frames when to accept/dispute, evidence selection, beta recommendations, refund overlap and pre-arbitration decisions. Required compelling evidence applies to identified fraud or goods/services-not-received cases; without it, the card brand will not accept the dispute. A separate refund does not cancel/prevent a chargeback and can double the loss; Braintree disclaims liability after loss/acceptance of an already-refunded charge. Pre-arbitrations rarely win without new compelling evidence and carry a processing fee regardless of outcome; the dated U.S. flat-rate note auto-accepts under USD 1,000 and permits representation above USD 1,000. Raw locators: `21-44`, `47-99`, `107-117`, `122-134`.

## Position 4 — `articles-nab-statements-reconciliation`

**Actual route:** `wiki/index.md` → `[[braintree-index]]` → `[[payment-reconciliation-reporting]]` → `[[source-braintree-articles-nab-statements-reconciliation]]` → `raw/braintree/articles/nab/statements-reconciliation-2026-09-16.md`

1. **PASS — exact scope.** This is a Braintree-hosted, NAB-labelled account/processor snapshot for monthly **Transact** and **Merchant** statements plus daily settlement and monthly fee reconciliation. It was fetched `2026-09-16`, with page metadata updated `2025-05-19`; it states no region, jurisdiction, currency or single payment-method scope. Pricing-model qualifications apply to statement sections. Raw locators: `1-19`, `37-78`.
2. **PASS — purpose/action and consequences.** Merchant Statements are available by the ninth via Control Panel to users with `View Statements`; Transact Statements require Braintree support. Reconcile daily Settlement Batch Summary totals against bank statements and monthly Merchant/Transact fees against the bank fee debit. Next-day deposit wording is conditional on an NAB business banking account; another bank may delay arrival. Fees debit on the last business day, making interim deposits gross and expected to match the settlement batch. Exact section fields and procedures remain at raw `17-32`, `37-78`, `81-96`.

## Outcome

**APPROVE — 8/8 answers PASS.** No material retrieval failure or answer blocker. The retained NAB-versus-generic chargeback-fee qualification is explicit and correctly scoped.
