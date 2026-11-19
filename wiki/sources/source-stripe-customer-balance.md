---
title: "Stripe: Customer Balance"
type: source
date_ingested: 2026-05-05
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/customer-balance"
raw_files:
  - "stripe-payments-customer-balance-2026-11-07.md"
  - "stripe-customer-balance-2025.md"
tags: [stripe, customer-balance, bank-transfers, payments, reconciliation, invoicing]
---

## Summary

Stripe distinguishes a customer's cash balance, a per-currency reconciliation layer for bank transfers, from an invoice balance, a liability offset for future invoices. The 2026-11-07 page adds an Accounts v2 access/version qualifier and an explicit Dashboard bank-transfer enablement step before a cash-balance PaymentIntent. Both captures describe seven cash-balance transaction types (new raw lines 9-31, 125-187; old raw lines 8-26, 115-185).

## Balance types and permitted uses

- **Cash balance** receives overpayments and bank transfers that have not been automatically reconciled to outstanding payments. A customer may have a separate balance in each accepted bank-transfer currency. Available funds can pay later obligations of the *same customer* or be returned to that customer's bank account up to the available amount (new raw lines 9-17).
- Cash cannot be added directly or topped up as a wallet; the page calls it a reconciliation layer, not digital wallet or e-money. It is not for other purposes (new raw lines 15-17).
- **Invoice balance** records merchant-customer liability. It cannot fund a direct payment; it offsets future invoices and can be adjusted through a Customer Balance Transaction (new raw lines 19-21). Do not treat these two ledgers as interchangeable.

## View a cash balance and preserve customer identity

Retrieve a Customer with `cash_balance` expanded, or use the Customer page's Payment methods section in Dashboard. The expanded object shows `available` by currency and `settings.reconciliation_mode` in the sample (new raw lines 23-56, 123).

For a customer-configured **Account** in Accounts v2, the page says to use the Customers API endpoint with the `acct_` Account ID as the path parameter, for example `/v1/customers/acct_xxxxx`. This differs from a Customers v1 `cus_` ID (new raw lines 25-38, 42-56). The November page says Accounts v2 was generally available for Connect users and in public preview for other Stripe users; participants in that preview must specify a preview API version. This is documented capture scope, not proof that a particular account has access (new raw lines 27-31).

The May capture illustrated `stripe.customers.retrieve(id, { expand: ["cash_balance"] })` in Node.js; the November page uses curl. The example-language change does not remove the retrieval behavior (old raw lines 22-37; new raw lines 23-38).

## Pay from available cash balance

**Enable bank transfers in Dashboard before creating the intent**, as the November guide explicitly instructs (new raw lines 125-129). Its curl examples create and confirm a PaymentIntent with `payment_method_data[type]=customer_balance`, an amount and currency, and either `customer_account` for Accounts v2 or `customer` for Customers v1; they also include an illustrative `return_url` (new raw lines 131-159). The May Node.js examples additionally specified `payment_method_types: ["customer_balance"]` and `payment_method_data.type`; omission of `payment_method_types` from the new curl examples is not evidence that the field was removed from the API (old raw lines 119-157).

The page says a cash-balance payment succeeds if sufficient funds exist and fails otherwise. For insufficient funds, use the separate bank-transfer-funding route to collect more (new raw lines 161-167). Creating an Intent with `confirm=true`, or including `return_url`, does not by itself prove that a particular payment succeeded, redirected, or had adequate funds; check the actual PaymentIntent state.

## Cash-balance transaction types

The current page lists changes per customer across all cash-balance currencies (new raw lines 169-177). The seven types retain their prior meanings:

| Type | Recorded change |
| --- | --- |
| `funded` | Incoming bank transfer; later automatic application depends on reconciliation (new raw line 181) |
| `applied_to_payment` | Cash applied to a PaymentIntent through automatic or manual reconciliation (new raw line 182) |
| `unapplied_from_payment` | Funds on a partially funded Intent returned to cash balance when that Intent was modified or canceled (new raw line 183) |
| `refunded_from_payment` | Successful Intent refunded to customer cash balance for later use (new raw line 184) |
| `return_initiated` | Return of unspent funds to the customer's bank was initiated; completion is not implied (new raw line 185) |
| `return_canceled` | Bank return attempt was canceled or bank details could not be collected (new raw line 186) |
| `transferred_to_balance` | Funds moved from customer cash balance to Stripe balance after failed refunds or insufficient refund details (new raw line 187) |

## Related Pages

- [[stripe-customer-balance]] — customer-balance concept and identity/prerequisite qualifications
- [[source-stripe-customer-balance-funding-instructions]] — bank-transfer funding instructions
- [[source-stripe-customer-balance-reconciliation]] — allocation and reconciliation behavior
- [[source-stripe-bank-transfers-refunds]] — returns and refund status
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-payments-customer-balance-2026-11-07|Customer balance guide, captured 2026-11-07]] — current pinned full page, including access and bank-transfer enablement qualifiers
- [[raw/stripe-customer-balance-2025|Customer balance guide, captured 2026-05-05]] — earlier full guide and Node.js examples
