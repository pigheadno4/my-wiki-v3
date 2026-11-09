---
title: "Stripe: Record Usage for Billing with the API"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-api"
raw_files:
  - "stripe-billing-subscriptions-usage-based-recording-usage-api-2026-11-07.md"
  - "stripe-usage-based-billing-recording-usage-api-2025.md"
tags: [stripe, billing, usage-based, meters, ingestion, api, rate-limits, webhooks]
---

## Overview

Stripe's May 5 and November 7, 2026 captures of this API guide explain recording usage for [[stripe]] Billing Meters. Configure a meter first, then send meter events with its configured event name, customer ID and numeric value; timestamp is optional. Events may be sent as they occur or in batches. Processing is asynchronous, so meter summaries and upcoming invoices may lag. See [[stripe-usage-based-billing]].

## Key takeaways

- Create a v1 Meter Event using the API. Both captures advise idempotency keys to avoid duplicate reporting; an event identifier can be supplied and is generated if omitted. The May capture illustrates Node.js; the November capture illustrates curl. These are dated examples, not SDK requirements.
- Event timestamps must be within the past 35 calendar days and no more than 5 minutes in the future. The 35-day bound governs acceptance, **not invoice inclusion**. Report usage for a subscription service period before its invoice finalizes: an event accepted after finalization may appear in summaries without updating that invoice or being added to the next. Threshold invoices include only usage received before invoice creation. The linked grace-period guide contains applicable rules and exceptions.
- The payload's numeric usage value accepts decimals, including on invoices. If overall cycle usage is negative, the invoice line item usage quantity is reported as 0.
- The November capture states dimension cardinality limits for configured dimension payload key-value combinations: 10,000 per meter in each event-receipt hour and 100 per customer on a meter across events. Previously counted combinations continue to process; newly introduced combinations beyond either limit are invalid and surface in `v1.billing.meter.error_report_triggered` with `meter_event_dimension_count_too_high`. These are separate from request-rate limits.
- For the v1 Meter Event endpoint in live mode, the November capture states 1,000 calls/second **per Stripe account**, separately from the account global rate limit, with one concurrent call per customer per meter. Sandbox Meter Events count toward the global rate limit; connected-account Meter Event calls count toward the basic limit. Connect platform requests using the `Stripe-Account` header have the regular 100 operations/second limit. The May capture additionally said sandbox meter event **stream** calls counted toward the basic limit; the November text does not restate that stream sentence, so this capture pair does not establish a changed stream rule. Stripe suggests pre-aggregation or v2 streams for higher volumes and monitoring `429` responses with exponential backoff.
- API v2 Meter Event Streams are described for live mode only, up to 10,000 events/second, with a contact-sales path for up to 200,000/second. Create a Meter Event Session, use its 15-minute stateless authentication token to send stream events, and refresh the session on token expiry. Stream requests are excluded from the Workbench Logs tab. The May example is Node.js and the November example is Ruby. The captures do not establish account-specific access or successful ingestion.
- Invalid asynchronously processed events can produce the thin events `v1.billing.meter.error_report_triggered` and `v1.billing.meter.no_meter_found`. Configure a Thin event destination, retrieve full event details, correct invalid events and resend. The May webhook example is Node.js; the November example is Python.

## Detail locators

- Idempotency and event creation: November raw, "Create meter events" and "Idempotency"; May raw, same sections. Neither same-URL capture establishes that omission of an optional timestamp defaults to now or that the event identifier itself is used for cancellation.
- Invoice cutoffs and accepted-event distinction: November raw, "Event timestamps". For broader finalization exceptions, see [[source-stripe-usage-based-billing-configure-grace-period]].
- Dimension limits and over-limit error: November raw, "Dimension cardinality limits".
- Mode, account and concurrency limits: November raw, "Rate limits"; compare May raw, "Rate limits" for the dated sandbox stream sentence.
- API v2 streams and example languages: both raws, "High-throughput ingestion with higher rate limits (API v2)".
- Thin event types, sample payloads, possible `reason.error_types.code` values and handler steps: both raws, "Handle meter event errors". The nine listed codes include customer, dimension, archived meter, timestamp, value and missing-meter errors; `no_meter` is listed only for `v1.billing.meter.no_meter_found`.

## Related

- [[stripe]] — provider context
- [[stripe-usage-based-billing]] — usage-based billing concept and reciprocal source route
- [[source-stripe-usage-based-billing-configure-grace-period]] — invoice finalization rules and exceptions

## Raw Sources

- [[raw/stripe-billing-subscriptions-usage-based-recording-usage-api-2026-11-07|Stripe API recording-usage guide, fetched 2026-11-07]]
- [[raw/stripe-usage-based-billing-recording-usage-api-2025|Stripe API recording-usage guide, fetched 2026-05-05]]
