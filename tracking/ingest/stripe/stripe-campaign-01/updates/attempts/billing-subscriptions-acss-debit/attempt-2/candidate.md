---
title: "Stripe Subscriptions — Set Up Canadian Pre-Authorized Debit (ACSS Debit) Subscription"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/acss-debit"
raw_files:
  - "stripe-billing-subscriptions-acss-debit-2026-11-07.md"
  - "stripe-subscriptions-acss-debit-2026.md"
tags: [stripe, billing, subscriptions, acss-debit, canada, cad, pad, mandate, microdeposit]
---

## Summary

Stripe's Canadian pre-authorized debit (ACSS/PAD) subscription guide describes server-side Subscription creation and client-side Stripe.js `stripe.confirmAcssDebitPayment` for bank details and mandate acknowledgment. Its price example is CAD; this guide does not establish a universal CAD-only eligibility rule. As captured on 2026-11-07, Checkout subscription mode remains on a waitlist. In the paid initial-invoice flow, set the payment method as the subscription default for future billing after `invoice.payment_succeeded`; successful verification of a trial's `pending_setup_intent` instead sets the subscription default automatically. Microdeposit verification can take up to 10 days (bounded by the billing-period date), and fulfillment must wait for payment evidence as well as an active subscription. Enabled Direct Debit retries can automatically retry Canadian PAD insufficient-funds failures; the guide does not establish account eligibility.

## Key constraints

- **Canadian PAD subscription guide** — the illustrated monthly price is CAD, not a universal currency restriction.
- **Checkout subscription mode not yet supported** in the 2026-11-07 capture; waitlist described.
- **Conditional retries** — with Direct Debit retries enabled, Stripe can automatically retry Canadian PAD payments that fail because of insufficient funds. The 2026-05-13 capture instead said payments were never automatically retried; see dated evidence below.
- `acss_debit` payment method type appears explicitly in the 2026-05-13 Node.js example. The 2026-11-07 curl example omits that field; omission does not establish a default or universal recipe.

## Subscription creation

The 2026-11-07 guide creates an `incomplete` subscription using `payment_behavior=default_incomplete`, with `customer_account` for customer-configured Accounts v2 or `customer` for Customers v1. Its curl samples expand `latest_invoice.payment_intent`, while the adjacent prose still tells you to return `latest_invoice.confirmation_secret.client_secret`. The older Node.js sample below explicitly selects `acss_debit` and expands `latest_invoice.payments` and `latest_invoice.confirmation_secret`; the capture does not resolve whether the newer sample returns every value needed for the client step.

2026-05-13 Node.js example (Customers v1; historical sample, not a current universal recipe):

```js
stripe.subscriptions.create({
  customer: customerId,
  items: [{ price: priceId }],
  payment_behavior: 'default_incomplete',
  payment_settings: { payment_method_types: ['acss_debit'] },
  expand: ['latest_invoice.payments', 'latest_invoice.confirmation_secret']
})
```

## Client-side mandate flow

`stripe.confirmAcssDebitPayment(clientSecret, { payment_method: { billing_details: { name, email } } })`

- Required: `name` + `email` in billing_details
- Opens on-page modal UI for bank account collection + verification + mandate acknowledgment
- Customer acknowledges the Stripe-configured mandate once; later subscription charges need no fresh mandate acknowledgment. This does not guarantee later payment success.
- Instant verification can make the subscription `active`; manual verification leaves it `incomplete` pending microdeposits. Active status alone does not prove the first payment succeeded.

## Microdeposit extended window

Customers have **10 days** to verify (vs 23h normal), but not past billing period date. Max 3 failed attempts. Standard microdeposit codes: `32,45`=verify, `10,11`=exceed attempts.

## Payment confirmation and default payment method

Before fulfilling goods or services, the 2026-11-07 guide requires both an `active` related subscription and either the `invoice.paid` event or a `succeeded` underlying PaymentIntent. A subscription can be `active` while its first payment is still processing. Separately, in the paid initial-invoice flow, listen to `invoice.payment_succeeded` for a new subscription (`billing_reason=subscription_create`) and set `subscription.default_payment_method` from the payment method used for that invoice. The trial `pending_setup_intent` path below sets the subscription default automatically after successful verification. Do not substitute this default-method webhook step for the fulfillment check.

## Trial period

Returns `pending_setup_intent`. Use `stripe.confirmAcssDebitSetup` / `verifyMicrodepositsForSetup`. SetupIntent `succeeded` → auto-sets `default_payment_method`.

## Save for future use

Use a SetupIntent with `mandate_options.default_for=['invoice','subscription']` as shown in the CAD example. After it succeeds, update `configuration.customer.billing.default_payment_method` for a customer-configured Account v2, or `invoice_settings.default_payment_method` for a Customer v1.

## Dated retry statement

> [!warning] Contradiction
> The 2026-05-13 guide said Canadian PAD payments were never automatically retried. The 2026-11-07 guide says that, if Direct Debit retries is enabled, Stripe can automatically retry Canadian PAD payments that fail because of insufficient funds. This is a conditional possibility, not proof that retries are enabled for an account or apply to every failure.

## Test tokens (6)

`pm_acssDebit_success`, `pm_acssDebit_noAccount`, `pm_acssDebit_accountClosed`, `pm_acssDebit_insufficientFunds`, `pm_acssDebit_debitNotAuthorized`, `pm_acssDebit_dispute`

## Test accounts (7)

Institution `000`, Transit `11000`. Accounts: `000123456789` (success), `900123456789` (3-min delay success), `000222222227` (fail), `900222222227` (3-min fail), `000666666661` (fail microdeposits), `000777777771` (weekly limit), `000888888881` (transaction limit).

## Related pages

- [[stripe-acss-debit]] — concept page (updated with subscription facts)
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-billing-subscriptions-acss-debit-2026-11-07|2026-11-07 Canadian PAD subscription guide]] — current captured guide, including conditional retries and fulfillment check
- [[raw/stripe-subscriptions-acss-debit-2026|2026-05-13 Canadian PAD subscription guide]] — historical Node.js rendering and original retry statement
