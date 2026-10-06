---
title: "Braintree Prohibited Transactions"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/risk-and-security/compliance/prohibited-transactions"
raw_files:
  - "braintree/articles/risk-and-security/compliance/prohibited-transactions-2026-09-16.md"
tags: [braintree, compliance, prohibited-transactions, sanctions, banking]
---

## Overview

This collected Braintree webpage describes prohibited-transaction restrictions associated with regulations and financial sanctions, including restrictions involving certain countries, people, entities, organizations, and banks. It outlines possible processing-bank and funding-bank outcomes and directs merchants to applicable government sources because restrictions depend on the business and counterparty context and can change. This is historical Braintree guidance, not current law, legal advice, a complete prohibited-party or country list, merchant approval, or proof of an individual authorization, decline, settlement block, or notification.

## Key takeaways

- The page attributes prohibitions to regulations and financial sanctions imposed by governing bodies and scopes affected transactions to certain restricted or high-risk countries, individuals, corporate entities, and organizations. It does not provide an exhaustive list or establish that any named merchant or counterparty is permitted or prohibited.
- It says restrictions can also apply to banks linked to prohibited sources or countries. A credit card may fail to process when its BIN indicates issuance from a high-risk region or bank; this possibility is not a guaranteed decision rule or an individual transaction outcome.
- In the page's described general pattern, the processing bank declines most prohibited transactions. If the processing bank authorizes one, the funding bank will typically prevent settlement and Braintree says it will notify the merchant. Authorization therefore does not establish settlement, while the modal wording does not guarantee a particular bank outcome or notification.
- Restrictions vary with the business's country of domicile and its counterparties and may change as laws and political conditions evolve. The page directs merchants to applicable government sources, using US OFAC resources only as an example; the snapshot is not current or complete legal authority for any jurisdiction.

> [!warning] Snapshot and decision boundary
> Treat this captured Braintree guidance as a historical retrieval route. Confirm current restrictions with applicable official authorities and obtain account-specific guidance where needed; this page does not establish current law, merchant eligibility or approval, or a transaction's authorization, settlement, or funding result.

## Detail locators

- Restricted or high-risk countries, people, entities, and organizations: raw line 16.
- Bank restrictions and the possible BIN-linked processing outcome: raw line 18.
- Processing-bank decline, rare authorization, funding-bank settlement prevention, and notification: raw line 20.
- Business-domicile and counterparty variation, fluidity, and government-source direction: raw line 22.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Compliance orientation: [[source-braintree-articles-risk-and-security-compliance-overview]]

## Raw Sources

- [[raw/braintree/articles/risk-and-security/compliance/prohibited-transactions-2026-09-16|Braintree Prohibited Transactions]] - complete collected snapshot for prohibited-transaction scope, possible bank outcomes, and the jurisdiction- and time-dependent restriction warning
