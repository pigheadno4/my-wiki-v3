---
title: "Managed payouts | Adyen for Platforms"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/managed-payouts"
raw_files:
  - "adyen/docs/platforms/managed-payouts/2026-09-15.md"
tags: [adyen, platforms, managed-payouts, balance-accounts, payout-schedules]
---

## Overview

This 2022-last-modified [[adyen]] for Platforms overview, captured 2026-09-15, describes managed payout schedules that automate payouts from users' balance accounts on a balance platform. A platform can arrange a schedule with its Adyen contact and apply it to balance accounts sharing a location and currency. The scheduled destination is a user's transfer instrument or bank account in the local payout route; the page is about payout configuration, not a payment settlement guarantee, a legal ownership determination or proof that a beneficiary bank received funds. [[adyen-platforms]]

## Schedule scope and constraints

- Adyen contact involvement is part of creating managed payout schedules and choosing parameters around desired receipt time, sales-day closing time and user time zone. A balance account can use only one managed payout schedule per currency, and each schedule supports one location and currency. Managed schedules support **local payouts in the same country and currency**; different payout currency or a bank account in another country is routed to custom payouts. The page gives no direct self-service/API role or bank-instrument setup procedure here. See raw lines 19–37.
- Managed payout schedules do **not** change settlement timing for pass-through settlement or sales-day payouts of T+7 or more. Those payments settle according to their indicated delay and pay out once settled. Thus an accelerated schedule cannot be read as overriding the underlying settlement delay. See raw lines 33–36.
- The page's configuration table distinguishes **Standard** and **Accelerated** types, described as two or one days after settlement, and weekday, weekly or monthly payout frequency. Weekly/monthly runs include funds only up to one or two days before the chosen date. Payout ETA is explicitly **estimated** and depends on local/currency cutoffs and the Adyen contract. Minimum/maximum payout amounts and a retained balance can constrain what leaves the balance account; the payout description appears on a user's bank statement and is set with Adyen contact help for local requirements. These are configuration choices and descriptions, not proof of a specific payout's arrival. See raw lines 39–49.
- The US example selects a weekday Standard schedule, 9 AM local ETA, USD 200 minimum and USD 100 retained amount before applying it to users' balance accounts. These numbers illustrate one desired setup; they do not create global payout thresholds, a guaranteed arrival time or bank-credit evidence. After going live, the platform can contact Adyen to update or add schedules. For multiple locations and supported payout currencies, the page calls for a schedule per location/currency; its EU/US/Canada example is illustrative. See raw lines 51–87.

## Evidence boundary and next routes

- The page routes implementation to **Use managed payouts** and observation to **View payout executions**, but does not itself show an execution record, a failure/return lifecycle or beneficiary-bank confirmation. Use the specific execution and transfer evidence for any actual payout outcome; a configured schedule or estimated ETA does not prove that funds left a balance account or reached a bank. See raw lines 89–102.

## Detail locators

- **Product purpose, Adyen contact and desired-receipt/closing-time/time-zone inputs:** raw lines 15–25.
- **One schedule per currency/account, one location/currency per schedule, local-only route and settlement-delay limit:** raw lines 27–37.
- **Type, frequency, ETA/cutoff/contract, amount controls and bank-description parameters:** raw lines 39–49.
- **Illustrative US schedule and post-live update route:** raw lines 51–75.
- **Multiple-location/currency schedules and child-page navigation:** raw lines 77–102.

## Related

- [[adyen-platforms]]

## Raw Sources

- [[raw/adyen/docs/platforms/managed-payouts/2026-09-15|Adyen Platforms managed-payout overview — collected 2026-09-15]]
