---
title: "Stripe — Customized Start of Day"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-payouts-start-of-day-2026.md"
tags: [stripe, payouts, start-of-day, timezone, apac, reconciliation]
---

## Summary

Customized start of day groups automatic payout contents by local-timezone day instead of UTC day — aids reconciliation. APAC only; not retroactive.

## Key Details

- **Available in**: AU, HK, ID, IN, JP, MY, NZ, PH, SG, TH
- **Default**: UTC midnight (except some APAC markets)
- **Express/Custom accounts**: cannot change directly — platform sets for all connected accounts
- **Allowed range**: usually between midnight and morning in local timezone
- **Not immediate**: takes effect at the new time (e.g. setting midnight from 7am = 17 hours wait)
- **Not retroactive**: transactions before change stay on original UTC day; only new transactions follow new timezone

## Setup

Dashboard → Settings → Business → Bank accounts and currencies → Start of day section.

## Related Pages

- [[stripe-payouts]] — concept page (updated with start of day note)

## Raw Sources

- [[stripe-payouts-start-of-day-2026]] — verbatim customized start of day guide (2 screenshots)
