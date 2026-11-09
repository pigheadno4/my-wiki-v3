---
title: "Stripe: Save ACH Direct Debit Details for Future Payments"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: https://docs.stripe.com/payments/ach-direct-debit/set-up-payment
raw_files:
  - "stripe-ach-set-up-payment-2025.md"
tags: [stripe, ach, us-bank-account, setup-intent, checkout, financial-connections, microdeposits]
---

## Summary

The 2026-11-07 base-URL capture is a variant index for Checkout, Elements, iOS, Android, and React Native. It contains no instructions from those linked variants. The detailed 2026-05-02 capture at the same URL covers all five routes for saving ACH bank account details for future payments; its instructions below are dated to that capture. A SetupIntent's success records setup or bank verification, not a later ACH debit or settlement.

## Route coverage in the 2026-05-02 guide

- **Checkout**: setup mode collects a reusable `us_bank_account` PaymentMethod. The Checkout Session includes `payment_method_types` with `us_bank_account` and Financial Connections `payment_method` permission. After the session, use the saved PaymentMethod ID with a later PaymentIntent when actually initiating a payment.
- **Elements**: create a SetupIntent for `us_bank_account`; collect bank details with `stripe.collectBankAccountForSetup`, display mandate terms and obtain customer authorization, then confirm with `stripe.confirmUsBankAccountSetup`.
- **iOS, Android, and React Native**: the older capture also has distinct mobile SetupIntent variants. Their route-specific SDK methods and examples remain in the older raw capture; the 2026-11-07 index only links to the variants and does not verify their current instructions or SDK versions.

## Setup, verification, and reuse

The older Elements and mobile flows use Financial Connections for instant verification by default, with manual bank entry and microdeposit verification as a fallback. For a SetupIntent, `succeeded` means the bank account was instantly verified or verification was unnecessary; `requires_action` means further verification is needed. For microdeposits, the dated guide describes a descriptor code with up to 10 failed attempts or two amounts with up to 3, and a 10-day verification timeout. In the Elements route, obtain authorization by showing the mandate terms before confirming the SetupIntent.

After SetupIntent success, updating the customer's `invoice_settings.default_payment_method` is **optional**; saving the reusable PaymentMethod does not itself make it the customer's invoice default. The older guide separately shows a later PaymentIntent using the saved PaymentMethod and customer to initiate a debit. ACH Direct Debit is a delayed-notification payment method, so successful setup or bank verification does not demonstrate that any subsequent debit has settled. Sandbox examples in the older capture settle instantly in the test balance, unlike live payments; they are not evidence of real bank receipt or current live timing.

## Financial Connections data scope

The older Checkout route requires the `payment_method` permission. The Elements SetupIntent sample requests both `payment_method` and `balances`; the latter is an additional data permission for a balance check, not a universal setup requirement. Access to Financial Connections account data requires requested permissions and successful Financial Connections authentication. Manually entered accounts verified by microdeposits have no `financial_connections_account` ID on the PaymentMethod and no additional Financial Connections balance data in this guide. The older guide discusses Accounts v2 customer-configured Accounts and Customers v1 as different customer representations; its Accounts v2 availability and preview conditions are dated, not reverified by the new index.

## Evidence boundary

The 2026-11-07 capture is navigation only. The Checkout, Elements, iOS, Android, and React Native variant destinations were not fetched in this job. Their present instructions, availability, SDK versions, and any changed setup or verification behavior remain unverified. No live SetupIntent, bank verification, PaymentIntent, ACH notification, or settled bank receipt was observed.

## Raw Sources

- [[raw/stripe-ach-set-up-payment-2025|2026-05-02 ACH save-for-future guide]] — historical detailed Checkout, Elements, iOS, Android, and React Native variant content, including examples and microdeposit error tables.

## Related raw API references

- [[raw/stripe-payments-ach-direct-debit-set-up-payment-2026-11-07|2026-11-07 ACH save-for-future variant index]] — navigation to the five route variants only; no fetched variant instructions.
