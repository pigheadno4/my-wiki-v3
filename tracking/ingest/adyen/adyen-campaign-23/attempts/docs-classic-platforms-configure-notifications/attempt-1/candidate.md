---
title: "Adyen Classic Platforms: Configure notifications"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/configure-notifications"
raw_files:
  - "adyen/docs/classic-platforms/configure-notifications/2026-09-15.md"
tags: [adyen, classic-platforms, notifications, webhooks]
---

## Overview

This 2021-modified guide captured 2026-09-15 configures notification webhooks for **Classic Adyen for Platforms**. It says Classic Platforms API create, update and delete requests are asynchronous, so the final result is learned from notifications delivered to configured server URLs. The guide directs new implementations to a separate integration guide; its Notification API should not be substituted for modern Platforms webhooks. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- POST `/createNotificationConfiguration` supplies a delivery URL and chosen notification event types. The Classic Notification v6 test-host examples also show API-version, active, include/exclude event selection and optional credentials/protocol fields. The page gives POST endpoints to retrieve one configuration by `notificationId`, list all with an empty request, update settings by `notificationId`, and delete configurations by `notificationIds`. Deletion is an explicit removal action; do not infer ongoing delivery to a removed configuration.
- The receiving server should acknowledge each notification with literal `[accepted]`. The page describes at-least-once delivery: without acknowledgment within 10 seconds, Adyen queues notifications to that endpoint and retries at increasing intervals, then every eight hours for the following seven days. At-least-once delivery means consumers must allow for repeat delivery; an initial API response or test sample is not a final business-operation outcome.
- POST `/testNotificationConfiguration` targets a `notificationId`; an empty `eventTypes` array generates all configured types for the test. Its successful and failed example responses are test diagnostics, not proof that a particular live endpoint is subscribed, acknowledging, or processing real events.
- Example consistency warning: the create request sets `apiVersion: 6` and `sslProtocol: SSL`, while the shown response says `apiVersion: 5` and `SSLInsecureCiphers`. The update example repeats this 6/5 and protocol mismatch. The get-one example requests `notificationId: 20272` but returns `2`. Treat these as conflicting sample values, not a demonstrated transformation rule.

## Detail locators

- Classic scope and asynchronous-final-result rule: raw lines 19–31. Create endpoint and test-host request/response: 33–90; conflicting `apiVersion`/protocol fields: 45, 61, 73, 87.
- Get-one by ID, get-list and update operations: raw lines 92–243. Get-one ID mismatch: lines 103 and 124. Update request/response API-version and protocol mismatch: lines 197, 214, 226, 240. Delete by ID array: lines 245–266.
- Literal acknowledgment, 10-second queue/retry behavior and seven-day schedule: raw lines 268–289. Test endpoint, empty event-type behavior and example diagnostics: lines 291–371. HMAC-signature navigation only: lines 373–381.

## Related

- [[adyen]] — provider.
- [[adyen-classic-platforms]] — Classic account-holder integration context.
- [[adyen-platforms]] — separate modern Platforms model.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/configure-notifications/2026-09-15|Classic notification configuration — 2026-09-15 snapshot]]
