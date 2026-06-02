---
title: "Stripe — Payout Trace IDs"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-payouts-trace-ids-2026.md"
tags: [stripe, payouts, trace-id, missing-payout, bank, sigma, connect]
---

## Summary

Trace IDs are banking partner identifiers for tracking missing or delayed payouts. Provide to your bank if payout is missing after 10 business days.

## Key Details

- **Format**: varies by bank (no standard)
- **Availability**: retrieved from banking partner up to 10 days after payout marked as paid

## 3 Statuses

| Status | Meaning |
| --- | --- |
| `pending` | Not yet received; `value` = null |
| `supported` | Available in `trace_id.value` |
| `unsupported` | Country unsupported or retrieval failed |

## Access Methods

- **Dashboard**: Payout → Details section
- **API**: `payout.trace_id.value` + `.status` via `stripe.payouts.retrieve('po_xxx')`
- **Sigma**: `transfers` table — `trace_id_status`, `trace_id` columns
- **Payout Reconciliation Report**

## Unsupported Countries

Argentina, Bolivia, Chile, Colombia, Egypt, Japan, Philippines, UK (Instant Payouts only).

## Connect

Platforms can retrieve trace IDs for connected accounts via API — connected accounts can self-service.

## Related Pages

- [[stripe-payouts]] — concept page (updated with trace ID note)
- [[source-stripe-payouts-reconciliation]] — payout reconciliation

## Raw Sources

- [[stripe-payouts-trace-ids-2026]] — verbatim payout trace IDs guide
