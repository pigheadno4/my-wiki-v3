---
title: "Bacs Direct Debit (Stripe)"
type: concept
category: technology
tags: [stripe, bacs, bank-debit, uk, gbp, mandates, disputes]
---

## Definition

Bacs Direct Debit lets businesses in the November 2026 supported-location list debit customers' UK bank accounts in GBP under a Direct Debit Instruction mandate. API enum: `bacs_debit`. It is reusable and delayed; disputes are final and cannot be countered or appealed. The May guide described UK Stripe businesses and an outside-UK platform path for UK connected accounts; see [[source-stripe-bacs-direct-debit]] for the dated change.

**Currency/customer**: GBP presentment and GB bank-account customers. **Merchant location**: May listed UK Stripe accounts plus outside-UK platforms for UK connected accounts; November lists additional supported merchant countries and cross-border coverage, subject to approval, identity verification and account/MCC conditions.

## Limits

- Per transaction: November default **10,000 GBP**; May said **100,000 GBP** (dated conflict). Contact support for higher limits.
- New users: separate **10,000 GBP weekly** limit, which increases as they process more Bacs payments.

## Settlement

| Scenario | Payment Success | Funds Available | Cutoff |
| --- | --- | --- | --- |
| Existing mandate | T+3 at 21:00 UTC | T+4 at 00:00 UTC | 20:00 Europe/London |
| New mandate | — | T+7 | — |

New mandate timeline: T+0 mandate submitted → T+3 mandate active + payment submitted → T+5 funds leave customer bank → T+7 funds in Stripe.

`expected_debit_date` available on `payment_method_details` for Charges (estimated, not guaranteed).

## Mandates (DDI)

Required before any debit. Called a Direct Debit Instruction (DDI). Requires: sort code, account number, name, email, full address.

Customers can cancel at any time via merchant or their bank. Cancellation invalidates all future debits on that mandate — must collect a new mandate to continue.

Mandate events:

| Event | Trigger | Still usable? |
| --- | --- | --- |
| `mandate.updated` | Rejected, canceled, or reactivated by Bacs network | Yes, if new status is `active` |
| `payment_method.automatically_updated` | Customer's bank account details changed | Yes |

## Debit Notifications

Bacs requires notice when bank details are collected/confirmed and before each debit. May said Stripe emailed by default; November excepts enterprise accounts with a custom service user number (SUN) from Stripe's default sending. Sending your own notices requires eligibility and approval. These mandate/advance-debit notices are not payment-success receipts; the SUN exception does not remove the notice duty.

## Disputes

- **Unlimited** dispute window (no time limit)
- **Final and uncontestable** — must resolve directly with customer
- If customer disputes after refund, lose both the disputed amount and the refund separately

## Refunds

- Max 180 days from original payment
- 3–4 business days to process
- Full or partial refunds supported
- Refunds are outside the Bacs scheme (provided by Stripe)

## Connect

- November: supported-location platforms can use destination charges with or without `on_behalf_of`, but must first enable Bacs Direct Debit on the platform before accepting payments. Omitting `on_behalf_of` makes the platform settlement merchant; with it, the supported-location connected account additionally needs `bacs_debit_payments` capability. Platform enablement and connected-account capability do not by themselves establish account approval or identity verification.
- May: UK-platform destination charges for UK connected accounts were described as capability-exempt, while outside-UK platforms needed it; keep this as dated and scope-specific.
- `settings.bacs_debit_payments.display_name` enables Custom Branding on the connected account.

## Custom Branding

- 50 GBP/month per active account
- May said the name appears on new mandates five business days after request; November says Custom Branding typically activates in ten business days and appears on mandates created after activation. A request is not proof of activation.
- Set via `settings.bacs_debit_payments.display_name` on capability request or account update
- Without display_name: defaults to Stripe branding
- Unused accounts revert to Stripe branding automatically

## Product Support

- Connect, Checkout, Payment Links, Subscriptions, Invoicing, Elements
- **Payment Element**: cannot create SetupIntents for Bacs — use Checkout setup mode instead
- **Express Checkout Element**: not supported

## Integration

**Checkout (May 2, 2026 guide)**: A manually configured payment-mode Session example selects `payment_method_types: ['bacs_debit']`; `payment_intent_data.setup_future_usage: 'off_session'` is in its optional save-for-later example. Handle `checkout.session.completed` as debit authorization, then `checkout.session.async_payment_succeeded` for later payment success and fulfillment or `checkout.session.async_payment_failed` for follow-up. A `success_url` redirect does not prove payment success.

**Elements**: Create Customer → Payment Element (collects mandate automatically) → PaymentIntent → `stripe.confirmPayment`. Handle `payment_intent.succeeded` / `payment_intent.processing` / `payment_intent.payment_failed`.

**Optional target_date**: `payment_method_options.bacs_debit.target_date` on Checkout Session — 3–15 days out, best-effort, delayed to next business day if weekend/holiday.

**Mandate reference prefix**: `payment_method_options.bacs_debit.mandate_options.reference_prefix` on PaymentIntent/SetupIntent/Checkout — 12 chars max, uppercase/numbers/spaces/`./_/-/&`, cannot start with `DDIC` or `STRIPE`.

## Failure Codes

| Code | Retryable |
| --- | --- |
| `account_closed` | No |
| `bank_ownership_changed` | No |
| `debit_not_authorized` | No |
| `invalid_account_number` | No |
| `generic_could_not_process` | Yes |
| `insufficient_funds` | Yes |

## Billing Retries

May labeled Direct Debit retries private preview. November omits that label and describes insufficient-funds retries for subscription and/or one-off invoices: up to two automatic retries within 30 days of the original attempt, with no debit-failure fee for Stripe-initiated retries. The capture does not prove account-specific availability.

## Bacs subscriptions: Checkout guide

The 2026-05-13 and 2026-11-07 Bacs subscription guide documents a Checkout path with `mode='subscription'` and at least one recurring Price. Its May Node.js examples explicitly select `bacs_debit`; November curl examples omit that field and direct Dashboard payment-method configuration. This guide alone does not resolve other subscription UI paths or account eligibility.

**Delayed notification** — `checkout.session.completed` records debit authorization, not payment success. Before fulfillment, verify the related subscription is `active` and wait for `invoice.paid` or a `succeeded` underlying PaymentIntent; `active` alone can precede the first payment. `checkout.session.async_payment_succeeded` reports later payment success, not immediate funds availability. Bacs notification emails are not sent in sandboxes.

**Delayed test accounts recommended** (three-minute processing) to better simulate live behavior. The sandbox table includes immediate success, delayed success and failure, and a success followed immediately by dispute; these are test outcomes, not settlement evidence.

**Test account mandate behavior**: `debitNotAuthorized` failures → mandate `inactive` (PM cannot be reused); `insufficientFunds` failures → mandate stays `active` (PM can be retried).

## Sources

- [[source-stripe-bacs-direct-debit]] — 2026-05-02 and 2026-11-07 Bacs overview: dated merchant scope and limits, DDI mandate/notice conditions, delayed outcomes, refunds/disputes, Connect, branding and retries
- [[source-stripe-bacs-accept-payment]] — May 2, 2026 full Checkout and web Elements Bacs payment guide, including delayed payment states, sandbox cases, optional target dates, and mandate prefix rules; November 7 capture is a Checkout/Elements variant index for navigation only.
- [[source-stripe-subscriptions-bacs-debit]] — Bacs subscription Checkout guide (2026-05-13 and 2026-11-07): delayed fulfillment, sandbox-copy change, nine test accounts, and deprecated dynamic tax-rate field
