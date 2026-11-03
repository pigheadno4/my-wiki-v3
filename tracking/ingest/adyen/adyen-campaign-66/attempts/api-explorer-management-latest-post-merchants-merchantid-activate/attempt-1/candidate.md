---
title: "Adyen Management API v3: Request merchant account activation"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/activate"
raw_files:
  - "adyen/api-explorer/Management/latest/post/merchants/(merchantId)/activate/2026-11-03.md"
tags: [adyen, management-api, merchant-account, activation]
---

## Overview

The captured [[adyen]] Management API v3 TEST reference documents `POST /merchants/{merchantId}/activate`, which requests activation of the merchant account identified by the path parameter. The result arrives asynchronously through a `merchant.updated` webhook. A successful request response is not itself confirmation that the account is activated. This endpoint applies when an integration requires it, such as Adyen for Platforms Manage, with access set up by an Adyen contact. See [[adyen-account-structure]] and [[adyen-api-access]].

## Key takeaways

- The sole documented input is the required string path parameter `merchantId`, the merchant account identifier. No request body, conditional input, default, rate limit, or idempotency contract is stated in this capture.
- The API credential must have the `Management API—Accounts read and write` role. The captured server is `https://management-test.adyen.com/v3`; the page does not provide a live server URL.
- A 200 means the request succeeded and can optionally return distinct `companyId` and `merchantId` fields. A 204 means the request was processed with no additional content. Neither response states the activation outcome; check the asynchronous `merchant.updated` result. Once the merchant account is activated, the page says it can be used to accept payments and payouts. That statement does not establish any particular payment, payout, settlement, or bank receipt.
- This page does not state deletion, reversal, propagation time, further review/approval stages, or current account eligibility. Its `latest` URL and 2026-11-03 capture do not establish present availability.

## Detail locators

- Purpose, asynchronous result, integration and role prerequisites, TEST v3 server: pinned raw lines 5–18.
- Required path identity: pinned raw lines 20–25; no request-body section appears before responses at line 27.
- 200 and 204 semantics and optional IDs: pinned raw lines 27–40.
- Error cases: 400, 401, 403, 422, and 500 at pinned raw lines 43–140. The error schemas include a generic `requestId` described as essentially the same as `pspReference`; this does not imply a payment occurred.

## Related

- [[source-adyen-api-explorer-managementnotification-latest-post-merchant-updated]] — merchant update notification reference; this operation routes its activation result there.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/activate/2026-11-03|2026-11-03 pinned API Explorer snapshot]]
