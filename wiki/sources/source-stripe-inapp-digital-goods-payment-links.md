---
title: "Accept iOS Digital Goods Payments with Payment Links"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/mobile/digital-goods/payment-links"
raw_files:
  - "stripe-mobile-digital-goods-payment-links-2026-11-07.md"
  - "stripe-inapp-digital-goods-payment-links-2025.md"
tags: [stripe, mobile, ios, digital-goods, payment-links, universal-links, apple-pay, webhooks, client-reference-id]
---

## Summary

The April and November 2026 captures describe an iOS digital-goods and subscription path that opens a **Stripe-hosted Payment Link page in Safari** and returns to the app through a universal link. A merchant with a limited product/price catalog can create the static link in the Dashboard without a server endpoint for link creation; the guide separately calls for a **production webhook endpoint** to handle fulfillment. Stripe-hosted Checkout and a merchant-owned Elements web checkout are named as alternatives for a dynamic cart or attaching a Customer to the Checkout Session. This guide does not describe a native in-app iOS payment form, user authentication, or a complete entitlement algorithm. The November capture changes Markdown and formatting, not demonstrated product behavior or platform policy. See [[stripe-inapp-payments]] and [[stripe-payment-links]]. [April capture](../../raw/stripe-inapp-digital-goods-payment-links-2025.md#L4-L36), [April fulfillment](../../raw/stripe-inapp-digital-goods-payment-links-2025.md#L142-L146); [November capture](../../raw/stripe-mobile-digital-goods-payment-links-2026-11-07.md#L5-L37), [November fulfillment](../../raw/stripe-mobile-digital-goods-payment-links-2026-11-07.md#L141-L145).

## Dated iOS and Apple Pay scope

Both captures say an iOS app selling digital products, content, or subscriptions in the **US or EEA can accept Apple Pay** using Payment Links and say the app cannot accept Apple Pay for these goods in other regions. This is a dated Stripe guide statement, not a live wallet-display, merchant-eligibility, or current App Store-policy guarantee. The page routes physical items, goods/services consumed outside the app, and real-time person-to-person services to the native iOS payment guide. It says Payment Links support cards and Apple Pay by default and additional methods can be enabled in Dashboard settings. [April scope](../../raw/stripe-inapp-digital-goods-payment-links-2025.md#L8-L20), [April methods](../../raw/stripe-inapp-digital-goods-payment-links-2025.md#L113); [November scope](../../raw/stripe-mobile-digital-goods-payment-links-2026-11-07.md#L9-L21), [November methods](../../raw/stripe-mobile-digital-goods-payment-links-2026-11-07.md#L112).

## Link creation and app return

Create a one-time-product or subscription Payment Link in the Dashboard, select **Don't show confirmation page**, and set a universal link as the success URL. The one-time example optionally lets customers choose what to pay. The app button opens the link's Stripe-hosted page in Safari. To return to the app, configure `/.well-known/apple-app-site-association` served as `application/json`, the Associated Domains entitlement, and a fallback page for redirect URLs. A return URL is navigation, not an independently verified payment or entitlement state. [April universal links](../../raw/stripe-inapp-digital-goods-payment-links-2025.md#L38-L90), [April Dashboard/app](../../raw/stripe-inapp-digital-goods-payment-links-2025.md#L92-L113), [April app button](../../raw/stripe-inapp-digital-goods-payment-links-2025.md#L135-L140); [November universal links](../../raw/stripe-mobile-digital-goods-payment-links-2026-11-07.md#L39-L89), [November Dashboard/app](../../raw/stripe-mobile-digital-goods-payment-links-2026-11-07.md#L91-L112), [November app button](../../raw/stripe-mobile-digital-goods-payment-links-2026-11-07.md#L134-L139).

| Guide path | Link/payment-page creation | Fulfillment |
| --- | --- | --- |
| Payment Links | Static Dashboard link; no application endpoint needed to create it | Production webhook endpoint or equivalent trusted receiver for fulfillment |
| Stripe-hosted Checkout | Separate dynamic-cart path named by this guide | Follow the linked guide |
| Elements | Separate custom web-checkout path named by this guide | Follow the linked guide |

The comparison is route guidance from this capture, not a full specification of the other two integrations. [April alternatives](../../raw/stripe-inapp-digital-goods-payment-links-2025.md#L14), [April webhook](../../raw/stripe-inapp-digital-goods-payment-links-2025.md#L142-L146); [November alternatives](../../raw/stripe-mobile-digital-goods-payment-links-2026-11-07.md#L15), [November webhook](../../raw/stripe-mobile-digital-goods-payment-links-2026-11-07.md#L141-L145).

## URL parameters and reconciliation

`prefilled_email` fills an **editable** field, so the final checkout email may differ. `locked_prefilled_email` fills an uneditable field and takes precedence if both are supplied. Valid email values should be URL encoded. `client_reference_id` is an alphanumeric/dash/underscore string of up to 200 characters that the guide says appears on the Checkout Session in `checkout.session.completed` for reconciliation. **Invalid values of all three parameters are disregarded while the payment page continues to work.** These URL-supplied values are context for reconciliation, not user authentication, proof of ownership, or a guarantee that a reference will be present. [April parameter table](../../raw/stripe-inapp-digital-goods-payment-links-2025.md#L115-L133); [November parameter table](../../raw/stripe-mobile-digital-goods-payment-links-2026-11-07.md#L114-L132).

```text
https://buy.stripe.com/test_eVa3do41l4Ye6KkcMN?prefilled_email=jenny%40example.com&client_reference_id=id_123
```

This is the guide's test URL shape; it does not authenticate the app user. [April example](../../raw/stripe-inapp-digital-goods-payment-links-2025.md#L131-L133); [November example](../../raw/stripe-mobile-digital-goods-payment-links-2026-11-07.md#L130-L132).

## Webhook fulfillment boundary

The guide says Stripe sends `checkout.session.completed` after a successful purchase and describes reading `client_reference_id` from the Session payload to reconcile an order or user. It instructs a production webhook endpoint subscribed to appropriate event types. The existing source's shorthand “identify user/order → grant entitlement” is only a flow sketch: the capture does not show a completed trusted identity check, payment-state validation, duplicate-event handling, or an actual successful access grant. A success-page redirect or an untrusted URL parameter alone cannot establish an entitlement. [April fulfillment](../../raw/stripe-inapp-digital-goods-payment-links-2025.md#L142-L155); [November fulfillment](../../raw/stripe-mobile-digital-goods-payment-links-2026-11-07.md#L141-L154).

## Related Pages

- [[stripe-inapp-payments]] — main mobile payment paths concept
- [[stripe-payment-links]] — Payment Links concept
- [[source-stripe-inapp-digital-goods-checkout]] — separate Stripe-hosted Checkout path
- [[source-stripe-inapp-digital-goods-custom-checkout]] — separate merchant-owned Elements web checkout path
- [[source-stripe-inapp-ios-android-purchases]] — dated platform overview
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-mobile-digital-goods-payment-links-2026-11-07|November 7, 2026 iOS Payment Links guide]] — full webpage content (163 lines)
- [[raw/stripe-inapp-digital-goods-payment-links-2025|April 22, 2026 iOS Payment Links guide]] — historical webpage content (165 lines)
