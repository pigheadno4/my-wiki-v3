---
title: "Adyen Platforms Transfer Instrument components"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/components-overview/before-payment/transfer-instrument-component"
raw_files:
  - "adyen/docs/platforms/components-overview/before-payment/transfer-instrument-component/2026-09-15.md"
tags: [adyen, platforms, onboarding, ui-components, transfer-instruments, verification]
---

## Overview

This 2026-09-15 Platforms component guide covers the Transfer Instrument Configuration and Management UI components for bank-account information in an API-only onboarding flow. Configuration allows permission-based instant verification or document upload for Adyen to validate a bank account. Management lists instruments with verification statuses and errors and supports add, edit, and remove user flows. This component path covers transfer instruments only; the rest of API-only onboarding still needs separate API integration. Its statements overlap the existing [[source-adyen-docs-platforms-onboard-users-components]] guide but retain this page's distinct canonical route and raw evidence.

## Key takeaways

- Onboarding components work only with legal entities created with **Legal Entity Management API v3 or v4**. The guide requires Adyen for Platforms, a Legal Entity Management API key to create authentication sessions, language/browser support, preceding API-only onboarding steps, and review of verification guidance. Feature guidance also varies by component-library version; the API entity version and library version are separate qualifications.
- The platform server sends Session Authentication API `POST /sessions` with the LEM API key, an allowed origin (HTTPS on live), `product=onboarding`, and a `legalEntity` policy resource. Its `legalEntityId` is the entity with the platform contractual relationship that owns the bank account; for a sole proprietorship it is the individual owner's entity ID. Policy roles are `transferInstrumentConfiguration` and/or `transferInstrumentManagement` for the enabled components. The session response is passed to the frontend through a token-refresh callback; the sample URL is a test endpoint, not a live operation.
- Configuration collects bank-account information and offers an instant-verification permission path or document upload for Adyen validation. Management displays the added accounts with statuses/errors and lets users add, edit, or delete. The guide says changes are applied immediately, but a component entry or displayed status alone does not prove verification approval, payout eligibility, a successful payout, or bank receipt.
- Component properties specify `test` versus `live`, locale, root legal-entity ID, token callback, and component events. The configuration `complete` event means successful submission and UI completion; management `add`, `edit`, and `remove` events signal actions to the host application. The example completion payload includes bank account details and empty verification fields, so use the actual resource and verification status to establish outcomes.
- The configuration `openBankingPartnerConfigId` row marks it required for US/CA and says Adyen can customize the brand identifier for open-banking verification. Optional settings concern intra-region cross-border payout-account selection and local versus IBAN format where applicable; they do not grant country-wide payout eligibility. This snapshot lists supported locales and links browser support to the general components page.

## Detail locators

- Opening through `## Requirements`: LEM v3/v4, API-only scope, version variance, prerequisites.
- `## Transfer Instrument Configuration component` and `## Transfer Instrument Management component`: bank-data collection, validation paths, status/error list and changes.
- `## 1. Create an authentication session from your server`: LEM credential, legal-entity scope, role, origin and onboarding product.
- `## 3. Configure component properties`: environment, root entity, callbacks, US/CA identifier, optional settings.
- `## User flow and events`: event semantics and illustrative data payload.
- `## Supported languages`: locales.

## Related

- [[adyen-platform-components]] — main component-suite concept.
- [[adyen-platforms]] — parent Platforms context.
- [[source-adyen-docs-platforms-onboard-users-components]] — overlapping onboarding-components guide.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/components-overview/before-payment/transfer-instrument-component/2026-09-15|Adyen Transfer Instrument components guide (fetched 2026-09-15)]]
