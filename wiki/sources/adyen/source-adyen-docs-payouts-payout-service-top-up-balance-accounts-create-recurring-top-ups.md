---
title: "Adyen Payout Service recurring balance-account top-ups"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/top-up-balance-accounts/create-recurring-top-ups"
raw_files:
  - "adyen/docs/payouts/payout-service/top-up-balance-accounts/create-recurring-top-ups/2026-09-15.md"
tags: [adyen, payouts, payout-service, top-ups, direct-debit, balance-accounts]
---

## Overview

This 2020-modified, 2026-09-15-captured [[adyen]] **enterprise-payouts** guide configures recurring **bank direct-debit pulls from a funding transfer instrument into the business's balance account**. A configured schedule can trigger a direct-debit request when balance conditions are met; Adyen describes later booking to the balance account. Schedule creation, an active status or a trigger record is not proof that a debit succeeded, funds settled, or the balance was credited. [[adyen-payouts]]

## Key takeaways

- The API route requires a Configuration API credential with **BankAPI Advanced Webservice role**; Customer Area setup requires **Balance platform base** and **Configure scheduled payouts** roles. The account holder must have active **receiveFromTransferInstrument** capability with valid `verificationStatus`; the source instrument needs sufficient funds. The page supports **EUR and USD only** and explicitly excludes on-demand top-ups. For API setup, Terms of Service must be accepted first; Customer Area handles the direct-debit agreement in its wizard. Configuration, Transfer and Transaction webhooks are listed for monitoring. See raw lines 23–38 and 248–252.
- The Configuration API uses `POST /balanceAccounts/{balanceAccountId}/recurringTopUps` with source `counterparty`, description, `topUpAmount` and `trigger`; a transfer-instrument source requires `counterparty.transferInstrumentId`. Select **exactly one** of fixed top-up or target-balance amount, in currency minor units; specifying both fails. The threshold is required; schedule checks can be weekdays, weekly, monthly or continuously monitored by default. An optional `status` defaults to active. See raw lines 40–99.
- **Threshold boundary conflict:** the API table says a top-up triggers when available balance is **below** the threshold, while Customer Area says **less than or equal to**. At an exact threshold, this page does not establish which trigger rule wins; verify the selected channel's behavior before relying on it. See raw lines 95–99 and 240–246.
- **Field-name conflict:** the API table calls the fixed-amount branch `topUpAmount.fixed`, but the later placeholder example uses `topUpAmount.fixedAmount`. Do not copy that example as an authoritative schema for fixed top-ups without checking the API reference. See raw lines 76–83 and 203–225.
- The example's USD 500 available balance is **above** its USD 250 weekly trigger, so the shown `active` response is schedule creation, not a direct-debit or credit event. When a top-up does trigger, a transfer record appears; Transfer/Transaction views and the Balance Platform Accounting Report distinguish its status and booked transactions (`topUp`/`bankDirectDebit`). See raw lines 103–178 and 254–268.
- For timed schedules the guide states a 07:00 trigger in the **account's timezone** and gives USD T+2 and EUR next-business-day settlement examples tied to **ET/CET cutoff times**. These are dated timing descriptions, not a universal credit guarantee across account timezones or failed funding/route conditions. Creation can fail for invalid currency, inactive direct-debit configuration/capability, unsigned terms, unavailable route, insufficient access to instrument or duplicate sweep. See raw lines 270–304.

## Detail locators

- **Direction, roles, capability, currency and agreement gates:** raw lines 19–38.
- **API create fields, amount exclusivity and threshold schedule:** raw lines 40–99.
- **Weekly USD example and active response:** raw lines 103–178.
- **Dynamic descriptions and fixed-field mismatch:** raw lines 182–225.
- **Customer Area wizard and threshold disagreement:** raw lines 228–252.
- **Tracking, dated cutoffs and creation errors:** raw lines 254–304.

## Related

- [[adyen-payouts]]
- [Manage recurring top-ups](https://docs.adyen.com/payouts/payout-service/top-up-balance-accounts/manage-recurring-top-ups)
- [Top-up webhooks](https://docs.adyen.com/payouts/payout-service/top-up-balance-accounts/top-up-webhooks)

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/top-up-balance-accounts/create-recurring-top-ups/2026-09-15|Adyen recurring top-ups — collected 2026-09-15]]
