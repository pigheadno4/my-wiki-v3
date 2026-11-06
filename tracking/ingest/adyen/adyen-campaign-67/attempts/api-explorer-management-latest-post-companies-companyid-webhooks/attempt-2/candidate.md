---
title: "Management API: Set up a company webhook"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/webhooks"
raw_files:
  - "adyen/api-explorer/Management/latest/post/companies/(companyId)/webhooks/2026-11-05.md"
tags: [adyen, management-api, webhooks, company-account]
---

## Overview

The captured Management API reference documents `POST /companies/{companyId}/webhooks` for a company-account webhook subscription. It lists a Test `https://management-test.adyen.com/v3` server and requires the caller's API credential to have **Management API—Webhooks read and write**. `companyId` identifies the company account. This is configuration of an outbound notification destination, not a webhook event or payment request. [[adyen]] [[adyen-webhooks]]

## Key takeaways

- The request body marks `active`, `communicationFormat`, `filterMerchantAccountType`, `filterMerchantAccounts`, `type`, and `url` required. The `filterMerchantAccounts` description narrows that field to `includeAccounts` or `excludeAccounts`; it says the list is not needed for `allAccounts`. `url` is the public notification destination. `communicationFormat` is `soap`, `http`, or `json`; the request `type` options are in the raw table.
- `active: true` is necessary for Adyen to send account-event webhooks. Optional certificate acceptance flags default to `false`; `networkType` defaults to `public`; `populateSoapActionHeader` defaults to `false` and applies only to SOAP. Optional `encryptionProtocol` lists TLSv1.3, TLSv1.2, and HTTP on Test only, and describes TLSv1.2 if omitted. Optional username/password are destination basic-auth credentials.
- The `200` response says the request succeeded and describes the webhook configuration, including required `active`, `communicationFormat`, `type`, and `url`. The parent `_links` object is optional; within it, `generateHmac`, `self`, and `testWebhook` objects are marked required when that parent is present. `id`, `hasError`, `hasPassword`, `hmacKeyCheckValue`, `accountReference`, and `_links.company` are optional. A returned configuration or `active: true` does not establish notification delivery, endpoint security, HMAC generation, successful test, merchant payment capability, or a financial outcome.
- The reference lists 400, 401, 403, 422, and 500 errors. It gives no idempotency header, propagation delay, delivery guarantee, reversal procedure, or Live URL for this operation. These are boundaries of this captured page, not claims that those behaviors never exist.

> [!warning] Contradiction
> The operation lists a Test `/v3` server, but its `200` response example uses `/v1` in the self, company, generateHmac, and testWebhook hrefs. The example does not resolve which versioned links should be used for later calls. The request table omits `terminal-api-notification` from `type`, while the response table includes it; this snapshot does not reconcile create-time acceptance of that value.

## Detail locators

- Caller role, Test server, and company path identity: raw lines 5–21.
- Complete request fields, conditional merchant filter, defaults, optional authentication, and webhook types: raw lines 24–44. The JSON request example is lines 46–66; its values are illustrative.
- `200` response fields and resource links: raw lines 67–109. Error statuses and payload fields: lines 112–209. The JSON `200` example is lines 211–316; its values and `/v1` hrefs are illustrative.

## Related

- [[adyen-webhooks]] — Adyen webhook concepts and delivery boundaries.
- [[source-adyen-docs-development-resources-webhooks-configure-and-manage]] — separate setup and management guide; its behavior is not imported into this API reference.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/webhooks/2026-11-05|Pinned Management API company webhook POST reference]]