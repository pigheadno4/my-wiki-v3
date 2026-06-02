---
title: "Stripe: Migrating to New ACH Direct Debit APIs"
type: source
date_ingested: 2026-05-02
original_format: webpage
raw_files:
  - "stripe-ach-migration-2025.md"
tags: [stripe, ach, us-bank-account, migration, legacy, payment-intents, mandates, webhooks]
---

## Summary

Migration guide from legacy ACH (Charges API / Tokens API) to Payment Intents or Checkout Sessions API. Key differences in settlement speed, balance type, mandates, microdeposits, and webhooks.

## Key Migration Points

**Legacy vs new settlement**: T+6 → T+4 (T+2 with faster settlement).

**Balance type change**: `source_type=bank_account` → `source_type=card`. Must update payout/transfer logic.

**Balance transaction timing**: legacy = on charge creation; new = on submission to banking partner (`charge.updated` event, not API response).

**Mandates**: enforced in new API; must create mandates for existing `BankAccount` objects before reuse.

**Microdeposits**: legacy = 2 random amounts; new = 1¢ descriptor code + hosted page + 10-day window + auto emails.

**Identify legacy**: `payment_method_details.type = 'ach_debit'` (legacy) vs `'us_bank_account'` (new).

**Webhook mapping**:
- `charge.pending` → `payment_intent.processing`
- `charge.succeeded` → `payment_intent.succeeded` (but `charge.succeeded` still sent)
- `charge.failed` → `payment_intent.payment_failed` (but `charge.failed` still sent)
- New: `mandate.updated` (mandate becomes inactive)

## Raw Sources

- [[stripe-ach-migration-2025]] — verbatim webpage content (feature comparison, behavioral differences, webhook mapping, legacy identification)
