---
title: "Adyen Checkout API v72 POST /donationCampaigns — List campaigns"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/post/donationCampaigns"
raw_files:
  - "adyen/api-explorer/Checkout/latest/post/donationCampaigns/2026-09-15.md"
tags: [adyen, checkout, api, giving, donations]
---

## Overview

This captured API Explorer reference documents Checkout API v72 `POST /donationCampaigns` at the test server. It queries active donation campaigns using donation context; it does not create a campaign or make a donation. See [[adyen]] and [[adyen-giving]].

## Key takeaways

- The request body table marks `currency` and `merchantAccount` required. `label` and `locale` are optional. `store` is marked optional in the table but described as required for Adyen for Platforms integrations using a platform model; its identifier meaning differs between balance-platform and classic integrations. `Idempotency-Key` is an optional header with a 64-character maximum.
- A 200 response may contain `donationCampaigns`, an array of active campaigns for the merchant account. Campaign details can include a unique campaign `id`, nonprofit details, banner/logo/terms URLs, and fixed-amount or roundup donation configuration. The array itself and many child fields are marked optional in this schema; child-field requiredness applies when its containing object is present.
- This discovery response does not establish donation eligibility for a particular shopper, a donation request, authorization, settlement, or a `DONATION` webhook outcome. The reference lists 400, 401, 403, 422, and 500 errors. Its generic 422 example says “Return URL is missing,” but no `returnUrl` is listed for this request; do not infer one from that example.
- The URL says `latest`, while the captured server is `https://checkout-test.adyen.com/v72` (2026-09-15 snapshot). It does not establish a current live version.

## Detail locators

- Purpose, test server, header and request body with conditional `store`: raw lines 5–27.
- Response campaign object, optionality and donation types: raw lines 38–64.
- HTTP error tables and illustrative payloads: raw lines 67–247.

## Related

- [[source-adyen-docs-online-payments-donations-integration-options-advanced-flow]] — online Giving integration guide.
- [[adyen-giving]] — provider concept route.

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/post/donationCampaigns/2026-09-15|Captured Checkout API POST /donationCampaigns reference]]
