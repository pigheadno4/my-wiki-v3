---
title: "Stripe — Orchestration: Manage Rules"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-orchestration-rules-2026.md"
tags: [stripe, orchestration, rules, routing, multi-processor, private-preview]
---

## Summary

Dashboard guide for creating and managing Orchestration routing rules. Covers the 7 available rule conditions, execution order semantics, and rule lifecycle (save/test/activate/duplicate/deactivate).

## Rule Conditions

| Condition | Notes |
| --- | --- |
| Amount | Must also specify currency |
| BIN | First 6 or 8 digits of card |
| Card country | Card issuing country |
| Card issuer | Issuing financial institution |
| Card type | credit card / debit card / prepaid card |
| Currency | Presentment currency |
| Metadata | PaymentIntent metadata fields |

## Execution Model

- Conditions evaluated **left to right**; first match wins
- Each rule has: main processor + (optional) retry processor
- Default action applied if no condition matches
- No active rules → all payments route to Stripe

## Rule Lifecycle

- **Draft**: saved but not live; can edit freely
- **Activate**: goes live; one active set at a time — activating new rules auto-deactivates current
- **Cannot edit active rules** — must duplicate, edit draft, then re-activate
- **Deactivate**: via overflow menu; payments return to routing to Stripe

## Related Pages

- [[stripe-orchestration]] — concept page (updated with rule conditions)
- [[source-stripe-orchestration-route-payments]] — API integration guide

## Raw Sources

- [[stripe-orchestration-rules-2026]] — verbatim rules management guide (58 lines)
