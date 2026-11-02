---
title: "Adyen Classic Platforms Hosted Onboarding Page"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/onboard-users/hosted-onboarding-page"
raw_files:
  - "adyen/docs/classic-platforms/onboard-users/hosted-onboarding-page/2026-09-15.md"
tags: [adyen, classic-platforms, onboarding, account-holders, verification]
---

## Overview

This 2021-modified Classic Adyen for Platforms guide, captured 2026-09-15, describes sending an existing account holder to Adyen's Hosted Onboarding Page (HOP) to supply verification information. It calls HOP the recommended lower-effort route and directs new implementations to a separate newer integration guide. This is a Classic account-holder workflow, not a current balance-platform API flow. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- Hosted onboarding must be enabled for the platform through Adyen Support, which also receives a default return URL. The platform chooses upfront or staggered collection: the guide says upfront aims to collect data for all payment-processing and payout tiers once, while staggered requires another HOP URL when processed funds exceed the current tier (raw lines 47–57). Neither choice proves verification approval or payout execution.
- Create a Classic account holder and retain its `accountHolderCode`; when the holder chooses to onboard, POST to `/getOnboardingUrl` and redirect them to the returned one-time URL (raw lines 31–41, 59–69, 87–105). The guide says the returned URL must be used once within 15 seconds. A successful redirect starts a 30-minute session; if the redirect is late or the holder reloads after the session starts, the holder receives HTTP 401 and the platform must request a new URL (raw lines 87–112).
- `returnUrl`, `shopperLocale` and `platformName` are optional request parameters; account-holder updates arrive through `ACCOUNT_HOLDER_UPDATED`, and subsequent verification results through `ACCOUNT_HOLDER_VERIFICATION` webhooks (raw lines 67–70, 113–122). Returning to the platform site or receiving the URL response is not a verification result. On expiry or incomplete onboarding, generate a new URL; entered information is saved per section so the next session resumes at remaining sections (raw lines 114–120).
- The prose/bullet calls the returned field `redirectURL`, while the JSON example spells it `redirectUrl`. Preserve that mismatch rather than assuming both spellings are valid response keys; confirm against the actual API contract before implementing the parser (raw lines 87–105). The sample `pspReference` is recommended for troubleshooting, not evidence of completion (raw lines 89–100).
- Separately, this HOP guide calls the optional **request** parameter `returnUrl` in prose and JSON (raw lines 69, 81), while [[source-adyen-docs-classic-platforms-onboard-users-hosted-onboarding-page-customize-experience]] calls it a `returnURL` object (companion raw line 113). Preserve that request-field casing mismatch independently of the `redirectURL`/`redirectUrl` **response** mismatch above; verify the request contract before sending it.
- Customer Area access on behalf of a holder is a separate operational route that requires the **Manage HOP settings** role (raw lines 124–132). The page says a newly created holder can immediately process payments, but that statement alone does not establish completed verification or payouts (raw lines 59–63).

## Detail locators

- Classic-only scope, recommended HOP and customizable language, appearance and notification options: raw lines 19–29. Four-step flow and 30-minute session: raw lines 31–41.
- Enablement, default return URL, upfront/staggered collection: raw lines 47–57. Holder creation and optional URL parameters: raw lines 59–70. Test request/response example and response-field mismatch: raw lines 71–101.
- 15-second one-time URL, 401 cases, renewed URL, progress and verification webhooks: raw lines 103–122. Role-gated Customer Area access: raw lines 124–132.

## Related

- [[adyen-classic-platforms]] — Classic account-holder and account model.
- [[source-adyen-docs-classic-platforms-onboard-users-custom-onboarding]] — platform-built alternative.
- [[source-adyen-docs-classic-platforms-verification-process]] — verification and payout gates.
- [[adyen-platforms]] — separate newer platform model.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/onboard-users/hosted-onboarding-page/2026-09-15|Classic Hosted Onboarding Page, captured 2026-09-15]]
