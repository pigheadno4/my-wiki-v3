---
title: "Adyen Riverty Web Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/riverty/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/riverty/web-drop-in/2026-09-15.md"
tags: [adyen, riverty, web, drop-in, buy-now-pay-later, redirect, capture]
---

## Overview

This [[adyen|Adyen]] guide, fetched and marked last modified 2026-09-15, adds Riverty to an existing **Web Drop-in** integration. It has separate Sessions and Advanced flow instructions; it is a method add-on, not a complete base integration. See [[adyen-online-payments]]. The captured guide does not prove current account eligibility or a successful payment.

## Key takeaways

- **Setup and flows:** Sessions requires an existing Web Drop-in Sessions integration, Checkout API v68 or later, and Riverty enabled in Customer Area. Advanced requires existing Web Drop-in Advanced integration, redirect action handling, and Customer Area enablement. The guide says activation defaults to standard pricing and to contact an account manager before activation to check Enterprise-pricing eligibility. Advanced `/paymentMethods` discovery specifies countryCode AT, BE, DE, NL or CH and currency EUR or CHF; this list alone does not establish every country/currency pairing or merchant availability.
- **Request and shopper scope:** Sessions `/sessions` requires shopper first/last name, telephone, email, billing and delivery addresses, and `lineItems`; each line item needs `quantity`, `description` and `id`. The Advanced `/payments` table marks billing address and line items required but delivery address and telephone optional; send delivery address only when it or the delivery person differs from billing, with delivery first/last names then required. The page says B2B is currently unsupported and a business name in shopperName may cause rejection. For DACH operations, VAT in line items must not be null for Riverty's uncollectible-debt VAT reclaim process. Advanced supports the listed Riverty payment types `riverty` (Pay in 14), `riverty_account` (Monthly Consolidated Invoice), `sepadirectdebit_riverty` (Secure Direct Debit, IBAN required), and `riverty_installments` (3, 6, 12 or 24 fixed installments), with `subtype: redirect`; these are request values, not an account-level promise.
- **Advanced redirect and risk:** The example Advanced response has `resultCode: RedirectShopper` and `action.type: redirect`. Profile tracking is recommended for Austria, Germany and Switzerland to improve acceptance, not described as universally mandatory. Riverty's implementation support must provide `profileTrackingShopId` before implementing it; the encrypted profile ID is sent as `deviceFingerprint` in `/payments`. The table names `paymentMethod.deviceFingerprint` while the prose and example use top-level `deviceFingerprint`; verify the correct field placement against the applicable API before implementation.
- **Capture lifecycle:** After goods are sent, **all Riverty payments require manual capture**, even if other methods use automatic capture. Capture triggers the shopper invoice and payment schedule. Authorization expires if not manually captured within 30 days unless Riverty extends the period after Support contact. For partial capture, send the captured `amount` and only captured `lineItems`; their sum must match or Adyen adds a dummy line item. Manually cancel any unclaimed remainder. Multiple partial captures require Support setup and each creates a new invoice. The example capture response's `status: received` is receipt of the modification request, not proof of final settlement.
- **Cancellation and refund:** Cancel an uncaptured payment; refund after capture. An empty cancellation request after a partial capture releases the remaining balance. Partial refunds specify amount and refunded line items; mismatched sums cause a dummy line item. Specify `capturePspReference` to identify the capture being partially refunded, because omitting it selects the last capture even when unintended. Example refund `status: received` does not establish completed refund.
- **Go live and sample caveats:** Riverty requires checkout Terms & Conditions and data protection guidelines for shopper approval before payment. The captured curl samples have missing shell continuations between `-X POST` and `-d`; the partial-capture sample also contains `https: //`. They are illustrative rather than copy-ready. Sessions requires a delivery address while Advanced describes it as conditional, so preserve the flow-specific field requirements. The Advanced prose says the merchant sends the invoice, while the capture section only says capture triggers an invoice to the shopper; this page does not consistently identify the invoice sender.

## Detail locators

- Sessions prerequisites and pricing: pinned raw lines 29–39; Sessions field table and DACH VAT note: lines 45–55; Sessions v71 test request: lines 60–126; optional import/no extra config: lines 129–145.
- Sessions capture, expiration, partial capture and modification examples: lines 149–233; cancel and refund instructions: lines 235–269; refund example response: lines 537–569; go-live requirement: lines 571–579.
- Advanced prerequisites and flow: lines 585–607; profile tracking: lines 609–623; available-method filters and v72 discovery example: lines 627–667; Advanced request fields and method types: lines 690–708; redirect response: lines 710–801.
- Advanced capture, cancellation, refunds and test/live: lines 803–923 and 1191–1233. Check the exact request table and relevant API reference before adapting an example to a deployed Checkout API version.

## Related

- [[adyen-online-payments]] — provider integration concept

## Raw Sources

- [[raw/adyen/docs/payment-methods/riverty/web-drop-in/2026-09-15|Riverty Web Drop-in guide, fetched 2026-09-15]]
