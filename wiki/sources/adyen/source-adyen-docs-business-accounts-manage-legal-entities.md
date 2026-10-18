---
title: "Manage legal entities | Adyen Business accounts"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/manage-legal-entities"
raw_files:
  - "adyen/docs/business-accounts/manage-legal-entities/2026-09-15.md"
tags: [adyen, business-accounts, legal-entities, onboarding, verification]
---

## Overview

This 2024-modified, 2026-09-15-captured [[adyen]] Business accounts guide describes Legal Entity Management API v3 and Customer Area/hosted-onboarding routes to create, view and update a user's legal-entity resource. A legal entity represents an individual or organization and its associations for Adyen verification; its generated `LE...` ID is used in later account-holder creation and entity reads/updates. See [[adyen-business-accounts]] for the product route. Creating or changing this resource is not proof of verified status, capability enablement, Business account opening, legal ownership or a live transfer.

## Key takeaways

- A legal entity contains identifying, address and tax information for an individual or organization, plus associations such as an organization's signatory. Adyen uses it for verification checks. This guide's operations sit inside a broader onboarding and verification process; minimum create information depends on the user's **location and entity type**. The US private-company request and TEST-host examples are illustrations, not a universal field checklist or live-resource evidence. [Raw: lines 19–35, 41–61]
- The create route is Legal Entity Management API `POST /legalEntities` with `individual` or `organization` details. Its response contains a generated legal-entity ID to save for **creating an account holder**, viewing the entity and updating it. The legal entity, account holder, balance account and bank/payment instrument are distinct resources; creation of the first does not instantiate the others or complete verification. [Raw: lines 27–35, 365–392]
- For viewing, Customer Area, the API and hosted onboarding are listed. Customer Area shows the account holder's **main legal entity**, with transfer-instrument bank-account information and organization associations. Individual/sole-proprietorship PII is redacted unless the viewer has `View account holders PII data`. API `GET /legalEntities/{id}` returns the requested entity's `individual`/`organization` details; each associated entity requires its own GET by the returned `legalEntityId`. Do not confuse an association ID with the main legal entity or infer unredacted UI access from API examples. [Raw: lines 394–427, 572–607]
- When details change, the guide says to update the legal entity. Customer Area update requires `Manage account holders and legal entities` and leads through hosted onboarding. API `PATCH /legalEntities/{id}` updates only parameters passed in the body; verification checks run again after detail updates. An API response or submitted change does not imply renewed verification has passed. [Raw: lines 609–634, 955]
- **Entity-type change is narrower than ordinary detail updates:** only the **main** legal entity's type can change directly, and direct switches are individual ↔ organization. For an associated entity with the wrong type, create a new entity. All verification checks rerun after a type change. The page lists retained LE ID, transfer instruments, bank statement details, proof of industry, processed amounts and business lines; only specified name/country fields migrate between individual and organization, so a further PATCH may be needed for full details. Organization → sole proprietorship uses organization → individual, then an association PATCH. These are captured procedure rules, not a guarantee of continuing eligibility. [Raw: lines 957–993, 1184–1204]

## Detail locators

- Legal-entity identity, LEM API version, onboarding/verification context and location/type-dependent create input: raw lines 19–35.
- TEST code samples and generated ID use for account holder/view/update: raw lines 37–392.
- Customer Area visibility, PII role, API GET and associated-entity reads: raw lines 394–607.
- Customer Area update role, hosted flow, PATCH field scope and verification rerun: raw lines 609–634, 955.
- Main-versus-associated type-change limits, retained/migrated data, direct transitions and follow-up PATCH: raw lines 957–1204.

## Related

- [[adyen-business-accounts]] — Business accounts product route
- [[adyen-platforms]] — broader platform context
- [Verification overview](https://docs.adyen.com/business-accounts/verification-overview) — linked verification process
- [Onboard users](https://docs.adyen.com/business-accounts/onboard-users) — linked broader onboarding
- [Manage account holders](https://docs.adyen.com/business-accounts/manage-account-holders) — linked account-holder creation/capabilities
- [Legal Entity Management API v3](https://docs.adyen.com/api-explorer/legalentity/3/overview) — linked API reference

## Raw Sources

- [[raw/adyen/docs/business-accounts/manage-legal-entities/2026-09-15|Adyen Business accounts manage legal entities — collected 2026-09-15]]
