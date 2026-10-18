---
title: "Adyen for Platforms in-person payments"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/in-person-payments"
raw_files:
  - "adyen/docs/platforms/in-person-payments/2026-09-15.md"
tags: [adyen, platforms, in-person-payments, terminal-api, split-payments, balance-accounts]
---

## Overview

This 2023-last-modified [[adyen]] for Platforms page, captured 2026-09-15, explains processing point-of-sale payments on behalf of platform users and booking each payment's funds, commission and fees between the users' balance accounts and the platform's liable balance account. It is a Platforms in-person channel guide, not a merchant-of-record ruling, current country/product eligibility decision, or evidence that a particular terminal payment, settlement or payout completed. [[adyen-platforms]]

## Requirements and split behavior

- The stated integration path uses a POS app integrated with **Terminal API**, then payment terminals or a Mobile solution; a **standalone solution** can serve as fallback. The page requires Transfers API credentials, with additional credentials dependent on the chosen integration. It calls for a server that receives/accepts Standard webhooks and subscription to Transfer or Transaction webhooks, and account-holder capabilities **receivePayments** and **receiveFromPlatformPayments**. Listed POS design/checklist requirements differ for terminals, Android Mobile, iOS Mobile and standalone. The guide does not show that any account holder currently has those capabilities.
- Funds and fees must be booked to the correct user and platform liable balance accounts. The platform can set automatic split-configuration profiles on a user's store or supply transaction-specific split instructions in API requests; request instructions **override** profile instructions. If neither exists, the page says the **whole transaction amount and fees** book to the platform liable balance account. This default is financially material and is not an automatic user payout or commission split.
- Terminal API integrations with payment terminals or a Mobile solution can use profile or per-request splits. The standalone solution supports **profiles only** and cannot split individual payment or refund requests. Do not infer standalone request-level split support from the general POS/Terminal API statement.
- The USD 620 flow of funds is an **example**: USD 600 to a user's balance account, USD 20 commission to the liable balance account, USD 5 fees deducted there, then illustrated settlement and USD 600/USD 15 payouts to separate transfer instruments. Those values, currency and depicted lifecycle are not merchant-specific configuration, proof of an authorized/captured payment, actual settlement, or bank receipt. The page provides no country-specific availability rule or API version for this Platforms scenario; follow the linked channel guides for implementation details.

## Detail locators

- **Platforms/user in-person scope and distinct balance-account destinations:** raw lines 15–19.
- **Terminal/Mobile/standalone, credential, webhook and capability prerequisites:** raw lines 21–37.
- **Profile/request split precedence and no-instructions liable-account default:** raw lines 39–50.
- **Standalone-only profile limitation:** raw lines 52–56.
- **Illustrative USD pay-in, book, settle and payout diagram:** raw lines 58–79.

## Related

- [[adyen-platforms]]
- [[adyen-terminal-api]] — POS message/integration context
- [[adyen-payouts]] — separate payout outcome

## Raw Sources

- [[raw/adyen/docs/platforms/in-person-payments/2026-09-15|Adyen Platforms in-person payments — collected 2026-09-15]]
