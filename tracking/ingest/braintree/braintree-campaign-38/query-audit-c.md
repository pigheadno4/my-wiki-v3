# Braintree Campaign 38 fixed query audit — Group C

Analysis end: `2026-10-04T09:07:01Z`

Overall verdict: **PASS — 8/8 fixed questions across jobs 9–12.**

## Shared checks

- Read all four selected source pages and pinned raw snapshots in full. SHA-256 matches the manifest for all four: `a97a0449…177`, `ba3798a…f1e`, `7e3d205e…e29`, and `336e8c7e…7ff`.
- `wiki/index.md:8` routes to `[[braintree-index]]`. The provider index exposes each selected main concept once (`wiki/braintree-index.md:552,570`); every intended concept-to-source entry and source-to-main-concept return link is present once. Each source has one manifest-matching `raw_files` entry and one path-qualified Raw Sources link to the pinned raw.
- The filename/topic gap sweep found the four pinned pages and adjacent `raw/braintree/articles/moneris/reconciliation-2026-09-16.md`. No extra full read was needed: the fixed questions require no claim from that adjacent page, and source-listed related raw targets remain navigation-only. Deferred provider source-catalog entries were not treated as route failures because the approved route uses provider index → main concept.

## 9. Brazil reconciliation — PASS

**Route:** `wiki/index.md:8` → `wiki/braintree-index.md:570` → `wiki/concepts/payment-reconciliation-reporting.md:115` → `wiki/sources/braintree/source-braintree-articles-br-reporting-reconciliation-reconciliation.md:43,48` → `raw/braintree/articles/br/reporting-reconciliation/reconciliation-2026-09-16.md`.

1. **Documented scope:** This is the exact Braintree-hosted Brazil (`/articles/br/`) reconciliation document. It covers a monthly merchant statement, PayPal-account-to-bank sweep reconciliation, the combined PayPal/Braintree Unified Disbursement Report, and Braintree Control Panel/dispute reports. The page states no pricing model or settlement currency and supplies no sibling-region or independent bank authority. Raw locators: route metadata at `:1,6-9`; purpose at `:14-16`; combined-report/account arrangement at `:40-42`.
2. **Purpose, action, and consequential conditions:** Start with statement **Disbursement Details** and compare its **Total Disbursed** amount with deposits, but use the Unified Disbursement Report when partnering-bank debt repayment can divert settled funds. Batch-settlement sweep timing is conditional and bank visibility is stated as expected, not guaranteed. The Disbursement Summary is delayed one to three business days, permission-gated, excludes transaction fees, and is selected by merchant account/date; disputes route to the Disputes Financial Impact Report's **Disbursement Date**. Raw locators: `:19-30`, `:40-53`, `:57-66`, `:71-73`.

## 10. Moneris change your bank account — PASS

**Route:** `wiki/index.md:8` → `wiki/braintree-index.md:552` → `wiki/concepts/braintree-payment-platform.md:31` → `wiki/sources/braintree/source-braintree-articles-moneris-change-your-bank-account.md:50,60` → `raw/braintree/articles/moneris/change-your-bank-account-2026-09-16.md`.

1. **Documented scope:** This Braintree-hosted Moneris merchant-account article documents requesting a change to the business checking account used for settled-transaction payouts. The replacement account must be a Canadian-based business checking account; savings, deposit-only, and prepaid debit accounts are excluded. A USD-presenting merchant account is documented with a USD deposit account and a CAD fee account. It is a document-upload/account-support route, not independent Moneris policy or proof of a completed change or payout. Raw locators: `:14-21`, `:52-53`, `:71-78`.
2. **Purpose, action, and consequential conditions:** Upload either an embossed voided cheque or a signed official-letterhead bank letter through the Control Panel Business Uploads Tool. Online-banking and sample-cheque screenshots are rejected; the cheque needs the DBA/legal name, while the letter needs account/transit numbers, branch-officer signature/contact details, and an issue date within six months. Support reviews the upload and follows up only with the authorized signer, who is distinct from an Account Admin and cannot be managed in the Control Panel. Separate fee/funding accounts require documentation and purpose designation for each. Raw locators: `:19-25`, `:29-49`, `:58-66`, `:71-78`.

## 11. Moneris pricing and fees — PASS

**Route:** `wiki/index.md:8` → `wiki/braintree-index.md:552` → `wiki/concepts/braintree-payment-platform.md:32` → `wiki/sources/braintree/source-braintree-articles-moneris-pricing-fees.md:42,53` → `raw/braintree/articles/moneris/pricing-fees-2026-09-16.md`.

1. **Documented scope:** This is a Braintree-hosted Moneris account-route pricing document for the account-selected blended or interchange-plus model. It describes fee categories and operation-qualified treatment but gives no numeric rate or currency and is not Braintree Orchestration, an API contract, independent Moneris authority, or a merchant-specific agreement. Raw locators: fee categories/model dependency at `:17-30`; signup-selected model and blended/IC+ definitions at `:33-45`.
2. **Purpose, action, and consequential conditions:** The discount rate applies only to successful transactions and is deducted from daily disbursements; the per-transaction fee applies to all transactions, including refunds, non-$0 authorizations, voids, and gateway rejections. Refunds do not return original transaction fees. Voids incur the per-transaction fee, with associated void fees stated to return at the beginning of the following month. Chargebacks and pre-arbitrations incur a non-refundable fee regardless of outcome, while retrievals do not incur it “at this time.” Mailed statements are conditional on processing transactions; Control Panel summaries are separate. Raw locators: `:30`, `:48-57`, `:60-64`.

## 12. Moneris statements — PASS

**Route:** `wiki/index.md:8` → `wiki/braintree-index.md:570` → `wiki/concepts/payment-reconciliation-reporting.md:116` → `wiki/sources/braintree/source-braintree-articles-moneris-statements.md:46,55` → `raw/braintree/articles/moneris/statements-2026-09-16.md`.

1. **Documented scope:** This Braintree-hosted Moneris-route document describes a monthly processing statement mailed to the business address three to five business days after month start, only when transactions were processed. It covers sales, refunds, fees, chargebacks, account debits/credits, and deposit reconciliation. Only the Interchange and Wholesale Discount Fees section is expressly limited to interchange-plus accounts; the page states no currency or general account-eligibility rule. Raw locators: `:14-18`, `:41-43`.
2. **Purpose, action, and consequential conditions:** Use the card-type sales summary and daily activity totals to reconcile monthly activity and deposits; inspect Monthly Summary and Transaction Fees for assessed fees/chargebacks, Financial Details for daily debits/credits and destination account plus possible GST/HST, the interchange section for IC+-qualified fee type/amount/rate, and Chargeback Summary for amount/count/reason. “Should match” deposit language is reconciliation guidance, not payment, settlement, funding, or bank-receipt proof. Raw locators: `:21-38`, `:41-53`.
