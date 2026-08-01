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

The notification lifecycle guide confirms asynchronous JSON delivery for all notification types over HTTPS POST. It describes exponential-backoff retries with jitter for up to 48 hours and at-least-once delivery, so receivers must tolerate duplicates and make processing idempotent.

## Authenticity and authoritative data

Webhook payloads contain minimal event information. A consumer can treat the notification as a change hint and retrieve authoritative details from the corresponding Metronome API, or verify the webhook directly.

For signature verification, compute HMAC-SHA256 over `X-Metronome-Date`, a newline, and the exact request-body bytes using the secret unique to that webhook. Compare the result with `Metronome-Webhook-Signature`, reject requests older than five minutes, and avoid reserializing parsed JSON before verification.

## Payload evolution

Metronome may add backward-compatible fields without notice. Integrations should validate the documented fields they require rather than rejecting payloads solely because additional fields appear.

The dashboard quickstart identifies payment-status webhooks as the notification path for payment-gated commits; the dedicated webhook guide remains the authority for delivery and verification mechanics.

The architecture guide also says incoming usage can trigger alert and threshold evaluation and webhooks. This is an architectural timing statement, not a delivery guarantee; retry, deduplication, and verification behavior remains governed by the dedicated webhook guide.

For prepaid balance thresholds, `payment_gate.threshold_reached` marks the trigger, `payment_gate.payment_status` reports `paid` or `failed`, and `payment_gate.payment_pending_action_required` signals that intervention is needed. External payment gates additionally use `payment_gate.external_initiate`; the integrator must retain its `workflow_id` to release or cancel the pending commit.

Product architecture may require timely notifications for balance alerts, tier changes, and payment events, but the planning guide supplies no latency or delivery guarantee. The manual payment-gated commit flow emits `payment_gate.payment_status` with `paid` or `failed` and can emit `payment_gate.payment_pending_action_required`; webhook-delivery retries are not payment retries.

The trial example delivers `alerts.low_remaining_contract_credit_and_commit_balance_reached` with fields including `credit_type_id`, `remaining_balance`, and `triggered_by`. The merchant consumes it as an action signal. Alert scope and trigger semantics live in [[metronome-alerts-and-notifications]], while this page's dedicated webhook source remains authoritative for signature verification, delivery retries, ordering, and deduplication.

Offset-notification payloads omit the `properties` field used by threshold payloads, so receivers must parse notification types without assuming one universal shape. Their `timestamp` is the source event time, not the offset fire or delivery time. The UI workflow says a configured offset produces events for all customers to every configured webhook.

## Go-live webhook and retry checks

Metronome's go-live checklist places three checks in its webhook-and-error-handling section: keep the endpoint online and verify signatures with the Metronome webhook secret, make processing safe on duplicate deliveries, and exercise a policy worded as retry on `5xx` or network failure, backoff on `429`, and dead-letter plus alert on `4xx`. The source does not identify that status policy's direction or owner, so it must not be labeled either a webhook-receiver contract or Metronome's outbound-delivery contract. The dedicated webhook guide remains authoritative: Metronome retries outbound delivery responses above `299`. Webhook-delivery retry, API-call retry, and payment retry remain distinct, and these checks do not guarantee timely delivery, revenue preservation, processing success, event ordering, or payment recovery. [[source-metronome-guides-implement-metronome-production-checklist]]

## Sources

- [[source-metronome-guides-platform-configuration-setup-webhooks]] — event families, delivery semantics, deduplication, and signature verification
- [[source-metronome-guides-get-started-metronome-dashboard-quickstart]] — payment-status notification use for payment-gated commits
- [[source-metronome-guides-customers-billing-optimize-customer-experience-prepaid-balance-thresholds]] — threshold, payment-status, action-required, and external-initiation events
- [[source-metronome-guides-get-started-how-metronome-works]] — event-time alert evaluation boundary
- [[source-metronome-guides-implement-metronome-planning-your-billing-architecture]] — notification needs as an architecture consideration
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-manual-payment-gated-commits]] — manual payment-status and action-required notifications
- [[source-metronome-guides-pricing-packaging-billing-model-guides-create-a-trial]] — trial balance-alert delivery example
- [[source-metronome-guides-customers-billing-set-up-notifications-create-and-manage-notifications]] — asynchronous HTTPS delivery, jittered retries, at-least-once semantics, and idempotent receiver guidance
- [[source-metronome-guides-customers-billing-set-up-notifications-offset-notifications]] — offset-specific payload shape, source-event timestamp semantics, and all-configured-webhooks UI behavior

## Related

- [[metronome-customers-and-contracts]]
- [[metronome-invoicing]]
- [[metronome-usage-based-billing]]
- [[metronome-alerts-and-notifications]]
