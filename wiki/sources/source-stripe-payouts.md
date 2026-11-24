---
title: "Stripe — Receive Payouts"
type: source
date_ingested: 2026-05-11
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payouts"
raw_files:
  - "stripe-payouts-2026-11-07.md"
  - "stripe-payouts-2026.md"
tags: [stripe, payouts, bank-account, payout-schedule, settlement, currencies, instant-payouts]
---

## Overview

The May 11 and November 7, 2026 guides describe how Stripe sends your available balance to a bank account. After your first successful live payment, Stripe typically schedules the first payout to complete within 7–14 days, depending on your industry, country and risk level. The Dashboard shows expected deposit dates, and the recipient bank can take additional time to make the funds available. Connect platforms follow the separate connected-account payout route.

## Schedule and settlement timing

Manual payouts let you choose when to send available funds and how much to send. Daily automatic payouts run on business days. Weekly and monthly schedules allow selected days, with missing month dates moved to the last day. Payouts scheduled for weekends or holidays arrive on the next business day. The guides describe processing in UTC except in APAC markets.

Brazil and India always use automatic daily payouts. Thailand defaults to automatic daily payouts. Japan defaults to manual and offers weekly and monthly schedules. Daily payouts are unavailable in Japan. These rules can differ for Connect cross-border payouts.

The schedule controls when funds are sent. Settlement timing controls when the balance becomes available after payment confirmation or capture, the transaction time in Stripe’s T+X notation. The country table gives initial settlement timing for the first payout and a default for later payouts. Account risk criteria can prevent a switch to the published default. The May Japan row instead describes weekly payouts covering payments processed up to four business days earlier. The November Japan row gives seven calendar days initially and four business days by default, separate from the schedule options.

A Connect platform’s `delay_days` follows the connected account country’s business-day or calendar-day rule, with business-day exceptions for Brazil Pix, Boleto, debit and prepaid payouts, and Singapore PayNow. See November lines 1097–1187 for the timing rules and country table. The separate payment-method table adds USD Bank Transfers at five business days and retains standard ACH Debit at four business days. Eligible US merchants can use two-business-day ACH settlement from payment creation. Eligible Instant Payouts have a separate route and usually arrive within 30 minutes.

## Same-day manual payouts

The November table gives eligibility and limits for same-day manual payouts. Each listed route allows up to ten same-day manual payouts per day, with a maximum of one million of the eligible currency per payout.

| Region and currency | Standard settlement timing | Initiation cutoff | Other manual payouts |
| --- | --- | --- | --- |
| US, USD | T+2 or slower | Before 5 pm US/Eastern | Typically within one business day |
| GB, GBP | T+3 or slower | Before 5 pm Europe/London | Typically within two business days |
| CH, EU, GB, MT and NO, EUR | T+3 or slower | Before 4 pm Europe/Copenhagen | Typically within one business day |

For the EUR route, a recipient bank with a high failure rate on same-day banking rails receives funds the next business day. The May guide described US and UK business-hours eligibility at standard T+2 and T+3, respectively, and phrased the US cap as ten manual payouts per day. See May lines 1067–1075 and November lines 1078–1088.

## Bank accounts and currencies

Set bank details in Dashboard payout settings and match the bank currency to the configured currency. Required details vary with bank location. The country table covers more than 80 locations and identifies Connect cross-border-only destinations. UK sort code and account number are examples whose applicability depends on currency and Stripe account country. Other examples include US routing and account numbers, IBAN in many European markets, Australian BSB, Canadian transit and institution numbers, India's IFSC, Mexico's CLABE, bank and branch codes in Brazil and Singapore, and Hong Kong clearing and branch codes. See November lines 21–1010 for the complete country formats and examples, including Japanese bank and branch names and codes, account number and account owner name.

The May guide listed traditional checking and savings accounts, virtual accounts such as N26, Revolut and Wise with potentially higher failure rates, and eligible debit cards for Instant Payouts. The November guide separately requires a Japanese `futsū` or `tōza` account in the legal entity’s name. Services that do not open the account in that name, including Wise and Payoneer in the guide's examples, are unsupported for Japan payouts. For cross-border payouts to Japan the recipient bank must also participate in FXYCS.

Supported markets can configure one bank account per supported settlement currency and select a default currency, which can be changed. Payments presented in configured currencies settle without conversion. Payments in other currencies convert to the default. November says applicable non-primary-currency fees are charged at settlement, with some non-primary currencies exempt. The referenced free-currency table has no rows in either capture. Normal payout initiation carries no Stripe fee. May described fees on most non-primary-currency payouts. See November lines 1020–1036 and 2986–2988.

For eligible US businesses, payment proceeds settle into their Stripe financial account. External bank details are needed for payouts to an external bank. The November guide also lets an approved Stripe Capital applicant select the Stripe financial account for financing proceeds, with access within minutes, or choose the default external bank account. New Stripe users are not immediately eligible for Capital. See November lines 1016–1018 and 1038–1044.

## Minimums, failures and test payouts

An available balance below the applicable payout minimum stays in Stripe until it increases. A persistent negative balance can lead Stripe to debit the bank account, so the account must support credits and debits. The minimum table and debit explanation are at November lines 1217–1290.

A failed payout can initially show as `paid` and change to `failed` within five business days. Bank return and notice to Stripe can take up to five additional business days. Stripe notifies by email and in Dashboard and reattempts at the next scheduled interval after account details are corrected. Incorrect account details can send funds to the wrong account and leave Stripe unable to recover them. See November lines 2976–2984.

Test payouts simulate outcomes without bank processing. Both guides document test-only debit-card fixtures and November adds country-specific bank fixtures for success, named failures and some Instant Payouts ineligibility cases. Use these with test API keys. A live-mode connected account cannot accept fixture numbers in Dashboard. See November lines 1292–2974.

## Related Pages

- [[stripe-payouts]] — payout lifecycle, schedule and related reporting guides
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-payouts-2026-11-07|November 7, 2026 Receive payouts guide]]
- [[raw/stripe-payouts-2026|May 11, 2026 Receive payouts guide]]
