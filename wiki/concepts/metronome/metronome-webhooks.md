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

## Sources

- [[source-metronome-guides-platform-configuration-setup-webhooks]] — event families, delivery semantics, deduplication, and signature verification

## Related

- [[metronome-customers-and-contracts]]
- [[metronome-invoicing]]
- [[metronome-usage-based-billing]]
