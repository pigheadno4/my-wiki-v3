---
title: "Accept iOS Digital Goods Payments with Stripe Checkout"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/mobile/digital-goods/checkout"
raw_files:
  - "stripe-mobile-digital-goods-checkout-2026-11-07.md"
  - "stripe-inapp-digital-goods-checkout-2025.md"
tags: [stripe, mobile, ios, digital-goods, checkout, universal-links, storekit, webhooks, app-to-web]
---

## Summary

Stripe's 2026-11-07 capture describes a US iOS digital-goods and subscription app-to-web Checkout path: model credits with Products and Prices, use a customer-configured Account (Accounts v2) or Customer (Customers v1), open Checkout in Safari, return through a Universal Link, and update server-owned entitlements from payment events. The 2026-04-22 capture documented the Customers v1 route. The guide's US storefront statement is dated documentation, not a current App Store approval or account-eligibility determination.

> See also [[source-stripe-inapp-ios-android-purchases]] for the platform overview. Android US direct in-app processing is a separate route; physical goods, outside-app consumption, and person-to-person services use the native app payment guide. Managed Payments is an optional merchant-of-record integration, not part of this baseline flow.

## Customer identity and availability

- **Accounts v2 branch (2026-11-07):** The guide recommends customer-configured Account objects for most use cases. It says Accounts v2 is generally available for Connect users and in public preview for other Stripe users. Preview participants must specify a preview API version and enable **Reusable payment methods for Global Payouts** in Dashboard Account previews and features. This is captured availability wording, not proof of eligibility for a particular account. The example creates an Account with `stripe.v2.core.accounts.create` and stores its ID against the app user (raw lines 194–219).
- **Customers v1 branch (retained):** Create or reuse a Customer, store that ID against the app user, and pass `customer` in the Checkout Session. The full branch remains in the 2026-11-07 guide (raw lines 227–256, 419–524); the new recommendation does not establish deprecation.
- The guide's one-time and subscription Sessions use `customer_account` for Accounts v2 (raw lines 345–358, 391–404) and `customer` for Customers v1 (raw lines 451–464, 498–511). Both example branches include `integration_identifier` as an integration label for independent conversion measurement; this example does not prove the field is required or that measurement occurred.

## Flow overview

1. For the documented US iOS case, detect the app's StoreKit storefront and check `SKPaymentQueue.canMakePayments()` before offering the buy button. The StoreKit check respects device purchase restrictions; it is not a policy approval.
2. Configure Products and Prices, then create or reuse the app user's customer-configured Account or Customer according to the selected branch. Create a Checkout Session on the server with the branch's identity, a Price in `line_items`, `mode: 'payment'` or `'subscription'`, `origin_context: 'mobile_app'`, and a Universal Link `success_url`. Return the Session URL to the app.
3. Open the Session URL in Safari with `UIApplication.shared.open`. Configure the domain's `/.well-known/apple-app-site-association` as `application/json`, the `applinks:` Associated Domains entitlement, a browser fallback page, and the app's incoming-URL handler.
4. The Universal Link can bring the customer back to the app; the app should fetch current entitlements from its server. The return URL is a UI signal, not authority to grant credits.
5. Independently process verified server webhooks and grant a coin transaction idempotently only after paid status. With optional dynamic payment methods, `checkout.session.completed` can precede payment clearance: check `session.payment_status === 'paid'`; otherwise wait for `checkout.session.async_payment_succeeded` and handle `checkout.session.async_payment_failed`. This paid-status qualification comes from [[source-stripe-checkout-dashboard-payment-methods]], not from an executable example in this guide.
6. The captured guide says Checkout redirects after webhook acknowledgement, or after about 10 seconds when the event is not acknowledged properly. Redirect and fulfillment have separate timing; do not infer payment finality from their order.

## Universal Links setup

1. Serve `/.well-known/apple-app-site-association` with the `application/json` MIME type.
2. Add `applinks:example.com` to Associated Domains.
3. Provide a fallback page at the HTTPS success URL if the app link does not open.
4. Handle the incoming URL in the app, then fetch server-owned entitlements.

```json
{
  "applinks": {
    "details": [{
      "appIDs": ["TEAMID.com.example.MyApp"],
      "components": [{ "/": "/checkout_redirect*" }]
    }]
  }
}
```

The guide includes the association-file setup and Universal Link debugging steps, including `?mode=developer`, Associated Domains Development, and `swcutil_show.txt` (new raw lines 258–310, 706–749; old raw lines 174–226).

## Checkout Session fields

The following are branch-specific fields from the captured one-time-payment examples, not complete runnable endpoints. Use `mode: 'subscription'` and a recurring Price for the subscription examples.

```javascript
const common = {
  line_items: [{ price: priceId, quantity: 1 }],
  mode: 'payment',
  origin_context: 'mobile_app',
  success_url: 'https://example.com/checkout_redirect/success',
};
// Accounts v2 example: { ...common, customer_account: customerAccountId }
// Customers v1 example: { ...common, customer: customerId }
```

The examples also show optional `integration_identifier` as an integration label. The captured guide says Apple Pay appears by default on a supported device and describes dynamic payment methods as an additional option (new raw lines 417, 524). Checkout studio provides configure/preview navigation (new raw line 11); Checkout and Payment Links settings can optionally show yearly subscription prices in monthly terms and control tax display (new raw lines 755–757).

## Swift client and fulfillment boundary

The guide opens the server-returned Session URL in Safari. Its `.onOpenURL` success handler displays a success view and says to fetch the latest customer entitlements from the server (new raw lines 526–570). A substring match on a return URL is illustrative presentation handling, not a payment check.

> [!warning] Contradiction
> Both captured Node.js webhook examples declare `let event` inside `if (webhookSecret)` and later read `event.data.object` outside that block (old raw lines 447–474; new raw lines 641–668). The sample therefore has a block-scope error before customer lookup. The shared new sample also indexes `session.customer` although the Accounts v2 Sessions use `customer_account` (new raw lines 354, 400, 668–673). Neither branch is verified runnable fulfillment code; these captures do not resolve Accounts v2 event-to-app-user mapping. Implement and verify event extraction, identity mapping, paid-status checks, asynchronous outcomes, and idempotency before using a handler to grant credits.

## Test cards

| Number | Captured test outcome |
| --- | --- |
| 4242 4242 4242 4242 | Immediate successful processing |
| 4000 0000 0000 3220 | 3D Secure 2 authentication then success |
| 4000 0000 0000 9995 | `insufficient_funds` decline |

These documented test numbers do not prove a particular app integration is approved or working.

## Out of scope and related pages

- User authentication is assumed; the examples rely on an app user database and do not build login.
- Native StoreKit in-app purchases are outside this app-to-web Checkout guide.
- [[stripe-inapp-payments]] — mobile payment context
- [[stripe-checkout]] — Checkout Sessions and paid-status fulfillment
- [[source-stripe-inapp-ios-android-purchases]] — platform overview
- [[source-stripe-checkout-dashboard-payment-methods]] — delayed-method payment-status and asynchronous-event rule

## Raw Sources

- [[raw/stripe-mobile-digital-goods-checkout-2026-11-07|2026-11-07 iOS digital-goods Checkout guide]]
- [[raw/stripe-inapp-digital-goods-checkout-2025|2026-04-22 earlier Customers v1 guide]]
