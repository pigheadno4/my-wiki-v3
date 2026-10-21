# C27 FX-fee disclosure retrieval checks

## Q1 — Purpose and scope

**Query:** What does the Marketplace financial-products FX-fee page ask a platform to present to a user?

**Answer:** For a transaction with currency conversion, the dated Adyen guideline says the FX rate and additional fees must be clearly presented at transaction time and in statements for the relevant period (raw lines 19–23). It illustrates variable, fixed and third-party-fee presentation; its closing note says UK FCA-derived guidance applies to marketplaces in all regions as Adyen guidance, while the page expressly disclaims legal advice (raw lines 25–101). Route: [[index]] → [[adyen-index]] → [[adyen-financial-products]] → [[source-adyen-docs-marketplaces-compliance-financial-products-foreign-exchange-fees]] → [[raw/adyen/docs/marketplaces/compliance-financial-products/foreign-exchange-fees/2026-09-15]].

## Q2 — Arithmetic and delivery boundary

**Query:** Can the fixed-fee table be used as a live conversion quote, and do the intermediary-fee examples prove the amount a beneficiary received?

**Answer:** No. The first Fixed Fee table pairs a 1.26 GBP/USD rate with £100 paid, £0 fixed fee, £3 total fees added and a £126.10 recipient amount, which does not reconcile in currency or arithmetic (raw lines 38–48). Other rows are illustrative fee arrangements (raw lines 50–72). The third-party examples contrast upfront `Pay all fees?` with recipient-paid deductions, while the text says intermediary banks may deduct fees; they do not prove an individual bank charge or beneficiary receipt (raw lines 74–99). Route: [[index]] → [[adyen-index]] → [[adyen-financial-products]] → [[source-adyen-docs-marketplaces-compliance-financial-products-foreign-exchange-fees]] → [[raw/adyen/docs/marketplaces/compliance-financial-products/foreign-exchange-fees/2026-09-15]].
