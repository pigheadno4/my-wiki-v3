---
title: "Stripe: Migrate ACH Bank Accounts from Another Processor"
type: source
date_ingested: 2026-05-02
original_format: webpage
raw_files:
  - "stripe-ach-migrate-from-processor-2025.md"
tags: [stripe, ach, us-bank-account, migration, processor, setup-intent, verification-skip]
---

## Summary

Guide for migrating verified ACH bank accounts from another payment processor to Stripe. Two options: Stripe-managed migration or self-service manual migration.

## Key Details

**Stripe-managed**: submit intake form; Stripe coordinates with old processor; provides CSV/JSON mapping of old→new IDs.

**Manual migration**: contact Stripe support to enable `verification_method: 'skip'` capability. Then create confirmed SetupIntent with:
- Raw bank details (`routing_number`, `account_number`, `account_holder_type`)
- `mandate_data.customer_acceptance.type: 'offline'` with original authorization timestamp
- `verification_method: 'skip'`

Store resulting PaymentMethod ID for future payments.

## Raw Sources

- [[stripe-ach-migrate-from-processor-2025]] — verbatim webpage content
