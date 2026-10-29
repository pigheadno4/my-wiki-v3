---
title: "Adyen Ratepay Web Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ratepay/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/ratepay/web-drop-in/2026-09-15.md"
tags: [adyen, ratepay, web, drop-in, open-invoice, direct-debit]
---

## Overview

Adyen's Ratepay Web Drop-in guide adds Ratepay to an existing Web Drop-in integration. Drop-in renders the method and collects shopper information; the merchant's server sends the payment request. This 2026-09-15-captured guide covers Open Invoice and Direct Debit, their setup and payment fields, result presentation, and later capture, cancellation, and refund steps. It is documentation evidence, not proof that a merchant account is enabled or a payment succeeded. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The prerequisites are an existing Web Drop-in integration and adding Ratepay in the **test** Customer Area. Web Drop-in v6 imports `AdyenCheckout` and `RatePay`. In `/paymentMethods`, the documented country/currency combinations are AT/EUR, DE/EUR, NL/EUR (v3.22.1 or later), and CH/CHF. The method types are `ratepay` for Open Invoice and `ratepay_directdebit` for Direct Debit (v5.13.0 or later). Direct Debit is unavailable for shoppers in Switzerland.
- The merchant must collect shopper details and `lineItems`, calculate Ratepay's device fingerprint for risk evaluation, and pass it with the payment request. Drop-in's `onSubmit` provides `state.data` to pass to the server, which calls `/payments`. Both method tables require shopper name, telephone, email, date of birth, billing address, fingerprint and line items; delivery address is required when it differs from billing. Direct Debit additionally requires bank country code, IBAN, and account owner name.
- **Source example conflict:** the Direct Debit parameter table specifies `paymentMethod.type=ratepay_directdebit`, but its curl example and repeated SDK examples use `ratepay`. Treat those examples as inconsistent with the table; this snapshot does not verify a corrected request.
- `/payments` returns `resultCode`, `pspReference`, and `merchantReference`; Open Invoice additionally can return `additionalData.openinvoicedata.descriptor`, which the merchant should print on the invoice for bank transfer matching. The guide lists Authorised, Cancelled, and Refused result handling; Authorised is authorization, with capture still due after shipment.
- **Open Invoice only:** manual capture after goods are sent is required even when automatic capture is enabled for other methods; capture triggers the invoice. A partial capture specifies `modificationAmount` and item data in `additionalData.openinvoicedata`; cancel any unclaimed balance manually. Multiple partial captures require Support setup and create an invoice per capture. An uncaptured Ratepay payment can be cancelled; a captured one needs refund. Partial refund uses `modificationAmount`, `acquirerReference` if multiple captures exist, and Open Invoice item data. Live acceptance requires a request in the live Customer Area and Ratepay live credentials.

## Detail locators

- Raw `# Ratepay Drop-in integration`, lines 15–33: purpose, shopper/item/fingerprint/capture sequence, prerequisites.
- Raw `## Show Ratepay in your payment form`, lines 43–61: country/currency and method/version table. `## Optional Drop-in configuration`, lines 63–277: names, icons, and method-specific prefill/display settings.
- Raw `## Calculate the device fingerprint` and `## Make a payment`, lines 279–304 and 961–1004: server transition, Open Invoice/Direct Debit required fields, CH exclusion, and Direct Debit type conflict.
- Raw lines 2311–2347: response fields, result codes, and Open Invoice manual capture. Raw `### Partial captures` and `## Refunds and cancellations`, lines 2349–2447: partial capture, multiple-capture support gate, cancellation/refund conditions and item data.
- Raw `## Test and go live`, lines 2449–2455: live setup and test-payment status route. Request bodies and SDK examples throughout the raw are examples, not verified executable recipes.

## Related

- [[adyen-online-payments]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/ratepay/web-drop-in/2026-09-15|Ratepay Web Drop-in guide, captured 2026-09-15]]
