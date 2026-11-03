---
title: "GET /balancePlatforms/{id} — Get a balance platform | Adyen Balance Platform API"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balancePlatforms/(id)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(id)/2026-11-02.md"
tags: [adyen, balance-platform, api-explorer, resource-read]
---

## Overview

This [[adyen]] Balance Platform API Explorer snapshot documents `GET /balancePlatforms/{id}`, which returns a balance platform by its unique balance-platform ID. The captured server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; the URL says `latest`, while the server path identifies `v2`. This is a balance-platform resource read, not a balance-account, account-holder, payment or transfer operation. See [[adyen-platforms]] for platform context.

## Key takeaways

- The only parameter table is for the path: `id` is a required string identifying the balance platform. This page specifies no request body, query parameter, default or limit for this GET operation. [Raw: lines 9–17]
- A 200 response is labeled request success. Its body requires the balance-platform `id`; `description` and `status` are optional. The listed status values are `Active`, `Inactive`, `Closed` and `Suspended`. The example showing `Active` is illustrative, not a guarantee of a particular platform's state. [Raw: lines 19–29, 131–141]
- Error sections cover 400 request-reading/understanding, 401 authentication, 403 insufficient permissions, 422 validation and 500 server-processing failures. They give a shared error-body shape with required `detail`, `errorCode`, HTTP `status`, `title` and `type`, and optional fields including `invalidFields` and `requestId`; required nested validation fields apply only when `invalidFields` is present. [Raw: lines 32–129]
- The generic 422 example describes a payment-instrument `balanceAccountId` change, and the generic 500 example describes payment-instrument creation. Neither establishes a GET balance-platform-specific mutation or failure condition. A returned resource or status does not by itself establish current eligibility, resource creation or update, verification, authorization, booking, settlement, payout or bank receipt. [Raw: lines 182–207]

## Detail locators

- Purpose, TEST v2 server and required path ID: pinned raw lines 5–17.
- 200 response schema and status values: lines 19–29; success example: lines 131–141.
- Error headings and schemas: lines 32–129; generic error examples: lines 143–207.

## Related

- [[adyen-platforms]] — platform and user resource context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(id)/2026-11-02|GET /balancePlatforms/{id} — captured 2026-11-02]]