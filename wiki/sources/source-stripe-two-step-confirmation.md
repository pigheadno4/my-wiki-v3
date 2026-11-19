---
title: "Stripe — Build Two-Step Confirmation"
type: source
date_ingested: 2026-05-11
date_updated: 2026-11-15
canonical_url: https://docs.stripe.com/payments/build-a-two-step-confirmation
original_format: webpage
raw_files:
  - "stripe-payments-build-a-two-step-confirmation-2026-11-07.md"
  - "stripe-two-step-confirmation-2026.md"
tags: [stripe, payment-element, confirmation-token, two-step, review-page, tax, customer-session, elements]
---

## Summary

The 2026-11-07 full capture describes a two-step web payment checkout: collect details in the Payment Element before creating a PaymentIntent, create a ConfirmationToken, optionally show a review page or run validation and tax calculation, then create the PaymentIntent on the server and confirm it from the client with the token. The 2026-05-11 capture documents the same core sequence. A ConfirmationToken or displayed review page is not a confirmed payment; a redirect or return page alone does not establish payment success or settlement.

## Flow and boundaries

1. Enable at least one payment method. Collect details with the Payment Element and deferred Elements configuration. Live checkout requires HTTPS; load Stripe.js directly from `js.stripe.com`, and avoid nesting the Payment Element in another iframe when redirect methods are possible.
2. On form submission, call `elements.submit()` for validation and wallet collection; handle an immediate error before calling `stripe.createConfirmationToken({ elements, params })`.
3. Pass the ConfirmationToken ID to the server. Retrieve the token and use `payment_method_preview` for relevant review-page details or additional business validation. The token carries collected details, but creating it has not created or confirmed a PaymentIntent.
4. Optionally calculate tax with Stripe Tax using a collected billing address, then show the total. The Payment Element does not calculate tax by default. The captured example's tax field access uses `paymentMethodPreview.billingDetails.address` while its review example uses `payment_method_preview`; these snippets do not establish one executable field shape without checking the relevant API/SDK.
5. Create a PaymentIntent on the server with the amount and currency, returning its `client_secret` to the client. If a Tax Calculation was used, the example illustrates using `amount_total` and linking its ID through `hooks.inputs.tax`; that hook and recalculation are commented optional code, not mandatory steps.
6. Call `stripe.confirmPayment({ clientSecret, confirmParams: { confirmation_token: id, return_url } })` on the client. The guide describes an optional `redirect: 'if_required'` for avoiding card redirects. Redirect methods can pass through an intermediate authorization site. Handle immediate errors and verify the resulting PaymentIntent state before treating an order as paid.

## Elements and payment-method conditions

- The November Elements table lists `mode`, `currency`, `amount`, `setupFutureUsage`, `captureMethod`, `onBehalfOf`, `allowedPaymentMethodTypes`, `paymentMethodConfiguration`, `paymentMethodCreation`, and `paymentMethodOptions`. Match supplied Elements options such as `captureMethod`, `setupFutureUsage`, and `paymentMethodOptions` to equivalent parameters at Intent creation or confirmation; mismatches can cause unexpected behavior or errors. The guide does not require every listed option to be set or all options to be literally identical to PaymentIntent fields.
- The 2026-05-11 table used `paymentMethodTypes`; the 2026-11-07 table uses `allowedPaymentMethodTypes`. In the November table, manually enabling card installments requires `mode='payment'` and explicitly specifying `allowedPaymentMethodTypes`, and conflicts with `paymentMethodCreation='manual'`. These dated table names do not prove a universal runtime rename or compatibility rule.
- November documents suppression of US bank account microdeposit verification only when the Payment Element renders before Intent creation and the payment amount is 0. The May table did not include this note; it is not a general rule for US bank account payments.
- This integration path excludes BLIK and **pre-authorized debits using ACSS**. It does not make a claim about every ACSS flow. A client-created deferred Intent cannot use `customer_balance` with dynamic payment methods because that path lacks the required customer-configured Account or Customer; for `customer_balance`, create the PaymentIntent on the server with that object and return its client secret.

## Saved payment methods and Accounts v2

Create a server-side `CustomerSession` using `customer` for a Customer or `customer_account` for a customer-configured Account, enable its `payment_element` component, configure the saved-method features (`payment_method_redisplay`, `payment_method_save`, `payment_method_save_usage`, `payment_method_remove`), and pass `customerSessionClientSecret` to `stripe.elements()`. The guide also describes `require_cvc_recollection` on both the PaymentIntent and Elements and `paymentElement.on('change', e => e.value.payment_method)` for detecting saved-method selection.

Both captures say not to combine `setup_future_usage` and `payment_method_save_usage` in one payment transaction. The May capture says doing so causes an integration error; the November capture says `setup_future_usage` controls save behavior. Preserve that dated explanation difference rather than assuming the old failure is impossible. In the captured Accounts v2 guidance, Accounts v2 is generally available for Connect users and in public preview for other Stripe users, with a preview API version required for preview users. November adds a Dashboard route under Account previews and features to enable **Reusable payment methods for Global Payouts**; this is an enrollment instruction, not proof of a particular account's eligibility.

## Layouts and disclosures

The Payment Element supports `accordion` (default) and `tabs` layouts through `elements.create('payment', { layout: { type: '...' } })`. The guide places responsibility on the merchant to disclose and obtain the rights and consents needed for Stripe's Elements interaction, cookie, and IP-address collection.

## Dated example changes

The November capture uses Ruby for several server examples and `https://js.stripe.com/endive/stripe.js` in its HTML example. The May capture includes Node.js server examples and `https://js.stripe.com/dahlia/stripe.js`. These are capture-specific examples; their difference does not establish Node.js removal, an obligatory Stripe.js migration, payment-method eligibility, or payment execution.

## Related Pages

- [[stripe]] — company overview
- [[stripe-payment-intents]] — PaymentIntent lifecycle, deferred creation, and confirmation context
- [[source-stripe-payments-existing-customers]] — saved-payment-method display for returning customers

## Raw Sources

- [[raw/stripe-payments-build-a-two-step-confirmation-2026-11-07|Full canonical guide captured 2026-11-07]]
- [[raw/stripe-two-step-confirmation-2026|Full canonical guide captured 2026-05-11]]
