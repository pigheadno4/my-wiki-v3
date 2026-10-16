---
title: "Adyen Platforms customize hosted onboarding"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/onboard-users/customize-hosted-onboarding"
raw_files:
  - "adyen/docs/platforms/onboard-users/customize-hosted-onboarding/2026-09-15.md"
tags: [adyen, platforms, hosted-onboarding, themes, verification]
---

## Overview

This Adyen page (last modified 2024-02-27; captured 2026-09-15) covers customization, testing and troubleshooting of a hosted onboarding page for Adyen for Platforms or Adyen Issuing integrations. It describes Customer Area themes, locale and settings supplied when creating an onboarding link, test-only instant-bank-verification credentials, and a debug UI. These presentation and user-action controls do not themselves change Adyen's verification requirements, grant an account-holder capability, or prove onboarding approval. See [[adyen]] and [[adyen-platforms]] for the Platforms route; Issuing remains a separately scoped integration.

## Key takeaways

- **Prerequisites and theme identity:** For API-initiated hosted onboarding, the page requires Legal Entity Management API credentials. Creating or editing themes in Customer Area requires Manage hosted onboarding themes plus Balance platform admin role or Balance platform base role. The company-account Developers > Onboarding themes flow sets logo, header, background, browser tab, external links and optional invitation email appearance. A saved theme has a unique ID passed to the onboardingLinks request; Onboarding on Invite separately requires Apply to use the theme for invites and the hosted page. Logo/header/redirect, readable contrast and support-link choices are recommendations, not verification gates.
- **Link-level controls:** The onboardingLinks request may set locale and settings. Browser language is the default, with en-US fallback if unsupported; an unsupported locale falls to an available value for its language. Settings govern selected user actions, including acceptedCountries when editPrefilledCountry is allowed, bank-account format choice, intra-region cross-border payout-account choice, legal-entity type/country editing, legal-age enforcement, instant bank verification UI, PCI-questionnaire signing flags, transfer-instrument limit and debug UI. Defaults and exact conditions are in the raw table; these switches are not evidence of country eligibility, KYC success, PCI compliance or actual payout.
- **Testing and troubleshooting:** The instant-bank-verification accounts and credentials are explicitly for the test environment, not proof of live bank verification. The browser debug UI is enabled by default, intended for support and engineering rather than platform users, and can be disabled through allowDebugUi. Its report includes SDK version, locale, main legal-entity ID, settings, task statuses and legal-entity data; the guide says it is sensitive and should be shared only to the minimum necessary with the team or Adyen Support.
- The page does not identify an onboarding-version requirement. Its dated examples and locale/country table require current integration and API checks before use. The PCI flag rows combine 'required to sign' with 'set true to allow' wording; do not infer a compliance outcome from that wording alone.

## Detail locators

- Integration and API/Customer Area role prerequisites: pinned raw lines 29-37.
- Theme creation, Apply versus theme ID, brand assets and email scope: pinned raw lines 39-108.
- Theme view/update and locale fallback: pinned raw lines 110-140; dated language list at 142-168.
- Link settings, conditions and defaults, including acceptedCountries, age, verification, PCI flags and debug UI: pinned raw lines 170-192.
- Test-only bank credentials: pinned raw lines 194-220. Debug UI audience, sensitive report and contents: lines 222-243.

## Related

- [[adyen-platforms]] — platform onboarding concept and reciprocal source route.
- [[source-adyen-docs-platforms-onboard-users-onboarding-versions-onboarding-v4]] — separate version-specific onboarding evidence.
- [[source-adyen-docs-platforms-verification-requirements]] — separate verification-input scope.

## Raw Sources

- [[raw/adyen/docs/platforms/onboard-users/customize-hosted-onboarding/2026-09-15|Adyen Customize and test hosted onboarding, captured 2026-09-15]]
