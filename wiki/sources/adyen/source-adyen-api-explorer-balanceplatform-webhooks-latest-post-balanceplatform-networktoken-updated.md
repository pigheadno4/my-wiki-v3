---
title: "Adyen Balance Platform webhook: network token updated"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.networkToken.updated"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.networkToken.updated/2026-09-15.md"
tags: [adyen, issuing, webhooks, network-tokens]
---

## Overview

This 2026-09-15 capture documents the incoming `balancePlatform.networkToken.updated` webhook that Adyen sends for an internal network-token status update during provisioning. It is an event contract, not a merchant POST operation or a payment result. The `latest` route does not independently verify a current API version. See [[adyen]], [[adyen-issuing]] and [[adyen-webhooks]].

## Key takeaways

- The envelope requires `data`, `environment` (`test` or `live`) and top-level `type`; queue `timestamp` is optional. Every listed `data` field, including token `id`, associated `paymentInstrumentId`, `status`, `decision`, `authenticationApplied`, token `type`, and risk/validation details, is optional in this table. The page supplies no example payload and no allowed values for `data.status` or `authentication.result`; an update event alone does not establish that the token is active, authentication succeeded, or a payment occurred.
- `data.decision` lists `approved`, `declined` and `requiresAuthentication`. The separate [[source-adyen-docs-issuing-webhook-types-network-tokens-events|Issuing network-token webhook guide]] lists `requireAuthentication` for that decision instead (its raw line 41). Treat the differing enum spellings as an unresolved source conflict; do not silently normalize them.
- Optional `authentication` identifies process method (`sms_OTP` or `email_OTP`) and result, while `authenticationApplied` indicates whether authentication was triggered during provisioning. `data.type` can be `wallet` or `cof`; `wallet` details are returned only for wallet type. `validationFacts.reasons` is sent only for an invalid `walletValidation` result. Risk scores, transaction-rule results and validation facts are documented fields, not proof of approval or payment authorization.
- A `2xx` response accepts the webhook. This page does not establish delivery order, retries, deduplication or signature mechanics.

## Detail locators

- Event trigger: pinned raw title/introduction, lines 5–7.
- Envelope, token/payment-instrument IDs, decision and authentication: `## Parameters > ### Request body`, lines 11–24.
- Requestor, risk/validation and wallet-only details: same table, lines 25–48.
- Acknowledgement: `## Responses > ### 200 Success`, lines 50–58.

## Related

- [[source-adyen-docs-issuing-webhook-types-network-tokens-events]] — separate wallet-focused lifecycle guide; its decision enum spelling differs from this API Explorer table.
- [[source-adyen-docs-issuing-network-tokens]] — network-token types and lifecycle overview.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.networkToken.updated/2026-09-15|Network token updated webhook snapshot]]
