---
title: "Braintree Moneris Statements"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/moneris/statements"
raw_files:
  - "braintree/articles/moneris/statements-2026-09-16.md"
tags: [braintree, moneris, statements, reconciliation, fees, chargebacks]
---

## Overview

This collected [[braintree]]-hosted Moneris-route article describes a monthly processing statement mailed to the business address on file, the statement's sales, refund, fee, chargeback, debit and credit sections, and its use in helping reconcile account deposits. It is a document snapshot for [[payment-reconciliation-reporting]], not an independent current Moneris API or policy source, a merchant-specific pricing or currency agreement, or proof that a payment, credit, debit or deposit occurred.

## Key takeaways

- The article says Moneris mails the statement three to five business days after the beginning of the month. It also says no statement is issued when no transactions were processed.
- The Sales Summary by Card Type provides monthly gross and net sales, refunds, transaction counts and average sale amounts by card type. The Daily Activity Summary adds daily gross sales, returns or refunds, net sales, discount and transaction fees, and chargebacks; its per-day totals are presented as reconciliation figures that should match account deposits.
- The Monthly Summary reports total discount and transaction fees plus total chargebacks debited for the month. The Transaction Fees section further organizes assessed fees, including chargeback fees, by card brand and includes the associated transaction amount, volume, rate and total debited fee.
- Financial Details reports daily debits and credits by card type, the destination account number, possible GST or HST charges, and monthly totals for GST/HST and account credits. The article does not identify the statement currency, so GST/HST references must not be used to infer a currency or conversion rule.
- The Interchange and Wholesale Discount Fees section applies only to accounts on the interchange-plus pricing model and reports assessed interchange-fee type, amount and rate by card brand. This condition does not establish that a particular account uses interchange-plus pricing or that the listed fee treatment is current.
- The Chargeback Summary reports monthly chargeback amount, count and reason by card brand. These statement fields are reporting descriptions, not evidence of a particular chargeback or its outcome.

> [!warning] Exact account-route snapshot only
> Keep the mailing timing, statement contents, reconciliation language, pricing condition, GST/HST references and account-credit or debit descriptions within this captured Braintree Moneris documentation route. Do not transfer them to sibling Braintree processor, regional, Marketplace or pricing-account guides, and do not treat them as current independent Moneris policy, an API contract, a currency rule, account eligibility, or merchant-specific pricing.

> [!warning] Statement reconciliation is not money-movement proof
> The article says daily totals should match deposits and that the statement can help reconcile deposits. Those statements describe the document's intended use; they do not prove payment acceptance, settlement, funding, bank receipt, or any individual deposit.

## Detail locators

- Mailing timing, business-address destination and no-transaction qualification: `# Statements`, raw line 16.
- Monthly processing-summary purpose and reconciliation route: `# Statements`, raw line 18.
- Sales and refund totals, transaction counts and average sale amounts by card type: `## Sales Summary by Card Type`, raw lines 21-23.
- Monthly discount and transaction fees plus chargebacks debited: `## Monthly Summary`, raw lines 26-28.
- Daily sales, refund, fee and chargeback fields and deposit-matching language: `## Daily Activity Summary`, raw lines 31-33.
- Daily account debits and credits, account number, GST/HST and credited monthly total: `## Financial Details`, raw lines 36-38.
- Interchange-plus-only fee section and card-brand organization: `## Interchange and Wholesale Discount Fees`, raw lines 41-43.
- Assessed transaction-fee fields and chargeback-fee inclusion: `## Transaction Fees`, raw lines 46-48.
- Monthly chargeback amount, count and reason by card brand: `## Chargeback Summary`, raw lines 51-53.

## Related

- Company: [[braintree]]
- Main concept: [[payment-reconciliation-reporting]]

## Related raw API references

- [[raw/braintree/articles/moneris/reconciliation-2026-09-16|Braintree Moneris Reconciliation]] - unread navigation-only destination linked for reconciliation context; not used as factual evidence here
- [[raw/braintree/articles/moneris/pricing-fees-2026-09-16|Braintree Moneris Pricing and Fees]] - unread navigation-only destination linked for interchange-plus pricing context; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/moneris/statements-2026-09-16|Braintree Moneris Statements]] - fully read collected article covering monthly mailing timing, statement sections, account activity, pricing-qualified interchange detail and reconciliation use
