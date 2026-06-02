---
title: "Save and Retrieve Customer Payment Methods"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-payment-element-saved-payment-methods-2025.md"
tags: [stripe, payment-element, saved-payment-methods, allow-redisplay, cvc-recollection, link, customer-session, subscription]
---

## Summary

Reference for the Payment Element's Saved Payment Methods feature. Covers `allow_redisplay` semantics, CVC re-collection, subscription removal warning, handling legacy `unspecified` PMs, Link integration, and consent override.

## Supported Payment Methods

`card`, `us_bank_account`, `acss_debit`, `sepa_debit`, `bacs_debit`, `au_becs_debit`, `nz_bank_account`

## Link Integration

Works without extra config. Business-saved PMs shown first (before Link PMs) after page loads.

![Payment Element with Link and saved PM checkbox](../raw/assets/stripe-payment-element-spm-with-link.png)
![Payment Element with saved PM selected](../raw/assets/stripe-payment-element-spm-saved.png)

## `allow_redisplay` Values

| Value | Meaning | When set |
| --- | --- | --- |
| `always` | PM renders and can be reused for future sessions | Customer checks "Save for future" |
| `limited` | PM won't display for future purchases | Checkbox unchecked; subscription auto-save |
| `unspecified` | PM won't render in Payment Element by default | Legacy PMs (saved outside checkout) |

**Display order**: most recently added first; default PM always first.

## CVC Re-Collection

```js
payment_method_options: { card: { require_cvc_recollection: true } }
// Set on the PaymentIntent
```

## Subscription Removal Warning

Removing a saved PM from the Payment Element's Saved section **also removes it from active subscriptions**. To prevent this:

```js
// In CustomerSession options
components: {
  payment_element: {
    features: { payment_method_remove: 'disabled' }  // prevent removal
  }
}
```

Manage payment method changes through an account settings page that shows existing subscriptions instead.

## Legacy PMs with `allow_redisplay: 'unspecified'`

PMs saved from Card Element, direct API use, etc. have `unspecified` and won't display. Fix:

1. **Update individually**: `stripe.paymentMethods.update(id, { allow_redisplay: 'always' })` — only if proper consent was collected
2. **CustomerSession filter**: configure `features.payment_method_allow_redisplay_filters` to include `unspecified`

CustomerSession is required for Payment Element to display any saved PMs.

## Consent Override

If collecting consent outside the Payment Element (e.g. in T&C text):

```js
stripe.confirmPayment({
  elements,
  confirmParams: {
    payment_method_data: {
      allow_redisplay: 'always'  // overrides checkbox value
    }
  }
});
```

Also works with `confirmSetup` and `createConfirmationToken`.

## Payment Intents Path: CustomerSession Required

For the PI path, create a CustomerSession alongside the PaymentIntent and pass `customerSessionClientSecret` to Elements:

```js
stripe.elements({
  clientSecret: piSecret,
  customerSessionClientSecret: csSecret,
});
```

Features configured on CustomerSession: `payment_method_redisplay`, `payment_method_save`, `payment_method_save_usage`, `payment_method_remove`.

> `setup_future_usage` on PaymentIntent and `payment_method_save_usage` on CustomerSession are **mutually exclusive** — setting both causes an integration error.

## Related Pages

- [[stripe-saved-payment-methods]] — concept page
- [[source-stripe-checkout-save-during-payment]] — Checkout Sessions save-during-payment patterns
- [[stripe-payment-intents]] — Payment Intents concept page
- [[stripe-link-authentication-element]] — Link autofill integration

## Raw Sources

- [[stripe-payment-element-saved-payment-methods-2025]] — verbatim saved PMs guide
