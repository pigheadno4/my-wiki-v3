---
title: "Build a Subscriptions Integration with Elements"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/advanced/build-subscriptions"
raw_files:
  - "stripe-build-subscriptions-elements-2025.md"
tags: [stripe, subscriptions, checkout-sessions, payment-intents, elements, entitlements, billing, plan-change, proration, cancel, accounts-v2]
---

## Summary

The 2026-04-21 capture at this URL contains **two distinct web subscription integrations** using Elements: Checkout Sessions API with embedded components and a lower-level Payment Intents API route. Both use Products, recurring Prices, customer records, subscription/invoice events, and status-aware provisioning; their client secrets and confirmation calls differ. The 2026-11-07 capture is only an index linking these two variants. It does not verify either variant's current body or establish a deprecation or changed runtime behavior. The instructions below are dated to the April capture.

## Choose the Variant

| April 2026 captured path | Server and client boundary |
| --- | --- |
| [Checkout Sessions API variant](https://docs.stripe.com/payments/advanced/build-subscriptions.md?platform=web&ui=embedded-components) | Server creates a subscription-mode Session with `ui_mode: "elements"`, then sends **Session `client_secret`**. Client initializes Checkout Elements SDK and calls Checkout `actions.confirm()` (old lines 10–30, 349–430, 435–464, 583–617). |
| [Payment Intents API variant](https://docs.stripe.com/payments/advanced/build-subscriptions.md?platform=web&ui=elements) | Server creates a subscription with `payment_behavior: "default_incomplete"`, expands `latest_invoice.confirmation_secret` for the first PaymentIntent, then sends that **invoice PaymentIntent confirmation secret**. Client creates regular Elements and calls `stripe.confirmPayment()` (old lines 1115–1133, 1503–1558, 2429–2492). |

The April guide recommends Checkout Sessions with Payment Element for most integrations because it provides tax, discount, shipping, and currency support with less custom code. Payment Intents is presented as a lower-level path requiring more code and maintenance (old lines 28–34, 1131–1137). The November index names both paths but gives no recommendation (new lines 9–14).

## Shared Objects and Customer Models

The guide covers Product, Price, Subscription, Invoice, PaymentIntent, PaymentMethod, Feature, ProductFeature, and active Entitlement, using either a Customers v1 `Customer` or a customer-configured Accounts v2 `Account` (old lines 46–73, 1150–1189). The sample sells monthly Basic at 5 USD and Premium at 15 USD; these are illustrative example prices (old lines 89–107, 1205–1225). ProductFeatures associate features with products; active entitlements are the feature-access source to query or track via `entitlement.active_entitlement_summary.updated` (old lines 62–73).

For Accounts v2, the April capture says general availability for Connect users and public preview for other Stripe users; preview participants need a preview API version (old lines 265–273, 1381–1389). Its Session code samples pin `apiVersion: "2026-03-25.dahlia"` (old lines 357–430). That example version is not a universal Accounts v2 requirement or evidence of a particular account's access in November. Customers v1 uses `customer`; Accounts v2 uses `customer_account` in the examples (old lines 357–430, 1511–1558).

## Checkout Sessions Path — April 2026 Capture

The server sample creates a Checkout Session with `mode: "subscription"`, `ui_mode: "elements"`, a customer identifier, recurring Price line item, and return URL, then returns `session.client_secret` (old lines 349–430). The client passes that secret to `stripe.initCheckoutElementsSdk`, mounts `checkout.createPaymentElement()`, and can display `getSession().lineItems` and `session.total.total.amount` (old lines 435–581).

The original source's confirm fragment omitted the `checkout.loadActions()` call and left `actions` undefined. This **partial illustrative fragment** shows the missing boundary from old lines 449–464 and 594–617; it assumes an initialized `stripe` instance and a Session `clientSecret` received from the server:

```js
const checkout = stripe.initCheckoutElementsSdk({ clientSecret });
checkout.on("change", (session) => {
  document.getElementById("pay-button").disabled = !session.canConfirm;
});
const loadActionsResult = await checkout.loadActions();
if (loadActionsResult.type === "success") {
  const { actions } = loadActionsResult;
  document.getElementById("pay-button").addEventListener("click", async () => {
    const result = await actions.confirm();
    if (result.type === "error") {
      document.getElementById("confirm-errors").textContent = result.error.message;
    }
  });
}
```

The April React variant instead uses `CheckoutElementsProvider` and `useCheckout()` from `@stripe/react-stripe-js/checkout`, with `checkoutState.checkout.confirm()` (old lines 467–518, 620–660). These are Checkout calls, not the Payment Intents `stripe.confirmPayment()` call.

## Payment Intents Path — April 2026 Capture

After the customer chooses a Price, the server creates a subscription with `payment_behavior: "default_incomplete"`, `save_default_payment_method: "on_subscription"`, and an expanded `latest_invoice.confirmation_secret` (old lines 1465–1558). The guide's `billing_mode: { type: "flexible" }` sample says that feature needs API version `2025-06-30.basil` or later (old lines 1503–1509). Its response examples show `status: "incomplete"` before the first payment (old lines 1563–1972, 1975–2383); creating that subscription is **not** proof of paid access.

The client passes the invoice PaymentIntent secret to `stripe.elements({ clientSecret })`, mounts a Payment Element, and calls `stripe.confirmPayment({ elements, confirmParams: { return_url } })` (old lines 2385–2492). The return flow checks the PaymentIntent status: `succeeded`, `processing`, or `requires_payment_method` require different customer messages and follow-up (old lines 2494–2551). A redirect, created Subscription, or `processing` state alone does not establish settled payment or access.

## Provisioning, Changes, and Cancellation

Verify webhook signatures and reconcile `invoice.paid`, `invoice.payment_failed`, and `customer.subscription.created`, `.updated`, and `.deleted` state (old lines 663–753, 2553–2643). A `customer.subscription.created` event means **record and check the subscription state**, not automatically grant paid access. The April instructions check `subscription.status`; for paid access, `active` status or active entitlements govern provisioning, while trial access needs its own `trialing` qualification. An initial Payment Intents subscription can still be `incomplete` (old lines 745–753, 1503–1510, 1967, 2377, 2633–2641). `invoice.paid` is a paid event, but the application still checks the governing state and product before provisioning. Store product, subscription, status, and customer identifiers to handle later failures and cancellations.

| April captured event | Appropriate action |
| --- | --- |
| `invoice.paid` | Recheck paid status or active entitlement; provision or renew eligible access after trial |
| `invoice.payment_failed` | Notify and recover payment; later subscription can become `past_due` |
| `customer.subscription.created` | Record and inspect status; do not treat creation as payment |
| `customer.subscription.updated` | Sync status, plan, and access |
| `customer.subscription.deleted` | Revoke access for the canceled subscription |

The optional plan-change example updates an existing subscription item with its ID and new Price and triggers `customer.subscription.updated`; `invoices.createPreview` shows a possible prorated amount, with `customer` or `customer_account` depending on model (old lines 828–1017, 2718–2907). The cancellation examples call `stripe.subscriptions.del(id)` immediately and then handle `customer.subscription.deleted`; they say a canceled subscription cannot be reactivated and a new one must be created. This example is **not** a `cancel_at_period_end` flow (old lines 755–804, 2645–2694).

## Tests and Other Locators

The April capture provides card, BECS, and SEPA sandbox test values, including authentication, decline, and asynchronous `processing` cases (old lines 806–826, 2696–2716). It also shows optional PaymentMethod retrieval for display and disclosure duties for Elements interaction data (old lines 1019–1113, 2909–3003). These examples are dated documentation, not proof of successful payment, account eligibility, or current variant behavior.

## Related Pages

- [[stripe-subscriptions]] — subscription states, paid versus trial access, and this guide's route
- [[source-stripe-checkout-build-subscriptions]] — earlier subscription guide
- [[stripe-checkout]] — Checkout concept and Sessions flows

## Related raw API references

- [[raw/stripe-payments-advanced-build-subscriptions-2026-11-07|2026-11-07 variant index only]] — names the Checkout Sessions and Payment Intents URLs; contains no variant-body payment instructions

## Raw Sources

- [[raw/stripe-build-subscriptions-elements-2025|Full two-variant guide, fetched 2026-04-21]] — dated factual evidence for the flows above
