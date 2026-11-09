---
title: "Stripe: Record Usage for Billing"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage"
raw_files:
  - "stripe-billing-subscriptions-usage-based-recording-usage-2026-11-07.md"
  - "stripe-usage-based-billing-recording-usage-2025.md"
tags: [stripe, billing, usage-based, meters, ingestion]
---

## Overview

Stripe's dated recording-usage hub for basic [[stripe-usage-based-billing|Billing Meters]] explains how existing Billing Meters users record customer usage and routes to the API, Dashboard CSV, and Amazon S3 guides. The 2026-11-07 capture adds Stripe's recommendation to use Metronome for most new usage-based integrations, including when adding usage pricing to an existing flat-rate subscription. This is integration-selection guidance, not a Billing Meters retirement notice or a requirement for existing users to migrate.

## Key takeaways

- **Scope and destination:** This basic Billing Meters path sends events to Stripe's `/v1/billing/meter_events`. The November guide frames it for customers already using Billing Meters. For a new integration it recommends Metronome, whose ingest API is separate from Stripe's meter-event endpoint.
- **Comparison in the November guide:** Stripe describes Metronome as applying pricing to ingested events in real time and tracking running balances and usage continuously, with high-volume ingest positioning. Those descriptions do not establish account-specific availability or measured throughput. Its comparison with end-of-period Stripe aggregation does not mean Stripe meter-event summaries are unavailable during a period.
- **Existing recording flow:** Configure a meter before adding usage. The hub routes to the Stripe API, Dashboard CSV upload, and Amazon S3 bulk ingestion. Stripe processes meter events asynchronously; summaries and upcoming invoices may lag recently received events.
- **Separate legacy route:** Stripe links a different guide for its previous usage-based billing process. The new Metronome recommendation does not reclassify this basic Billing Meters flow as that legacy process.

## Detail locators

- November 2026 selection guidance and comparison: [[raw/stripe-billing-subscriptions-usage-based-recording-usage-2026-11-07|November capture]], lines 9–17.
- Meter prerequisite, asynchronous processing, and three recording routes: same November capture, lines 19–31; [[raw/stripe-usage-based-billing-recording-usage-2025|May capture]], lines 8–20.
- The November capture's pricing-models and compare-options links are navigation to separately scoped documentation; their detailed contracts are not established here.

## Related

- [[stripe]]; [[stripe-usage-based-billing]]
- [[source-stripe-usage-based-billing-recording-usage-api]]; [[source-stripe-usage-based-billing-recording-usage-dashboard]]; [[source-stripe-usage-based-billing-recording-usage-s3]] — recording-route detail pages.

## Raw Sources

- [[raw/stripe-billing-subscriptions-usage-based-recording-usage-2026-11-07|November 7, 2026 recording-usage capture]]
- [[raw/stripe-usage-based-billing-recording-usage-2025|May 5, 2026 recording-usage capture]]
