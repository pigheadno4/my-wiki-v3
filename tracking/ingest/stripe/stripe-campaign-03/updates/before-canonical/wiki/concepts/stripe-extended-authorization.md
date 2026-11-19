---
title: "Stripe Extended Authorization (Online)"
type: concept
category: technology
tags: [stripe, extended-authorization, capture, payment-intents, ic-plus, visa, mastercard]
---

## Overview

Extended authorizations increase the card authorization validity window from the default **7 days** (online) to up to **30 days**, allowing you to hold customer funds longer before capturing. Used for travel, hospitality, and rental bookings where the final amount isn't known at authorization time. **IC+ pricing required.**

For in-person extended authorizations, see [[stripe-terminal-extended-authorizations]].

## Validity Windows by Network

| Network | Category | Window |
| --- | --- | --- |
| Visa | Hotel, lodging, vehicle rental, cruise | 30 days (effective 29d 18h) |
| Visa | All other (CIT only, excl. Japan, healthcare, bill/debt) | 30 days + **+0.08% fee** |
| Mastercard (excl. Maestro/Cirrus) | All categories | 30 days |
| AmEx | Lodging and vehicle rental only | 30 days (must capture by end of stay/rental) |
| Discover | Airline, bus, car rental, cruise, commuter, ferry, hotel, lodging, railway | 30 days |
| Diners Club (beta, US) | All categories | 30 days |
| UnionPay (beta) | Global excl. US/CA (all); US/CA via Discover (T&E) | 27–29 days / 30 days |

**Always use `capture_before` field for the actual deadline** — don't rely on rule tables as networks can change rules without notice.

## Key Constraints

- **AmEx**: must capture by end of customer's stay or rental, not just within 30 days
- **Visa non-T&E**: +0.08% fee; customer-initiated only; excludes Japan, healthcare, bill/debt repayment merchants
- **Visa exact window**: 29 days 18 hours (reduced from 31 days in Sept 2023 to avoid non-compliance fees)
- **Discover Sept 2023**: removed eating/drinking, taxicabs, boat/RV/truck rental, timeshares, trailer parks, equipment rental, amusement parks

## API

```js
// Enable at confirm
payment_method_options: { card: { request_extended_authorization: 'if_available' } }

// Check on charge after confirmation
charge.payment_method_details.card.extended_authorization.status  // 'enabled' | 'disabled'
charge.payment_method_details.card.capture_before                 // Unix timestamp deadline
```

## Related IC+ Features

- [[stripe-multicapture]] — multiple partial captures up to authorized amount
- [[stripe-overcapture]] — capture above authorized amount
- [[stripe-terminal-extended-authorizations]] — in-person variant (different availability rules)

## Sources

- [[source-stripe-extended-authorization]] — full guide with network tables, 2023 changes, test cards, 3 integration paths
