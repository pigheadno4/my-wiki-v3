---
title: "Stripe — Agentic Commerce Suite: Custom Integration (Third-Party Processors)"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-agentic-commerce-custom-integration-2026.md"
tags: [stripe, agentic-commerce, spt, shared-payment-token, third-party-processor, reverse-api, custom-integration]
---

## Summary

Custom ACS integration for merchants using third-party payment processors. Uses a reverse API pattern: Stripe calls your backend when agents route checkout requests. You receive a Shared Payment Token (SPT), resolve it to network credentials, charge via your processor, and record the payment.

## Architecture

Stripe acts as the intermediary between agents and your backend. You implement four reverse API endpoints:

| Hook | Method | Action |
| --- | --- | --- |
| Checkout creation | `POST /agentic/checkouts` | Create checkout; return line items, fulfillment options, totals |
| Checkout updated | `POST /agentic/checkouts/:id` | Agent selects shipping/updates info; recalculate totals; set `ready_for_payment` |
| Checkout confirmed | `POST /agentic/checkouts/:id/confirm` | Receive SPT + risk details; resolve SPT → charge → record payment |
| Checkout retrieve | `GET /agentic/checkouts/:id` | Return current checkout state |

## Checkout Status Enum

`incomplete` | `ready_for_payment` | `requires_escalation` | `processing` | `completed` | `canceled`

## Shared Payment Token (SPT)

Agent provides `token: "spt_xxx"` at confirm. Resolve via:

```bash
POST /v1/shared_payment/granted_tokens/:id/resolve
```

Returns `agentic_token` or `dpan` credential type — both include number, expiry, cryptogram (CAVV/TAVV/DCVV), ECI, encrypted block. Stripe may use Mastercard Agent Pay or Visa Intelligent Commerce tokens on your behalf.

## Payment Recording

After charging via third-party processor:

```bash
POST /v1/payment_records/report_payment
  payment_method_details[shared_payment_granted_token]=spt_xxx
  amount_requested[value]=1000
  outcome=guaranteed
  processor_details[type]=custom
  processor_details[custom][payment_reference]=auth_order_id_1
```

## Totals Breakdown Types

`items_base_amount`, `discount`, `subtotal`, `fulfillment`, `tax`, `total`, `packing_fee`

## Testing

Use Workbench Blueprints to simulate `UpdateSession` and `CompleteSession` reverse API requests in sandbox.

## Related Pages

- [[stripe-agentic-commerce]] — concept page (updated with custom integration + SPT)
- [[source-stripe-agentic-commerce-for-sellers]] — standard ACS integration (Stripe as processor)

## Raw Sources

- [[stripe-agentic-commerce-custom-integration-2026]] — verbatim custom integration guide (640 lines)
