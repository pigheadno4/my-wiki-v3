---
title: "Adyen for Platforms balance-account top-up overview"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/top-up-balance-account"
raw_files:
  - "adyen/docs/platforms/top-up-balance-account/2026-09-15.md"
tags: [adyen, platforms, top-ups, balance-accounts, transfers]
---

## Overview

This 2026-09-15 Adyen for Platforms overview defines a top-up as an incoming transfer from an external source that increases a platform user's balance account, which otherwise commonly receives customer-payment funds. It also says the platform's liable balance account may be topped up if needed. The page routes to scheduled and on-demand top-ups and to webhook guidance; it does not by itself define their distinct request schemas, funding-method eligibility, fee handling, state transitions or proof of completed credit.

## Key takeaways

- The stated use cases are covering negative balances after refunds or chargebacks and ensuring a user balance account has enough funds for a transfer. These are purposes for a top-up, not a guarantee that a particular deficit is cured or subsequent transfer succeeds.
- A scheduled top-up is configured to trigger according to timing and amount; an on-demand top-up is initiated when needed, in addition to or instead of a schedule. The page's description names a pull sweep and direct debit from a verified transfer instrument, while the body covers both routes. Treat that description as a route cue, not a rule that every on-demand top-up uses a pull sweep or direct debit; consult the linked route-specific guides.
- After a scheduled or on-demand top-up is initiated, Adyen says it triggers an incoming external transfer from the request's specified source into the target balance account. Triggering is distinct from a successful debit of the external source and a booked credit to the user or liable balance account. The linked webhook guide owns event and outcome interpretation. This overview does not establish current eligibility, source-bank ownership, legal fund ownership, a completed transfer, or a beneficiary bank receipt.

## Detail locators

- Opening — user balance-account and liable-balance-account destinations, top-up definition, and refund/chargeback or transfer-liquidity use cases (raw lines 15–28).
- `How it works` — scheduled versus on-demand selection and incoming-external-transfer trigger after initiation (lines 30–37).
- `Next steps` — route to scheduled, on-demand and top-up webhook guides; these linked pages own detailed fields, method and status rules (lines 39–51).

## Related

- Company: [[adyen]]
- Main concept: [[adyen-platforms]]
- Related sources: [[source-adyen-docs-platforms-top-up-balance-account-scheduled-top-ups]], [[source-adyen-docs-platforms-top-up-balance-account-on-demand-top-ups]], [[source-adyen-docs-platforms-top-up-balance-account-top-up-webhooks]]

## Raw Sources

- [[raw/adyen/docs/platforms/top-up-balance-account/2026-09-15|2026-09-15 Platforms balance-account top-up overview]]
