---
title: "ACSS Debit / Canadian Pre-Authorized Debit (Stripe)"
type: concept
category: technology
tags: [stripe, acss, acss-debit, canada, cad, bank-debit, mandates, pad, disputes]
---

## Definition

ACSS Debit (Canadian Pre-Authorized Debit / PAD) lets CA and US businesses pull funds from customers' Canadian bank accounts via the Automated Clearing Settlement System (ACSS). API enum: `acss_debit`. Business-initiated, delayed notification, reusable. Not guaranteed — disputes possible.

**Currency**: CAD (primary); USD supported but risky (cross-currency debits frequently fail with delayed error up to 5 days).

**Countries**: CA customers; CA and US business accounts.

## Settlement

| Settlement | Payment Success | Funds Available | Cutoff |
| --- | --- | --- | --- |
| Standard | T+4 at 21:00 UTC | T+5 at 00:00 UTC | 17:00 US/Eastern |

T+4 payment success and T+5 Stripe-balance availability count business days **after submission**, which may differ from creation; neither establishes a customer-bank receipt or a guaranteed final outcome. `expected_debit_date` on Charge `payment_method_details` is estimated, not guaranteed. A submitted or processing payment is not final: the November guide distinguishes `payment_intent.processing` and `checkout.session.completed` from the subsequent PaymentIntent or Checkout asynchronous success/failure events. See [[source-stripe-acss-debit]] (https://docs.stripe.com/payments/acss-debit; old raw/stripe-acss-debit-2025.md:111-121; new raw/stripe-payments-acss-debit-2026-11-07.md:266-276,302-311).

## Mandates (PAD Agreements)

Governed by Payments Canada Rule H1. Requires: institution number, transit number, account number, name, email. First debit initiated immediately after mandate acceptance. Mandate confirmation email must be sent ≤5 calendar days after acceptance.

Each mandate must specify:

- **Payment schedule**: `interval` (predictable, with `interval_description`) / `sporadic` (irregular, requires express per-payment authorization) / `combined`
- **Transaction type**: `personal` or `business`
- **`default_for`**: set to `['invoice', 'subscription']` to reuse for Invoicing/Subscriptions without a new mandate

Customers can cancel at any time (including oral notice). Cancellation invalidates future debits — must collect new mandate.

## Debit Notification Emails

Payments Canada requires:

1. Mandate confirmation (≤5 days after acceptance)
2. Debit-notification email each time a debit is made; for custom emails, use `charge.pending` as the trigger, without treating it as final debit success.

Stripe sends the notifications automatically. If sending custom notifications, support mandate confirmations, debit notifications, and applicable microdeposit reminders together; partial substitution is not supported. Mandate confirmation is due no later than five calendar days after acceptance and includes the mandate, institution/transit numbers, and account last four. A custom debit notice includes contact information, account last four, and the amount to be debited. The captures do not establish a universal before-each-charge delivery deadline for the debit email. See [[source-stripe-acss-debit]] (https://docs.stripe.com/payments/acss-debit; old raw/stripe-acss-debit-2025.md:168-188; new raw/stripe-payments-acss-debit-2026-11-07.md:179-198).

## Disputes

- **Personal accounts**: up to 90 calendar days, "no questions asked"
- **Business accounts**: up to 10 business days
- **Bank-final PAD disputes** — no evidence submission or appeal; `charge.dispute.created` is sent when the customer files and `charge.dispute.closed` when the dispute closes. The older capture grouped both events at creation but did not prove simultaneous delivery. See [[source-stripe-acss-debit]] (https://docs.stripe.com/payments/acss-debit; old raw/stripe-acss-debit-2025.md:190-196; new raw/stripe-payments-acss-debit-2026-11-07.md:107-127).
- Dispute fee charged by Stripe
- Risk of double-credit if refund issued while customer also disputes

## Transaction Failures

Payments can fail post-confirmation (insufficient funds, invalid account, debits disabled by customer). If PaymentIntent already `succeeded`, failure creates a dispute with reason:

- `insufficient_funds`
- `incorrect_account_details`
- `bank_cannot_process`

Stripe charges a failure fee in this situation.

## Refunds

- Max 180 days from original payment
- ~3 business days to process
- Full and partial refunds supported
- Labeled as credit (not refund) on customer bank statement

## Statement Descriptors

Truncated to 15 alphanumeric chars. Dynamic override via `statement_descriptor` on PaymentIntent. Connect `on_behalf_of` causes descriptor to come from connected account.

## Product Support

- Connect, Checkout, Subscriptions, Invoicing. The 2026-05-02 [[source-stripe-acss-accept-payment]] guide described Checkout subscription mode as unsupported at that date; the 2026-11-07 base-URL index does not establish its current status.
- Elements: the retained payment-integration evidence describes a PaymentIntent path and excludes Checkout Sessions API, Express Checkout Element, and Mobile Payment Element. The 2026-11-07 ACSS setup index also links an Elements variant, but that variant body was not captured here; the link alone neither verifies a SetupIntent implementation nor overturns the earlier path-specific limits.

## Integration

**Checkout (2026-05-02 guide)**: Explicit `payment_method_types: ['acss_debit']` is used for manual method configuration; Dashboard-managed dynamic methods can omit that field, but `payment_method_options` and mandate options remain required (`payment_schedule`, `transaction_type`; `interval_description` for `interval`/`combined`). Optional `verification_method: 'instant'` or `'microdeposits'`; optional best-effort `target_date` (3–15 days, incompatible with `microdeposits`). See [[source-stripe-acss-accept-payment]].

**Direct API**: Create PaymentIntent → pass `client_secret` to client → `stripe.confirmAcssDebitPayment` opens on-page modal for bank collection + verification + mandate. Returns `processing` when the bank account was instantly verified **or verification was unnecessary**; this is submitted/processing, not final payment success. `requires_action` calls for additional verification, such as microdeposits. Fulfill only after the later success outcome; see [[source-stripe-acss-accept-payment]] (2026-05-02 guide).

**Microdeposit verification**: 2 deposits (1–2 days, `ACCTVERIFY` descriptor); hosted page via `next_action.verify_with_microdeposits.hosted_verification_url`; or custom: `stripe.verifyMicrodepositsForPayment(clientSecret, { amounts: [32, 45] })`. 3-attempt limit, 10-day timeout → `requires_payment_method`.

## Billing Retries

The May 2, 2026 guide labeled Billing Retries a private preview. The November 7, 2026 guide omits that phase label and describes optional automatic Direct Debit retries for failed PAD payments caused by insufficient funds: at most one retry within 30 days of the original attempt, without a debit failure fee for a Stripe-initiated automatic retry. The omission does not establish general availability or account enablement. See [[source-stripe-acss-debit]] (https://docs.stripe.com/payments/acss-debit; old raw/stripe-acss-debit-2025.md:269-271; new raw/stripe-payments-acss-debit-2026-11-07.md:258-264).

## ACSS Subscriptions

**Checkout subscription mode not yet supported** in the 2026-11-07 guide (waitlist). With Direct Debit retries enabled, Stripe can automatically retry Canadian PAD subscription payments that fail for insufficient funds; availability or enablement for a particular account is unverified.

> [!warning] Contradiction
> The 2026-05-13 subscription guide said Canadian PAD payments were never automatically retried. The 2026-11-07 guide documents this conditional insufficient-funds retry path; see [[source-stripe-subscriptions-acss-debit]].

Create with `payment_behavior=default_incomplete`; the 2026-05-13 Node.js example explicitly sets `payment_method_types=['acss_debit']`, while the 2026-11-07 curl sample omits that field. Client uses `stripe.confirmAcssDebitPayment` to collect bank details and mandate acknowledgment in an on-page modal. Later charges need no new mandate acknowledgment, but payment success must still be checked.

**Fulfillment:** before supplying goods or services, verify the related subscription is `active` and either `invoice.paid` occurred or the underlying PaymentIntent is `succeeded`; `active` alone can precede first-payment completion. **Future default PM in the paid initial-invoice flow:** separately, after `invoice.payment_succeeded` for a new subscription (`billing_reason=subscription_create`), set `subscription.default_payment_method` from the paid invoice's method. For the trial `pending_setup_intent` path, successful verification automatically sets the subscription default.

**Trial period**: returns `pending_setup_intent`; use `confirmAcssDebitSetup` / `verifyMicrodepositsForSetup`. SetupIntent `succeeded` → auto-sets `default_payment_method`.

**Save for future use**: SetupIntent with `mandate_options.default_for=['invoice','subscription']`.

## Sources

- [[source-stripe-acss-debit]] — May/November 2026 Canadian PAD overview: conditional eligibility/limits, settlement and delayed outcomes, mandates/notices, bank-final disputes, refunds, Connect, and dated retry guidance
- [[source-stripe-acss-accept-payment]] — integration guide: Checkout + Direct API paths, verification options, microdeposit flow, 6 test tokens, 7 test accounts
- [[source-stripe-acss-set-up-payment]] — retained 2026-05-02 Checkout setup and Direct API SetupIntent guide, including off-session mandate reuse; the 2026-11-07 canonical capture only indexes Checkout, Elements, and Direct API variants, without establishing the Elements implementation.
- [[source-stripe-acss-custom-pad-agreement]] — custom PAD mandate guide: 11 requirement rows, including two conditional `payment_schedule` rows; pre-debit notice is required unless expressly waived, with waiver text bolded, highlighted, or underlined; full exact recourse text required. The thirty-day cancellation notice in the table is sample wording, not a universal term.
- [[source-stripe-subscriptions-acss-debit]] — Canadian PAD subscription guide (2026-05-13 and 2026-11-07 captures): conditional insufficient-funds retries, payment-confirmed fulfillment, default-PM webhook, and microdeposit/trial flows
