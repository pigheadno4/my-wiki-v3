---
title: "Adyen ManagementNotification: merchant.updated"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/ManagementNotification/latest/post/merchant.updated"
raw_files:
  - "adyen/api-explorer/ManagementNotification/latest/post/merchant.updated/2026-09-15.md"
tags: [adyen, management-notification, webhooks, merchant-accounts, verification, capabilities]
---

## Overview

This 2026-09-15 API Explorer `ManagementNotification/latest` reference defines the incoming `merchant.updated` webhook for changes to a merchant account's verification status and capabilities. When verification fails, the notification can include errors and possible remediation actions. It concerns a merchant-account resource and its capability settings, not a payment transaction or proof that processing and payouts are ready.

## Key takeaways

- The body table marks top-level `createdAt`, `data`, `environment`, and `type` required. Within `data`, `capabilities`, `merchantId`, and merchant-account `status` are marked required; `legalEntityId` is optional. For each capability value, `requested` and `requestedLevel` are marked required, while `allowed`, `allowedLevel`, `capability`, `problems`, `verificationDeadline`, and `verificationStatus` are optional. See **Parameters → Request body**, raw lines 11–29.
- `capabilities` is keyed by capability. The page uses `sendToTransferInstrument` as a payout-to-bank-account example and `receivePayments` in its payload examples. An optional `allowed: true` indicates successful verification for that capability; `verificationStatus` can be `pending`, `invalid`, `valid`, or `rejected`. A `problems` array can carry verification errors and remediation actions. The examples illustrate these structures, not a universally present problem list. See raw lines 16–24 and 33–124.
- Merchant-account `status` is separate from capability verification. The status table says `PreActive` cannot process payments; `Active` permits Customer Area access and, if the company account is also Active, enables processing and payouts. `InactiveWithModifications` disallows new payments but permits modifications and payouts; `Inactive` disables processing and payouts; `Closed` is irreversible. The `merchant-updated-valid` example has `receivePayments.allowed: true` and `verificationStatus: valid` while `status` remains `PreActive`, so it is not proof of payment readiness. See raw lines 27 and 33–53.
- The response section says the request succeeded at `200 Success` and marks `notificationResponse` optional; any `2xx` HTTP status accepts the webhook. Receiver acceptance does not establish a merchant-account transition, capability approval, a payment, or a payout. This page states no delivery-order, retry, deduplication, or signature-verification rule. See raw lines 125–133.

## Detail locators

- **Parameters → Request body, raw lines 11–29** — requiredness, capability fields and verification states, merchant/legal-entity identities, merchant-account status definitions, environment and event type.
- **Request examples → merchant-updated-valid, raw lines 33–53** — TEST example with valid allowed `receivePayments` capability and `PreActive` merchant account.
- **Request examples → merchant-updated-with-errors, raw lines 55–124** — TEST example with `allowed: false`, invalid verification, legal-entity problem, error codes, and nested remediation actions.
- **Responses, raw lines 125–133** — `200 Success`, optional `notificationResponse`, and any-`2xx` webhook acceptance.

## Related

- [[adyen]]
- [[adyen-account-structure]]
- [[adyen-webhooks]]
- [[source-adyen-api-explorer-management-latest-overview]] — Management API context for merchant-account operations; its API requests are separate from this notification.

## Raw Sources

- [[raw/adyen/api-explorer/ManagementNotification/latest/post/merchant.updated/2026-09-15|Adyen API Explorer — merchant.updated (2026-09-15)]]
