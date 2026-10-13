---
title: "Adyen in-person account structure and store creation"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/design-your-integration/determine-account-structure"
raw_files:
  - "adyen/docs/point-of-sale/design-your-integration/determine-account-structure/2026-09-15.md"
tags: [adyen, point-of-sale, account-structure, merchant-accounts, stores, settlement]
---

## Overview

This Adyen Docs guide applies to any Adyen in-person payment integration or solution. It explains how a company account, merchant accounts, and stores relate, how merchant-account choices affect payout, reporting, access, and cost allocation, and how to request merchant accounts and create stores in Customer Area. These account and store choices are distinct from Terminal API message behavior.

## Key takeaways

- The company level represents the core business; one or more merchant accounts below it receive funds and reconciliation reports; one or more stores under a merchant represent physical locations and have store IDs. Account groups do not combine payouts: Adyen says each merchant account still receives a separate payout. A terminal must be assigned to a store or merchant account in the same location where it is used, so the guide calls for at least one merchant account per country/region.
- Account structure affects bank settlement, reconciliation, Customer Area access, and who sees store data. Adyen presents a merchant account per store or business unit as a common setup, and recommends merchant accounts per legal entity, country/region, or brand with store IDs underneath for many locations. These are business trade-offs, not one required architecture. In the comparison table, the latter option shows one bank transfer per settlement currency and fees reported at the merchant-account level; per-store allocation can need additional finance processes. Involve Finance when deciding.
- To create stores in Customer Area, the user needs the Merchant POS Terminal Management Admin role. Where stores are used under a merchant account, wait for confirmation that the merchant account is ready. Customer Area supports one-by-one creation or a CSV upload of up to 100 stores at once; the form presents default payment methods for the country/region and lets the user select listed additional methods. The page links a separate API store-management route without specifying its request behavior.

## Detail locators

- Integration scope, Customer Area role, three levels, payout grouping, and same-location terminal assignment: `## Requirements` and `## Account levels`, raw lines 21–40.
- Merchant-versus-store trade-offs, settlement currency, fees, reporting, access, and the guide's recommendations: `## 1. Determine account structure` and `### Account structure and settlement`, raw lines 42–81.
- Merchant-account request and test/live Customer Area choice: `## 2. Get merchant accounts`, raw lines 83–92. Store confirmation prerequisite, one-by-one flow, payment-method selection, and CSV cap: `## 3. Create stores`, raw lines 94–156.

## Related

- [[adyen]] — provider context.
- [[adyen-pos-store-management]] — account and store ownership; Management API automation is a separate linked guide.
- [[adyen-terminal-api]] — terminal messaging boundary; this account-structure guide covers any in-person solution.
- [[source-adyen-docs-point-of-sale-design-your-integration-determine-account-structure-automate-store-management]] — separate Management API store administration guide.
- [Configure features](https://docs.adyen.com/point-of-sale/design-your-integration/determine-account-structure/configure-features) — next-step navigation, not evidence read for this entry.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/design-your-integration/determine-account-structure/2026-09-15|Adyen Docs: Set up your account for in-person payments (2026-09-15 snapshot)]]
