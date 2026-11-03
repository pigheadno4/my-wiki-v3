---
title: "Set tax electronic-delivery consent for a legal entity | Adyen LEM API v4"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities/(id)/setTaxElectronicDeliveryConsent"
raw_files:
  - "adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/setTaxElectronicDeliveryConsent/2026-11-03.md"
tags: [adyen, platforms, legal-entity-management, tax-forms, electronic-delivery, consent]
---

## Overview

This [[adyen]] Legal Entity Management API reference, captured 2026-11-03, describes `POST /legalEntities/{id}/setTaxElectronicDeliveryConsent` for setting electronic-delivery consent status for tax forms. The captured server is the LEM v4 TEST endpoint `https://kyc-test.adyen.com/lem/v4`; the page separately lists live and test rate limits. See [[adyen-platforms]] for the platform context and the separate US tax-form e-delivery guide for the user-consent workflow.

## Key takeaways

- The required path `id` identifies a legal entity: the owner's individual legal entity for a sole proprietorship, or the organization legal entity for an organization. The request-body table marks `US1099k` as an optional boolean for consent to electronic delivery of Form US1099-K; it does not state a default, require the whole body, or show a request example. [Raw: lines 20–31]
- The page lists 700 requests per five seconds in live, 200 per five seconds in test, and five failed requests per ten seconds. These are captured reference limits, not evidence of a caller's live access. [Raw: lines 9–18]
- The `200 Success` section instructs readers to inspect the actual response code for request status and specifies no success response fields. A success response here is request-status evidence, not evidence that a form was generated, delivered, received, or that a broader legal requirement was met. [Raw: lines 33–36]
- The listed failures are `400` unreadable/invalid request, `401` authentication required, `403` insufficient permissions, `422` validation error, and `500` server processing error. Each error table lists optional `errorCode`, `errorType`, `message`, `pspReference`, and `status`; the generic `pspReference` field does not make this a payment operation. [Raw: lines 39–101]

## Detail locators

- Purpose and rate limits: raw lines 5–18.
- Path identity and request-body field: raw lines 20–31.
- Success wording: raw lines 33–36.
- Error categories and optional error fields: raw lines 39–101.

## Related

- [[adyen-platforms]] — platform and legal-entity context.
- [[source-adyen-docs-platforms-us-tax-forms-edelivery-consent]] — separate Platforms consent-workflow guide; its claims belong to that guide.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/setTaxElectronicDeliveryConsent/2026-11-03|LEM v4 setTaxElectronicDeliveryConsent API reference — captured 2026-11-03]]