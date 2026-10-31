---
title: "Adyen Management Webhooks v3 overview"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/ManagementNotification/latest/overview"
raw_files:
  - "adyen/api-explorer/ManagementNotification/latest/overview/2026-09-15.md"
tags: [adyen, management-webhooks, management-api, terminals]
---

## Overview

This 2026-09-15 Adyen API Explorer snapshot labels the `ManagementNotification/latest` family **Management Webhooks v3**. Adyen says these webhooks notify a merchant system about events affecting Adyen company and merchant accounts, stores, payment terminals, and payment methods when using Management API. When an event occurs, Adyen sends an HTTP POST with event details to a URL on the merchant server. This is a catalog, not an individual event payload contract. See [[adyen]], [[adyen-webhooks]], and [[adyen-terminal-management]].

## Key takeaways

- The listed POST routes cover `merchant.created`, `merchant.updated` (merchant account capability updated), `paymentMethod.created`, `paymentMethodRequest.removed`, `paymentMethodRequest.scheduledForRemoval`, `terminalAssignment.completed`, `terminalBoarding.triggered` (result of terminal boarding), and `terminalSettings.modified`. The route names and summaries identify event subjects; they do not supply payload requiredness, status semantics, or delivery guarantees.
- `terminalAssignment.completed`, `terminalBoarding.triggered`, and `terminalSettings.modified` are Management Webhooks concerning terminal administration. They are distinct from Standard transaction webhooks and terminal-generated messages. An event listing alone does not prove a particular terminal's state, capability, or payment readiness.

## Detail locators

- Pinned raw, lines 5–11: family/version label, scope and HTTP POST direction.
- Pinned raw, lines 13–25: eight General endpoint names and one-line summaries. Open the individual event reference for field and response rules.

## Raw Sources

- [[raw/adyen/api-explorer/ManagementNotification/latest/overview/2026-09-15|Management Webhooks v3 API Explorer overview, captured 2026-09-15]]
