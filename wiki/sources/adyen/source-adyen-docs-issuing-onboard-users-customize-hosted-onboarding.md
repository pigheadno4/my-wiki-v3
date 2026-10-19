---
title: "Adyen hosted onboarding: customize and test"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/onboard-users/customize-hosted-onboarding"
raw_files:
  - "adyen/docs/issuing/onboard-users/customize-hosted-onboarding/2026-09-15.md"
tags: [adyen, issuing, onboarding, legal-entities, themes]
---

## Overview

This 2026-09-15-captured Adyen guide covers customization, language, settings, test instant-bank-verification credentials and debugging for hosted onboarding. Its requirements explicitly allow an Adyen for Platforms **or** Adyen Issuing integration; the path location alone does not make every setting Issuing-specific. The page describes configuration and test procedures, not proof of completed legal-entity verification or current availability. [[adyen]] [[adyen-issuing]]

## Key takeaways

- API-initiated hosted onboarding requires Legal Entity Management API credentials. Creating or editing themes in Customer Area requires **Manage hosted onboarding themes** plus **Balance platform admin** or **Balance platform base** role. See raw lines 29-37.
- A theme controls logo, page header, browser-tab title/favicon, background and branded external links. Adyen *recommends* a `redirectUrl`, accessible contrast and contextual branding; these are guidance rather than all mandatory fields. After saving the theme in Customer Area, pass its unique theme ID to POST `/legalEntities/{id}/onboardingLinks` to create a hosted onboarding link. Tab title is limited to 60 characters; logo and background-image file limits are listed in raw. See lines 39-96.
- Themes and assets can be viewed in Customer Area or via Legal Entity Management `GET /themes` and `GET /themes/{id}`; Customer Area also edits themes. See raw lines 98-122.
- The page defaults to browser language, with `en-US` when that language is unsupported. A link request can specify `locale`; an unsupported locale falls to the next available value for that language (the page's `en-GB` example falls to `en-US`). Its locale table is a dated snapshot, not a current language-support claim. See raw lines 124-156.
- The onboarding-link `settings` object controls user actions. Notable defaults in the snapshot are `allowDebugUi=true`, `changeLegalEntityType=true`, `editPrefilledCountry=true`, `enforceLegalAge=false`, and `instantBankVerification=true`; `acceptedCountries` empty allows all locations supported by hosted onboarding **when** country editing is allowed. The full settings/defaults table is at raw lines 158-176.
- Instant bank verification's institution credentials are explicitly for the **test** environment, with country/region examples at raw lines 178-204. The browser debug UI is enabled by default and intended for support/engineering, not end users; it can expose legal-entity JSON, task status, settings and other sensitive information. Share its report only with the team or Adyen Support to the minimum needed. See raw lines 206-229.

## Detail locators

- Theme setup steps, asset constraints and external-link suggestions: raw lines 39-96.
- Dated supported-locale table: raw lines 124-156.
- Complete onboarding-link settings/defaults table: raw lines 158-176.
- Country/region test-bank account table: raw lines 178-204.
- Debug access shortcut and report contents: raw lines 206-229.

## Related

- [[adyen-issuing]] — Issuing concept and source route.
- [[source-adyen-docs-issuing-manage-legal-entities]] — legal-entity management and hosted onboarding context.

## Raw Sources

- [[raw/adyen/docs/issuing/onboard-users/customize-hosted-onboarding/2026-09-15|Adyen Customize and test hosted onboarding, captured 2026-09-15]]
