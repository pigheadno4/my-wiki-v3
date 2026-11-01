---
title: "Adyen A2A Issuer iDEAL profile registration"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/a2aissuer-api/latest/post/ideal/profile/register"
raw_files:
  - "adyen/api-explorer/a2aissuer-api/latest/post/ideal/profile/register/2026-09-15.md"
tags: [adyen, business-accounts, ideal, a2a-issuer, api]
---

## Overview

This captured A2A Issuer API v1 `POST /ideal/profile/register` reference starts registration of a new iDEAL profile linked to the supplied account holder and payment instruments. The user **must be redirected** to the response URL to finish registration. A successful request or redirect URL is not completed profile registration, iDEAL payment authentication, or payment execution. See [[adyen]] and [[adyen-business-accounts]].

## Key takeaways

- The request requires `accountHolderId` and an array of `paymentInstrumentIds`. The page lists distinct TEST and LIVE `/a2aissuer-api/v1` servers. Its example contains two instrument IDs, without stating a minimum or maximum.
- The 200 response table marks the parent `redirectUrl` object optional, while `href` is required within it and is described as a short-lived URL for the iDEAL registration page. The introductory instruction to redirect the user remains important; the table does not guarantee `redirectUrl` in every 200 response.
- The page documents 400 malformed-request, 422 validation, and 500 server-error responses. Illustrated 422 cases include an already registered profile (`1069_007`), missing or invalid request data (`29_001`), account holder not found (`30_012`), and payment instrument not found (`30_032`). Example 500 codes include `1069_001` and `1069_002`; these are examples rather than exhaustive outcomes. Optional problem fields are in the response tables, with required `name`, `value`, and `message` only within an `invalidFields` item.

## Detail locators

- Purpose, redirect requirement, servers and request schema: pinned raw lines 5–23.
- Request example: lines 25–36.
- Response schemas for 200/400/422/500: lines 37–103.
- Response examples and error codes: lines 105–207.

## Related

- [[adyen-business-accounts]]
- [[source-adyen-docs-business-accounts-send-funds-ideal-integration]]

## Raw Sources

- [[raw/adyen/api-explorer/a2aissuer-api/latest/post/ideal/profile/register/2026-09-15|A2A issuer iDEAL profile register API Explorer capture]]
