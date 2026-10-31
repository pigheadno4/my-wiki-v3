---
title: "Adyen Configuration webhooks v2 overview"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/overview"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/overview/2026-09-15.md"
tags: [adyen, webhooks, balance-platform, configuration]
---

## Overview

Captured API Explorer overview headed **Configuration webhooks v2**. Adyen describes events on a platform, including account-holder capability changes and sweep-configuration changes, for which it sends an HTTP POST with event details to a URL on the receiver's server. The `POST` rows below describe incoming webhook types, not merchant-initiated API calls. See [[adyen]], [[adyen-webhooks]], and [[adyen-platforms]].

## Key takeaways

- The catalog lists account-holder, balance-account, recurring-top-up, managed-payout-schedule, sweep, card-order, mandate, network-token, payment-instrument, and score-signal events. It distinguishes create/update/delete event names where listed, plus payout-schedule automatic-application failure and execution failed/skipped/succeeded names. These are route labels and summaries; the overview does not define event payload fields or what each named outcome proves.
- The page suggests using webhook information to update internal statuses when a capability status changes. That example does not define a required status transition or establish verification, authorization, transfer booking, payout settlement, or bank receipt.
- The captured heading names v2 while the trusted URL contains `latest`; this snapshot alone does not prove a currently served version. The overview does not specify event delivery order, retry or deduplication behavior, authentication or signature rules, or failure/reversal semantics beyond the listed event names. Follow the individual event reference and relevant webhook guidance for those details.

## Detail locators

- Family name, sender, receiver, POST direction and illustrative uses: pinned raw lines 5–10.
- `## Endpoints` → `### General`: event names and summaries, pinned raw lines 12–45.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/overview/2026-09-15|Captured Configuration webhooks v2 overview (2026-09-15)]]
