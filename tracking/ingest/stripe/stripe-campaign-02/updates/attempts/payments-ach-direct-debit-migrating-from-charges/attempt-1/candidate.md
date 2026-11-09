---
title: "Stripe: Migrate Existing ACH Bank Accounts"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/ach-direct-debit/migrating-from-charges"
raw_files:
  - "stripe-ach-migrate-bank-accounts-2025.md"
tags: [stripe, ach, us-bank-account, migration, bank-account, mandates, checkout-sessions, payment-intents]
---

## Summary

The 2026-05-02 guide at this canonical URL explains how to reuse existing ACH `BankAccount` objects collected through Stripe's Tokens API with Checkout Sessions or the Payment Intents API. It includes verified-account prerequisites, mandate acknowledgment for Payment Intents, saved-bank-account display, Invoicing and Subscriptions defaults, and a criterion for identifying legacy Charges. The 2026-11-07 capture of the same base URL is a short index linking to separate Checkout Sessions and Payment Intents variants; it does not reproduce those instructions. The linked variants were not captured in this unit, so the older mechanics remain dated evidence rather than verified November behavior.

> [!warning] Historical migration notice
> The 2026-05-02 guide said Stripe was removing support for legacy ACH Direct Debit integrations and that merchants creating legacy ACH payments must migrate to Payment Intents or Checkout Sessions (old raw lines 16–18). The November index does not establish the current retirement schedule or status.

## Prerequisites by integration path (2026-05-02 guide)

| Path | Saved bank-account prerequisite |
| --- | --- |
| Checkout Sessions API | The customer's bank account is verified. |
| Payment Intents API | The customer's bank account is verified **and** an active mandate exists for that bank account. |

An already verified BankAccount does not need repeat verification for either path (old raw lines 22–28). An existing active mandate can satisfy the Payment Intents prerequisite; creating another mandate is not universally required before every use. This distinction qualifies the guide's later first-use mandate examples.

## Checkout Sessions path (2026-05-02 guide)

To display saved verified bank accounts, the guide's Checkout Sessions example passes a `customer`, sets `payment_method_types: ['us_bank_account']`, and uses `saved_payment_method_options.allow_redisplay_filters: ['unspecified', 'always']` (old raw lines 34–70). It says Checkout then displays saved verified accounts for that customer. The example uses `ui_mode: 'elements'` and `return_url`; do not treat those fields as a universal Checkout configuration.

If the Customer already has an email, the guide says Checkout pre-fills it and does not let the customer edit it; the React and HTML examples check the Session email before rendering an editable input (old raw lines 73–99).

## Payment Intents path and mandate (2026-05-02 guide)

Confirming a PaymentIntent or SetupIntent requires authorization to debit the account. If a previously saved verified BankAccount already has an active mandate, it can be reused under the guide's stated prerequisite. Otherwise, the guide shows these ways to document authorization before first use: confirm a SetupIntent with `mandate_data.customer_acceptance` (including an offline example); provide `mandate_data` at PaymentIntent confirmation; or use a PPD mandate for qualifying offline preauthorization. It also describes prior online authorization data and warns that placeholder IP or user-agent data should be identifiable if used (old raw lines 105–161). Authorization collected for the first use can support later reuse of the BankAccount as a PaymentMethod, subject to mandate validity (old raw line 114).

The captured examples pass the saved `BankAccount` ID directly as `payment_method` in PaymentIntent or SetupIntent calls (old raw lines 164–193). `paymentMethods.retrieve(BANKACCOUNT_ID)` returns a `us_bank_account` PaymentMethod view; the guide says this does **not** create a second object, only another view of the same underlying bank account (old raw lines 196–263).

## Invoicing and Subscriptions (2026-05-02 guide)

For continued use of a saved BankAccount, **collect mandate acknowledgment first**. Then update the customer's `invoice_settings.default_payment_method`, or set `default_payment_method` directly on the invoice or subscription as appropriate (old raw lines 265–329). Setting a default alone is not authorization to debit. The example uses the same saved bank-account ID in these fields.

## Identify legacy ACH Charges (2026-05-02 guide)

The guide says `Charge.payment_method_details.type` is `ach_debit` for a legacy integration and `us_bank_account` for the newer integration (old raw lines 332–334). It lists legacy creation paths: Create Charge API; Invoices or Subscriptions charging a Customer's legacy BankAccount `default_source` without a `default_payment_method` on the Customer, invoice, or subscription; and a PaymentIntent using `payment_method_type: ach_debit` (old raw lines 336–340). These are dated identification criteria from the May capture, not new November API rules.

## Related

- [[stripe-ach-direct-debit]] — ACH Direct Debit concept
- [[source-stripe-ach-direct-debit]] — payment-method timing, mandates, disputes, and refunds
- [[source-stripe-ach-migration]] — broader legacy ACH migration

## Related raw API references

- [[raw/stripe-payments-ach-direct-debit-migrating-from-charges-2026-11-07|2026-11-07 migration variant index]] — links to Checkout Sessions and Payment Intents variants; no instructions captured in this base-page snapshot.

## Raw Sources

- [[raw/stripe-ach-migrate-bank-accounts-2025|2026-05-02 full migration guide]]
