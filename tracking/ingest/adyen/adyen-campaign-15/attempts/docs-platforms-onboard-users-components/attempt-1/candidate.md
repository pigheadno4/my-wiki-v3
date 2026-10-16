---
title: "Adyen Platforms onboarding components"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/onboard-users/components"
raw_files:
  - "adyen/docs/platforms/onboard-users/components/2026-09-15.md"
tags: [adyen, platforms, onboarding, kyc-components, transfer-instruments, verification]
---

## Overview

Adyen's Platforms Onboarding components let a platform place prebuilt bank-account **transfer instrument** configuration and management UI inside its own frontend. They are compatible only with legal entities created using Legal Entity Management API **v3 or v4**. The components cover part of an API-only onboarding flow, and the guide also suggests using them alongside hosted onboarding so users can manage submitted data in the platform UI. Other API-only onboarding steps still need API calls.

## Key takeaways

- The **Transfer Instrument Configuration** component collects bank-account information and creates the transfer-instrument resource. A user can give permission for instant bank verification or upload documents for Adyen to validate the account. The **Management** component lists accounts with verification statuses/errors and lets users add or delete them; the page says changes are applied immediately. A submitted resource, `complete` event, or displayed status is not by itself verification approval, a valid payout destination for a specific payment, or proof of payout.
- Prerequisites include an Adyen for Platforms integration, a Legal Entity Management API key for Session authentication API, supported language/browser checks, completion of the linked API-only steps before creating transfer instruments, and review of verification guidance. Component-library features can vary by version; the page recommends the latest version and shows `@adyen/kyc-components`, but does not fix one package version for every integration. LEM entity-version compatibility and component-library version are separate conditions.
- The platform server creates an authentication session with the LEM API key. The request includes `allowOrigin` (the component's URL; **HTTPS only on live**), `product: onboarding`, and a policy scoped to the `legalEntityId` of the entity that has the contractual platform relationship **and owns the bank account**. For a sole proprietorship, use the individual owner's legal-entity ID. Policy roles are `transferInstrumentConfiguration` and/or `transferInstrumentManagement` for the components used. The frontend receives session data/token through a `fetchToken` refresh function; the LEM API key belongs in the server-side request, not in the example component markup.
- Component properties distinguish `test` and `live` environment and require the root legal-entity ID, token-refresh callback and locale. For configuration, `openBankingPartnerConfigId` is marked required for US/CA instant-bank-verification branding, with Adyen-contact customization; optional settings include limited intra-region cross-border account selection and local-format/IBAN choice. Consult the raw parameter rows for exact context, not as a blanket region or payout eligibility grant.
- The integration must listen for component events to manage the user flow. Configuration `complete` means the user finished and the transfer instrument was submitted; management `add`, `edit` and `remove` signal user actions. The guide's callback example contains bank-account details and partially empty verification fields; it is illustrative, not a consent record or approval payload. Handle these bank details as sensitive user data and verify the actual resource/status separately before relying on it.

## Detail locators

- Opening and `## Transfer Instrument components` — LEM v3/v4 entity compatibility, API-only versus hosted use, partial functionality and library-version warning.
- `## Requirements` / `## Transfer Instrument Configuration component` / `## Transfer Instrument Management component` — Platforms/API-key/language/browser prerequisites, permission-versus-document path, status/error display and immediate add/delete effects.
- `## 1. Create an authentication session from your server` — server request, `allowOrigin`, policy resource owner, component roles, onboarding product and token handoff.
- `## 2. Install component library in your front end` / `## 3. Configure component properties` — package import, environment, locale, root entity, refresh function, US/CA open-banking config and optional account-format/cross-border settings.
- `## User flow and events` — completion and management events plus example bank-account/verification data; an event is not a verification decision.
- `## Supported languages` — available locale codes; browser support is linked to a separate guide.

## Related

- Company: [[adyen]]
- Platforms concept: [[adyen-platforms]]

## Raw Sources

- [[raw/adyen/docs/platforms/onboard-users/components/2026-09-15|2026-09-15 Platforms Onboarding components guide]]
