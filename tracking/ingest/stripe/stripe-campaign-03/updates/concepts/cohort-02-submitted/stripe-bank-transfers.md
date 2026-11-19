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
| Payment confirmation | November 7, 2026 overview: **delayed**; access is labeled **instant provisional**. Customer funding and reconciliation precede the documented completed-payment step, and standard payout timing applies. May 5, 2026 properties panel said **No**. |
| Recurring payments | Yes (requires customer action to fund) |
| Disputes | Conflict in November 7 overview: capability row says USD only; detailed reversal section discusses USD and CAD. CAD applicability is unresolved here. |
| Manual capture | No |
| Refunds | Yes / Partial yes |
| API enum | `customer_balance` |
| Requires redirect | No |

## Business Locations

- **EUR or USD**: 34 countries (AT, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IT, LI, LT, LU, LV, MC, MT, NL, NO, PL, PT, RO, SE, SI, SK, SM, US)
- **GBP**: November 7, 2026 overview lists AT, AU, BE, BG, CA, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HK, HR, HU, IE, IT, LI, LT, LU, LV, MC, MT, NL, NO, PL, PT, RO, SE, SG, SI, SK, SM, US; the May 5 capture listed GB only. This is merchant-account eligibility for GBP, not a statement that cross-border payments are supported.
- **JPY**: JP only
- **MXN**: MX only

## Customer Balance Model

Unlike card payments, Stripe cannot control the amount a customer pushes. Funds land in the **customer cash balance**:

- Stripe **attempts** to return unreconciled funds held for **more than 75 days**; it may contact the customer for missing bank details. A return attempt is not a completed refund.
- If Stripe can't determine bank account info by **90 days** → swept to merchant's Stripe balance
- EU EUR payments: beneficiary name must exactly match business name on Stripe to avoid screening delays

## Product Support

Supported: Connect, Checkout (non-subscription, non-setup modes), Payment Element, Subscriptions, Invoicing.
Unsupported in the overview's product rows: Payment Links, Express Checkout Element, Mobile Payment Element and Customer Portal. The November 7, 2026 cross-border row and unsupported-features paragraph also label International transfers unsupported; its US wire section nevertheless discusses domestic and international SWIFT receipt for US bank-transfer users. See the unresolved [[source-stripe-bank-transfers]] wire conflict before deciding account, currency or rail eligibility.

The November 7 overview lists Checkout Sessions and PaymentIntents as supported APIs; its PaymentIntent payment-method enum is `customer_balance`. SetupIntents, manual capture, and `setup_future_usage` are unsupported. Checkout excludes subscription and setup mode; Invoices and Subscriptions require `send_invoice` collection. The May 5, 2026 acceptance guide separately documents a hosted Checkout Session flow backed by a PaymentIntent. Its November variant index links an Elements Checkout Sessions route, whose detailed prerequisites and behavior were not captured. See [[source-stripe-bank-transfers-accept-payment]].

## International and Domestic Wires

The November 7 overview's US wire section says US bank-transfer users can accept domestic and international SWIFT wires; international wires can take 3–5 business days to settle into the cash balance, Stripe does not refund them, and US accounts accept SWIFT in USD only. The same capture also labels cross-border payments unsupported and says International transfers are unsupported. Treat exact account, currency, and rail eligibility as unresolved by this overview.

## Disputes

- **USD (ACH)**: the November 7, 2026 detailed section says a remitting-bank reversal must be sent no later than five days after payment, with evidence supplied to the bank. The capability row separately limits dispute support to USD transactions.
- **CAD (ACH)**: the same detailed section says reversals are initiated by the remitting bank and honored by the beneficiary bank. Its USD-only capability row and presentment-currency list do not establish CAD payment or dispute availability; applicability remains unresolved.
- **Other currencies**: the detailed section says bank transfers cannot be reversed except USD and CAD. Read that dated statement with the capability-row conflict; do not infer a universal or current irreversibility rule from this page.

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

Three distinct paths are documented in [[source-stripe-bank-transfers-refunds]]:

1. **Bank-transfer payment → customer bank**: Stripe needs destination bank details and may request them by Customer email (or `instructions_email`); missing Customer email can make refund creation fail. A payment can be refunded within 180 days of creation, and each bank-directed refund, including a partial refund, might incur a fee. Its Refund can move `requires_action` → `pending` → `succeeded`; a bank return can move it back to `requires_action`. `pending` is processing, while `succeeded` marks successful payout.
2. **Bank-transfer payment → customer cash balance**: choose **Customer cash balance** as the Dashboard refund destination. This succeeds immediately and is free. The pinned guide does not document a `destination: 'customer_balance'` API argument for this path.
3. **Available cash balance → customer bank**: use the Customer's cash-balance Dashboard refund flow or create a Refund with `origin: 'customer_balance'`, `customer`, `amount`, and `currency`, optionally `instructions_email`. This is a return of available cash balance, distinct from refunding a PaymentIntent.

The bank-directed **payment refund** can be canceled while it is still `requires_action` and before bank details arrive, using the payment Dashboard or `POST /v1/refunds/{id}/cancel` (older Node example: `stripe.refunds.cancel({ refund: id })`). An **available cash-balance return** can be canceled only before bank details arrive, through the Dashboard; cancellation credits the amount back to available cash balance.

**45-day warning:** The pinned guide says 45 days from the customer's receipt of the bank-detail request and a return to customer cash balance, but its status table says `failed` at 45 days after Refund creation and nearby prose says `refund.failed` with a return outside Stripe. Those clock and funds-destination statements are unresolved in the capture. Confirm the Refund and balance state rather than treating creation or `pending` as customer receipt.

International (SWIFT) refunds and automated refund emails are **not supported**; the guide describes a separate manual return path.

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
| EU | `eu_bank_transfer` + `country` | In the May 5, 2026 manual examples, the request's country selects IBAN localization; Dashboard-managed selection uses Customer or Stripe-account country. The guide says new localized VBANs are unavailable for ES. |
| JP | `jp_bank_transfer` | May 5 automatic-method examples include `return_url`; manual examples omit it. |
| MX | `mx_bank_transfer` | May 5 automatic-method examples include `return_url`; manual examples omit it. |

Or use `automatic_payment_methods: { enabled: true }`. If customer balance covers amount → immediate `succeeded`.

**May 5, 2026 PaymentIntent funding events**: First confirmation with insufficient balance emits `payment_intent.requires_action`, including when pre-existing cash balance partially applies. Later incoming funds that still leave the Intent incomplete emit `payment_intent.partially_funded`; `payment_intent.succeeded` marks completion. Changing a partially funded Intent amount returns applied funds to customer balance; other open Intents may receive them automatically, while manual reconciliation requires reapplication.

**Reconciliation**: automatic by default; override per customer: `cash_balance.settings.reconciliation_mode = 'manual'`.

**Testing**: `POST /v1/test_helpers/customers/{id}/fund_cash_balance` or `stripe test_helpers customers fund_cash_balance`.

## Checkout Constraints

Payment mode only (no subscription/setup mode). Single currency. One-time line items only. Customer must be specified in session. Delayed notification method.

## Subscription integration

Requires `collection_method='send_invoice'` and `payment_method_types=['customer_balance']`. Cash balance is central — every bank transfer subscription must have an associated Customer/Account. Set `days_until_due` for the payment window.

Invoice sent when due → auto-paid if cash balance sufficient → otherwise includes bank transfer instructions + Hosted Invoice Page link. Reconciliation (auto or manual) runs when funds arrive.

Accounts v2: manage cash balance via `v1/customers/acct_xxxxx/cash_balances`.

## Sources

- [[source-stripe-bank-transfers]] — May 5 and November 7, 2026 full overviews: virtual-account and customer-cash-balance model, expanded GBP account eligibility, Checkout Sessions and PaymentIntents support, sender-info examples, Connect, and unresolved cross-border/SWIFT and USD/CAD dispute contradictions.
- [[source-stripe-bank-transfers-accept-payment]] — May 5, 2026 full PaymentIntent, Checkout and Direct API guide, plus November 7 variant-index navigation (including an unread Elements Checkout Sessions route); consult the source's dated qualifications.
- [[source-stripe-bank-transfers-vban]] — VBAN permanence, allocation triggers, best practices, per-region daily/lifetime limits
- [[source-stripe-bank-transfers-refunds]] — 4 refund flows, refund status lifecycle, 45-day/180-day constraints, international wire limitation, test helpers
- [[source-stripe-subscriptions-bank-transfers]] — subscription setup: send_invoice+customer_balance required, days_until_due, cash balance auto-pay, reconciliation flow
