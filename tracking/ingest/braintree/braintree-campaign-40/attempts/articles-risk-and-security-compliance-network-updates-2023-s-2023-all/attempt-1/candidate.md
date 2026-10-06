---
title: "Braintree All Spring 2023 Network Updates"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/risk-and-security/compliance/network-updates/2023/s-2023-all"
raw_files:
  - "braintree/articles/risk-and-security/compliance/network-updates/2023/s-2023-all-2026-09-16.md"
tags: [braintree, network-updates, card-networks, visa, mastercard, compliance]
---

## Overview

This Braintree-hosted release guide summarizes the card-network changes the page associated with Spring 2023 across Visa, Mastercard and all-network topics. It organizes historical fee changes, mandates and feature updates by network and market, and identifies changes that could require merchant action. The page says its information was accurate as of March 31, 2023, was subject to change and might not apply to every merchant or transaction; treat it as a historical [[braintree]] documentation snapshot for [[braintree-payment-platform]], not current network policy, pricing, account applicability or execution proof.

## Key takeaways

- For the all-network currency update, the page says Visa and Mastercard would change Icelandic krona from two minor units to zero. It expected the network change on April 15, 2023 and recommended that merchants stop accepting minor units by April 10, 2023 to avoid transaction impact.
- The Mastercard sections include a Canada Digital Enablement Fee change, an APAC commercial large-ticket interchange program with a cumulative eligibility list, new service-location fields described as a future informational update, and a Europe final-authorization clearing deadline. For the last item, the body says that beginning May 22, 2023, Europe merchants had to submit the clearing record within three calendar days after final-authorization approval, down from seven, while estimated and incremental authorization transactions were excluded.
- The Visa sections cover historical account-verification, estimated/incremental-authorization, CVV2, non-domestic-currency-settlement and secure-credential fees. They also describe a marketplace-reporting mandate: from April 15, 2023, specified domestic marketplace transactions involving a foreign marketplace retailer required five listed clearing indicators, with the page stating a 0.10% incremental manual-reporting fee when foreign-retail volume lacked them. Exact rates, exclusions, market labels and effective dates remain in the raw locators below rather than being generalized.
- The Visa AVS section says several redundant result codes would stop being returned and maps them to retained result codes, with no AVS-fee impact stated. The account-name-inquiry section describes separate first, middle and last name match decisions, renames the full-name decision, and gives an opt-in historical fee schedule. Integrations interpreting these response values should use the exact captured mappings and dates rather than infer present behavior from this snapshot.

> [!warning] Historical authority boundary
> This is Braintree's dated summary of network announcements, not independent or current Visa, Mastercard, legal, pricing or merchant-account authority. The page itself says the information was accurate as of March 31, 2023, subject to change and potentially inapplicable to some merchants or transactions. Confirm present requirements, pricing, eligibility and account-specific action through the applicable current network and Braintree channels.

> [!warning] Source-internal label conflicts
> The at-a-glance table labels the Account Verification Fee Update as Mastercard / Canada, while the detailed body labels it Visa / Canada. It also labels Non-Domestic Currency Settlement as Global while the body labels it EMEA. This entry does not resolve either conflict or transfer one label across the other; consult the exact raw passages and current authoritative channels for any decision.

## Detail locators

- Release-guide purpose, possible merchant action and snapshot qualification: `## SPRING 2023 RELEASE GUIDE`, raw lines 17-29.
- At-a-glance title/type/network/market catalog, including conflicting labels: table at raw lines 31-46.
- Icelandic krona minor-unit change, recommended merchant cutoff and expected network date: `## What is the Icelandic Krona changes update?`, raw lines 52-66.
- Mastercard Canada Digital Enablement Fee scope, rate and descriptors: `## What is the new Digital Enablement Fee update?`, raw lines 72-84.
- Mastercard APAC commercial large-ticket program rate and cumulative qualification criteria: `## What is the new interchange program for APAC fee change?`, raw lines 87-107.
- Mastercard service-location data-field mandate and informational readiness qualification: `## What is the Standardization of transaction data elements mandate?`, raw lines 112-120. The linked appendix is navigation only unless independently read.
- Mastercard Europe final-authorization clearing deadline and estimated/incremental exclusion: `## What are the Revised Standards for Europe Region Final Authorization Clearing Submission Acceleration?`, raw lines 123-127.
- Visa Canada account-verification body label, fee amounts and descriptors: `## What is the new Account Verification Fee update?`, raw lines 133-143.
- Visa estimated/incremental authorization fee, definitions, unchanged processing statement and transaction exclusions: `## What is the Estimated and Incremental Authorization fee update?`, raw lines 146-159.
- Visa CVV2 fee and no-fee result/authentication conditions: `## What is the Card Verification Value 2 (CVV2) pricing change fee change?`, raw lines 162-172.
- Visa non-domestic currency settlement body market label and phased table: `## What is the Non-Domestic Currency Settlement fee change?`, raw lines 175-183.
- Visa Europe secure-credential fee scope, exclusions and effective date: `## What is the Secure Credential Framework Will Be Expanded in Europe change?`, raw lines 186-199.
- Visa marketplace-reporting transaction condition, required indicators and incomplete-reporting fee: `## What is the Visa Marketplace Reporting mandate?`, raw lines 202-215.
- Visa AVS code consolidation and exact old-to-new mappings: `## What is the Address Verification Service update?`, raw lines 218-244.
- Visa account-name inquiry fields, renamed decision and opt-in fee dates: `## What is the Account Verification Messages update?`, raw lines 247-264.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]

## Related raw API references

- [[raw/braintree/articles/risk-and-security/compliance/network-updates/appendix-2026-09-16|Braintree network-updates appendix]] - linked from the service-location section; navigation only and not read as evidence for this entry

## Raw Sources

- [[raw/braintree/articles/risk-and-security/compliance/network-updates/2023/s-2023-all-2026-09-16|Braintree All Spring 2023 Network Updates]] - complete captured historical release guide
