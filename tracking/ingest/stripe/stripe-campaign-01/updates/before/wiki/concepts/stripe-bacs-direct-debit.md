---
title: "Bacs Direct Debit (Stripe)"
type: concept
category: technology
tags: [stripe, bacs, bank-debit, uk, gbp, mandates, disputes]
---

## Definition

Bacs Direct Debit lets UK businesses pull funds from customers' UK bank accounts. API enum: `bacs_debit`. Business-initiated, delayed notification, reusable. Disputes are final and uncontestable.

**Currency**: GBP only. **Country**: UK customers; UK business accounts only (platforms outside UK can initiate on behalf of UK connected accounts).

## Limits

- Per transaction: 100,000 GBP
- New users: 10,000 GBP weekly (increases as you process more)

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

Stripe auto-emails customers when mandate is created and before each debit. Custom email templates require approval from Stripe.

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

- `bacs_debit_payments` capability required for `on_behalf_of`
- UK platforms don't need capability for destination charges
- `settings.bacs_debit_payments.display_name` enables Custom Branding

## Custom Branding

- 50 GBP/month per active account
- Business name appears on new mandates 5 business days after request
- Set via `settings.bacs_debit_payments.display_name` on capability request or account update
- Without display_name: defaults to Stripe branding
- Unused accounts revert to Stripe branding automatically

## Product Support

- Connect, Checkout, Payment Links, Subscriptions, Invoicing, Elements
- **Payment Element**: cannot create SetupIntents for Bacs — use Checkout setup mode instead
- **Express Checkout Element**: not supported

## Integration

**Checkout**: `payment_method_types: ['bacs_debit']`, `mode: 'payment'` + `setup_future_usage: 'off_session'`. Handle 3 async events: `checkout.session.completed` → `checkout.session.async_payment_succeeded` (fulfill) / `checkout.session.async_payment_failed` (retry).

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

Private preview. Automatic retry of failed payments caused by insufficient funds. Works for subscription invoices and one-off invoices.

## Bacs Subscriptions (Checkout only)

Bacs subscriptions use Checkout (`payment_method_types: ['bacs_debit']`, `mode='subscription'`). No custom Elements path.

**Delayed notification** — do NOT fulfill on `checkout.session.completed` alone. Wait for `checkout.session.async_payment_succeeded` or `invoice.paid`. Bacs notification emails are NOT sent in sandboxes.

**Delayed test accounts recommended** (3-min processing) to simulate live behavior; instant accounts settle immediately in sandbox.

**Test account mandate behavior**: `debitNotAuthorized` failures → mandate `inactive` (PM cannot be reused); `insufficientFunds` failures → mandate stays `active` (PM can be retried).

## Sources

- [[source-stripe-bacs-direct-debit]] — primary source: settlement, mandates, disputes, refunds, Connect, Custom Branding
- [[source-stripe-bacs-accept-payment]] — integration guide: Checkout + Elements paths, 11 test accounts, 6 failure codes, target_date, mandate reference prefix
- [[source-stripe-subscriptions-bacs-debit]] — Bacs subscription: Checkout-only, delayed notification events, 9 test accounts, inline pricing, trials, tax rates
