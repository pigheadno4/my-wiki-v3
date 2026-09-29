---
title: "Braintree Kount Custom"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/fraud-tools/premium/kount-custom"
raw_files:
  - "braintree/articles/guides/fraud-tools/premium/kount-custom-2026-09-16.md"
tags: [braintree, kount-custom, fraud-tools, risk-decisions, fraud-management]
---

## Overview

This collected Braintree guide documents the Kount Custom integration, including the decision handoff between Kount and Braintree, fixed gateway actions, timeout and discrepancy boundaries, and the division of support responsibilities. The page says Kount Custom is no longer offered to new merchants and points those merchants to Fraud Protection Advanced; that statement is page-scoped evidence from the collected snapshot, not verification of current product support or eligibility.

## Key takeaways

- When a transaction is created, Braintree sends its information to Kount and waits for a risk decision within a small communication window. Braintree then either sends the transaction to the processor or gateway rejects it according to Kount's decision.
- Kount Custom account rules influence Kount's decisions, while the page says Braintree's action for each named decision cannot be changed. **Decline** is gateway rejected; **Approve**, **Review**, and **Escalate** are sent to the processor, while **Not Evaluated** is sent to the processor by default. Sending a transaction to the processor is not evidence of processor approval or settlement.
- Braintree treats the decision as final when its communication window closes and does not re-evaluate the transaction for risk. Kount may continue evaluating it, so the Braintree gateway can remain **Not Evaluated** while the Kount Agent Web Console later shows a different final decision.
- A timeout or an evaluation error can produce **Not Evaluated**. The page documents a configurable gateway rejection only for transactions that are **Not Evaluated** because of a timeout; it does not state the same option for evaluation errors.
- The guide routes transaction scores, fraud rules, Kount reporting, the Kount Agent Web Console and Kount user-defined fields to a Kount Account Manager. It routes device-data issues, Braintree custom-field mapping and integration issues to Braintree.

## Integration and decision boundaries

> [!warning] Collected Kount Custom evidence
> Keep this Kount Custom integration distinct from Braintree-branded Fraud Protection and Fraud Protection Advanced products. The 2026-09-16 collection and the page's referral to Fraud Protection Advanced do not establish current availability, migration, feature equivalence or eligibility for any product.

The page's risk-decision table and accompanying explanation are the authority for the named Kount-to-Braintree mappings. The exact UDF setup procedure, required corresponding Braintree custom-field relationship, fraud-prefix rules, payment-method UDF table and troubleshooting note remain in the raw page rather than being reproduced here.

## Detail locators

- New-merchant availability statement and navigation to Fraud Protection Advanced: `# Kount Custom > **AVAILABILITY**`, lines 17-18.
- Braintree-to-Kount transaction handoff, communication window and no-re-evaluation warning: `### Braintree and Kount interaction`, lines 23-31.
- Named Kount decisions, fixed Braintree actions, Escalate rendering and merchant influence through Kount rules: `### Risk decisions`, lines 36-50.
- **Not Evaluated** causes and timeout-specific rejection configuration: `#### Not Evaluated transactions`, lines 53-61.
- Persistent Braintree-versus-Kount decision discrepancy after the communication window: `#### Risk decision discrepancies`, lines 64-68.
- UDF purpose, corresponding custom-field prerequisite, exact prefix setup and troubleshooting: `### User defined fields`, lines 71-93.
- Automatically passed payment-method UDF reference table: `#### Payment method UDFs`, lines 98-105.
- Kount-versus-Braintree support responsibility split: `### Getting help`, lines 108-124.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-kount-custom]]

## Raw Sources

- [[raw/braintree/articles/guides/fraud-tools/premium/kount-custom-2026-09-16|Braintree Kount Custom guide]] - complete collected page covering availability, Kount-to-Braintree risk decisions, decision finality, discrepancies, UDF integration and support responsibilities

## Related raw API references

- [[raw/braintree/articles/guides/fraud-tools/premium/fraud-protection-advanced-2026-09-16|Braintree Fraud Protection Advanced guide]] - navigation-only related collected page; not factual evidence for this source
