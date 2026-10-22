---
title: "Adyen Payout Service third-party card payouts"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/pay-out-to-cards"
raw_files:
  - "adyen/docs/payouts/payout-service/pay-out-to-cards/2026-09-15.md"
tags: [adyen, payouts, payout-service, cards, transfers-api]
---

## Overview

This 2023-modified, 2026-09-15-captured [[adyen]] **Payout Service** guide describes sending the business's balance-account funds to a **third-party Mastercard or Visa cardholder**, such as a freelancer or provider, through the **Transfers API**. It covers one-off and recurring paths. The page says funds **typically** become available within 30 minutes, with issuer-dependent variation; this is not a guarantee of cardholder receipt for a particular request. It is separate from the legacy Online Payout API flow in [[adyen-payouts]].

## Key takeaways

- The dated support table lists **EEA** domestic and cross-border payouts to cards issued in the EEA or UK, in the card-issuance country's local currency except **ISK**; **US** domestic payouts in USD; and **UK** domestic and cross-border payouts to EEA-issued cards in GBP. The table is a guide snapshot, not proof a specific card, issuer, account or route is enabled. See raw lines 21–29.
- A **one-off** flow conditionally enables additional data in Checkout `/payments` responses when checking payout eligibility or tokenizing card details; a zero-auth eligibility check is **optional**. Card-detail tokenization is **required if the business is not fully PCI compliant**. The payout request then uses Transfers API `/transfers`. Do not turn the optional check into a universal prerequisite or assume location alone establishes card eligibility. See raw lines 40–55.
- A **recurring** flow enables additional `/payments` response data, optionally checks eligibility with zero auth, stores card details by tokenization, then requests payouts using `/transfers`. The page says its check/store steps are needed only the first time; since the check is expressly optional, this does not make zero auth mandatory. See raw lines 57–66.
- A `/transfers` request is a payout initiation step, distinct from accounting booking, card-network acceptance, later scheme checks and cardholder availability. The related [[source-adyen-docs-payouts-payout-service-payout-lifecycle]] guide distinguishes card `accepted` for processing from final availability and notes later `refused` after scheme checks. See this page's raw lines 19 and 55–66; related lifecycle raw lines 69–73 and 95–103.

## Detail locators

- **Third-party source/destination, Transfers API and timing qualifier:** raw lines 15–19.
- **EEA/US/UK issue-region and currency matrix:** raw lines 21–29.
- **One-off conditional/optional checks and PCI-dependent tokenization:** raw lines 40–55.
- **Recurring setup and subsequent payout requests:** raw lines 57–66.
- **Child navigation:** raw lines 68–76.

## Related

- [[adyen-payouts]]
- [[source-adyen-docs-payouts-payout-service-payout-lifecycle]]
- [Manage card details](https://docs.adyen.com/payouts/payout-service/pay-out-to-cards/manage-card-details)
- [Funds disbursement](https://docs.adyen.com/payouts/payout-service/pay-out-to-cards/funds-disbursement)

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/pay-out-to-cards/2026-09-15|Adyen third-party card payouts — collected 2026-09-15]]
