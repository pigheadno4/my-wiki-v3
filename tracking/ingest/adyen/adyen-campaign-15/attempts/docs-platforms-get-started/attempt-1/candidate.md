---
title: "Get started with Adyen for Platforms"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/get-started"
raw_files:
  - "adyen/docs/platforms/get-started/2026-09-15.md"
tags: [adyen, platforms, onboarding, integration, go-live]
---

## Overview

Adyen's Platforms getting-started guide (page metadata last modified 2022-10-26; captured 2026-09-15) outlines the process from contacting Adyen through scoping, test-account setup, building/testing, live application and separate live configuration. It is an orientation for an Adyen for Platforms integration, not a contract, current availability decision, merchant-of-record allocation, completed user verification, capability grant, payment split, payout or live approval. The platform-family route is [[adyen-platforms]]; this page does not define Classic Platforms, the separate Marketplaces documentation, or an Issuing implementation.

## Key takeaways

- Contact Adyen to register interest and have Adyen assess whether its **current platform capabilities** fit the use case. This is a sales/design prerequisite, not an automatic platform-account entitlement (raw lines 21–28, 42–44).
- Scope and design with an Adyen contact how the platform collects user data/documents, accepts online and/or in-person payments, splits sale amounts/fees/commission, manages transaction-level risk, pays users, and reports/reconciles platform and user balances. These are design topics and links to child guides, not confirmed settings or financial outcomes (raw lines 46–54).
- Adyen sets up a test account and sends Customer Area admin credentials. The page lists company account, merchant account, account holders and balance accounts as managed platform resources, alongside payments/transfers, API credentials, webhooks, reports and financial products such as Issuing/Capital. It does not define legal ownership or liabilities of those accounts, a reserve/liable account, or a transfer instrument; consult dedicated resources before choosing an architecture (raw lines 56–69).
- With test credentials, build against the platform integration guides and test what was built in the test environment. After test integration, contact Adyen to take the account live; applying is a separate step from approval or activation (raw lines 71–87).
- **Test setup is not replicated to live.** Replicate configuration in the live environment, test there too, and follow the linked go-live checklist. A completed local/test integration is not proof of live readiness, verified users, granted capabilities, payment execution or payout receipt (raw lines 89–95).

## Detail locators

- Scope, contact requirement and ordered onboarding steps: raw lines 15–44.
- Design topics and user/payment/balance planning links: raw lines 46–54.
- Test account, Customer Area and resource identities: raw lines 56–69.
- Build/test/live application and separate live configuration: raw lines 71–101.

## Related

- [[adyen-platforms]] — dedicated Adyen for Platforms concept and source route.
- [[adyen-account-structure]] — separate company/merchant account hierarchy; not the whole platform funds model.
- [[adyen-financial-products]] — separate financial-products family, mentioned only as Customer Area management navigation here.
- [[adyen]] — provider page.

## Raw Sources

- [[raw/adyen/docs/platforms/get-started/2026-09-15|Adyen for Platforms getting-started, captured 2026-09-15]]
