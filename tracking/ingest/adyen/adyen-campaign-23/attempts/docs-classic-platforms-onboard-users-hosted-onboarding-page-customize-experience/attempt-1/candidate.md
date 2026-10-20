---
title: "Adyen Classic Platforms: Customize Hosted Onboarding Page"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/onboard-users/hosted-onboarding-page/customize-experience"
raw_files:
  - "adyen/docs/classic-platforms/onboard-users/hosted-onboarding-page/customize-experience/2026-09-15.md"
tags: [adyen, classic-platforms, hosted-onboarding, verification, customization]
---

## Overview

This 2022-modified, 2026-09-15-captured **Classic Adyen for Platforms** guide describes optional `/getOnboardingUrl` request controls for the Hosted Onboarding Page (HOP): which verification information to collect, which summary pages to show, language, editing previously verified data, platform display name and post-session return URL. It is a Classic account-holder verification UI route, separate from newer Platforms hosted onboarding. The companion [[source-adyen-docs-classic-platforms-onboard-users-hosted-onboarding-page|HOP guide]] owns enablement, one-time URL timing, session recovery and verification-result webhooks. See [[adyen]] and [[adyen-classic-platforms]].

## Key takeaways

- By default HOP collects information for every verification check that applies to the account holder's legal-entity type. Set `collectInformation` on `/getOnboardingUrl` to collect selected bank, business, individual, PCI-questionnaire or shareholder information, singly or in combination. Set `showPages` to show or hide the welcome and listed summary pages; the **welcome page is hidden by default**.
- HOP normally uses the browser language, falling back to `en-US` if unsupported. The account holder can select a language; `shopperLocale` can render the page in a specified supported language. If that requested locale is unsupported, HOP falls back to browser language, then to `en-US` if the browser language is also unsupported. The supported locale table is a dated snapshot.
- HOP is described as a one-time onboarding tool, so account holders cannot edit already verified data by default. Supplying `editMode` changes that behavior to allow editing after checks have passed; this alters what the holder can change and does **not** by itself establish that updated information is accepted or verified.
- `platformName` changes the welcome-page name, relevant only when that page is displayed. The page says a `returnURL` object overrides the platform's default return URL after onboarding completion or session timeout, with a **500-character maximum**. The companion HOP page calls the optional request parameter `returnUrl` (companion raw line 69), while this page says `returnURL` (pinned raw line 113); verify the exact API contract before sending it. A return redirect is not a verification decision.

## Detail locators

- Pinned raw lines 15–34: Classic scope and customizable `/getOnboardingUrl` capabilities.
- Pinned raw lines 36–48: default legal-entity checks and `collectInformation` categories; lines 50–62: `showPages` categories and hidden welcome default.
- Pinned raw lines 64–96: browser/`shopperLocale` fallback and supported locale table; lines 98–102: verified-data editing default and `editMode`.
- Pinned raw lines 104–114: platform display name, return redirect and URL length; companion HOP raw line 69 uses different return-parameter casing.

## Related

- [[source-adyen-docs-classic-platforms-onboard-users-hosted-onboarding-page]] — HOP enablement, redirect/session and webhook guide.
- [[adyen-classic-platforms]] — Classic account-holder/onboarding context.
- [[adyen-platforms]] — newer model with separate hosted-onboarding configuration.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/onboard-users/hosted-onboarding-page/customize-experience/2026-09-15|Classic HOP customization guide, captured 2026-09-15]]
