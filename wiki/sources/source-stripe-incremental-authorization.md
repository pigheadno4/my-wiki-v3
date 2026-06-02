---
title: "Stripe — Incremental Authorization (Online)"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-incremental-authorization-2026.md"
tags: [stripe, incremental-authorization, capture, payment-intents, checkout, ic-plus, sca, visa, mastercard, discover]
---

## Summary

IC+ feature allowing you to increase the authorized amount on a confirmed PaymentIntent before capture. Each increment appears as a separate pending card statement entry; all collapse into one final entry after capture. Covered across three integration paths (Stripe-hosted, Embedded Checkout, Elements).

## Statement Behavior

- Before capture: each increment appears as a **separate pending entry** (e.g., 10 USD + 5 USD increment = two pending entries)
- After capture: all pending entries removed, one final captured amount appears

## Availability

| Network | Country | Payment Type | Categories |
| --- | --- | --- | --- |
| Visa | Global | All | All |
| Mastercard | Global (excl. MX; excl. JPY for JP) | All | All |
| AmEx | Global | All | All (some issuers don't support — check status field) |
| Discover | Global | All card types | T&E: car rental, hotels, commuter, ferries, railways, bus/tour, cruise, boat rental, grocery, EV charging, restaurants, bars, motels, resorts, trailer parks, equipment rental, auto/truck/RV rental, parking, amusement parks, circuses, recreation |
| Discover | Global | Card not present only | Taxicabs and limousines |
| Diners Club (beta) | US/CA/UK | Card present | Same T&E as Discover |
| Diners Club (beta) | Global | Card not present | Same T&E as Discover + taxicabs |
| UnionPay (beta) | Global | Card not present | Same T&E as Discover + taxicabs |
| JCB (beta) | Global | Card not present | Same T&E as Discover + taxicabs |

## SCA Countries

When requesting incremental auth in SCA countries: Stripe auto-configures PM for future off-session usage; initial auth requires 3DS; subsequent increments treated as MIT (potentially SCA-exempt). **No liability shift for MIT transactions.** Must disclose to customer that payment is saved for off-session use.

## API

**Enable**: `payment_method_options.card.request_incremental_authorization: 'if_available'`

**Check**: `charge.payment_method_details.card.incremental_authorization.status` → `available` or `unavailable`

**Increment**: `POST /payment_intents/:id/increment_authorization` with `amount` as new total (not delta)

**Limits**:
- Max **10 increments** per PaymentIntent
- Per increment cap: greater of +$500 or +500% over previously authorized amount

**On failure**: `card_declined` error; PI remains capturable at previous amount; any field updates (metadata, etc.) not saved

## Key Constraint

Incremental authorization does **NOT extend the authorization validity window** — must still capture before the initial authorization expires.

## Related Pages

- [[stripe-incremental-authorization]] — concept page
- [[stripe-terminal-incremental-authorizations]] — in-person Terminal variant
- [[stripe-extended-authorization]] — extends the auth window (different feature)

## Raw Sources

- [[stripe-incremental-authorization-2026]] — verbatim guide, all 3 UI variants (771 lines)
