---
title: "Adyen Forward API webhook — forwardApi.notification"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Forward-API-webhooks/latest/post/forwardApi.notification"
raw_files:
  - "adyen/api-explorer/Forward-API-webhooks/latest/post/forwardApi.notification/2026-09-15.md"
tags: [adyen, webhooks, forward-api, payments]
---

## Overview

This 2026-09-15 snapshot of the Forward API webhooks `latest` `forwardApi.notification` reference describes an incoming notification after Adyen forwarded a payment request to a third-party service on the merchant's behalf. Its title calls the Forward API request completed; this is a webhook contract, not an instruction to make a payment. See [[adyen]], [[adyen-webhooks]], and [[adyen-online-payments]].

## Key takeaways

- The outer `type` and `createdAt` are marked required; `version`, `environment`, and `data` are optional in the displayed table. The example uses `type: "forwardApi.notification"`, `version: "1"`, and `environment: "test"`; it does not pin all `latest` events to version 1.
- Within the optional `data` object, the table marks `eventDateTime`, `externalPsp`, `merchantAccountCode`, `merchantCountryCode`, `merchantReference`, `pspReference`, `scheme`, `shopperReference`, and `storedPaymentMethodId` required. `pspReference` is Adyen's request reference; `externalPsp` names the third-party service. Optional `externalPspTransactionStatus` is the status returned by that service, not a blanket authorization guarantee.
- Optional booleans distinguish whether network-transaction-reference and transaction-link-ID paths were requested versus found in the third-party response. The raw third-party response body is optional. See the pinned table for exact names and scope.
- The response section says `200 Success`, "The request has succeeded," and an optional `notificationResponse`; any HTTP `2xx` accepts the webhook. That receiver acknowledgement is separate from the third-party transaction status or payment finality.

## Detail locators

- Complete request body table, including amount currency/minor-unit value, reference matching flags, third-party body/status, identities, environment and version: raw lines 9–35. Nested required fields are conditional on the optional `data` object being present.
- Single recurring example with third-party status `Authorised`, externalPsp `adyen`, VISA, EUR 100, and a raw response body: raw lines 37–62. These are example values, not universal outcomes.
- Response and `2xx` acceptance wording: raw lines 63–71. The page gives no delivery ordering, retry, deduplication, signature, or financial settlement rule.

## Related

- [[adyen]] — provider context.
- [[adyen-webhooks]] — webhook-family context.
- [[adyen-online-payments]] — payment context.

## Raw Sources

- [[raw/adyen/api-explorer/Forward-API-webhooks/latest/post/forwardApi.notification/2026-09-15|Forward API webhooks latest forwardApi.notification, captured 2026-09-15]]
