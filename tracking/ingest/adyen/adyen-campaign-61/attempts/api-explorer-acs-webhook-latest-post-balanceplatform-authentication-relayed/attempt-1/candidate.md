---
title: "Adyen ACS relayed OOB authentication webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/acs-webhook/latest/post/balancePlatform.authentication.relayed"
raw_files:
  - "adyen/api-explorer/acs-webhook/latest/post/balancePlatform.authentication.relayed/2026-09-15.md"
tags: [adyen, issuing, acs, three-d-secure, webhooks]
---

## Overview

This 2026-09-15-captured ACS API Explorer endpoint describes an incoming `balancePlatform.authentication.relayed` webhook when a cardholder must perform out-of-band authentication for an issued card. The receiving platform must return **HTTP 200 with `authenticationDecision` in the body within two seconds**; the page says authentication stops if Adyen does not receive the response in time. This is an authentication decision handoff, separate from later payment authorisation or financial outcome. [[adyen]] [[adyen-issuing]]

## Key takeaways

- The request schema marks `environment` (`test` or `live`), challenge `id`, `paymentInstrumentId`, `purchase` and notification `type` required. Within `purchase`, date, merchant name and original amount are required, including three-character currency and minor-unit integer value. `threeDSRequestorAppURL` is optional; if absent, the 3DS Requestor App does not support auto-switching. `timestamp` is optional and denotes when the event was queued.
- The 200 response schema requires `authenticationDecision` with required `status` of `refused` or `proceed`. A generic `2xx` receipt is not the stated decision contract here. The response example shows `proceed`, but neither that example nor an HTTP 200 proves the cardholder finished the later challenge or that the purchase was authorised.
- **Schema/example mismatch:** the request example contains `id`, `paymentInstrumentId` and `purchase`, but omits schema-required `environment` and notification `type`. Treat it as illustrative, not a complete required-field template.
- The reference lists 400, 401, 403, 422 and 500 error sections, each with optional `errorCode`, `errorType`, `message`, payment `pspReference` and HTTP `status` fields. It does not specify a retry, fallback, signature or general delivery policy for this webhook.

## Detail locators

- Trigger, mandatory HTTP 200 decision and two-second stop condition: pinned raw lines 5–11.
- Full incoming request schema, optional app-switch URL and minor-unit amount: `## Parameters > ### Request body`, lines 15–29; incomplete request example: lines 31–47.
- 200 decision body and `refused`/`proceed` values: `## Responses > ### 200 Success`, lines 48–57; example `proceed`: lines 124–135.
- Generic error response sections and optional fields: raw lines 60–122.

## Related

- [[adyen-issuing]] — issuer-side card and OOB authentication context.
- [[source-adyen-docs-issuing-3d-secure-oob-auth-sdk-authenticate-cardholders]] — separate guide for SDK challenge and later ACS finalization; its ten-minute challenge window is distinct from this page's two-second decision deadline.
- [[adyen-webhooks]] — general webhook context; this event has a specific response contract.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/acs-webhook/latest/post/balancePlatform.authentication.relayed/2026-09-15|ACS relayed authentication reference captured 2026-09-15]]
