---
title: "Stripe — Instant Payouts for Dashboard Users"
type: source
date_ingested: 2026-05-11
date_updated: 2026-11-22
original_format: webpage
raw_files:
  - "stripe-payouts-instant-2026.md"
  - "stripe-payouts-instant-banks-2026.md"
  - "stripe-payouts-instant-advance-funding-2026.md"
tags: [stripe, payouts, instant-payouts, liquidity, debit-card, api, daily-limit]
---

## Summary

The May 11 and [November 7, 2026 Dashboard user guides](https://docs.stripe.com/payouts/instant-payouts) from [[stripe]] list the same 36 account countries. Eligible Dashboard users can request an Instant Payout at any time, including weekends and holidays, with funds typically settling at the payout destination within 30 minutes. Funds left in the balance follow the standard payout schedule.

## Key Details

- **Account and balance**: Check individual eligibility in the Dashboard. New users are ineligible immediately after joining. Requests require a positive eligible balance and a configured, eligible payout destination.
- **Request paths**: Use **Pay out** in the Balances Dashboard, the mobile Dashboard app if eligible for both, or the Payouts API.
- **Daily limits**: Up to 10 Instant Payouts per day and a separate account-specific daily maximum amount shown in the Dashboard. Each payout counts toward the day it was requested, even if it arrives on a subsequent day. Reset times depend on the account region.
- **Currencies**: Instant Payouts cannot use multi-currency settlement.
- **Fee**: The November guide says Stripe charges a fee per payout and pre-deducts it from the eligible balance shown. It omits the May 11, 2026 rates of 1% for CA, EU, UK, SG, NO, HK and MY, and 1.5% for US, AU, NZ and AE.

## Funds Eligibility (`instant_available` balance)

The Balances API reports eligible funds before any payout is requested. A completed card charge can count immediately, including funds pending in the payout schedule window, while ACH and SEPA debits count only after full settlement. The balance covers supported payment methods and local Instant Payout currencies. It includes only funds that become available within roughly six business days, based on the payout schedule.

Stripe caps the amount at the remaining daily allowance and pre-deducts the fee. Stripe withholds pending recovery debits and Stripe Capital repayments to prevent negative balances. A positive `instant_available` amount identifies funds eligible to be paid out and does not indicate that a payout has started or arrived.

## API

Read `instant_available` using the Balances API, then request the payout with `method: 'instant'` and the ID of an eligible debit card or bank account as the destination. The May guide shows Node.js and the November guide shows curl with the same request semantics. Both use a debit card in the creation example.

```js
// Check balance
const balance = await stripe.balance.retrieve();
// balance.instant_available[0].amount

// Create instant payout using an eligible debit card or bank account ID
await stripe.payouts.create({
  amount: 50,
  currency: 'usd',
  method: 'instant',
  destination: eligibleDestinationId,
});
```

## Payout Methods by Country

- **US, GB, EU, SE, DK, AU, SG**: debit card or eligible bank account
- **CA, CZ, HU, NO, PL, RO, NZ, MY, AE**: debit card only
- **HK**: eligible bank accounts only

## Institution and rail directory

The [institution-support directory](https://docs.stripe.com/payouts/instant-payouts-banks) captured on May 11 and November 7, 2026 covers multiple countries. Eligible Stripe users select the country and destination type and use the local currency. Check whether the applicable table lists all or some debit cards or accounts. The Canadian table covers Visa or PLUS debit cards. UK bank accounts must use Faster Payments, and the directory links the Pay.UK sort-code checker. Applicable European account sections say banks *should* support receiving SEPA Instant Payments and point to the European Payments Council register.

Both snapshots list some exact US display names under both All and Some within the same destination type. First Bank and First National Bank have conflicting debit-card rows. Bank of America N.A., Citibank Fsb, Wells Fargo Bank and Wells Fargo Bank NA have conflicting account rows. A display-name match alone does not identify the institution or establish eligibility for the specific card or account.

The November 7 United States account table adds Lead Bank as “Some accounts.” In the Germany debit-card table, N26 GMBH changes from “All debit cards” in May to “Some debit cards” in November. Use the two dated directories below for the exact listings.

## Minimum and Maximum Transaction Amounts

US USD 0.50–9,999, CA CAD 0.60–9,999, GB GBP 0.40–9,999, Euro Area EUR 0.40–9,999, AU AUD 0.50–9,999, SG SGD 0.50–9,999, HK HKD 5–9,999, NZ NZD 0.50–9,999, MY MYR 2–9,999 and AE AED 2–9,999. The table also lists CZ CZK 10–99,999, DK DKK 5–9,999, HU HUF 200–999,999, NO NOK 5–9,999, PL PLN 2–9,999, RO RON 2–9,999 and SE SEK 5–9,999. Both captures list the same currency amounts.

## Related Pages

- [[stripe-payouts]] — concept page (updated with Instant Payouts)
- [[source-stripe-payouts-next-day]] — next-day settlement vs Instant Payouts comparison

## Raw Sources

- [[stripe-payouts-instant-2026]] — verbatim Instant Payouts guide (223 lines)
- [[stripe-payouts-instant-banks-2026]] — US institution support lookup (8,721 lines; thousands of banks/credit unions)
- [[stripe-payouts-instant-advance-funding-2026]] — Advance funding mechanics: advance/advance_funding/payout balance transactions, negative balance recovery, multi-day alignment
