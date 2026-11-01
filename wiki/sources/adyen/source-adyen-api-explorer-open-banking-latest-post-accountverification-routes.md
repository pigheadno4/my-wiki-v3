---
title: "Adyen Open Banking Gateway v1: account-verification routes"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/open-banking/latest/post/accountVerification/routes"
raw_files:
  - "adyen/api-explorer/open-banking/latest/post/accountVerification/routes/2026-09-15.md"
tags: [adyen, open-banking, account-verification, api]
---

## Overview

This 2026-09-15-captured Open Banking Gateway v1 reference documents `POST /accountVerification/routes` on test and live `obgateway` servers. It creates a list of available provider redirection routes for verifying an external third-party individual's bank account. A successful connection later generates a unique code used to request bank reports and verify identity. A route-list response alone is provider availability and flow entry, not a completed connection, consent or bank-account verification.

## Key takeaways

- The request requires `country`, where the individual's bank account is registered, and `redirectUrl`, where Adyen redirects the individual after the open-banking flow. Adyen uses the country to determine an available provider and configure the flow for that location. Optional `locale` controls UI language and defaults to `en-US`.
- Optional `state` helps identify the request in callback handling; the page says a per-session value can protect against CSRF and must use URL-encodable characters. This is guidance and a value constraint, not proof that callback validation was performed.
- A 200 response requires a `routes` array. Each listed route requires a `link` and `provider` object with `name` and `logoURL`; the link redirects the individual when selected. The example names Tink, but it does not guarantee Tink or any other provider for a given country or request.
- The page describes 400 malformed request, 401 invalid or insufficient API credential, 422 validation, 429 rate limit and 500 server errors. It gives no error examples, rate limit threshold, connection result, report payload or identity-verification outcome here.

## Detail locators

- Purpose and Gateway v1 test/live servers: raw lines 5–15.
- Request fields, country/provider selection, redirect, locale default and state guidance: raw lines 17–37.
- 200 route/provider schema: raw lines 38–50.
- 400/401/422/429/500 problem schemas: raw lines 53–145.
- Illustrative provider route response: raw lines 147–164.

## Related

- [[adyen]] — provider.
- [[adyen-business-accounts]] — existing Open Banking and external-individual verification source routes; this Gateway flow is separate from consented TPP access to a Business Account holder.
- [[source-adyen-docs-business-accounts-verify-account-holder]] — separate guide for connection, report and identity-check stages.

## Raw Sources

- [[raw/adyen/api-explorer/open-banking/latest/post/accountVerification/routes/2026-09-15|Open Banking Gateway v1 POST /accountVerification/routes (captured 2026-09-15)]]
