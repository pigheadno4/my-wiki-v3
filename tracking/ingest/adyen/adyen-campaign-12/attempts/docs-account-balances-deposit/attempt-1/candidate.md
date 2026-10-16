---
title: "Adyen merchant-account deposit"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/account/balances/deposit"
raw_files:
  - "adyen/docs/account/balances/deposit/2026-09-15.md"
tags: [adyen, account-balances, deposit, exposure, payouts]
---

## Overview

Adyen's deposit guide describes funds Adyen withholds on a merchant account to cover potential processing losses and liabilities, especially chargebacks if other account funds are insufficient. Adyen calculates the deposit requirement; unlike the reserve, the merchant cannot set its own deposit amount. The guide describes accounting and payout adjustments, not evidence that a particular merchant's bank transfer occurred. See [[adyen]] and [[adyen-account-structure]] for provider and merchant-account context.

## Key takeaways

- Adyen recalculates the merchant-account requirement daily before payout using estimated exposure and available coverage. If exposure exceeds coverage by more than EUR10,000, Adyen automatically withholds funds from the next payout. The guide's EUR30,000 exposure/EUR18,000 coverage example raises the required deposit by the full EUR12,000 gap, not merely the EUR2,000 above the trigger. An increase books sales funds to deposit; a decrease releases excess deposit into the next payout amount. These are conditional account-balance rules, not confirmation that a payout or deposit release has arrived.
- Exposure includes unfulfilled paid transactions and forecast chargebacks/refunds. The latter forecast uses historical reversal data from the past 180 days, expected reversal rate and chargebackable volume. Coverage includes pending and payable processing balances plus securities coverage such as a case-reviewed bank guarantee, actual deposit and case-assessed accepted risk. Pending means captured funds approved to be paid to Adyen, while payable means funds received by Adyen and about to be paid to the merchant; neither definition by itself proves the merchant received cash.
- If the required deposit exceeds the actual deposit balance, the guide says funds are deducted from later payouts until the requirement is met. A merchant's held deposit remains merchant-owned. After processing stops, Adyen describes gradual repayment after chargeback costs; it estimates return of any remainder when potential chargeback exposure ends, approximately six months after processing stops. This is a conditional estimate, not a fixed release date.
- The standard model uses a fixed fulfillment-time assumption. The delivery-date/airline-date-of-travel model applies where fulfillment times vary significantly and requires a `deliveryDate` on each transaction in that model. The optimization section offers levers such as fulfillment time, chargeback rate and a bank guarantee; its examples do not promise a particular reduction.
- To view deposit details, the user needs the Merchant financial role and must switch to the merchant account in the live Customer Area, then open Balances > Balances overview > Deposit. The page does not establish a merchant's current eligibility, calculated amount, or live transfer result.

## Detail locators

- Deposit versus reserve, recalculation and increase/decrease handling: raw lines 17–23. Merchant financial role and Customer Area route: `## Check your deposit details`, lines 25–35.
- Chargeback use, merchant ownership and conditional repayment: `## Why you need a deposit`, lines 39–45. Daily threshold, full-gap example and payout withholding: `## How the deposit is calculated`, lines 47–62.
- Fulfillment and 180-day reversal forecast: `## Exposure`, lines 64–80. Pending/payable processing coverage, bank guarantee, actual deposit and accepted risk: `## Coverage`, lines 82–105.
- Fixed versus dynamic fulfillment model and `deliveryDate`: `## Deposit types`, lines 107–121. Suggested optimization paths and illustrative subscription example: `## Optimize your deposit`, lines 123–160.

## Related

- [[adyen]] — provider context.
- [[adyen-account-structure]] — merchant-account scope and related balance-viewing source.

## Related raw API references

- The raw guide links to user roles, next-payout negative payable, Customer Area and various payment-method/risk pages. These are navigation until separately read.

## Raw Sources

- [[raw/adyen/docs/account/balances/deposit/2026-09-15|Adyen Docs: Deposit (2026-09-15 snapshot; page last modified 2021-11-22)]]
