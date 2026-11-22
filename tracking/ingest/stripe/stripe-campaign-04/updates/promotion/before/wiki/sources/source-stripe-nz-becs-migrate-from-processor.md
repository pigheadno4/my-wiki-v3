---
title: "Stripe: Migrate NZ BECS Bank Accounts from Another Processor"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-nz-becs-migrate-from-processor-2025.md"
tags: [stripe, nz-becs, becs, new-zealand, nzd, migration, setup-intents, mandates]
---

## Summary

Guide for migrating NZ bank accounts from another payment processor to Stripe. Requires retaining copies of Direct Debit Authorities (DDAs), sending customers pre-migration and first-debit notifications, and creating confirmed SetupIntents with offline mandate acceptance.

## Key Details

**Notification requirements before migration**:
- Pre-migration notice to customers: Stripe New Zealand Limited (auth code `3143978`), migration date, your contact details
- Tell customers no action required unless they wish to cancel

**Post-migration notifications**:
1. Stripe automatically sends mandate confirmation emails after importing bank account details
2. Stripe sends pre-debit notification on each payment post-migration
3. Merchant must also send a separate first-debit notification in addition to Stripe's automatic one

**Migration process** (per customer/bank account):
1. Create or retrieve Customer/Account object
2. Create + confirm SetupIntent with:
   - Raw bank details: `bank_code`, `branch_code`, `account_number`, `suffix`
   - `billing_details.email` + `billing_details.name` (required for Stripe auto-emails)
   - `mandate_data.customer_acceptance.type: 'offline'` + original DDA `accepted_at` timestamp
3. Store resulting PaymentMethod ID for future payments

## Raw Sources

- [[stripe-nz-becs-migrate-from-processor-2025]] — verbatim webpage content
