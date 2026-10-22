---
title: "Adyen Payout Service balance-account top-ups"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/top-up-balance-accounts"
raw_files:
  - "adyen/docs/payouts/payout-service/top-up-balance-accounts/2026-09-15.md"
tags: [adyen, payouts, payout-service, balance-accounts, recurring-top-ups, direct-debit]
---

## Overview

This 2020-09-11-modified, 2026-09-15-captured [[adyen]] **Payout Service** overview describes recurring top-ups that pull funds **from a linked bank transfer instrument by direct debit into a balance account**. A configured balance trigger starts the outgoing direct-debit request, which can lead to an incoming balance-account transfer. This is funding for later payouts, not a payout to a beneficiary. The page's shortened request-to-balance description is not proof of a successful debit or booked credit. See [[adyen-payouts]].

## Key takeaways

- Recurring top-ups are described as maintaining enough balance for necessary transfers, including partner, claim, driver and seller payout use cases. Those are examples of what a funded balance can support, not a promise that any later payout occurs. See raw lines 17–28.
- Configure **either** a fixed top-up value or a target available-balance amount. For target amounts, the overview says the balance is increased toward that target when a top-up is triggered; the funding and credit are separate stages, so this is the configured amount logic rather than an instant-credit guarantee. See raw lines 30–35 and 64–70.
- A recurring top-up uses **both** `trigger.schedule` and `trigger.threshold`. The account-timezone schedule checks on weekdays, weekly Monday, or monthly first day at 07:00; an omitted schedule defaults to continuous monitoring. A below-threshold available balance triggers an outgoing direct-debit request. This overview says **below**, while the linked creation guide's Customer Area wording says **less than or equal to**; do not assume exact-threshold behavior is identical across setup channels. See raw lines 37–48 and [[source-adyen-docs-payouts-payout-service-top-up-balance-accounts-create-recurring-top-ups]].
- The bank funding source is identified by `counterparty.transferInstrumentId`. The page shows where to find that ID in the **test** Customer Area and says to contact an Adyen point of contact if no instrument is listed. An ID or configured schedule does not establish valid consent, sufficient funds or successful collection. See raw lines 50–62.
- The child guides carry the operational gates and status evidence: [[source-adyen-docs-payouts-payout-service-top-up-balance-accounts-sign-terms-of-service]] describes direct-debit Terms acceptance before API setup (Customer Area wizard handles its own flow); [[source-adyen-docs-payouts-payout-service-top-up-balance-accounts-create-recurring-top-ups]] adds roles, capability, currency and source-funding conditions; [[source-adyen-docs-payouts-payout-service-top-up-balance-accounts-top-up-webhooks]] separates configuration, transfer status and credited transaction and shows later rejected/returned cases. The overview's three-step process does not collapse those gates or make booking final. See raw lines 64–88 for this page's process and child navigation.

## Detail locators

- **Purpose, funding direction and payout use cases:** raw lines 15–28.
- **Fixed versus target amount:** raw lines 30–35.
- **Schedule/threshold checks and account timezone:** raw lines 37–48.
- **Funding instrument and test Customer Area lookup:** raw lines 50–62.
- **Request-to-transfer overview and child-guide routes:** raw lines 64–88.

## Related

- [[adyen-payouts]]
- [[source-adyen-docs-payouts-payout-service-top-up-balance-accounts-create-recurring-top-ups]]
- [[source-adyen-docs-payouts-payout-service-top-up-balance-accounts-sign-terms-of-service]]
- [[source-adyen-docs-payouts-payout-service-top-up-balance-accounts-top-up-webhooks]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/top-up-balance-accounts/2026-09-15|Payout Service top-up overview — collected 2026-09-15]]
