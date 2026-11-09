---
title: "Stripe: Save ACSS/PAD Payment Details for Future Payments"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/acss-debit/set-up-payment"
raw_files:
  - "stripe-acss-set-up-payment-2025.md"
tags: [stripe, acss, acss-debit, canada, cad, setup-intents, mandates, microdeposits, save-payment-method]
---

## Summary

The retained 2026-05-02 guide explains saving Canadian pre-authorized debit (PAD/ACSS Debit) bank details for later payments through Checkout setup mode or the Direct API SetupIntent flow. The 2026-11-07 exact-URL capture is only a variant index linking Checkout, Elements, and Direct API. Its newly listed Elements route is navigation, not evidence of that variant's implementation, supported objects, account eligibility, or a change to the older Checkout/Direct API instructions. None of the linked variant bodies was captured in this job.

The older guide describes Canadian PAD as a delayed-notification method: funds are not immediately available after payment, and a payment typically takes five business days to arrive. It permits CAD or USD, but the debit currency must match the customer's bank-account currency; a mismatch can produce a delayed failure up to five business days later (old raw lines 18–24, 337–341).

## Mandate options in the 2026-05-02 guide

The customer must authorize the PAD agreement; a Mandate records that authorization. Both Checkout and Direct API parameter tables distinguish requiredness (old raw lines 70–76 and 380–386):

| Parameter under `payment_method_options[acss_debit]` | Requiredness and meaning |
| --- | --- |
| `currency` | Required; `cad` or `usd`, matching the bank-account currency |
| `mandate_options.payment_schedule` | Required; `interval`, `sporadic`, or `combined` |
| `mandate_options.transaction_type` | Required; `personal` or `business` |
| `mandate_options.interval_description` | Required only for `interval` or `combined` schedule |
| `mandate_options.default_for` | Optional array of mandate purposes |

## Checkout setup mode (2026-05-02 guide)

The Checkout example creates a Customer, then a Checkout Session with `mode: 'setup'`, `payment_method_types: ['acss_debit']`, and the applicable mandate options. It gives Stripe-hosted and full embedded page examples, each with a different return URL shape (old raw lines 39–128). The hosted modal collects account details, mandate authorization, and either instant verification or a microdeposit fallback. Microdeposits normally appear in one to two business days and the customer receives a verification link (old raw line 131). The guide optionally selects `verification_method: 'instant'` or `'microdeposits'` on the Checkout Session (old raw lines 215–325). Its token, account-number, and `32`/`45` amount tables are **test/sandbox cases**, not evidence of a live bank debit (old raw lines 133–168).

## Direct API SetupIntent (2026-05-02 guide)

Create or retrieve a Customer, then create a SetupIntent with `payment_method_types: ['acss_debit']`, customer identity, and matching currency and mandate options; pass the **SetupIntent** client secret to the customer-facing flow (old raw lines 356–447). The historical examples show a Customers v1 `customer` field and later separate Accounts v2 `customer_account` examples for verification-method options; those illustrative snippets do not establish universal account eligibility.

On the client, `stripe.confirmAcssDebitSetup` requires the account-holder name and customer email in `payment_method.billing_details`. Its hosted on-page modal collects bank account details, verification, mandate presentation, and authorization (old raw lines 505–540). `succeeded` means the account was instantly verified **or verification was unnecessary**; `requires_action` means further bank verification is needed (old raw lines 544–549). SetupIntent success saves the method and mandate for possible future use; it is not a successful future debit or funds receipt. The guide requires mandate and bank-detail confirmation email after setup; Stripe sends it by default unless custom notifications are configured (old raw lines 551–553).

For a customer taking the microdeposit route, the old guide gives a hosted verification page or `stripe.verifyMicrodepositsForSetup` with a test amount pair `[32, 45]`. Deposits appear in one to two business days; there are three failed attempts and a ten-day timeout. Successful verification returns SetupIntent `succeeded` and a `setup_intent.succeeded` event; the error table uses `last_setup_error` for failure details (old raw lines 567–631). The prose also calls the timeout object a PaymentIntent and names `setup_intent.payment_failed`; those inconsistent words in a SetupIntent section are not proof that setup completion is payment completion or that the exact failure event name is correct. Verify event behavior against a current version-specific reference before implementation.

## Later off-session charging (2026-05-02 guide)

With an **existing authorized mandate**, charge only within that mandate's terms; debiting outside them can lead to a dispute. A later off-session PaymentIntent is a separate action using `customer`, `payment_method`, and `mandate` IDs, amount/currency, `payment_method_types: ['acss_debit']`, and `confirm: true` (old raw lines 170–210, 670–711). A debit notification email must be sent when reusing the mandate; Stripe handles it by default unless the integration sends custom notifications (old raw lines 213 and 713). A confirmed PaymentIntent or a successful SetupIntent is not proof that a delayed debit finally settled.

If the terms change, the guide instead says to reuse the PaymentMethod with **new customer authorization and a new mandate**: include the existing `payment_method` ID when creating a new Intent, omit the bank details in confirmation, send a new mandate confirmation email, and expect a three-day charge delay (old raw lines 715–722). This is distinct from a debit under an existing mandate.

## Related Pages

- [[stripe-acss-debit]] — Canadian PAD scope, mandate and payment lifecycle
- [[source-stripe-acss-accept-payment]] — accepting a payment rather than only setting up future use
- [[source-stripe-subscriptions-acss-debit]] — subscription-specific flow

## Related raw API references

- [[raw/stripe-payments-acss-debit-set-up-payment-2026-11-07|2026-11-07 ACSS setup variant index]] — navigation to Checkout, Elements, and Direct API; no captured variant implementation

## Raw Sources

- [[raw/stripe-acss-set-up-payment-2025|2026-05-02 ACSS setup guide]] — retained Checkout and Direct API bodies (830 lines)
