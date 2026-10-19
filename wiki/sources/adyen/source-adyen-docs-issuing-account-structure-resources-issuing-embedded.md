---
title: "Adyen Embedded Issuing account structure"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/account-structure-resources/issuing-embedded"
raw_files:
  - "adyen/docs/issuing/account-structure-resources/issuing-embedded/2026-09-15.md"
tags: [adyen, issuing, embedded-issuing, account-structure]
---

## Overview

Adyen's 2026-09-15 captured guide describes account resources for a platform or marketplace offering business expense cards to independent business users. The users fund their cards: in **embedded issuing with acquiring**, the platform acquires their customer payments through Adyen; in **standalone embedded issuing**, it does not acquire those payments through Adyen and the users top up from verified transfer instruments. These are resource and example descriptions, not proof that a particular platform is eligible or that a card, transfer, or payment has succeeded. [[adyen-issuing]] [[adyen]]

## Key takeaways

- **Acquiring model:** The guide says a balance platform and merchant account are required in each region where the platform is registered and wants to acquire. In its salon example, the platform owns the company account, regional merchant accounts and balance platforms, liable account holder and liable balance account, and business legal entities for verification; user/cardholder resources include country-linked stores and account holders, currency balance accounts, card-linked balance accounts, verified transfer instruments, user legal entities for KYC, business lines, and card payment instruments. The example says customer transactions settle in the merchant accounts. See raw lines 26–80.
- **Standalone model:** The construction-platform example has a platform company account, merchant account, linked balance platform, liable account holder and balance account, and legal entity. Each user has an account holder, balance accounts, verified transfer instrument for top-ups, legal entities for KYC, and a card payment instrument. The page explicitly says this model does not acquire user payments through Adyen. See raw lines 86–122.
- **Card funding boundary in both examples:** An account holder has at least one balance account per currency for user funds and one or more accounts linked to cards; multiple cards may share a card-linked account, but it must be separate from the balance account holding the user's funds. The card is connected to the cardholder's balance account, from which the example says card spending is deducted. See raw lines 68–80 and 112–122.
- **Source inconsistency:** In the salon acquiring example, the business-line description unexpectedly says food and delivery services and the card-spend sentence says food orders. Treat those as an internal example mismatch, not a definition of salon industry or required card use. See raw lines 30, 78–80.

## Detail locators

- Model definitions and user responsibility for funding: raw lines 19–24.
- Acquiring regional condition and platform/cardholder ownership lists: raw lines 32–80.
- Standalone example and ownership lists: raw lines 86–122.
- Verified transfer instruments may be used for payout or top-up in the acquiring example, while the standalone example specifically describes top-up: raw lines 74 and 118.

## Related

- [[adyen-issuing]] — main Issuing concept.
- [[adyen-platforms]] — platform context.

## Raw Sources

- [[raw/adyen/docs/issuing/account-structure-resources/issuing-embedded/2026-09-15|Account structure with Embedded issuing, captured 2026-09-15]]
