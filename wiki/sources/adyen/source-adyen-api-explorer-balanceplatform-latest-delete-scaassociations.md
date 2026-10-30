---
title: "DELETE /scaAssociations — Delete association to devices | Adyen Balance Platform API"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/scaAssociations"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/delete/scaAssociations/2026-09-15.md"
tags: [adyen, balance-platform, sca, device-associations, api-explorer]
---

## Overview

This [[adyen]] Balance Platform API Explorer snapshot documents `DELETE /scaAssociations` for deleting one or more SCA associations for a device. The captured server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; the URL contains `latest`, while the server path identifies `v2`. This is an association deletion route for an entity, not evidence that the registered device itself is deregistered. See [[adyen-business-accounts]] for the related SCA device management context.

## Key takeaways

- The page lists `WWW-Authenticate` as a required SCA authentication header. Its request-body table marks `entityId`, `entityType`, and `scaDeviceIds` required. `entityType` can be `accountHolder`, `legalEntity`, or `paymentInstrument`; `scaDeviceIds` is the list of associated device IDs to remove. The example uses an account holder and one device ID; it does not narrow the documented entity types or establish a list-size limit. [Raw: lines 12–38]
- A 204 response is labeled successful association deletion. The page also documents 401 authentication required, 403 insufficient permissions, and 500 server-could-not-process errors. Its optional error-body fields and nested `invalidFields` requirements are schema details, not evidence of any additional runtime status. [Raw: lines 39–99]
- Deletion affects the specified SCA associations. The snapshot does not specify device deregistration, reversal, downstream propagation timing, a separate verification step, or any payment or funds movement. A successful sample or documented response is not proof of a live deletion. [Raw: lines 5–7, 23–25, 39–46]

## Detail locators

- Purpose and TEST v2 server: pinned raw lines 5–10.
- Required header and body fields, entity-type values, and sample request: lines 12–38.
- 204 and 401/403/500 response headings, descriptions, and error schemas: lines 39–99.

## Related

- [[adyen-business-accounts]] — related SCA device management and evidence boundary.
- [[source-adyen-docs-business-accounts-manage-sca-devices]] — separate guide to registered-device association and device deregistration flows; its `DELETE /registeredDevices/{id}` route has different request identity.
- [[adyen-api-access]] — general credential access boundary; this endpoint's listed SCA header and errors are specific to the captured contract.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/delete/scaAssociations/2026-09-15|DELETE /scaAssociations — captured 2026-09-15]]
