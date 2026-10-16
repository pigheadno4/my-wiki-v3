---
title: "Adyen Giving peak-season guide"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/industries/peak-season/giving"
raw_files:
  - "adyen/docs/industries/peak-season/giving/2026-09-15.md"
tags: [adyen, giving, donations, peak-season, nonprofit]
---

## Overview

This 2026-09-15 Adyen Giving page sits under the peak-season guidance and introduces shopper donations to a nonprofit associated with a purchase. It routes merchants to in-person, online, and platform Giving documentation. Its year-end framing is seasonal advice, not an eligibility window or a claim that a particular campaign, donation, or nonprofit bank transfer occurred. See [[adyen-giving]] for the Giving product route and [[adyen-peak-season-readiness]] for the seasonal hub.

## Key takeaways

- The page describes a shopper option to donate to a selected nonprofit after a physical-store or online purchase, through a fixed amount or a round-up amount. It says Adyen covers donation fees and transfers the full donated amount directly to the nonprofit’s bank account. This is the guide’s product description, not proof of a specific raised amount, settlement or bank receipt.
- A merchant can use the Customer Area **Campaigns** interface to set up and manage a campaign and choose a nonprofit. For in-person payments, the guide says a configured campaign can automatically present a donation prompt on the terminal without integration work, or the merchant can trigger that prompt through a Terminal API payment request.
- For online payments, the guide says the merchant’s integration displays a donation form after campaign setup and sends a separate `/donations` API request in addition to its payment request if the shopper opts in. The in-person terminal prompt and online integration/API request are different implementation paths; the page provides no full request schema or donation-outcome verification.
- Before starting or reviewing a campaign, the page directs readers to channel-specific supported countries, regions, currencies, methods, interaction flows, terminal models and donation options. Those linked lists are navigation, not verified support matrices in this raw snapshot. Platform donations are linked as a further route without implementation detail here.
- The seasonal framing names the final two months of the year and mentions tax-deduction deadlines in some regions. It does not limit Giving to those months, specify current nonprofit or merchant eligibility, grant Customer Area permissions, or prove that a merchant campaign was activated.

## Detail locators

- Page metadata, seasonal description and full-fee claim: pinned raw lines 5–23.
- Donation option, nonprofit settlement claim, campaign interface and channel scope: pinned raw lines 25–31.
- In-person campaign/prompt and supported-feature navigation: pinned raw lines 33–41.
- Online campaign/form/API path and supported-feature navigation: pinned raw lines 43–50.
- Linked POS, online and platform guides: pinned raw lines 52–56.

## Related

- [[adyen]]
- [[adyen-giving]]
- [[adyen-peak-season-readiness]]
- [[adyen-index]]

## Raw Sources

- [[raw/adyen/docs/industries/peak-season/giving/2026-09-15|Adyen Giving seasonal page snapshot (2026-09-15)]]
