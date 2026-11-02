---
title: "Adyen Classic HOP v6 getOnboardingUrl"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Hop/latest/post/getOnboardingUrl"
raw_files:
  - "adyen/api-explorer/Hop/latest/post/getOnboardingUrl/2026-09-15.md"
tags: [adyen, classic-platforms, hosted-onboarding, api-explorer]
---

## Overview

Captured Classic Hosted Onboarding Page (HOP) `POST /getOnboardingUrl` contract, served under the listed **Hop/v6** test base URL. A platform requests a link for an existing Classic account holder to provide onboarding information on an Adyen-hosted page. This is a URL issuance step, separate from the holder's session, verification outcome, payment processing or payout. See [[adyen]] and [[adyen-classic-platforms]].

> [!warning] Contradiction
> The September 2026 API Explorer contract [[source-adyen-api-explorer-hop-latest-post-getonboardingurl]] says its one-time `redirectUrl` must be used within **30 seconds** (raw line 66); the separately captured Classic guide [[source-adyen-docs-classic-platforms-onboard-users-hosted-onboarding-page]] says **15 seconds** (guide raw lines 87–110). Keep these link-use windows source-qualified. The guide's subsequent 30-minute session is a different limit; these snapshots do not resolve the operational link window.

## Key takeaways

- The request body requires `accountHolderCode`, the code supplied when the platform created the Classic account holder. `collectInformation` is optional; by default HOP collects information for all KYC checks applicable to the holder's legal entity type, and its six optional check flags default to true (the PCI questionnaire applies only to partner platforms). `showPages` is optional; its page flags mostly default true, while `checksOverviewPage` and `welcomePage` default false. These controls select collection/presentation, not verification approval.
- Optional `editMode` permits editing checks after they have all passed. `returnUrl` redirects on completion or session timeout, is limited to 500 characters, and otherwise falls back to the platform default. `shopperLocale` falls back to browser language and then `en-US` if unsupported. `mobileOAuthCallbackUrl` is for bank OAuth through Trustly/PayMyBank.
- The 200 response table marks `invalidFields`, `pspReference`, `redirectUrl` and `resultCode` optional. `pspReference` identifies the request; it does not establish an onboarding or financial result. The table says a returned `redirectUrl` must be used once within **30 seconds**. The response example shows a successful test URL, but does not make every optional field guaranteed.
- **Conflicting retained evidence:** the separately captured [[source-adyen-docs-classic-platforms-onboard-users-hosted-onboarding-page]] says the one-time redirect URL must be used within **15 seconds** and that the hosted session then lasts 30 minutes (companion raw lines 87–110). This API Explorer contract says **30 seconds** for use of `redirectUrl` (this raw line 66) and does not state session duration. Preserve this discrepancy; do not treat either number as a universal safe window.
- The page lists 400 parsing, 401 authentication, 403 permission, 422 validation and 500 server error responses. It does not specify an authentication mechanism or required role. Its generic error-body `pspReference` description says “payment,” which does not change this operation's HOP URL purpose.

## Detail locators

- Purpose and Hop/v6 test server: raw lines 5–10.
- Required account-holder identity, KYC collection flags/defaults, edit, OAuth callback, return URL, locale and page visibility: raw lines 12–39.
- Request example: raw lines 41–49.
- 200 response, optional fields, request reference and one-time 30-second redirect URL: raw lines 50–67; example at 134–146.
- Error statuses and optional error-body fields: raw lines 70–132.

## Related

- [[adyen-classic-platforms]] — Classic account-holder and hosted-onboarding route.
- [[source-adyen-docs-classic-platforms-onboard-users-hosted-onboarding-page]] — separate HOP guide with conflicting 15-second URL instruction and 30-minute session guidance.
- [[adyen]] — provider index.

## Raw Sources

- [[raw/adyen/api-explorer/Hop/latest/post/getOnboardingUrl/2026-09-15|Hop v6 getOnboardingUrl API Explorer page, captured 2026-09-15]]
