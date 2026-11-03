---
title: "Adyen Legal Entity Management API v4: create a hosted onboarding link"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities/(id)/onboardingLinks"
raw_files:
  - "adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/onboardingLinks/2026-11-03.md"
tags: [adyen, legal-entity-management, onboarding, api-reference]
---

## Overview

This 2026-11-03 capture of `POST /legalEntities/{id}/onboardingLinks` is a Legal Entity Management API v4 reference for obtaining an Adyen-hosted onboarding-page link for a specified legal entity. The caller redirects its user to the returned URL. The page lists the TEST server `https://kyc-test.adyen.com/lem/v4`; its `latest` URL is a capture route, not evidence of future version currency. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- Path `id` is the required legal-entity identifier. The request-body table marks `locale`, `redirectUrl`, `settings` and `themeId` optional; it does not independently state whole-body requiredness. `themeId` identifies a hosted-onboarding theme. Optional nested settings govern country choice, payout-account format, debug UI, legal-entity type/country editing, legal age, introduction screens, instant bank verification, PCI signing prompts and a transfer-instrument count limit. Consult the table for individual defaults and conditions.
- `locale` falls back to browser language if omitted or unsupported, then `en-US` if that is unsupported. `acceptedCountries` defaults to an empty array, allowing all countries/regions supported by hosted onboarding; its restriction applies when `editPrefilledCountry` is allowed. `redirectUrl` is the post-completion destination.
- A `200` response lists an optional `url` field for redirecting the user. The URL expires after four minutes, is single-use and can be clicked only once; create a new link after expiry. Returning a link does not establish that onboarding was completed, identity verified, a capability approved, PCI obligations satisfied, or any payment or payout executed.
- Captured limits are 700 requests per five seconds in live, 200 per five seconds in test, and five failed requests per ten seconds. The reference lists 400, 401 (authentication required), 403 (insufficient permissions), 422 (validation) and 500 responses. Its generic error body includes an optional `pspReference` description, but this endpoint is a link request, not evidence of a payment. The capture does not specify idempotency, deletion/reversal, asynchronous approval or propagation semantics.

## Detail locators

- `## Servers`, `## Parameters` → test v4 base, required path ID, optional request fields, nested settings, defaults and conditions.
- `## Request examples` → sample theme, redirect and locale; example values are illustrative.
- `## Responses` → link lifetime and reuse restrictions, errors and limits; `## Response examples` → illustrative URL only.

## Related

- [[adyen-platforms]] — Platforms and marketplace onboarding context.
- [[source-adyen-api-explorer-legalentity-latest-overview]] — separate API v4 overview and API-key/live-server context.
- [[source-adyen-api-explorer-legalentity-latest-get-themes]] — theme listing reference.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/onboardingLinks/2026-11-03|2026-11-03 captured endpoint reference]]