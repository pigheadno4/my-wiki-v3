---
title: "Adyen Marketplaces: Customize and test hosted onboarding"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/onboard-users/customize-hosted-onboarding"
raw_files:
  - "adyen/docs/marketplaces/onboard-users/customize-hosted-onboarding/2026-09-15.md"
tags: [adyen, marketplaces, platforms, hosted-onboarding, verification]
---

## Overview

This 2024-modified, 2026-09-15-captured **Marketplaces / Adyen for Platforms or Issuing** guide covers hosted-onboarding theme creation, page language and link settings, test instant-bank-verification data, and an internal debug UI. These controls shape the onboarding experience; creating a theme or link, viewing a task status, or running a test flow does not establish a user’s completed verification or enabled capability. [[adyen-platforms]]

## Theme and link setup

- The stated integration requirement is Adyen for Platforms or Adyen Issuing. **API-initiated** hosted onboarding needs Legal Entity Management API credentials. Creating or editing themes in Customer Area requires `Manage hosted onboarding themes` and either `Balance platform admin role` or `Balance platform base role`. See [[raw/adyen/docs/marketplaces/onboard-users/customize-hosted-onboarding/2026-09-15|raw lines 29–37]].
- A Customer Area company-account theme can set logo, header, browser title/favicon, background and external-link branding. The guide recommends a return `redirectUrl`, contrast/accessibility and branded support/privacy/FAQ links. Save and copy the **theme ID** to pass when POSTing `/legalEntities/{id}/onboardingLinks`; a saved theme alone does not create that link. See [[raw/adyen/docs/marketplaces/onboard-users/customize-hosted-onboarding/2026-09-15|raw lines 39–96]]. Browser-title and asset limits are at raw lines 72–86.
- Themes can be viewed in Customer Area or with LEM `GET /themes` / `GET /themes/{id}`; this page describes updating themes in Customer Area. See [[raw/adyen/docs/marketplaces/onboard-users/customize-hosted-onboarding/2026-09-15|raw lines 98–122]].

## Locale, settings and test limits

- Browser language is the default; unsupported browser language renders **en-US**. The onboarding-link request can set a locale, and an unsupported locale falls back to another supported value for its language (the page gives `en-GB` → `en-US`). The snapshot’s supported locale list is at [[raw/adyen/docs/marketplaces/onboard-users/customize-hosted-onboarding/2026-09-15|raw lines 124–156]].
- The onboarding-link `settings` object controls **UI actions**: selectable countries (default empty list allows supported hosted-onboarding countries), payout-bank format/cross-border choice, legal-entity-type and prefilled-country edits, `enforceLegalAge`, introduction screens, `instantBankVerification`, debug UI and transfer-instrument count. Exact defaults and semantics are at [[raw/adyen/docs/marketplaces/onboard-users/customize-hosted-onboarding/2026-09-15|raw lines 158–176]]. Enabling a UI choice does not override regional, verification or payout eligibility.
- The instant-bank-verification section supplies **TEST-environment** institution/account credentials by country; treat them only as test fixtures, not live bank credentials or proof of successful verification. See [[raw/adyen/docs/marketplaces/onboard-users/customize-hosted-onboarding/2026-09-15|raw lines 178–204]].

## Debug-data boundary

- `allowDebugUi` is **true by default** and the debug UI is intended for support/engineering, not marketplace users. The page gives a keyboard shortcut and copy action for support requests. Its report contains sensitive metadata, settings/experiments, task statuses, legal-entity JSON, associations and account-holder capabilities; share only the minimum required with the team or Adyen Support for troubleshooting. See [[raw/adyen/docs/marketplaces/onboard-users/customize-hosted-onboarding/2026-09-15|raw lines 206–227]].

## Related

- [[adyen-platforms]] — modern Platforms onboarding context.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/onboard-users/customize-hosted-onboarding/2026-09-15|Customize and test hosted onboarding (captured 2026-09-15)]]
