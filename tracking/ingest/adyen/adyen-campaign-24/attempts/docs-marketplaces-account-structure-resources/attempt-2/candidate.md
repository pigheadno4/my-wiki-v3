---
title: "Adyen Marketplace: account structure and resources"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/account-structure-resources"
raw_files:
  - "adyen/docs/marketplaces/account-structure-resources/2026-09-15.md"
tags: [adyen, marketplaces, account-structure, balance-platform]
---

## Overview

This Marketplace-path account-structure guide (last modified 2021-11-03; captured 2026-09-15) distinguishes the marketplace's **company and merchant accounts** in Adyen's payment-processing platform from its **balance platform** and associated account holders and balance accounts. Merchant accounts process payments for users; the balance platform accounts for incoming split funds, user balances, internal movement and payouts. The described resources and possible flows are architecture guidance, not proof that a particular marketplace has opened accounts, verified users, executed splits or paid out funds. [[adyen]] [[adyen-platforms]]

## Key takeaways

- An Adyen account includes a company account connecting one or more merchant accounts. Merchant accounts configure payment methods, processing currencies, risk rules and reports; multiple accounts may be useful for different acquiring regions and payment methods, though the page says one is usually enough.
- Merchant accounts connect to a **balance platform**, which the guide calls the accounting system for business funds flow. For a sale, it can split incoming funds between the marketplace and the user (a third-party seller, service provider or contractor). The default statement is a separate balance platform for each acquiring region. The page then makes a special case for a global marketplace with multiregional sellers who transfer funds to each other: **one balance platform for all acquiring regions**, with **no additional financial products** for users. Do not apply the default and special case simultaneously.
- Depending on the marketplace's business model and use case, the user resources to create include an **account holder** carrying capabilities, linked to that user's **main legal entity and balance account**; the user's balance account holds that user's funds. A transfer instrument is identified here as a verified bank account for payout. This separates user identity/capabilities, held funds and external destination.
- The marketplace's own **liable account holder** represents its business; its **liable balance account** holds its funds and may be debited when user balance accounts go negative because of refunds or chargebacks. The page says Adyen creates the listed platform/liable resources. A negative-balance liability possibility is not evidence of an actual debit or settlement.
- Management API or Customer Area manages company/merchant processing resources, while Configuration API or Customer Area manages the balance-platform resources; these are distinct scopes.

## Detail locators

- Raw lines 19–43 describe company/merchant accounts, their processing role and management routes.
- Raw lines 45–57 describe balance-platform fund accounting, split/onboarding/payout/internal-transfer uses.
- Raw lines 59–62 give the conditional multiregion single-platform rule and product restriction.
- Raw lines 64–77 define user account holder, legal-entity link, user balance account, liable resources and their management route.

## Related

- [[adyen-platforms]] — main Platforms concept for Marketplace route.
- [[adyen]] — provider context.
- [[adyen-classic-platforms]] — separate Classic resource model.
- [[adyen-index]] — provider navigation.

## Raw Sources

- [[raw/adyen/docs/marketplaces/account-structure-resources/2026-09-15|Adyen Marketplace account structure, captured 2026-09-15]]
