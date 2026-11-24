---
title: "Stripe Payouts"
type: concept
category: technology
tags: [stripe, payouts, bank-account, payout-schedule, settlement, currencies, instant-payouts]
---

## Overview

Stripe payouts transfer your available balance to your bank account. Initial payout takes 7–14 days after first payment; subsequent payouts follow your chosen schedule.

## Payout Schedule

| Schedule | Behavior |
| --- | --- |
| Manual | You initiate; choose amount and timing |
| Daily | Automatic every business day (default for most) |
| Weekly / Monthly | Specific days; missing dates → last day of month |

Non-business days → next business day. All times UTC (APAC: local timezone).

**Country restrictions**: Brazil and India always automatic daily. Japan: no daily (default manual).

**Key distinction**: schedule controls when funds are *sent*, not when they *become available*.

## Settlement and Currencies

- Add one bank account per settlement currency
- Payments in configured currencies settle without conversion
- Payments in unconfigured currencies auto-convert to default
- Default currency selectable and changeable at any time

**Multi-currency settlement** (no FX fees): available in AE, AU, CH, EU, GB, HK, LI, NO, SG, US. Setup: Dashboard → Payout Settings → Manage Currencies → attach one bank account per currency (currency must match). Cannot pay out until minimum balance met per currency. See [[source-stripe-payouts-multicurrency]].

## Supported Bank Account Types

- Traditional checking/savings
- Virtual banks (N26, Revolut, Wise) — higher payout failure rate
- Debit cards (instant payouts, if eligible)
- US Treasury financial accounts

## Country Coverage (80+ countries)

Major native (non-cross-border) markets: US, UK, EU, Australia, Canada, India, Japan, Singapore, Hong Kong, Mexico, Brazil, New Zealand, Thailand.

Most other countries require cross-border payout accounts. Bank account format varies by country (IBAN for EU, SWIFT+account for many others, local formats for US/UK/AU/CA/IN/JP/SG/HK/MX/BR).

## Instant Payouts

Available in 37 countries. Within 30 minutes, any time including weekends. Fee: **1%** (CA/EU/UK/SG/NO/HK/MY) or **1.5%** (US/AU/NZ/AE). Not compatible with multi-currency settlement. Daily limits: max 10/day, daily maximum amount, region-specific reset time. `instant_available` balance: fee pre-deducted, capped by daily limit, card funds immediate (ACH/SEPA only after settlement). Payout methods: debit card (most countries) or eligible bank account (US/GB/EU/SG/AU/HK). API: `method: 'instant'`.

**Advance funding** (when payout exceeds available balance): Stripe pulls from pending balances, creating `advance_funding` transactions (one per day of pending funds pulled) and one `advance` transaction (credits available balance). Failed/canceled instant payouts reverse all transactions. Negative available balance: advance funding skips dates where cumulative balance is still negative. Filter via `stripe.balanceTransactions.list({ source: 'po_xxx' })`. See [[source-stripe-payouts-instant]].

## Next-Day Settlement

**US only** (not new users immediately). Domestic transactions except ACH direct debits settle next business day. Fee: **0.6% monthly** (prior month's accelerated charges, auto-debited). Limit: >$1M adds 1 extra day. Toggle on/off in payout settings. vs Instant Payouts: next-day is automatic/continuous (0.6%), Instant is manual/on-demand (within 30 min, higher fee). See [[source-stripe-payouts-next-day]].

## Minimum Balance

Retains a fixed amount in Stripe account after each automatic payout to cover refunds/disputes/fees. Not supported in Brazil, India, Thailand. Recommended: 4–5× average daily volume. Reconciliation report shows minimum as a `-X USD` transaction. Platforms: configure per connected account via `Balance Settings API` (`minimum_balance_by_currency`, merge semantics). Notify connected accounts before setting. See [[source-stripe-payouts-minimum-balance]].

## Customized Start of Day

**APAC only** (AU, HK, ID, IN, JP, MY, NZ, PH, SG, TH). Groups payout contents by local-timezone day instead of UTC day — aids reconciliation. Default: UTC midnight. Express/Custom accounts cannot change (platform sets). Not immediate (takes effect at the new time). Not retroactive (pre-change transactions stay on UTC day). Setup: Dashboard → Settings → Business → Bank accounts and currencies → Start of day. See [[source-stripe-payouts-start-of-day]].

## Statement Descriptors

Two levels: **Account-level** (all auto+manual payouts; Dashboard → Payout settings) and **Payout-level** (single manual payout; API `statement_descriptor` field or Dashboard balance overview). Precedence: payout-level → account-level → default `'STRIPE'`. Banks don't guarantee display. See [[source-stripe-payouts-statement-descriptors]].

## Trace IDs

Unique banking partner identifier for tracking missing/delayed payouts. Provide to bank if payout missing after 10 business days. Statuses: `pending` (not yet received), `supported` (`payout.trace_id.value`), `unsupported`. Available up to 10 days post-paid. Unsupported: Argentina, Bolivia, Chile, Colombia, Egypt, Japan, Philippines, UK Instant Payouts. See [[source-stripe-payouts-trace-ids]].

## Reconciliation

**Automatic payouts**: reconcilable via Dashboard, payout reconciliation report, or API. **Manual payouts**: Stripe cannot identify included transactions — merchant responsible.

**API flow**: get payout ID (`po_xxx`) → `stripe.balanceTransactions.list({ payout: 'po_xxx' })` → optional `expand: ['data.source']` to inline Charge/Refund objects. Listen for `payout.reconciliation_completed` webhook. BalanceTransaction `type` values: `charge`, `refund`, `stripe_fee`, `payout`. See [[source-stripe-payouts-reconciliation]].

## Sources

- [[source-stripe-payouts]] — payout timing, schedule options, multi-currency, 80+ country bank account tables
- [[source-stripe-payouts-reconciliation]] — reconciliation: API flow, BalanceTransaction types, expand pattern
- [[source-stripe-payouts-trace-ids]] — Trace IDs: 3 statuses, access methods, unsupported countries
- [[source-stripe-payouts-statement-descriptors]] — Statement descriptors: 2 levels, precedence order, bank display caveat
- [[source-stripe-payouts-multicurrency]] — Multi-currency settlement: availability (10 regions), setup, no FX fees, minimum balance
- [[source-stripe-payouts-next-day]] — Next-day settlement: US only, 0.6% fee, ACH excluded, vs Instant Payouts comparison
- [[source-stripe-payouts-instant]] — Instant Payouts: 37 countries, 30 min, 1–1.5% fee, daily limits, instant_available balance rules
- [[source-stripe-payouts-start-of-day]] — Customized start of day: APAC only, groups by local timezone, not retroactive
- [[source-stripe-payouts-minimum-balance]] — Minimum balance: retain fixed amount, 4-5× daily volume recommended, Connect API, Brazil/India/Thailand excluded
