---
title: "Adyen Management API: get merchant terminal settings"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/terminalSettings"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/terminalSettings/2026-11-07.md"
tags: [adyen, management-api, point-of-sale, terminal-settings]
---

## Overview

This 2026-11-07 snapshot of the Management API `latest` reference describes `GET /merchants/{merchantId}/terminalSettings` on the listed TEST `/v3` server. It reads settings configured for the merchant account; those settings apply to its terminals unless overridden at store or individual-terminal level. This configuration read is distinct from on-device application and payment execution. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- `merchantId` is the required path parameter and identifies a merchant account. The capture lists no query parameter or request body. The API credential needs Terminal settings read or read and write; sensitive settings additionally need Terminal settings Advanced read and write. Live requests are rate limited, without a numerical limit stated here.
- `200` means the request succeeded and describes optional settings groups including receipts, connectivity, gratuities, hardware, Terminal API notification URLs and shared key, payment, refunds, standalone, store-and-forward, surcharge, and Wi-Fi. Do not assume any particular group appears or that example values are defaults. `204` is success with no content.
- Consequential field qualifications remain in the response table: DCC enablement carries receipt and terms responsibilities; first contactless-currency change requires contacting Adyen for a compliance check; unreferenced refunds carry loss liability; store-and-forward prose names `maxAmount`, `maxPayments`, and `supportedCardTypes` configuration. These are field descriptions in a GET response, not this GET's required inputs or proof of feature activation.
- Documented failures are `400` request problem, `401` authentication required, `403` insufficient permission, `422` validation error, and `500` server processing error. A readback establishes the documented configuration response at capture scope, not device propagation, current Live eligibility, compliance, authorization, capture, or settlement.

## Detail locators

- Purpose, roles, Live rate-limit notice, TEST server, and merchant path ID: pinned raw lines 5–29.
- `200` optional response schema and feature-specific conditions, units, defaults, nested required properties: pinned raw lines 31–196. In particular inspect lines 47–56, 70–77, 103–105, 134–163, and 145–155 before using those features.
- `204` and error response shapes: pinned raw lines 199–300. The `200` JSON at lines 302–399 is illustrative.

## Related

- [[adyen-terminal-management]] — fleet configuration concept and related task references.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/terminalSettings/2026-11-07|2026-11-07 pinned GET merchant terminal settings reference]]