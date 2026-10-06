---
title: "Braintree Fall 2023 Visa and Mastercard Network Updates"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/risk-and-security/compliance/network-updates/2023/f-2023-all"
raw_files:
  - "braintree/articles/risk-and-security/compliance/network-updates/2023/f-2023-all-2026-09-16.md"
tags: [braintree, network-updates, visa, mastercard, fees, compliance, historical-snapshot]
---

## Overview

This [[braintree|Braintree]] article is a historical release guide collecting Visa and Mastercard fee, mandate, and feature changes labeled as Fall 2023. Where stated, it identifies network, market, effective date, account or transaction condition, and merchant action. Despite the title, the body says Braintree identified key updates for Spring 2023 and says the information was accurate as of March 31, 2023, subject to change, and potentially inapplicable to some merchants or transactions.

> [!warning]
> Treat this as a dated Braintree-hosted snapshot, not current law, current Visa or Mastercard policy, proof of account applicability, or proof of merchant compliance. The URL path is routing metadata, not date authority; use the dates stated in the body and preserve its internal conflicts.

## Key takeaways

- Visa's collected updates include a Europe-scoped Secure Credential Framework fee (all European countries except Turkey and France) for domestic and interregional ecommerce PAN-approved authorizations processed without Visa EMV Payment Tokens or Visa Secure, a US Digital Commerce Services Fee, region-specific Visa Digital Credential Updater pricing, US and interregional interchange changes, an APAC-excluding-Japan account-verification fee revision, regional Processing Integrity fees, and a cross-border fee increase for listed APAC markets.
- For the Secure Credential Framework item, the page says merchants can avoid the described fee by passing transactions with tokens or using 3DS. For Visa Digital Credential Updater, Braintree network-tokenization merchants are described as automatically enrolled; opting out can leave a token unusable after its PAN changes and can increase declines and cart abandonment.
- For Visa Processing Integrity, the page tells merchants to authorize only valid transactions, reverse or cancel quickly, and clear timely with relevant authorization data. It associates authorization/clearing mismatches and unmatched settlement records with named fees and states a $0.05 per-transaction charge when processing-integrity issues exist. Dates vary by EU, CEMEA, Canada, and APAC.
- Mastercard's collected updates include a US card-not-present preauthorization fee, a US excessive-authorization-retry fee after more than 35 attempts in 30 days, regional recurring-CNP Authorization Optimizer fees tied to insufficient-funds responses and Merchant Advice Codes, an APAC optimizer rule with a country list, and global MAC 40 and 41 signals for non-reloadable prepaid and single-use virtual cards. In the separate US/Canada/Europe recurring-CNP Authorization Optimizer section, the page says the fee applies whether or not the merchant uses the MAC; that statement does not describe the APAC optimizer rule. MAC 40 and 41 themselves have no associated fee.
- Preserve source conflicts rather than normalizing them: the excessive-retry prose starts the $0.15 fee on November 1, 2023, while its table shows January 1, 2023; the US Authorization Optimizer prose says October 9, 2023, while its table says October 1; and the APAC optimizer paragraph first lists decline code 82 but later prints 832 in the fee combination.

## Detail locators

- Release context, snapshot disclaimer, and at-a-glance network/market table: raw lines 17-45.
- Visa Secure Credential Framework, Digital Commerce Services Fee, and Visa Account Updater Suite pricing: raw lines 51-89.
- Visa US interchange and interregional structure/rate changes, including detailed rate tables: raw lines 92-478.
- Visa APAC account-verification fee revision and market table: raw lines 481-529.
- Visa Processing Integrity regions, merchant actions, fee conditions, and amount: raw lines 532-553.
- Visa sales and ATM manual-cash cross-border pricing for Australia, Singapore, Hong Kong/Macau, and Malaysia: raw lines 556-572.
- Mastercard US preauthorization and excessive-retry fees, including the prose/table date conflict: raw lines 578-596.
- Mastercard recurring-CNP Authorization Optimizer markets, insufficient-funds condition, fees, MAC 24-30 retry intervals, and use-independent fee: raw lines 599-632.
- Mastercard APAC Authorization Optimizer condition, fee, code inconsistency, and country scope: raw lines 637-647.
- Mastercard global MAC 40 and 41 meanings, no-fee statement, and optional customer/retry uses: raw lines 650-664.

## Related

- [[braintree-payment-platform]] - provider-level context and reciprocal source route

## Raw Sources

- [[raw/braintree/articles/risk-and-security/compliance/network-updates/2023/f-2023-all-2026-09-16|Braintree Fall 2023 network updates raw snapshot]]
