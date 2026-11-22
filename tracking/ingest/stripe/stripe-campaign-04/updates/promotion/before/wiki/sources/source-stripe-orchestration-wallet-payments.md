---
title: "Stripe — Orchestration: Wallet Payments"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-orchestration-wallet-payments-2026.md"
tags: [stripe, orchestration, apple-pay, google-pay, wallets, off-session, private-preview]
---

## Summary

Apple Pay and Google Pay can be routed to different processors via Orchestration. Key constraint: saved mobile wallet payment methods require `off_session=true`; customer-present flows must re-prompt via native wallet integrations.

## Key Rules

- **Saved mobile wallet PM**: pass `off_session=true` during PaymentIntent confirmation
- **Customer present**: cannot reuse saved wallet PM — must use Apple Pay/Google Pay integrations to re-prompt
- **Testing**: Payment Links can be used to quickly test Apple Pay / Google Pay routing

## Related Pages

- [[stripe-orchestration]] — concept page (updated with wallet note)
- [[source-stripe-orchestration-feature-support]] — feature matrix (wallets listed as supported)

## Raw Sources

- [[stripe-orchestration-wallet-payments-2026]] — verbatim wallet payments guide (21 lines)
