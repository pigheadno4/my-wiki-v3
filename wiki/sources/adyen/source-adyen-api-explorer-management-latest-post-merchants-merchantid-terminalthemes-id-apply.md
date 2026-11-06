---
title: "Management API: apply a terminal theme at merchant level"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes/(id)/apply"
raw_files:
  - "adyen/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes/(id)/apply/2026-11-07.md"
tags: [adyen, management-api, android-terminals, terminal-themes]
---

## Overview

This 2026-11-07 Management API `latest` v3 TEST reference describes `POST /merchants/{merchantId}/terminalThemes/{id}/apply`. It applies the identified theme to Android terminals under the merchant account, except where a different theme is applied at store or individual-terminal level. The API credential needs the Management API - Terminal themes read and write role. See [[adyen]] and [[adyen-android-terminals]].

## Key takeaways

- Required path `merchantId` identifies the merchant account; required `id` identifies the terminal theme. The captured server is `https://management-test.adyen.com/v3`. No request body, query parameters, defaults, or limits are documented.
- The 403 example says merchant-level application requires a theme owned by the merchant account or company. This is an example-specific ownership condition, not an exhaustive permission policy.
- `200 OK` is the documented success response, without a response body or terminal-state readback. The reference supplies no propagation timing; API success alone does not verify the theme is displayed on a particular device or establish any payment outcome.

## Detail locators

- Scope, lower-level overrides, credential role, server and path identifiers: pinned raw lines 5–22.
- Success and error status labels: pinned raw lines 24–43.
- 401, 403 ownership, 404 and 500 example bodies: pinned raw lines 45–97.

## Related

- [[adyen-android-terminals]] — Android-terminal scope and other theme references.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes/(id)/apply/2026-11-07|Merchant terminal-theme apply API Explorer snapshot]]