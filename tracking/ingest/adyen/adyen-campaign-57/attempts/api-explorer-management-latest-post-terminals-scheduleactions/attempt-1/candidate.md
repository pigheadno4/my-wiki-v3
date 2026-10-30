---
title: "Adyen Management API v3: schedule terminal actions"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/terminals/scheduleActions"
raw_files:
  - "adyen/api-explorer/Management/latest/post/terminals/scheduleActions/2026-09-15.md"
tags: [adyen, management-api, terminals, terminal-actions, scheduling, api]
---

## Overview

This 2026-09-15-captured Management API v3 reference documents `POST /terminals/scheduleActions`, which schedules one action for specified terminals. The listed server is `https://management-test.adyen.com/v3`. An API credential needs the **Management API—Terminal actions read and write** role. Scheduling acknowledgement is distinct from an action taking effect on a terminal. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- The endpoint accepts **one action per request** and at most **100 terminal IDs**. If one or more terminal IDs has an error, the page says the action is scheduled for none of the terminals; fix the IDs and retry. Optional `storeId`, when present, requires all listed terminals to be assigned to that store. The body table marks `actionDetails`, `scheduledAt`, `storeId` and `terminalIds` individually **not required**; do not convert the examples into a stricter schema. The `actionDetails` type and allowed action list are not expanded in this capture.
- `scheduledAt` is described as RFC 3339 without `Z` before the time offset, with an example such as `2021-11-15T12:16:21+0100`. The action is sent with the first terminal maintenance call after the specified time in the terminal's time zone; an empty value sends it as soon as possible at the next maintenance call. A scheduled time is therefore not proof of execution at that instant.
- The `200` response can include an `items` list of per-terminal action `id` and `terminalId`, `terminalsWithErrors`, `totalErrors` and `totalScheduled`. The page explicitly says `totalScheduled` does **not** mean the action has happened. The examples show `InstallAndroidApp` with an `appId` and `UninstallAndroidCertificate` with a `certificateId`; these are illustrated action types, not a complete allowed-value list. The `verification-error` example returns `422` for empty terminal IDs.
- The page notes live-environment rate limits without numbers. It lists `400`, `401`, `403`, `422` and `500` errors. For action status and eventual outcome, use the separate [[source-adyen-docs-point-of-sale-android-terminals-deploy-apps-terminal-actions-api|Android terminal actions guide]], which describes querying an action ID; this scheduling response alone does not prove installation, removal, device connectivity, payment readiness or transaction success.

## Detail locators

- Purpose, one-action/100-ID limits, all-or-none terminal-ID error rule, role and v3 test server: raw lines 5–24.
- Request-body fields and maintenance-call timing: lines 26–34.
- Android app/certificate request examples and empty-ID example input: lines 36–87.
- `200` scheduled-action identifiers, errors and counts: lines 88–104.
- Error schema: lines 107–204; illustrative responses: lines 206–279.

## Related

- [[adyen-terminal-management]] — terminal fleet administration.
- [[adyen-android-terminals]] — Android app/certificate deployment context.
- [[source-adyen-docs-point-of-sale-android-terminals-deploy-apps-terminal-actions-api]] — separate planning, timing and action-status guide.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/terminals/scheduleActions/2026-09-15|POST /terminals/scheduleActions API Explorer capture]]
