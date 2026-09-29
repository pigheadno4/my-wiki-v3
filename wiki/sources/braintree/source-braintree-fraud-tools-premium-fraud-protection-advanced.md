---
title: "Braintree Fraud Protection Advanced"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/fraud-tools/premium/fraud-protection-advanced"
raw_files:
  - "braintree/articles/guides/fraud-tools/premium/fraud-protection-advanced-2026-09-16.md"
tags: [braintree, fraud-protection-advanced, fraud-management, risk-decisions, card-transactions]
---

## Overview

This collected Braintree article describes Fraud Protection Advanced as a Premium Fraud Management Tool that uses machine learning and device and transaction data to evaluate card transactions. Its stated purpose is to provide fraud scores that help merchants reject transactions highly suspected of fraud while avoiding over-blocking likely good transactions.

The page is a retrieval route for this specific Braintree product's merchant eligibility, configurable rules and review flow, and gateway actions for its risk decisions. It does not establish current availability or eligibility, identify an exact "latest SDK" version, or supply evidence for sibling fraud products.

## Key takeaways

- The page limits availability to eligible merchants using Braintree Direct and the latest SDKs, without naming an SDK or version. Its feature table also states that Fraud Protection Advanced has additional fees, supports merchant-created customizable rules, provides detailed risk data, and includes transaction review and webhooks.
- For suspicious payments needing human judgment, a merchant can create a filter with the decision label **Review**. The documented review flow lets the merchant decide whether the payment is fraudulent or legitimate, and the page links to webhooks for notifications after a reviewed transaction is approved or rejected.
- For a new transaction, Fraud Protection Advanced sends information to PayPal's internal fraud management service and reaches a risk decision using adaptive rules and fraud filters. The Braintree gateway sends **Approve** and **Review** decisions to the processor, gateway-rejects **Decline**, and sends **Not Evaluated** to the processor by default.
- The default Transaction Risk Filter rejects transactions whose risk score is above the configured threshold; the page describes 1000 as riskiest and 0 as least risky. A transaction receives **Not Evaluated** when the risk-decision delivery exceeds an internal threshold and times out or when evaluation errors.

> [!warning] Collected eligibility and decision boundary
> Treat the Braintree Direct eligibility, unspecified "latest SDKs" requirement, fees, risk-decision mapping, default filter behavior, and **Not Evaluated** fallback as page-scoped collected evidence. The 2026-09-16 snapshot is not proof of current support, account enablement, an exact SDK version, processor approval, successful settlement, or the behavior of other Braintree or PayPal fraud products.

## Detail locators

- Product identity, card-transaction purpose, machine-learning use and stated score objective: `# Fraud Protection Advanced`, lines 14-18.
- Configurable-rule, code-change, Braintree Direct/latest-SDK, risk-data, review/webhook and fee summary: `## Premium Fraud Management Tools`, lines 26-35.
- Additional capability categories: `## How Fraud Protection Advanced Works`, lines 38-50.
- Dashboard custom-field types and configuration procedure: `### Custom Fields`, lines 53-84.
- Manual-review designation, decision purpose and reviewed-transaction webhook route: `### Review queue`, lines 87-91.
- Collected payment-method compatibility list: `### Payment methods supported`, lines 94-101.
- Risk-decision processing, gateway action mapping and default Transaction Risk Filter scoring behavior: `## Risk decisions`, lines 104-115.
- Control Panel decision lookup procedure: `## Risk decisions`, lines 117-125.
- **Not Evaluated** timeout/error conditions and the page's Device Data Captured diagnostic: `### Not Evaluated transactions`, lines 128-138.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-fraud-protection-advanced]]

## Related raw API references

- [[raw/braintree/articles/guides/fraud-tools/premium/overview-2026-09-16|Braintree Premium Fraud Management Tools overview]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/general/webhooks/fraud-protection/node-2026-09-16|Braintree Node.js fraud-protection webhook reference]] - navigation-only concrete SDK fallback for the linked webhook topic; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/articles/guides/fraud-tools/premium/fraud-protection-advanced-2026-09-16|Braintree Fraud Protection Advanced article]] - complete collected page covering product purpose, eligibility, features, review flow, payment-method scope, risk decisions and Not Evaluated conditions
