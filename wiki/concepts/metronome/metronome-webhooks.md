---
title: "Metronome Webhooks"
type: concept
category: technology
tags: [metronome, webhooks, notifications, integrations]
---

## Definition

Metronome webhooks deliver HTTP POST notifications when billing and configuration events occur. Documented event families include usage thresholds, contract and balance-object lifecycle events, invoices, integration failures, marketplace disablement, and payment-gating workflows.

## Delivery model

A receiver must expose a public HTTPS endpoint and return a successful status such as `200 OK`. Responses above `299` trigger exponential-backoff retries that eventually settle at a 15-minute cadence and can continue until two days after the initial attempt. Metronome recommends storing the payload, acknowledging it, and processing it asynchronously.

Retries and multiple configured destinations can produce duplicate deliveries. Consumers should therefore use the notification `id` as a deduplication key.

## Authenticity and authoritative data

Webhook payloads contain minimal event information. A consumer can treat the notification as a change hint and retrieve authoritative details from the corresponding Metronome API, or verify the webhook directly.

For signature verification, compute HMAC-SHA256 over `X-Metronome-Date`, a newline, and the exact request-body bytes using the secret unique to that webhook. Compare the result with `Metronome-Webhook-Signature`, reject requests older than five minutes, and avoid reserializing parsed JSON before verification.

## Payload evolution

Metronome may add backward-compatible fields without notice. Integrations should validate the documented fields they require rather than rejecting payloads solely because additional fields appear.

The dashboard quickstart identifies payment-status webhooks as the notification path for payment-gated commits; the dedicated webhook guide remains the authority for delivery and verification mechanics.

The architecture guide also says incoming usage can trigger alert and threshold evaluation and webhooks. This is an architectural timing statement, not a delivery guarantee; retry, deduplication, and verification behavior remains governed by the dedicated webhook guide.

For prepaid balance thresholds, `payment_gate.threshold_reached` marks the trigger, `payment_gate.payment_status` reports `paid` or `failed`, and `payment_gate.payment_pending_action_required` signals that intervention is needed. External payment gates additionally use `payment_gate.external_initiate`; the integrator must retain its `workflow_id` to release or cancel the pending commit.

## Sources

- [[source-metronome-guides-platform-configuration-setup-webhooks]] — event families, delivery semantics, deduplication, and signature verification
- [[source-metronome-guides-get-started-metronome-dashboard-quickstart]] — payment-status notification use for payment-gated commits
- [[source-metronome-guides-customers-billing-optimize-customer-experience-prepaid-balance-thresholds]] — threshold, payment-status, action-required, and external-initiation events
- [[source-metronome-guides-get-started-how-metronome-works]] — event-time alert evaluation boundary

## Related

- [[metronome-customers-and-contracts]]
- [[metronome-invoicing]]
- [[metronome-usage-based-billing]]
