---
title: "Adyen Payments App API v1 overview"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/payments-app/latest/overview"
raw_files:
  - "adyen/api-explorer/payments-app/latest/overview/2026-09-15.md"
tags: [adyen, payments-app, mobile-pos, api-explorer]
---

## Overview

Captured **Payments App API v1** directory for boarding and managing the separate Adyen Payments App on Android mobile devices. The API uses merchant, store and app-installation resource paths on management test/live servers. This page is an endpoint index, not a boarding-token, installation or payment transaction schema. See [[adyen]] and [[adyen-mobile-pos]].

## Key takeaways

- Each Payments App API request requires an API key in `X-API-Key`; the page says to generate it in Customer Area and use a live Customer Area key for live requests. It does not state an API role, token scope or authorization outcome.
- Versioning is in the endpoint URL. The page shows `management-test.adyen.com/v1` and `management-live.adyen.com/v1`; its example request path is merchant-level `/merchants/{merchantId}/generatePaymentsAppBoardingToken`.
- The directory lists POST boarding-token creation at merchant or `{storeId}` scope, GET Payments App lists at merchant or store scope, and POST `/merchants/{merchantId}/paymentsApps/{installationId}/revoke` to revoke an instance's authentication. These path identities are distinct; the overview supplies no request/response fields, token lifetime, installation state transition, revocation timing, error conditions or reversal procedure.
- Listing an endpoint or sending a boarding-token or revoke command does not by itself prove the Android app boarded, authenticated or processed a payment. The page contains no asynchronous event contract or financial authorization, capture, reconciliation, settlement or bank-receipt evidence.

## Detail locators

- API identity and purpose: raw lines 5–7.
- API key authentication: raw lines 9–11.
- URL versioning, test example and live-key/live URL instructions: raw lines 13–23.
- Test/live v1 servers: raw lines 25–31.
- Five merchant/store/installation endpoints: raw lines 33–42.

## Related

- [[adyen-mobile-pos]] — separate Android Payments App route.
- [[adyen]] — provider index.

## Raw Sources

- [[raw/adyen/api-explorer/payments-app/latest/overview/2026-09-15|Payments App API v1 overview, captured 2026-09-15]]
