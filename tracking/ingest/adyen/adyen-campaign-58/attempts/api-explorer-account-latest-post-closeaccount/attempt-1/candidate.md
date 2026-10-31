---
title: "Adyen Account API: POST /closeAccount"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Account/latest/post/closeAccount"
raw_files:
  - "adyen/api-explorer/Account/latest/post/closeAccount/2026-09-15.md"
tags: [adyen, classic-platforms, account-api, account-closure]
---

## Overview

This 2026-09-15 capture of the Adyen Account API Explorer documents `POST /closeAccount` against the listed TEST Account v6 server. It closes the Classic Platforms account identified by `accountCode`. This is an account operation, not an account-holder or newer balance-account operation. See [[adyen]] and [[adyen-classic-platforms]].

## Key takeaways

- A closed account cannot process transactions, pay out its funds, or be reopened. Payments made to it are sent to the platform's liable account instead.
- The request body lists `accountCode` (string) as required. The page does not state a balance-empty prerequisite, a closure reversal, or a live-environment endpoint.
- HTTP 200 says the request succeeded; HTTP 202 says it was accepted for processing but processing was not complete. Do not treat a 202 as completed closure or proof of any payout or movement of funds. Both response schemas list `accountCode`, `invalidFields`, `pspReference`, `resultCode`, and `status` as optional; `status` permits `Active`, `Inactive`, `Suspended`, or `Closed`.
- Listed error classes are 400 (request reading/understanding), 401 (authentication), 403 (permissions), 422 (validation), and 500 (server processing). The response examples show generic 400 and 403 payloads, not closure-specific recovery rules.

## Detail locators

- Endpoint, irreversible effects, liable-account routing: raw lines 5–10.
- Required request field and example: raw lines 12–26.
- 200 and 202 response meanings and optional fields: raw lines 27–64.
- Error response classes and schemas: raw lines 67–129; generic examples: lines 131–155.

## Related

- [[adyen-classic-platforms]] — older platform account model and source routes.

## Raw Sources

- [[raw/adyen/api-explorer/Account/latest/post/closeAccount/2026-09-15|Account API Explorer POST /closeAccount capture]]
