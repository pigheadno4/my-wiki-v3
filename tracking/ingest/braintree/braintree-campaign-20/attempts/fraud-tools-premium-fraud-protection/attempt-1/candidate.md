---
title: "Braintree Fraud Protection"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/fraud-tools/premium/fraud-protection"
raw_files:
  - "braintree/articles/guides/fraud-tools/premium/fraud-protection-2026-09-16.md"
tags: [braintree, fraud-protection, premium-fraud-management, risk-decisions, card-transactions]
---

## Overview

This collected Braintree article documents the named **Fraud Protection** product, one of Braintree's Premium Fraud Management Tools. The page describes machine-learning evaluation of card transactions using customer-device and transaction data, with fraud scores intended to help merchants reject transactions highly suspected of fraud while avoiding over-blocking likely good transactions.

This is a retrieval route for Fraud Protection itself. It does not establish the capabilities, eligibility or decision states of **Fraud Protection Advanced**, other premium products, Basic Fraud Tools, 3D Secure, chargeback-protection products or Control Panel security features.

## Key takeaways

- The page says merchants can view and tune fraud filters through what the collected snapshot calls a **new** Fraud Protection merchant interface. It does not provide an eligibility rule, account-enablement procedure, fee statement or current-support guarantee.
- For a new transaction, Fraud Protection sends transaction information to PayPal's internal Fraud Protection service and uses adaptive rules and fraud filters to reach a risk decision. The documented gateway mapping sends **Approve** decisions to the processor and gateway-rejects **Decline** decisions. Sending a transaction to the processor is not evidence of processor approval or settlement.
- The page states that Transaction Risk Filter is enabled by default and rejects transactions whose risk score exceeds the configured score. It describes 1000 as the riskiest score and 0 as the least risky; exact filter tuning and the Control Panel lookup procedure remain in the raw locators.
- The page routes merchants to the Transaction Detail page for a transaction's Fraud Protection risk decision and says that **Device Data Captured: True** in the Premium Fraud Management Tools Information section indicates that Premium Fraud Management Tools are functioning. This page-scoped diagnostic is not proof of current product availability or of a successful payment outcome.

> [!warning] Product and outcome boundary
> Keep the product explicitly titled **Fraud Protection** distinct from **Fraud Protection Advanced** and from other fraud, authentication, chargeback and account-security tools. The collected page documents only **Approve** and **Decline** risk decisions for this product. Treat the 2026-09-16 snapshot as collected evidence, not proof of current support, merchant eligibility, enablement, processor approval or settlement.

## Detail locators

- Named product identity, card-transaction purpose, machine-learning use, input categories and stated fraud-score objective: `# Fraud Protection`, lines 14-18.
- Fraud-filter visibility and tuning through the named merchant interface: `# Fraud Protection`, line 20.
- New-transaction analysis, adaptive rules and filters, gateway decision mapping, default Transaction Risk Filter and score direction: `## Risk decisions`, lines 23-32.
- Transaction Detail lookup procedure: `## Risk decisions`, lines 34-42.
- Premium Fraud Management Tools device-data diagnostic: `## Risk decisions > **NOTE**`, lines 45-46.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-fraud-protection]]
- Administrative concept: [[braintree-control-panel]]
- Distinct product: [[braintree-fraud-protection-advanced]]

## Related raw API references

- [[raw/braintree/articles/guides/fraud-tools/premium/overview-2026-09-16|Braintree Premium Fraud Management Tools overview]] - linked navigation-only authority; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/articles/guides/fraud-tools/premium/fraud-protection-2026-09-16|Braintree Fraud Protection article]] - complete collected page covering the named product's purpose, merchant-interface statement, risk-decision flow, default filter and Control Panel diagnostic
