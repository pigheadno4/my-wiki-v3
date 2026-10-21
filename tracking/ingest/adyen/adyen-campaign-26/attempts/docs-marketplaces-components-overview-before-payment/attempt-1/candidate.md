---
title: "Adyen Marketplace before-payment components"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/components-overview/before-payment"
raw_files:
  - "adyen/docs/marketplaces/components-overview/before-payment/2026-09-15.md"
tags: [adyen, marketplaces, platforms, ui-components, onboarding]
---

## Overview

This 2026-09-15 Marketplace page is a short **before-payment Onboarding component navigation hub**. It says users must be onboarded and their identity/business information verified before the marketplace accepts payments on their behalf; components let users enter and submit that information to Adyen in the platform UI. The page lists Individual Legal Entity, Terms of Service and Transfer Instrument child routes. These brief card descriptions are not a detailed integration specification or proof of completed verification. See [[adyen]] and [[adyen-platform-components]].

## Key takeaways

- **Individual Legal Entity card:** Routes to a component for personal details and identity-document submission, status display and updates. This hub does not give entity-specific requirements, document acceptance or a completed identity-verification result (raw lines 21–25).
- **Terms of Service card:** Routes to viewing and accepting required Terms documents, monitoring status and downloading signed copies. The card does not establish that a particular user accepted the current terms or that every onboarding/capability gate is satisfied (raw lines 27–31).
- **Transfer Instrument card:** Routes to bank-account add/update/delete, instant-verification or document-upload paths and verification-status view. These are advertised child capabilities, not proof a bank instrument exists, passed Adyen verification or can receive a payout. A separate detailed Marketplace Transfer Instrument guide owns the integration and version boundaries (raw lines 33–37).
- **Navigation boundary:** The Marketplace-path hub names all three child cards, whereas the captured parallel Platforms-path before-payment hub names Transfer Instrument only. Use this page to select the relevant child guide; it provides no session credential/role, LEM/API version, region, account eligibility or payment-outcome rule. It also links to an Onboarding components page and the general component library (raw lines 19–42).

## Detail locators

- Onboarding and verification purpose: pinned raw lines 15–19.
- Individual Legal Entity, Terms of Service, Transfer Instrument card labels and summaries: pinned raw lines 21–37.
- Onboarding-components and general library routes: pinned raw lines 39–42.

## Related

- [[adyen-platform-components]] — main component-suite concept.
- [[adyen-platforms]] — marketplace/platform context.
- [[source-adyen-docs-marketplaces-components-overview-before-payment-transfer-instrument-component]] — existing detailed bank-instrument child guide.
- [[source-adyen-docs-platforms-components-overview-before-payment]] — parallel Platforms-path hub with a narrower listed child set.

## Raw Sources

- [[raw/adyen/docs/marketplaces/components-overview/before-payment/2026-09-15|Marketplace before-payment component hub, captured 2026-09-15]]
