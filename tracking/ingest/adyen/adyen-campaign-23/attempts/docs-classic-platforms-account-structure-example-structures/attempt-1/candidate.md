---
title: "Classic Platforms example account structures"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/account-structure/example-structures"
raw_files:
  - "adyen/docs/classic-platforms/account-structure/example-structures/2026-09-15.md"
tags: [adyen, classic-platforms, account-structure, splits, payouts]
---

## Overview

This Classic Adyen for Platforms example page (last modified 2019-09-02; captured 2026-09-15) illustrates a company account with two merchant accounts, one platform, account holders and platform accounts, then compares simple and multiple-account/bank-account payout structures. The page directs new implementations to a different integration guide. These are **Classic** account/account-holder examples under [[adyen-classic-platforms]], with provider context at [[adyen]]; they are not the modern balance-platform resource model or proof of a real transaction.

## Key takeaways

- In its fictional **Example Travel** structure, the page lists an Adyen company account and two merchant accounts (`ExampleTravel_NL` and `ExampleTravel_US`) connected to `ExampleTravel_Platform`. That platform has a business account holder with one account, an individual account holder with multiple accounts, and the platform's own account holder and liable account (raw lines 21–37).
- The page identifies **merchant accounts and platform accounts** as the resources where funds flow. In its Dutch trip example, the customer payment is processed in the Netherlands merchant account; the illustrated split settles funds into the platform liable account and the individual account holder's **Account 2**, where account-holder funds stay until payout to that holder's **verified bank account** (raw lines 41–47). The example describes direction and destination, not an observed authorization, capture, settlement or bank receipt.
- The common one-to-one structure has one account holder, one platform account and one bank account, with payout from the platform account to the holder's verified bank account (raw lines 49–58).
- An account holder can optionally have multiple platform accounts to separate business-line funds/accounting history and can have multiple bank accounts. For many-to-many relationships, the platform selects the **source account** and **verified destination bank account** when instructing payout. The illustration chooses Account 2 to Bank account 1; one-to-many or many-to-one structures require specifying whichever source or destination is ambiguous (raw lines 60–79). This flexibility does not imply a bank account has passed verification in a particular account.

## Detail locators

- Fictional company/merchant/platform/account-holder inventory and linked diagram: raw lines 21–37.
- Blue-box funds-flow explanation and Dutch trip split-to-payout illustration: raw lines 41–47.
- One-to-one and optional many-to-many account/bank-account structures, including payout selection: raw lines 49–79.

## Related

- [[adyen-classic-platforms]] — Classic model and source route.
- [[adyen]] — provider.
- [[adyen-index]] — provider index.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/account-structure/example-structures/2026-09-15|Classic Platforms example structures, captured 2026-09-15]]
