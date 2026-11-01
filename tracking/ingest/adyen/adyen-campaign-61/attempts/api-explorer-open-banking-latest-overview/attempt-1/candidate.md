---
title: "Adyen Open Banking API v1 overview"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/open-banking/latest/overview"
raw_files:
  - "adyen/api-explorer/open-banking/latest/overview/2026-09-15.md"
tags: [adyen, open-banking, account-verification, api]
---

## Overview

This Open Banking API v1 overview lists a route-creation operation for third-party individual bank-account verification and a report-read operation. The route step lists Account Information Service Providers (AISPs); a successful connection produces a code used to request the bank report and verify identity. The report supplies identity verification and bank-account details. This is a catalog and authentication overview, not an endpoint payload contract or proof of a particular completed verification. [[adyen]] [[adyen-business-accounts]]

## Key takeaways

- The API credential needs an `X-API-Key` header and the stated `Role for OpenBanking account verification use case: EXTERNAL`; the page directs contacting Adyen to set up that role. See raw lines 15–32.
- The test and live API bases are `obgateway-test.adyen.com/obgateway/v1` and `obgateway-live.adyen.com/obgateway/v1`, respectively. See raw lines 34–40.
- The endpoint table lists `POST /accountVerification/routes` to create verification routes and `GET /accountVerification/reports/{code}` to retrieve a report. The page does not define their request bodies, response fields, code lifetime, consent sequence, or report outcome rules; consult their individual references. See raw lines 42–48.
- Do not conflate this external individual bank-account verification route with registered account-holder capability verification or Business Account opening.

## Detail locators

- Purpose and route/report relationship: raw lines 5–13.
- Authentication and role: raw lines 15–32.
- Hosts and operation catalog: raw lines 34–48.

## Related

- [[adyen-business-accounts]]
- [[source-adyen-docs-business-accounts-verify-account-holder]]

## Raw Sources

- [[raw/adyen/api-explorer/open-banking/latest/overview/2026-09-15|Open Banking API v1 overview snapshot]]
