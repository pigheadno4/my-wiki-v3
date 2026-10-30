---
title: "Adyen Configuration API v2 overview"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/overview"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/overview/2026-09-15.md"
tags: [adyen, configuration-api, balance-platform, api-reference]
---

## Overview

This 2026-09-15 capture of the Configuration API **v2** overview describes an API for managing a balance platform and catalogs endpoints for account holders, balance accounts, cards/payment instruments and business accounts. The `latest` documentation URL does not change the captured `/bcl/v2` contract. It is a route into operation references, not an operation-level schema. [[adyen]] [[adyen-platforms]] [[adyen-api-access]]

## Key takeaways

- Every Configuration API request needs an API key in `X-API-Key`; the key is generated in the relevant Customer Area. Platforms/marketplace setup and Issuing use different linked credential instructions. See raw lines 9–20.
- Versioning uses a `vXX` URL suffix. The listed TEST server is `https://balanceplatform-api-test.adyen.com/bcl/v2`; the text separately names the LIVE `https://balanceplatform-api-live.adyen.com/bcl/v2` base and a live Customer Area key. See lines 22–35.
- The endpoint table identifies routes by method, path and summary only. It includes account holders, balance accounts, platform, payment instruments/cards, grant offers/accounts, sweeps, payout schedules, transfer limits, webhooks, SCA devices/associations and more; these are distinct resource identities. It does not give request-body or property requiredness, response/error shapes, operation roles, lifecycle rules or execution outcomes. See lines 37–137.

## Detail locators

- General account-holder, balance-account, platform and grant routes: raw lines 39–65.
- Payment-instrument, card-data, PIN, transaction-rule and registered-device routes: raw lines 66–94.
- Payout schedules, recurring top-ups, transfer limits, webhook settings, mandates, authorized card users and SCA routes: raw lines 95–137. The `DELETE`, `PATCH`, `approve` and `initiate` labels are navigation, not evidence of exact side effects or completion.

## Related

- [[adyen-issuing]] — card-program context; operation-level issuing requirements live in its linked guides.
- [[adyen-business-accounts]] — separate financial-product context and eligibility boundaries.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/overview/2026-09-15|Configuration API v2 overview, captured 2026-09-15]]
