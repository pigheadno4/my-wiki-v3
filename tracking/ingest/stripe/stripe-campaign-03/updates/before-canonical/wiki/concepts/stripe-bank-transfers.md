---
title: "Bank Transfers (Stripe)"
type: concept
category: technology
tags: [stripe, bank-transfers, customer-balance, payments, ach, sepa, swift, wire]
---

## Definition

Stripe Bank Transfers is a push-payment method where customers send funds to a virtual bank account number that Stripe provides. Stripe uses this virtual account for reconciliation without exposing the merchant's real account details. Funds are held in a **customer cash balance** to handle overpayment and underpayment before being applied to invoices or payments.

## Key Properties

| Property | Value |
| --- | --- |
| Currencies | EUR, GBP, JPY, MXN, USD |
| Payment confirmation | No (push payment — not instant) |
| Recurring payments | Yes (requires customer action to fund) |
| Disputes | USD and CAD only |
| Manual capture | No |
| Refunds | Yes / Partial yes |
| API enum | `customer_balance` |
| Requires redirect | No |

## Business Locations

- **EUR or USD**: 34 countries (AT, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IT, LI, LT, LU, LV, MC, MT, NL, NO, PL, PT, RO, SE, SI, SK, SM, US)
- **GBP**: GB only
- **JPY**: JP only
- **MXN**: MX only

## Customer Balance Model

Unlike card payments, Stripe cannot control the amount a customer pushes. Funds land in the **customer cash balance**:

- Unreconciled funds auto-returned at **75 days**
- If Stripe can't determine bank account info by **90 days** → swept to merchant's Stripe balance
- EU EUR payments: beneficiary name must exactly match business name on Stripe to avoid screening delays

## Product Support

Supported: Connect, Checkout (non-subscription, non-setup modes), Payment Element, Subscriptions, Invoicing.
Unsupported: Payment Links, Express Checkout Element, Mobile Payment Element, Customer Portal, International transfers.

PaymentIntents only — no SetupIntents, no manual capture, no `setup_future_usage`.

## International and Domestic Wires

Available for US accounts only. SWIFT transfers settle in 3–5 business days. No refunds for international wires. US accounts accept SWIFT in USD only.

## Disputes

- **USD (ACH)**: reversible within 5 days of payment; merchant must provide evidence to remitting bank.
- **CAD (ACH)**: reversals always initiated by remitting bank; beneficiary bank must honor.
- All other currencies: **irreversible**.

## Sender Information API

`stripe.customers.retrieveCashBalanceTransaction(customerId, transactionId)` — returns `type: 'funded'` with region-specific sender details:

| Region | Fields |
| --- | --- |
| EU | `bic`, `iban_last4`, `sender_name`, `network` (sepa) |
| GB | `account_number_last4`, `sender_name`, `sort_code` |
| JP | `sender_bank`, `sender_branch`, `sender_name` |
| MX | `clabe_last4`, `sender_bank`, `sender_name` |
| US | `sender_name`, `network` (`ach` or `domestic_wire_us`) |

## Refunds

Four refund flows:

1. **Payment → customer bank**: Stripe emails customer for bank details; 45-day window; may incur fee; 180-day refund window from payment creation.
2. **Cancel pending refund**: `stripe.refunds.cancel({ refund: id })` — only while `requires_action`.
3. **Payment → customer cash balance**: immediate and free.
4. **Cash balance → customer bank**: `stripe.refunds.create({ origin: 'customer_balance', customer, amount, currency })`.

Refund status: `requires_action` → `pending` → `succeeded` / back to `requires_action` (bank rejection) → `failed` at 45 days (`refund.failed` event). Customer email required.

International (SWIFT) refunds: **not supported** — manual process required.

## Connect

All charge types supported. `on_behalf_of` not supported. Direct charges require the connected account to have activated the bank transfers capability.

## Virtual Bank Account Numbers (VBANs)

VBANs are **permanent** — once allocated to a customer they belong to them forever; any future funds go to their cash balance. Stripe reuses an existing VBAN if one matches the customer and country.

**Allocation triggers**: PaymentIntent with `customer_balance` PM, Invoice with `customer_balance` PM, or Funding Instructions API (proactive).

**Best practices**: only allocate VBANs to customers likely to pay; don't assign to inactive customers or in registration flows.

**Per-region limits**:

| Region | Daily | Lifetime | Fee beyond |
| --- | --- | --- | --- |
| US | 10,000 | — | — |
| UK | 5,000 | — | — |
| EU | 5,000 | 50,000 | Yes (>1,000 EU allocations) |
| JP | 1,000 | — | — |
| MX | 1,000 | — | — |

## Integration — PaymentIntents

**Create PaymentIntent** with `payment_method_types: ['customer_balance']`, `funding_type: 'bank_transfer'`, and region-specific `bank_transfer.type`:

| Region | `bank_transfer.type` | Notes |
| --- | --- | --- |
| US | `us_bank_transfer` | |
| UK | `gb_bank_transfer` | |
| EU | `eu_bank_transfer` + `country` | IBAN localized to customer's country; ES unavailable |
| JP | `jp_bank_transfer` | requires `return_url` |
| MX | `mx_bank_transfer` | requires `return_url` |

Or use `automatic_payment_methods: { enabled: true }`. If customer balance covers amount → immediate `succeeded`.

**Status lifecycle**: `requires_action` (balance insufficient) → `payment_intent.partially_funded` (partial received) → `payment_intent.succeeded`.

**Reconciliation**: automatic by default; override per customer: `cash_balance.settings.reconciliation_mode = 'manual'`.

**Testing**: `POST /v1/test_helpers/customers/{id}/fund_cash_balance` or `stripe test_helpers customers fund_cash_balance`.

## Checkout Constraints

Payment mode only (no subscription/setup mode). Single currency. One-time line items only. Customer must be specified in session. Delayed notification method.

## Subscription integration

Requires `collection_method='send_invoice'` and `payment_method_types=['customer_balance']`. Cash balance is central — every bank transfer subscription must have an associated Customer/Account. Set `days_until_due` for the payment window.

Invoice sent when due → auto-paid if cash balance sufficient → otherwise includes bank transfer instructions + Hosted Invoice Page link. Reconciliation (auto or manual) runs when funds arrive.

Accounts v2: manage cash balance via `v1/customers/acct_xxxxx/cash_balances`.

## Sources

- [[source-stripe-bank-transfers]] — overview: virtual account model, customer balance, international wires, disputes, sender info API, Connect, product/API support tables
- [[source-stripe-bank-transfers-accept-payment]] — full integration guide: PI creation per region, status lifecycle, reconciliation modes, Checkout constraints, testing
- [[source-stripe-bank-transfers-vban]] — VBAN permanence, allocation triggers, best practices, per-region daily/lifetime limits
- [[source-stripe-bank-transfers-refunds]] — 4 refund flows, refund status lifecycle, 45-day/180-day constraints, international wire limitation, test helpers
- [[source-stripe-subscriptions-bank-transfers]] — subscription setup: send_invoice+customer_balance required, days_until_due, cash balance auto-pay, reconciliation flow
