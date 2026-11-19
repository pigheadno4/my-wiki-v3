---
title: "Stripe: Bank Transfer Payments"
type: source
date_ingested: 2026-05-05
date_updated: 2026-11-15
original_format: webpage
canonical_url: https://docs.stripe.com/payments/bank-transfers
raw_files:
  - "stripe-payments-bank-transfers-2026-11-07.md"
  - "stripe-bank-transfers-2025.md"
tags: [stripe, bank-transfers, customer-balance, payments, ach, sepa, swift, wire, connect]
---

## Summary

Stripe's bank transfer overview describes a push-payment method. Stripe supplies a virtual account number, the customer sends funds from their bank, Stripe holds incoming funds in that customer's cash balance, and reconciliation applies them to a payment or invoice. Receipt of funds and provisional access do not by themselves mean the payment is complete: the November 7 customer-experience sequence marks completion after reconciliation and notification. This page compares the November 7, 2026 full capture with the May 5, 2026 capture.

## Key Details

**Activation and identity.** Enable bank transfers in Payment methods settings. The customer's virtual account details and transfer reference are used to send funds; the real merchant bank account is not exposed. Checkout requires a Customer on the session. The incoming Cash Balance Transaction has type `funded`; its `funded.bank_transfer` fields describe the sender and payment rail. A funding transaction, a cash balance, a reconciled PaymentIntent or invoice, and a merchant payout are different states and objects.

**Timing and recurrence.** The November capture labels access “Instant provisional access,” payment confirmation “Delayed,” and settlement “Standard payout schedule.” Recurring payments are supported only while the customer keeps enough cash balance to cover each invoice. Stripe attempts to return unreconciled funds held for **more than 75 days**. It may contact the customer if bank details are missing; only if it cannot determine account information by day 90 does it sweep the unreconciled funds to the merchant's Stripe balance. These are an attempted return and conditional sweep, not unconditional completed refunds.

**Eligibility.** The listed presentment currencies are EUR, GBP, JPY, MXN, and USD, with merchant-country eligibility per currency. The November GBP row lists AT, AU, BE, BG, CA, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HK, HR, HU, IE, IT, LI, LT, LU, LV, MC, MT, NL, NO, PL, PT, RO, SE, SG, SI, SK, SM, and US; the May capture listed GB only. EUR or USD have their separate account-country row; JPY is listed for JP and MXN for MX. IBAN localization is listed for DE, FR, IE, and NL. There is no extra bank-transfer-specific amount limit beyond Stripe's currency minimum and maximum. For EU EUR transfers, the beneficiary name should exactly match the business name registered with Stripe to avoid screening delays.

**Products and APIs.** The November matrix lists full-page and embedded Checkout, Payment Element, Billing, Invoicing, and Connect as supported. Checkout Sessions and PaymentIntents are supported APIs; the PaymentIntent method enum is `customer_balance`. Checkout does not support bank transfers in subscription or setup mode. Invoices and Subscriptions support only `send_invoice` collection. SetupIntents, `setup_future_usage`, manual capture, Payment Links, Express Checkout Element, in-app payments, Managed Payments, Customer Portal, Radar, and Terminal are listed unsupported. The matrix says no redirect is required. Checkout session Customer requirement remains in both captures.

**Refunds and disputes.** Full and partial refunds may go to the customer bank account or back to the cash balance. Stripe needs bank details for a bank-account refund and may email the customer to collect them. The November capability row says dispute support is **USD transactions only**, while the detailed section on the same page says USD and CAD bank transfers can be reversed and describes CAD ACH reversals. The capture's presentment-currency list omits CAD. Treat CAD availability and dispute applicability as unresolved in this overview; USD ACH reversals are described with a five-day deadline. Do not generalize “irreversible” across all other cases from this contradictory page.

**Wire contradiction.** The November payment-support row says cross-border payments are not supported, and its unsupported-features paragraph says International transfers are unsupported. Yet the same November wire section says US bank-transfer users can accept domestic and international SWIFT wires, with 3–5 business days to settle into customer balance, possible fee deductions, no Stripe refund for international wires, and USD-only SWIFT receipt for US accounts. The May capture contains the same wire-versus-unsupported contradiction. This overview does not resolve whether a particular cross-border transfer is eligible; verify the exact account, currency, and rail before relying on wire receipt.

**Sender information.** In the Dashboard, open the customer's cash balance Funding transaction. The November API example uses `GET /v1/customers/{customer}/cash_balance_transactions/{transaction}` via curl; the May example used the Node SDK method `stripe.customers.retrieveCashBalanceTransaction(customerId, transactionId)`. These examples are dated representations of the Cash Balance Transactions API, not evidence that the Node method was removed. `funded.bank_transfer` examples show EU BIC/IBAN last four and SEPA network; GB account number last four and sort code; JP sender bank/branch; MX CLABE last four; and US ACH or domestic-wire network.

**Connect.** Bank transfers can be used with all Connect charge types. `on_behalf_of` is unsupported. Direct charges require the connected account itself to activate the method and have the relevant capability. Capability activation and incoming funding do not establish that a particular payment succeeded.

## Related

- [[stripe]] — Stripe company route.
- [[stripe-bank-transfers]] — concept and reciprocal conflict notes.
- [[stripe-customer-balance]] — cash-balance and reconciliation concept.

## Raw Sources

- [[raw/stripe-payments-bank-transfers-2026-11-07|2026-11-07 full bank transfer overview]] — complete newer factual capture, 453 lines.
- [[raw/stripe-bank-transfers-2025|2026-05-05 bank transfer overview]] — retained historical factual capture, 408 lines; includes the dated Node sender-info example.
