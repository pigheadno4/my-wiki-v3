---
title: "Stripe: Accept a Canadian Pre-Authorized Debit Payment (ACSS)"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/acss-debit/accept-a-payment"
raw_files:
  - "stripe-acss-accept-payment-2025.md"
tags: [stripe, acss, acss-debit, canada, cad, usd, checkout, payment-intents, mandates, microdeposits, verification]
---

## Summary

The 2026-05-02 guide covers Canadian pre-authorized debit (PAD/ACSS Debit) through Checkout and a Direct API PaymentIntent flow, including mandate options, bank verification, delayed payment status, testing, and target debit dates. The 2026-11-07 capture at the same base URL is a 14-line index to separate Checkout and Direct API variants; it contains no detailed flow text. This navigation change is not evidence that the older instructions were deprecated or still describe current variant behavior. The details below are attributed to the May guide; current variant contents require separate capture.

## Checkout path in the 2026-05-02 guide

The Checkout compatibility section lists Canadian customer geography, CAD and USD supported/presentment currencies, and payment and setup modes. It says a Session's one-time line-item Prices must all use the **same** currency, either `cad` or `usd`; the guide marks Checkout subscription mode as not yet supported at this date. Its presentment discussion warns a CAD account may fail a USD debit or vice versa, often after a delay, so CAD is safest unless the customer's account can accept USD debits. The later setup step says all line items use `cad`, in tension with the broader compatibility and presentment text. Treat that step as CAD-oriented setup guidance, not proof that USD is universally unsupported.

The guide's explicit `payment_method_types: ['acss_debit']` is a manual configuration example. When payment methods are managed in the Dashboard, default dynamic payment methods allow omitting `payment_method_types` from the Checkout Session; **`payment_method_options` remains necessary**. For the PAD mandate, `payment_method_options.acss_debit.mandate_options.payment_schedule` and `transaction_type` are required; `interval_description` is required when schedule is `interval` or `combined`. The schedule values are `interval`, `sporadic`, and `combined`; transaction type is `personal` or `business`. The historical examples show both a Stripe-hosted page and an embedded page. During Checkout, the modal collects bank details, verification and mandate acknowledgement; a microdeposit fallback can defer processing.

## Direct API path in the 2026-05-02 guide

The server creates or retrieves a customer object and creates a PaymentIntent with amount, currency and PAD mandate options. The examples use `currency: 'cad'`, while the prose says currency is **usually** CAD; the example is not a universal CAD-only requirement. `setup_future_usage: 'off_session'` is optional when reuse is intended. The guide separates customer-configured Accounts v2 from Customers v1 examples: it describes Accounts v2 as generally available for Connect users and public preview for others, with a preview API version for preview participants. That is a dated availability statement, not current eligibility. The PaymentIntent's client secret is passed to the client, not the whole Intent or the server API key.

On the client, `stripe.confirmAcssDebitPayment(clientSecret, { payment_method: { billing_details: { name, email } } })` opens a modal for bank collection, verification and PAD mandate authorization. Account holder name and customer email are required billing details for this method. The `processing` status means the bank account was instantly verified **or verification was unnecessary**, and the payment has been submitted for processing. `requires_action` means further bank verification is needed. Neither status itself confirms a successful debit.

## Verification, payment outcome, and target date

The default historical flow offers instant verification or microdeposits, with instant-only and microdeposit-only options. When microdeposits are used, two deposits with `ACCTVERIFY` in the statement descriptor can take one to two business days to appear. The customer can use the Stripe-hosted verification URL in `next_action.verify_with_microdeposits.hosted_verification_url`, or a custom form with `stripe.verifyMicrodepositsForPayment`. Three failed attempts or a ten-day timeout can prevent verification; the Intent then requires new payment-method details. The direct flow's error table distinguishes a mismatched amount with unchanged status from failed send, exceeded attempts or timeout that lead to `requires_payment_method` and `last_payment_error`.

PAD is delayed notification: the May guide says success or failure notice can take up to five business days after initiating the debit, and a payment typically takes five business days to arrive. A `payment_intent.processing` webhook says the payment was submitted, so wait. `payment_intent.succeeded` reports success and is the guide's fulfillment point; `payment_intent.payment_failed` covers declined payments or failed microdeposit verification. Webhooks should confirm the final outcome before fulfillment.

Both variants describe optional `target_date` as three to 15 days from the current date, incompatible with `verification_method: 'microdeposits'`. It is best effort: a weekend, bank holiday, other non-business day, or fewer than three business days' lead time can move the debit to the next available business day, and the customer's bank may process on another date. The Direct API variant also says a PaymentIntent with a target date can be canceled up to three business days before that date; this is historical guide text, not a tested outcome.

## Sandbox fixtures and related conditions

The historical guide has six test payment-method tokens, seven test account numbers with institution `000` and transit `11000`, and microdeposit amounts: `32` plus `45` verifies; `10` plus `11` simulates too many attempts; other combinations fail verification. The `pm_acssDebit_success` token is described as succeeding immediately **in the test scenario** and is not a live settlement promise. The sandbox microdeposit-email address pattern is `{any_prefix}+test_email@{any_domain}`. Full scenarios and status distinctions remain in the raw.

The May Checkout section also describes a refund period up to 180 days and a bank-dispute window up to 90 calendar days without an appeals process. Those are historical guide statements; consult the primary [[source-stripe-acss-debit]] route for the broader PAD context rather than inferring current dispute rules from the November index.

## Detail locators

- [[raw/stripe-acss-accept-payment-2025|2026-05-02 detailed guide]], Checkout lines 8–394: currency and internal CAD wording tension 20–58; mandate options 61–67; hosted and embedded examples 69–142; sandbox fixtures 148–195; verification and target date 207–386.
- Same guide, Direct API lines 395–940: Accounts v2/Customers v1 boundaries 416–459; PaymentIntent mandate fields 462–528; client collection 601–670; microdeposit actions and error states 688–752; payment outcome and webhooks 754–768; sandbox fixtures 770–809; instant/microdeposit-only examples and target date 811–936.

## Related Pages

- [[stripe-acss-debit]] — PAD concept and payment-state context.
- [[source-stripe-acss-debit]] — primary PAD source.
- [[stripe]] — provider.

## Related raw API references

- [[raw/stripe-payments-acss-debit-accept-a-payment-2026-11-07|2026-11-07 base-URL variant index]] — Checkout and Direct API links at lines 9–14; their bodies were not captured in this unit.

## Raw Sources

- [[raw/stripe-acss-accept-payment-2025|ACSS acceptance guide, captured 2026-05-02]] — historical Checkout and Direct API detail.
