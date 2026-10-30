---
title: "Adyen Legal Entity Management API v4: POST /legalEntities"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities"
raw_files:
  - "adyen/api-explorer/legalentity/latest/post/legalEntities/2026-09-15.md"
tags: [adyen, legal-entity, platforms, verification, api-reference]
---

## Overview

This 2026-09-15-captured Legal Entity Management API v4 test-server reference defines `POST /legalEntities` to create a legal entity containing information about a platform user for Adyen verification checks. Adyen says results are conveyed by webhook or API response. Creation and a returned legal-entity ID do not establish verified identity, an allowed capability, an account holder, or a completed payment. See [[adyen-platforms]] for the platform resource context.

## Key takeaways

- The request schema marks top-level `type` required and lists `individual`, `organization`, `soleProprietorship`, and `trust`. Each matching object is conditionally required when its type is selected. However, `unincorporatedPartnership` has its own conditionally required object and a request/response example despite omission from the top-level `type` enum. This internal mismatch is unresolved; the example is not a guarantee that the value is accepted.
- Conditional nested rules matter: individual name and residential address; organization legal name and registered address; sole proprietorship and trust name, governing-law country and registered address; trust subtype. Address city/state choices require companion postal/street data, and state is required for Australia/New Zealand. In the individual and organization request branches, support information is required if you have a platform setup; the captured sole-proprietorship, trust and unincorporated-partnership branches do not list a support field. Other country, tax, organization and association rules remain in the raw field table. The schema lists required properties but does not separately specify whole-body requiredness.
- An optional `capabilities` request may ask for actions, but the response distinguishes `requested` from `allowed`; Adyen sets `allowed: true` after successful verification. Response capability verification statuses include pending, invalid, valid and rejected, and optional `problems` and verification deadlines can explain issues or future capability loss. A sample created individual has `requested: true`, `allowed: false`, `verificationStatus: pending`. Do not infer approval from the 200 or request alone.
- The optional `x-requested-verification-code` header accepts one suberror code and is test-only. Stated rate limits are 700 live and 200 test requests per five seconds; failed requests have a separate five per ten seconds limit. The captured server is test `/lem/v4`; the `latest` URL does not establish the currently served version or live eligibility.
- Errors are 400, 401, 403, 422 and 500. The error schema includes a `pspReference` described as a payment reference, but this create-legal-entity operation is not a payment. No endpoint-specific role or exact verification completion time is given.

## Detail locators

- Purpose, verification result channels and rate limits: raw lines 5–20. Test-only header: lines 24–27.
- Request schema and conditional entity branches: raw lines 30–240; top-level type/partnership mismatch at lines 210–211. Country/entity request examples: lines 242–504.
- Response capability allowed/requested/verification status, legal-entity `id`, problems and deadlines: raw lines 505–787. Error schemas: lines 790–852. Response examples, including pending capability and partnership: lines 854–1133.

## Related

- [[adyen-platforms]] — platform user and legal-entity context.
- [[adyen-api-access]] — general credential context; this page lists 401/403 but no role.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/post/legalEntities/2026-09-15|POST /legalEntities captured 2026-09-15]]
