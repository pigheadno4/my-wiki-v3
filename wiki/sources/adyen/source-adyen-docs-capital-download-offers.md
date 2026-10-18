---
title: "Adyen Capital: Download financing offers for eligible users"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/download-offers"
raw_files:
  - "adyen/docs/capital/download-offers/2026-09-15.md"
tags: [adyen, capital, offers, csv, customer-area]
---

## Overview

This 2026-09-15-modified [[adyen]] Capital guide describes a Customer Area CSV export of financing-offer information for eligible account holders across a selected balance platform. It supports analysis and potential marketing selection, subject to Adyen's Capital guidelines. Downloading or inspecting this dated offer list does not select, accept or sign an offer, create a grant, or prove disbursement or repayment. [[adyen-capital]]

## Key takeaways

- Each account holder's offer is personalized from processing history and has its own expiration date. The CSV contains eligible **minimum and maximum grant amounts**, not a committed exact amount; the later actual offer may vary within the range (raw lines 19–21). Offer data is described as generated daily at midnight CET. A new offer can appear even with an active grant, in some cases reflecting subsequent-grant eligibility; absence from the file means no active offers available for that account holder in the guide's snapshot (raw line 23).
- The requirements name an Adyen for Platforms integration, the Customer Area **Capital base role**, a user operating in a linked supported country/region, and Capital UI/marketing guideline compliance. The guide says an offer remains valid for seven days and a new one is generated after expiry only if qualification continues; the amount can change (raw lines 27–37). The linked country list and guidelines are separate sources; this page does not itself establish current regional eligibility or campaign approval.
- In Customer Area for the **selected balance platform**, go to Financial products > Capital and choose Download Capital Offers CSV; the action generates a local CSV of eligible account holders and offer details (raw lines 39–44). The file schema lists balance-platform name, account-holder ID, min/max amount (strings in major units), currency code, and validity start/expiry timestamps with timezone (raw lines 48–70). The sample rows and filename are examples, not current offers for those IDs or proof a file was downloaded in a real account.
- The page points to a separate API offer route (raw lines 72–74). It does not describe authentication beyond Customer Area role prerequisites, API request bodies, grant request or funding outcome. Do not conflate this export with an accepted formal grant offer or live financing event.

## Detail locators

- Personalization, range, daily generation and active-grant/subsequent-offer nuance: raw lines 19–25.
- Requirements, Capital base role, seven-day validity and supported-region link: raw lines 27–37.
- Customer Area download path: raw lines 39–44.
- Sample filename/rows and CSV column types: raw lines 46–70.
- Separate API navigation: raw lines 72–74.

## Related

- [[adyen-capital]]
- [[source-adyen-docs-capital-get-grant-offers-static-offers]] — account-holder-specific offer route.
- [[source-adyen-docs-capital-get-grant-offers-dynamic-offers]] — dynamic range/formal offer distinction.
- [[source-adyen-docs-capital-make-grant-request]] — separate grant request.
- [[source-adyen-docs-capital-compliance-guidelines]] — linked compliance guidance.

## Raw Sources

- [[raw/adyen/docs/capital/download-offers/2026-09-15|Captured Capital offer-download guide]]
