---
title: "Stripe: Disputed PayPal Payments"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-paypal-disputes-2025.md"
tags: [stripe, wallets, paypal, disputes, chargebacks, evidence, testing]
---

## Summary

Explains how PayPal dispute management works through Stripe — the process, resolution, fees, multiple disputes per payment, and test scenarios. PayPal disputes are low-risk due to mandatory customer authentication, but buyers have a 180-day window to dispute.

## Key Details

**Dispute window**: 180 calendar days from purchase (same as refund window). Customers can file via PayPal or via their bank/card issuer.

**Notification channels**: email, Stripe Dashboard, `charge.dispute.created` webhook, push notification.

**Direct customer contact**: PayPal may offer direct resolution between merchant and customer; Stripe doesn't support this — must use PayPal directly to contact customer.

**Evidence submission**: 2–19 calendar days depending on dispute category. PayPal decision: within 30 calendar days of evidence submission.

**Appeals**: PayPal allows appeals on lost disputes; Stripe doesn't support appeals — must use PayPal directly. Dispute stays open on Stripe until final PayPal resolution.

**Fees**: PayPal may charge dispute fees (terms set by PayPal). Stripe charges no additional fees for PayPal disputes.

**Multiple disputes per payment**: Category change on PayPal reopens the original dispute on PayPal but creates a new dispute on Stripe. Result: multiple Stripe disputes for one payment, all linked to the same PayPal dispute. Edge case: two same-category disputes if customer loses on PayPal then re-files with their bank.

## Test Scenarios (7 email patterns)

| Email pattern | Dispute category |
| --- | --- |
| `.*dispute_credit_not_processed@.*` | Credit not processed |
| `.*dispute_duplicate@.*` | Duplicate charge |
| `.*dispute_fraudulent@.*` | Fraudulent transaction |
| `.*dispute_general@.*` | Uncategorized |
| `.*dispute_not_received@.*` | Product not received |
| `.*dispute_product_unacceptable@.*` | Product unacceptable |
| `.*dispute_subscription_cancelled@.*` | Subscription cancelled |

Test resolution: pass `winning_evidence` or `losing_evidence` as `uncategorized_text` in evidence submission (API or Dashboard Additional information field).

## Raw Sources

- [[stripe-paypal-disputes-2025]] — verbatim dispute management guide (102 lines); no fixes needed
