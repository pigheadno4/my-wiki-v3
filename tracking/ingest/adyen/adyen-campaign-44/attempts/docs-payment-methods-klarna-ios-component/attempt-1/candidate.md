---
title: "Adyen Klarna iOS Redirect Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/klarna/ios-component"
raw_files:
  - "adyen/docs/payment-methods/klarna/ios-component/2026-09-15.md"
tags: [adyen, klarna, ios, components, redirect, capture, tokenization]
---

## Overview

This 2026-09-15 Adyen Docs guide adds Klarna to an existing iOS Components integration through Sessions or Advanced flow. It covers payment request data, Redirect Component configuration, capture, recurring tokens and test/live checks. It is integration guidance, not evidence of merchant enablement, shopper approval, capture or settlement. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- First build the matching Sessions or Advanced iOS Components integration and add Klarna in Customer Area. `/sessions` is described as the default with Components v5.0.0+; `/payments` is shown for an additional use case. In both request tables, `lineItems` must total `amount.value` and each line must have a `description`; `countryCode` must match the billing-address country. `shopperEmail` is marked required with an explicit dispute-defense note. Optional shopper name/address can be collected on Klarna's page, and some products or business models can require Base64-encoded merchant attachment data. The page warns not to send that merchant data in TEST because test values cause an error.
- For iOS Components v5.0.0+, use `InstantPaymentComponent` for `.other("klarna")`, retain it, assign the session as delegate for Sessions or self for Advanced, and initiate payment. The v4.x.x example uses `KlarnaComponent` and `KlarnaPaymentMethod`. No other Klarna-specific Component configuration is stated. These are versioned snippets, not proof that the sample request is valid for all markets.
- Automatic capture can be configured when adding Klarna in live Customer Area only if capture delay is immediate and shipping complies with Klarna's 24-hour scheme rule. Otherwise manual capture is required within 90 days of authorization, even when merchant-account automatic capture is enabled; the authorization expires without it. Manual `/payments/{paymentPspReference}/captures` requires merchant account, amount and invoice `lineItems`. Its `status: received` response acknowledges the request; the later `CAPTURE` webhook reports success or failure. On failure, the guide says to review the reason, correct the issue and resubmit.
- The separate partial-capture paragraph uses legacy `/capture` with `modificationAmount` below the authorized amount and correct `additionalData.openinvoicedata` for items charged. Its endpoint/field family differs from the preceding Checkout `/captures` manual-capture procedure; use each section's own route and linked API reference rather than combining the examples. Optional shipping/tracking invoice data cannot express different delivery addresses for one multi-item order.
- The recurring section creates a token with `storePaymentMethod: true` and `shopperReference` in `/payments`; the `recurring.token.created` webhook follows settlement and yields `storedPaymentMethodId`. Future `/payments` calls use that ID, the same shopper reference, `shopperInteraction: ContAuth`, a recurring processing model and ordinary Klarna request parameters. Its concrete sample is **Klarna Pay Now** (`klarna_paynow`), not a universal template for every Klarna product.
- Before live use, the guide calls for test-environment checks, adding Klarna to live Customer Area, accurate invoice lines/VAT, a fallback when Klarna rejects a shopper, and legal/privacy/brand review. Its live-test advice warns that unrealistic shopper data, unsuitable amount or repeated same-device/IP attempts can cause `Refused`; test bypasses those live checks. This snapshot does not prove live eligibility or results.

> [!warning] Example conflict
> The request tables say `shopperLocale` must match `countryCode` and currency, while the Sweden/SEK examples use `en_US`. Treat that locale as illustrative and verify a supported market combination; the page does not reconcile the mismatch.

## Detail locators

- Sessions/Advanced prerequisites and `/sessions` versus `/payments` tables, including email dispute note and TEST merchant-data warning: pinned raw lines 21–60 and 757–774. Request samples and language-specific API-library versions: lines 62–1494.
- Component v5.0.0+ and v4.x.x snippets: lines 1498–1553.
- Automatic/manual capture condition, 90-day expiry, `/captures` request/response and webhook: lines 1555–1571 and 2017–2048. Shipping/tracking and partial `/capture` route: lines 2052–2130.
- Recurring token creation/use and Pay Now sample: lines 2132–2244. Test/live guidance and refusal boundaries: lines 2246–2273.

## Related

- [[adyen-online-payments]] — main provider payment integration concept

## Raw Sources

- [[raw/adyen/docs/payment-methods/klarna/ios-component/2026-09-15|Klarna iOS Component guide, captured 2026-09-15]]
