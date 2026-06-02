---
title: "Stripe Terminal: Extended Authorizations"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-extended-authorizations-2025.md"
tags: [stripe, stripe-terminal, extended-authorization, payment-intents, card-present]
---

## Summary

Guide for extending the capture window on a confirmed Terminal PaymentIntent beyond the standard 48-hour window (or 5 days for Visa). Covers eligibility by card brand and MCC, setup, and how to determine the validity window.

## Key Takeaways

- **Use case**: extend the time between authorization and capture — e.g., hotel checks in a guest (authorizes) and captures when they check out
- **Default capture window**: 48 hours for most cards; 5 days for Visa
- **Not supported on**: Interac and eftpos (single-message payment methods)
- **Setup**: set `request_extended_authorization: true` + `capture_method: manual` at PaymentIntent creation
- **`capture_before`** field (on the Charge, only available after PaymentIntent is confirmed): gives the exact expiry timestamp — always use this rather than relying on card brand rules, which can change
- If not captured by `capture_before`: PaymentIntent transitions to `canceled` automatically

## Validity Window by Card Brand and MCC

| Card brand | Eligible merchant categories | Window |
| --- | --- | --- |
| Visa | Hotel, lodging, vehicle rental, cruise line | 30 days (actual: 29d 18h) |
| Visa | Aircraft/bicycle/boat/clothing/DVD/equipment/furniture/motor home/motorcycle rental, trailer parks & campgrounds | 10 days (actual: 9d 18h) |
| Mastercard (excl. Maestro/Cirrus) | All | 30 days |
| American Express | Lodging and vehicle rental | 30 days* |
| Discover | Airline, bus charter/tour, car rental, cruise line, local/suburban commuter, passenger transportation (incl. ferries), hotel, lodging, passenger railway | 30 days |

\* Amex caveat: even within the 30-day window, you must capture by the end of the customer's stay or rental period.

## See Also

- [[stripe-terminal-extended-authorizations]] — concept page
- [[stripe-terminal-incremental-authorizations]] — related: increasing the authorized amount (vs extending the capture window)

## Raw Sources

- [[stripe-terminal-extended-authorizations-2025]] — verbatim webpage content
