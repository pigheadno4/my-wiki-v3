# Walley API-only retrieval checks

## Q1 — Scope and availability

Query: What is the Walley API-only page for, and can it prove current country/account eligibility or live success?

Expected route: `wiki/index.md` PSP Indexes line 10 → `wiki/adyen-index.md` line 2610 → `wiki/concepts/adyen-online-payments.md` Sources → `wiki/sources/adyen/source-adyen-docs-payment-methods-walley-api-only.md` Overview/Detail locators → `raw/adyen/docs/payment-methods/walley/api-only/2026-09-15.md` `## Requirements` lines 21–26 and `## Build your payment form for Walley` lines 28–52. Expected answer: 2023-modified API-only custom Web form/redirect guide with v66 minimum, Support-assisted test setup and distinct B2C/B2B types; no current enablement or live-processing proof.

## Q2 — Flow, capture and source warnings

Query: What are Walley B2C/B2B data and country rules, how are redirect, pending results, capture and refund handled, and which examples should be treated cautiously?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-walley-api-only.md` Key takeaways/Detail locators → `raw/adyen/docs/payment-methods/walley/api-only/2026-09-15.md` lines 32–69, 71–110, 351–427, 429–538, 540–618. Expected answer: discovery pairs DK/DKK, FI/EUR, NO/NOK, SE/SEK, with DK/DKK B2C only and walley_b2b requiring company.name; phone/email and specified item fields required. Redirect action and URL-decoded redirectResult go through /payments/details, while Pending/Received awaits AUTHORISATION webhook. Capture after goods sent within 90 days; immediate auto capture may encounter asynchronous 403, so delayed/manual paths apply; B2B partial capture needs matching item data, and remainder needs manual cancellation. Cancel before capture, refund after; partial refund item sum must match amount. Warnings: NO/EUR examples conflict with NO/NOK discovery, partial-capture sample URL and PSP-reference fields are inconsistent, and sample received status is not final capture proof.
