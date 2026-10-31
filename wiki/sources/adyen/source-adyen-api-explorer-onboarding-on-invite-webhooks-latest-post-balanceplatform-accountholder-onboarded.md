---
title: "Adyen onboarding-on-invite accountHolder.onboarded webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/onboarding-on-invite-webhooks/latest/post/balancePlatform.accountHolder.onboarded"
raw_files:
  - "adyen/api-explorer/onboarding-on-invite-webhooks/latest/post/balancePlatform.accountHolder.onboarded/2026-09-15.md"
tags: [adyen, platforms, onboarding, webhooks]
---

## Overview

This 2026-09-15-captured onboarding-on-invite webhook reference says Adyen sends `balancePlatform.accountHolder.onboarded` when a new account holder has been onboarded to the balance platform. The payload can contain references and IDs for resources Adyen created for that account holder, usable when processing payments or making payouts. It is an incoming event about onboarding and resource creation, not an instruction to initiate a payment or payout.

## Key takeaways

- The request-body table requires top-level `data`, `environment` (`test` or `live`), and `type`. `timestamp` is optional and describes queue time. Within required `data`, all listed resource objects and fields are marked optional, including `accountHolder`, primary `balanceAccount`, `balancePlatform`, `capabilities`, `creationDate` (event trigger time), `legalEntityId`, `merchantId`, `stores`, and `transferInstruments`. Do not make an example ID a required schema property.
- Resource identity is object-specific: `accountHolder.id`, `balanceAccount.id`, `balancePlatform`, `legalEntityId`, `merchantId`, store IDs, and transfer-instrument IDs name different resources. Store entries can carry a balance-account ID, business-line ID, split-configuration ID and payment-method list; transfer instruments can carry their own ID and associated balance-account ID. Follow the raw table and example for optional nested fields.
- `capabilities` is an optional map keyed by capability such as `receivePayments`; `allowed`, `enabled`, `requested`, and `verificationStatus` within each capability are optional. The TEST example shows `receivePayments` allowed/enabled/requested true and verification `valid`, but onboarding does not make those example values universal or prove any other account holder's verification or capability approval.
- The TEST example has a top-level `data.id` matching `accountHolder.id`, although the displayed request-body table does not list `data.id`. It also shows `balanceAccount.id` ending `0001` while a store's `balanceAccountId` ends `000001`; the example does not establish that these two strings match. Do not repair either discrepancy by inference.
- The response section says a receiver can return any `2xx` HTTP status to accept the webhook; its `notificationResponse: "[accepted]"` is an example response body, with the field marked optional. Receiver acceptance is separate from onboarding, verification, capability state, payment execution and payout bank receipt. No delivery, order, retry, deduplication or signature rule appears on this page.

## Detail locators

- Raw lines 5–9: onboarding trigger and created-resource reference purpose.
- Raw lines 13–50: body schema, optional resource/capability fields and time meanings.
- Raw lines 52–114: TEST sample IDs, capability values and resource association discrepancy.
- Raw lines 115–134: `2xx` acceptance and optional example response body.

## Related

- [[adyen]] — company route.
- [[adyen-platforms]] — account-holder onboarding and capability context.
- [[adyen-webhooks]] — receipt and family distinctions.

## Raw Sources

- [[raw/adyen/api-explorer/onboarding-on-invite-webhooks/latest/post/balancePlatform.accountHolder.onboarded/2026-09-15|accountHolder.onboarded reference, captured 2026-09-15]]
