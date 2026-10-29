---
title: "Adyen Klarna Web Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/klarna/web-component"
raw_files:
  - "adyen/docs/payment-methods/klarna/web-component/2026-09-15.md"
tags: [adyen, klarna, web-components, buy-now-pay-later]
---

## Overview

Adyen's Klarna Web Component guide adds Klarna to an existing Sessions or Advanced flow Web Components integration. The shopper can complete the payment in a Klarna widget in the merchant checkout or be redirected to Klarna. This is a 2026-09-15 documentation snapshot, not evidence of merchant enablement or a completed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Add Klarna in Customer Area for either flow. The page says /sessions is the default with Components v5.0.0 or later; /payments covers an additional use case. Choose the configured component type: `klarna_paynow` (Pay Now), `klarna` (buy now, pay later), or `klarna_account` (Pay Over Time), subject to the method's supported countries and regions.
- For the documented /sessions and /payments requests, line-item totals must equal `amount.value`, each item needs `description`, and `countryCode` must agree with the billing-address country. The page marks `shopperEmail` required and says to include it to defend against disputes; shopper name and billing address are recommended, while recipient name has a conditional delivery-address rule. Locale must match country and currency. Some products or business models may require Base64 encoded merchant data, but the page warns against test values in the test environment.
- `useKlarnaWidget: true` shows the widget; omission or false initiates redirect. Web v6 imports `Klarna` and uses `new Klarna(checkout).mount(...)`; v5 and earlier show `checkout.create(...).mount(...)`. The optional-configuration prose says “Drop-in” although this page targets Components, and its v6 mount snippet does not pass the shown widget configuration; verify the version-specific configuration path before relying on that snippet.
- Automatic capture can be configured in live Customer Area only when capture delay is immediate and the merchant complies with Klarna's shipping-within-24-hours scheme rule. Otherwise manually capture within 90 days of authorization, even if merchant-account automatic capture is enabled; uncaptured authorization then expires. The main manual flow uses `/payments/{paymentPspReference}/captures` with invoice line items. A `status: received` capture response is an accepted request, with a distinct capture PSP reference; wait for the CAPTURE webhook to determine success, and review failure reason before retrying.
- The later shipping and partial-capture examples use the legacy `/capture` endpoint, `modificationAmount`, and `additionalData.openinvoicedata`, unlike the preceding Checkout `/captures` flow. Treat these as separately scoped examples rather than mixing their request shapes. Partial capture needs an amount below the authorized amount and correct invoice amounts. One delivery address applies to a multiple-item order.
- For recurring Klarna, the page describes `storePaymentMethod: true` and `shopperReference` in an initial /payments request, then a `recurring.token.created` webhook after settlement. The server must be able to receive the Recurring tokens life cycle events webhook; the page links to setup in Customer Area. Future /payments calls use that shopper reference, the stored payment method ID, `shopperInteraction: ContAuth`, a recurring processing model, and all ordinary Klarna request parameters. The shown future-payment example is specifically Klarna Pay Now with an actively shopping customer.

> [!warning] Locale example conflicts with the request tables
> Both the `/sessions` and `/payments` tables say `shopperLocale` must match `countryCode` and currency, but their SE/SEK examples use `en_US`. Reconcile the locale against the supported country/currency rules before using these examples; this page does not identify a replacement locale.

## Detail locators

- Requirements and /sessions versus /payments API field tables: raw lines 27–74 and 771–789. Locale prose is at lines 69 and 783; conflicting SE/SEK examples are at lines 85–90 and 803–807. Sample /sessions curl uses Checkout API v70; /payments curl uses v72, both in TEST. The library snippets list their own versions and are examples, not an SDK-wide version promise.
- Component types, widget option, and v6/v5 mounting: raw lines 1512–1569.
- Automatic and manual capture requirements, /captures payload and outcome: raw lines 1571–1587 and 2033–2065.
- Shipping/partial-capture legacy examples: raw lines 2068–2146.
- Recurring token sequence, server webhook setup prerequisite and future payment: raw lines 2154–2266 (especially 2175).
- Test and go-live conditions: raw lines 2268–2295. In the source, live testing needs real shopper data and reasonable amounts; repeated same-device/IP tests can trigger velocity checks. Test bypasses those live checks, so test approval does not establish live eligibility.

## Related

- [[adyen-online-payments]] — broader Adyen integration architecture.
- [[adyen-payment-capture]] — general capture lifecycle; this source carries Klarna-specific capture conditions.
- [[adyen-tokenization]] — general stored-payment context; this source carries Klarna's sequence.

## Raw Sources

- [[raw/adyen/docs/payment-methods/klarna/web-component/2026-09-15|Klarna Web Component, captured 2026-09-15]]
