---
title: "Adyen Onboarding on invite webhooks v1 overview"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/onboarding-on-invite-webhooks/latest/overview"
raw_files:
  - "adyen/api-explorer/onboarding-on-invite-webhooks/latest/overview/2026-09-15.md"
tags: [adyen, webhooks, platforms, onboarding]
---

## Overview

This 2026-09-15 snapshot is Adyen's **Onboarding on invite webhooks v1** overview. Adyen says it sends these webhooks to notify a platform system when a new account holder is onboarded in its balance platform through the onboarding on invite flow. [[adyen]] [[adyen-webhooks]] [[adyen-platforms]]

## Key takeaways

- The catalog lists one `POST` event route, `balancePlatform.accountHolder.onboarded`, summarized as “Account holder onboarded.”
- This overview is a family and endpoint directory. It does not define that event's payload, resource identifiers, required fields, webhook response, timing, delivery, retry, ordering, deduplication, signature, verification or capability status. The event reference supplies event-specific payload, identifiers, capability fields and response details; delivery, ordering, retry, deduplication, signature, and current verification or eligibility need separate evidence.
- The “onboarded” event label does not itself establish current account-holder verification, active capabilities, payment execution, or payout eligibility.

## Detail locators

- Family identity and purpose: pinned raw lines 5–7.
- Endpoint method, path and summary: pinned raw lines 9–14.

## Related

- [[adyen]]
- [[adyen-webhooks]]
- [[adyen-platforms]]

## Related raw API references

- `raw/adyen/api-explorer/onboarding-on-invite-webhooks/latest/post/balancePlatform.accountHolder.onboarded/2026-09-15.md` — event-specific reference; not evidence for this entry.

## Raw Sources

- [[raw/adyen/api-explorer/onboarding-on-invite-webhooks/latest/overview/2026-09-15|Adyen Onboarding on invite webhooks v1 overview (2026-09-15)]]
