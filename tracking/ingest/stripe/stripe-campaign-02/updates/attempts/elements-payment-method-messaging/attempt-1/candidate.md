---
title: "Stripe Payment Method Messaging Element"
type: source
date_ingested: 2026-11-09
canonical_url: https://docs.stripe.com/elements/payment-method-messaging
original_format: webpage
raw_files:
  - "stripe-elements-payment-method-messaging-2026-11-07.md"
  - "stripe-payment-method-messaging-element-2025.md"
tags: [stripe, elements, bnpl, buy-now-pay-later, payment-method-messaging, klarna, affirm, afterpay, clearpay, connect]
---

## Summary

The Payment Method Messaging Element is a web Stripe UI component that displays localized information about available buy now, pay later (BNPL) plans on product, cart, and payment pages. Its displayed plans depend on the customer's location, currency, and payment amount. It is messaging about possible plans, not evidence of payment authorization or completion of a financing application.

## Key Takeaways

- The captured plain Stripe.js and React examples initialize with a publishable key, pass `amount` and `currency`, and show `countryCode` as optional. The plain Stripe.js example uses `stripe.elements()` without a `clientSecret`; these examples alone do not establish every API validation rule or a universal PaymentIntent requirement.
- When **Dynamic payment methods** are used, the Element pulls payment method preferences from the Stripe Dashboard. A manually specified `paymentMethodTypes` list is an alternative. Either way, it displays only plans for which the customer is eligible.
- By default, payment methods use dynamic ordering optimized for the customer; `paymentMethodOrder` can set a preferred order. Ordering is distinct from Dashboard preference selection.
- If only a “pay now” option is available, or the supplied `countryCode` and `currency` combination has no eligible plan, no messaging renders.
- The captures list Affirm, Afterpay/Clearpay, and Klarna; Klarna is described here for one-time payments only.
- The info icon opens a modal with a usage overview, a terms summary per available plan, and links to full terms. Merchants remain responsible for data-use disclosures and rights/consents, and for applicable BNPL promotion rules.

## Initialization

The 2026-11-07 HTML example loads `https://js.stripe.com/endive/stripe.js`, creates a placeholder, and mounts the Element:

```js
const stripe = Stripe('<<YOUR_PUBLISHABLE_KEY>>');
const elements = stripe.elements();
const options = {
  amount: 9900, // 99.00 USD
  currency: 'USD',
  countryCode: 'US', // optional buyer country
};
elements.create('paymentMethodMessaging', options).mount('#payment-method-messaging-element');
```

The 2026-04-21 capture instead showed `https://js.stripe.com/dahlia/stripe.js`. The changed example path does not establish that the earlier path is unsupported or that a deployment must migrate. Both captures also show `<PaymentMethodMessagingElement options={{...}} />` from `@stripe/react-stripe-js` inside `<Elements>`.

## Options Shown in the Captures

| Option | Evidence and role |
| --- | --- |
| `amount` | Included in both plain Stripe.js and React examples as the payment amount in the smallest currency unit; the captures do not explicitly declare option requiredness. |
| `currency` | Included in both examples as a currency code; the captures do not explicitly declare option requiredness. |
| `countryCode` | Marked optional in examples; buyer country affects plan eligibility. |
| `paymentMethodTypes` | Manual list of payment methods as an alternative to Dashboard preferences when using Dynamic payment methods; eligibility filtering still applies. |
| `paymentMethodOrder` | Sets a preferred display order instead of the default dynamic ordering. |

The linked Stripe.js option reference and Dynamic payment methods guide were not assessed for this source. Their API validation and account-specific eligibility details should not be inferred from these captures.

## Supported Plans and Display

The captured page lists plans from Affirm, Afterpay/Clearpay, and Klarna (one-time payments only). It does not state that every provider or plan is available for every customer. Eligibility depends on location, currency, and amount. Only “pay now” availability produces no message, as does a `countryCode`/`currency` combination with no eligible plan.

## Info Modal

Selecting the ⓘ icon opens a modal with a step-by-step BNPL usage overview, a summary of terms for each available plan, and a link to each plan's full terms. The older capture contains [a local preview image](../raw/assets/stripe-payment-method-messaging-element-info-modal.png); the newer capture points to a different image URL. That link change is navigation, not evidence of changed modal behavior.

## Connect

For Connect platforms creating direct charges, identify the connected account rendering the Element by setting `stripeAccount` on the Stripe instance before creating the Element:

```js
const stripe = Stripe('<<YOUR_PUBLISHABLE_KEY>>', {
  stripeAccount: '{{CONNECTED_ACCOUNT_ID}}',
});
```

## Appearance

The captures show the Appearance API for color, typography, and spacing variables and a `.PaymentMethodMessaging` rule such as `textAlign`:

```js
const appearance = {
  variables: {
    colorText: 'rgb(84, 51, 255)',
    fontSizeBase: '16px',
    fontFamily: 'Ideal Sans, system-ui, sans-serif',
  },
  rules: { '.PaymentMethodMessaging': { textAlign: 'right' } },
};
const elements = stripe.elements({appearance});
```

## Disclosure and Promotion

Stripe says it collects customer interaction information with Elements, including cookies and IP addresses to identify Elements seen during a checkout session. The merchant is responsible for the disclosures, rights, and consents needed for that use. Stripe also places responsibility for compliance with applicable BNPL promotion laws, rules, and regulations on the merchant. These are obligations described by the captured page, not a claim that rendering the Element completes compliance.

## Related Pages

- [[stripe-payment-method-messaging-element]] — concept page
- [[stripe-elements]] — parent Elements framework
- [[stripe]] — company page
- [Stripe.js Element option reference](https://docs.stripe.com/js/elements_object/create_element?type=paymentMethodMessaging) — linked reference; contents not assessed for this update
- [Dynamic payment methods guide](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods) — linked guide; contents not assessed for this update

## Raw Sources

- [[raw/stripe-elements-payment-method-messaging-2026-11-07|2026-11-07 Stripe Payment Method Messaging Element capture]] — same canonical URL, current collected page
- [[raw/stripe-payment-method-messaging-element-2025|2026-04-21 Stripe Payment Method Messaging Element capture]] — earlier same-URL page and dated example
