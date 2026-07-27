---
title: "Metronome Webhooks"
type: source
date_ingested: 2026-07-27
original_format: webpage
raw_files:
  - "metronome/guides/platform-configuration/setup-webhooks-2026-07-13.md"
tags: [metronome, webhooks, platform-configuration, integrations]
---

## Overview
This Metronome documentation page describes the webhook events it can deliver and how a receiving service should acknowledge, deduplicate, and verify them. It covers billing and marketplace events as well as payment-gating workflows, and documents a custom HTTPS handler or a Slack destination as delivery options.

## Key takeaways
- Threshold alerts, contract/commit/credit system notifications, offset notifications, invoice events, integration issues, marketplace disablement, and payment-gating events are documented webhook categories.
- A public HTTPS handler must return a successful response such as `200 OK`; delivery failures are retried with exponential backoff, ultimately at a 15-minute cadence for up to two days.
- Consumers should deduplicate using the notification `id`, because retries and multiple configured destinations can produce duplicate deliveries.
- A consumer can obtain authoritative details from the Metronome API or verify the `Metronome-Webhook-Signature` against the raw request bytes.

## Details
### Event coverage and configuration
Threshold notifications use `alerts.<notification_type>` and monitor real-time metrics when defined thresholds are crossed. System notifications cover contract, commit, and credit events; offset notifications can be scheduled relative to a known object date. `invoice.finalized` occurs after the grace period and requires setup through a Metronome representative. The Stripe-only `invoice.billing_provider_error` is automatically sent when a destination is configured and the Stripe integration is enabled, but it does not cover errors that reside entirely within Stripe. The page also documents `integration.issue`, marketplace-metering-disabled events for AWS, Azure, and GCP, and payment-gating events for threshold, status, required action, and externally initiated workflows.

### Delivery and duplicate handling
Metronome requires a publicly accessible HTTPS endpoint. Status codes above `299` trigger retries; an unacknowledged notification is retried with exponential backoff until a 15-minute cadence, then until acceptance or two days from the initial attempt (about 200 retries). The page recommends queuing a payload, returning `200`, then validating or processing it asynchronously. It cautions that delivery may repeat after retries or when multiple webhook URLs are configured; use the event `id` to deduplicate. The published webhook IP list may change, with at least 30 days' notice.

### Authenticity and payload evolution
Webhooks contain minimal event information, so the page suggests fetching full data from the corresponding Metronome API endpoint when appropriate. Alternatively, compute HMAC-SHA256 over `X-Metronome-Date`, a newline, and the exact request-body bytes using the per-webhook secret, then compare it with `Metronome-Webhook-Signature`. Prefer `X-Metronome-Date` to `Date`, reject requests older than five minutes, and do not reserialize parsed JSON before signature verification. Metronome may add backward-compatible fields without notice, so consumers should validate only fields expected by the documented integration.

### Slack delivery
Instead of building a custom handler, a team can create a Slack incoming webhook, add it as a Metronome webhook destination, configure a test notification, and trigger that notification to confirm delivery in the Slack channel.

## Related
- Companies: [[metronome]]
- Concepts: [[metronome-webhooks]]

## Raw Sources
- [[setup-webhooks-2026-07-13]] — verbatim Metronome documentation page
