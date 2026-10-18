---
title: "Adyen Platforms balance-account settlement delay"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/custom-payouts/configure-settlement-delay"
raw_files:
  - "adyen/docs/platforms/custom-payouts/configure-settlement-delay/2026-09-15.md"
tags: [adyen, platforms, custom-payouts, settlement-delay, balance-accounts]
---

## Overview

This Adyen for Platforms Configuration API guide (last modified and captured 2026-09-15) explains overriding the merchant-account default settlement delay for a particular user's balance account when it is created or updated. The delay specifies the business days after a settlement batch before those funds become available in that balance account. It is an availability setting, not an instruction to initiate a bank payout or proof of bank receipt. See [[adyen]], [[adyen-platforms]] and [[source-adyen-docs-platforms-custom-payouts]].

## Key takeaways

- **Gates and incompatibility:** The Configuration API credential needs Balance Platform BCL role, and the platform must contact its Account Manager to enable custom sales-day settlement delay. A one-day settlement delay requires previous Adyen approval. The page says a custom settlement delay cannot be used on a balance account with a managed payout schedule. It directs subscribing to balance-account created/updated Configuration webhooks.
- **Create or update:** Include platformPaymentConfiguration in POST /balanceAccounts for a new account or PATCH /balanceAccounts/{id} for an existing one. The page documents settlementDelayDays as integers 1–20 or null (default), counted in business days from the settlement batch until availability. Its three-day PATCH payload is an example, not a universal default. A successful response echoes the configuration; the balanceAccount.created or .updated webhook follows after the delay is applied.
- **Sales-day closing time warning:** The optional salesDayClosingTime is conditionally required if that account previously had a specific closing time: include it on every account update, or it resets to 00:00. The page documents HH:MM with hours 00–07 and minutes 00. This condition matters when patching settlementDelayDays even if the example payload omits the closing-time field.
- **Evidence boundary:** The example response and webhook show a balance-account configuration in TEST. They do not prove a settlement batch has completed, available funds have increased, a scheduled/on-demand payout was requested, or a beneficiary bank received money.

## Detail locators

- Merchant default and balance-account override: pinned raw lines 15-19.
- API role, webhooks, approval, managed-schedule incompatibility and Account Manager setup: pinned raw lines 21-31.
- POST/PATCH targets and field constraints, including closing-time reset: pinned raw lines 33-46.
- Three-day PATCH example, response and TEST balance values: pinned raw lines 48-292.
- Applied-configuration webhook route and test event: pinned raw lines 294-322; payout guide navigation: lines 324-327.

## Related

- [[adyen-platforms]] — main Platforms concept and reciprocal source route.
- [[source-adyen-docs-platforms-custom-payouts]] — parent custom-payout overview.

## Raw Sources

- [[raw/adyen/docs/platforms/custom-payouts/configure-settlement-delay/2026-09-15|Adyen Configure settlement delay, captured 2026-09-15]]
