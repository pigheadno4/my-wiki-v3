---
title: "Adyen Management Notification: merchant.created"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/ManagementNotification/latest/post/merchant.created"
raw_files:
  - "adyen/api-explorer/ManagementNotification/latest/post/merchant.created/2026-09-15.md"
tags: [adyen, management, webhooks, merchant-accounts]
---

## Overview

Captured API Explorer `ManagementNotification/latest` `POST merchant.created` reference for an incoming notification that a merchant account was created. Its `POST` heading describes webhook delivery, not a merchant-account creation request. The event describes a Management merchant account, with company and merchant IDs; it does not by itself establish legal-entity verification, allowed capabilities, Customer Area access, payment processing, or payout readiness. The `latest` label gives no numbered version. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- The body table marks `createdAt`, `data`, `data.capabilities`, `data.companyId`, `data.merchantId`, `data.status`, `environment`, and `type` required. `data.legalEntityId` is optional. `environment` can be `test` or `live`; the example has `type: "merchant.created"` and `status: "PreActive"`.
- Capability entries are keyed by capability name. Within an entry, `requested` and `requestedLevel` are marked required; `allowed`, `allowedLevel`, `capability`, `problems`, `verificationDeadline`, and `verificationStatus` are optional. `requested` describes what was asked for, while `allowed` describes permission after successful verification. The example requests `sendToTransferInstrument` but does not show `allowed` or `verificationStatus`; it is not payout authorization.
- The merchant status governs readiness: `PreActive` has been created but has no Customer Area access or payment processing; `Active` gives access, with payment processing and payouts enabled **if the company account is also Active**; `InactiveWithModifications` cannot process new payments but can modify payments and receive payouts; `Inactive` disables payment processing and payouts; `Closed` is irreversible and disables login, payment processing, and payouts. The example's `PreActive` cannot be treated as an active merchant account.
- The `200` response section says the request succeeded, while the optional `notificationResponse` row says any HTTP `2xx` accepts the webhook. That is receiver acceptance, separate from the merchant resource's status or capability verification. This page gives no delivery, ordering, retry, deduplication, signature, or later activation guarantee.

## Detail locators

- Event identity: raw lines 5–7.
- Required envelope, capabilities, identities, statuses, and environment: raw lines 11–30.
- Illustrative `PreActive` merchant and requested capability: raw lines 32–52.
- HTTP response and optional body field: raw lines 53–61.

## Related

- [[adyen]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/api-explorer/ManagementNotification/latest/post/merchant.created/2026-09-15|Captured merchant.created Management notification]]
