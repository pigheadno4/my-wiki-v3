---
title: "Adyen legacy POS Terminal Management API: findTerminal"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/postfmapi/latest/post/findTerminal"
raw_files:
  - "adyen/api-explorer/postfmapi/latest/post/findTerminal/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-management, deprecated-api]
---

## Overview

Captured legacy POS Terminal Management API v1 TEST reference for `POST /findTerminal`. Given a terminal ID, it returns the company account, merchant account or store to which that terminal is assigned. The page says this API was deprecated from 2025-01-01 and support stopped on 2025-04-01, and directs fleet automation to the Management API. This legacy lookup contract does not define the newer Management API contract. [[adyen]] [[adyen-terminal-management]]

## Key takeaways

- The request body requires `terminal`, the unique terminal ID in `[Device model]-[Serial number]` form. The shown server is `https://postfmapi-test.adyen.com/postfmapi/terminal/v1`. See raw lines 11–28.
- The 200 response requires `companyAccount` and `terminal`. Only a company-account level indicates company inventory; a `merchantAccount` with no `store` indicates merchant assignment; `store` is the assigned store code when present. `merchantInventory: true` means merchant inventory and cannot be boarded; `false` means assigned as an in-store terminal that is ready to be boarded or already boarded. Thus the lookup alone does not distinguish those latter two states or prove operational/payment readiness. See raw lines 29–41 and sample lines 108–121.
- The page lists 400 request-reading, 401 authentication, 403 insufficient-permission, 422 validation and 500 server errors. The example error codes are illustrative response examples, not an exhaustive status map. See raw lines 44–106 and 123–169.
- The dated deprecation/support notice and TEST server limit this to captured legacy reference evidence; no current endpoint availability, successful terminal boarding, applied configuration or payment result follows from this page. See raw lines 5–12.

## Detail locators

- Purpose, deprecation and TEST server: raw lines 5–12.
- Request property and example: raw lines 14–28.
- Assignment semantics and response fields: raw lines 29–41.
- Error schemas and examples: raw lines 44–169.

## Related

- [[adyen-terminal-management]] — current terminal-fleet administration concept; keep its Management API routes distinct from this legacy endpoint.

## Raw Sources

- [[raw/adyen/api-explorer/postfmapi/latest/post/findTerminal/2026-09-15|Legacy findTerminal reference captured 2026-09-15]]
