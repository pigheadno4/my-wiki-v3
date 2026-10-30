---
title: "Adyen Recurring API v68 POST /disablePermit"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Recurring/latest/post/disablePermit"
raw_files:
  - "adyen/api-explorer/Recurring/latest/post/disablePermit/2026-09-15.md"
tags: [adyen, recurring-api, permit, tokenization]
---

## Overview

This 2026-09-15 Recurring API **v68** reference describes `POST /disablePermit`: disabling a permit previously linked to a `recurringDetailReference`. It is a permit operation in [[adyen]]'s recurring/token context, routed through [[adyen-tokenization]], rather than a payment authorization or a general stored-method deletion. The captured server is `https://pal-test.adyen.com/pal/servlet/Recurring/v68`; `latest` in the page URL does not establish a later version or live access.

## Key takeaways

- The request table marks `merchantAccount` and the **permit `token` to disable** as required properties (raw lines 12–18). It does not separately mark the whole request body required. The page does not request a `recurringDetailReference` field; that reference describes the permit's prior linkage (lines 5–18).
- The `200 Success` section says the request succeeded and lists optional `pspReference` (a reference associated with the request) and optional `status` (status of the disable request) (lines 20–29). It does not define `status` values, effective disable timing, propagation to other systems, or a payment result. The response PSP reference is not the permit token.
- Error categories are 400 request reading/understanding, 401 authentication, 403 permissions, 422 request validation, and 500 server processing. Their response fields are optional in the captured tables (lines 32–99).

## Detail locators

- Purpose and v68 test server: raw lines 5–10.
- Request properties and response acknowledgement: raw lines 12–29.
- Complete error tables: raw lines 32–99.

## Related

- [[adyen-tokenization]] — provider concept and recurring-token context.

## Raw Sources

- [[raw/adyen/api-explorer/Recurring/latest/post/disablePermit/2026-09-15|Recurring API POST /disablePermit reference, captured 2026-09-15]]
