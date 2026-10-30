---
title: "Adyen Legal Entity Management API v4: list hosted-onboarding themes"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/get/themes"
raw_files:
  - "adyen/api-explorer/legalentity/latest/get/themes/2026-09-15.md"
tags: [adyen, legal-entity-management, hosted-onboarding, themes, api]
---

## Overview

This 2026-09-15-captured Legal Entity Management API v4 reference documents `GET /themes`, a read that lists hosted-onboarding page themes. The shown server is `https://kyc-test.adyen.com/lem/v4`; the `latest` URL does not establish current live availability or version. Theme records concern onboarding-page presentation, not a legal entity, account-holder capability, verification result or completed onboarding. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The endpoint lists themes and has no request parameters or body in this capture. A `200` response marks the `themes` array required and `next`/`previous` page strings optional, present only when the corresponding page exists. Within a theme record, `id`, `createdAt` and `properties` are marked required; `description` and `updatedAt` are optional. The two illustrated light/dark theme properties and IDs are examples, not a complete property contract or proof of a configured user's page.
- The captured rate limits are **700 requests per 5 seconds** for live environments, **200 per 5 seconds** for test, and **5 failed requests per 10 seconds**. These are source-time API limits, not evidence of a live endpoint or access grant.
- The page lists `400` unreadable request, `401` authentication, `403` insufficient permissions, `422` validation and `500` server errors, but gives no exact credential role or theme-application procedure. The optional error-body field named `pspReference` is described generically as a payment PSP reference; its presence in the schema does not make this a payment endpoint.
- The separate [[source-adyen-docs-platforms-onboard-users-customize-hosted-onboarding|Platforms hosted-onboarding guide]] explains theme creation/application and link settings in its own scope. A theme list response does not create or apply a theme, verify an entity, grant a capability or prove user completion.

## Detail locators

- Method, purpose, rate limits and v4 test host: raw lines 5–18.
- `200` pagination and theme item schema: lines 20–35.
- Error meanings and generic body fields: lines 38–100.
- Two illustrative theme/property objects: lines 102–143.

## Related

- [[adyen-platforms]] — platform onboarding context.
- [[adyen-issuing]] — separate Issuing use of hosted onboarding.
- [[source-adyen-docs-platforms-onboard-users-customize-hosted-onboarding]] — theme setup and application guide.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/get/themes/2026-09-15|GET /themes API Explorer capture]]
