---
title: "Adyen Foreign Exchange API v1 overview"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/foreignexchange/latest/overview"
raw_files:
  - "adyen/api-explorer/foreignexchange/latest/overview/2026-09-15.md"
tags: [adyen, foreign-exchange, currencies, api-reference]
---

## Overview

Captured Foreign Exchange API **v1** overview. It says the API manages and converts currencies enabled for an integration and catalogs `POST /rates/calculate` as an amount-calculation endpoint. This page gives authentication and endpoint routes, not that operation's request/response contract, an executable quote, or a completed currency conversion. See [[adyen]] and [[adyen-currencies-and-fx]].

## Key takeaways

- The page recommends API-key authentication via `X-API-Key`; for Issuing, it directs key generation in Balance Platform Customer Area. For `rates/calculate`, it specifies a credential of format `ws@BalancePlatform.[YourBalancePlatform]`. A live key must be generated in the relevant live Customer Area.
- The server list gives test `https://balanceplatform-api-test.adyen.com/fx/api/v1` and live `https://balanceplatform-api-live.adyen.com/fx/api/v1`. Other prose instead uses `/fx/v1`, and its going-live sentence directs use of a **test** host after generating a live key. These captured URL conflicts need resolution against the operation contract and current Adyen configuration before use; the overview alone cannot settle the correct live endpoint.
- The single endpoint table is navigation. It does not define required request fields, rate validity, amount units, eligibility, idempotency, error schema, execution, or a financial outcome. `latest` in the documentation URL does not change the captured v1 label.

## Detail locators

- Raw `Authentication`, `Credential format`, and `Header format`: key source and header example.
- Raw `Versioning`, `Going live`, and `## Servers`: conflicting versioned path and environment text.
- Raw `## Endpoints` / `### General`: `POST /rates/calculate` route only.

## Related raw API references

- The endpoint catalog names `POST /rates/calculate`; inspect its separate raw contract for method-specific fields and response behavior.

## Raw Sources

- [[raw/adyen/api-explorer/foreignexchange/latest/overview/2026-09-15|Foreign Exchange API v1 overview (2026-09-15 capture)]]
