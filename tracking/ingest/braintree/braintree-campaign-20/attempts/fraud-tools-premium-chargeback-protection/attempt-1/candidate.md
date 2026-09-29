---
title: "Braintree Chargeback Protection Tools"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/fraud-tools/premium/chargeback-protection"
raw_files:
  - "braintree/articles/guides/fraud-tools/premium/chargeback-protection-2026-09-16.md"
tags: [braintree, chargeback-protection, fraud-management, disputes, credit-cards, debit-cards]
---

## Overview

This collected Braintree article distinguishes PayPal's **Chargeback Protection tool** from its **Effortless Chargeback Protection tool** for eligible credit- and debit-card transactions. It documents their real-time risk-decision role, conditional chargeback protection, integration and account conditions, a bypass consequence, and page-scoped payment and processor eligibility boundaries.

## Key takeaways

- For the Chargeback Protection tool, PayPal evaluates each credit- or debit-card transaction in real time. The page says PayPal processes a transaction it does not deem fraudulent or high risk and declines one it considers high risk, with no manual review or later re-review of a declined transaction.
- The stated protection is conditional: for an eligible processed transaction, the disputed amount and PayPal Chargeback fees are waived only when a chargeback is received and the merchant supplies required evidence. Evidence requirements can vary by goods or services, and the page asks for delivery or shipment proof when an eligible chargeback arrives.
- Effortless Chargeback Protection is a separately named tool that removes the delivery-confirmation requirement for **eligible fraud chargebacks**. The page does not say that it removes every evidence requirement, covers every transaction or chargeback, or guarantees a favorable dispute outcome.
- Integration requires the mandatory fields in the linked developer guide, and signup can require additional data depending on the business's risk profile. That linked guide is navigation only here and is not evidence for an unlisted field inventory.
- Although the page first says a PayPal decline cannot be overridden, it documents `Options.SkipAdvancedFraudChecking` as a bypass. A merchant using that bypass must still pay for the services and waives the right to indemnification for the chargeback amount and PayPal chargeback fee.
- The page says merchants should have a Braintree business account and says Chargeback Protection is available in the US and Brazil. After enabling either Chargeback Protection tool, a merchant cannot use Fraud Protection tools unless Chargeback Protection is disabled. In supported regions, the page describes both tools as compatible with debit- and credit-card transactions that Braintree should fund and with Braintree's use of Fiserv, American Express and Wells Fargo; this wording does not prove eligibility for a particular merchant or transaction.

> [!warning] Conditional protection and incomplete chargeback-type route
> This page does not establish a general chargeback guarantee. Protection is limited by transaction and chargeback eligibility, required evidence, region, account, funding and processor conditions. It refers to an **Eligible Chargeback Types** section that is not present in the collected raw, so the covered chargeback types cannot be reconstructed from this source. The 2026-09-16 collection date also does not prove current availability, eligibility or support.

## Detail locators

- Named tools, conditional waiver and Effortless delivery-confirmation distinction: `## Overview`, lines 17-23.
- Real-time PayPal decisioning, decline finality and evidence variability: `### Fraud Evaluation and Chargebacks`, lines 26-30.
- Mandatory developer-guide fields and possible additional signup data: `### Integration`, lines 33-35.
- Bypass consequence and Transaction Details labels: `### Transaction statuses`, lines 38-44.
- Dispute notification, evidence-submission routes and proof links: `### Managing chargebacks`, lines 54-79.
- Payment, funding and processor scope: `### Supported payment technologies` through `### Supported processor connections`, lines 82-89.
- Business-account, product-exclusivity and regional eligibility statements: `### Eligibility`, lines 92-97.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-chargeback-protection]]
- Related concept: [[disputes]]

## Related raw API references

- [[raw/braintree/docs/guides/premium-fraud-management-tools/overview-2026-09-16|Braintree Premium Fraud Management Tools developer guide]] - unread navigation-only route linked for mandatory integration fields and evidence submission; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/guides/fraud-tools/premium/chargeback-protection-2026-09-16|Braintree Chargeback protection tools article]] - complete collected page covering the two named tools, decision flow, conditional protection, bypass consequence and eligibility boundaries
