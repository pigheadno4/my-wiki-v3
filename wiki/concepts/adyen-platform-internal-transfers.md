---
title: "Adyen for Platforms internal fund transfers"
type: concept
category: technology
tags: [adyen, platforms, internal-transfers, balance-accounts]
---

## Definition

An Adyen for Platforms internal fund transfer moves funds between balance accounts within a platform, including platform liable-to-user, same-user and different-user balance-account relationships. It is distinct from an external payout from a balance account to a user's verified bank-account transfer instrument. The overview routes to scheduled and on-demand initiation, return and webhook detail. [[source-adyen-docs-platforms-internal-fund-transfers]]

## Evidence boundary

The overview does not define currency, timing, role, failure or booked-status rules, and it does not prove that a particular transfer, return or bank payout occurred. Use the linked process and event guides for those details.

## Sources

- [[source-adyen-docs-marketplaces-internal-fund-transfers]] — 2020-modified, 2026-09-15-captured Marketplace orientation to liable/user balance-account transfers, distinct external bank payouts and scheduled/on-demand/return/webhook process routes.


- [[source-adyen-docs-marketplaces-internal-fund-transfers-return-transfers]] — 2020-modified, 2026-09-15-captured Marketplace Transfers API guide for an equal-amount return of an original internal push transfer by incoming ID, with conditional cross-holder capabilities and webhook outcome tracking.


- [[source-adyen-docs-marketplaces-internal-fund-transfers-on-demand-fund-transfers]] — 2020-modified, 2026-09-15-captured Marketplace Customer Area/Transfers API internal balance-account guide for conditional capability gates, one extra approval, one-attempt future execution and two-sided booking evidence.


- [[source-adyen-docs-marketplaces-internal-fund-transfers-approve-cancel-transfers]] — 2020-modified, 2026-09-15-captured Marketplace optional transfer-review guide for approval, cancellation, 30-day expiry and webhooks; example payloads are bank transfers, not internal two-leg booking proof.


- [[source-adyen-docs-marketplaces-internal-fund-transfers-internal-transfer-webhooks]] — 2026-09-15-captured Marketplace Transfer-webhook guide for two-sided internal balance-account received, authorised and booked stages and nested return modifications; TEST examples have amount mismatch and do not prove bank payout.


- [[source-adyen-docs-marketplaces-internal-fund-transfers-scheduled-fund-transfers]] — 2020-modified, 2026-09-15-captured Marketplace account-to-account sweep guide for role/capability gates, account-time-zone cron, amount controls and two-sided booked-transfer evidence; optional examples drift into bank-payout fields.


- [[source-adyen-docs-platforms-internal-fund-transfers-return-transfers]] — 2020-modified, 2026-09-15-captured Platforms Transfers API guide for returning an original internal push transfer by ID and equal amount, with conditional cross-holder capabilities and webhook outcome tracking.


- [[source-adyen-docs-platforms-internal-fund-transfers-approve-cancel-transfers]] — 2020-modified, 2026-09-15-captured Platforms Transfers API optional approval/cancellation guide for pending requests, 30-day expiry and review webhooks; bank-transfer examples do not prove internal booking.


- [[source-adyen-docs-platforms-internal-fund-transfers-on-demand-fund-transfers]] — 2020-modified, 2026-09-15-captured Customer Area/Transfers API internal balance-account request guide with capability gates, optional review, one-attempt future execution and two-sided booking evidence.


- [[source-adyen-docs-platforms-internal-fund-transfers-scheduled-fund-transfers]] — 2020-modified, 2026-09-15-captured Platforms guide for scheduled internal balance-account sweeps, account-time-zone cron, prerequisites, amount controls and separate creation versus booked-transfer evidence.


- [[source-adyen-docs-platforms-internal-fund-transfers]] — 2020-modified, 2026-09-15-captured Platforms orientation to internal balance-account transfers, distinct external payouts and process routes.

- [[source-adyen-docs-platforms-internal-fund-transfers-internal-transfer-webhooks]] — 2026-09-15 Transfer-webhook guide for separate outgoing/incoming balance-account legs, received-to-authorised-to-booked internal movement and nested return modifications; test examples have amount and ID inconsistencies, and no bank payout is shown.


## Related

- [[adyen-platforms]] — parent platform context.
