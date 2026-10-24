---
title: "Adyen PayPal API-only integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypal/api-only"
raw_files:
  - "adyen/docs/payment-methods/paypal/api-only/2026-09-15.md"
tags: [adyen, paypal, api-only, redirect, recurring]
---

## Overview

This [[adyen]] guide adds PayPal-specific steps to an **existing Advanced-flow API-only Web integration**. It assumes redirect handling, PayPal added in Customer Area, and completion of separate PayPal setup. It covers method discovery, a server `/payments` request and redirect, conditional risk fields, outcome webhooks, refunds, token-based recurring payments, and test/live gates. The page is not a complete general Advanced-flow guide and its TEST examples do not prove merchant enablement or payment success. [[adyen-online-payments]]

## Key takeaways

- The existing integration must handle `action.type: redirect`. The custom payment form lists PayPal and needs no other shopper input fields **for this method-specific form**. `/paymentMethods` uses a supported `countryCode` and `amount.currency` from the page's tables and returns a `paypal` type in its TEST example. Listed countries/currencies and a sample response are discovery guidance, not a promise that a particular merchant or shopper can use PayPal. See raw lines 23–84.
- The `/payments` section lists `lineItems` for item information with quantity, description, itemCategory, sku, amountExcludingTax and taxAmount; its Required column is blank. `additionalData.paypalPairingId` is only for customer-initiated Fraudnet transactions using the same pairing ID in Fraudnet and Adyen. `additionalData.paypalRisk` is only for marketplaces or specified verticals, with fields confirmed by the PayPal account manager and encoded as a stringified `additional_data` array. The v71 TEST request example uses `paymentMethod.type: paypal`, `subtype: sdk`, a `returnUrl`, line items and risk data; the `sdk` subtype and unconditional-looking sample risk object are not explained as universal API-only requirements. See raw lines 86–142 and 637–709.
- The payment response example has `resultCode: RedirectShopper` and a redirect action. Redirect initiation or shopper return is not final payment proof. The page says the synchronous `resultCode` is only current status and to use webhooks for final outcome, particularly with risk rules applied after authorization. AUTHORISATION success/false and optionally enabled OFFER_CLOSED events have distinct order actions; even a synchronous `Authorised` can later fail. See raw lines 621–635 and 731–768.
- A PayPal payment can be **cancelled before capture**; after capture, returning funds requires a **refund**. Recurring requires PayPal Support enabling **Reference Transactions**, PayPal account permissions to charge an existing customer and manage recurring payments, plus token-lifecycle webhook setup. An initial `/sessions` or `/payments` request uses `storePaymentMethod: true`, `shopperInteraction: Ecommerce`, shopper reference and a Subscription or UnscheduledCardOnFile model; `shopperEmail` is required for a zero-value authorization and should be omitted otherwise. The page says `recurring.token.created` arrives **when the payment has been settled**, carrying `storedPaymentMethodId`; later requests use that ID, matching shopper reference, `ContAuth`, and the recurring model. The guide does not describe a separate shopper-consent or billing-agreement UX; token setup is not proof of later payment success. See raw lines 770–831. [[adyen-tokenization]]
- Seller Protection applies here to **physical goods** and, if participating, calls for deliveryAddress, shopperName and lineItems; the page recommends checking a test payment's eligibility rather than assuming it. For live use it separately requires a live PayPal business account/environment and says PayPal appears only when the shopper is logged in and has a valid payment method. See raw lines 717–729 and 833–852.
- There are source/example inconsistencies. The `/paymentMethods` currency list omits **HUF**, but a later HUF section gives whole-amount rounding advice and warns PayPal may reject discrepant transaction/line-item totals. Several library snippets have malformed risk-data strings or missing/odd imports, including the PHP, NodeJS and TypeScript examples; they are not copy-ready. The page's sample `paypalRisk` data also appears despite its conditional prose. See raw lines 50–53, 255–269, 343–394, 560–619, and 711–715.

## Detail locators

- Country/currency discovery table and TEST v71 `/paymentMethods` example: raw lines 46–84.
- `/payments` parameter table and language-specific TEST examples: raw lines 86–619. The language snippets name distinct library versions; their common shape does not establish version compatibility.
- Conditional marketplace risk-field examples and exact stringified format: raw lines 637–709.
- Result-code and webhook action tables, optional PayPal-details setting: raw lines 731–768.
- Refund/capture boundary and recurring token lifecycle: raw lines 770–831.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypal/api-only/2026-09-15|Adyen PayPal API-only snapshot]]
