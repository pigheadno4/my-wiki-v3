---
title: "Configure sales day closing time for Adyen for Platforms | Adyen Docs"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/settle-funds/configure-closing-time"
raw_files:
  - "adyen/docs/platforms/settle-funds/configure-closing-time/2026-09-15.md"
tags: [adyen, platforms, sales-day, settlement, balance-accounts]
---

## Overview

This Adyen for Platforms guide describes configuring the sales-day closing time on a new or existing balance account. The default is midnight in the balance account's local time zone; a later hourly cutoff can keep after-midnight business activity in the prior sales day. The page also identifies a separate business-day settlement-delay setting and payment-method exceptions. This 2026-09-15 webpage snapshot explains configuration and its webhook signal, not a completed settlement batch, available balance, payout, or beneficiary-bank receipt. [[adyen]] [[adyen-platforms]]

## Key takeaways

- The page calls for a Configuration API credential with **Balance Platform BCL role** and subscription to Configuration webhooks. Configure `platformPaymentConfiguration` through POST `/balanceAccounts` for a new account or PATCH `/balanceAccounts/{id}` for an existing one. A successful API response includes the supplied configuration; after application, Adyen describes `balancePlatform.balanceAccount.created` or `.updated` webhook by account case. These are settings evidence, not proof that a transaction was captured or funds became available.
- `salesDayClosingTime` uses `HH:MM`, with hours `00` through `07` and minutes `00`; default `00:00`. The introductory example places a restaurant's 03:00 closing in the balance account's local time zone and says its next sales day starts 03:01. The source does not define daylight-saving transitions or establish a cutoff for a particular account without its returned configuration and time zone.
- `settlementDelayDays` is a separate conditional field: include it when different from the merchant account default; the table says allowed values are integers 1–20 business days or `null` for default. Moving the sales-day cutoff is not itself a promise of a specific availability date, payout initiation, or bank arrival.
- The guide states that funds for **Affirm** and **maestro_USA** settle on the payment method's schedule instead of the configured sales-day closing time. Check the actual method/variant before applying a general cutoff rule.
- The sample prose says a 01:00 closing with funds available after two business days, but the displayed PATCH body sets only `salesDayClosingTime`; it does not include `settlementDelayDays`. Its later webhook example displays 06:00 while the request/response example displays 01:00. Treat those as illustrative fragments, not proof that the sample request set a two-day delay or that the webhook followed that exact request. The SDK snippets and endpoints are test-environment, version-labeled examples.

## Detail locators

- Default local-time-zone sales day and after-midnight example: pinned raw lines 15–19.
- BCL role, Configuration webhooks, 07:00 limit and Affirm/maestro_USA exceptions: pinned raw lines 21–31.
- POST/PATCH account routes, `platformPaymentConfiguration`, exact closing-time format/default and conditional business-day delay: pinned raw lines 33–47.
- Test PATCH and versioned SDK examples, including omitted delay despite the two-day prose: pinned raw lines 48–284.
- API response configuration and created/updated webhook descriptions; 01:00 versus 06:00 examples: pinned raw lines 286–340.

## Related

- [[adyen-platforms]] — main platform/balance-account concept route.
- [[adyen-reporting]] — report timing and reconciliation context; this setting is not a reporting outcome.
- [[source-adyen-docs-reporting-dynamic-sales-day]] — separate merchant-report sales-day guide with its own scope and timing rules.

## Raw Sources

- [[raw/adyen/docs/platforms/settle-funds/configure-closing-time/2026-09-15|Configure sales day closing time — 2026-09-15 snapshot]]
