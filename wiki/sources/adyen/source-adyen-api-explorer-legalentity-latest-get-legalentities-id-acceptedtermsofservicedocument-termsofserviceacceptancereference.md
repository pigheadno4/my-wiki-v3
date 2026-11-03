---
title: "GET /legalEntities/{id}/acceptedTermsOfServiceDocument/{termsofserviceacceptancereference} — Get accepted Terms of Service document | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/get/legalEntities/(id)/acceptedTermsOfServiceDocument/(termsofserviceacceptancereference)"
raw_files:
  - "adyen/api-explorer/legalentity/latest/get/legalEntities/(id)/acceptedTermsOfServiceDocument/(termsofserviceacceptancereference)/2026-11-03.md"
tags: [adyen, legal-entity-management, terms-of-service, onboarding, api-explorer]
---

## Overview

This [[adyen]] Legal Entity Management API Explorer snapshot documents `GET /legalEntities/{id}/acceptedTermsOfServiceDocument/{termsofserviceacceptancereference}`, a read of an accepted Terms of Service document for a legal entity. The captured server is TEST `https://kyc-test.adyen.com/lem/v4`; the URL says `latest` while the server path identifies `v4`. See [[adyen-platforms]] for platform onboarding context.

## Key takeaways

- Two string path parameters are required: `id` is the legal-entity identifier, and `termsofserviceacceptancereference` is an Adyen-generated reference for accepted Terms of Service. For a sole proprietorship, `id` is the owner's individual legal-entity ID; for an organization, it is the organization ID. An optional `termsOfServiceDocumentFormat` query accepts JSON, PDF or TXT; no format default is stated. [Raw: lines 20–32]
- A 200 says the request succeeded. The response table marks `document`, legal-entity `id`, `termsOfServiceAcceptanceReference` and `termsOfServiceDocumentFormat` all optional. If present, `document` is the accepted document in the requested format represented as Base64-encoded bytes. The page specifies no success example or guarantee that every 200 includes the document. [Raw: lines 34–45]
- Rate limits are 700 requests per five seconds in live environments, 200 per five seconds in test, and five failed requests per ten seconds. Only a TEST server URL is listed. The page does not name a caller role or request-body fields. [Raw: lines 9–18, 20–32]
- Error sections list 400 request-reading/understanding, 401 authentication, 403 insufficient permissions, 422 validation and 500 server processing. Their generic error-body fields are all optional; the `pspReference` description is a generic payment-reference field, not evidence of a payment. [Raw: lines 48–110]
- Retrieving an accepted-document record is distinct from presenting terms, recording a new acceptance, verifying the authorized signatory, or proving legal-entity verification and capability approval. The response has no signer identity, acceptance timestamp, review status or financial outcome. This dated TEST v4 capture does not establish current live availability or compliance for a particular user. [Raw: lines 5–45]

## Detail locators

- Purpose, rate limits and TEST v4 server: pinned raw lines 5–18.
- Required path IDs and optional document format: lines 20–32.
- 200 optional response fields and Base64 document representation: lines 34–45.
- Error meanings and problem-body schema: lines 48–110.

## Related

- [[adyen-platforms]] — platform onboarding and Terms of Service context.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/get/legalEntities/(id)/acceptedTermsOfServiceDocument/(termsofserviceacceptancereference)/2026-11-03|GET accepted Terms of Service document — captured 2026-11-03]]