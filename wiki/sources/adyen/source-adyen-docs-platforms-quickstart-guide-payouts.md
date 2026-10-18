---
title: "Adyen for Platforms payouts quickstart"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/quickstart-guide/payouts"
raw_files:
  - "adyen/docs/platforms/quickstart-guide/payouts/2026-09-15.md"
tags: [adyen, platforms, payouts, balance-accounts, settlement]
---

## Overview

This 2026-09-15 Adyen for Platforms quickstart explains the path from a platform user's processed payment to settlement into that user's balance account, then an external payout to the user's verified bank-account transfer instrument. It compares managed automatic payouts, custom scheduled or on-demand payouts, and cashout of pending funds before settlement. It is a selection and timing guide, not a transfer request specification or evidence that a particular bank received funds.

## Key takeaways

- The page distinguishes a shopper purchase, settlement to the user's balance account, and a later external payout to a verified bank account. The settlement schedule combines sales day and settlement delay. A balance-account credit/value date is not the beneficiary bank-credit date. The guide does not establish merchant-of-record status, legal ownership or a specific user's verification/capability state.
- **Managed payouts** are presented as Adyen-managed automatic scheduling with execution tracking and estimated arrival times. **Custom payouts** give the platform control over scheduled and API-triggered on-demand payout timing. **Cashout** offers access to pending funds before settlement and is a distinct product route. Payout transfer webhooks can report events and an estimated bank arrival time after trigger; an estimate is not receipt confirmation. The linked product guides own eligibility, routing and execution details.
- Timing and amount depend on the balance account's local sales-day window, settlement delay, payout route and priority. The snapshot says a default 00:00–23:59 local sales day and a default two-business-day settlement delay, with configurable closing time up to 07:00 and a possible premium faster delay depending on region/situation. Managed/custom scheduled payout amounts use available-funds calculation; on-demand requests specify an amount. For custom scheduling, the guide recommends triggering after funds are credited and before a cutoff that varies by location, currency and priority. Its UK and US priority choices are dated recommendations, not universal rules or a promised bank arrival time.
- For methods without sales-day settlement, balance credit waits until Adyen receives funds from the payment partner. For partner-settled methods such as the named Titres-restaurant example, the guide says no value date is shown and users arrange payout with that partner; the usual Adyen balance-account payout path cannot be assumed.
- The page routes payout reconciliation to per-user balance-account dashboard components and reporting. It says Adyen passes a configured statement description to the recipient bank; its appearance on a specific bank statement is not established by this page. A missed payout for one user can reflect missing/unverified KYC details, while multiple-user misses can relate to an Adyen or bank incident; investigate account and service evidence, then use support if unresolved. These are possibilities, not diagnoses or retry instructions.

## Detail locators

- `How it works` — user balance-account settlement, verified external transfer instrument, managed/custom choice and estimated-arrival webhook route (raw lines 19–27).
- `Choose a payout solution` — managed, custom scheduled/on-demand and pre-settlement cashout distinctions (lines 29–39).
- `Fund availability` — local sales day, closing time, default delay, value date, priority, amount and partner-settlement exceptions (lines 41–50).
- `Recommendations` — custom schedule versus funds-credit and transfer-cutoff timing, regional priority suggestions and estimated-time communication (lines 52–64).
- `Payout reconciliation`, `Transfer statement descriptions` and `Missed payouts` — dashboard/report routes, description handoff to bank, KYC/incident possibilities and support route (lines 66–95).

## Related

- Company: [[adyen]]
- Main concept: [[adyen-platforms]]
- Related sources: [[source-adyen-docs-platforms-managed-payouts]], [[source-adyen-docs-platforms-custom-payouts]], [[source-adyen-docs-platforms-quickstart-guide-reporting]]

## Raw Sources

- [[raw/adyen/docs/platforms/quickstart-guide/payouts/2026-09-15|2026-09-15 Platforms payouts quickstart]]
