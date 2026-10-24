---
title: "Adyen PayPal Redirect Component for iOS"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypal/ios-component"
raw_files:
  - "adyen/docs/payment-methods/paypal/ios-component/2026-09-15.md"
tags: [adyen, paypal, ios, components, online-payments, recurring-payments]
---

## Overview

This [[adyen]] guide, last modified and captured 2026-09-15, adds the **PayPal Redirect Component** to an existing iOS Components integration after the separate PayPal setup steps. It covers Sessions (the default for Components v5.0.0+) and an additional-use-case `/payments` route, version-specific iOS component setup, payment-outcome webhooks, recurring tokens and capture-dependent refunds. See [[adyen-online-payments]]. Its examples are TEST requests, not proof of live PayPal enablement, authorization, capture, settlement or shopper funds receipt. See raw lines 15–34 and 510–522.

## Key takeaways

- The `/sessions` and `/payments` reference tables describe optional `lineItems`, **customer-initiated Fraudnet-only** `additionalData.paypalPairingId` when the same pairing ID is passed to Fraudnet and Adyen, and `additionalData.paypalRisk` **only for marketplaces or specified verticals** when PayPal requires those fields. The applicable risk keys must come from the PayPal account manager; if sent, use a stringified `additional_data` array. These conditions do not make the illustrated risk payload universal. For HUF transactions, the page recommends rounding both transaction and line-item amounts to whole HUF units and checking their sum; it warns PayPal may reject a discrepancy. See raw lines 36–44, 514–522 and 1035–1113.
- For iOS Components v5.0.0+, the guide shows `InstantPaymentComponent` after checking that the PayPal method is returned, with the **session** as delegate for Sessions and the host as delegate for Advanced. It shows an older `PayPalComponent` path for v4.x.x. The `/payments` example uses `paymentMethod.type: paypal` with `subtype: sdk`; these are version/flow-specific examples, not evidence that a merchant can show or process PayPal. See raw lines 524–565 and 1115–1170.
- The synchronous `resultCode` is for displaying a **current** shopper status. Even `Authorised` can later fail from post-authorization risk rules; `Pending`/`Received` are unresolved, and `Error`, `Refused` and `Cancelled` have different shopper actions. The page instructs waiting for the **AUTHORISATION** webhook for the final outcome; `OFFER_CLOSED` is optional and reports an incomplete/expired offer only if enabled. Optional PayPal detail fields require webhook settings. These authorization events do not by themselves show capture or settlement. See raw lines 1172–1209.
- PayPal recurring use requires PayPal Support to enable **Reference Transactions**, permissions on the PayPal account, and recurring token lifecycle webhooks. For initial token creation the guide specifies `Subscription` or `UnscheduledCardOnFile`, `shopperInteraction: Ecommerce`, shopper reference, and `storePaymentMethod: true`; `shopperEmail` is required **only** for its zero-value authorization case and excluded for nonzero requests. It says `recurring.token.created` arrives when the payment **has settled**, carrying `storedPaymentMethodId`; later token requests use that ID with the same shopper reference and `ContAuth`. The instructions do not prove permission grant, token creation, settlement or successful later charges. See raw lines 1211–1268 and [[adyen-tokenization]].
- Before capture, the guide directs cancellation; after capture, refund. For an **immediate-capture partial refund**, its introductory prose says include `lineItems`, but the adjacent parameter table leaves `lineItems` unmarked as required and says Adyen adds a dummy item if totals differ. For **later capture**, the guide requires `capturePspReference` when later capture, multiple-partial-capture enablement and intent for more than one partial capture all apply; without the capture reference PayPal can fail to locate the transaction. The refund response example has `status: received` and a **refund** PSP reference, not completed shopper credit. Its partial-refund example uses EUR 1200 and a Polo shirt despite the earlier USD 1000 shoe/sock order, so it must not be treated as a continuation of that order. See raw lines 1270–1390 and [[adyen-refunds]].
- PayPal Seller Protection advice is scoped to **physical goods** and requests delivery address, shopper name and line items for participating merchants; checking a test payment's eligibility is a recommendation, not a guarantee. Sandbox testing uses business/personal test accounts. Live operations require separate PayPal business-account setup; the page says live PayPal is available only when the shopper is logged in and has a valid PayPal payment method. See raw lines 1392–1427.

## Detail locators

- **Prerequisites, Sessions fields, TEST `/sessions` examples:** raw lines 21–509. The Go example says library v10.4.0 while importing `/v9/` paths (lines 312–318); Python/Ruby `paypalRisk` snippets do not match the stated stringified JSON shape (lines 405–407, 450–452).
- **Advanced `/payments` request/examples:** raw lines 510–1033. The PHP sample swaps the risk-array/shopper-reference placeholders (lines 678–684); do not copy it as a request contract.
- **HUF rounding and conditional risk-field data/format:** raw lines 1035–1113.
- **v5 versus v4 iOS component patterns, response/webhooks:** raw lines 1115–1209.
- **Recurring setup, token timing and parameters:** raw lines 1211–1268.
- **Capture-dependent cancellation/refund, example conflicts and Seller Protection:** raw lines 1270–1404.
- **Sandbox versus live prerequisites:** raw lines 1406–1427.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen-refunds]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypal/ios-component/2026-09-15|PayPal iOS Redirect Component guide — captured 2026-09-15]]
