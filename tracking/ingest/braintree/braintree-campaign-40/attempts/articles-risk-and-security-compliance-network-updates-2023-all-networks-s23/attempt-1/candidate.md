---
title: "Braintree Icelandic Krona Spring 2023 All-Network Update"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/risk-and-security/compliance/network-updates/2023/all-networks-S23"
raw_files:
  - "braintree/articles/risk-and-security/compliance/network-updates/2023/all-networks-S23-2026-09-16.md"
tags: [braintree, network-updates, visa, mastercard, currencies, isk]
---

## Overview

This collected Braintree webpage is a narrow historical all-network notice about a planned Spring 2023 change to Icelandic krona minor units. It says Visa and Mastercard would move ISK from two minor units to zero, gives an expected network date, and recommends an earlier merchant cutoff. It is a dated [[braintree]] retrieval route for [[braintree-currencies]], not current currency metadata, present Visa or Mastercard policy, merchant-specific applicability, or proof that a merchant changed amount handling.

## Key takeaways

- The notice labels the update as a new feature/update for all networks and the global market. Its body specifically names Visa and Mastercard.
- The page says Visa and Mastercard would remove Icelandic krona minor units, changing the currency from two decimal places to zero minor units. Its table identifies the currency as Iceland Krona, ISO code `ISK/352`, with a change from `2` to `0`.
- The page expected the network change on April 15, 2023, but separately recommended that merchants stop accepting minor units by April 10, 2023 so transactions would not be impacted. The earlier date is merchant guidance in this historical notice, not the network effective date.

> [!warning] Historical currency and network boundary
> Treat the values, dates and merchant recommendation as claims in this captured Braintree notice. The page does not establish current ISO currency metadata, current Visa or Mastercard rules, present Braintree processing behavior, merchant-account applicability, or completed implementation. Verify current currency representation and network requirements through current authoritative sources before changing amount handling.

## Detail locators

- Update classification and scope: `## What is the Icelandic Krona changes update?`, raw lines 17-21.
- Expected network date versus recommended merchant cutoff: note under the update, raw lines 24-25.
- Currency name, ISO code and old/new minor-unit values: table at raw lines 29-31.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-currencies]]
- Broader historical guide: [[source-braintree-articles-risk-and-security-compliance-network-updates-2023-s-2023-all]] - contains the same Icelandic-krona notice within the combined Spring 2023 network release guide.

## Raw Sources

- [[raw/braintree/articles/risk-and-security/compliance/network-updates/2023/all-networks-S23-2026-09-16|Braintree All Networks Spring 2023 Icelandic krona update]] - complete collected narrow historical notice
