---
title: "Adyen Riverty API-only integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/riverty/api-only"
raw_files:
  - "adyen/docs/payment-methods/riverty/api-only/2026-09-15.md"
tags: [adyen, riverty, api-only, redirect, capture, refunds, online-payments]
---

## Overview

This captured [[adyen]] guide adds Riverty to an existing Advanced-flow API-only integration. It covers merchant-built form data, method discovery, redirect and details handling, manual capture after shipment, partial-capture balance handling, refunds, risk data and go-live checkout consent. It is a method-specific route under [[adyen-online-payments]], not evidence of a merchant's current enablement or a completed payment.

## Key takeaways

- **Setup, pricing and form:** The page requires an existing API-only integration with redirect handling and Riverty added in Customer Area. Activation defaults to standard pricing; it advises contacting an account manager before activation to check Enterprise-pricing eligibility. The form collects identity, contact, birth-date and billing/delivery data; IBAN is optional in the generic form list but required for the Secure Direct Debit type (raw lines 23–78, 123–141).
- **Discovery and product identity:** For `/paymentMethods`, the guide lists country codes AT, BE, DE, NL and CH and currencies EUR or CHF; the NL/EUR example response has `type: riverty`. The `/payments` table distinguishes `riverty` Pay in 14, `riverty_account` Monthly Consolidated Invoice, `sepadirectdebit_riverty` Secure Direct Debit, and `riverty_installments` fixed 3/6/12/24-month installments, with required subtype `redirect`. The table's values are method-discovery inputs, not a promise that every product is available in every country/currency or to every shopper (raw lines 80–141).
- **Payment data and risk:** The `/payments` table marks billing address, shopper first/last name, email, line items and type/subtype required. Phone, birth date, shopper IP and `deviceFingerprint` are unmarked; IBAN is conditionally required for Secure Direct Debit. B2B is stated unsupported. Only send a delivery address if address or recipient differs; when sent, delivery first and last name are required even if matching the shopper, and a first-time shopper may face risk rejection if delivery differs from billing. If that differing delivery address causes a risk rejection, the guide says to send only the billing address and deliver the package there. Each line item requires quantity, description and ID; DACH VAT must not be null for the described reclaim process. Profile tracking is recommended for AT, DE and CH, requires a `profileTrackingShopId` from Riverty support, and sends an encrypted ID; its prose says `deviceFingerprint` and the table says `paymentMethod.deviceFingerprint`, while the sample places it top-level. That placement conflict needs version-specific verification before implementation (raw lines 47–61, 123–141, 145–160).
- **Redirect and capture:** After `/payments`, the response example has `RedirectShopper` and a redirect action for Riverty-hosted profile tracking or additional risk checks; then the base flow handles redirect and additional details to obtain status. All Riverty payments must be **manually captured after goods are sent**, even where other methods auto-capture. Capture triggers an invoice and the payment schedule, but the page conflicts on who sends that invoice: its process summary says the merchant sends it (raw line 45), while the line-item table says Riverty sends it (raw line 137). The capture statement at line 243 does not resolve the sender. Without capture within 30 days, the authorization expires unless Support arranges a longer period (raw lines 220–245).
- **Partial captures, cancellation and refunds:** A partial capture supplies amount and matching item lines; if the item sum differs, Adyen adds a dummy line item. Unclaimed authorization after partial capture should be manually cancelled; the page says an empty cancel request after a partial capture releases the remainder. Multiple partial captures require Support setup and generate separate invoices. Uncaptured payments can be cancelled; captured payments are refunded. Partial refund amount and item lines should match or a dummy line is added. `capturePspReference` identifies which capture to refund; omitting it selects the last capture, possibly the wrong one (raw lines 247–258, 321–330, 553–565).
- **Go-live and example caveats:** Riverty requires Terms & Conditions and data-protection guidelines for shopper approval before payment. The capture curl example has a malformed `https: //` URL; the shown discovery, payment, capture, cancel and refund curl snippets also place `-X POST` on a line without continuation before `-d`, so do not copy them verbatim. The example response `status: received` is request receipt, not a proven settled outcome (raw lines 89–106, 143–150, 264–272, 333–345, 571–579, 997–1003).

## Detail locators

- Requirements, profile tracking and form fields: pinned raw lines 15–78.
- Method discovery, payment fields and redirect: pinned raw lines 80–239.
- Capture, partial capture, remainder cancellation and examples: pinned raw lines 241–552.
- Refund/cancellation distinctions, examples and go-live: pinned raw lines 553–1007.

## Related

- [[adyen-online-payments]] — online payment architecture and method routes.
- [[source-adyen-docs-payment-methods-riverty]] — captured Riverty product overview; use this page for API-only lifecycle details.

## Raw Sources

- [[raw/adyen/docs/payment-methods/riverty/api-only/2026-09-15|Riverty API-only guide, captured 2026-09-15]]
