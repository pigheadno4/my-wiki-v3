---
title: "Adyen Terminal API POST /admin Custom Admin Request"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/terminal-api/latest/post/admin"
raw_files:
  - "adyen/api-explorer/terminal-api/latest/post/admin/2026-09-15.md"
tags: [adyen, terminal-api, api-explorer, admin-request]
---

## Overview

This 2026-09-15 API Explorer snapshot describes Terminal API `POST /admin` as a Custom Admin Request and its Custom Admin Response. The raw starts with `Empty.` before the one-sentence request description; it does not define an administrative operation beyond the optional service identifier. See [[adyen]] and [[adyen-terminal-api]].

## Key takeaways

- The listed cloud test server URLs are `https://device-api-test.adyen.com/v1/merchants/{merchantAccount}/devices/{deviceId}/sync` and `/async`; a local-hosting entry is `<local-terminal-IP-address>`. These are listed transport destinations, not an assertion that any device or merchant is enabled. The `/v1` segment belongs to those cloud URLs; the captured page is under `terminal-api/latest` and states no explicit Terminal API protocol version.
- The request-body table names only optional string `ServiceIdentification`, the identification of the administrative service to process. The page supplies no required request fields, request wrapper, caller identity, session identifier, field limit, default or timing rule.
- A `200 Success` section says its response conveys the Custom Admin result. Its response body requires `Response` and nested string `Result`, with values `Success`, `Failure`, or `Partial`. `ErrorCondition` is optional in the table, while the `Response` description says it must be present when `Result` is other than `Success`; for `Success` it is absent or not used. Optional `AdditionalResponse` is processing-status information logged by the POI if present. The enum values and exact field wording remain in the raw table.
- The `200 Success` section label does not establish `Response.Result=Success`; inspect the body result. This page defines no payment authorization, capture, reversal, settlement, bank receipt, authentication mechanism, asynchronous completion or correlation rule. It does not specify HTTP error responses.

## Detail locators

- Endpoint variants and environment: raw lines 10–19.
- Request field and requiredness: raw lines 21–26.
- Response shape, conditional error semantics and error-condition values: raw lines 28–40.

## Related

- [[adyen]]
- [[adyen-terminal-api]]

## Raw Sources

- [[raw/adyen/api-explorer/terminal-api/latest/post/admin/2026-09-15|Adyen API Explorer POST /admin snapshot, 2026-09-15]]
