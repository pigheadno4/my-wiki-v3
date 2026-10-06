---
title: "Braintree Network Updates Appendix"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/risk-and-security/compliance/network-updates/appendix"
raw_files:
  - "braintree/articles/risk-and-security/compliance/network-updates/appendix-2026-09-16.md"
tags: [braintree, mastercard, network-updates, compliance, transaction-data]
---

## Overview

This collected Braintree-hosted appendix is a companion table for Mastercard transaction-data-element standardization. It maps transaction types to acceptor and service-location representations, then separates authorization from settlement fields and identifies whether values come from Masterfile, System, the merchant through a new specification field, or are marked N/A. It is historical documentation for [[braintree]] and [[braintree-payment-platform]], not current Mastercard policy or proof of merchant-account applicability.

## Key takeaways

- The transaction-type table covers how acceptor names, business or processing addresses, and service locations are represented for physical, remote and service-specific transaction patterns. Use the exact raw table rather than treating one row as a general rule.
- In the authorization table, most acceptor details come from Masterfile, Version Code comes from System, and four service-location fields come from the merchant through a new specification field. The notes mark some fields optional and say Fiserv would not create or send them; the page does not define the applicable processor or account scope, so those statements should not be transferred to other setups.
- In the settlement table, acceptor fields come from Masterfile while service-location city, subdivision, country and postal code come from the merchant through a new specification field, conditionally when the transaction location differs from the merchant location at the corresponding geographic level.
- The linked Spring 2023 release guide identifies the mandate as Mastercard / Global and describes April 2023 clearing fields and June 2023 authorization fields. The appendix body itself gives no effective period, region, readiness state or merchant-account eligibility, so that parent-guide context must not be presented as current policy or as an appendix-stated account rule.

> [!warning] Captured wording and applicability
> Several table notes are grammatically irregular: authorization's Service Location City Name row compares a State to the merchant-location city, while other rows use similarly incomplete "other than the city the merchant location" wording. Preserve the exact table when implementing or interpreting fields rather than silently normalizing these conditions. The appendix also does not establish successful enablement, authorization, clearing or settlement for any transaction.

## Detail locators

- Transaction-type to acceptor-name, address and service-location mapping: `### Standardization of transaction data elements mandate`, raw lines 17-33.
- Authorization field ownership, optional-field/Fiserv notes and conditional merchant-supplied service-location fields: `### Mastercard's Standardization for authorization`, raw lines 36-57.
- Settlement field ownership and conditional merchant-supplied service-location fields: `### Mastercard's Standardization for settlement`, raw lines 60-77.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Historical parent guide: [[source-braintree-articles-risk-and-security-compliance-network-updates-2023-s-2023-all]] - supplies the linked Mastercard / Global and April/June 2023 context; its snapshot qualifications remain controlling.

## Raw Sources

- [[raw/braintree/articles/risk-and-security/compliance/network-updates/appendix-2026-09-16|Braintree Network Updates Appendix]] - complete collected appendix tables for transaction-type representation and Mastercard authorization/settlement field ownership
