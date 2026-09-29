---
title: "Braintree Kount Custom"
type: concept
category: technology
tags: [braintree, kount-custom, fraud-tools, risk-decisions, fraud-management]
---

## Braintree Kount Custom

Braintree's collected Kount Custom guide describes an integration in which Braintree sends new-transaction information to Kount for a risk decision within a small communication window. Kount Custom account rules influence Kount's decision, and Braintree applies a fixed action for each named decision: **Decline** is gateway rejected; **Approve**, **Review**, and **Escalate** are sent to the processor; **Not Evaluated** is sent to the processor by default. Sending to the processor does not establish processor approval or settlement. [[source-braintree-fraud-tools-premium-kount-custom]]

## Decision finality and discrepancies

When the Braintree-to-Kount communication window closes, Braintree treats its received risk decision as final and does not re-evaluate the transaction for risk. Kount can continue evaluating, so a transaction can remain **Not Evaluated** in Braintree while Kount later displays a different final decision. The guide says a timeout or evaluation error can produce **Not Evaluated**, but documents optional gateway rejection only for the timeout case. [[source-braintree-fraud-tools-premium-kount-custom]]

## Availability and responsibility boundary

The collected page says Kount Custom is no longer offered to new merchants and directs those merchants to Fraud Protection Advanced. Treat this as snapshot-scoped Kount Custom evidence, not proof of current availability, migration, equivalence or eligibility for either product. The guide assigns Kount scores, fraud rules, reporting, the Kount Agent Web Console and UDF questions to a Kount Account Manager, while assigning device-data issues, Braintree custom-field mapping and integration issues to Braintree. [[source-braintree-fraud-tools-premium-kount-custom]]

## Sources

- [[source-braintree-fraud-tools-premium-kount-custom]] - Kount Custom availability statement, Braintree-to-Kount decision handoff, fixed gateway actions, finality and discrepancy limits, and support responsibility split
