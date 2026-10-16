---
title: "Adyen Dynamic sales day closing time"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/dynamic-sales-day"
raw_files:
  - "adyen/docs/reporting/dynamic-sales-day/2026-09-15.md"
tags: [adyen, reporting, sales-day, reconciliation, payout-schedule]
---

## Overview

This [[adyen]] guide describes a merchant-account sales-day cutoff that can be closed for a particular night by a Management API request, so a variable close in a business application can align with Adyen's settlement-details report and payable-batch grouping. It affects which sales-day report receives captured payments; it does not demonstrate payout or bank receipt. See [[adyen-reporting]] for the reporting route.

## Key takeaways

- The merchant account normally closes at a static time, defaulting to midnight. A night-audit business application can close at a different time each night; if its close and Adyen's cutoff differ, reconciliation can become difficult. A successful dynamic request closes that night's sales day at the time the request is sent. If no request arrives, or it arrives too late, the static cutoff applies. The next day also defaults to the static cutoff unless another request is sent. [Raw: Solution to reconciliation problems, lines 31–39; Set the closing time for this night, lines 74–111]
- Eligibility in this snapshot requires **Sales day payout T+1 or T+2** and a one-to-one relationship between the merchant account and the business application closing the sales day. The guide says Sales day payout, and thus this feature, is unavailable in Africa, Brazil, and Turkey. It specifically does not solve the case where several applications feed one merchant account but close at different times. [Raw: When dynamic closing times do not help, lines 41–55]
- Preparation requires moving the merchant account's static closing time after midnight; the guide recommends 06:00 as the latest possible time, rather than making that exact setting mandatory. In Customer Area, select Sales day payout T+1 or T+2 and the closing time. The static-setting user needs **Change payout schedule** or **Merchant admin**; the nightly API credential needs **Management API—Sales Day Payout read and write**. [Raw: Requirements, lines 21–29; Preparation, lines 57–72]
- Send `POST /merchants/{merchantId}/closeSalesDay` after midnight but before 06:00 in the account time zone, or before its earlier static closing time. A missing body, `closeNow: true`, and `closeNow: false` have the same documented immediate-close effect. Check the response for `salesDayClosed: true`; the example 422 `36_001` can reflect an already closed night or an out-of-window request. Do not treat the response as a payment settlement or payout confirmation. [Raw: Set the closing time for this night, lines 74–111; Troubleshooting, lines 113–133]
- Payments captured before the close request go in that sales day's Settlement details report; those captured after it go to the next sales day's payable pending batch and report. This is a booking/reporting cutoff based on capture timing, not a claim about when a shopper paid or when funds reach a bank. [Raw: Booking of payments, lines 135–140]
- This is a 2026-09-15 snapshot. It does not establish current regional/account eligibility, successful execution of a particular API call, completed settlement, or financial finality.

## Detail locators

- Account cutoff, hotel/restaurant Night Audit context, and static fallback: `Solution to reconciliation problems`, lines 31–39.
- T+1/T+2 and region limits, one-to-one relationship and multi-application exception: `When dynamic closing times do not help`, lines 41–55.
- Roles, static-cutoff preparation, recommended 06:00, and Customer Area settings: `Requirements`, lines 21–29; `Preparation: set the static closing time`, lines 57–72.
- Request timing, endpoint, optional body, response, and next-day reset: `Set the closing time for this night`, lines 74–111.
- 422 example and possible causes: `Troubleshooting`, lines 113–133.
- Captured-payment assignment across report and payable batch: `Booking of payments`, lines 135–140.

## Related

- [[adyen]] — provider page.
- [[adyen-reporting]] — reporting concept.
- [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level-settlement-details-report]] — the report whose daily grouping this cutoff affects.

## Raw Sources

- [[raw/adyen/docs/reporting/dynamic-sales-day/2026-09-15|Adyen Dynamic sales day closing time (2026-09-15)]]
