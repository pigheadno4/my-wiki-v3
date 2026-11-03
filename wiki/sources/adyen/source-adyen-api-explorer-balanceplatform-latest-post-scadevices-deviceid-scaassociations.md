---
title: "POST /scaDevices/{deviceId}/scaAssociations — Create SCA device associations | Adyen Balance Platform API"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/post/scaDevices/(deviceId)/scaAssociations"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/post/scaDevices/(deviceId)/scaAssociations/2026-11-03.md"
tags: [adyen, balance-platform-api, sca, device-association, api-reference]
---

## Overview

This 2026-11-03-captured Balance Platform API `/bcl/v2` reference creates associations between an SCA-enabled device and specified entities. It lists the TEST server `https://balanceplatform-api-test.adyen.com/bcl/v2`; it does not list a live server or prove account-specific access. [[adyen]] [[adyen-business-accounts]] [[adyen-issuing]]

## Key takeaways

- `POST /scaDevices/{deviceId}/scaAssociations` requires the string path `deviceId`, the SCA device being associated. The request body requires an `entities` array; each entity object requires an `id` and a `type` of `accountHolder`, `legalEntity`, or `paymentInstrument`. The example uses one account-holder ID, but does not set a cardinality limit for the array.
- `201 Success` says association created and returns required `scaAssociations` array entries with `entityId`, `entityType`, `scaDeviceId`, and `status` (`active` or `pendingApproval`). A created association may be `pendingApproval` when the account holder has existing devices, so creation does not guarantee immediate readiness for use.
- When the entity allows only one associated device **and** single-device replacement is enabled for the account, the new association immediately replaces the existing one: the new status is `active`, and the prior device is no longer associated. The captured reference does not specify the approval procedure or timing for a pending association, nor does it establish device registration completion, an authenticated user action, payment authorization, or a transfer outcome.
- The operation lists `400` invalid input, `401` authentication, `403` permissions, `404` device not found, `422` validation, and `500` server errors. Their error-body fields are mostly optional in the captured table. The page specifies no endpoint-specific idempotency, version/conflict, reversal, or default behavior.

## Detail locators

- Purpose and conditional association/replacement status: raw lines 5–10.
- Required path and body fields, allowed entity types, and one-entity request example: raw lines 12–39.
- `201` response fields and status values: raw lines 40–52; example `pendingApproval` response: raw lines 168–183.
- Error response classes and optional error-body fields: raw lines 55–166.

## Related

- [[adyen-business-accounts]] — SCA device context for Business Accounts.
- [[adyen-issuing]] — separate issued-card SCA device context.
- [[source-adyen-api-explorer-balanceplatform-latest-delete-scaassociations]] — separate association deletion reference; deleting an association is distinct from device deregistration.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/post/scaDevices/(deviceId)/scaAssociations/2026-11-03|POST SCA device associations captured 2026-11-03]]
