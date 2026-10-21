---
title: "Adyen Marketplaces get started"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/get-started"
raw_files:
  - "adyen/docs/marketplaces/get-started/2026-09-15.md"
tags: [adyen, marketplaces, onboarding, integration, go-live]
---

## Overview

This 2022-modified Marketplace get-started guide, captured 2026-09-15, lays out the route from contacting Adyen and designing a marketplace integration through test implementation, live-account application, live configuration and further testing. It is scoped to Adyen for Platforms marketplace use cases and uses account holders and balance accounts; it does not describe the older Classic Platforms account model. [[adyen]] [[adyen-marketplaces]]

## Key takeaways

- The guide requires contacting Adyen to register interest; Adyen then helps assess whether its marketplace capabilities fit the use case (raw lines 21–28, 42–44). An Adyen contact works with the platform to design user data/document collection, online payment splits, risk, payouts, reporting and reconciliation (raw lines 46–54). The example split description passes sale amount and some fees to a user while booking commission and remaining fees to the marketplace; it is a design topic, not evidence of a particular executed split.
- Adyen sets up a test account and sends Customer Area admin credentials. The dashboard can manage company/merchant accounts, account holders, balance accounts, payments/transfers, API credentials, webhooks, reports and optional financial products (raw lines 56–69). Having dashboard access or resources does not establish live activation or a successful payment/payout.
- Build after receiving test credentials, test the API integration in the test environment, and contact Adyen to take the account live after building and testing (raw lines 71–87). The guide recommends testing again after live configuration (raw lines 77–81).
- Test-account setup and configuration are **not replicated** to the live account. The platform must separately reproduce the setup and test its integration in the live environment; the page also points to a go-live checklist (raw lines 89–95). Applying for live or completing a test is not proof that a live account is configured or that money moved.

## Detail locators

- Integration type, sales-contact requirement and seven-step sequence: raw lines 21–44. Design areas for onboarding, splits, risk, payouts and reporting: raw lines 46–54.
- Test Customer Area setup/resources: raw lines 56–69. Build, test and live-account contact: raw lines 71–87. Separate live setup and live testing: raw lines 89–95.

## Related

- [[adyen-marketplaces]] — Marketplace model and source route.
- [[adyen-platforms]] — broader current Adyen for Platforms context; Marketplace guide remains a separate route.
- [[adyen-classic-platforms]] — older Classic integration with distinct account/resources.

## Raw Sources

- [[raw/adyen/docs/marketplaces/get-started/2026-09-15|Marketplace get started, captured 2026-09-15]]
