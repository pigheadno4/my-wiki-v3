---
title: "Adyen Klarna Android Drop-in v4.x.x"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/klarna/android-drop-in/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/klarna/android-drop-in/earlier-versions/2026-09-15.md"
tags: [adyen, klarna, android, drop-in, v4]
---

## Overview

This 2026-09-15-captured guide adds Klarna to an existing **Android Drop-in v4.x.x Advanced flow**. Drop-in shows eligible Klarna methods and redirects the shopper to Klarna; the merchant server sends the payment request and returned action details, then captures an authorized payment under Klarna's shipping and timing rules. The page is an integration snapshot, not proof of current merchant enablement or a successful payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The requirements table calls for an existing Advanced-flow Android Drop-in integration and Klarna added in Customer Area. The introduction and “See also” link instead target a Sessions-flow guide; use the actual Advanced prerequisite for this v4.x.x page. Drop-in uses `countryCode` and `amount.currency` from `/paymentMethods` to display the three product categories: Pay Now, Pay Later, and Pay Over Time, subject to the captured country/currency matrix.
- When Drop-in returns `paymentComponentData.paymentMethod`, pass it to the merchant server for `/payments`. The request also needs `lineItems` totaling `amount.value`, each with a `description`; `shopperEmail` and `countryCode` are marked required. Country, currency, billing-address country and locale must be compatible. Shopper name and billing address are recommended; a different delivery recipient has conditional name fields. Some business models need encoded merchant data, but test values cause a TEST error.
- A `RedirectShopper` response supplies the action for Drop-in. After the shopper returns, the server posts `actionComponentData.details` to `/payments/details`, then presents `Authorised`, `Cancelled`, or `Refused`. The guide attributes refusal to Klarna risk checks and advises another method. `Authorised` here precedes the separate capture step.
- Automatic capture can be configured in the live Customer Area only if capture delay is immediate and the merchant complies with Klarna's shipping-within-24-hours scheme rule. Otherwise, manually capture within 90 days of authorization, even if merchant-account automatic capture is enabled; the authorization expires if not captured. The main manual route uses Checkout `/payments/{paymentPspReference}/captures` with invoice `lineItems`. A `status: received` response carries a capture PSP reference distinct from the payment reference; the CAPTURE webhook gives final success or failure and a reason for repair/retry.
- Later shipping/tracking and partial-capture examples use legacy `/capture`, `modificationAmount`, and `additionalData.openinvoicedata`. They have a different request shape than Checkout `/captures`. For the legacy partial example, the amount is below the authorized amount and invoice amounts must be correct; one order cannot specify different delivery addresses per item.
- The recurring route adds `storePaymentMethod: true` and `shopperReference` to /payments. Only after settlement does the page describe a `recurring.token.created` webhook with a stored method ID. Later /payments uses the ID, shopper reference, `ContAuth`, a recurring model, and the ordinary Klarna request parameters. The shown token example is Klarna Pay Now for an actively purchasing shopper.

## Detail locators

- v4.x.x scope, requirements and country/currency discovery matrix: raw lines 15–62. Payment data and locale matrix: lines 63–126.
- TEST `/payments` sample uses Checkout API v72; language-specific library examples show their own versions: raw lines 128–846. Redirect and result handling: lines 848–913.
- Capture conditions and Checkout request/response/webhook distinction: raw lines 915–931 and 1377–1410. Shipping/tracking and legacy partial-capture examples: lines 1412–1490.
- Recurring token sequence: raw lines 1492–1604. Testing and live requirements: lines 1606–1633.
- The “See also” Android Drop-in route links to Sessions despite the Advanced requirement (raw line 1637).

## Related

- [[adyen-online-payments]] — broader provider integration context.
- [[adyen-payment-capture]] — general capture lifecycle; this source holds Klarna-specific conditions.
- [[adyen-tokenization]] — general stored method lifecycle; this source holds the Klarna example.

## Raw Sources

- [[raw/adyen/docs/payment-methods/klarna/android-drop-in/earlier-versions/2026-09-15|Klarna Android Drop-in v4.x.x, captured 2026-09-15]]
