---
title: "Braintree Compliance Overview"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/risk-and-security/compliance/overview"
raw_files:
  - "braintree/articles/risk-and-security/compliance/overview-2026-09-16.md"
tags: [braintree, compliance, pci-dss, ofac, bgn, eur]
---

## Overview

This collected Braintree webpage is a compliance orientation for merchants accepting or storing payment methods. It assigns responsibility for applicable government and sanctions requirements to the merchant, routes to separate card-brand, prohibited-transaction, PCI DSS, and ecommerce-disclosure guidance, and includes a dated Bulgarian lev (BGN)-to-euro (EUR) account and processing transition. It is Braintree's captured guidance, not current law, legal advice, merchant-specific account terms, or proof of PCI or other certification.

## Key takeaways

- The page says payment-processing requirements can come from card brands, governing bodies, processors, and private organizations, and warns that noncompliance can lead to fines, account holds, seizure of funds, or legal action. For government rules and financial sanctions, it places responsibility on the merchant to know and follow applicable requirements. Its US-based, internationally transacting example points to OFAC and says compliance is required; that example is not a complete jurisdictional or sanctions analysis.
- For the captured BGN transition, the page states that authorization and settlement would change to EUR from January 1, 2026. It directs a merchant with a BGN merchant account to use an existing EUR merchant account from that date or contact Braintree or its CSM if no EUR account exists.
- The transition details say BGN would be converted at a fixed rate from January 1, 2026 and that a transaction presented in BGN after December 31, 2025 at 23:59 CET would be rejected. For an original transaction billed in BGN, a chargeback dispute must still be submitted in BGN; disputes submitted on or after January 1 are described as converting and settling in EUR, with the response and reconciliation amount in EUR while the original amount remains BGN.
- The article says historical BGN transactions remain displayed in BGN and Control Panel reporting is not impacted. Separately, it states that Braintree will suspend the BGN merchant account on December 15, 2025.
- Card-brand rules cover secure processing and restricted or illegal goods and services, with restrictions varying by merchant location and Braintree integration. The article says PCI DSS applies to businesses that handle, process, or store credit cards and requires annual action. It also says certain business details and disclosures must be visible on merchant websites, mobile apps, invoices, and contracts for card-brand consumer-protection and cardholder-rights rules, and that Braintree reviews those platforms for the necessary information.

> [!warning] Dated BGN transition statements
> The snapshot gives two different operational dates: BGN merchant-account suspension on December 15, 2025, and rejection of BGN-presented transactions only after December 31, 2025 at 23:59 CET. It does not explain account or transaction behavior between those dates. Preserve both statements and confirm current account-specific handling with Braintree rather than treating this snapshot as proof of present operability.

> [!warning] Authority boundary
> This Braintree page summarizes obligations and links to more detailed guidance. It does not establish current law, a complete jurisdiction or restricted-goods analysis, merchant eligibility, successful account conversion, or compliance certification.

## Detail locators

- General compliance sources, possible consequences, and processor-help framing: opening paragraph, raw line 16.
- Merchant responsibility and US/international OFAC example: `## Government and regulatory compliance`, raw lines 19-25.
- BGN-to-EUR effective date and authorization/settlement statement: `### Bulgarian Lev (BGN) Currency Transition to Euro (EUR)`, raw lines 28-30.
- EUR merchant-account direction: `#### Merchant Account Requirements`, raw lines 33-35.
- Fixed-rate conversion and BGN rejection cutoff: `##### Currency Conversion`, raw lines 38-42.
- BGN chargeback submission, conversion, response, and reconciliation treatment: `##### Chargebacks`, raw lines 45-54.
- Reporting continuity and historical transaction display: `##### Reporting`, raw lines 57-61.
- BGN merchant-account suspension date: `##### Account Suspension`, raw lines 64-66.
- Card-brand requirements, restricted goods, regional/integration variation, and legal-policy routes: `## Card brand compliance`, raw lines 74-80.
- PCI DSS applicability and annual-action statement: `## PCI compliance`, raw lines 83-87.
- Ecommerce disclosure surfaces and Braintree review statement: `## Ecommerce website compliance`, raw lines 90-94.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Parent risk-and-security route: [[source-braintree-articles-risk-and-security-overview]]

## Related raw documentation

- [[raw/braintree/articles/risk-and-security/compliance/prohibited-transactions-2026-09-16|Braintree Prohibited Transactions]] - linked navigation; not read as factual evidence for this entry
- [[raw/braintree/articles/risk-and-security/compliance/network-compliance-2026-09-16|Braintree Network Compliance]] - linked navigation; not read as factual evidence for this entry
- [[raw/braintree/articles/risk-and-security/compliance/pci-compliance-2026-09-16|Braintree PCI Compliance]] - linked navigation; not read as factual evidence for this entry
- [[raw/braintree/articles/risk-and-security/compliance/ecommerce-website-requirements-2026-09-16|Braintree Ecommerce Website Requirements]] - linked navigation; not read as factual evidence for this entry

## Raw Sources

- [[raw/braintree/articles/risk-and-security/compliance/overview-2026-09-16|Braintree Compliance Overview]] - complete collected snapshot for merchant responsibility, compliance categories, and the dated BGN-to-EUR account and processing transition
