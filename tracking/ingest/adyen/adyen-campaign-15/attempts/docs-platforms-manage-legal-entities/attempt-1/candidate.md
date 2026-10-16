---
title: "Adyen for Platforms: Manage legal entities"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/manage-legal-entities"
raw_files:
  - "adyen/docs/platforms/manage-legal-entities/2026-09-15.md"
tags: [adyen, platforms, legal-entities, onboarding, verification]
---

## Overview

This Adyen for Platforms guide explains creation, viewing and updating of a user's legal entity resource with Legal Entity Management API v3, Customer Area or Hosted onboarding. A legal entity describes an individual or organization on a Balance Platform, including identifying information and associations used in Adyen verification. It is distinct from the linked account holder and does not itself define a balance account, legal seller, merchant of record or funds owner. The page is a 2024-modified, 2026-09-15-captured guide; examples and API responses do not establish current compliance or successful verification for any user. See [[adyen]] and [[adyen-platforms]] for provider and platform scope.

## Key takeaways

- The guide requires the Adyen for Platforms integration type. Legal Entity Management API operations require a Legal Entity Management web service user with Manage LegalEntities via API and Balance Platform BCL Legal Entity roles. Required creation data depends on location and entity type; the US organization request is an example, not a universal schema. POST `/legalEntities` returns a generated legal entity ID used later to create an account holder, view/update that entity, or start Hosted onboarding. Creating the resource is only a step toward verification of the linked account holder.
- View the main entity from the account holder in Customer Area, GET `/legalEntities/{id}`, or a Hosted onboarding link. Associated entities have separate IDs and API retrieval. The Customer Area shows transfer-instrument bank-account information under the main entity view, but this does not make the legal entity a balance-account ledger or establish bank ownership or movement. For an individual or sole proprietorship, listed PII is redacted unless the user has the View account holders PII data role.
- Changes to account-holder details, such as address or ownership, call for legal-entity updates. Customer Area editing requires Manage account holders and legal entities and opens Hosted onboarding; API PATCH `/legalEntities/{id}` updates only fields supplied in the body. Hosted onboarding details updates rerun verification checks. A submitted change or updated API response is not a verified state.
- Entity type can change only for the main legal entity; an incorrectly typed associated entity requires a new legal entity. A main-entity type change reruns all verification checks. The page lists retained legal entity ID, transfer instruments, bank-statement details, proof of industry, processed amounts and business lines; between individual and organization it migrates country and name to corresponding fields. API-only direct type changes are limited to individual↔organization, and additional required information may need a subsequent PATCH. The organization-to-sole-proprietorship API route first changes to individual, then associates a sole proprietorship.
- Sample calls use `kyc-test.adyen.com/lem/v3` and language-specific SDK versions. Follow the verified raw locators for exact request bodies and current API references. This snapshot does not prove a live account's eligibility, legal classification, completed verification, compliance sign-off or any payment/payout event.

## Detail locators

- Resource meaning, association/verification context and Legal Entity Management API: raw lines 17–25. Integration type and API credential roles: `## Requirements`, lines 27–33. Location/type-dependent creation data and POST route: lines 35–43; test examples and generated ID uses: lines 45–401.
- Customer Area, API and Hosted onboarding view routes, associated-entity lookup and PII redaction/role: `## View legal entity details`, lines 403–626.
- Customer Area update role and API PATCH behavior: `## Update a legal entity`, lines 628–651. Hosted update and verification rerun: lines 972–981. Main-only type change, associated-entity replacement, retained/migrated fields and API-only type restriction: lines 983–1036. Additional PATCH after migration and sole-proprietorship sequence: lines 1227–1247.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — current platform integration and separate account-resource routes.
- [[adyen-account-structure]] — Adyen company/merchant account hierarchy, distinct from Balance Platform legal entity and account-holder resources.

## Related raw API references

- The raw page links to Legal Entity Management API operations, region-specific KYC information, verification overview, account-holder creation and hosted/API-only onboarding. Those destinations own detailed requirements and statuses until independently read.

## Raw Sources

- [[raw/adyen/docs/platforms/manage-legal-entities/2026-09-15|Adyen Docs: Manage legal entities (2026-09-15 snapshot; page last modified 2024-01-04)]]
