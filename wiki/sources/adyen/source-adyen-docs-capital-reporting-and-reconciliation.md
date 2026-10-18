---
title: "Capital reporting and reconciliation | Adyen"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/reporting-and-reconciliation"
raw_files:
  - "adyen/docs/capital/reporting-and-reconciliation/2026-09-15.md"
tags: [adyen, capital, platforms, repayments, reconciliation, reports, webhooks]
---

## Overview

This [[adyen]] Capital guide describes how a Capital-enabled Adyen for Platforms integration can reconcile booked disbursements and repayments using balance-platform Transfer/Transaction webhooks or Balance Platform Accounting and Payout Reports. It explains the repayment's sales-date alignment, report identifiers and principal/fee split. See [[adyen-capital]]; [[adyen-reporting]] covers the wider report evidence boundary.

## Key takeaways

- A Capital-supporting Platforms integration is required. To configure Accounting Report columns, the guide lists Merchant admin, Merchant report, Merchant financial or Merchant POS Report roles; report generation/download require the respective Generate and Download Balance Platform reports roles. Webhook reconciliation requires subscribing to both Transfer and Transaction webhooks. These are guide prerequisites, not proof a particular account has Capital capability or report access. [Raw: lines 26–40]
- For a user with an active grant, Adyen reserves a fixed percentage of net captured volume and books repayment approximately one hour after sales-day close, before payout, aligned to the sales date. It processes repayments daily as funds settle, independent of payout cadence. A payout scheduled at or near close may precede the repayment, leaving it out of that payout report; the guide advises at least an hour's gap. Over-reservation can be released at booking, while pre-close chargebacks and refunds may adjust reserved funds; a post-booking chargeback does not adjust that repayment, and a refund may arrive too late for the day's booking. A settlement-delay change during the sales day can yield two repayment bookings. [Raw: lines 38–62]
- A scheduled repayment has one outgoing `repayment` transfer. An unscheduled repayment has an incoming `capitalFundsCollection` transfer followed by an outgoing `repayment` transfer, both on the user's balance account; reconcile both lines. The page says each new disbursement has dedicated bank-account details for unscheduled repayment, which must not be reused from an earlier disbursement. [Raw: lines 64–68]
- In Transfer webhooks, identify a repayment by `category=grants`, `type=repayment`, outgoing direction, and grant-ID `reference`; `received` and `authorized` precede `booked`. Match `transfer.id` in a `balancePlatform.transaction.created` webhook to confirm balance-account booking; for the outgoing repayment, the transfer reference matches the related grant ID. The guide recommends triggering completed-repayment reconciliation from the transaction webhook, not a timer. [Raw: lines 70–93]
- In the Balance Platform Accounting Report, use `Category=grants`, the relevant `Type` and `Booking Date`; verify sales-date alignment through `Value Date`. Match `Transfer Id`, `Transaction Id` and `Reference` to webhooks or other reports. Add `Capital Principal Amount` and `Capital Fee Amount` columns to see the proportional principal/fee split for each repayment. The Payout Report groups repayment transfer lines with related sales and payouts by payout date; its `grants/repayment` rows use Transfer Id and Reference. Webhook amounts use minor units, report amounts payment currency, and outgoing repayment amounts appear negative in reports. [Raw: lines 95–143, 177–187]
- Report and webhook rows are individual repayment bookings. The page directs readers to `GET /grants/{grantId}` or a Capital grant webhook for outstanding principal, fee, total and status; its documented fully repaid condition is total zero **and** status `Repaid`. The worked USD 77.20 example and a `bankTransfer` payout row do not establish any actual user's debt, completed financing, or beneficiary bank receipt. [Raw: lines 144–175]

## Detail locators

- Integration, roles, webhook subscriptions and payout-timing limitation: raw lines 26–40.
- Repayment timing, reservation adjustments, settlement-delay split and scheduled/unscheduled transfers: raw lines 42–68.
- Transfer/Transaction webhook identity, statuses and booking confirmation: raw lines 70–93.
- Accounting and Payout Report grains, principal/fee columns and joins: raw lines 95–143.
- Illustrated dates/signs, outstanding-grant check and cross-report identifiers/units: raw lines 144–187.

## Related

- [[adyen-capital]] — Capital product and grant lifecycle context
- [[adyen-reporting]] — provider reporting evidence boundary
- [[adyen-platforms]] — balance-platform context
- [Repayment](https://docs.adyen.com/capital/repayment) — related Capital lifecycle guide
- [Get grant details](https://docs.adyen.com/capital/get-grant-balances) — linked outstanding-balance guide
- [Capital webhook types](https://docs.adyen.com/capital/webhook-types) — linked webhook structures

## Raw Sources

- [[raw/adyen/docs/capital/reporting-and-reconciliation/2026-09-15|Adyen Capital reporting and reconciliation — collected 2026-09-15]]
