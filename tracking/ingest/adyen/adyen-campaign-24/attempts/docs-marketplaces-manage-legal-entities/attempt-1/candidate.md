---
title: "Adyen Marketplaces: manage legal entities"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/manage-legal-entities"
raw_files:
  - "adyen/docs/marketplaces/manage-legal-entities/2026-09-15.md"
tags: [adyen, marketplaces, platforms, legal-entities, onboarding, verification]
---

## Overview

This 2024-modified page, captured 2026-09-15, describes creating, viewing, and updating individual or organization legal-entity resources for users on an Adyen Balance Platform. The resource holds identity and tax details plus associations with other entities; Adyen uses its details for verification. It is a Marketplaces guide within [[adyen-platforms]], issued by [[adyen]]. Its operations are part of onboarding and verification, not evidence that a particular user passed verification or obtained a capability.

## Key takeaways

- Use Legal Entity Management API v3 to manage the resources. The stated prerequisite is a Legal Entity Management web-service user with **Manage LegalEntities via API** and **Balance Platform BCL Legal Entity role**. Minimum creation information depends on the user's location and entity type. Create an individual or organization with POST `/legalEntities`; retain the generated legal-entity ID for account-holder creation, viewing, updating, and hosted onboarding. See raw lines 19–43 and 373–400.
- View a legal entity through Customer Area, the API, or hosted onboarding. API retrieval uses GET `/legalEntities/{id}`; each associated entity needs its own GET by the returned `legalEntityId`. For individual and sole-proprietorship records, Customer Area redacts listed personally identifiable information unless the user has the **View account holders PII data** role. See raw lines 403–436 and 593–626.
- Update changed account-holder details through Customer Area/hosted onboarding or PATCH `/legalEntities/{id}`. The Customer Area path requires **Manage account holders and legal entities**. API PATCH updates only supplied parameters. Hosted onboarding requires an onboarding link and redirects the user to its returned URL. Updating legal-entity details reruns verification checks. See raw lines 628–651 and 972–981.
- A main legal entity's type can be changed through hosted onboarding or, for API-only onboarding, PATCH plus additional required information. All verification checks rerun. Only the main entity's type can change; an incorrect associated entity type requires a new legal entity. The API-only direct type change supports individual↔organization; organization→sole proprietorship uses a subsequent association step. The page lists retained resources and migrated name/country fields, and says to PATCH again for remaining details such as the complete address. See raw lines 983–1013, 1029–1036, and 1227–1247.

## Detail locators

- Creation request/response examples in several languages: raw lines 41–400. The US organization data is illustrative.
- Viewing routes, redaction, associated-entity lookup, and hosted onboarding: raw lines 403–626.
- Updating routes and request examples: raw lines 628–981.
- Entity-type changes, retained/migrated fields, API examples, and follow-up PATCH: raw lines 983–1247.

## Related

- [[adyen]] — provider profile.
- [[adyen-platforms]] — modern Adyen for Platforms and Marketplace route.
- [[source-adyen-docs-platforms-manage-legal-entities]] — separate Platforms URL for a closely related LEM v3 guide; keep source provenance distinct.
- [[adyen-classic-platforms]] — legacy Classic Platforms resource model, distinct from this Balance Platform legal entity.

## Raw Sources

- [[raw/adyen/docs/marketplaces/manage-legal-entities/2026-09-15|Manage legal entities — pinned 2026-09-15 raw snapshot]]
