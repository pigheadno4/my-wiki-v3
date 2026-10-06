---
title: "Braintree Currencies Reference"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/currencies"
raw_files:
  - "braintree/docs/reference/general/currencies-2026-09-16.md"
tags: [braintree, currencies, settlement, zero-decimal, merchant-accounts]
---

## Overview

This collected Braintree general reference lists currency codes and names described by the page as supported in the Braintree API, marks zero-decimal entries, records a dated Bulgaria BGN-to-EUR transition, and defines Braintree's scheme- and exotic-currency settlement categories. Availability remains conditioned on account setup, company country and possible country-of-transaction restrictions.

## Key takeaways

- The page's API currency list is not an eligibility matrix: it says available currencies differ by account setup and the country where the company is located, and it points to restrictions that may prohibit transactions from particular countries. It does not map availability by merchant, processor, payment method, presentment/settlement combination or transaction region.
- An asterisk marks the entries the page classifies as zero-decimal. The complete code/name table is retained in the raw rather than duplicated here. This Braintree snapshot is not independent ISO currency metadata, card-network authority, or an exchange-rate/FX guarantee.
- The page says that, effective January 1, 2026, EUR replaced BGN for Bulgaria; BGN is no longer supported for authorization or settlement, and integrations using BGN should use EUR for transactions involving Bulgaria.
- In this reference, a scheme currency is made available by the acquirer and/or card schemes for settlement, while an exotic currency is sourced by Braintree rather than provided by the acquirer and/or card schemes for settlement. These definitions describe settlement sourcing; they do not prove that a listed currency is enabled for a particular account, processor or payment method.

> [!warning] Snapshot and qualification boundary
> This is a 2026-09-16 capture of a Braintree-hosted reference. It does not establish current currency support, individual account eligibility, successful authorization or settlement, processor/payment-method coverage, exchange rates, or current ISO/card-network rules. Use the applicable account and payment-method documentation alongside this reference.

## Detail locators

- API-support framing, account setup, company-country and prohibited-transaction qualifications: `# Currencies > NOTE`, lines 16-17.
- Currency code/name entries and zero-decimal asterisk convention: `# Currencies`, lines 20-155.
- Bulgaria BGN-to-EUR authorization and settlement transition: `# Currencies > NOTE`, lines 160-161.
- Scheme-currency definition and table: `##### 1Scheme currency`, lines 166-185.
- Exotic-currency definition and table: `##### 2Exotic currency`, lines 189-198.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-currencies]]
- [[source-braintree-get-started-currencies]] - separate collected guide for presentment and settlement definitions, multi-currency setup, approvals and account integration
- [[source-braintree-auth-multi-currency-node]] - connected-merchant currency creation route with Braintree Auth and payment-method qualifications

## Raw Sources

- [[raw/braintree/docs/reference/general/currencies-2026-09-16|Braintree Currencies reference]] - complete collected page containing the qualified API currency table, zero-decimal markers, Bulgaria transition notice and scheme/exotic settlement-source definitions
