---
title: "Adyen Issuing: Onboard and verify users"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/onboard-users"
raw_files:
  - "adyen/docs/issuing/onboard-users/2026-09-15.md"
tags: [adyen, issuing, onboarding, verification, source-of-funds]
---

## Overview

Adyen's Issuing onboarding guide contrasts hosted onboarding, where users provide information through an Adyen-hosted page, with API-only onboarding, where the platform builds the UI and submits user data. The legal-entity type and operating country determine the information to collect; Adyen says verification starts automatically after it receives that information. This is a 2026-09-15 capture of a page marked last modified 2023-07-07. It describes routes and requirements for [[adyen-issuing]], not completed verification or current eligibility.

## Key takeaways

- With hosted onboarding, the platform makes Legal Entity Management API and Configuration API calls to create and customize resources for the Adyen-hosted page. Adyen presents it as the recommended, lower-integration-effort collection route. The page can be themed and localized, and includes Terms of Service acceptance if users need it (raw lines 30–42). The hosted operating-location list at raw lines 44–86 is a dated documentation snapshot, not a universal live-availability promise.
- Instant hosted bank-account verification is available only for the listed location and legal-entity-type combinations; qualifying users log into online banking and confirm account details, instead of supplying a bank statement (raw lines 88–119). The hosted ID-document autofill, guided organization decision-maker roles, and decision-maker invitation features are each limited to onboarding v3 or v4 (raw lines 127–158); ID autofill supports only documents with Latin characters (raw line 133).
- With API-only onboarding, the platform builds its own UI and submits collected data through the Legal Entity Management and Configuration APIs. Optional embedded onboarding components can create the relevant resources from user input, avoiding the platform's corresponding create-resource request (raw lines 160–164).
- Under the page's onboarding v4 requirements for issuing cards, a business line must be created with `service: issuing` and an industry code (raw lines 166–172). Adyen says it must verify the source of funds for card issuing and business accounts and may request evidence depending on funding type (raw lines 174–189). If funds were not processed through Adyen, the prose instructs `sourceOfFunds.adyenProcessedFunds: false` plus `sourceOfFunds.type` and an origin description (raw line 187). If processed through Adyen, it says to set `sourceOfFunds.adyenProcessedFunds: true`. The funding-source table instead says `businessLines.adyenProcessedFunds` for the Adyen-processed row (raw line 193); this field-path discrepancy is unresolved in this snapshot. Consult the raw table for accepted types, document content, and age limits (raw lines 189–280).

## Detail locators

- `Hosted onboarding` and supported operating locations: raw lines 30–86. `Requirements` states no additional preparation for an existing Issuing integration at lines 26–28; it does not establish one.
- `Instant bank account verification in hosted onboarding`: raw lines 88–119, with country/entity-type matrix.
- Hosted v3/v4 ID autofill and decision-maker features: raw lines 127–158.
- `API-only onboarding`, v4 business line, and source-of-funds instructions: raw lines 160–189.
- Source-of-funds table: raw lines 191–280; inspect the row and prose together because of the field-path mismatch noted above.

## Related

- [[adyen]] — provider context.
- [[adyen-issuing]] — Issuing concept.
- [[source-adyen-docs-issuing-onboard-users-components]] — optional embedded components.
- [[source-adyen-docs-issuing-integration-checklist]] — separate setup and live transition context.

## Raw Sources

- [[raw/adyen/docs/issuing/onboard-users/2026-09-15|Adyen Issuing onboard users, captured 2026-09-15]]
