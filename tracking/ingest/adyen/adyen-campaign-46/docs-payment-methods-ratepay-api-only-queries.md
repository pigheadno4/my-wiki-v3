# Fixed retrieval queries — Ratepay API-only

## Q1 — Identity and scope

**Query:** What does Adyen's Ratepay API-only guide cover, and what should a reader not infer?

**Expected:** The 2026-09-15-captured guide at `https://docs.adyen.com/payment-methods/ratepay/api-only` adds Ratepay to an existing API-only integration: merchant-built payment form, server API requests, Open Invoice and Direct Debit fields, results and modifications. It does not prove account enablement, a working executable sample, current eligibility or live transaction success. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-ratepay-api-only.md` → `raw/adyen/docs/payment-methods/ratepay/api-only/2026-09-15.md`. Evidence: raw `# Ratepay for API only` lines 15–28 and `## Test and go live` lines 1576–1582.

## Q2 — Request, method distinction and capture

**Query:** How do the Ratepay API-only Open Invoice and Direct Debit paths differ, and what warnings govern capture and examples?

**Expected:** Test Customer Area setup and API-only integration first. Optional `/paymentMethods` lookup lists AT/EUR, DE/EUR, NL/EUR and CH/CHF; Open Invoice `ratepay`, Direct Debit `ratepay_directdebit`, with Direct Debit unavailable in CH (raw lines 23–49). Shopper name, DOB, telephone, email, billing address, conditional delivery address, fingerprint and `lineItems` are required in the payment path; Direct Debit additionally has bank country, IBAN and owner (raw lines 53–88, 745–761). Its Direct Debit table says `ratepay_directdebit`, but curl and repeated SDK examples use `ratepay` (raw lines 749, 784–785, 1099–1100); no corrected payload or success is proven. The introduction's general capture statement is narrowed by the detailed `## Capture the payment` section expressly limited to Open Invoice (raw lines 21, 1470–1474). There, manual capture follows shipment and triggers invoice; partial capture needs amount/item data, unclaimed balance cancellation, and Support setup for multiple captures. Uncaptured payments may be cancelled and captured payments refunded; partial refund needs capture reference where multiple captures exist and invoice item data for Open Invoice (raw lines 1476–1540). The partial-capture JSON example has a trailing comma (line 1520), so do not claim it is ready to execute. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-ratepay-api-only.md` → pinned raw.
