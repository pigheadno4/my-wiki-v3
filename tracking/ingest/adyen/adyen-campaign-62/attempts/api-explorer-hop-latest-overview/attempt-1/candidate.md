---
title: "Adyen Hosted onboarding API v6 overview (Classic Platforms)"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Hop/latest/overview"
raw_files:
  - "adyen/api-explorer/Hop/latest/overview/2026-09-15.md"
tags: [adyen, classic-platforms, hosted-onboarding, api-explorer, hop]
---

## Overview

This 2026-09-15 API Explorer snapshot identifies the **Hosted onboarding API v6** as a Classic Platforms integration surface. A platform can request links to Adyen-hosted onboarding or PCI questionnaire pages and provide them to its account holders. The page directs new implementations to a separate new integration guide. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- The listed test base URL is `https://cal-test.adyen.com/cal/services/Hop/v6`; versioning uses a `vXX` endpoint suffix. The two listed operations are `POST /getOnboardingUrl` and `POST /getPciQuestionnaireUrl`. The overview supplies no operation request or response schemas, required account-holder identifiers, link validity, session lifecycle, error conditions, or timing limits; consult each operation's own reference for those details.
- For authentication, the page instructs use of an `X-API-Key` header with an Adyen-provided API key, or alternatively username/password Basic authentication. Going live requires new web-service-user credentials for live endpoints. The page does not list the live base URL or establish live access.
- Generating or offering a hosted-page link is distinct from the account holder completing onboarding, passing verification or a PCI questionnaire, and any payment, payout, settlement, or bank receipt. This overview documents endpoints, not the result of a specific call or account-holder action.

## Detail locators

- Classic/new-integration scope and hosted-link purpose: [[raw/adyen/api-explorer/Hop/latest/overview/2026-09-15#L5|raw lines 5–9]].
- Authentication and live credentials: [[raw/adyen/api-explorer/Hop/latest/overview/2026-09-15#L11|raw lines 11–27]].
- Versioned test server and endpoint list: [[raw/adyen/api-explorer/Hop/latest/overview/2026-09-15#L29|raw lines 29–46]].

## Related

- [[adyen-classic-platforms]] — Classic account-holder model and hosted onboarding route.
- [[adyen]] — provider overview.

## Related raw API references

- `POST /getOnboardingUrl` and `POST /getPciQuestionnaireUrl` are named operations in this overview; their separate references have not been read for this source.

## Raw Sources

- [[raw/adyen/api-explorer/Hop/latest/overview/2026-09-15|Adyen Hosted onboarding API v6 overview capture, 2026-09-15]]
