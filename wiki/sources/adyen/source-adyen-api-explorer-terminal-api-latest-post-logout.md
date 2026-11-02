---
title: "Adyen Terminal API POST /logout Logout Request"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/terminal-api/latest/post/logout"
raw_files:
  - "adyen/api-explorer/terminal-api/latest/post/logout/2026-09-15.md"
tags: [adyen, terminal-api, api-explorer, logout]
---

## Overview

This 2026-09-15 API Explorer snapshot describes Terminal API `POST /logout` as a Logout Request and Logout Response. The request's optional `MaintenanceAllowed` field expresses whether the POI may go to maintenance after the session closes; the page does not promise that maintenance will occur. Its opening `Empty.` provides no further operation description. See [[adyen]] and [[adyen-terminal-api]].

## Key takeaways

- Listed cloud test destinations are `https://device-api-test.adyen.com/v1/merchants/{merchantAccount}/devices/{deviceId}/sync` and `/async`; a local-hosting entry is `<local-terminal-IP-address>`. These identify cloud merchant/device URL parameters or a local terminal address, not a message caller, operator or session identifier. `/v1` is in the cloud URL; the `terminal-api/latest` page states no explicit Terminal API protocol version.
- The request-body table lists only optional boolean `MaintenanceAllowed`. It says the field indicates that the POI terminal is able to or has to go to maintenance and is sent to express that, after closing the session, the POI may go to maintenance. The snapshot supplies no required request property, explicit session key, default, limit, logout timing or reversal behavior.
- The `200 Success` section conveys the Logout result. Its response body requires `Response` and nested string `Result`, whose possible values are `Success`, `Failure`, and `Partial`. The table marks `ErrorCondition` optional, while the parent `Response` description says it must be present when `Result` is other than `Success`; for `Success` it is absent or unused. Optional `AdditionalResponse` is processing-status information logged by the POI if present. The raw table lists the error-condition values.
- The `200 Success` section label does not establish `Response.Result=Success` or confirm that a session closed. This page does not specify command acknowledgement separate from the response, authentication, correlation, asynchronous completion, payment authorization/capture, reconciliation, settlement, bank receipt or HTTP error responses.

## Detail locators

- Operation description and endpoint variants: raw lines 5–19.
- Request-body field: raw lines 21–26.
- Response result, conditional error and logging fields: raw lines 28–40.

## Related

- [[adyen]]
- [[adyen-terminal-api]]

## Raw Sources

- [[raw/adyen/api-explorer/terminal-api/latest/post/logout/2026-09-15|Adyen API Explorer POST /logout snapshot, 2026-09-15]]
