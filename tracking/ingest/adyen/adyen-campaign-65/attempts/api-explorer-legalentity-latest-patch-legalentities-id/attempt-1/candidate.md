---
title: "Adyen Legal Entity Management API v4: Update a legal entity"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/patch/legalEntities/(id)"
raw_files:
  - "adyen/api-explorer/legalentity/latest/patch/legalEntities/(id)/2026-11-03.md"
tags: [adyen, legal-entity-management, platforms, onboarding, verification, api-reference]
---

## Overview

The 2026-11-03-captured Legal Entity Management API v4 TEST reference describes `PATCH /legalEntities/{id}` to update the legal entity identified by required path `id`. A legal-entity type change must be sent with only the new `type`; other information needs a separate request. If `entityAssociations` is updated, the submitted array replaces the entire association array, so omitted entries are removed. This is a legal-entity data update, not verification approval, capability enablement or a payment/payout result. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The only listed server is `https://kyc-test.adyen.com/lem/v4`. The reference states live rate limits of 700 requests per five seconds, test limits of 200 per five seconds and a failed-request limit of five failures per ten seconds. The optional `x-requested-verification-code` header can use `0_0001` to resolve legal-entity suberrors only in TEST; it is not a live remediation route.
- The request body lists optional top-level `capabilities`, `entityAssociations`, `individual`, `organization`, `reference`, `soleProprietorship`, `trust`, `type`, `unincorporatedPartnership` and `verificationPlan`. Optional parents contain required nested properties when their branch is supplied. The prose requires `individual`, `organization`, `soleProprietorship`, `trust` or `unincorporatedPartnership` for its matching `type`; association entries require `legalEntityId` and association `type`. `reference` has a 150-character maximum; `verificationPlan=upfront` is named for marketplace upfront verification. Exact per-field/country validation remains in the raw schema.
- The conditional branch detail matters: individual name and residential address, organization legal name and registered address, sole-proprietorship name and registered address, trust governing-law country/name/registered address/trust subtype, and unincorporated-partnership governing-law country/name/registered address have nested requirements. Address and identification subfields have further country- and presence-based conditions; optional parent fields are not globally required for every PATCH.
- A `200` response requires legal-entity `id` but does not by itself indicate completed verification. Optional `capabilities` entries separate `requested` and `requestedLevel/Settings` from `allowed` and `allowedLevel/Settings`; the schema says to check `allowed` for permission and says Adyen sets it true after successful verification. `verificationStatus` can be `pending`, `invalid`, `valid` or `rejected` at capability and supporting-transfer-instrument levels. The schema expressly allows an individually `allowed` supporting transfer instrument even if the parent capability is not allowed because other supporting entities failed. Optional `problems` and `verificationDeadlines` expose errors and future capability-disallowance deadlines, not proof of present approval.

> [!warning] Contradiction
> The request and response top-level `type` rows list only `individual`, `organization`, `soleProprietorship` and `trust`, while both schemas contain an `unincorporatedPartnership` branch expressly required when `type` is `unincorporatedPartnership`. The pinned page does not reconcile the enum with the branch; do not infer that the unlisted value is accepted or rejected.

- The labeled `updateLegalEntitySoleProp` example sends only an association but shows a response with top-level `type: individual`; example labels and returned fields do not prove a type transition. The `200` samples include IDs and entity details but no demonstrated `allowed=true` or completed verification.
- Listed errors are `400` malformed/unclear request, `401` authentication required, `403` insufficient permission, `422` validation error and `500` server processing failure. The reference states no idempotency key, concurrency/version-conflict behavior or verification-completion timing. The dated TEST snapshot does not establish current live eligibility, accepted legal status, capability permission, payment authorization, transfer, settlement or bank receipt.

## Detail locators

- Raw lines 5–35: operation rules, whole-array replacement, rate limits, TEST v4 server, path and TEST-only verification-code header.
- Raw lines 38–252: full request schema, type-conditioned entity branches, country/address rules, association identities and verification plan.
- Raw lines 254–328: six request examples, including isolated type change and association updates.
- Raw lines 329–615: complete `200` schema, response ID, requested/allowed/verification fields, supporting entities, problems, instruments and deadlines.
- Raw lines 618–680: `400`, `401`, `403`, `422` and `500` error schemas.
- Raw lines 682–892: six `200` examples; the sole-proprietorship label/individual response and other example values are illustrative.

## Related

- [[adyen-platforms]] — Platforms onboarding and verification concept; this v4 API reference governs this PATCH.
- [[source-adyen-api-explorer-legalentity-latest-post-legalentities]] — separate legal-entity creation reference.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/patch/legalEntities/(id)/2026-11-03|Update legal entity API reference (2026-11-03)]]