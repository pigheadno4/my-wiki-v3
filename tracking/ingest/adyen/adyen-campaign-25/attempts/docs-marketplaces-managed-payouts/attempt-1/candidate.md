---
title: "Adyen Marketplaces managed payouts"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/managed-payouts"
raw_files:
  - "adyen/docs/marketplaces/managed-payouts/2026-09-15.md"
tags: [adyen, marketplaces, platforms, managed-payouts, balance-accounts]
---

## Overview

This 2022-modified, 2026-09-15-captured Marketplace guide from [[adyen]] describes managed payout schedules for automating payouts from users' balance accounts in [[adyen-platforms]]. A platform arranges a schedule with its Adyen contact and applies it to balance accounts sharing a location and currency. It is configuration guidance, not evidence that a payment settled, a payout executed or a beneficiary bank received funds. Keep this Balance Platform route distinct from legacy Classic Platforms and the separate legacy Payout API.

## Key takeaways

- An Adyen contact helps create and configure schedules using desired user receipt time, sales-day closing time and user time zone. One balance account can use only one managed schedule per currency, and each schedule supports one location and currency. Managed schedules support only local payouts within the same country and currency; a different payout currency or bank-account country calls for custom payouts. See raw lines 19–37.
- Managed payout schedules do **not** change settlement timing for pass-through payments or sales-day payouts with T+7 or longer delay. Those funds follow their indicated settlement delay and can be paid out once settled. A faster schedule is not an override of that underlying settlement dependency. See raw lines 33–36.
- The configuration table offers Standard and Accelerated types, described as funds arriving two or one days after settlement, respectively; weekday, weekly or monthly frequencies; minimum/maximum payout amounts and a retained available balance. A weekly/monthly run can include funds only up to one or two days before the selected payout date. **Payout ETA is estimated** and depends on location/currency cutoff times and the platform's contract with Adyen. These are schedule parameters, not bank-credit guarantees. See raw lines 39–49.
- The US example selects a Standard weekday schedule with a 9 AM local ETA, USD 200 minimum and USD 100 retained amount before applying it to user balance accounts. These figures describe one proposed setup, not universal thresholds or proof of execution. Adyen contact can update/add schedules after go-live. Multiple payout locations and supported currencies require separate schedules for each location/currency pair, illustrated by EU/EUR, US/USD and Canada/CAD and USD. See raw lines 51–87.
- The page points to separate **Use managed payouts** and **View payout executions** guides. It does not itself show a payout execution, transfer lifecycle, return, retry or bank receipt. See raw lines 89–102.

## Detail locators

- Product purpose, Adyen contact and schedule inputs: raw lines 15–25.
- One-schedule-per-currency/account, one-location/currency-per-schedule, local-only and settlement-delay constraints: raw lines 27–37.
- Type, frequency, estimated ETA, amount and statement-description options: raw lines 39–49.
- Illustrative US schedule, post-live update and multiple-location/currency examples: raw lines 51–87.
- Child route to use schedules and view executions: raw lines 89–102.

## Related

- [[adyen]] — provider profile.
- [[adyen-platforms]] — modern Marketplace balance-platform payout model.
- [[source-adyen-docs-platforms-managed-payouts]] — distinct Platforms URL with closely related schedule guidance.
- [[adyen-classic-platforms]] — legacy Classic Platforms payout model, not interchangeable.
- [[adyen-payouts]] — separate legacy Payout API concept, not this Balance Platform schedule.

## Raw Sources

- [[raw/adyen/docs/marketplaces/managed-payouts/2026-09-15|Managed payouts — pinned 2026-09-15 raw snapshot]]
