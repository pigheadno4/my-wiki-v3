---
title: "DELETE /merchants/{merchantId}/payoutSettings/{payoutSettingsId} — Delete a payout setting | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/delete/merchants/(merchantId)/payoutSettings/(payoutSettingsId)"
raw_files:
  - "adyen/api-explorer/Management/latest/delete/merchants/(merchantId)/payoutSettings/(payoutSettingsId)/2026-11-03.md"
tags: [adyen, management-api, merchant-account, payout-settings]
---

## Overview

This 2026-11-03 Management API v3 reference describes `DELETE /merchants/{merchantId}/payoutSettings/{payoutSettingsId}` on the listed `https://management-test.adyen.com/v3` server. It deletes the payout setting identified by `payoutSettingsId` under the merchant account identified by `merchantId`. Both path values are required. The page says to use this endpoint when the integration requires it, such as Adyen for Platforms Manage, and that an Adyen contact sets up access. The API credential must have the `Management API—Payout account settings read and write` role. See [[adyen]] and [[adyen-account-structure]].

## Key takeaways

- The captured contract lists only the two required path parameters; it shows no query parameters or request-body fields. The merchant account ID and payout-setting ID are distinct resource identities.
- The documented success response is `204`; the page directs the caller to inspect the actual response code for request status. It specifies no success payload or returned payout-setting state.
- A successful delete response concerns the configuration request. This reference does not specify timing, reversibility, effects on pending or future payouts, recipient-bank receipt, or settlement. It gives no idempotency or conflict behavior.
- Listed failures are `400` request problem, `401` authentication required, `403` insufficient permissions, `422` validation error, and `500` server error. Their repeated response schema includes `detail`, `errorCode`, `instance`, `invalidFields`, `requestId`, `response`, `status`, `title` and `type`; consult the raw tables for requiredness and nested fields. No live server is listed in this snapshot.

## Detail locators

- Deletion purpose, Adyen-contact access and credential role: raw lines 5–13.
- TEST v3 server and required path IDs: raw lines 15–24.
- `204` success status: raw lines 26–29.
- `400`, `401`, `403`, `422`, `500` error descriptions and response schemas: raw lines 32–129.

## Related

- [[source-adyen-docs-account-manage-payout-account-details]] — Merchant payout-bank-details guidance; this separate document does not change the captured delete contract.
- [[adyen-payouts]] — Broader payout concepts and lifecycle boundaries.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/delete/merchants/(merchantId)/payoutSettings/(payoutSettingsId)/2026-11-03|Pinned Adyen payout-setting deletion reference (2026-11-03)]]
