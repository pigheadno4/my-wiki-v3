---
title: "ACH Direct Debit"
type: concept
category: technology
tags: [stripe, ach, bank-debit, us-bank-account, mandates, disputes, financial-connections]
---

## Definition

ACH Direct Debit lets US businesses pull funds from customers' US bank accounts. API enum: `us_bank_account`. Business-initiated, delayed notification, reusable. Not guaranteed — disputes and payment failures possible.

**Currency**: USD only. **Country**: US customers; 33+ business countries.

## Settlement

| Type | Timing | Cutoff |
| --- | --- | --- |
| Standard (T+4) | 4 business days | 21:00 ET |
| Faster (T+2) | 2 business days | 14:00 ET (eligible US users only) |

## Mandates

Required before any debit. Two types:

- **Online**: embedded in checkout UI (Stripe-hosted flows handle automatically)
- **Offline**: written/verbal authorization for custom flows

Custom payment forms must display mandate text. Stripe emails mandate confirmation + microdeposit notification to customer's billing email.

## Verification

- **Financial Connections** (instant): customer logs into bank
- **Microdeposits** (delayed): 10-day window to verify; reverts to new payment method if not completed

## Disputes

- **Personal accounts**: up to 60 calendar days
- **Business accounts**: up to 2 business days
- **Final and uncontestable** through ACH network — resolve directly with customer
- First dispute: mandate invalidated (must collect new mandate)
- Second dispute: bank account blocked entirely

**Proof of Authorization inquiry**: upload evidence via Dashboard or Files API; `charge.dispute.created` with `warning_needs_response` status.

## Blocked Accounts

Stripe blocks accounts on certain ACH returns. Listen for `payment_method.automatically_updated` event; check `us_bank_account.status_details.blocked`. Block removed event signals account is usable again.

## Refunds

- Max 180 days from original payment
- Min 3 business days to process
- Appears as credit on bank statement (not labeled "refund")

## Statement Descriptor

Truncated to first 16 alphanumeric chars; no `<>'"`. Dynamic override via `statement_descriptor` on PaymentIntent.

## Connect

Requires `us_bank_account_ach_payments` capability. PaymentMethod cloning supported (duplicates mandate authorization). Charge type determines merchant of record on mandate/emails.

## ACH Subscriptions

Create with `payment_behavior=default_incomplete` + `payment_settings.payment_method_types=['us_bank_account']`. Expand `latest_invoice.confirmation_secret` — use `confirmation_secret.client_secret` on client.

**Microdeposit window**: customers have **10 days** to verify (vs 23h normal `incomplete_expired`), but not past the billing cycle date.

**Default PM must be set manually**: after `invoice.payment_succeeded` with `billing_reason=subscription_create`, update `subscription.default_payment_method` via webhook — not set automatically.

**Trial period**: returns `pending_setup_intent`. Use Setup variants (`collectBankAccountForSetup`, `confirmUsBankAccountSetup`). SetupIntent `succeeded` → automatically sets subscription `default_payment_method`.

## Billing Retries

Max 2 retries; within 40 days of original payment. For recurring subscriptions or one-off invoices.

## Nacha Compliance (effective 2026-03-20)

Nacha requires `PURCHASE` in the Company Entry Description for e-commerce ACH debits (WEB or TEL SEC code, consumer, physical/digital goods). Excludes services, donations, and bill payments.

**Configure via Dashboard** (global): Settings > Payment methods > ACH Direct Debit > ACH classification → auto / all goods / none.

**Configure via API** (per-transaction): `payment_method_options.us_bank_account.transaction_purpose` on PaymentIntent:

- `goods` — adds `PURCHASE` label
- `services` / `other` — no label
- Omitted — falls back to Dashboard setting, then auto-classify

Connect: platform Dashboard setting covers direct charges + destination charges + separate charges without `on_behalf_of`. Connected accounts configured separately.

## SEC Codes

Standard Entry Class (SEC) codes define how a customer authorized the transaction. Stripe defaults to WEB (consumers) and CCD (businesses).

| Code | Name | Use case |
| --- | --- | --- |
| WEB | Internet/Mobile Initiated | Consumer, internet or mobile; refunds use PPD |
| CCD | Corporate Credit or Debit | All `account_holder_type=company` PaymentMethods |
| PPD | Prearranged Payment and Deposit | Written/signed consumer authorization; requires `collection_method: 'paper'` |
| TEL | Telephone-Initiated | Oral authorization over phone; private beta; single entries only |

PPD requires `mandate_data.customer_acceptance.type: 'offline'` + `payment_method_options.us_bank_account.mandate_options.collection_method: 'paper'`. TEL requires an existing customer relationship and captured oral authorization (recording or prior written notice).

## vs Instant Bank Payments

| | ACH Direct Debit | Instant Bank Payments |
| --- | --- | --- |
| Confirmation | Up to 4 business days | Instant |
| Failure protection | Financial Connections data | Bank-initiated returns guaranteed by Stripe |
| Cost | Lower | Higher |
| Best for | Large/recurring B2B | Instant confirmation needed |

## Sources

- [[source-stripe-ach-direct-debit]] — primary source: settlement, mandates, disputes, verification, refunds, Connect, testing
- [[source-stripe-ach-accept-payment]] — integration guide: Checkout/Elements/PaymentIntents, verification options, Financial Connections, payment reference, target debit date
- [[source-stripe-ach-set-up-payment]] — save for future: Checkout setup mode + SetupIntents API, Financial Connections, microdeposit verification, balance check
- [[source-stripe-ach-migration]] — legacy migration: T+6→T+4, balance type change, mandate enforcement, microdeposit change, webhook mapping
- [[source-stripe-ach-migrate-bank-accounts]] — migrate existing bank accounts: mandate creation, BankAccount as PaymentMethod, Checkout saved accounts, Invoices/Subscriptions
- [[source-stripe-subscriptions-ach-debit]] — ACH subscription setup: 10-day microdeposit window, default PM webhook required, trial flow via SetupIntent, Checkout delayed notification events, test account table
- [[source-stripe-ach-migrate-from-processor]] — migrate from another processor: Stripe-managed vs self-service, verification_method skip, raw bank details SetupIntent
- [[source-stripe-ach-sec-codes]] — SEC codes: WEB/CCD/PPD/TEL definitions, defaults, PPD paper mandate integration, TEL beta requirements
- [[source-stripe-ach-nacha-compliance]] — Nacha compliance (2026-03-20): PURCHASE label requirement, transaction_purpose API field, Dashboard classification setting
