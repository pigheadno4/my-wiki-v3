---
title: "POST /balanceAccounts — Create a balance account | Adyen Balance Platform API"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/post/balanceAccounts/2026-09-15.md"
tags: [adyen, balance-platform, balance-accounts, account-holders, api-explorer]
---

## Overview

This [[adyen]] Balance Platform API Explorer snapshot documents `POST /balanceAccounts` to create a balance account that holds funds of an associated account holder. The captured server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; the URL says `latest`, while the server path identifies `v2`. The account holder, created balance account and any separate legal entity, payment instrument or transfer instrument are distinct resources. See [[adyen-platforms]] for the platform resource context.

## Key takeaways

- The request-body table marks only `accountHolderId` required. The response table marks `accountHolderId` and the new balance-account `id` required; the account holder ID associates the two resources. The EUR, CAD, GBP and USD request/response examples illustrate payloads and do not establish live creation, enabled currencies or funded balances. [Raw: lines 14–17, 27–65, 66–84, 194–279]
- `defaultCurrencyCode` is optional, defaults to EUR, and cannot be changed after creation. The optional description and reference have maximum lengths of 300 and 150 characters. The optional `timeZone` defaults to the account holder's time zone. If metadata is later updated, omitted existing key-value pairs are deleted. [Raw: lines 18–20, 24–25]
- Optional `platformPaymentConfiguration` contains sales-day closing time and settlement delay. The closing-time field permits HH:MM with hours 00–07 and minutes 00, defaulting to 00:00. `settlementDelayDays` permits 1–20 or null, defaults to null, and requires Custom Sales Day Payout enablement; the page says to contact the account or implementation manager for enablement. This is a conditional configuration prerequisite, not a universal requirement to create an account. [Raw: lines 21–23]
- The 200 response is labeled request success; its `status` field is optional and described as active by default. The response's optional `balances` array defines amount fields, with required child fields only within an included balance object. Example zero balances do not prove later available funds, settlement or payout. [Raw: lines 66–92, 194–279]
- The page lists 400 request-reading/understanding, 401 authentication, 403 permission, 422 validation and 500 server-processing errors. The generic 422 example talks about changing a payment instrument's balanceAccountId, and the 500 example says payment-instrument creation failed. Those examples do not establish a balance-account-specific status transition or failure condition. [Raw: lines 95–192, 320–346]

## Detail locators

- Purpose, TEST v2 server and request schema: pinned raw lines 5–25.
- Request examples: lines 27–65. Success schema, including balance-field meanings and status: lines 66–92.
- Error headings and schemas: lines 95–192. Success and generic error examples: lines 194–346.

## Related

- [[adyen-platforms]] — platform account-holder and balance-account resource context.
- [[source-adyen-docs-platforms-account-structure-resources]] — account holder, balance account, legal entity and instruments as separate platform resources.
- [[adyen-business-accounts]] — separate financial product; this balance account creation reference does not itself prove an opened Business Account or payment instrument.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/post/balanceAccounts/2026-09-15|POST /balanceAccounts — captured 2026-09-15]]
