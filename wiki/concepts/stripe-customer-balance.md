---
title: "Customer Balance (Stripe)"
type: concept
category: technology
tags: [stripe, customer-balance, bank-transfers, payments, reconciliation, invoicing]
---

## Definition

The Stripe customer balance is a per-customer ledger with two distinct sub-balances:

| Type | Purpose | Usable for payment? |
| --- | --- | --- |
| **Cash balance** | Reconciliation layer for incoming bank transfers | Yes — up to available amount |
| **Invoice balance** | Liability offset between merchant and customer | No — only offsets future invoices |

## Cash Balance

Funds flow in when customers overpay via bank transfer or when transfers aren't automatically reconciled. Each customer can hold cash balances in multiple currencies (one per accepted bank transfer currency).

**Constraints**: cannot be topped up directly; not a digital wallet or e-money; can only be used for future payments or returned to the customer's bank account.

**Refund and return routes**: A bank-transfer payment refunded to the Customer cash balance through the Dashboard succeeds immediately and is free; this differs from returning available cash balance to the customer's bank. For the latter, [[source-stripe-bank-transfers-refunds]] documents a Refund with `origin: 'customer_balance'`, Customer ID, amount, and currency, or a Dashboard flow. An unprocessed return can be canceled through the Dashboard before bank details arrive, crediting the amount back to available cash balance. Bank-directed Refunds can require details and pass through `requires_action` and `pending`; those states do not show customer receipt. The captured guide has unresolved 45-day clock and post-failure funds-location wording (new raw lines 19, 49, 54; old raw lines 18, 52, 57).

**Retrieve**: expand `cash_balance` on the Customers API. A Customers v1 customer uses its `cus_` ID; a customer-configured Accounts v2 Account uses its `acct_` ID as the path parameter at `GET /v1/customers/acct_xxxxx`. The November 2026 guide says Accounts v2 was generally available for Connect users, in public preview for other Stripe users, and required a preview API version for preview participants. The May Node.js example uses `stripe.customers.retrieve(id, { expand: ['cash_balance'] })`. See [[source-stripe-customer-balance]] for the dated route. Separately, the November funding-instructions guide uses a customer-configured Account ID at `/v1/customers/acct_xxxxx/funding_instructions`; this is a funding-instructions route, not cash-balance retrieval, and does not establish account-specific access. See [[source-stripe-customer-balance-funding-instructions]].

**Pay from cash balance**: The November 2026 guide first says to enable bank transfers in Dashboard. Create a PaymentIntent with `payment_method_data.type: 'customer_balance'`, the amount/currency, and `customer_account` for a customer-configured Accounts v2 Account or `customer` for Customers v1; its example sets `confirm: true`. The May Node.js example also includes `payment_method_types: ['customer_balance']`, while November curl omits it, without proving API removal. The page says sufficient available cash succeeds and insufficient cash fails; verify the actual Intent state before treating a request or return URL as payment success. See [[source-stripe-customer-balance]].

## Reconciliation

**Modes**: `automatic` (default) or `manual`. Override per customer: `stripe.customers.update(id, { cash_balance: { settings: { reconciliation_mode: 'manual' } } })`. Reset with `merchant_default`.

**Automatic priority order** (US/UK/EU/MX, November 7, 2026 capture):

1. Match transfer reference → single invoice number (capped at the triggering transfer amount).
2. Match transfer reference → single incomplete PI by `display_bank_transfer_instructions.reference` (same cap).
3. Match the exact *available cash balance* to a group of 1–5 invoices and PIs → smallest group → most invoices → oldest PIs.
4. Fully fund eligible invoices, oldest **due** first.
5. Apply remainder to oldest incomplete PIs.

The full same-currency available balance includes earlier unreconciled transfers; later steps consider funds remaining after reference matching. JPY skips reference matching, then matches an exact-balance group, fully funds invoices by oldest **finalization** time, and applies the remainder to PIs by oldest **confirmation** time. Automatic invoice eligibility is `open` and current or overdue within the last **365 days**. The May 5, 2026 source said **30 days**, matched the amount sent, and used oldest finalization in the US/UK/EU/MX invoice fallback; treat those as dated descriptions.

Automatic partial funding of an incomplete PI can occur on arrival of funds. Automatic partial invoice payment requires the automatic partial reconciliation setting and the invoice number in the transfer memo. At invoice finalization, existing balance applies only if it fully pays after the configured underpayment threshold; otherwise it remains in cash balance. See [[source-stripe-customer-balance-reconciliation]] for the dated source and manual-payment distinction.

**Manual reconciliation**: A manual-mode customer receives no automatic application. An incomplete or partially funded PI or an open invoice (including overdue) can be funded in the Dashboard; an invoice can be partially funded there. The PI API is `POST /v1/payment_intents/{id}/apply_customer_balance` with `currency` and optional `amount` (defaults to the PI's remaining requested amount).

**Webhook examples**: The November 7, 2026 source uses `customer_cash_balance_transaction.created`, a single transaction object; filter for `type: funded` before considering eligible same-currency PIs and recheck balance after each application. The May 5, 2026 source used `cash_balance.funds_available` with an aggregate CashBalance snapshot, including earlier funds. The newer example does not establish deprecation of the older event. Neither event alone proves an invoice or PI is paid.

**Unreconciled funds**: The bank-transfer overview says Stripe attempts return after funds have been held for **more than 75 days**; the reconciliation guide describes returning the aged portion at **75 days**, with newer funds aging separately. A return attempt can fail. If customer bank account information still cannot be determined by **day 90**, remaining aged funds are swept to the merchant's Stripe balance. This is not another return attempt, and the merchant remains responsible for reconciliation. See [[source-stripe-customer-balance-reconciliation]] and [[source-stripe-bank-transfers]].

## Invoice Balance (Credit Balance)

Adjusted via Customer Balance Transactions. Applied at invoice finalization to reduce amount due. Represents a liability — not spendable as cash. Distinct from credit balance (see Customer Credit Balance docs).

## Cash Balance Transaction Types

| Type | Description |
| --- | --- |
| `funded` | Customer made a bank transfer; funds may auto-apply to open PaymentIntents |
| `applied_to_payment` | Funds applied to a PaymentIntent (auto or manual reconciliation) |
| `unapplied_from_payment` | Partially funded PaymentIntent was modified/canceled; funds returned to cash balance |
| `refunded_from_payment` | Successful PaymentIntent refunded back to cash balance |
| `return_initiated` | Unspent funds being returned to customer's bank account |
| `return_canceled` | Return attempt canceled (bank details not collected or refund canceled) |
| `transferred_to_balance` | Funds swept to merchant's Stripe balance due to failed refund or missing bank details |

## Funding Instructions

`stripe.customers.createFundingInstructions(id, { funding_type: 'bank_transfer', bank_transfer: { type }, currency })` — retrieve virtual bank account details without a PaymentIntent.

Per-region `financial_addresses` examples: US → ABA (ACH/domestic wire) and SWIFT; UK → sort_code (May: Bacs/FPS; November 2026: Bacs/CHAPS/FPS); EU → IBAN/BIC (SEPA); JP → zengin; MX → SPEI/CLABE. The captured SEPA pricing description includes up to 1,000 VBANs without a stated per-account denominator; Spain's restriction applies to creating **new localized VBANs**, not all funding instructions. Networks describe the captured address schema, not every actual customer's returned address. See [[source-stripe-customer-balance-funding-instructions]].

Live mode: Stripe says each customer receives a unique **set of bank-transfer details**, not necessarily one VBAN; a response can contain distinct financial-address types. Sandbox/test details are invalid and might not always be unique. The May 2026 funding guide describes a Dashboard PDF ownership letter; the November page links to a separate letter page whose content was not in this capture. See [[source-stripe-customer-balance-funding-instructions]].

## See Also

- [[stripe-bank-transfers]] — primary funding mechanism for the cash balance
- [[source-stripe-customer-balance]] — overview: two balance types, transaction types, payment from balance API

## Sources

- [[source-stripe-customer-balance]] — 2026-05-05 and 2026-11-07 full customer-balance guides: cash versus invoice ledger, `cus_`/`acct_` retrieval, November Accounts v2 access scope and bank-transfer enablement before a cash-balance PaymentIntent, and seven transaction types; requested payment is not confirmed success.
- [[source-stripe-customer-balance-reconciliation]] — May 5 and November 7, 2026 webpage captures: automatic and manual reconciliation, transaction versus aggregate webhook examples, and aged-portion 75/90-day handling
- [[source-stripe-customer-balance-funding-instructions]] — May/November 2026 funding-instructions guide: Customer/API address shapes, UK CHAPS table addition, Accounts v2 customer-configured Account route, SEPA VBAN limit, and dated ownership-letter route
- [[source-stripe-bank-transfers-refunds]] — bank-transfer payment refunds, available cash-balance returns, cancellation boundaries, and captured 45-day wording conflict
