---
title: "Adyen Account API v6 POST /deleteShareholders"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Account/latest/post/deleteShareholders"
raw_files:
  - "adyen/api-explorer/Account/latest/post/deleteShareholders/2026-09-15.md"
tags: [adyen, classic-platforms, account-api, shareholders]
---

## Overview

This captured Account API v6 `POST /deleteShareholders` reference describes deletion of shareholders associated with a **Classic Platforms account holder**. The request selects the account holder by `accountHolderCode` and the shareholders to delete by `shareholderCodes`; both body properties are required in the table. This is a destructive operation scoped to those selected shareholders. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The listed server is `https://cal-test.adyen.com/cal/services/Account/v6`. The request example supplies one shareholder code, but the body schema calls `shareholderCodes` an array of strings; the example does not set a one-code limit. See raw lines 9–30.
- A `200` response is labeled “The request has succeeded.” A `202` response says the request was accepted for processing **and processing has not been completed**. Do not treat a 202 acknowledgment as deletion completion. The page does not specify a later completion signal or propagation time. See raw lines 31–64.
- Both 200 and 202 response tables make `invalidFields`, `pspReference` and `resultCode` optional. `invalidFields` can contain validation errors that would prevent requests from being processed; inspect the returned fields rather than assuming they are always present or that a request receipt proves the selected records are gone. See raw lines 36–64.
- Documented error classes are 400 (request reading/understanding), 401 (authentication required), 403 (insufficient permissions), 422 (request validation), and 500 (server could not process). The example 400 and 403 error codes/messages are examples, not an exhaustive code list. See raw lines 67–155.

## Detail locators

- Operation identity and TEST v6 server: raw lines 5–10.
- Required selector properties and request example: raw lines 12–30.
- 200 versus incomplete-processing 202 and optional response fields: raw lines 31–64.
- Error response tables and 400/403 examples: raw lines 67–155.

## Related

- [[adyen-classic-platforms]] — Classic account-holder and shareholder context.
- [[source-adyen-api-explorer-account-latest-overview]] — Account API v6 overview and authentication/version boundary.
- [[source-adyen-docs-classic-platforms-account-holders-and-accounts]] — Classic account-holder structure and onboarding.

## Raw Sources

- [[raw/adyen/api-explorer/Account/latest/post/deleteShareholders/2026-09-15|POST /deleteShareholders, captured 2026-09-15]]
