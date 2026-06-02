---
title: "Stripe: CIT and MIT"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-cit-mit-2025.md"
tags: [stripe, cards, cit, mit, merchant-initiated, subscriptions, compliance, card-account-updater]
---

## Summary

Explains the CIT/MIT distinction imposed by card networks, MIT compliance requirements, and the card brand change rule that blocks MIT until new cardholder agreement is obtained.

## Key Details

**MIT**: merchant-initiated without customer present; requires prior written agreement covering transaction types, frequency, amount, cancellation policy.

**Card brand change**: Card Account Updater may change card brand → must prompt cardholder to update; cannot charge MIT until new agreement. Detect via `payment_method.automatically_updated` event.

**Authorization window**: differs by CIT vs MIT; use `payment_method_details.card.capture_before` for accurate window.

## Raw Sources

- [[stripe-cit-mit-2025]] — verbatim webpage content
