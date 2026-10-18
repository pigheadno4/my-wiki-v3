---
title: "Adyen Platforms internal fund transfers overview"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/internal-fund-transfers"
raw_files:
  - "adyen/docs/platforms/internal-fund-transfers/2026-09-15.md"
tags: [adyen, platforms, internal-transfers, balance-accounts]
---

## Overview

This Adyen for Platforms orientation page (last modified 2020-09-11; captured 2026-09-15) defines internal fund transfers as movement between balance accounts within the platform. It contrasts a payout, which moves funds externally from a balance account to a user's verified bank-account transfer instrument. The page maps eligible source/destination relationships and routes to scheduled, on-demand, return and webhook guides; it does not document a particular transfer's execution or booking. See [[adyen]], [[adyen-platforms]] and [[adyen-platform-internal-transfers]].

## Key takeaways

- **Balance-account roles:** The platform can initiate transfers between its liable balance account and one user's balance account, between two balance accounts of the same user, or between balance accounts of two users within the platform. These are internal balance-account movements, not external bank payouts. The page does not state that a reserve account is a source or destination, nor does it establish ownership or available funds in any example account.
- **Initiation choices and examples:** Separate guides cover a schedule that triggers transfers by timing and amount, and on-demand transfers when needed. Example purposes include a platform bonus from liable balance to a user, an additional user fee, or a user's own balance-account movement. They are use cases, not evidence of a completed transfer or an unconditional debit permission.
- **Separate return and evidence routes:** The page links a return action described as sending funds back to the sender without creating a new transfer, plus a guide to related webhooks. It does not specify the return request, eligible status, failure handling, timing, currency, roles, API version, webhook statuses or report grain. Follow those dedicated guides and observed events for those details; this overview alone proves neither request acceptance nor booked movement.

## Detail locators

- Internal-versus-external definition and eligible balance-account relationships: pinned raw lines 15-21.
- Scheduled and on-demand initiation routes: pinned raw lines 23-26.
- Illustrative bonuses, fees and user movements: pinned raw lines 28-36.
- Separate schedule, on-demand, return and webhook navigation: pinned raw lines 38-54.

## Related

- [[adyen-platform-internal-transfers]] — main internal-transfer concept and reciprocal source route.
- [[adyen-platforms]] — parent platform context.

## Related raw API references

- [[raw/adyen/docs/platforms/internal-fund-transfers/scheduled-fund-transfers/2026-09-15|Scheduled fund transfers]] — separate route; not evidence for this entry.
- [[raw/adyen/docs/platforms/internal-fund-transfers/on-demand-fund-transfers/2026-09-15|On-demand fund transfers]] — separate route; not evidence for this entry.
- [[raw/adyen/docs/platforms/internal-fund-transfers/return-transfers/2026-09-15|Return transfers]] — separate route; not evidence for this entry.
- [[raw/adyen/docs/platforms/internal-fund-transfers/internal-transfer-webhooks/2026-09-15|Internal-transfer webhooks]] — separate route; not evidence for this entry.

## Raw Sources

- [[raw/adyen/docs/platforms/internal-fund-transfers/2026-09-15|Adyen Transfer funds internally, captured 2026-09-15]]
