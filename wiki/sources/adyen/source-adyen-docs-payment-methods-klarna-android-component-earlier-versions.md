---
title: "Adyen Klarna Redirect Component v4.x.x for Android"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/klarna/android-component/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/klarna/android-component/earlier-versions/2026-09-15.md"
tags: [adyen, klarna, android, components, redirect, v4]
---

## Overview

This captured Adyen guide describes adding Klarna to an existing **Android Components v4.x.x Advanced flow** using the Redirect Component. The merchant shows an eligible Klarna method, submits shopper and item details from its server, hands the returned redirect action to the Android app, sends returned details from the server, and captures an authorized payment after goods are sent. The page metadata says last modified 2019-09-06, while its examples include later Checkout API and library versions; this snapshot does not establish one historical runtime version or current merchant eligibility. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The guide requires an existing Advanced flow Android Components integration and Klarna added in Customer Area. `/paymentMethods` discovery is scoped by listed country/currency combinations for Pay Now (`klarna_paynow`), buy now pay later (`klarna`), and Pay Over Time (`klarna_account`). Its country/product table is a captured availability matrix, not proof of enablement for any merchant.
- The server `/payments` request uses the chosen Klarna type, shopper data, matching country/billing country/currency and compatible locale, plus `lineItems` whose total matches `amount.value` and whose items have descriptions. The table marks `shopperEmail` and `countryCode` required; shopper name/billing address are recommended for experience, and recipient name in delivery address is conditional. Some products/business models may need encoded merchant data, but test values there cause an error in TEST.
- A `RedirectShopper` result returns an `action` for the client. After the shopper returns, the server posts `actionComponentData.details` to `/payments/details`; its result can be `Authorised`, `Cancelled`, or `Refused`. `Authorised` is the payment authorization/result shown to the shopper, with capture still required under the stated rules. Refusal is attributed to Klarna risk checks; the guide advises offering another method.
- Automatic capture can be configured in live Customer Area only when capture delay is immediate and the merchant complies with Klarna's shipping-within-24-hours scheme rule. Otherwise manually capture within 90 days of authorization even if merchant-account automatic capture is enabled; the authorization expires if missed. The main manual route uses Checkout `/payments/{paymentPspReference}/captures` with invoice `lineItems`. Its `status: received` response has a new capture PSP reference; the CAPTURE webhook reports final success or failure and supplies a reason for retry after repair.
- The later shipping/tracking and partial-capture examples instead use legacy `/capture`, `modificationAmount`, and `additionalData.openinvoicedata`. Keep those request shapes distinct from Checkout `/captures`. A partial amount must be less than authorized and its invoice amounts correct; multiple items cannot have different delivery addresses in one order.
- Recurring Klarna token creation adds `storePaymentMethod: true` and `shopperReference` to /payments. After settlement, the `recurring.token.created` webhook provides the stored ID. Later token payments include that ID, matching shopper reference, `ContAuth`, a recurring model and ordinary Klarna parameters. The sample is specifically Klarna Pay Now with an actively purchasing shopper.

## Detail locators

- v4.x.x identity, Advanced prerequisite, country/currency/product matrix: raw lines 15–79. The locale matrix is raw lines 83–118.
- /payments fields, TEST example (Checkout API v72), redirect action: raw lines 120–142 and 866–882; library examples occupy lines 146–864.
- Return and result handling: raw lines 884–929. The redirect step links to a Sessions-flow anchor although the page requires Advanced flow; follow the actual base integration's return handling.
- Capture conditions, Checkout capture fields and async outcome: raw lines 931–947 and 1393–1426. The capture examples use later library versions than the payment examples.
- Legacy shipping/partial-capture examples: raw lines 1428–1506. Recurring: lines 1508–1620. Testing/live caveats: lines 1622–1649.
- The source's “See also” Android Components link also points to Sessions despite the Advanced requirement (raw line 1653).

## Related

- [[adyen-online-payments]] — provider integration architecture.
- [[adyen-payment-capture]] — general capture lifecycle; this source holds Klarna-specific conditions.
- [[adyen-tokenization]] — general token lifecycle; this source holds the Klarna example.

## Raw Sources

- [[raw/adyen/docs/payment-methods/klarna/android-component/earlier-versions/2026-09-15|Klarna Redirect Component v4.x.x, captured 2026-09-15]]
