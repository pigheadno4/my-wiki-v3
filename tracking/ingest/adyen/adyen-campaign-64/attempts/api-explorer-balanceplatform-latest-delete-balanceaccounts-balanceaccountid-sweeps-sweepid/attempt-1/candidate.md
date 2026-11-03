---
title: "Adyen Balance Platform API v2 DELETE balance-account sweep"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/balanceAccounts/(balanceAccountId)/sweeps/(sweepId)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/delete/balanceAccounts/(balanceAccountId)/sweeps/(sweepId)/2026-11-02.md"
tags: [adyen, balance-platform, platforms, sweeps, configuration-api]
---

## Overview

This 2026-11-02 [[adyen]] Balance Platform API v2 TEST reference documents `DELETE /balanceAccounts/{balanceAccountId}/sweeps/{sweepId}`, deleting a sweep configuration for a balance account. Both path IDs are required and identify separate resources: the balance account and its sweep. The listed server is `https://balanceplatform-api-test.adyen.com/bcl/v2`; the `latest` documentation URL does not establish current version, live access or a particular account's eligibility. See [[adyen-platforms]] for the platform resource context.

## Key takeaways

- The only listed inputs are required string path parameters `balanceAccountId` and `sweepId`. The page lists no query or request-body parameters, defaults or numeric limits (raw lines 12–18).
- The success section gives HTTP `204` and says to inspect the actual response code for request status; it supplies no success response body or returned sweep state (raw lines 20–24). A successful deletion is configuration evidence. This page does not say whether already initiated sweep transfers are cancelled or reversed, whether deletion is recoverable, or when a separate webhook/readback reflects it.
- The listed errors are 400 request-reading, 401 authentication, 403 insufficient permissions, 422 validation and 500 server processing, with shared problem-response fields (raw lines 26–123). The generic 422 and 500 JSON examples concern payment-instrument changes/creation, so they do not establish sweep-specific failure conditions (raw lines 166–191). No 404 status or idempotency contract is listed.
- Removing a sweep configuration is distinct from executing a sweep transfer, booking funds, settling a payment, paying out or confirming bank receipt. The response supplies no financial outcome evidence.

## Detail locators

- Endpoint, TEST v2 server and path IDs: raw lines 5–18.
- 204 success and absence of a success body: raw lines 20–24.
- Error descriptions, schemas and generic examples: raw lines 26–191.

## Related

- [[adyen-platforms]] — balance-account sweep context.
- [[source-adyen-api-explorer-balanceplatform-latest-post-balanceaccounts-balanceaccountid-sweeps]] — separate sweep-configuration creation reference.
- [[source-adyen-api-explorer-balanceplatform-webhooks-latest-post-balanceplatform-balanceaccountsweep-deleted]] — separate deletion-event schema; event receipt is not funds-movement proof.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/delete/balanceAccounts/(balanceAccountId)/sweeps/(sweepId)/2026-11-02|DELETE balance-account sweep reference, captured 2026-11-02]]