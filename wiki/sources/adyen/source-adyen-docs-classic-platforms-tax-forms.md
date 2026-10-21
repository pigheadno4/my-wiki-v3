---
title: "Adyen Classic Platforms 1099-K tax forms"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/tax-forms"
raw_files:
  - "adyen/docs/classic-platforms/tax-forms/2026-09-15.md"
tags: [adyen, classic-platforms, tax-forms, 1099-k, us]
---

## Overview

This 2023-modified Classic Adyen for Platforms guide, captured 2026-09-15, describes retrieving a US sub-merchant's 1099-K as Base64 content through Classic Account API `/getTaxForm` and delivering a decoded PDF. It states a historical **2024** federal gross-volume threshold; the page directs new integrations to a different guide and does not establish current tax law or filing status for any entity. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The page frames Adyen's US 1099-K filing scope as US-based merchants/sub-merchants to whom it pays out directly **and** who cross the processed-volume threshold; some states have their own requirements (raw lines 19–28). It states that for **2024** the federal gross processed-volume threshold is USD 5,000 per calendar year, with state thresholds varying. Gross volume is before fees, chargebacks and refunds (raw lines 30–33). These dated claims are not a current threshold determination or tax advice.
- To provide a digital form, show a platform UI link/button, make a **server-side** POST `/getTaxForm` with `accountHolderCode`, `formType` such as `1099-K`, and applicable `year`, then decode the returned Base64 `content` and provide a PDF to the sub-merchant (raw lines 35–57, 74–83). The table also returns `contentType`, for example `application/pdf` (raw lines 74–79).
- The page says a form is generated only for sub-merchants meeting its volume or transaction threshold; querying a holder below threshold returns an error (raw line 59). The guide's Account API v6 TEST curl uses year 2019 solely as an example (raw lines 61–72); it does not show that an actual 2019, 2024 or current form exists for a particular holder. A response containing Base64 content is a retrieval artifact, not proof that the PDF was delivered to the sub-merchant or filed with a tax authority.

## Detail locators

- Classic-only scope, historical filing subject/condition and 2024 gross threshold: raw lines 19–33. UI-to-server-request-to-PDF flow: raw lines 35–45.
- Request parameters, below-threshold error and test v6 example: raw lines 47–72. Response fields and decoding/delivery: raw lines 74–83.

## Related

- [[adyen-classic-platforms]] — older account-holder/account model.
- [[source-adyen-docs-platforms-us-tax-forms]] — separate newer Platforms tax-form guide; do not transfer its conditions or API into this Classic source.
- [[adyen-platforms]] — newer balance-platform model.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/tax-forms/2026-09-15|Classic 1099-K form guide, captured 2026-09-15]]
