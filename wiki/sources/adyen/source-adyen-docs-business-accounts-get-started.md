---
title: "Get started with Business Accounts | Adyen"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/get-started"
raw_files:
  - "adyen/docs/business-accounts/get-started/2026-09-15.md"
tags: [adyen, business-accounts, platforms, integration, onboarding]
---

## Overview

This [[adyen]] Business Accounts onboarding overview, last modified 2022-10-26 and captured 2026-09-15, outlines the preparation, design, build, test and separate live setup for offering user business accounts through Adyen for Platforms. It is a route into child implementation guides, not an account-opening procedure or evidence of an opened account. See [[adyen-business-accounts]].

## Key takeaways

- The page requires an Adyen for Platforms integration. Creating business accounts must be **enabled for the balance platform**, with confirmation from an Adyen contact. It also lists implementing Adyen's Authentication SDK for PSD2 compliance for **online transactions**. This historical guide does not establish current product/country eligibility or that enablement has occurred for any platform. [Raw: lines 19–29]
- Its six-stage sequence is to complete the underlying platform or marketplace integration checklist, contact Adyen to register interest, scope/design with Adyen, build, test and configure live separately. Adyen's contact is described as helping assess whether current capabilities fit the use case, not automatically approving it. [Raw: lines 31–48]
- The design phase routes to financial-regulation guidance; required user capabilities; onboarding and Terms of Service; creating accounts for third-party fund sending/receiving; account-holder authentication; and sending, receiving and tracking transfers. Those child guides own specific resource, consent, verification, transfer and account rules. Merely following these links is not proof a user's account exists or can move funds. [Raw: lines 50–59]
- Build begins with test credentials. The platform is responsible for testing its API integration in test, and the page recommends retesting after live configuration. **Test configuration is not replicated to live**; recreate setup in live and test there too. The checklist describes work to perform, not tests or a financial operation that have been completed. [Raw: lines 61–79]

## Detail locators

- Captured provenance, Platforms prerequisite, account enablement and Authentication SDK: raw lines 1–29.
- Six stages, Adyen contact and implementation-design routes: raw lines 31–59.
- Test credentials/testing, separate live setup and go-live checklist: raw lines 61–79.
- Related account structure, detailed checklist and access guides: raw lines 81–85.

## Related

- [[adyen-business-accounts]] — Business Accounts product route
- [[adyen-platforms]] — underlying platform integration
- [Integration checklist](https://docs.adyen.com/business-accounts/integration-checklist) — detailed child setup
- [Account structures and resources](https://docs.adyen.com/business-accounts/account-structure-resources) — resource model
- [Create business accounts](https://docs.adyen.com/business-accounts/create-business-accounts) — account creation child guide

## Raw Sources

- [[raw/adyen/docs/business-accounts/get-started/2026-09-15|Adyen Business Accounts get started — collected 2026-09-15]]
