---
title: "Add Custom Payment Methods to the Payment Element"
type: source
date_ingested: 2026-04-21
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/payment-element/custom-payment-methods"
raw_files:
  - "stripe-payment-element-custom-payment-methods-2025.md"
tags: [stripe, payment-element, custom-payment-methods, cpmt, third-party, payment-records, reporting, xss]
---

## Summary

Stripe Elements can display custom payment methods (CPMs) that the merchant processes through a third-party payment service provider (PSP). The November 7, 2026 capture is a navigation page with routes for Checkout Sessions (`payment-ui=embedded-components`) and Payment Intents (`payment-ui=elements`). It links the variants without including their implementation bodies. The April 21, 2026 capture briefly describes merchant-instructed payments with the Payment Element under Checkout Sessions and contains the detailed Payment Intents implementation below.

The separate May 8, 2026 product overview marked Checkout and Express Checkout Element unsupported. Its November 7, 2026 matrix lists Checkout as supported and Express Checkout Element as supported in private preview, and links to an Express Checkout section. The captured November base implementation page still lists two variants and contains no Express Checkout implementation section. Individual Checkout UI support, merchant eligibility and parity with the Payment Intents flow require separate evidence. See [[source-stripe-custom-payment-methods]] and the dated matrices in Related Raw API References.

## Payment Intents Elements Setup (April 21, 2026)

The detailed April integration calls for a Stripe account and a completed deferred payments integration.

1. In Dashboard, go to Settings > Payments > Custom Payment Methods, set the display name and logo, and obtain the `cpmt_` method type ID.
2. Add the type ID to the `customPaymentMethods` array when initializing `stripe.elements({...})`. CPMs appear last by default. Set `paymentMethodOrder` to change the order.
3. Submit and validate the Elements form, then route the selected method. The merchant processes and finalizes the custom payment through its PSP under the applicable agreement and laws.
4. Optionally report the actual PSP result to Stripe for consolidated reporting.

## Display Types

### Static

```js
customPaymentMethods: [{
  id: 'cpmt_....',
  options: { type: 'static', subtitle: 'Optional subtitle' }
}]
```

![Static CPM in Payment Element](../raw/assets/stripe-payment-element-custom-pm-static.png)

A customer selection can route to the merchant’s payment flow or an external payment page.

### Embedded (Preview)

```js
customPaymentMethods: [{
  id: 'cpmt_....',
  options: {
    type: 'embedded',
    embedded: {
      handleRender: (container) => { /* render into container */ },
      handleDestroy: () => { /* cleanup */ }
    }
  }
}]
```

![Embedded CPM with custom content](../raw/assets/stripe-payment-element-custom-pm-embedded.png)

The April examples use `handleRender` to render in the supplied DOM container and `handleDestroy` for cleanup. The React example uses a portal. Render only trusted content in the supplied container to prevent cross-site scripting. The April warning calls the callback `handleEmbed`. The callback list and examples use `handleRender`. The tag-specific Stripe.js 9.14.0 declarations list `handleRender(HTMLDivElement)` and optional `handleDestroy`. Those declarations also include a private-access beta Express Checkout configuration, with its own scope. See [[source-github-stripe-js]].

## Submit Handler Pattern

In the April deferred Payment Intents flow, await `elements.submit()` and handle submission errors before routing. Use the returned `selectedPaymentMethod` to route the matching `cpmt_` to the merchant server or an external payment page. Other selections follow the Stripe payment flow. The November Stripe.js Submit reference specifically scopes the call to Elements created without an Intent and requires awaiting completion before continuing.

April’s illustrative request uses POST on the client and GET in the server example for the same route, with abbreviated validation and PSP result handling. The merchant’s implementation needs a consistent request contract and must use the external processor’s actual result. Display, selection and redirect establish only progress in the checkout flow.

## Recording to Stripe (Optional)

In April’s Payment Intents server example, create a `PaymentMethod` with `type: 'custom'` and set `custom.type` to the Dashboard’s `cpmt_` type ID. Put the resulting `pm_` instance ID in `payment_method_details.payment_method` on the `paymentRecords.reportPayment(...)` request. The external processor’s payment reference belongs separately in `processor_details.custom.payment_reference`. Include the amount, currency, timing and actual PSP outcome. The sample uses `guaranteed` after successful PSP processing and sends `2026-03-25.dahlia` with `invoice_partial_payments_beta=v3` in its Stripe-Version header.

The separate November Report a payment reference shows `POST /v1/payment_records/report_payment` with `2026-10-28.endive` and inline custom payment method details. Its initialized-record example returns `payment_method: null` and zero guaranteed amount. The reference also allows reporting terminal outcomes directly. The April `pm_` pattern and its beta suffix belong to that example; version compatibility and merchant access require separate confirmation. A Payment Record describes the reported external activity. External payment completion depends on the PSP result and settlement follows the external PSP’s process.

## Logo Guidelines

- For transparent background logos, ensure contrast with the Payment Element background.
- For background fill logos, include rounded corners in the file if needed.
- Use a variant that scales to 16×16px, typically the standalone mark.

## Related Pages

- [[stripe-custom-payment-methods]] — concept page
- [[source-stripe-custom-payment-methods]] — product overview and integration matrix
- [[source-github-stripe-js]] — versioned web SDK declarations
- [[stripe-payment-element]] — parent element
- [[stripe-payment-intents]] — API in the detailed April implementation
- [[stripe]] — company page

## Related raw API references

- [[raw/stripe-payments-payment-element-custom-payment-methods-2026-11-07|November variant index]] — November 7 navigation index for Checkout Sessions and Payment Intents
- [[raw/stripe-custom-payment-methods-2025|May product overview]] — May 8 product overview and integration matrix
- [[raw/stripe-payments-payment-methods-custom-payment-methods-2026-11-07|November product overview]] — November 7 product overview and integration matrix
- [[raw/stripe-js-elements-submit-2026-11-07|Stripe.js Submit reference]] — Stripe.js submit API for Elements initialized without an Intent
- [[raw/stripe-api-payment-record-report-2026-11-07|Report a payment API]] — versioned Endive Report a payment example and available outcomes

## Raw Sources

- [[raw/stripe-payment-element-custom-payment-methods-2025|April detailed implementation]] — April 21, 2026 full capture, including brief Checkout Sessions and detailed Payment Intents guidance
