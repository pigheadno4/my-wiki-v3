---
title: "Braintree Chargeback Reason Codes"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/risk-and-security/chargebacks-retrievals/chargeback-reason-codes"
raw_files:
  - "braintree/articles/risk-and-security/chargebacks-retrievals/chargeback-reason-codes-2026-09-16.md"
tags: [braintree, disputes, chargebacks, retrievals, reason-codes, card-networks]
---

## Overview

This collected [[braintree]] article is a lookup reference for reason codes Braintree says accompany received credit-card disputes. It organizes the captured mappings by card brand and dispute type, with separate JCB retrieval and chargeback tables.

Its central use is interpreting the codes surfaced to merchants in this Braintree snapshot. It is not independent card-network authority, an exhaustive current network-rule inventory, or evidence for Automated Clearing House (ACH) return codes.

## Key takeaways

- The article groups reason-code mappings for American Express, Diners, Discover, Elo, Hipercard, JCB, Maestro, Mastercard, UnionPay and Visa. Use the table locators below for the exact code-to-reason or code-to-description rows rather than copying the inventory into this retrieval page.
- Most brand tables map a code to a normalized reason label such as fraud, duplicate, credit not processed or product not received. The Diners and JCB tables instead provide descriptions, and JCB divides retrieval reason codes from chargeback reason codes.
- ACH return codes are outside this page's scope; the article routes readers to a separate ACH support article. That linked article was not read as evidence for this entry.
- Visa decimal-form reason codes are represented in this page as four characters with a zero because the reason-code representation does not support decimals; the article gives `10.4 = 1040` as its example.

> [!warning] Snapshot and interpretation boundary
> The article says the list was generated on 2025-09-22 from chargeback reason codes then actively received and surfaced to merchants, is subject to change, and may omit currently known codes. It also says codes can vary by processing region or payment network. Treat the tables as a captured Braintree merchant-surfacing reference, not independent current network rules or a guarantee that a code applies to a particular account, region or dispute.

## Detail locators

- Document purpose, card-brand organization, regional/network qualification, list-generation date and non-exhaustiveness: raw lines 13-21.
- Separate ACH return-code route: raw line 23.
- American Express mappings: `## American Express`, raw lines 26-55.
- Diners descriptions: `## Diners`, raw lines 60-123.
- Discover, Elo and Hipercard mappings: `## Discover` through `## Hipercard`, raw lines 126-164.
- JCB retrieval and chargeback descriptions: `## JCB`, raw lines 167-293.
- Maestro and Mastercard mappings: `## Maestro` through `## Mastercard`, raw lines 296-337.
- UnionPay mappings: `## UnionPay`, raw lines 340-345.
- Visa decimal-format warning and mappings: `## Visa`, raw lines 348-401.

## Related

- Company: [[braintree]]
- Main concept: [[disputes]]

## Related raw API references

- [[raw/braintree/articles/guides/payment-methods/ach-2026-09-16|Braintree ACH support article]] - linked navigation for ACH return codes; not read as factual evidence for this entry

## Raw Sources

- [[raw/braintree/articles/risk-and-security/chargebacks-retrievals/chargeback-reason-codes-2026-09-16|Braintree Chargeback Reason Codes]] - complete collected snapshot containing the card-brand tables, date and variability qualifications, and Visa representation warning
