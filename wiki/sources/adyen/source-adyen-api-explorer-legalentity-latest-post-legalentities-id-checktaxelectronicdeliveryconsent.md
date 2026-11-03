---
title: "POST /legalEntities/{id}/checkTaxElectronicDeliveryConsent — tax-form electronic-delivery consent status | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities/(id)/checkTaxElectronicDeliveryConsent"
raw_files:
  - "adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/checkTaxElectronicDeliveryConsent/2026-11-03.md"
tags: [adyen, platforms, legal-entity-management, tax-forms, electronic-delivery, consent]
---

## Overview

This 2026-11-03-captured [[adyen]] Legal Entity Management API reference describes `POST /legalEntities/{id}/checkTaxElectronicDeliveryConsent`, which returns the status of consent for electronic delivery of tax forms. Its listed server is the TEST `https://kyc-test.adyen.com/lem/v4`; the `latest` documentation URL does not establish current live availability or eligibility. See [[adyen-platforms]]. [Raw: lines 5–18]

## Key takeaways

- The required path `id` is the legal-entity ID: the owner's individual legal-entity ID for a sole proprietorship, or the organization's ID for an organization. This endpoint lists no request body or query parameters. [Raw: lines 20–25]
- A `200` means this request succeeded. The response table lists optional boolean `US1099k` for consent to electronically deliver Form US1099-K. Because it is marked optional, the operation reference alone does not specify a default for an absent field; it does not report form generation, filing, delivery, receipt, tax compliance or payment. [Raw: lines 27–35]
- The captured limits are 700 requests per five seconds in live environments, 200 per five seconds in test, and five failed requests per ten seconds. Only the TEST server is listed here. [Raw: lines 9–18]
- The page lists `400` malformed/understood-request, `401` authentication, `403` permission, `422` validation and `500` server-error cases. Their optional error fields include `errorCode`, `errorType`, `message`, `pspReference` and `status`; the generic `pspReference` description is not evidence that this consent lookup initiated a payment. [Raw: lines 38–100]

## Detail locators

- Purpose, rate limits and TEST v4 server: raw lines 5–18.
- Legal-entity path identity and parameter table: raw lines 20–25.
- `200` response and optional `US1099k`: raw lines 27–35.
- Error statuses, descriptions and body tables: raw lines 38–100.

## Related

- [[adyen-platforms]] — platform context and source route
- [[source-adyen-docs-platforms-us-tax-forms-edelivery-consent]] — separate, earlier platform guide for the broader consent workflow; its statements are not part of this endpoint's response schema

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/checkTaxElectronicDeliveryConsent/2026-11-03|Legal Entity Management consent-status endpoint — captured 2026-11-03]]