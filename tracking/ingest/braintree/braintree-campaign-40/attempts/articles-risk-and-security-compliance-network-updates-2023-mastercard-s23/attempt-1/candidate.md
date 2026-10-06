---
title: "Braintree Mastercard Spring 2023 Network Updates"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/risk-and-security/compliance/network-updates/2023/mastercard-s23"
raw_files:
  - "braintree/articles/risk-and-security/compliance/network-updates/2023/mastercard-s23-2026-09-16.md"
tags: [braintree, mastercard, network-updates, fees, mandates, historical-snapshot]
---

## Overview

This collected [[braintree|Braintree]] webpage, titled "Mastercard Networks," records four Mastercard items associated with Spring 2023: a Canada card-not-present fee, an APAC commercial large-ticket interchange program, global service-location data fields, and a Europe final-authorization clearing deadline. Treat it as a historical Braintree-hosted notice for [[braintree-payment-platform]], not current Mastercard policy or law, a merchant-specific fee schedule, account applicability evidence, compliance proof, or proof that a fee was assessed.

## Key takeaways

- For Canada, the page says Mastercard would introduce the Digital Enablement Fee on March 13, 2023 and retire certain existing card-not-present fees. It states a 0.02% rate on all card-not-present authorizations, with a $0.02 USD minimum and $0.20 USD maximum per transaction.
- For APAC, the page describes a lower 0.325% commercial large-ticket cross-border interchange rate that may reduce acceptance cost. Eligibility is cumulative, not alternative: the transaction must exceed $10,000 USD, be card-not-present, be invoiced and settled with Mastercard in USD, be non-travel-and-entertainment spend, be cross-border and intraregional Asia/Pacific, have a non-Korean issuer country, and be accepted by a B2B acceptance enabler registered in Mastercard's Business Payment Aggregator Program. The page defines the BPA in this context as merchant of record accepting card transactions on behalf of an end supplier; it separately says the BIN may be in any currency.
- For the global transaction-data mandate, the page says new service-location fields were planned for clearing messages in April 2023 and authorization messages in June 2023. It describes the item as information about a future update and says merchants were not expected to be ready yet; because the captured applicability phrase is grammatically unclear, this entry does not infer which merchants would ultimately have to supply the details.
- For Europe, the page says that beginning May 22, 2023, a merchant processing there had to submit the clearing record for a transaction authorized as a final authorization within three calendar days of approval, down from seven. It explicitly excludes estimated and incremental authorization transactions.

> [!warning] Historical and applicability boundary
> The dates, rates, regions, actor/action statements, and conditions above belong to this collected Braintree page. Confirm current network rules, account applicability, pricing, and required action through applicable current Mastercard and Braintree channels. The broader combined Spring 2023 release page overlaps this child page but is not unconditional authority for Mastercard-only claims here.

> [!warning] Captured wording boundary
> The service-location section says the mandate would require "merchants that move" to provide more detailed location information. That wording is incomplete or unclear as captured, so this entry preserves the stated future-information/readiness status and does not reconstruct the affected merchant class.

## Detail locators

- Canada Digital Enablement Fee date, retired-fee statement, card-not-present scope, rate, minimum, maximum, and fee descriptors: `## What is the new Digital Enablement Fee update?`, raw lines 17-29.
- APAC program purpose, rate descriptor, rate, and cumulative merchant/transaction eligibility list: `## What is the new interchange program for APAC fee change?`, raw lines 32-52.
- Global service-location fields, message types, stated months, unclear merchant phrase, readiness qualification, and appendix link: `## What is the Standardization of transaction data elements mandate?`, raw lines 57-65. The linked appendix is navigation only unless independently read.
- Europe final-authorization clearing deadline, prior timeline, effective date, and estimated/incremental exclusion: `## What are the Revised Standards for Europe Region Final Authorization Clearing Submission Acceleration?`, raw lines 68-72.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Broader combined release snapshot: [[source-braintree-articles-risk-and-security-compliance-network-updates-2023-s-2023-all]]

## Related raw API references

- [[raw/braintree/articles/risk-and-security/compliance/network-updates/appendix-2026-09-16|Braintree network-updates appendix]] - linked by the service-location section; navigation only and not read as evidence for this entry

## Raw Sources

- [[raw/braintree/articles/risk-and-security/compliance/network-updates/2023/mastercard-s23-2026-09-16|Braintree Mastercard Spring 2023 network updates]] - complete collected historical page with the stated regions, dates, actors, actions, transaction conditions, fee table, readiness wording, and clearing exception
