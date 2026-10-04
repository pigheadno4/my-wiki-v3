---
title: "Braintree Fraud Protection"
type: concept
category: technology
tags: [braintree, fraud-protection, premium-fraud-management, risk-decisions, card-transactions]
---

## Braintree Fraud Protection

Braintree's collected guide describes the product explicitly titled **Fraud Protection** as a Premium Fraud Management Tool that applies machine learning to customer-device and transaction data to evaluate card transactions. Its stated purpose is to provide fraud scores that help merchants reject transactions highly suspected of fraud while reducing over-blocking of likely good transactions. [[source-braintree-fraud-tools-premium-fraud-protection]]

## Decision flow

For a new transaction, the guide says Fraud Protection sends transaction information to PayPal's internal Fraud Protection service and uses adaptive rules and fraud filters to reach a risk decision. The documented gateway mapping sends **Approve** to the processor and gateway-rejects **Decline**. Transaction Risk Filter is described as enabled by default and rejecting scores above its configured threshold, with 1000 identified as riskiest and 0 as least risky. Sending a transaction to the processor does not establish processor approval or settlement. [[source-braintree-fraud-tools-premium-fraud-protection]]

## Scope boundary

This concept covers the named **Fraud Protection** product in the collected page. Keep it distinct from [[braintree-fraud-protection-advanced]], Basic Fraud Tools, 3D Secure, chargeback-protection products and Control Panel security. The page does not establish current support, merchant eligibility, account enablement, fees or any risk-decision states beyond **Approve** and **Decline**.

## Sources
- [[source-braintree-premium-fraud-management-tools-server-side-node]] - Node.js server-side device-data forwarding and risk-response route, with decision reasons qualified to Fraud Protection and no authorization or settlement inference

- [[source-braintree-fraud-tools-premium-fraud-protection]] - named product purpose, fraud-filter interface, approve/decline gateway mapping, default Transaction Risk Filter and transaction-detail diagnostic
