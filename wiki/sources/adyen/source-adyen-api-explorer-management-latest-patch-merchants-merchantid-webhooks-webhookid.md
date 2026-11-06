---
title: "Update a merchant webhook | Adyen Management API v3"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/webhooks/(webhookId)"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/webhooks/(webhookId)/2026-11-05.md"
tags: [adyen, management-api, webhooks, merchant-account]
---

## Overview

`PATCH /merchants/{merchantId}/webhooks/{webhookId}` changes the specified merchant-account webhook configuration using new values in the request. The captured Management API server is `https://management-test.adyen.com/v3`. Both merchant-account `merchantId` and webhook-configuration `webhookId` are required path identifiers, and the API credential needs **Management API—Webhooks read and write**. This operation concerns configuration, not a payment or webhook event. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- The request body lists optional fields for `active`, endpoint `url`, `communicationFormat` (`soap`, `http`, `json`), description, endpoint username/password, certificate acceptance, encryption protocol, and other settings. For Standard webhooks, optional `additionalSettings` can include event codes and boolean properties. The raw gives no required body property; its example changes only `active`.
- `active` must be true for Adyen to send account-related webhooks. `encryptionProtocol: HTTP` is permitted only in Test; when omitted, the documented fallback is `sslVersion: TLSv1.2`. `networkType` defaults to `public`; `populateSoapActionHeader` applies only with SOAP. The three certificate-acceptance flags default to false.
- A 200 success returns the full configuration with new request values, including required response fields `active`, `communicationFormat`, `type`, and `url`; a 204 success has no additional content. The returned `id`, account reference, HMAC checksum, error flag and related links have their own schema locations. A `generateHmac` or `testWebhook` link does not indicate either action has run.
- A successful configuration update does not establish event delivery, endpoint health, payment authorization, account eligibility or compliance. `hasError: true` signals troubleshooting via a separate test endpoint.

> [!warning] Captured version mismatch
> The captured server list specifies Management API **v3 test**, but the illustrative 200 response uses `management-test.adyen.com/v1` resource links. Treat those as example links, not the endpoint version or live availability.

## Detail locators

- Raw lines 5–42: update purpose, required read-and-write role, test server, path identifiers and complete optional request-body field table.
- Raw lines 44–51: illustrative request containing only `active: true`.
- Raw lines 54–98: 200 response schema and separate 204 no-content success. Company/merchant links are conditional on configuration scope; `filterMerchantAccounts` conditional wording belongs to the returned configuration, not this PATCH request.
- Raw lines 101–198: 400, 401, 403, 422 and 500 errors; 401 is authentication required, 403 insufficient permissions and 422 request validation error.
- Raw lines 200–300: illustrative 200 configuration; example-only values and v1 links do not override the captured v3 test server.

## Related

- [[adyen-webhooks]] — webhook configuration and event context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/webhooks/(webhookId)/2026-11-05|PATCH merchant webhook, captured 2026-11-05]]