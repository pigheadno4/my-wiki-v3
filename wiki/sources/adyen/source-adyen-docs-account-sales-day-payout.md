---
title: "Adyen Sales day payout"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/account/sales-day-payout"
raw_files:
  - "adyen/docs/account/sales-day-payout/2026-09-15.md"
tags: [adyen, sales-day-payout, merchant-settlement, payout-timing, reconciliation]
---

## Overview

Adyen's Sales day payout groups funds from a sales day into a payable batch after a configured payout delay, rather than tying the merchant payout to each shopper payment method's settlement timeline. It is the default model in the captured page, while Pass-through payout is the only available model in Africa, Brazil, and Turkey. Use is subject to Adyen's Sales day payout Terms of Service. This merchant settlement model is distinct from the legacy outbound Payout API. [[adyen]] [[adyen-sales-day-payout]]

## Key takeaways

- A sales day is midnight to midnight in the merchant account's local time zone by default. A different fixed closing time can be configured, as late as 6:00 AM, and the page points to a separate dynamic-closing route for some cases.
- The payout delay is the interval after a sale until its funds are assigned to a payable batch. Payout frequency affects grouping: daily is the default, while a monthly frequency can place several sales days into one batch. The page separately says a payable batch closes two hours after its sales-day closing time; it does not resolve the exact close for a non-daily schedule. The page's weekday schedule is an example for a daily frequency and two-business-day delay, not a universal payout promise.
- Delay depends on the merchant account's payment-method settlement mix, accepted currencies, and acquiring country or region. The page describes typical two- or three-business-day delays under stated conditions, partner-connected delays of three, seven, or twelve business days by industry, and potentially longer delays for slower methods. Bank holidays can extend a currency's delay when they fall on or between sales and payout days.
- Refunds, chargebacks, and other adjustments enter the payable batch when they occur, regardless of the original transaction's sales day. If Adyen cannot capture funds for a sale it already paid out, it subtracts them from a current payable batch. Consult Next Payout for the current payable balance rather than treating a sales-day total as the final transfer amount.
- The payable batch closes two hours after the sales-day closing time. After it closes, Adyen creates a bank payout instruction and starts a Settlement details report if automatic report generation is configured. Batch assignment, closure, instruction creation, and report generation are separate from bank receipt.
- For eligible merchant locations, a request to decrease the delay is reviewed by Adyen. The page gives unsupported currency/acquiring mix, unsupported payment-method mix, request error, and other reasons for refusal; some unsupported-method funds use Pass-through settlement when Adyen receives them. This snapshot does not establish a particular merchant's accelerated eligibility or bank-arrival date.

## Detail locators

- Opening and `## How it works`, lines 19–43: model, default and regional exception, payable-batch assignment, payout frequency, and illustrative schedule.
- `### Adjustments to your payout`, lines 45–51: timing of refunds, chargebacks, capture shortfalls, and Next Payout balance.
- `## Payout delay` and `### Payout delay calculation`, lines 53–88: assignment meaning, weekday example, bank-holiday caveat, currency/acquiring and partner qualifications.
- `## Decreasing your payout delay`, lines 90–114: eligible merchant locations, approval process, refusal reasons, and Pass-through outcome.
- `## Defining your sales day`, lines 116–122: local-time-zone default, fixed cutoff through 6:00 AM, and dynamic route.
- `## Payable batch closing and report generation` and `## Bank holidays`, lines 124–143: two-hour close, payout instruction, conditional automatic report generation, and holiday examples.

## Related

- [[adyen-sales-day-payout]] — provider concept for this merchant settlement model.
- [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level-settlement-details-report]] — report generated after batch close when configured automatically.

## Raw Sources

- [[raw/adyen/docs/account/sales-day-payout/2026-09-15|Adyen Sales day payout, fetched 2026-09-15]]
