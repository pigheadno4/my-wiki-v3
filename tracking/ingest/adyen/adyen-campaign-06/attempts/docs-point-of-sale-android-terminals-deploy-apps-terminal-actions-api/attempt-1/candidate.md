---
title: "Schedule terminal actions to deploy Android apps and certificates"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/android-terminals/deploy-apps/terminal-actions-api"
raw_files:
  - "adyen/docs/point-of-sale/android-terminals/deploy-apps/terminal-actions-api/2026-09-15.md"
tags: [adyen, point-of-sale, android-terminals, management-api, app-deployment, terminal-actions]
---

## Overview

Adyen's dated Management API guide explains how to schedule installation or removal of an Android app, app version, or certificate on Adyen Android payment terminals. This is terminal fleet administration for a Terminal API integration or standalone solution, separate from Terminal API payment messaging and merchant-phone Mobile SDK use. The guide's test-endpoint and language-library snippets illustrate requests; they do not establish a live deployment outcome or current model/firmware eligibility. [[adyen]] [[adyen-terminal-api]]

## Key takeaways

- An API credential needs an API key and Management API roles for Terminal actions read, Terminal actions read and write, and Terminal settings read. The hardware scope is Android payment terminals. Live scheduling endpoints have rate limits. See `## Requirements` in the pinned raw.
- The guide first routes app requirements and Customer Area upload; Adyen signs and converts uploaded apps, and signs uploaded certificates where needed. The company-level GET endpoints list uploaded apps or certificates in `ready` status and provide their IDs; `ready` is an upload state, not proof of installation. See `## Android terminal actions` and `## 1. Get Android app and certificate IDs`.
- Android actions bypass the ordinary restart-hour wait (06:00 AM by default for other configuration changes). Without `scheduledAt`, an action takes effect at the next maintenance call, or immediately if WebSockets are enabled. With a date/time, it takes effect at the first maintenance call after that time in the terminal's time zone, or at the specified time if WebSockets are enabled. Keep terminals on and network-connected overnight as Adyen recommends for maintenance. An affected app that is open closes when the action runs. See `## When planned actions take effect`.
- A scheduling request specifies one action for up to 100 terminal IDs. If any terminal ID fails validation, none are scheduled; after IDs pass validation, the response can still report per-terminal scheduling failures. An optional `storeId` must match the terminals' assigned store. `totalScheduled` counts planned actions, not completed actions. See `## 3. Schedule an Android terminal action`.
- A returned `TRAC` action ID can be queried for `pending`, `successful`, `failed`, or `cancelled` status and a result when present. Details are available for actions you planned, not Adyen-planned actions. See `## Get terminal action details`.

## Detail locators

- `## 1. Get Android app and certificate IDs`: GET `/companies` for company identity, then company-level `/androidApps` or `/androidCertificates` for ready IDs; response fields, pagination and dated library examples.
- `## 2. Get terminal IDs`: GET `/terminals`, filters by merchant, store, country and brand model, paginated response, and terminal ID extraction. Its S1E/S1F2 and firmware values are examples, not a universal compatibility list.
- `## 3. Schedule an Android terminal action`: POST `/terminals/scheduleActions`, `terminalIds`, optional `storeId` and `scheduledAt`, app/certificate `actionDetails`, 422 `invalidFields` reasons, and `totalScheduled`/`totalErrors`/`items` response interpretation.
- `## Get terminal action details`: GET `/companies/{companyId}/terminalActions/{actionId}`, action status and result fields. The raw curl example omits the company ID in its displayed URL; use the linked endpoint shape rather than copying that example as an authoritative path.

## Related

- [[adyen-terminal-api]] — distinguishes payment messaging from Management API terminal administration.
- [[adyen-pos-store-management]] — related Management API store administration, including assignment and store identity; it does not define this Android app deployment action.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/android-terminals/deploy-apps/terminal-actions-api/2026-09-15|Adyen schedule terminal actions to deploy apps, fetched 2026-09-15]]
