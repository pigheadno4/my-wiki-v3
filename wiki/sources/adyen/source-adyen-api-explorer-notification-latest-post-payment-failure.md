---
title: "Adyen Notification POST /PAYMENT_FAILURE — Classic split booking failure"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Notification/latest/post/PAYMENT_FAILURE"
raw_files:
  - "adyen/api-explorer/Notification/latest/post/PAYMENT_FAILURE/2026-09-15.md"
tags: [adyen, classic-platforms, notifications, split-payments]
---

## Overview

This 2026-09-15 snapshot of Adyen Notification `latest` POST /PAYMENT_FAILURE describes an incoming notification when booking a split payment for a capture or refund fails. It is a Classic Platforms notification, not a merchant payment or refund API call. See [[adyen]] and [[adyen-classic-platforms]].

## Key takeaways

- The page says that when booking fails because an account has an invalid status or an `accountCode` is unknown, funds are credited or debited to or from the platform's liable account instead of the account in the split data. This describes allocation on the stated failure path, not whether an individual payment, capture, refund or subsequent reconciliation completed.
- The request-body table marks top-level `eventDate`, `eventType`, `executingUserKey`, `live` and `pspReference` required. It marks `content` and `error` optional. Within `content`, the four payment/modification merchant and PSP references are optional and identify capture/refund versus original payment; use the table at raw lines 11–33 for exact names and descriptions.
- The sole JSON example is labeled `paymentFailure` but sets `eventType` to `TRANSFER_FUNDS`; its `content` includes `invalidFields`, `amount`, account codes, `status` and `transferCode`, whereas the PAYMENT_FAILURE request table documents `errorFields`, `errorMessage` and payment/modification references. Treat this example as internally mismatched rather than a normative PAYMENT_FAILURE payload.
- The response section shows `200 Success` and an optional `notificationResponse` string to set to `[accepted]` to acknowledge receipt. That receiver acknowledgement is distinct from the booking outcome.

## Detail locators

- Notification purpose and liable-account fallback: raw lines 5–7.
- Complete request-body schema, including optional error fields and the live/test flag: raw lines 9–33. Optional parent objects do not make their child descriptions a required payload contract.
- Mismatched `paymentFailure` JSON example: raw lines 35–78. Response table and receipt acknowledgement: raw lines 79–87.

## Related

- [[adyen]] — provider context.
- [[adyen-classic-platforms]] — Classic split-payment and liable-account context.
- [[source-adyen-docs-classic-platforms-processing-payments]] — separate Classic split-processing guide.

## Raw Sources

- [[raw/adyen/api-explorer/Notification/latest/post/PAYMENT_FAILURE/2026-09-15|Adyen Notification latest POST /PAYMENT_FAILURE, captured 2026-09-15]]
