---
title: "Adyen for Platforms quickstart guide"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/quickstart-guide"
raw_files:
  - "adyen/docs/platforms/quickstart-guide/2026-09-15.md"
tags: [adyen, platforms, quickstart, account-structure, onboarding]
---

## Overview

This 2026-09-15 Adyen for Platforms quickstart orients a platform to its Adyen team, three resource groups and next-step guides. It describes payment processing on behalf of platform users, who are third-party sellers, service providers or contractors. It is an account-structure and navigation page, not a complete setup, test-to-live, onboarding, payment, payout or reporting procedure. It does not establish a merchant of record, legal seller or fund owner for any particular transaction.

## Key takeaways

- During initial integration, the page identifies Sales Manager, Project Operations Manager and Implementation Manager roles; the Account Manager becomes the main contact after the Platform Review Meeting when the solution goes live. The page describes team contacts, not Customer Area permissions.
- The Adyen account group includes the company account, merchant accounts and stores. The company account represents the platform's core business and holds merchant accounts; merchant accounts process user payments and contain payment-method, currency, risk, store and report settings. Stores are described for payer-statement accuracy and easier settlement aggregation/reconciliation. The page points to the Management API for these resources.
- The balance-platform group includes the user's account holder and balance account, plus the platform's liable account holder and liable balance account. An account holder is linked to its user's balance account and main legal entity; it specifies permitted activities, with receipt of transfers and payout to a verified transfer instrument given as examples. The balance account holds user funds. The liable balance account holds platform funds and can bear deductions if user balances go negative through refunds or chargebacks. The page points to the Configuration API.
- Legal Entity Management resources comprise a user's legal entity, verified-bank-account transfer instrument, supporting documents and business line. These are described as linking the Adyen account to the balance platform and supporting verification; the page points to the Legal Entity Management API. Resource existence or example permissions do not prove completed verification, an enabled capability, a payout or bank receipt.
- The next-step list links separate guides for payments/commission allocation, onboarding/KYC, payouts, terminals, reporting, Customer Area and support. The list marks all except terminals as required, but the linked child pages contain the operational detail. This overview gives no test/live credential setup or outcome evidence; the mention of going live in the team-role section is not production activation proof.

## Detail locators

- `## Adyen Team`: contact roles and Platform Review Meeting handoff.
- `## Adyen for Platforms`: platform-user relationship.
- `### Resources`, parts 1–3: Adyen account, balance platform and Legal Entity Management objects and API routes.
- `### Account structure`: diagram and implementation-manager design reference.
- `## Next steps`: linked payments, onboarding, payouts, terminals, reporting, Customer Area and support guides.

## Related

- [[adyen-platforms]] — platform concept and source route.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/quickstart-guide/2026-09-15|Adyen for Platforms quickstart (fetched 2026-09-15)]]
