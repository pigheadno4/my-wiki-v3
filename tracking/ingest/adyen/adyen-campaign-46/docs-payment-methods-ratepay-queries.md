# Ratepay overview retrieval checks

## Q1 — Identity and scope

Query: What does Adyen's Ratepay overview cover, and can it prove today's merchant availability or a live payment?

Expected route: `wiki/index.md` PSP Indexes line 10 → `wiki/adyen-index.md` line 2557 → `wiki/concepts/adyen-online-payments.md` Sources → `wiki/sources/adyen/source-adyen-docs-payment-methods-ratepay.md` Overview/Detail locators → `raw/adyen/docs/payment-methods/ratepay/2026-09-15.md` `# Ratepay` lines 15–27 and `## How do you want to integrate?` lines 33–45. Expected answer: a 2022-modified, 2026-09-15-captured overview of Ratepay Open Invoice and secured direct debit, conditional risk/payout claims, a capability matrix, and Web/API-only links; no current enablement or live-payment proof.

## Q2 — Products, geography, and conflict

Query: Which Ratepay products and countries does the overview name, what does its matrix say, and how do risk and capture affect payout?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-ratepay.md` Key takeaways/Detail locators → `raw/adyen/docs/payment-methods/ratepay/2026-09-15.md` lines 23–31. Expected answer: Open Invoice prose lists AT, DE, NL, CH; secured direct debit prose lists AT, DE, NL; the combined matrix lists DE, AT, NL / EUR, “Additional action,” no recurring or chargebacks and checked refund/capture capabilities. Flag the internal CH mismatch. Risk transfer and up-front payment are stated only after successful preapproval risk checks; BNPL payment to the merchant is said to follow capture. Do not turn either conditional claim or the combined matrix into current account-specific eligibility.
