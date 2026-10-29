---
title: "Adyen PayBright Web Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paybright/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paybright/web-drop-in/2026-09-15.md"
tags: [adyen, paybright, web-drop-in, buy-now-pay-later, canada]
---

## Overview

This [[adyen]] guide describes PayBright additions to an existing Web Drop-in integration using Sessions or Advanced flow. It explicitly states that Adyen will **not accept new PayBright integrations**, following PayBright's acquisition by Affirm (raw line 19). Its subsequent setup and live-request instructions are retained as historical guidance for the described integration, not evidence that a new merchant can now enable PayBright. The related [[source-adyen-docs-payment-methods-paybright]] overview identifies the CA/CAD redirect product; [[adyen-online-payments]] provides general checkout context.

## Key takeaways

- **Eligibility and base flow:** The page asks for an existing Sessions or Advanced Drop-in integration and PayBright added in Customer Area (raw lines 28–44), while its opening says new integrations are not accepted (raw line 19). It says the merchant supplies shopper details for PayBright risk checks and product information through `lineItems` (raw lines 23–26). The later test/live section still describes a live Customer Area request (raw lines 1428–1434); that procedural text does not cancel the new-integration restriction.
- **Request data and internal wording tension:** The `/sessions` route is described as the default for Drop-in v5.0.0 or later, with `/payments` shown for an additional use case (raw lines 50–52, 794–809). Both request tables mark shopper name, birth date, email, phone, country, billing address and shopper reference as required; delivery address and locale are optional. They mark `lineItems` optional but recommended for approval rates, despite the opening instruction to provide them (raw lines 23–26, 54–65, 798–809). Delivery address falls back to billing address if omitted. The examples use `CA`, `CAD`, `paybright` and a discount line (raw lines 67–132, 811–879). Some Advanced Java/PHP examples instead use `USD` with `CA`, conflicting with the CA/CAD overview and the other examples (raw lines 880–967). Use the raw table and product scope, not those examples alone, for field and currency decisions.
- **Drop-in and capture:** The guide says no PayBright-specific Drop-in configuration is needed (raw lines 1317–1319). It says automatic capture follows authorization by default; delayed or manual capture is needed if capture should follow shipment or a partial capture is wanted. It says the shopper is charged the first installment on capture (raw lines 1321–1327). Partial captures are unavailable with automatic capture enabled in Customer Area (raw lines 1329–1333). A single partial capture automatically cancels the unclaimed amount; an account enabled for multiple partial captures retains the remainder, requires Support setup and creates a new invoice per capture (raw lines 1378–1380).
- **Modification boundary:** For the shown partial `/capture` path, specify `modificationAmount` and optionally invoice-line data; the guide maps `openinvoicedata.itemAmount` to `lineItems.amountExcludingTax` and `itemVatAmount` to `taxAmount` (raw lines 1333–1347). Uncaptured payments can be cancelled; captured payments require refund to return funds (raw lines 1382–1384). For partial refund, the prose links Checkout `/payments/{paymentPspReference}/refunds`, while its example is labelled `/refund` and uses legacy `originalReference`/`modificationAmount`/`openinvoicedata` fields (raw lines 1386–1426). Keep endpoint and field mappings separate; the examples do not demonstrate a completed capture or refund.
- **Test boundary:** The source points to PayBright test details and test Customer Area status lookup (raw lines 1428–1432). It does not demonstrate live merchant enablement, shopper approval or payment execution. Example SDK/API snippets are mixed vintages and TEST-oriented; consult the specific integration version before use.

## Detail locators

- New-integration restriction and method-specific purpose: pinned raw lines 15–26.
- Sessions/Advanced prerequisites and request tables: pinned raw lines 28–65, 794–809.
- Sessions `/sessions` examples: pinned raw lines 67–793.
- Advanced `/payments` examples and currency discrepancy: pinned raw lines 811–1315.
- Drop-in, capture and partial-capture rules: pinned raw lines 1317–1380.
- Refund/partial-refund prose and example: pinned raw lines 1382–1426.
- Test/live instructions: pinned raw lines 1428–1434.

## Related

- [[adyen-online-payments]] — provider online checkout context.
- [[source-adyen-docs-payment-methods-paybright]] — CA/CAD product overview and new-integration restriction.
- [[source-adyen-docs-payment-methods-affirm]] — separate Affirm method; PayBright acquisition does not make its integration rules interchangeable.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paybright/web-drop-in/2026-09-15|PayBright Web Drop-in guide, captured 2026-09-15]]
