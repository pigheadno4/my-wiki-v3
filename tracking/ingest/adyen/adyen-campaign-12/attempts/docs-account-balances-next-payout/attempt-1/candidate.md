---
title: "Adyen Next payout balance"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/account/balances/next-payout"
raw_files:
  - "adyen/docs/account/balances/next-payout/2026-09-15.md"
tags: [adyen, merchant-account, balances, next-payout, settlement]
---

## Overview

This Adyen guide defines a merchant account's **Next payout** balance as the **current** amount intended for settlement to its bank account at the next payout moment. It changes as sales, refunds and other adjustments are processed and can become negative. The page was last modified in 2023 and captured 2026-09-15. A displayed balance is not a completed payout or bank-receipt record. See [[adyen]] and [[adyen-account-structure]].

## Key takeaways

- **Moving position, not a final payout:** Next payout is a current amount for the next payout moment, not a fixed positive promise. The guide gives no universal payout frequency, cutoff, currency, specific payout date or bank-arrival time. Retrieve those from the relevant account configuration and payout/report sources.
- **Why it can be negative:** If merchant-account expenses exceed processed payments, Next payout may turn negative. The listed expenses are chargebacks, refunds and payouts, invoice deductions, and transaction fees including refund fees. The balance can change with later activity; a negative value is a position, not proof that any particular expense was finally settled.
- **Consequences and conditional funding:** A negative balance **may** prevent refunds, payouts or receipt of a deposit. If Reserve auto-funding is configured, the page says the amount needed to balance the negative Next payout will be debited from the payout bank account. This is conditional guidance, not evidence that auto-funding is configured or that a bank debit succeeded.
- **Other routes:** Without Reserve auto-funding, the page links options to transfer balance from another merchant account with positive Next payout or top up the Adyen account. Those links are separate procedures with their own eligibility, scope and completion evidence; this page does not prove a transfer or top-up took place.

## Detail locators

- Lines 15–19: Next payout identity, intended bank settlement and changing balance.
- `## Negative next payout`, lines 21–33: expense categories and possible restrictions.
- Lines 35–40: conditional Reserve auto-funding bank debit and linked alternative balance-transfer/top-up routes.
- `## See also`, lines 42–45: Monthly finance report and account-structure navigation.

## Related

- [[adyen-account-structure]] — account/balance concept and reciprocal source route.
- [[adyen-sales-day-payout]] — separate merchant payout-model and frequency context.
- [[source-adyen-docs-account-balances]] — broader pending/next-payout/reserve/deposit balance definitions.
- [[source-adyen-docs-account-getting-paid]] — separate payout cadence and bank-holiday qualifications.

## Raw Sources

- [[raw/adyen/docs/account/balances/next-payout/2026-09-15|Next payout, captured 2026-09-15]]
