---
title: "Adyen Marketplace Transfer Instrument components"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/components-overview/before-payment/transfer-instrument-component"
raw_files:
  - "adyen/docs/marketplaces/components-overview/before-payment/transfer-instrument-component/2026-09-15.md"
tags: [adyen, marketplaces, platforms, ui-components, onboarding, transfer-instruments, verification]
---

## Overview

This 2026-09-15-captured [[adyen]] Marketplace guide covers **Transfer Instrument Configuration** and **Transfer Instrument Management** components within [[adyen-platform-components]]. They provide bank-account entry, verification workflow and management UI in an API-only onboarding flow. They cover transfer instruments only; the marketplace must integrate other onboarding steps separately. UI submission or a displayed verification status does not by itself establish approved transfer-instrument capability, payout execution or beneficiary-bank receipt.

## Key takeaways

- Onboarding components are compatible only with legal entities created under **Legal Entity Management API v3 or v4**; this is separate from the component-library version, whose features may differ. The page requires Adyen for Platforms, a LEM API key for Session Authentication API, supported language/browser versions, prior API-only onboarding steps and review of verification guidance. Adyen recommends the components within API-only onboarding but explicitly keeps other onboarding API calls necessary. See raw lines 23–53.
- **Configuration** collects bank-account information and offers permission-based instant verification or document upload for Adyen validation. **Management** lists transfer instruments with verification statuses/errors and supports adding and deleting accounts; its callback table also has an edit action. The page says changes apply immediately, but that wording concerns component account management and does not demonstrate that an instrument is verified or a payout reached the bank. See raw lines 57–85 and 192–202.
- The marketplace server creates a Session Authentication API `POST /sessions` using its LEM key. The request includes `allowOrigin` (HTTPS only in live), `product=onboarding`, a `legalEntity` resource and the ID of the legal entity that has the marketplace contractual relationship and owns the bank account (individual-owner entity for sole proprietorships). Policy roles are `transferInstrumentConfiguration` and/or `transferInstrumentManagement` for the relevant component. The session response reaches the frontend through a token-fetch/refresh callback. Do not exchange a legal-entity-scoped session for arbitrary user or platform access. See raw lines 98–151 and 180–204.
- The front end installs `@adyen/kyc-components`, imports the component and sets environment, token callback, locale and root legal-entity ID. The Configuration property table marks `openBankingPartnerConfigId` required for **US/CA** and describes open-banking partner branding; optional settings concern intra-region cross-border payout-account selection and local-versus-IBAN format only where applicable. These settings do not prove regional payout route or account eligibility. The page lists test and live component environments and supported locales. See raw lines 152–234 and 605–633.
- The host application must listen to component events. Configuration's `complete` indicates the user finished submission/UI interaction; Management's `add`, `edit` and `remove` reflect user actions. The sample `complete` data contains bank details but several null verification fields, so neither that callback nor an example account ID proves final verification. Follow the actual resource/status before relying on an instrument for payout. See raw lines 562–603.

## Detail locators

- LEM v3/v4 compatibility, component scope, version variance and prerequisites: raw lines 23–53.
- Configuration and Management user interfaces: raw lines 57–85.
- Server session, allowed origin, product, legal-entity resource and roles: raw lines 87–151.
- Package install, component properties and US/CA/optional settings: raw lines 152–234.
- HTML/React/Vue and CSS customization examples: raw lines 236–561.
- Event callbacks, sample submission data and supported locales: raw lines 562–638.

## Related

- [[adyen]] — provider profile.
- [[adyen-platform-components]] — canonical component-suite concept.
- [[adyen-platforms]] — modern platform and legal-entity context.
- [[source-adyen-docs-marketplaces-onboard-users-components]] — broader onboarding component route.
- [[source-adyen-docs-platforms-components-overview-before-payment-transfer-instrument-component]] — separate Platforms URL for the related guide.

## Raw Sources

- [[raw/adyen/docs/marketplaces/components-overview/before-payment/transfer-instrument-component/2026-09-15|Marketplace Transfer Instrument components — pinned 2026-09-15 raw snapshot]]
