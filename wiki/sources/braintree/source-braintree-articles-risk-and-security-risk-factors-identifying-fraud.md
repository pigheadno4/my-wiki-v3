---
title: "Braintree Identifying Fraud Guide"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/risk-and-security/risk-factors/identifying-fraud"
raw_files:
  - "braintree/articles/risk-and-security/risk-factors/identifying-fraud-2026-09-16.md"
tags: [braintree, fraud-risk, transaction-review, carding, chargebacks]
---

## Overview

This collected Braintree risk guide is a manual investigation checklist for merchants assessing whether a transaction may be suspicious. It organizes common indicators across customer identity, billing and shipping addresses, email, IP address, and transaction patterns, then gives conditional next-step guidance. The page explicitly treats its questions as guidelines: an indicator is not proof of fraud, and the guide does not document a gateway risk decision or guarantee that fraud will be detected or prevented.

## Key takeaways

- Identity and contact checks include mismatches or irregularities in the customer name, cardholder identity, address, and email. The page also lists particular email-domain, formatting, country, and geography examples; treat these as snapshot-specific prompts for investigation rather than rules that establish fraud.
- IP review depends on the merchant implementing IP logging on its own web server. The suggested comparisons include prior fraud associated with the IP or geography and distance or mismatch among the IP, customer, billing, and shipping locations.
- Transaction-pattern indicators include unusually high volume in a short period, repeated amounts or card brands, multiple card numbers sharing a BIN, activity outside the merchant's normal demographic, prepaid or gift cards, and different cards sharing one customer name. The page calls concentrated transaction volume a common carding indicator, not a conclusive determination.
- When fraud is suspected, the guide suggests withholding products or services until the merchant feels confident that the transaction is legitimate, contacting the customer, and checking phone or email information. If the customer cannot be contacted or suspicion is confirmed, it suggests a void or refund to reduce the likelihood of chargebacks; that recommendation does not establish that either action will prevent a chargeback.

> [!warning] Indicator and outcome boundary
> The listed characteristics can also occur in legitimate transactions, and the page says fraudulent transactions can still slip through fraud tools. Use these signals to inform investigation, not as proof about a customer or transaction, and use the linked operational documentation for the actual void or refund procedure.

## Detail locators

- Guide purpose, fraud-tool limitation, and explicit guideline qualification: `# Identifying Fraud`, raw lines 14-18.
- Customer-name indicators: `## Customer name`, raw lines 21-26.
- Billing, shipping, geography, and delivery indicators: `## Customer address`, raw lines 29-34.
- Cardholder/email alignment, domain, and random-character indicators: `## Customer email`, raw lines 37-42.
- Merchant-side IP-logging prerequisite and IP/geography comparisons: `## Customer IP address`, raw lines 45-57.
- Transaction-volume, BIN, demographic, card-type, and shared-name indicators: `## Transaction details`, raw lines 60-71.
- Conditional contact, fulfillment, void/refund, and reporting guidance: `## Next steps`, raw lines 76-80.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-fraud-tools]]

## Related raw documentation

- [[raw/braintree/articles/guides/fraud-tools/overview-2026-09-16|Braintree Fraud Tools Overview]] - linked navigation; not read as behavioral evidence for this entry
- [[raw/braintree/articles/control-panel/transactions/bank-identification-numbers-2026-09-16|Braintree Bank Identification Numbers]] - linked navigation; not read as behavioral evidence for this entry
- [[raw/braintree/articles/control-panel/transactions/refunds-voids-credits-2026-09-16|Braintree Refunds, Voids, and Credits]] - linked operational route; not read as procedural evidence for this entry

## Raw Sources

- [[raw/braintree/articles/risk-and-security/risk-factors/identifying-fraud-2026-09-16|Braintree Identifying Fraud guide]] - complete collected snapshot covering manual fraud indicators, the merchant IP-logging prerequisite, guideline qualification, and conditional investigation and void/refund guidance
