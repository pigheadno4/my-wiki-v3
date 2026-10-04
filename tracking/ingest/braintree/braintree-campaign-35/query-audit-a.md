# Braintree C35 fixed query audit A

- Analysis end (UTC): `2026-10-04T05:58:52Z`
- Report handoff (UTC): `2026-10-04T06:00:14Z`
- Overall: **PASS — 8/8 fixed questions pass; no material retrieval failure**

## 1. `articles-wells-flat-chargebacks-retrievals-prearbs`

**Actual route:** `wiki/index.md:11,47` → `wiki/braintree-index.md:25,528` → `wiki/concepts/disputes.md:334` → `wiki/sources/braintree/source-braintree-articles-wells-flat-chargebacks-retrievals-prearbs.md:1-9,49,52-54` → `raw/braintree/articles/wells-flat/chargebacks-retrievals-prearbs-2026-09-16.md` (manifest SHA-256 `3d9940e3cff58885eb002fe311c420b5b4704c418b2f2b685da5fb34e43685ad`, verified).

- **Q1 — PASS.** Scope is the captured Braintree-owned **Wells Flat** credit-card-dispute route, not PayPal disputes, current independent Wells/card-network policy, or a universal Braintree schedule. The dated auto-accept rule is narrower still: US flat-rate merchants, pre-arbitrations under USD 1,000, “as of August 27th, 2025.” The same article's Pass-through Fee Report statements apply only to interchange-priced merchants and must not be transferred to the flat-rate scope. Locators: raw `17-18`, `48-58`, `167-200`; source `14,19,22,26-27`.
- **Q2 — PASS.** Purpose is to explain and operate the retrieval → chargeback → pre-arbitration → arbitration lifecycle through notifications, Control Panel/API responses, statuses, and reports. Material limits: arbitration is outside Braintree end-to-end support and accepts no further evidence; the reply-by opportunity closes at 12am in the account time zone and expiry sends Accept; non-auto-accepted pre-arbs should be represented only with new evidence, while the captured US-flat rule auto-accepts sub-USD-1,000 cases and permits a higher configured threshold. Detailed procedures/values: raw `23-58`, `63-84`, `87-129`, `134-200`, `203-238`; source locator map `32-44`.

## 2. `articles-wells-ic-chargebacks-retrievals-prearbs`

**Actual route:** `wiki/index.md:11,47` → `wiki/braintree-index.md:26,528` → `wiki/concepts/disputes.md:335` → `wiki/sources/braintree/source-braintree-articles-wells-ic-chargebacks-retrievals-prearbs.md:1-9,36-43` → `raw/braintree/articles/wells-ic/chargebacks-retrievals-prearbs-2026-09-16.md` (manifest SHA-256 `0ca6638f6061caf34962944a5cad33df33e72b2c834caea4951dbf7e53e2657e`, verified).

- **Q1 — PASS.** Scope is the captured Braintree-owned **Wells IC / interchange-pricing** credit-card-dispute route. It excludes PayPal disputes and must not be used as Wells Flat or other processor/account pricing. The raw explicitly assigns applicable arbitration/network pass-through fees and the Pass-through Fee Report to interchange-priced merchants; its USD 15 chargeback and pre-arb figures remain this captured Wells IC account evidence. Locators: raw `17-18`, `48-58`, `139-173`; source `14,20,23`.
- **Q2 — PASS.** Purpose is the same four-stage dispute lifecycle plus operational response/reporting for this IC scope. Consequential limits: arbitration creates no Braintree dispute, is absent from Control Panel/API/reports, and allows no additional evidence; reply-by expires at 12am in the account time zone and triggers Accept; contesting a chargeback or pre-arb needs timely evidence, with new/additional evidence especially consequential for pre-arbs; report access needs Create, Run, and Download Reports permission. Detailed procedures/values: raw `23-58`, `63-84`, `87-129`, `134-173`, `176-209`; source locator map `25-34`.

## 3. `articles-wells-ic-statements-reconciliation`

**Actual route:** `wiki/index.md:11,51` → `wiki/braintree-index.md:27,527` → `wiki/concepts/payment-reconciliation-reporting.md:111` → `wiki/sources/braintree/source-braintree-articles-wells-ic-statements-reconciliation.md:1-9,46-53` → `raw/braintree/articles/wells-ic/statements-reconciliation-2026-09-16.md` (manifest SHA-256 `7df26ee681adac4b8346f0c484514f1c1ab2e4fbcdc91bfc544a86e33bb26951`, verified).

- **Q1 — PASS.** Scope is captured Braintree **Wells IC+** merchant statements/reconciliation: interchange/pass-through fees and Braintree fees are separate, with aggregated-Amex versus merchant-owned-Amex treatment. It is not flat/blended pricing, Braintree Marketplace, another processor/account, current independent bank policy, or proof of a specific withdrawal/deposit. Multi-currency statements apply only to merchants with multi-currency merchant accounts. Locators: raw `14-18`, `74-121`, `181-201`; source `14-16,21-25,27-31`.
- **Q2 — PASS.** Purpose is to access/read statements and reconcile their Disbursement Details to bank deposits. Prerequisites/limits: Control Panel statement access needs View Statements; IC+ interchange and Braintree fees are withdrawn separately on the third business day of the following month; interchange uses settlement timing while Braintree fees use disbursement timing, so the volumes do not align; own-Amex disbursements are excluded; the stated 1–2-business-day bank appearance is an expectation, not deposit proof; Marketplace uses a separate guide. Detailed procedures/values: raw `23-54`, `74-121`, `127-178`, `181-201`; source locator map `33-44`.

## 4. `articles-wells-flat-statements-reconciliation`

**Actual route:** `wiki/index.md:11,51` → `wiki/braintree-index.md:28,527` → `wiki/concepts/payment-reconciliation-reporting.md:112` → `wiki/sources/braintree/source-braintree-articles-wells-flat-statements-reconciliation.md:1-9,40-48` → `raw/braintree/articles/wells-flat/statements-reconciliation-2026-09-16.md` (manifest SHA-256 `82342e3f1b84f5f82936873db11a581d637133bae1996587829783d618e863e2`, verified).

- **Q1 — PASS.** Scope is captured Braintree **Wells Flat** statements/reconciliation with merchant-account fee schedule and aggregated-Amex versus merchant-owned-Amex treatment. It does not establish IC+ rules, does not cover Braintree Marketplace statements, is not current independent bank policy, and does not prove a specific deposit. Multi-currency behavior is only for merchants with multi-currency merchant accounts. Locators: raw `17-18`, `76-105`, `172-192`; source `14,20-26`.
- **Q2 — PASS.** Purpose is to use statements—principally second-page Disbursement Details—to reconcile Braintree records to bank deposits. Prerequisites/limits: View Statements is required; Dashboard and Settlement Batch Summary must not be used for reconciliation; the disbursement date is send date, not availability date, with a captured 1–2-business-day expectation; own-Amex funds and certain report rows are excluded; Disbursement Summary requires Create, Run, and Download Reports permission; transaction-level fees use the dedicated report. Detailed procedures/values: raw `23-56`, `61-116`, `121-169`, `172-192`; source locator map `28-38`.

## Shared checks

- **Reciprocal routes:** PASS. Root exposes both `braintree-index` and the two generic concepts (`wiki/index.md:11,47,51`); Braintree index exposes all four sources (`25-28`) and both concepts (`527-528`); each concept links its assigned sources (`disputes.md:334-335`; `payment-reconciliation-reporting.md:111-112`); every source links back to its main concept and to the exact raw (`source` locators above). No selected source has a `Related raw API references` section requiring another evidence read.
- **Filename gap sweep:** sibling Wells raws found for Flat/IC pricing, Marketplace statements, and Flat pre-dispute programs, plus processor/region-specific dispute and reconciliation pages. None was needed to answer these exact pages: the four selected raws themselves state the ordinary-vs-Marketplace, Flat-vs-IC, account, pricing, report, deadline, and captured-authority boundaries. No contradictory extra evidence was discovered.
- **Non-blocking provenance caveat:** Wells Flat dispute raw frontmatter says `updateTime: 2025-08-19` (`raw:9`) while the body states a policy “As of August 27th, 2025” (`raw:172-173`). The body was fetched on 2026-09-16 and supports the captured statement, but this metadata mismatch reinforces that it must not be represented as independently current policy. It does not break retrieval or the source's qualified summary.
- **Material failures:** none.

## Verdict count

`8 PASS / 0 FAIL` — all fixed questions covered; close is not blocked by this audit.
