---
title: "Capital integration checklist | Adyen"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/integration-checklist"
raw_files:
  - "adyen/docs/capital/integration-checklist/2026-09-15.md"
tags: [adyen, capital, platforms, integration, checklist]
---

## Overview

This [[adyen]] Capital checklist, last modified 2022-10-26 and captured 2026-09-15, outlines setup from an existing Adyen for Platforms integration toward a Capital launch. It is a **preparation and testing sequence**, not evidence that a platform or user is currently eligible, that a grant offer was accepted, or that financing was disbursed. See [[adyen-capital]].

## Key takeaways

- The page requires an Adyen for Platforms integration and a user in a supported country/region, plus contacting Adyen about Capital and designing the implementation with an Adyen contact. Its `#supported-countriesregions` requirement link has no matching section in this captured page; use the separate current availability authority before selecting a region. [Raw: lines 19–30]
- The six listed stages are account-structure review, completion of the platform or marketplace integration checklist, API-key testing, webhook setup, Capital-feature implementation and go-live preparation. The account-structure list distinguishes company and merchant accounts, balance platform, account holder, balance account, legal entity, verified transfer instrument, grant reference generated on request, and disbursement reference generated when funds are disbursed. These IDs identify separate stages, not equivalent funding proof. [Raw: lines 32–61]
- The API table maps Capital API grant-offer/request/disbursement operations to a balance-platform credential and Capital Configuration/Grant Initiation roles; Configuration API resource/capability tasks to a balance-platform credential with BCL role; and Legal Entity Management API legal-entity tasks to a company-scope credential. The page then calls for server webhook endpoints, acknowledgements, Customer Area configuration and HMAC security. Exact role names, credentials and API routes are in the pinned table and linked guides. [Raw: lines 63–84]
- The checklist offers two implementation paths. For UI components, create an authentication session **on the server**, install and initialize the front-end library, refresh the session token, mount and optionally customize components. For an API-only UI, show personalized offers, present Adyen Terms of Service for digital signature and request the selected grant on the user's behalf. Showing an offer or signing a UI screen is not itself a grant disbursement. [Raw: lines 86–126]
- Test setup does **not** automatically move to live. Go-live preparation calls for recreating the setup in the live account, live credentials/endpoints and end-to-end tests of credentials, grant account, offers for users with the required capability, grant payout to the corresponding balance account or transfer instrument, and webhook receipt. These are checklist tasks, not evidence they were performed. The dated checklist does not establish current regional availability, eligibility, legal terms or a particular grant's final state. [Raw: lines 128–149]

## Detail locators

- Captured provenance and prerequisite/region link: raw lines 1–30.
- Six-stage sequence and account/resource/reference identities: raw lines 32–61.
- API credentials/roles and webhook setup: raw lines 63–84.
- Component server session and front-end path versus API-only offer/terms/request path: raw lines 86–126.
- Test-to-live separation and required live checks: raw lines 128–149.

## Related

- [[adyen-capital]] — Capital product context and evidence boundary
- [[adyen-platforms]] — underlying platform integration
- [Capital get started](https://docs.adyen.com/capital/get-started) — related integration design route
- [Capital user capabilities](https://docs.adyen.com/capital/manage-user-capabilities) — linked capability guide
- [Capital Terms of Service](https://docs.adyen.com/capital/terms-of-service) — linked terms route

## Raw Sources

- [[raw/adyen/docs/capital/integration-checklist/2026-09-15|Adyen Capital integration checklist — collected 2026-09-15]]
