---
title: "Stripe — Instant Payouts for Dashboard Users"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-payouts-instant-2026.md"
  - "stripe-payouts-instant-banks-2026.md"
  - "stripe-payouts-instant-advance-funding-2026.md"
tags: [stripe, payouts, instant-payouts, liquidity, debit-card, api, daily-limit]
---

## Summary

Instant Payouts give Stripe Dashboard users access to their balance within 30 minutes, any time including weekends. Available in 37 countries; 1–1.5% fee depending on country.

## Key Details

- **Speed**: Within 30 minutes, any day/time
- **Countries**: 37 (AE, AT, AU, BE, CA, EU countries, GB, HK, MY, NO, NZ, SG, US + more)
- **Fee**: 1% (CA, EU, UK, SG, NO, HK, MY); 1.5% (US, AU, NZ, AE)
- **Not compatible with**: multi-currency settlement
- **Daily limits**: max 10 payouts/day; max amount (check Dashboard); daily reset by region
- **New users**: not immediately eligible

## Funds Eligibility (`instant_available` balance)

- Card funds: available immediately after charge completion
- ACH/SEPA: only after full settlement (reversible before then)
- Only currencies Stripe supports for Instant Payouts in your country
- Only funds becoming available within ~6 business days
- Fee pre-deducted from balance shown
- Capped at remaining daily allowance
- Withholds pending recovery debits and Stripe Capital repayments

## API

```js
// Check balance
const balance = await stripe.balance.retrieve();
// balance.instant_available[0].amount

// Create instant payout
stripe.payouts.create({ amount: 50, currency: 'usd', method: 'instant', destination: '{{CARD_ID}}' })
```

## Payout Methods by Country

- **US, GB, EU, SE, DK, AU, SG**: debit card or eligible bank account
- **CA, CZ, HU, NO, PL, RO, NZ, MY, AE**: debit card only
- **HK**: eligible bank accounts only

## Pricing Table (min/max per currency)

US: $0.50–$9,999; CA: C$0.60–C$9,999; GB: £0.40–£9,999; EU: €0.40–€9,999; AU: A$0.50–A$9,999; SG: S$0.50–S$9,999; HK: HK$5–HK$9,999; NZ: NZ$0.50–NZ$9,999; MY: MYR2–MYR9,999; AE: AED2–AED9,999; + CZ, DK, HU, NO, PL, RO, SE.

## Related Pages

- [[stripe-payouts]] — concept page (updated with Instant Payouts)
- [[source-stripe-payouts-next-day]] — next-day settlement vs Instant Payouts comparison

## Raw Sources

- [[stripe-payouts-instant-2026]] — verbatim Instant Payouts guide (223 lines)
- [[stripe-payouts-instant-banks-2026]] — US institution support lookup (8,721 lines; thousands of banks/credit unions)
- [[stripe-payouts-instant-advance-funding-2026]] — Advance funding mechanics: advance/advance_funding/payout balance transactions, negative balance recovery, multi-day alignment
