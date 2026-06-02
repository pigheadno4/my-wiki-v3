---
title: "Stripe — Receive Payouts"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-payouts-2026.md"
tags: [stripe, payouts, bank-account, payout-schedule, settlement, currencies, instant-payouts]
---

## Summary

Comprehensive payout reference: initial payout timing, bank account requirements for 80+ countries, payout schedule options, multi-currency settlement, and supported account types.

## Initial Payout Timing

- First payout: 7–14 days after first successful payment
- May be longer based on industry risk and country

## Payout Schedule Options

| Schedule | Description |
| --- | --- |
| Manual | You control when and how much |
| Daily | Automatic every business day |
| Weekly | Specific day(s) of week |
| Monthly | Specific day(s) of month; missing dates → last day of month |

Non-business days (weekends/holidays) → next business day. All times UTC (except APAC markets).

**Country restrictions**: Brazil and India are always automatic daily; Japan has no daily option (default: manual).

**Note**: Schedule determines when payouts are *sent*, not when funds *become available*.

## Settlement and Currencies

- One bank account per settlement currency
- Payments in unconfigured currencies auto-convert to default currency
- Payments in configured currencies settle without conversion
- Default settlement currency selectable and changeable at any time

## Supported Account Types

- Traditional (checking, savings)
- Virtual bank accounts (N26, Revolut, Wise) — higher failure rate
- Debit cards (instant payouts, if eligible)
- US: Treasury financial accounts

## Bank Account Requirements (Key Countries)

| Country | Key fields |
| --- | --- |
| US | Routing number (9 digits) + account number |
| UK | Sort code (12-34-56) + account number |
| EU (most) | IBAN |
| Australia | BSB (6 digits) + account number |
| Canada | Transit number + institution number + account number |
| India | IFSC code (11 chars) + account number |
| Japan | Bank name + branch name + bank/branch codes + account number + owner name (katakana) |
| Mexico | CLABE (18 digits) |
| Brazil | Bank code + branch code + account number |
| Singapore | Bank code + branch code + account number |
| Hong Kong | Clearing code + branch code + account number |

Many countries are cross-border payouts only. Full list (80+ countries) in raw file.

## Related Pages

- [[stripe-payouts]] — concept page
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-payouts-2026]] — verbatim payouts reference (1634 lines, 80+ country bank account tables)
