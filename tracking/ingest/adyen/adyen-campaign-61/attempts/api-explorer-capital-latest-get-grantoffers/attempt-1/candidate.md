---
title: "Adyen Capital API: list available static grant offers"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/capital/latest/get/grantOffers"
raw_files:
  - "adyen/api-explorer/capital/latest/get/grantOffers/2026-09-15.md"
tags: [adyen, capital, grant-offers, api]
---

## Overview

`GET /grantOffers` on the Capital API v1 lists available static offers for the required query `accountHolderId`, including static offers created after a user selected a financing amount from dynamic offers. This is an offer-list read, distinct from accepting an offer, creating a grant, or disbursing financing. The captured reference lists test and live balance-platform Capital API hosts. [[adyen]] [[adyen-capital]]

## Key takeaways

- The request requires `accountHolderId` as a query parameter. A 200 response requires a `grantOffers` array; each offer entry requires `accountHolderId`, while amount, contract type, expiry, fee, offer ID, repayment, and validity start are marked optional at their respective levels. See raw lines 17–47.
- If the optional `amount` object is supplied, its currency and minor-unit value are required within it. If optional `fee` is supplied, its `amount` is required within that object. If optional `repayment` is supplied, its `basisPoints` is required within it. Do not read nested required fields as requiring their optional parent objects. See raw lines 32–47.
- The listed `contractType` values are `loan` and `cashAdvance`; `repayment.basisPoints` is the share of the user's incoming net volume deducted for repayment. `fee.aprBasisPoints` is optional and denominated in basis points. See raw lines 37–46.
- The reference lists 404 for an entity not found and 422 for request validation error, each with optional problem fields and conditionally required fields inside optional `invalidFields` entries. It provides no worked request or response examples. See raw lines 49–85.

## Detail locators

- API hosts and version: raw lines 9–15.
- Query parameter: raw lines 17–22.
- Offer-list response fields: raw lines 24–47.
- 404 and 422 error schemas: raw lines 49–85.

## Related

- [[adyen-capital]]

## Raw Sources

- [[raw/adyen/api-explorer/capital/latest/get/grantOffers/2026-09-15|Capital GET grantOffers snapshot]]
