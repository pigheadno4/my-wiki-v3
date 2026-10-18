---
title: "Pass-through settlement | Adyen for Platforms"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/settle-funds/pass-through-settlement"
raw_files:
  - "adyen/docs/platforms/settle-funds/pass-through-settlement/2026-09-15.md"
tags: [adyen, platforms, settlement, pass-through, reconciliation, deprecated]
---

## Overview

This 2025-last-modified [[adyen]] for Platforms guide, captured 2026-09-15, describes **pass-through settlement** for a balance account. It explicitly says the model is **deprecated and unavailable for new integrations**. Existing pass-through settlement follows the payment schemes' and methods' fund-delivery timing, so one sales day's funds can settle across several business days. Settlement to a balance account is distinct from a later payout to a bank; this page does not show a payout execution or bank receipt. [[adyen-platforms]]

## Key takeaways

- **Timing and reconciliation.** Sales enter a settlement batch when schemes or payment methods send funds to Adyen; after that batch closes, Adyen says it settles them on the **next business day**. Available funds settle daily on working days, Monday–Friday, excluding bank holidays; a capture-day holiday increases delay. A batch may contain sales from multiple sales days, so the page says **day-total reconciliation is unavailable** under this model and directs payment-level reconciliation to accounting reports. Its January 1–7 diagram is illustrative, not an account-specific settlement timetable. [Raw: lines 19–29, 37–39]
- **Adjustments.** Before a batch settles, Adyen adds or subtracts refunds, chargebacks and other adjustments as they occur. Their dates can differ from the original sales day. This affects what is in a settlement batch; the page does not define refund or chargeback initiation/approval, fee allocation, payout timing or bank-credit outcome. [Raw: Adjustments to the settlement, lines 33–35]
- **Deprecation versus documented configuration.** The page also says pass-through settlement is enabled by default on a balance account and shows a **reversion from sales-day settlement** for an existing account through PATCH `/balanceAccounts/{id}` with `platformPaymentConfiguration.settlementDelayDays: null` and `salesDayClosingTime: "00:00"`. Read that alongside the explicit new-integration deprecation warning; neither sentence alone proves present eligibility or a successful configuration change. Its sample response omits `settlementDelayDays`. The field table says an integer `settlementDelayDays` enables sales-day settlement and `salesDayClosingTime` uses `HH:MM` with hours 00–07 and minutes 00. [Raw: lines 41–62, 275–305]
- **Example limits.** The request and SDK snippets use test endpoints and pinned library versions. The Go sample labels library v10.2.0 but imports `/v9/` packages and uses `null` in a Go call; the Ruby snippet also uses `null`. These are not copy-ready proof of a valid live request. Verify the current Configuration API contract before acting on the sample, particularly because the model is deprecated. [Raw: lines 64–273]

## Detail locators

- Raw introduction and `How it works` (lines 15–35): deprecation, scheme/method timing, batch assignment, reconciliation and adjustments.
- Raw `Settlement frequency` (lines 37–39): weekday and bank-holiday qualifiers.
- Raw `Configure pass-through settlement` (lines 41–305): existing-account PATCH, test/library examples, response omission and field meanings.

## Related

- [[adyen-platforms]] — platform and user balance-account context
- [[adyen-reporting]] — provider reporting concept; accounting-report evidence remains in the linked raw guidance

## Raw Sources

- [[raw/adyen/docs/platforms/settle-funds/pass-through-settlement/2026-09-15|Adyen Platforms pass-through settlement — collected 2026-09-15]]
