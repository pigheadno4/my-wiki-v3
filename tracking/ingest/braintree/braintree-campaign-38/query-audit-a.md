# Braintree Campaign 38 fixed query audit — Group A

- Provider: **Braintree**
- Exact jobs: `articles-br-chargebacks-retrievals-prearbs`; `articles-br-reporting-reconciliation-disbursement-report`; `articles-br-reporting-reconciliation-activity-report`; `articles-br-transactions-installments`
- Scope: exactly eight fixed questions; read-only repository audit
- Analysis completed (UTC): `2026-10-04T09:12:11Z`
- Bounded conflict correction completed (UTC): `2026-10-04T09:13:58Z`
- Overall verdict: **PASS (8/8)**
- Concrete retrieval failures / repairs: **none / none**

## Shared checks

- The Braintree root route is `wiki/index.md:11`. `wiki/braintree-index.md` exposes the main concepts at `:574` (`braintree-payment-methods`), `:591` (`payment-reconciliation-reporting`) and `:592` (`disputes`); its aggregate source catalog also contains the four selected Braintree sources at `:25-28`, but those entries were not substituted for the required concept hops.
- Concept-to-source routes are present at `disputes.md:332`, `payment-reconciliation-reporting.md:111-112` and `braintree-payment-methods.md:23`. Each selected source reciprocates to the same main concept and has matching `raw_files` and `## Raw Sources` provenance.
- All selected source pages and pinned raw snapshots were read completely. Manifest SHA-256 verification passed: chargebacks `f013f75d92662951e3cabac6ecdfd5a041793cb1b935059836be546b7d03ecb4`; disbursement report `4a20801ca86e68a407f045f9a77285d57636da01492e5b6e33c6d5468c7a97ca`; activity report `11895722fef97803d9b8272fe0387e3f436ca9088e1ea0b9fe91445171cf83ee`; installments `54ee1289105a14dc67da30da371f0cf036df11ad7427132a7941fb23ded6a96f`.
- The object/action sweep matched one BR credit-card dispute article, two distinct BR report documents and one BR credit-card installment article. Filename and exact-purpose searches found the four pinned raws plus sibling-region dispute variants; those variants do not answer the exact BR scope and were not selected. None of the four sources has a `## Related raw API references` section. One retained installment conflict required and received a complete extra read of `raw/braintree/articles/br/payment-capabilities-2026-09-16.md` (57 lines): its final-installment remainder rule qualifies the selected article's unreconciled equal-split wording.

## 1. Braintree BR chargebacks, retrievals and pre-arbs — PASS (2/2)

Braintree route: `wiki/index.md:11` → `wiki/braintree-index.md:592` → `wiki/concepts/disputes.md:332` → `wiki/sources/braintree/source-braintree-articles-br-chargebacks-retrievals-prearbs.md` → `raw/braintree/articles/br/chargebacks-retrievals-prearbs-2026-09-16.md`.

**Q1 — What exact region/account/processor/document/pricing scope is documented?**

This is a Braintree-hosted **BR/Brazil route** snapshot for **credit-card** chargebacks, retrievals and pre-arbitrations; PayPal disputes are explicitly routed elsewhere (`raw.../chargebacks-retrievals-prearbs-2026-09-16.md:14-22`). Notifications, permissions, sub-merchant visibility, Control Panel interface and reply cutoff are account-sensitive (`:25-46`, `:49-85`). The article names a chargeback fee but gives no amount or currency, so it is not a transferable price schedule, sibling-region rule or independent bank/network authority.

**Q2 — What central purpose/action, consequential prerequisites, warnings and limitations are documented, and where are details in raw?**

The article tells merchants how to receive, manage, accept or contest these credit-card disputes. Every case has a reply-by date; at **12am in the account time zone**, evidence submission closes, expiration sends Accept on the merchant's behalf and removes the documented right to dispute (`:77-85`). Generally, opening a chargeback causes no debit or fee; acceptance or loss later debits the disputed amount plus a fee, and a loss can be debited up to 120 days after representment or rarely later (`:90-111`). Retrievals are non-financial and fee-free (`:114-120`); pre-arbs are second disputes where new compelling evidence matters (`:123-129`). Status and report details, including rare debit-at-Open behavior and installment adjustments, are at `:132-175`.

## 2. Braintree Brazil Disbursement Report — PASS (2/2)

Braintree route: `wiki/index.md:11` → `wiki/braintree-index.md:591` → `wiki/concepts/payment-reconciliation-reporting.md:111` → `wiki/sources/braintree/source-braintree-articles-br-reporting-reconciliation-disbursement-report.md` → `raw/braintree/articles/br/reporting-reconciliation/disbursement-report-2026-09-16.md`.

**Q3 — What exact region/account/processor/document/pricing scope is documented?**

This is Braintree's exact **Brazil `/articles/br/` Disbursement Report, document version 1.1**, for reconciling daily PayPal and Braintree deposits to a system of record (`raw.../disbursement-report-2026-09-16.md:14-24`, `:240-245`). In the documented Brazil route, the Funding Account is always a PayPal Account Number because both PayPal Wallet and credit/debit-card transactions are disbursed through a PayPal account (`:61-71`). It documents report data, not account availability, delivery/access, current eligibility, merchant pricing rates, bank policy or proof of fund arrival.

**Q4 — What central purpose/action, consequential prerequisites, warnings and limitations are documented, and where are details in raw?**

Use the report's Header, Summary, Detail and Footer to reconcile batch totals and event rows (`:27-55`): match the bank-statement PayPal deposit to Summary **Net Disbursed Amount**, group Detail rows by **Funding Account**, and sum **Net Disbursed** (`:61-71`). Sales/refund, installment and dispute filters and identifiers are at `:74-112`; Summary may carry a prior failed disbursement into the current day's amount (`:132-143`). Detail distinguishes created, settlement and disbursement dates plus transaction versus settlement currency and exchange rate (`:146-185`). Preserve the source defects that RD and RF descriptions incorrectly say their rows belong to Summary (`:150`, `:192`); the report remains reconciliation evidence, not settlement/fund-arrival proof.

## 3. Braintree Brazil Activity Report — PASS (2/2)

Braintree route: `wiki/index.md:11` → `wiki/braintree-index.md:591` → `wiki/concepts/payment-reconciliation-reporting.md:112` → `wiki/sources/braintree/source-braintree-articles-br-reporting-reconciliation-activity-report.md` → `raw/braintree/articles/br/reporting-reconciliation/activity-report-2026-09-16.md`.

**Q5 — What exact region/account/processor/document/pricing scope is documented?**

This is Braintree's **Brazil Activity Report, document version 1.1**, a daily report of the previous processing day's transactions in **Submitted for Settlement** or **Settlement Declined** state (`raw.../activity-report-2026-09-16.md:14-32`, `:185-190`). It covers credit/debit sales and refunds, new installments and installment adjustments. The Brazil snapshot states 2–30 days depending on card type, default 30 days, with 30 days for credit and 2 for debit; Predefined Funds Anticipation can accelerate credit-card funding for a premium (`:35-44`). It gives no premium price, account eligibility or SLA and is not settlement, disbursement or deposit proof.

**Q6 — What central purpose/action, consequential prerequisites, warnings and limitations are documented, and where are details in raw?**

The report supports receivables forecasting by storing projected disbursement dates and total fees (`:22-32`). Standard sale/refund matching uses Record Type, Record ID and Projected Disbursement Date (`:47-55`). A new installment's projected date starts `NULL`, is described as populated within twelve hours, and should be stored separately for later reconciliation (`:57-75`). Refunds and lost disputes adjust every installment equally; adjustments to already-disbursed installments are netted from the next disbursement and must be tracked separately (`:78-123`). Merchant-account, presentment/settlement currency and amount, projected-date and total-fee fields are at `:130-157`; projected dates and Submitted-for-Settlement status are forecasts, not completion evidence.

## 4. Braintree Brazil installment transactions — PASS (2/2)

Braintree route: `wiki/index.md:11` → `wiki/braintree-index.md:574` → `wiki/concepts/braintree-payment-methods.md:23` → `wiki/sources/braintree/source-braintree-articles-br-transactions-installments.md` → `raw/braintree/articles/br/transactions/installments-2026-09-16.md`.

**Q7 — What exact region/account/processor/document/pricing scope is documented?**

This is a Braintree **Brazil credit-card installment** article, not generic BNPL or PayPal Pay Later guidance. It describes installments 30 days apart in sets of 2–12, with unspecified associated fees (`raw.../installments-2026-09-16.md:14-16`). It says the account is set up by default for Visa, Mastercard, Amex, Elo and Hipercard, but does not define activation or merchant eligibility (`:19-29`); installments are credit-card-only and combo cards use `account_type` (`:31-33`). The total is in BRL, split equally, and must calculate to at least 5 BRL per installment (`:92-95`); no fee schedule or rounding rule is documented.

**Q8 — What central purpose/action, consequential prerequisites, warnings and limitations are documented, and where are details in raw?**

Create an installment sale with the total amount and integer count 2–12; the prose labels `installmentCount:String`, while the Ruby example uses nested `installments` / `count`, so the linked request reference must resolve the displayed-shape difference (`:36-90`). Submit for settlement immediately or later; later submission remains subject to authorization expiry, and an adjusted settlement total must be no greater than the authorization while preserving the 5-BRL minimum (`:108-146`). The selected raw says the total is split equally but gives no non-even rounding rule; the fully read Braintree Brazil Payment Capabilities raw says a non-even remainder is paid with the final installment (`raw/braintree/articles/br/payment-capabilities-2026-09-16.md:31-33`). Preserve that cross-page qualification rather than silently treating the selected article as a complete allocation rule. Refunds and chargebacks adjust installments (`installments-2026-09-16.md:151-182`), and the Search API or Control Panel exposes IDs, amounts, projected/actual clearing dates and adjustments (`:185-218`). Those response and timing fields do not prove authorization, settlement, clearing, disbursement or funding.

## Adjudication

All eight Braintree group-A answers passed. No new material defect was found beyond the preserved installment equal-split/final-remainder qualification; no broken route, provenance mismatch or corrective repository write was required.
