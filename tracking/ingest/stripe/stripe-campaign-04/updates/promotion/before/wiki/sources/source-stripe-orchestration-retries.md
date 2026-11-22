---
title: "Stripe — Orchestration: Cross-Processor Retries"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-orchestration-retries-2026.md"
tags: [stripe, orchestration, retries, multi-processor, 3d-secure, adaptive-acceptance, radar, private-preview]
---

## Summary

Details for Orchestration's cross-processor retry feature. Covers setup, and four retry behavior edge cases: 3DS, ineligible features, Radar blocks, and Adaptive Acceptance interaction.

## Setup

In Orchestration rule builder: add an Action with **Main processor** (initial attempt) + **Retry processor** (if initial fails).

## Retry Behavior Edge Cases

| Scenario | Retry behavior |
| --- | --- |
| 3DS attempted on main processor + fails (auth or payment) | **No retry** → `payment_intent.payment_failed` event |
| Retry processor doesn't support a payment feature (e.g., Connect `on_behalf_of`) | No retry |
| Stripe blocks transaction via Radar | Treated as decline → **retried on retry processor** |
| Adaptive Acceptance enabled + Stripe is main processor | Stripe may internally retry before cross-processor retry |
| Stripe is retry processor + Adaptive Acceptance | Potentially 2 retries: 1 cross-processor + 1 Adaptive Acceptance |

## Related Pages

- [[stripe-orchestration]] — concept page (updated with retry edge cases)
- [[source-stripe-orchestration-rules]] — rule setup

## Raw Sources

- [[stripe-orchestration-retries-2026]] — verbatim cross-processor retries guide (40 lines)
