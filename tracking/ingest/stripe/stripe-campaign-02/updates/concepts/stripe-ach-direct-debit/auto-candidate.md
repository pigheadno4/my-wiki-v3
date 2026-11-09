---
title: "ACH Direct Debit"
type: concept
category: technology
tags: [stripe, ach, bank-debit, us-bank-account, mandates, disputes, financial-connections]
---

## Definition

ACH Direct Debit lets eligible businesses in the documented US and European locations pull funds from customers' US bank accounts, with Canada labeled private preview in the 2026-11-07 capture. API enum: `us_bank_account`. USD presentment, delayed notification, reusable, and not guaranteed — disputes and payment failures remain possible. Account and industry eligibility require separate confirmation.

**Presentment currency**: USD. **Settlement**: the 2026-11-07 capture lists local-currency settlement for eligible merchant Stripe accounts. **Customer location**: US; business locations include the listed European countries and US, with Canada in private preview.

## Settlement

| Type | Timing | Cutoff |
| --- | --- | --- |
| Standard (T+4) | 4 business days | 21:00 ET |
| Faster (T+2) | 2 business days | 14:00 ET (eligible US users only) |

## Mandates

Required before any debit. Two types:

- **Online**: embedded in checkout UI (Stripe-hosted flows handle automatically)
- **Offline**: written/verbal authorization for custom flows

Custom Payment Intents forms must display mandate terms before confirmation. Nacha requires an electronic or hard copy of the mandate. With a billing email, Stripe defaults to sending mandate confirmation and, if microdeposit verification is needed, its verification notification. Custom notification flows also require microdeposit reminders.

## Verification

- **Financial Connections** (instant): customer logs into bank
- **Microdeposits** (delayed): 10-day window to verify; reverts to new payment method if not completed

## Financial Connections Pre-Collected Consent (Stripe.js 9.17.0)

`@stripe/stripe-js@9.17.0` adds optional `preCollectedConsent` to `collectBankAccountForPayment`, `collectBankAccountForSetup`, `collectFinancialConnectionsAccounts`, and `collectBankAccountToken`. Its required fields are `consent` (the server-returned Financial Connections consent object ID) and `collectedAt` (Unix seconds when the customer affirmatively accepted the complete consent text).

This requires beta access and server-side eligibility/validation. Supplying it does not guarantee omission of Stripe's consent pane. It is not a general `confirmPayment` option, proof of an ACH debit mandate, or a replacement for payment/setup confirmation. The package adds declarations, not the hosted Stripe.js implementation. Source: [[source-github-stripe-js]].

## Disputes

- **Personal accounts**: up to 60 calendar days
- **Business accounts**: up to 2 business days
- **Final and uncontestable** through ACH network — resolve directly with customer
- First dispute: mandate invalidated (must collect new mandate)
- Second dispute: bank account blocked entirely

**Proof of Authorization inquiry**: when Stripe requests proof before the bank decides a late return, `charge.dispute.created` can carry `warning_needs_response`; submit authorization evidence only on request and only once via Dashboard or Files API. This inquiry is not an appeal of a final ACH dispute.

## Blocked Accounts

Stripe can block bank accounts on certain ACH returns. Listen for `payment_method.automatically_updated` and inspect `us_bank_account.status_details.blocked`. When Stripe removes a block, the payment method can be reused only if an active mandate exists or a new one is collected.

## Refunds

- Max 180 days from original payment
- 2026-11-07 capture: asynchronous full refunds, up to 3 business days to complete; partial refunds marked unsupported. The 2026-05-02 capture instead listed partial refunds supported and at least 3 business days to process.

> [!warning] Contradiction
> The two dated ACH captures disagree on partial-refund support and the direction of the three-business-day timing. Neither establishes an effective change date or behavior for a specific historical payment; verify the account and payment before promising either.
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

Standard Entry Class (SEC) codes define how a customer authorized the transaction. **When no mandate collection method is specified**, the captured Stripe guide says WEB is the default for consumer bank accounts and CCD for business bank accounts.

| Code | Name | Use case |
| --- | --- | --- |
| WEB | Internet/Mobile Initiated | Consumer, internet or mobile; refunds use PPD |
| CCD | Corporate Credit or Debit | All `account_holder_type=company` PaymentMethods |
| PPD | Prearranged Payment and Deposit | Standing or single-entry consumer authorization in writing, signed **or otherwise authenticated**; provide a copy to the customer; the captured PPD mandate flow uses `collection_method: 'paper'` |
| TEL | Telephone-Initiated | Oral authorization over phone; November 7, 2026 capture labels private preview; single entries only, no standing or recurring TEL entries |

PPD requires offline customer acceptance and `payment_method_options.us_bank_account.mandate_options.collection_method: 'paper'` in the captured examples. For TEL, the November guide permits either a qualifying direct existing merchant-customer relationship **or**, without one, a customer-initiated telephone call; an affiliate-only relationship does not qualify. It also requires commercially reasonable identity and routing-number verification and explicit oral authorization containing online-mandate information and a customer inquiry number. Capture that authorization through an audio recording (subject to applicable recording law) or written notice **before the first debit**; the guide's sample wording is not prescribed verbatim. See [[source-stripe-ach-sec-codes]].

> [!warning] Contradiction: the previous concept said TEL was private beta and universally required an existing relationship. The November 7, 2026 capture labels it private preview and includes the customer-initiated-call alternative. Neither capture proves access for a particular account.

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
- [[source-stripe-ach-set-up-payment]] — save for future: dated 2026-05-02 Checkout setup mode, Elements and iOS/Android/React Native SetupIntent variants, Financial Connections and microdeposit verification; 2026-11-07 base URL is a five-route navigation index, with variant instructions not fetched
- [[source-stripe-ach-migration]] — dated legacy-to-Payment Intents/Checkout migration: T+6 versus T+4 (conditional T+2), active mandates, conditional balance-type updates, rare two-microdeposit fallback, and branch-specific webhook matrix; payout descriptors might differ
- [[source-stripe-ach-migrate-bank-accounts]] — 2026-05-02 full legacy BankAccount migration guide: verified-account prerequisites differ for Checkout and Payment Intents, with active mandate for the latter and mandate acknowledgment before Invoicing/Subscriptions defaults; 2026-11-07 base URL is a two-variant index
- [[source-stripe-subscriptions-ach-debit]] — ACH subscription setup: 10-day microdeposit window, default PM webhook required, trial flow via SetupIntent, Checkout delayed notification events, test account table
- [[source-stripe-ach-migrate-from-processor]] — migrate from another processor: Stripe-managed vs self-service, verification_method skip, raw bank details SetupIntent
- [[source-stripe-ach-sec-codes]] — SEC codes: WEB/CCD/PPD/TEL definitions, defaults, PPD paper mandate examples, and November 7 private-preview TEL conditions
- [[source-stripe-ach-nacha-compliance]] — Nacha compliance (2026-03-20): PURCHASE label requirement, transaction_purpose API field, Dashboard classification setting
