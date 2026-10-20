---
title: "Adyen Classic Platforms: Configure Score risk-signal notifications"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/identify-account-holder-risk/configure-notifications-for-risk-signals"
raw_files:
  - "adyen/docs/classic-platforms/identify-account-holder-risk/configure-notifications-for-risk-signals/2026-09-15.md"
tags: [adyen, classic-platforms, score, risk-signals, notifications]
---

## Overview

This 2022-modified, 2026-09-15-captured **Classic Adyen for Platforms** guide explains how to subscribe a platform server to `SCORE_SIGNAL_TRIGGERED` notifications when a new Score risk signal triggers for an account holder. It covers Classic Notification API configuration and a test example, not case adjudication or automatic payout/processing restriction. The companion [[source-adyen-docs-classic-platforms-identify-account-holder-risk|Score overview]] says a high score is not confirmed fraud and the platform owns review/action. See [[adyen]] and [[adyen-classic-platforms]].

## Key takeaways

- Create a notification configuration or update an existing one. The event configuration uses `eventType: SCORE_SIGNAL_TRIGGERED` with `includeMode: INCLUDE`, plus the server `notifyURL`. On update, `notificationId` identifies the configuration to change. The examples use Classic Notification API v6 **TEST** endpoints.
- **After completing setup, notify Adyen so it can turn on the webhook notification.** A configuration API response alone does not establish that risk-signal delivery has been enabled or a live signal has been received.
- The create example sends `active: false` but shows `active: true` in its response (pinned raw lines 40–49 versus 55–69). The update example sends and returns `active: false`. Treat these as inconsistent illustrations, not a reliable active-state transition rule; verify configuration behavior against the applicable API contract.
- The sample `SCORE_SIGNAL_TRIGGERED` body is marked `live: "false"` and contains `accountHolderCode`, `riskScore: 80` and `scoreSignalsTriggered: ["EmailSyntaxCheck"]`. These fields identify a test notification and a signal for investigation; they do not establish confirmed fraud, a disabled payout, or any completed account action.

## Detail locators

- Pinned raw lines 15–27: Classic scope, optional risk-signal subscription, event type, create/update choices and Adyen activation step.
- Pinned raw lines 29–70: create API, TEST request/response and `active` mismatch.
- Pinned raw lines 72–124: update API, `notificationId`, event inclusion and inactive TEST example.
- Pinned raw lines 126–147: sample event metadata, `live`, account-holder code, score and signal name.

## Related

- [[adyen-classic-platforms]] — Classic account-holder and notification context.
- [[source-adyen-docs-classic-platforms-identify-account-holder-risk]] — Score risk interpretation and platform-owned actions.
- [[source-adyen-docs-classic-platforms-configure-notifications]] — general Classic notification setup and handling.
- [[adyen-platforms]] — newer model with separate risk notifications.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/identify-account-holder-risk/configure-notifications-for-risk-signals/2026-09-15|Classic Score notification configuration guide, captured 2026-09-15]]
