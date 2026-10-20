---
title: "Adyen Issuing network token lifecycle webhooks"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/webhook-types/network-tokens-events"
raw_files:
  - "adyen/docs/issuing/webhook-types/network-tokens-events/2026-09-15.md"
tags: [adyen, issuing, network-tokens, digital-wallets, webhooks]
---

## Overview

This 2026-09-15-captured Issuing guide (marked modified 2026-03-16) explains `balancePlatform.networkToken.created` and `.updated` webhooks for the lifecycle of network tokens associated with **Adyen-issued cards added to digital wallets**, such as Apple Pay or Google Pay. These are issuer-side card-token events, not a merchant checkout token or a payment authorization result. [[adyen]] [[adyen-issuing]]

## Key takeaways

- Subscribe to Network token webhooks in the Customer Area. The payload `type` distinguishes created from updated; `data.status` lists `inactive`, `active`, `suspended`, and permanently `closed`, while `data.decision` lists `approved`, `requireAuthentication`, and `declined` for a token request (raw lines 19–41).
- A `created` event follows a wallet provisioning request and risk analysis. The created token is **inactive** even when the decision is `approved`. With `requireAuthentication`, the cardholder must complete SMS/email OTP two-factor authentication or phone-call verification before activation; the guide suggests showing pending verification. With `approved`, Adyen says it activates automatically and a later `.updated` webhook confirms `active` (raw lines 43–62, 104–112).
- An `.updated` event reports a later status change. The examples distinguish `active` with `authenticationApplied=false` after automatic activation from `active` with `authenticationApplied=true` after the required verification. `active` means the card is available in the wallet and ready for payments; it does not prove any particular payment was authorized or settled (raw lines 194–251).
- The `.updated` `closed` case is permanent. The guide lists failed provisioning risk analysis, cardholder wallet removal, platform PATCH revocation, and closure of the underlying payment instrument as closure scenarios. The status table also labels `suspended` temporarily disabled, but this page gives no suspended event example (raw lines 37–41, 283–326).

## Detail locators

- Webhook type/status/decision field table and subscription route: raw lines 26–41. The table names `declined`, but the worked `created` scenarios cover only `requireAuthentication` and `approved`; closure after failed risk analysis is under `.updated` (raw lines 43–50, 283–297).
- Authentication-required and automatic created samples, including network-token ID, `paymentInstrumentId`, `authenticationApplied`, wallet/device and test environment: raw lines 52–192. Sample IDs, wallet names and validation fields are illustrative.
- Updated active-without-authentication and active-after-authentication examples: raw lines 194–281. Closed reasons and sample: raw lines 283–326.

## Related

- [[adyen-issuing]] — Issuing program and reciprocal source catalog.
- [[source-adyen-docs-issuing-network-tokens]] — wallet versus card-on-file token types and lifecycle overview.
- [[source-adyen-docs-issuing-manage-network-tokens]] — separate API lookup and asynchronous status-management guide.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/issuing/webhook-types/network-tokens-events/2026-09-15|Issuing network token webhooks guide, captured 2026-09-15]]
