---
title: "Adyen Raise disputes API v4: remove a dispute attachment"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfers-api/latest/delete/disputes/(disputeId)/attachments/(attachmentId)"
raw_files:
  - "adyen/api-explorer/transfers-api/latest/delete/disputes/(disputeId)/attachments/(attachmentId)/2026-11-07.md"
tags: [adyen, issuing, disputes, attachments, transfers-api]
---

## Overview

This captured Raise disputes API v4 reference at a `transfers-api` URL describes `DELETE /disputes/{disputeId}/attachments/{attachmentId}`. It removes the identified attachment from the raised dispute; Adyen may retain the file for compliance purposes. [[adyen]] [[adyen-issuing]]

## Key takeaways

- Both path IDs are required: `disputeId` identifies the raised dispute and `attachmentId` identifies its attachment. The page lists no request body or query parameters.
- `204` means the attachment was successfully removed from the dispute. It does not state that Adyen erased every retained copy, and it does not establish a dispute decision or financial outcome.
- The captured test and live bases are `https://balanceplatform-api-test.adyen.com/btl/api/v4` and `https://balanceplatform-api-live.adyen.com/btl/api/v4`. Listed errors are `401` authentication required, `403` insufficient permissions, and `422` validation error; their response properties are optional at the top level.

## Detail locators

- Operation and possible compliance retention: raw lines 5–7. Servers and required path IDs: raw lines 9–23.
- `204` and error response schemas, including nested validation-field properties: raw lines 25–85.

## Related

- [[adyen-issuing]] — Issuing raised-dispute and supporting-information context.

## Raw Sources

- [[raw/adyen/api-explorer/transfers-api/latest/delete/disputes/(disputeId)/attachments/(attachmentId)/2026-11-07|Raise disputes API v4 attachment deletion reference]]
