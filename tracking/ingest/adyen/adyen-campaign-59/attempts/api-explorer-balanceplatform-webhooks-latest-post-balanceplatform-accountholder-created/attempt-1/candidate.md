---
title: "Adyen Balance Platform account holder created webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.accountHolder.created"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.accountHolder.created/2026-09-15.md"
tags: [adyen, webhooks, balance-platform, account-holders]
---

## Overview

Captured API Explorer reference for Adyen's incoming `balancePlatform.accountHolder.created` webhook. Adyen sends it when an account holder is successfully created. The event carries account-holder resource details; it does not itself establish that any requested capability has passed verification or that funds have moved. This is the 2026-09-15 capture at the `latest` URL, not a pinned API version.

## Key takeaways

- The webhook body marks top-level `data`, `environment`, and `type` required. The nested `data.accountHolder` object is marked optional in the table, while its `id` and `legalEntityId` properties are marked required within that object. `data.balancePlatform` and `timestamp` are optional in the webhook table. The account-holder `balancePlatform` description separately says the field is required in the *creation request* when API credentials span multiple balance platforms; this is not a webhook-body requirement.
- The account holder's `id` identifies the resource and `legalEntityId` identifies the associated legal entity against which Adyen performs verification. `reference` is the platform's optional reference; `migratedAccountHolderCode` is an optional Classic integration identifier.
- The optional `status` description gives `active`, `suspended`, and `closed`; `active` is described as the initial status, `suspended` blocks payouts, and `closed` permanently disables the account holder and its capabilities. The examples show `status: active` while capabilities are `allowed: false` and `verificationStatus: pending`. Creation or active status therefore does not prove a given capability is allowed.
- The second example includes capability `problems` for legal-entity and bank-account verification errors and transfer-instrument entries with pending verification. These are example payload details, not a promise that every creation event contains such errors or those instruments.
- The reference says to respond with any HTTP `2xx` to accept the webhook. It does not specify this event's delivery order, retry or deduplication behavior, signature verification, or financial settlement outcome. Use separately scoped guidance for those questions.

## Detail locators

- Trigger and event identity: raw lines 5–7, 95–98, 248–250.
- Body requiredness and resource identifiers: raw lines 11–32. Note the creation-request qualification on account-holder `balancePlatform` at line 16 and metadata omission warning at line 22; neither makes the field mandatory in the webhook body.
- Status, capability, and verification examples: raw lines 26–28, 59–92, 101–252. The examples differ in `test` versus `live` environment and their capability detail.
- Acknowledgment response: raw lines 253–261.

## Related

- [[adyen]]; [[adyen-webhooks]]; [[adyen-platforms]].

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.accountHolder.created/2026-09-15|2026-09-15 captured API Explorer reference]]
