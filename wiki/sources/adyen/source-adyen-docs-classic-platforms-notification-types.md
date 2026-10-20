---
title: "Adyen Classic Platforms notification types"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/notification-types"
raw_files:
  - "adyen/docs/classic-platforms/notification-types/2026-09-15.md"
tags: [adyen, classic-platforms, notifications, webhooks, payouts]
---

## Overview

This 2020-modified page captured 2026-09-15 catalogs notification event types for **Classic Adyen for Platforms**. It says messages go to endpoints configured by the platform and fields vary by event type. The page directs new implementations to a separate integration guide; these Classic event names are not the modern Platforms webhook contract. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The table covers Classic account/account-holder creation, closure, updates, status and verification; stores and deadlines; liable-account threshold and negative-balance compensation; direct debit, split-payment failure, transfer/refund requests, payout initiation, and report availability. It is an event-purpose index, not the payload schema or acknowledgment procedure for each event.
- `ACCOUNT_HOLDER_CREATED` can indicate either creation or an error during creation. `ACCOUNT_HOLDER_PAYOUT` is triggered on payout initiation and distinguishes `statusCode: Initiated` when the process started from `Failed` on error. An Initiated notification does not establish bank credit.
- `TRANSFER_FUNDS`, `REFUND_FUNDS_TRANSFER` and `SCHEDULED_REFUNDS` are described as triggered when the corresponding Fund API request is made. Their catalog entries do not by themselves prove transfer or refund completion. `DIRECT_DEBIT_INITIATED` likewise indicates initiation.
- `COMPENSATE_NEGATIVE_BALANCE` describes an end-of-month check for accounts with a negative balance one month old; when found, Adyen compensates from the liable platform account and sends the notification. This is a specific liable-account funds-direction statement, not evidence of a particular platform's balance or debit.

## Detail locators

- Classic-only boundary, configured endpoint and varying fields: raw lines 19–23. Full event-purpose table: lines 25–45.
- Account and account-holder events, liable-account threshold, payout statuses and verification: raw lines 27–37. Beneficiary setup and conditional negative-balance compensation: lines 38–39.
- Direct debit, split-payment failure, Fund API request-triggered transfer/refund events and report availability: raw lines 40–45. For endpoint configuration and acknowledgments, use [[source-adyen-docs-classic-platforms-configure-notifications]] as a separate guide.

## Related

- [[adyen]] — provider.
- [[adyen-classic-platforms]] — Classic integration context.
- [[source-adyen-docs-classic-platforms-configure-notifications]] — configuration, acknowledgment and retry navigation.
- [[adyen-platforms]] — separate modern Platforms model.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/notification-types/2026-09-15|Classic notification types — 2026-09-15 snapshot]]
