---
title: "POST /legalEntities/{id}/termsOfService — Get Terms of Service document | Adyen Legal Entity Management API"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities/(id)/termsOfService"
raw_files:
  - "adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/termsOfService/2026-11-03.md"
tags: [adyen, legal-entity-management-api, terms-of-service, legal-entity, api-reference]
---

## Overview

This captured Legal Entity Management API `/lem/v4` POST returns a Terms of Service document for a legal entity. Its listed server is TEST `https://kyc-test.adyen.com/lem/v4`; the page separately states live and test rate limits but does not list a live server URL. Document retrieval is separate from presentation to, or acceptance by, an authorized person. [[adyen]] [[adyen-platforms]]

## Key takeaways

- The required path `id` is the individual's legal-entity ID for a sole proprietorship or the organization's legal-entity ID for an organization. The body requires `language` (`en` or `fr`) and Terms `type`; optional `termsOfServiceDocumentFormat` defaults to `JSON` and permits `JSON`, `PDF`, or `TXT`. The raw lists twelve type values, including Platforms, Issuing, Capital, account, card, and direct-debit variants; use the raw enum rather than treating the `adyenIssuing` example as universal.
- A `200` means the document request succeeded. All listed response fields are optional: Base64-encoded `document`, legal-entity `id`, `language`, `termsOfServiceDocumentFormat`, `termsOfServiceDocumentId`, and `type`. French is available only for some integration types in certain countries/regions; the response description directs readers to an Adyen contact for details.
- Rate limits are 700 requests per 5 seconds in live, 200 per 5 seconds in test, and 5 failed requests per 10 seconds. The page lists `400`, `401`, `403`, `422`, and `500` errors with optional error-body fields. It states no caller role, idempotency rule, acceptance action, consent status, approval timing, or version/conflict behavior.
- A returned document or document ID does not prove that the correct signer viewed or accepted the Terms, that a requirement was satisfied, or that onboarding, verification, capability activation, grant funding, payment, or payout occurred.

## Detail locators

- Purpose, limits, TEST server and legal-entity path identity: raw lines 5–25.
- Body language, format/default, complete type enum and example: raw lines 28–43.
- `200` optional response fields and French qualification: raw lines 44–57.
- Error responses and illustrative document response: raw lines 60–137.

## Related

- [[adyen-platforms]] — onboarding and legal-entity context.
- [[source-adyen-docs-platforms-onboard-users-terms-of-service]] — separate guide for Terms presentation and acceptance.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/termsOfService/2026-11-03|POST Terms document captured 2026-11-03]]
