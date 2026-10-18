---
title: "Account structure | Adyen Business accounts"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/account-structure-resources"
raw_files:
  - "adyen/docs/business-accounts/account-structure-resources/2026-09-15.md"
tags: [adyen, business-accounts, platforms, account-structure]
---

## Overview

This 2021-modified, 2026-09-15-captured [[adyen]] Business accounts guide describes how Adyen for Platforms merchant accounts, a region-specific balance platform, account holders, legal entities, balance accounts and an externally facing `paymentInstrument` fit together. It distinguishes a payout transfer instrument from the Adyen-issued `bankAccount` payment instrument used for Business accounts. See [[adyen-business-accounts]] for the product route. The guide is structural documentation, not proof that an account or bank account number was created or that a named party owns funds.

## Key takeaways

- Business accounts are usually used with Adyen for Platforms. The page says merchant accounts connect to a balance platform that manages internal fund flows and that a separate balance platform is needed for each acquiring region. It routes to onboarding/capability requests, account-holder authentication, third-party send/receive funds and Open Banking guides; these are navigation, not demonstrated enabled capabilities. [Raw: lines 19–31]
- To enable a user, the page names an **account holder** linked to that user's **main legal entity** and balance account. The account holder determines what the user can do, with examples including transfers into a balance account and payouts to a **verified transfer instrument** (bank account). The **balance account** holds user funds and is the route for financial activities. Neither label alone establishes verification status, legal ownership or a successful payout. [Raw: lines 33–36]
- The prose says that a Business accounts user must have **two balance accounts**: one for holding funds and one linked to the business account payment instrument. It then gives an example of an account holder with **one** balance account linked to a `bankAccount` payment instrument, as well as a two-account example. This is an internal one-versus-two-account tension; do not turn the one-account diagram into a permitted production configuration or silently erase the example. Verify the applicable current integration design with Adyen before implementation. [Raw: lines 36, 44–49]
- For Business accounts, the page describes an Adyen-issued bank account as an externally facing `paymentInstrument` interacting with an associated balance account. It says creating that instrument generates an account number and each balance account may have only one `bankAccount` payment instrument. That payment instrument differs from the verified transfer instrument mentioned for payouts. The resource description does not prove actual account opening, assigned number, legal holder, funds availability or a completed third-party transfer. [Raw: lines 35, 38–47]

## Detail locators

- Platforms/balance-platform relationship and per-acquiring-region separation: raw lines 19–31.
- Account-holder, legal-entity, balance-account and payout transfer-instrument roles: raw lines 33–36.
- Business-account `paymentInstrument`, generated account number and one-per-balance-account limit: raw lines 38–42.
- Two-account requirement versus one-/two-account examples: raw lines 36, 44–49.

## Related

- [[adyen-business-accounts]] — Business accounts product route
- [[adyen-platforms]] — balance-platform context
- [Adyen for Platforms account structure](https://docs.adyen.com/platforms/account-structure-resources) — linked general model
- [Onboard users](https://docs.adyen.com/business-accounts/onboard-users) — linked onboarding guide
- [Manage account holders](https://docs.adyen.com/business-accounts/manage-account-holders) — linked capability context

## Raw Sources

- [[raw/adyen/docs/business-accounts/account-structure-resources/2026-09-15|Adyen Business accounts account structure — collected 2026-09-15]]
