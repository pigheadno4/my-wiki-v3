---
title: "Stripe — Extended Authorization (Online)"
type: source
date_ingested: 2026-05-11
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/extended-authorization"
raw_files:
  - "stripe-extended-authorization-2026.md"
tags: [stripe, extended-authorization, capture, payment-intents, checkout, ic-plus, sca, visa, mastercard]
---

## Summary

The May 11, 2026 full guide describes an IC+ online card feature that can extend an uncaptured authorization beyond the usual seven-day online window, up to 30 days under qualifying network and merchant-category rules. It covers hosted Checkout, embedded Checkout, and an advanced PaymentIntent/Elements path. The November 7, 2026 capture at the same canonical URL is only a three-variant index and does not verify current eligibility, rules, code, or outcomes. An authorization hold is not capture or available funds.

## Capture boundary and required payment state

The operational details and network table below are dated to May 11, 2026. The guide's hosted and embedded Checkout availability prose requires `mode: 'payment'` and `payment_intent_data.capture_method: 'manual'` on the Checkout Session; the advanced path requires `capture_method: 'manual'` on the PaymentIntent and confirms an uncaptured authorization. Set `payment_method_options.card.request_extended_authorization: 'if_available'` as a request, then inspect the associated Charge. Requesting the feature alone does not prove it was enabled. The guide's example PaymentIntent is `requires_capture`, with `amount_capturable` positive and `amount_received: 0`; this is distinct from capture, payment settlement, or available funds.

> [!warning] Contradiction in the May guide: hosted and embedded Checkout creation snippets set payment mode and `if_available` but omit the manual-capture parameter required by their own availability prose. The embedded return-page prose also calls a `complete` Checkout Session a succeeded payment, while the same guide's uncaptured example remains `requires_capture` with no amount received. Do not use those snippets or a return-page status alone to infer a working extended hold or captured funds; verify the PaymentIntent/Charge and capture state.

## Default vs Extended Windows

- May guide default: seven days for most online card networks; two days for in-person Terminal, which has separate rules.
- May guide extended upper bound: up to 30 days, conditional on network, merchant category, pricing, and payment-specific eligibility; use the Charge deadline rather than the table as a capture schedule.

## Availability by Network (May 11, 2026 capture)

The main availability text lists Visa, Mastercard, American Express, and Discover; a separate limited-support beta table lists Diners Club and UnionPay. These are dated category and network descriptions, not a current availability guarantee for a particular merchant or payment.

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

**September 2023 changes reported in the May 2026 capture**:
- Discover removed: eating/drinking, boat rental, RV/truck, timeshares, taxicabs, trailer parks, equipment rental, amusement parks
- Visa reduced from 31→30 days (effective 29d 18h buffer) to avoid non-compliance fees

## API and state boundaries (May 11, 2026)

**Prerequisite**: IC+ pricing in the guide. Hosted/embedded Checkout uses a payment-mode Session with manual capture; advanced PaymentIntent uses `capture_method: 'manual'`. Blended-pricing users are directed to Stripe support for feature access. Neither pricing nor a request establishes per-payment enablement.

**Request**: `payment_method_options.card.request_extended_authorization: 'if_available'`

**Check actual extension on associated Charge after confirmation**: `charge.payment_method_details.card.extended_authorization.status` → `enabled` or `disabled`

**Capture deadline**: `charge.payment_method_details.card.capture_before` (Unix timestamp) is the payment-specific validity deadline; the May guide says the window does not change after Checkout Session completion or PaymentIntent confirmation. Network rules can change, so use this field rather than calculating a deadline from the table. `requires_capture` means authorized and uncaptured, not paid out.

## Key Constraints (May 11, 2026)

- AmEx: must capture by end of customer's stay or rental (not just within 30 days)
- Visa non-T&E: +0.08% fee per transaction; only for customer-initiated transactions; excludes Japan and healthcare/bill/debt repayment merchants
- Capture no later than the relevant `capture_before` deadline and applicable category constraint. The network table is a dated guide, not the authoritative deadline for one payment.
- The old guide says merchants remain responsible for applicable network rules and law; the table alone cannot establish a compliant use case or a successful capture.

## Best Practices

Use clear statement descriptors to minimize disputes (customers may not recognize held funds after 30 days).

## Related Pages

- [[stripe]] — provider
- [[stripe-extended-authorization]] — concept page
- [[stripe-terminal-extended-authorizations]] — in-person extended authorizations (different availability rules)
- [[stripe-overcapture]] — related IC+ capture feature

## Raw Sources

- [[raw/stripe-extended-authorization-2026|May 11, 2026 full online extended-authorization guide]] — hosted Checkout, embedded Checkout, and advanced PaymentIntent variants, including dated network tables and examples.

## Related raw API references

- [[raw/stripe-payments-extended-authorization-2026-11-07|November 7, 2026 hosted, embedded, and advanced variant index]] — navigation only; the three variant bodies were not captured in this packet.
