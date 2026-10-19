---
title: "Adyen Issuing onboarding Transfer Instrument components"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/onboard-users/components"
raw_files:
  - "adyen/docs/issuing/onboard-users/components/2026-09-15.md"
tags: [adyen, issuing, onboarding, transfer-instruments, ui-components]
---

## Overview

This 2026-09-15 Issuing-path guide describes prebuilt **Transfer Instrument Configuration** and **Transfer Instrument Management** components for collecting and managing users' bank-account information in a platform onboarding UI. It overlaps the [[source-adyen-docs-platforms-components-overview-before-payment-transfer-instrument-component]] guide under a different canonical route; this entry retains the Issuing-path snapshot. The components can create a transfer-instrument resource from entered data, but cover only part of onboarding: other API calls remain necessary. See [[adyen-issuing]] and [[adyen-platform-components]].

## Key takeaways

- These Onboarding components are compatible only with legal entities created through **Legal Entity Management API v3 or v4**. This Transfer Instrument guide requires an **Adyen for Platforms** integration and a Legal Entity Management API key for the Session Authentication API. Component guidance/features may vary by library version, a separate qualification from the legal-entity API version (raw lines 19–50).
- Configuration gathers bank-account information. A user can give permission for instant verification or upload documents for Adyen's bank-account validation. Management lists added transfer instruments with verification statuses and applicable errors and supports adding or deleting accounts; the host application handles its emitted actions (raw lines 31–35, 57–75, 562–572).
- The platform server creates an authentication session with its LEM API key. The documented session policy scopes a `legalEntity` resource to the entity with the platform contractual relationship and bank-account ownership (individual owner for a sole proprietorship), with `transferInstrumentConfiguration` and/or `transferInstrumentManagement` roles and `product=onboarding`. The allowed origin is the component URL; live supports HTTPS only (raw lines 98–113).
- The front end installs `@adyen/kyc-components`, passes a callback to fetch/refresh the session, and configures the component. The configuration `complete` event indicates successful submission and component completion; management `add`, `edit`, and `remove` events report user actions to the host application. A submission or displayed verification status alone does not establish completed verification, payout eligibility, or a successful payout (raw lines 141–232, 562–601).

## Detail locators

- Prerequisite browser/language check, preceding API-only onboarding steps and verification guidance: raw lines 43–53; these linked guides provide their own detail.
- Configuration properties: raw lines 174–189. The `openBankingPartnerConfigId` row marks it required for US/CA; optional settings address intra-region cross-border payout-account selection and local/IBAN formats where applicable.
- Management properties, token-refresh examples, HTML/React/Vue templates and callback examples: raw lines 190–389. Example endpoints, entities and event payloads are illustrative.
- Optional CSS customization: raw lines 391–558. Supported locale table: raw lines 603–631.
- The management section says changes are applied immediately to direct payouts to the intended instrument (raw line 75). Treat that as the guide's component-flow description, not proof that a bank account is verified or that a payout reached a bank.

## Related

- [[adyen-issuing]] — Issuing route and related sources.
- [[adyen-platform-components]] — component-suite concept.
- [[source-adyen-docs-platforms-components-overview-before-payment-transfer-instrument-component]] — overlapping Platforms-path guide.

## Raw Sources

- [[raw/adyen/docs/issuing/onboard-users/components/2026-09-15|Issuing onboarding components guide, captured 2026-09-15]]
