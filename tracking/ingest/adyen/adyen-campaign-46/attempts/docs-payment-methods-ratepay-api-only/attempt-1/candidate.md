---
title: "Adyen Ratepay API-only integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ratepay/api-only"
raw_files:
  - "adyen/docs/payment-methods/ratepay/api-only/2026-09-15.md"
tags: [adyen, ratepay, api-only, open-invoice, direct-debit]
---

## Overview

Adyen's Ratepay API-only guide describes adding Ratepay to an existing API-only integration, where the merchant builds the payment form and calls the APIs from its server. It covers Open Invoice and Direct Debit requests, risk fingerprinting, result presentation, and payment modifications. This captured guide is not evidence of current account enablement, a valid complete implementation, or live payment success. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- Build an API-only integration and add the method in the **test** Customer Area. If using `/paymentMethods` to show available methods, the guide lists AT/EUR, DE/EUR, NL/EUR, and CH/CHF. Its types are `ratepay` (Open Invoice) and `ratepay_directdebit` (Direct Debit); Direct Debit is unavailable in Switzerland. The API-only page does not state the Web Drop-in page's version qualifiers.
- Collect shopper first/last name, date of birth, telephone, email, billing address and a delivery address if different from billing. Implement Ratepay device fingerprinting for risk evaluation. The server `/payments` tables require those details, `deviceFingerprint` and `lineItems` for both types; Direct Debit additionally requires bank country code, IBAN and owner name.
- **Source example conflict:** the Direct Debit parameter table says `paymentMethod.type=ratepay_directdebit`, but the Direct Debit curl and repeated SDK examples show `ratepay`. The examples do not establish a corrected Direct Debit payload or successful execution.
- The response section describes `additionalData.openinvoicedata.descriptor` as invoice payment purpose for bank-transfer matching, plus `resultCode`, `pspReference` and `merchantReference`. The guide lists Authorised, Cancelled and Refused outcomes. Authorised means the payment is authorized; it does not establish capture.
- **Capture scope tension:** the introduction says a Ratepay payment needs capture after goods are sent to trigger an invoice, while the detailed capture section explicitly says it applies **only to Ratepay Open Invoice**. That section requires manual capture after shipment, even if other methods use automatic capture. For Open Invoice partial capture, send `modificationAmount` and `additionalData.openinvoicedata` item data; cancel any unclaimed balance manually. Multiple partial captures require Support setup and create a separate invoice per capture.
- Uncaptured Ratepay payments can be cancelled; captured ones need refund to return funds. Partial refund specifies `modificationAmount`, capture `acquirerReference` when multiple partial captures exist, and `additionalData.openinvoicedata` item information only for Open Invoice. Live acceptance requires a request in the live Customer Area and Ratepay live credentials.

## Detail locators

- Raw `# Ratepay for API only`, lines 15–32: identity, setup, introduction's capture language, and fingerprint preparation.
- Raw `## Build your payment form for Ratepay` and `## Collect shopper details`, lines 34–65: country/currency, method types, Switzerland exclusion and shopper details.
- Raw `## Calculate the device fingerprint` and `## Make a payment`, lines 67–88 and 745–785: server request, required fields, Direct Debit bank data, and method-type example conflict. Many following SDK snippets are illustrative, not verified recipes.
- Raw lines 1438–1474: response, results, and Open Invoice capture scope. Raw `### Partial captures` and `## Refunds and cancellations`, lines 1476–1573: partial modifications and Support gate. The JSON partial-capture example has a trailing comma at line 1520.
- Raw `## Test and go live`, lines 1576–1582: live setup and test status.

## Related

- [[adyen-online-payments]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/ratepay/api-only/2026-09-15|Ratepay API-only guide, captured 2026-09-15]]
