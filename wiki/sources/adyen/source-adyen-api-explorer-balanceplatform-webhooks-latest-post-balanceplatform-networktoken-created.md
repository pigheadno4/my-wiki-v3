---
title: "Adyen network token created webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.networkToken.created"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.networkToken.created/2026-09-15.md"
tags: [adyen, webhooks, issuing, network-tokens]
---

## Overview

Captured API Explorer reference for Adyen's incoming `balancePlatform.networkToken.created` webhook. Despite the “created” event label, its trigger text says Adyen sends it when a network-token provisioning request is initiated. The payload can express `approved`, `declined`, or `requiresAuthentication` decisions, so event receipt alone is not proof of an active, usable token. The `latest` URL is a 2026-09-15 snapshot, not a fixed version.

## Key takeaways

- The body table requires top-level `data`, `environment`, and `type`; `timestamp` is optional. All listed `data` fields are marked optional, including network-token `id`, associated `paymentInstrumentId`, `decision`, `status`, token type (`wallet` or `cof`), requestor, authentication and validation detail. `environment` can be `test` or `live`.
- `authenticationApplied` says whether authentication was triggered; optional authentication detail has `sms_OTP` or `email_OTP` method and a result without enumerated values. `validationFacts.reasons` is only sent for an invalid `walletValidation` fact. The `wallet` object is returned only when the network-token type is `wallet`.
- The optional `transactionRulesResult` contains risk advice, a hard-block-rules result, score and triggered rules. The optional scheme risk score describes Visa `00`–`99`, where `00` means no score supplied. Wallet account/device scores are separate 1–5 values; the source describes their directions but does not make them authentication or provisioning outcomes.
- The reference instructs any HTTP `2xx` to accept the webhook. It gives no example payload or event-specific ordering, retry, deduplication, signature, completed authentication, token activation, payment authorization or settlement guarantee.

## Detail locators

- Event label and request-initiation trigger: raw lines 5–7.
- Envelope, token/payment-instrument IDs, decision and authentication: raw lines 11–25.
- Requestor, risk/validation and conditional wallet fields: raw lines 26–48.
- Acknowledgment: raw lines 50–58.

## Related

- [[adyen]]; [[adyen-webhooks]]; [[adyen-issuing]].

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.networkToken.created/2026-09-15|2026-09-15 captured API Explorer reference]]
