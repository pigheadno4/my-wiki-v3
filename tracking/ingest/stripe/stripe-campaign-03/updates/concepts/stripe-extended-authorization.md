---
title: "Stripe Extended Authorization (Online)"
type: concept
category: technology
tags: [stripe, extended-authorization, capture, payment-intents, ic-plus, visa, mastercard]
---

## Overview

In the May 11, 2026 full guide, extended authorizations can increase an online card authorization window from the usual **7 days** to up to **30 days**, subject to network and category rules, while the funds remain uncaptured. The guide describes hosted and embedded payment-mode Checkout Sessions with **manual capture**, or an advanced PaymentIntent with `capture_method: 'manual'`; it offers the feature to IC+ users and directs blended-pricing users to support. The November 7 index only links variant bodies and does not renew current eligibility or setup rules. The May Checkout snippets omit manual capture despite the guide's prerequisite prose, so do not treat those snippets alone as a complete working hold.

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

- [[source-stripe-extended-authorization]] — May 11, 2026 full guide for hosted Checkout, embedded Checkout, and advanced PaymentIntent online extended holds, network tables and September 2023 changes; the November 7 capture is a three-variant navigation index only.
- [[source-stripe-flexible-features-migration]] — 2026-05-11 full beta-to-GA migration guide for the pre-confirmation request and capture_before; the guide's status prose and JSON example conflict, and November capture is variant navigation only
