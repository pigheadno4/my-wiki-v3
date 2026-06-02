---
title: "Pay with Stripe Balance"
type: concept
category: technology
tags: [stripe, connect, stripe-balance, subscriptions, billing, accounts-v2]
---

## Definition

Pay with Stripe Balance lets Connect platforms collect subscription payments directly from connected accounts' available Stripe balances instead of using external payment methods like cards.

**Restrictions**: subscriptions only (not other goods/services); Accounts V2 preview only; cannot use Dynamic Payment Methods — must explicitly specify.

**Eligibility**: active connected account, controlled by platform, `card_payments` capability active.

## Settlement

- **Domestic** (same country): instant (T+0)
- **Cross-border** (different country): T+1

## Coverage

- **34+ countries** for connected accounts; **12 currencies** (USD, CAD, GBP, EUR, CHF, NOK, CZK, DKK, HUF, PLN, RON, SEK)
- Cross-border: Stripe auto-converts to platform's default currency
- Currency per country: most EUR countries support EUR only; some (CA, CZ, DK, HU, PL, RO, SE, NO) support local + EUR; CA supports CAD + USD; UK supports GBP + EUR

## Failure Handling

**Failure cause**: `insufficient_funds` if available balance in specified currency is insufficient (other-currency funds don't help).

**Automatic retries** (2 attempts):
1. First retry: ≥24h after failure
2. Second retry: next Sunday after first retry

**Avoidance strategies**:
- Tailor payout schedules to billing cycles (avoid payouts just before billing)
- Set minimum balance via Balance Settings API or Dashboard

**Manual retry flow**: set payout to manual → wait for incoming funds → check balance → retry if sufficient → restore payout schedule.

## Required Consent

Must obtain connected account approval before debiting. Recommended language: authorize platform to debit Stripe account balance for recurring subscription charges.

## Reporting

**Platform**: Charge + BalanceTransaction (`type: payment`, `reporting_category: charge`).

**Connected account**: BalanceTransaction only (negative, `type: stripe_balance_payment_debit` or `stripe_balance_payment_debit_reversal` for refunds).

## Sources

- [[source-stripe-balance-pay]] — primary source: eligibility, settlement, currencies, failure handling, reporting
