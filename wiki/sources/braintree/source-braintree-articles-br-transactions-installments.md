---
title: "Braintree Brazil Installment Transactions"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/br/transactions/installments"
raw_files:
  - "braintree/articles/br/transactions/installments-2026-09-16.md"
tags: [braintree, brazil, installments, credit-cards, transactions, brl]
---

## Overview

This collected Braintree Brazil article describes creating and managing credit-card installment transactions: a sale carries the total transaction amount and an installment count, can be submitted for settlement immediately or later, can be adjusted through refunds or chargebacks, and exposes installment details through transaction search or the Control Panel. The page describes installments as 30 days apart in sets of 2–12 and says fees are associated with them, but it provides no fee schedule or assessment rule.

Treat this as a 2026-09-16 snapshot of the article, not proof of current merchant or account eligibility, card enablement, successful authorization, settlement, clearing, disbursement or funding. It is a Brazil card-installment route, not generic BNPL or PayPal Pay Later guidance.

## Key takeaways

- The page says an account is set up by default to accept installments on Visa, Mastercard, Amex, Elo and Hipercard. It separately says Brazil installments are supported only for credit cards and points combo-card transactions to the sale request's `account_type` field. Those statements do not identify the account type or onboarding conditions and do not prove a particular merchant account is enabled.
- Creating an installment transaction requires the total transaction amount and an integer count from 2 through 12. The page labels the request field `installmentCount:String`, while its Ruby example uses nested `installments` / `count`; do not silently treat these displayed shapes as interchangeable without the linked request reference.
- The page says the amount is the total installment amount in Brazilian Real, is split equally across the requested installments, and must calculate to at least 5 BRL per installment. Its 50 BRL / 10-installment calculation is an example, not a broader guarantee or a rounding rule.
- A sale can be submitted for settlement immediately or later. Later settlement remains subject to authorization expiration; the page says the total amount can then be adjusted only to an amount equal to or lower than the authorization, while retaining the equal-split and 5 BRL-per-installment statements. A request or response does not prove final settlement or clearing.
- Refunds use the total amount to be refunded and return installment and adjustment data. Chargebacks can also adjust installments, with `adjustmentReason` identifying the trigger. Search API and Control Panel lookup expose installment IDs, amounts, projected and actual clearing dates, and adjustment amounts and reasons; these fields are records, not guarantees of future timing or payment completion.

## Evidence limitations

> [!warning] Account, fee, schedule and amount boundaries
> The article does not define production activation, merchant eligibility, account prerequisites, fee amounts, fee timing, buyer-facing choice, or a complete authorization, clearing, disbursement or funding lifecycle. Its 30-day statement describes installment spacing without assigning every debit or payout event. A separately collected same-date Brazil payment-capabilities page says that a non-even installment disbursement remainder is paid with the final installment; this article does not state a rounding or remainder rule for its equal-split wording, so the relationship remains unresolved rather than transferable as policy. [[raw/braintree/articles/br/payment-capabilities-2026-09-16|Braintree Brazil Payment Capabilities]]

## Detail locators

- Installment spacing, 2–12 range, fee mention, installment-set identity and refund/chargeback adjustments: opening paragraph below `# Installments`, raw line 16.
- Default card-brand list: `## Card Types`, raw lines 19–29.
- Credit-card-only scope and combo-card `account_type`: `### Installment support on combo cards`, raw lines 31–33.
- Required total amount, count range, displayed request-field label and complete Ruby example: `## Creating Installments > ### Request`, raw lines 36–90.
- BRL total, equal-split wording, 5 BRL calculated minimum and 50 BRL / 10 example: note after the Ruby example, raw lines 92–95.
- Sale response field: `## Creating Installments > ### Response`, raw lines 100–105.
- Immediate-versus-later settlement, authorization-expiration qualification, adjusted-amount ceiling and repeated per-installment minimum: `## Settling Installment Transactions`, raw lines 108–132.
- Settlement response's count, total amount and installment ID/amount array: settlement `### Response`, raw lines 137–146.
- Refund request and response data: `## Refunding Installments`, raw lines 151–175.
- Chargeback adjustment and `adjustmentReason`: `## Chargebacks`, raw lines 180–182.
- Search API / Control Panel detail inventory and procedures: `## Getting Installment Details`, raw lines 185–218.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Supporting concepts: [[braintree-currencies]], [[braintree-server-sdk]]
- Brazil account-navigation context only: [[source-braintree-articles-br-overview]]

## Raw Sources

- [[raw/braintree/articles/br/transactions/installments-2026-09-16|Braintree Brazil Installments]] - fully read 2026-09-16 snapshot covering card scope, sale and settlement inputs, amount constraints, adjustments and installment-detail retrieval
