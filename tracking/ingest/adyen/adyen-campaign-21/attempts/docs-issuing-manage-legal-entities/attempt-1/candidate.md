---
title: "Adyen Issuing: Manage legal entities"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/manage-legal-entities"
raw_files:
  - "adyen/docs/issuing/manage-legal-entities/2026-09-15.md"
tags: [adyen, issuing, legal-entities, onboarding, verification]
---

## Overview

This captured Issuing guide explains how a platform creates, views, and updates users' legal entity resources with the Legal Entity Management API, Customer Area, or Hosted onboarding. A legal entity describes an individual or organization on the Balance Platform, including user details and associations with other entities; Adyen uses its information for verification. These operations sit within onboarding and verification, not card issuance or payment execution. [[adyen]] [[adyen-issuing]]

## Key takeaways

- Create an individual or organization with `POST /legalEntities`; the minimum information varies by location and entity type. Save the generated legal entity ID for later account-holder creation, viewing, updates, or Hosted onboarding. The US organization request and test-environment SDK examples are examples, not a universal KYC checklist or live eligibility proof.
- View the main legal entity with `GET /legalEntities/{id}` or via the Customer Area/Hosted onboarding. To retrieve an associated entity's details by API, use the `legalEntityId` in each `entityAssociations` item for another GET. In the Customer Area, individual or sole-proprietorship PII is redacted unless the user has the **View account holders PII data** role.
- Update changed account-holder details with `PATCH /legalEntities/{id}`; the guide says only supplied body parameters are updated. The Customer Area update route requires the **Manage account holders and legal entities** role and opens Hosted onboarding. For Hosted onboarding links, the main legal entity ID is used, or the owner's individual legal entity ID for a sole proprietorship; redirect the user to Adyen's returned URL. Updating legal entity details reruns verification checks.
- A type change reruns all verification checks and is limited to the **main** legal entity; an incorrect associated legal entity type calls for a new legal entity. API-only onboarding directly changes only individual ↔ organization, followed by additional required information. Hosted onboarding lets a user select a different type and provide additional information. The guide lists retained resources and specific migrated name/country fields; it says to PATCH again for additional information such as a complete address.

## Detail locators

- Raw lines 19–25: resource identity, associations, verification purpose, Legal Entity Management API, and onboarding context.
- Raw lines 27–35 and 365–392: creation prerequisites, example request, generated ID, and downstream uses.
- Raw lines 395–422 and 424–611: Customer Area and API viewing, PII role, associated entity retrieval.
- Raw lines 612–643 and 964–973: Customer Area/API/Hosted onboarding update paths, role, patch behavior, sole-proprietorship ID, and verification rerun.
- Raw lines 975–1028 and 1219–1239: type-change boundaries, retained/migrated information, direct API transition limits, additional PATCH, and sole-proprietorship route.

## Related

- [[adyen-issuing]] — Issuing concept and source route.
- [[source-adyen-docs-issuing]] — Issuing overview.
- [[source-adyen-docs-issuing-get-started]] — program setup context.

## Raw Sources

- [[raw/adyen/docs/issuing/manage-legal-entities/2026-09-15|Manage legal entities — captured 2026-09-15]]
