---
title: "Stripe — Extended Authorization (Online)"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-extended-authorization-2026.md"
tags: [stripe, extended-authorization, capture, payment-intents, checkout, ic-plus, sca, visa, mastercard]
---

## Summary

IC+ feature extending card authorization validity from the default 7 days (online) up to 30 days, allowing capture of held funds after extended periods. Used for hotel/lodging, car rental, travel bookings where final amount isn't known at authorization time. Covered across three integration paths.

## Default vs Extended Windows

- Default: 7 days online, 2 days in-person Terminal
- Extended: up to 30 days depending on card network and merchant category

## Availability by Network

| Network | Category | Window |
| --- | --- | --- |
| Visa | Hotel, lodging, vehicle rental, cruise line | 30 days (effective 29d 18h) |
| Visa | All other (CIT only, no Japan/healthcare/bill/debt) | 30 days + **0.08% fee** |
| Mastercard (excl. Maestro/Cirrus) | All categories | 30 days |
| AmEx | Lodging and vehicle rental only | 30 days (must capture by end of stay/rental) |
| Discover | Airline, bus, car rental, cruise, commuter, ferry, hotel, lodging, railway | 30 days |
| Diners Club (beta, US via Discover) | All categories | 30 days |
| UnionPay (beta) | Global excl. US/CA | 27–29 days |
| UnionPay (beta, US/CA via Discover) | T&E categories | 30 days |

**September 2023 changes**:
- Discover removed: eating/drinking, boat rental, RV/truck, timeshares, taxicabs, trailer parks, equipment rental, amusement parks
- Visa reduced from 31→30 days (effective 29d 18h buffer) to avoid non-compliance fees

## API

**Enable**: `payment_method_options.card.request_extended_authorization: 'if_available'`

**Check availability**: `charge.payment_method_details.card.extended_authorization.status` → `enabled` or `disabled`

**Capture deadline**: `charge.payment_method_details.card.capture_before` (Unix timestamp) — use this rather than calculating from network rules, as rules can change

## Key Constraints

- AmEx: must capture by end of customer's stay or rental (not just within 30 days)
- Visa non-T&E: +0.08% fee per transaction; only for customer-initiated transactions; excludes Japan and healthcare/bill/debt repayment merchants
- `capture_before` is the authoritative deadline — do not rely on rule tables

## Best Practices

Use clear statement descriptors to minimize disputes (customers may not recognize held funds after 30 days).

## Related Pages

- [[stripe-extended-authorization]] — concept page
- [[stripe-terminal-extended-authorizations]] — in-person extended authorizations (different availability rules)
- [[stripe-overcapture]] — related IC+ capture feature

## Raw Sources

- [[stripe-extended-authorization-2026]] — verbatim extended authorization guide, all 3 UI variants (605 lines)
