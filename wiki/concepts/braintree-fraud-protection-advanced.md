---
title: "Braintree Fraud Protection Advanced"
type: concept
category: technology
tags: [braintree, fraud-protection-advanced, fraud-management, risk-decisions, card-transactions]
---

## Braintree Fraud Protection Advanced

Braintree's collected guide describes Fraud Protection Advanced as a Premium Fraud Management Tool that uses machine learning plus customer-device and transaction data to evaluate card transactions. Its stated purpose is to produce fraud scores that help merchants reject transactions highly suspected of fraud while reducing false-positive rejection of likely good transactions. [[source-braintree-fraud-tools-premium-fraud-protection-advanced]]

## Eligibility and decision flow

The guide limits availability to eligible Braintree Direct merchants using the latest SDKs, without identifying a concrete SDK or version, and states that additional fees apply. It documents customizable merchant rules, detailed risk data, transaction review and reviewed-transaction webhooks. For gateway handling, **Approve** and **Review** are sent to the processor, **Decline** is gateway rejected, and **Not Evaluated** is sent to the processor by default. A timeout beyond an internal risk-decision threshold or an evaluation error yields **Not Evaluated**. Treat these statements as collected page-scoped evidence, not proof of current eligibility, enablement, processor approval or settlement. [[source-braintree-fraud-tools-premium-fraud-protection-advanced]]

## Manual review route

A merchant can designate suspicious payments for manual review by creating a filter with the **Review** decision label, then approve or reject a reviewed transaction; the guide links to a separate webhook route for the resulting notification. Exact Dashboard procedures, custom-field settings, payment-method coverage and scoring configuration remain in the source's raw locators.

## Sources

- [[source-braintree-fraud-tools-premium-fraud-protection-advanced]] - product purpose, merchant eligibility, configurable rules, manual review, gateway risk-decision actions and Not Evaluated fallback
