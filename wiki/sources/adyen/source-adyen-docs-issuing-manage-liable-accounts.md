---
title: "Adyen Issuing: Manage liable balance accounts"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/manage-liable-accounts"
raw_files:
  - "adyen/docs/issuing/manage-liable-accounts/2026-09-15.md"
tags: [adyen, issuing, balance-platform, liable-balance-account, split-payments]
---

## Overview

This 2026-09-15 Adyen guide identifies two **platform-owned**, platform-funds-holding liable balance accounts in a balance platform: its main liable balance account and a reserved incorrect-splits account. It describes booking and correction paths, not evidence that a particular payment split or internal transfer has executed. [[adyen]] [[adyen-issuing]]

## Key takeaways

- The **main liable balance account** is tied to the balance platform and holds most of its funds. Adyen says transaction commissions on the platform are booked there; the platform may also use it to pay users' transaction fees or transfer funds to users, such as for balance corrections (raw lines 24-26). These are platform funds and actions, distinct from a user's balance account and card-linked funds.
- The **reserved incorrect-splits account** receives funds that an erroneous split would otherwise book to a nonexistent balance account or one unable to receive funds. The guide names a closed or suspended balance account, a closed or suspended account holder, or a holder lacking the required receive-funds capability as cases (raw lines 28-36).
- Adyen says the platform can later correct balances by transferring funds internally from that reserved account to another balance account on its platform (raw line 36). This is a possible correction route, not automatic recovery or proof of an actual internal transfer, card authorization, capture, or payout.

## Detail locators

- Platform ownership and account types: raw lines 19-22. Main-account bookings and uses: raw lines 24-26. Incorrect-split trigger and correction route: raw lines 28-36. The linked transfer-funds guide, not this short page, governs transfer execution details.

## Related

- [[adyen]] — provider.
- [[adyen-issuing]] — Issuing concept and source route.
- [[adyen-platforms]] — platform balance context.

## Raw Sources

- [[raw/adyen/docs/issuing/manage-liable-accounts/2026-09-15|2026-09-15 Adyen liable balance accounts guide]]
