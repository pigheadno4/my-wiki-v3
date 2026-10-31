---
title: "Adyen Account API v6 overview (Classic Platforms)"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Account/latest/overview"
raw_files:
  - "adyen/api-explorer/Account/latest/overview/2026-09-15.md"
tags: [adyen, classic-platforms, account-api, api-reference]
---

## Overview

This captured Account API v6 overview is an API Explorer directory for the **Classic Platforms** integration. It identifies account holders, accounts, bank accounts, shareholders and verification-related documents as account-related entities, with creation, retrieval, update and deletion operations. Adyen directs new implementations to its separate newer integration guide. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- Authentication is described as an `X-API-Key` header using an API key supplied with the API credential by an Adyen contact, or alternatively username/password basic authentication. The page says new web service user credentials are needed for live endpoints. See raw lines 13–29.
- The URL is versioned with a `vXX` suffix. The listed server and example are **TEST** at `https://cal-test.adyen.com/cal/services/Account/v6`; they do not establish a live endpoint or live access. See raw lines 31–40.
- The endpoint table lists `POST` operations for account-holder/account creation, retrieval, updates, closure and suspension, verification, document upload, and deletion of associated records. The overview supplies names and summaries, not operation request properties, response contracts, error semantics, or proof of a completed action. See raw lines 42–66 and the individual operation references.

## Detail locators

- Classic scope, newer-integration direction and entity types: raw lines 5–11.
- Authentication examples and live credential boundary: raw lines 13–29.
- Version suffix and captured TEST server: raw lines 31–40.
- Complete endpoint directory, including close/delete/state-changing operations: raw lines 42–66.

## Related

- [[adyen-classic-platforms]] — Classic account-holder and account context; keep distinct from the newer balance-platform model.
- [[source-adyen-docs-classic-platforms-api]] — Classic Platforms API reference directory.
- [[source-adyen-docs-classic-platforms-account-holders-and-accounts]] — account-holder and account onboarding flow.
- [[adyen-platforms]] — separate newer integration model.

## Raw Sources

- [[raw/adyen/api-explorer/Account/latest/overview/2026-09-15|Account API v6 overview, captured 2026-09-15]]
