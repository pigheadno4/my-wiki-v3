---
title: "Adyen AusPayNet Card-Not-Present Compliance Guide"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/auspaynet-compliance-guide"
raw_files:
  - "adyen/docs/online-payments/auspaynet-compliance-guide/2026-09-15.md"
tags: [adyen, auspaynet, australia, card-not-present, sca, 3d-secure]
---

## Overview

This Adyen guide describes how the Australian Payments Network Limited (AusPayNet) card-not-present framework affects Australian-issued and Australian-acquired CNP transactions, and routes merchants through fraud-threshold monitoring, SCA exemptions, and 3D Secure choices. It says it supplements the linked AusPayNet code and is not legal advice. These are claims in a 2026-09-15 webpage snapshot, not verification of current obligations.

## Key takeaways

- The stated scope requires **both** Australian issuance and Australian acquisition. The guide excludes card-present, MOTO, and transactions issued or acquired outside Australia, plus corporate, gift, and prepaid cards. Its threshold and SCA discussion should not be applied to those excluded cases.
- In this snapshot, a merchant exceeds the fraud threshold for a quarter only when **both** fraud losses exceed AUD 50,000 and the fraud-to-sales ratio is at least 0.2%. Adyen says it calculates fraud rates by merchant account each quarter and reports the figures to AusPayNet as acquirer. One breached quarter prompts fraud-reduction measures; after two consecutive breached quarters, the guide directs SCA on non-exempted CNP transactions. For a third quarter it recommends SCA on all CNP transactions; a fourth may bring sanctions. A quarter below the threshold ends the described all-CNP SCA requirement.
- The guide lists possible recurring, trusted-customer, and verified-wallet exemptions, but says they do not apply on first access, a changed payment instrument, or after more than 180 days since the cardholder last accessed the online service. Recurring payments must be flagged with `shopperInteraction: ContAuth` and the correct `recurringProcessingModel`; exemptions are conditional, not a general bypass.
- Adyen recommends 3D Secure as an SCA method and presents three implementation routes: Adyen handling after Support/account-manager setup, merchant Dynamic 3D Secure rules, or a per-request `authenticationData.attemptAuthentication` preference. The last route overrides Adyen's default compliance handling, so the guide limits that choice to integrations with extensive AusPayNet and 3D Secure knowledge. Its recommendation and dated code link do not establish current regulatory sufficiency or a specific issuer/authentication result.

## Detail locators

- Opening and `## AusPayNet CNP framework` (raw lines 14–33): supplement/not-legal-advice boundary, Australian issue-and-acquire scope, and exclusions.
- `## Merchant fraud threshold` and `## Exceeding the merchant fraud threshold` (raw lines 35–59): two-part quarterly threshold, fraud/sales measures, Adyen merchant-account reporting, consecutive-quarter responses, and below-threshold transition.
- `## Strong customer authentication` and `## SCA exemptions` (raw lines 61–88): two-factor description, recurring/trusted-customer/wallet routes, recurring request flags, and exemption exclusions.
- `## Using 3D Secure for SCA` (raw lines 90–104): recommendation, Adyen/Dynamic/API preference options, and default-logic override warning.

## Related

- Company: [[adyen]]
- Concept: [[adyen-3d-secure]]
- Related concept: [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/online-payments/auspaynet-compliance-guide/2026-09-15|2026-09-15 Adyen AusPayNet CNP guidance snapshot]]
