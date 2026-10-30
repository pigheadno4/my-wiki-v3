---
title: "Adyen Balance Platform API v2: approve a pending SCA association"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/scaAssociations"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/patch/scaAssociations/2026-09-15.md"
tags: [adyen, balance-platform, sca, api-reference]
---

## Overview

Captured Adyen Balance Platform API reference for `PATCH /scaAssociations` on the listed test `bcl/v2` server. It describes approving a previously created association in `pendingApproval`, linking an SCA device to an `accountHolder`, `legalEntity`, or `paymentInstrument`. This is an association-approval operation, not proof of a separate user authentication, account verification, card payment, or funds movement. See [[adyen]], [[adyen-platforms]], [[adyen-business-accounts]], and [[adyen-issuing]].

## Key takeaways

- The header table marks `WWW-Authenticate` required for authenticating through SCA (raw lines 14–17). The request-property table marks `entityId`, `entityType`, `scaDeviceIds`, and `status` required; the listed `entityType` values are `accountHolder`, `legalEntity`, and `paymentInstrument`, while `status` lists `active` and `pendingApproval` (lines 20–26). The page does not separately state request-body requiredness or define the authentication challenge procedure.
- The operation summary says it approves a previously created pending association; the example submits `status: active`. The property enum alone does not establish that submitting `pendingApproval` approves anything or define any other transition (lines 5–7, 23–39).
- A `200 Success` is labeled successful approval and returns `scaAssociations` with entity/device IDs, entity type, and status (lines 41–53). The documented `401`, `403`, and `500` cases are authentication required, insufficient permissions, and server processing failure (lines 56–110). No specific role name, live endpoint, propagation timing, idempotency, or downstream financial outcome is established here.

## Detail locators

- Request example: raw lines 28–40. Response schema and example: lines 41–53 and 112–128. Error response fields: lines 56–110.

## Related

- [[adyen-platforms]] — balance-platform context.
- [[adyen-business-accounts]] — related SCA device guidance for Business Accounts.
- [[adyen-issuing]] — related SCA device guidance for issuing cards.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/patch/scaAssociations/2026-09-15|PATCH /scaAssociations API reference, captured 2026-09-15]]
