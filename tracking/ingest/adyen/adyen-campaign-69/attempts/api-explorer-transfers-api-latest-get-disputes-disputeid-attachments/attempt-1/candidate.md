---
title: "List attachments to a raised Issuing dispute"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfers-api/latest/get/disputes/(disputeId)/attachments"
raw_files:
  - "adyen/api-explorer/transfers-api/latest/get/disputes/(disputeId)/attachments/2026-11-07.md"
tags: [adyen, issuing, disputes, attachments, api-explorer]
---

## Overview

Captured `transfers-api` URL reference for the Raise disputes API v4 GET that lists attachments associated with a raised dispute ID. This is Issuing dispute evidence, distinct from funds-movement Transfers API. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- The required path `disputeId` identifies the raised dispute. Captured TEST and LIVE bases are `https://balanceplatform-api-test.adyen.com/btl/api/v4` and `https://balanceplatform-api-live.adyen.com/btl/api/v4`. This operation's raw provides no query or body parameters.
- The reference labels `200` as a successful request but gives no success response-body schema or attachment fields. It cannot by itself establish attachment contents, dispute submission, chargeback acceptance, refund or financial outcome.
- Documented errors are `401` authentication required, `403` insufficient permissions, and `422` request validation. Their optional error fields and conditionally required `invalidFields` children remain in the raw. This GET does not describe an attachment add/delete action, dispute lifecycle transition, propagation timing or idempotency.

## Detail locators

- Operation and v4 TEST/LIVE servers: raw lines 5–15.
- Required dispute ID and bodyless documented 200: raw lines 17–27.
- 401, 403 and 422 schemas: raw lines 30–84.

## Related

- [[adyen-issuing]] — issued-card dispute context.
- [[source-adyen-api-explorer-transfers-api-latest-overview]] — Raise disputes API v4 catalog at this URL family.

## Raw Sources

- [[raw/adyen/api-explorer/transfers-api/latest/get/disputes/(disputeId)/attachments/2026-11-07|Raised-dispute attachment list, captured 2026-11-07]]