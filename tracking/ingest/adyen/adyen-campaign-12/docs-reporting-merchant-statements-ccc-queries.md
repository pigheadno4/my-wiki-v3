# Fixed queries — docs-reporting-merchant-statements-ccc

## Q1 — purpose, scope, and what not to infer

**Question:** For whom is the Canada Code of Conduct merchant statement guide intended, what is the report grain, and what does the resulting statement establish?

**Expected answer:** It is a Canada-focused method to build a merchant statement from PAR or IPAR for aggregate fees and effective merchant discount rate. The guide's transparency context is PCNO fees; its workflow groups costs first by PSP Reference, then calculates period totals by Payment Method. It does not say each PAR/IPAR row is a finished statement, prove statutory compliance, or prove receipt of payout funds in a bank. Route: [[index]] → [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-reporting-merchant-statements-ccc]] → [[raw/adyen/docs/reporting/merchant-statements-ccc/2026-09-15]]. Raw locators: opening lines 15–21; `How it works` lines 37–56; pivot and formulas lines 137–174.

## Q2 — capability, prerequisites, and warnings

**Question:** How are the statement amounts and effective merchant discount rate calculated, and which access, date, and currency conditions matter?

**Expected answer:** The guide requires Report service user for the API credential, lists Customer Area roles for configuring columns and Merchant report for generating/downloading, and requires Standard Webhook only if using automatically generated PAR instead of IPAR. Derived Main Amount (SC) equals Payable plus Commission plus Scheme Fees plus Interchange plus Markup, all in SC; commission is split into component registers when interchange-level data is provided. The pivot groups by PSP Reference and Payment Method; Total Cost of Payment sums interchange, scheme fees, markup, commission, and processing fees, and Effective Merchant Discount Rate divides total cost by Main Amount total. For multiple currencies, use exchange rates matching Booking Date, converting SC and FC fields to BC; choose the payments-only or platform/marketplace rate column as instructed. Confirm Processing Fee Currency before combining an FC figure with SC figures. Route: [[index]] → [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-reporting-merchant-statements-ccc]] → [[raw/adyen/docs/reporting/merchant-statements-ccc/2026-09-15]]. Raw locators: `Requirements` lines 23–35; column table lines 69–86; Main Amount lines 96–101; exchange-rate conversion lines 103–135; pivot and formulas lines 137–174.
