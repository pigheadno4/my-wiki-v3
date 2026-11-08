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

`expected_debit_date` available on `payment_method_details` for Charges (estimated, not guaranteed).

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
2. Pre-debit notice before each charge

Stripe sends these automatically. Can opt out for fully custom emails, but **all types must be supported** — partial custom is not allowed.

Custom custom emails must include: mandate text, institution/transit number, last 4 digits of account number. Pre-debit email triggered by `charge.pending` event.

## Disputes

- **Personal accounts**: up to 90 calendar days, "no questions asked"
- **Business accounts**: up to 10 business days
- **Final and uncontestable** — Stripe sends `charge.dispute.created` and `charge.dispute.closed` simultaneously
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

- Connect, Checkout (not subscription mode), Subscriptions, Invoicing
- Elements: PaymentIntent path only — not Checkout Sessions API, not Express Checkout Element, not Mobile Payment Element

## Integration

**Checkout**: `payment_method_types: ['acss_debit']`, mandate options required (`payment_schedule`, `transaction_type`; `interval_description` required for `interval`/`combined`). Optional `verification_method: 'instant'` or `'microdeposits'`. Optional `target_date` (3–15 days; incompatible with `microdeposits`).

**Direct API**: Create PaymentIntent → pass `client_secret` to client → `stripe.confirmAcssDebitPayment` opens on-page modal for bank collection + verification + mandate. Returns `processing` (verified) or `requires_action` (microdeposit pending).

**Microdeposit verification**: 2 deposits (1–2 days, `ACCTVERIFY` descriptor); hosted page via `next_action.verify_with_microdeposits.hosted_verification_url`; or custom: `stripe.verifyMicrodepositsForPayment(clientSecret, { amounts: [32, 45] })`. 3-attempt limit, 10-day timeout → `requires_payment_method`.

## Billing Retries

Private preview. Auto-retry for insufficient funds on subscription or one-off invoices.

## ACSS Subscriptions

**Checkout NOT supported** (waitlist only). **No auto-retry** — ACSS payments never retried.

Create with `payment_behavior=default_incomplete` + `payment_method_types=['acss_debit']`. Client uses `stripe.confirmAcssDebitPayment` — opens modal, collects bank + mandate acknowledgment. Customer acknowledges once; subsequent charges need no re-authorization.

**Default PM must be set manually** after `invoice.payment_succeeded` + `billing_reason=subscription_create`.

**Trial period**: returns `pending_setup_intent`; use `confirmAcssDebitSetup` / `verifyMicrodepositsForSetup`. SetupIntent `succeeded` → auto-sets `default_payment_method`.

**Save for future use**: SetupIntent with `mandate_options.default_for=['invoice','subscription']`.

## Sources

- [[source-stripe-acss-debit]] — primary source: settlement, mandates, payment schedules, disputes, refunds, statement descriptors, Connect
- [[source-stripe-acss-accept-payment]] — integration guide: Checkout + Direct API paths, verification options, microdeposit flow, 6 test tokens, 7 test accounts
- [[source-stripe-acss-set-up-payment]] — save for future: SetupIntent (Checkout setup mode + Direct API), off-session charging with mandate, reuse PM with new mandate
- [[source-stripe-acss-custom-pad-agreement]] — custom PAD mandate guide: 9 required elements, pre-notification waiver must be bold, exact recourse text, when/when-not-to-use
- [[source-stripe-subscriptions-acss-debit]] — ACSS subscription: Checkout NOT supported, no auto-retry, manual default PM webhook, 10-day microdeposit window, trial SetupIntent flow
