---
title: "Launch a hybrid business model"
type: source
date_ingested: 2026-09-07
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/billing-model-guides/hybrid-business-models"
raw_files:
  - "metronome/guides/pricing-packaging/billing-model-guides/hybrid-business-models-2026-07-13.md"
tags: [metronome, hybrid-pricing, subscriptions, usage-based-billing, credits]
---

## Overview

This guide is a retrieval entry point for launching a Metronome hybrid model that combines a seat subscription with pooled, usage-based AI credits. Its worked SeatsCo example connects catalog setup, a subscription-linked recurring credit, configuration-driven seat changes, balance notifications, paid top-ups, and customer-facing balance controls.

## Key takeaways

- Products and their subscription or usage prices are assembled on a rate card, including a conversion between a custom credit unit and fiat.
- A recurring credit can be linked to a subscription so seat quantity changes provision pooled credits according to configured proration behavior.
- Low-balance and spend alerts emit webhook signals that the merchant can use to restrict access or notify users; the guide does not describe those alerts as automatic access enforcement.
- Purchased top-up credits can be payment-gated so they release only after payment, and their priority can be set so monthly included credits are consumed first.
- In the SeatsCo example—not as a platform-wide default—the included monthly credits are use-it-or-lose-it at month end, while purchased top-ups expire one year after purchase.

## Essential boundary

The page is an end-to-end worked guide, not a complete API schema. Use its linked dedicated API references and the exact raw examples before implementing request fields, units, requiredness, lifecycle behavior, or provider-specific payment gating.

## Raw detail routes

- `Use case` contains the example's seat pricing, pooled included-credit terms, month-end expiry and reset, top-up price, and year-long top-up expiry.
- `Metronome building blocks` contains the subscription product, billable metric and usage product, rate-card conversion, and rate examples.
- `Implement a hybrid model for a customer` contains contract creation, subscription quantity changes, pooled-credit proration, and balance alerts.
- `Enable purchase of top-up credits` contains the purchase priority, optional payment gate, and one-year access-schedule example.
- `Optimize your customer's experience` contains the aggregate balance route and group-key-based per-user spend alert example.

## Related

- Companies: [[metronome]], [[stripe]]
- Concepts: [[metronome-usage-based-billing]], [[metronome-subscriptions]], [[metronome-credits-and-commits]], [[metronome-alerts-and-notifications]], [[metronome-integrations]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/billing-model-guides/hybrid-business-models-2026-07-13|2026-07-13 snapshot — hybrid subscription, pooled credits, seat changes, alerts, top-ups, and billing experience]]
