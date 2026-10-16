---
title: "Adyen for Platforms account structure and resources"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/account-structure-resources"
raw_files:
  - "adyen/docs/platforms/account-structure-resources/2026-09-15.md"
tags: [adyen, platforms, account-structure, merchant-account, balance-platform, liable-account]
---

## Overview

This 2021-last-modified Adyen for Platforms account-structure guide, captured 2026-09-15, maps the payment-processing company/merchant/store resources to the balance-platform resources for the platform and its users. It provides a design vocabulary, not a statement that a specific company has these resources, has completed verification, has received money, or has a particular merchant-of-record or legal-seller role. [[adyen-platforms]]

## Resource identities and relationships

- An Adyen sign-up gives the business a **company account** containing one or more **merchant accounts**. The merchant account configures payment methods, processing currencies, account-specific risk rules, stores and reports. The page says one merchant account is enough in most cases, while separate regional merchant accounts can help manage regional methods. A **store** in a merchant account routes transactions toward the correct platform user, supports payer-statement accuracy, and can aggregate settlements for reconciliation. These are processing/configuration resources, not individual user balance accounts.
- In this Platforms model, merchant accounts connect to a **balance platform**, an accounting system for funds within the business. The page says to have a **separate balance platform for each region in which payments are acquired**. A processed sale can be split between platform and user; the users are third parties such as sellers, service providers or contractors. The page routes onward to verification, payouts, internal transfers, reconciliation and optional financial products; it does not establish a specific user's eligibility, actual split, payout or bank credit.
- For each user, depending on business model/use case, an **account holder** specifies what the user can do and must link to the user's **balance account** and **main legal entity**. The balance account holds the user's funds and is the resource through which financial activities occur. Payouts are to a **verified transfer instrument**, identified here as a bank account. An Adyen-issued **payment instrument** (card or business account) is a separate resource, and a **grant account** relates to accepted Capital offers/repayment; neither should be collapsed into a payout-bank instrument or assumed present for every user.
- The platform business also has a **liable account holder** and **liable balance account** on the balance platform. The liable balance account holds business funds, and the page says funds **can** be deducted from it if user balance accounts become negative because of refunds or chargebacks. These liable resources are stated as Adyen-created, not user-owned balance accounts or a general reserve-account definition. The page routes management through Configuration API or Customer Area.

## Detail locators

- **Company, merchant and store resource/configuration hierarchy:** raw lines 19–47.
- **Regional balance-platform requirement, user split and product navigation:** raw lines 49–61.
- **User account holder, main legal entity, balance account, payment/grant and verified bank instrument:** raw lines 63–70.
- **Platform liable resources, negative-balance condition and management routes:** raw lines 72–78.

## Related

- [[adyen-platforms]]
- [[adyen-payouts]] — separate payout lifecycle

## Raw Sources

- [[raw/adyen/docs/platforms/account-structure-resources/2026-09-15|Adyen Platforms account structure — collected 2026-09-15]]
