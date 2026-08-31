---
title: "Metronome Webhooks"
type: concept
category: technology
tags: [metronome, webhooks, notifications, integrations]
---

## Definition

### System lifecycle publication status

The system notification event-type listing schema permits an optional `is_enabled` boolean on each lifecycle-event configuration, described as whether webhook publishing for that lifecycle event is enabled. The example omits the field, and this listing reference does not define how enablement is set or changed, whether disabled configurations are returned, or any delivery, retry, ordering, deduplication, or payload behavior.

Metronome webhooks deliver HTTP POST notifications when billing and configuration events occur. Documented event families include usage thresholds, contract and balance-object lifecycle events, invoices, integration failures, marketplace disablement, and payment-gating workflows.

## Delivery model

The threshold-notification create page says threshold notifications trigger webhooks and tells operators to configure endpoints before creation, but it does not define a create-specific payload, emission condition, evaluation-to-delivery latency, destination selection, retry, deduplication, ordering, signature, or failure contract. The create page's narrative and OpenAPI success representations also conflict, so a successful `POST /v1/alerts/create` must not be treated as evidence that evaluation completed or a webhook was emitted or delivered. Dedicated webhook authority remains controlling for at-least-once delivery, retries, duplicate handling, and verification. [[source-metronome-api-reference-alerts-create-a-threshold-notification]] [[source-metronome-guides-platform-configuration-setup-webhooks]]

A receiver must expose a public HTTPS endpoint and return a successful status such as `200 OK`. Responses above `299` trigger exponential-backoff retries that eventually settle at a 15-minute cadence and can continue until two days after the initial attempt. Metronome recommends storing the payload, acknowledging it, and processing it asynchronously.

Retries and multiple configured destinations can produce duplicate deliveries. Consumers should therefore use the notification `id` as a deduplication key.

The notification lifecycle guide confirms asynchronous JSON delivery for all notification types over HTTPS POST. It describes exponential-backoff retries with jitter for up to 48 hours and at-least-once delivery, so receivers must tolerate duplicates and make processing idempotent.

The managed custom-invoice guide uses `invoice.finalized` after the grace period as the trigger for retrieving finalized invoice data and upserting a downstream invoice. The event is not enabled by default and the refreshed page routes enablement through the Metronome support portal. This integration sequence does not replace the dedicated webhook authority for verification, retry, ordering, deduplication, or delivery semantics, and it does not establish downstream upsert idempotency or recovery. [[source-metronome-integrations-invoice-integrations-custom-invoice-integrations]]

For native Stripe invoice delivery, `invoice.billing_provider_error` is the Metronome notification type for an error sending an invoice to Stripe, and the guide assigns the receiver responsibility for triggering internal notifications and actions. The same page separately documents a Stripe-side 72-hour wait when `invoice.created` webhook delivery fails, extending the payment-timing surface beyond the usual up-to-one-hour wait. This assigned guide does not establish that either condition results in successful invoice delivery, eventual Stripe collection, payment finality, or end-to-end reconciliation.

## Authenticity and authoritative data

The customer-alert get endpoint provides the current threshold evaluation state for one customer/notification pair, not a historical sequence. Its documentation routes threshold-notification history to webhook notifications or event logs and positions live API lookup for targeted rather than bulk monitoring. [[source-metronome-api-reference-alerts-get-a-threshold-notification]]

Webhook payloads contain minimal event information. A consumer can treat the notification as a change hint and retrieve authoritative details from the corresponding Metronome API, or verify the webhook directly.

For signature verification, compute HMAC-SHA256 over `X-Metronome-Date`, a newline, and the exact request-body bytes using the secret unique to that webhook. Compare the result with `Metronome-Webhook-Signature`, reject requests older than five minutes, and avoid reserializing parsed JSON before verification.

`@metronome/sdk@3.10.0` implements that contract through `client.webhooks.verifySignature()` and `unwrap()`. The helper also rejects timestamps more than five minutes in the future, uses a timing-resistant signature comparison, and verifies before JSON parsing; it does not implement delivery deduplication or processing idempotency. [[source-github-metronome-node]]

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

- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-guarantee-zero-overages]] - webhook-triggered merchant access gating after commit exhaustion, with no guide-local transport, ordering, or cutoff-timing guarantee
- [[source-metronome-integrations-invoice-integrations-stripe]] — `invoice.billing_provider_error` operator action, Stripe `invoice.created` delivery fallback, and separation of Metronome notification handling from Stripe payment timing

- [[source-metronome-api-reference-credits-and-commits-release-external-payment-gate-threshold-commit]] — `payment_gate.external_initiate` workflow-ID correlation and the downstream outcome-reporting endpoint

- [[source-github-metronome-node]] - exact Node SDK raw-body, timestamp-tolerance, HMAC, and parsing behavior

- [[source-metronome-api-reference-notifications-list-system-notification-event-types]] - optional lifecycle-event webhook-publication status and its documented control boundary

- [[source-metronome-guides-platform-configuration-setup-webhooks]] — event families, delivery semantics, deduplication, and signature verification
- [[source-metronome-guides-get-started-metronome-dashboard-quickstart]] — payment-status notification use for payment-gated commits
- [[source-metronome-guides-customers-billing-optimize-customer-experience-prepaid-balance-thresholds]] — threshold, payment-status, action-required, and external-initiation events
- [[source-metronome-guides-get-started-how-metronome-works]] — event-time alert evaluation boundary
- [[source-metronome-guides-implement-metronome-planning-your-billing-architecture]] — notification needs as an architecture consideration
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-manual-payment-gated-commits]] — manual payment-status and action-required notifications
- [[source-metronome-guides-pricing-packaging-billing-model-guides-create-a-trial]] — trial balance-alert delivery example
- [[source-metronome-guides-customers-billing-set-up-notifications-create-and-manage-notifications]] — asynchronous HTTPS delivery, jittered retries, at-least-once semantics, and idempotent receiver guidance
- [[source-metronome-guides-customers-billing-set-up-notifications-offset-notifications]] — offset-specific payload shape, source-event timestamp semantics, and all-configured-webhooks UI behavior
- [[source-metronome-guides-customers-billing-set-up-notifications-system-notifications]] - system-event publication to all configured webhooks, notification-family payload differences, and lifecycle payload examples

- [[source-metronome-integrations-invoice-integrations-netsuite]] - `invoice.invoice_sync_status` and `payment.payment_status_sync` outcome signals, failure details, and manual invoice-resend context

- [[source-metronome-api-reference-alerts-get-a-threshold-notification]] — current-state API lookup versus webhook or event-log history routing and targeted-monitoring scope

## Related

- [[metronome-customers-and-contracts]]
- [[metronome-invoicing]]
- [[metronome-usage-based-billing]]
- [[metronome-alerts-and-notifications]]
