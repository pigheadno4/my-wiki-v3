---
title: "Stripe Payouts"
type: concept
category: technology
tags: [stripe, payouts, bank-account, payout-schedule, settlement, currencies, instant-payouts]
---

## Overview

Stripe payouts transfer your available balance to your bank account. Stripe typically schedules the first payout to complete within 7–14 days after your first successful live payment, depending on industry, country and risk. Subsequent payouts follow your chosen schedule, while settlement timing controls when funds become available and the recipient bank can take additional time. See [[source-stripe-payouts]].

## Payout Schedule

| Schedule | Behavior |
| --- | --- |
| Manual | You initiate; choose amount and timing |
| Daily | Automatic every business day (default for most) |
| Weekly / Monthly | Specific days; missing dates → last day of month |

Non-business days → next business day. All times UTC (APAC: local timezone).

**Country restrictions**: Brazil and India always use automatic daily payouts. Thailand defaults to automatic daily payouts. Japan defaults to manual, allows weekly and monthly, and has no daily option. Connect cross-border rules can differ. See [[source-stripe-payouts]] for the separate dated settlement table.

**Key distinction**: schedule controls when funds are *sent*, not when they *become available*.

## Settlement and Currencies

- Add one bank account per settlement currency
- Payments in configured currencies settle without conversion
- Payments in unconfigured currencies auto-convert to default
- Default currency selectable and changeable at any time

**Multi-currency settlement** (no FX fees): available in AE, AU, CH, EU, GB, HK, LI, NO, SG, US. Setup: Dashboard → Payout Settings → Manage Currencies → attach one bank account per currency (currency must match). Cannot pay out until minimum balance met per currency. See [[source-stripe-payouts-multicurrency]].

## Supported Bank Account Types

- Traditional checking/savings
- The May 2026 guide lists virtual accounts such as N26, Revolut and Wise, with a higher payout-failure caveat. The November guide requires a Japanese futsū or tōza account in the legal entity’s name and excludes services that do not open accounts in that name, such as Wise and Payoneer, for Japan payouts.
- Debit cards (instant payouts, if eligible)
- For eligible US businesses, payment proceeds settle into a Stripe financial account. Bank details are needed for payouts to an external account. The full guide separately describes an optional Stripe financial account destination for approved Stripe Capital financing.

## Country Coverage (80+ countries)

Major native (non-cross-border) markets: US, UK, EU, Australia, Canada, India, Japan, Singapore, Hong Kong, Mexico, Brazil, New Zealand, Thailand.

Most other countries require cross-border payout accounts. Bank account format varies by country (IBAN for EU, SWIFT+account for many others, local formats for US/UK/AU/CA/IN/JP/SG/HK/MX/BR).

## Instant Payouts

The May and November 2026 Dashboard guides list 36 account countries. For eligible accounts, funds typically settle within 30 minutes, including weekends. The May guide quoted **1%** (CA/EU/UK/SG/NO/HK/MY) or **1.5%** (US/AU/NZ/AE). The November guide retains the per-payout fee and pre-deduction without percentages. Multi-currency settlement is unsupported. Daily limits use request time and regional resets, with up to 10 payouts and a separate daily maximum amount. `instant_available` is capped by the remaining daily limit and includes eligible card funds after charge completion and ACH/SEPA after settlement. The destination table allows debit cards or eligible bank accounts in the US, GB, Euro Area, SE, DK, AU and SG, bank accounts only in HK, and debit cards only in the other listed destination row. Use `method: 'instant'` with an eligible `destination` for API requests. See [[source-stripe-payouts-instant#Institution and rail directory|the dated institution directory]] for country, rail and destination details.

**Advance funding** (when payout exceeds available balance): Stripe pulls from pending balances, creating `advance_funding` transactions (one per day of pending funds pulled) and one `advance` transaction (credits available balance). Failed/canceled instant payouts reverse all transactions. Negative available balance: advance funding skips dates where cumulative balance is still negative. Filter via `stripe.balanceTransactions.list({ source: 'po_xxx' })`. See [[source-stripe-payouts-instant]].

## Next-Day Settlement

The November 2026 guide lists 24 Dashboard-user countries and directs platforms to their account team for connected-account access. Eligible domestic funds become available in the Stripe balance the next business day. On a daily automatic schedule Stripe sends eligible funds to the bank then, with receipt subject to bank timing. The guide gives regional exclusions and thresholds. May listed US-only Dashboard access and a 0.6% monthly fee. November retains a monthly assessment on the previous month’s accelerated charges and gives no percentage. Instant Payouts are on demand and charged per payout. See [[source-stripe-payouts-next-day]] and [[source-stripe-payouts-instant]].

## Minimum Balance

The May and November 2026 guides describe paying out only the available funds above an enabled minimum on each automatic payout schedule. The reserve covers anticipated refunds, disputes and fees and is unavailable in Brazil, India and Thailand. Stripe generally recommends four to five times average daily processing volume. The reconciliation report includes a retained-amount transaction in the example currency. Platforms configure individual connected accounts using the Balance Settings API's `minimum_balance_by_currency`. Adding a currency preserves the existing minimum balance settings for other currencies. Stripe recommends explaining the effect on payouts to those customers beforehand. See [[source-stripe-payouts-minimum-balance]].

## Customized Start of Day

Customized start of day groups automatic payout contents by a local-day cutoff for reconciliation. Stripe's November 7, 2026 direct guide lists AU, HK, ID, IN, JP, MY, NZ, PH, SG and TH and offers an email preview request with unspecified eligibility. It describes the default as local midnight with some APAC exceptions. Connected accounts without the full Stripe Dashboard or under platform control inherit the platform cutoff. The linked Connect guide describes platform customization in selected markets and a private preview for US connected accounts. In the direct Dashboard, use **Settings** → **Linked accounts and payouts** → **Settlement and transfer rules** → **Start of day**. Changes take effect at the new cutoff and pre-change transactions retain their original payout settings and timing. The May 11 capture documented a UTC-midnight default with some APAC exceptions, a preceding Dashboard path and a common platform-selected cutoff for Express and Custom accounts. See [[source-stripe-payouts-start-of-day]].

## Statement Descriptors

Set the account descriptor for automatic and manual payouts in Dashboard payout settings. For a single manual payout, the Dashboard balance overview or API `statement_descriptor` can override it. Stripe falls back to `STRIPE` when neither value is set. The November 7, 2026 guide maps standard US ACH payouts to the 10-character ACH Company Entry Description and says Stripe silently truncates longer values before submission. The generic payout API request maximum is 22 characters. The beneficiary bank decides what appears. See [[source-stripe-payouts-statement-descriptors]].

## Trace IDs

Unique banking partner identifier for tracking missing/delayed payouts. Provide to bank if payout missing after 10 business days. Statuses: `pending` (not yet received), `supported` (`payout.trace_id.value`), `unsupported`. Available up to 10 days post-paid. Unsupported: Argentina, Bolivia, Chile, Colombia, Egypt, Japan, Philippines, UK Instant Payouts. See [[source-stripe-payouts-trace-ids]].

## Reconciliation

**Automatic payouts**: reconcilable via Dashboard, payout reconciliation report, or API. **Manual payouts**: Stripe cannot identify included transactions — merchant responsible.

**API flow**: get payout ID (`po_xxx`) → `stripe.balanceTransactions.list({ payout: 'po_xxx' })` → optional `expand: ['data.source']` to inline Charge/Refund objects. Listen for `payout.reconciliation_completed` webhook. BalanceTransaction `type` values: `charge`, `refund`, `stripe_fee`, `payout`. See [[source-stripe-payouts-reconciliation]].

## Sources

- [[source-stripe-payouts]] — payout timing, schedule options, multi-currency, 80+ country bank account tables
- [[source-stripe-payouts-reconciliation]] — reconciliation: API flow, BalanceTransaction types, expand pattern
- [[source-stripe-payouts-trace-ids]] — Trace IDs: 3 statuses, access methods, unsupported countries
- [[source-stripe-payouts-statement-descriptors]] — May and November guides to configuration precedence, standard US ACH truncation, and beneficiary-bank display
- [[source-stripe-payouts-multicurrency]] — Multi-currency settlement: availability (10 regions), setup, no FX fees, minimum balance
- [[source-stripe-payouts-next-day]] — May and November 2026 next-day settlement guides with dated country, balance, bank timing and fee qualifications.
- [[source-stripe-payouts-instant]] — May and November Dashboard guides to 36 listed countries, typical payout arrival, fees and amount limits, eligible balance, and destinations
- [[source-stripe-payouts-start-of-day]] — Automatic payout grouping by local-day cutoff, dated direct and Connect availability, and original transaction settings
- [[source-stripe-payouts-minimum-balance]] — May and November 2026 guides for retaining a reserve on automatic payouts, reconciling it and configuring connected-account currency settings.
