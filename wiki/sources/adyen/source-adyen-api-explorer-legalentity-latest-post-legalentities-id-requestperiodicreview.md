---
title: "Adyen Legal Entity Management API v4: request periodic review"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities/(id)/requestPeriodicReview"
raw_files:
  - "adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/requestPeriodicReview/2026-11-03.md"
tags: [adyen, legal-entity, platforms, verification, api]
---

## Overview

This 2026-11-03-captured Legal Entity Management API v4 reference documents `POST /legalEntities/{id}/requestPeriodicReview` to request a periodic data review for the legal entity of the user named in the path. Its only listed server is TEST `https://kyc-test.adyen.com/lem/v4`. The `latest` documentation route does not establish live availability or a caller's access. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- Required string path `id` is the unique legal-entity identifier. The captured page documents no request body, query parameter, conditional input, default, rate limit, specific caller role or idempotency key.
- A 204 says the request was successfully processed and returns no additional content. It is evidence of the review **request**, not a completed periodic review, a valid verification result, or permission to use a capability.
- This short reference lists no error responses, asynchronous result contract, review deadline, retry behavior, reversal, version/conflict rule or financial operation. Those absences are limits of this capture, not guarantees that failures or later review steps cannot occur.

## Detail locators

- Purpose and TEST server: pinned raw lines 5–10.
- Required legal-entity path ID and bodyless 204: pinned raw lines 12–22. No schemas or examples are present.

## Related

- [[adyen-platforms]] — Platforms verification context.
- [[source-adyen-docs-platforms-verification-overview-data-review-process]] — separate periodic data-review guide; consult it for workflow detail.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/post/legalEntities/(id)/requestPeriodicReview/2026-11-03|Legal Entity periodic-review request snapshot]]