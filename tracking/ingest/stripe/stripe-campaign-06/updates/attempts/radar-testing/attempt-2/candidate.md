---
title: "Stripe — Testing Stripe Radar"
type: source
date_ingested: 2026-05-10
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/radar/testing"
raw_files:
  - "stripe-radar-testing-2026-11-07.md"
  - "stripe-radar-testing-2026.md"
tags: [stripe, radar, testing, sandbox, test-cards, risk-level, backtesting]
---

## Summary

The May and November 2026 [[stripe]] Radar guides cover sandbox test payments and testing proposed rules against historical live-mode payments. November adds test card use with the Payment Evaluation API and sandbox block cases for SEPA Direct Debit and ACH Direct Debit.

## Sandbox Test Payments

Both guides document creating sandbox card payments in the Dashboard or with the create-charge API using a test key. The **Card numbers**, **Tokens**, and **PaymentMethods** tables provide inputs for three cases.

- **Rule-dependent highest risk.** The test produces a `highest` risk charge that can be blocked depending on rules. The guide uses the legacy `Block if :risk_level: = 'highest'` rule as an example. The November [[source-stripe-radar-risk-settings|risk settings guide]] explains when the rule may still be enabled.
- **Always-blocked highest risk.** The test produces a `highest` risk charge that is blocked regardless of rules.
- **Elevated risk.** The test produces an `elevated` risk charge. The fixture description establishes the risk level only.

The November guide also says to use the documented test card numbers with the Payment Evaluation API to force the corresponding `fraudulent_payment` risk level. See [[source-stripe-radar-multiprocessor]] for API access, sandbox test keys and processor outcome boundaries.

For November’s non-card sandbox block cases, see **SEPA Direct Debit** for the test IBAN and **ACH Direct Debit** for the test account and routing numbers. The fixtures simulate Radar blocks in a sandbox.

## Rule Backtesting

Before adding or updating a rule, Stripe searches matching historical live-mode payments. Operators can inspect the matching payments and compare counts and volume for disputes or early fraud warnings, refunds, blocked and failed payments, and succeeded payments. **Blocked and failed** includes payments blocked by Radar or Stripe and payments declined by issuers. **Succeeded** includes successfully processed payments that have yet to be identified as fraudulent or refunded. **Overrides** on an Allow backtest are payments previously blocked by Radar that the proposed rule would allow.

The separate November [[source-stripe-radar-rules|rules guide]] describes a six-month simulation in its Review rules section (lines 270–278 of the November rules capture). The testing guides describe historical live-mode payments without specifying a time window.

## When to Implement Each Rule Type

| Rule type | Considerations |
| --- | --- |
| Block | Weigh the fraud, early warnings, fraudulent refunds or issuer declines matched by the rule against the cost of blocking legitimate payments. |
| Review | Use relevant disputes, early fraud warnings or fraudulent refunds to identify cases that merit closer human inspection. |
| Request 3DS | Balance the fraud signals matched and the cost to legitimate customers. A 3DS request may be frictionless. A fraud-liability shift after frictionless authentication can still coexist with an early fraud warning. |
| Allow | Review previously blocked matches and Overrides. The backtest cannot determine which previously blocked charges would have been fraudulent if allowed. |

## Related Pages

- [[stripe-radar]] — Radar concept and testing scope
- [[source-stripe-radar-rules]] — rule creation and historical simulation guidance
- [[source-stripe-radar-multiprocessor]] — Payment Evaluation API scope and sandbox testing

## Raw Sources

- [[raw/stripe-radar-testing-2026-11-07|Stripe Radar testing guide captured 2026-11-07]]
- [[raw/stripe-radar-testing-2026|Stripe Radar testing guide captured 2026-05-10]] — includes the backtesting screenshot
