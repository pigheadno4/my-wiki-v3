---
title: "Adyen Balance Control API v1 overview"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/BalanceControlv1/latest/overview"
raw_files:
  - "adyen/api-explorer/BalanceControlv1/latest/overview/2026-09-15.md"
tags: [adyen, balance-control, api-explorer, merchant-accounts, transfers]
---

## Overview

This 2026-09-15 API Explorer overview identifies **Adyen Balance Control API v1** as an API for transferring funds between merchant accounts that belong to the same legal entity and the same company account. It lists `POST /balanceTransfer` as the operation to start a balance transfer. This is a merchant-account Balance Control route, distinct from Adyen for Platforms balance-account Transfers API routes. [[adyen]] [[adyen-account-structure]]

## Key takeaways

- Requests must authenticate with either an API key or basic-auth username and password. The page shows an illustrative `X-API-Key` header and says API credentials must be generated for live endpoints; it does not name a credential role or define a complete authorization policy. See raw lines 9–18.
- The overview says the API uses a `vXX` suffix in endpoint URLs, and explicitly shows the TEST base `https://pal-test.adyen.com/pal/servlet/BalanceControl/v1` and `.../v1/balanceTransfer` example. The page title states v1; the URL's `latest` segment is a documentation route, not an additional version. See raw lines 20–29.
- The endpoint table only says `POST /balanceTransfer` “Start a balance transfer.” It supplies no request/response schema, merchant-account identifier fields, currency or amount requirements, limits, execution or booking status, failure/reversal behavior, timing, idempotency/correlation, asynchronous outcome, or deprecation rule. This overview alone cannot establish transfer completion, source/destination balance changes, settlement, or bank receipt. See raw lines 31–36.

## Detail locators

- Product purpose and same-entity/company scope: raw lines 5–7.
- Authentication and live-credential qualification: raw lines 9–18.
- Versioning and TEST URL: raw lines 20–29.
- Endpoint list: raw lines 31–36.

## Related

- [[adyen-account-structure]] — merchant/company account hierarchy and reciprocal source route.

## Raw Sources

- [[raw/adyen/api-explorer/BalanceControlv1/latest/overview/2026-09-15|Adyen Balance Control API v1 overview raw snapshot]]
