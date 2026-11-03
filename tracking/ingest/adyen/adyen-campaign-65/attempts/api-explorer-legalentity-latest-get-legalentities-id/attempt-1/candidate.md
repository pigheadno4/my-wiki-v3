---
title: "Adyen Legal Entity Management API v4: GET /legalEntities/{id}"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/get/legalEntities/(id)"
raw_files:
  - "adyen/api-explorer/legalentity/latest/get/legalEntities/(id)/2026-11-03.md"
tags: [adyen, legal-entity, platforms, verification, api]
---

## Overview

This 2026-11-03-captured Legal Entity Management API v4 reference describes `GET /legalEntities/{id}`, which returns one legal entity named by required path `id`. The listed server is TEST `https://kyc-test.adyen.com/lem/v4`; the page separately states Live and Test request rate limits. The `latest` route and this readback are not proof of a caller's current live access or a user's approval. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The only documented request input is required string path `id`; no query or request body is specified. The page states 700 requests per 5 seconds in Live, 200 per 5 seconds in Test, and 5 failed requests per 10 seconds. These are the captured endpoint limits, not a guaranteed throughput for a particular credential.
- A 200 returns a legal-entity resource. The response table marks root `id` required and `reference` optional (maximum 150 characters); optional branches include `individual`, `organization`, `soleProprietorship`, `trust`, and `unincorporatedPartnership`, with prose that makes the corresponding branch required when its `type` applies. The root `type` value list names only individual, organization, sole proprietorship and trust, while the table separately says `unincorporatedPartnership` is required when `type` is that value. Treat that as a schema tension, not proof that the branch is unavailable.
- Optional `capabilities` is keyed by capability. `requested` records a request; `allowed` says whether permitted; `verificationStatus` can be pending, invalid, valid or rejected. Requested and allowed levels/settings are separate. Transfer-instrument supporting-entity capability statuses can differ from the parent entity, and the table explicitly permits an allowed supporting entity even when the parent is not allowed because other supporting entities failed verification. The 200 example depicts requested-but-not-allowed, pending capabilities; it is illustrative, not approval.
- The response can also include entity associations (with required associated `legalEntityId` and relationship `type` within each item), document IDs/details, transfer instruments with masked identifiers, verification problems and deadlines. `verificationDeadlines` names capabilities that will be disallowed if unresolved by the deadline. Conditional field requirements in entity/address branches are **response-schema descriptions**, not GET request inputs. Readback does not create an entity, complete verification, grant a capability, execute a transfer or prove settlement.
- The page lists 400, 401, 403, 422 and 500 errors. Its generic error schema includes optional `pspReference` labeled as a payment reference; this does not make the legal-entity GET a payment operation. No endpoint-specific idempotency, update, approval, reversal, or version/conflict semantics are supplied.

## Detail locators

- Purpose, rate limits, TEST server, path and 200: pinned raw lines 5–35.
- Capability requested/allowed/verification and supporting-entity distinctions: response schema lines 35–57; illustrative pending example lines 380–453.
- Associations, document branches and individual details: lines 58–120. Organization, problem and sole-proprietorship branches: lines 121–237. Transfer instruments, trust, unincorporated partnership, root type and deadlines: lines 238–313.
- Generic error schemas: lines 316–378.

## Related

- [[adyen-platforms]] — platform legal-entity and verification context.
- [[source-adyen-api-explorer-legalentity-latest-post-legalentities]] — separate creation reference.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/get/legalEntities/(id)/2026-11-03|Legal Entity GET snapshot]]