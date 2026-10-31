---
title: "Adyen deprecated POS Terminal Management API v1 overview"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/postfmapi/latest/overview"
raw_files:
  - "adyen/api-explorer/postfmapi/latest/overview/2026-09-15.md"
tags: [adyen, pos, terminal-management, deprecated]
---

## Overview

Captured 2026-09-15 API Explorer overview for the deprecated **POS Terminal Management API v1** (`postfmapi`). It catalogs operations to inspect terminals and stores and assign terminals to a merchant account or store. This older fleet-administration API is separate from the newer Management API and from payment messaging through the Terminal API. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- The page dates deprecation from January 1, 2025 and says support stops April 1, 2025; it directs fleet-management automation to the Management API. These are the captured page's stated dates, not a present-day service test.
- Each request requires an API key in `X-API-Key` and the **POS Terminal Management API role** on the API credential, with roles set up by an Adyen contact. The page also says new web-service-user credentials are needed when going live and specifies a live Customer Area API key for the live endpoint.
- The versioned test base is `https://postfmapi-test.adyen.com/postfmapi/terminal/v1`; the stated live base is `https://postfmapi-live.adyen.com/postfmapi/terminal/v1`. Versioned endpoint Boolean responses are strings `"true"`/`"false"`; without a version suffix they are Boolean values. This overview lists five POST endpoints but supplies no per-operation request/response schema or evidence of assignment completion, terminal readiness or actual payments.

## Detail locators

- Purpose, deprecation, authentication, role, versioning, live/test endpoint details: [[raw/adyen/api-explorer/postfmapi/latest/overview/2026-09-15|raw lines 5–47]].
- Endpoint catalog: raw lines 49–58, covering `assignTerminals`, `findTerminal`, `getStoresUnderAccount`, `getTerminalDetails` and `getTerminalsUnderAccount`. Consult each operation's own pinned raw for its contract.

## Related

- [[adyen-terminal-management]] — fleet administration context and Management API route.

## Raw Sources

- [[raw/adyen/api-explorer/postfmapi/latest/overview/2026-09-15|deprecated POS Terminal Management API v1 overview captured raw]]
