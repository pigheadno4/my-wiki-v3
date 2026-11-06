---
title: "Adyen Open Banking account verification report retrieval"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/open-banking/latest/get/accountVerification/reports/(code)"
raw_files:
  - "adyen/api-explorer/open-banking/latest/get/accountVerification/reports/(code)/2026-11-07.md"
tags: [adyen, open-banking, account-verification, bank-accounts]
---

## Overview

This 2026-11-07-captured Open Banking Gateway `latest` v1 Test/Live reference documents `GET /accountVerification/reports/{code}`. The required path `code` is received in the `redirectUrl` query after a successful open banking flow; this endpoint reads the resulting account verification report. See [[adyen]] and [[adyen-business-accounts]].

## Key takeaways

- A `200` response requires report `id`, `country` (where the third-party individual's bank account is registered), and an `accounts` array. Each account entry requires its own `accountId`, account name/number/type, currency, identifiers object and associated parties. Regional identifier objects under `identifiers` are optional; see the raw schema and ACH, BSB, EFT and IBAN examples for detail.
- The report supplies identity and bank-account details after a successful connection. The response schema has no approval, account eligibility, payment, balance, booking, or settlement outcome field. Retrieving it does not itself open a Business Account, authorize a payout, or prove bank receipt.
- The page lists `400` malformed request, `401` invalid credential or wrong permissions, `404` missing entity, `422` validation, `429` rate limit, and `500` server error. It states no code lifetime, use count, idempotency rule, report freshness guarantee, or specific caller role.

> [!warning] Contradiction
> The response table calls `accountId` a unique bank-account identifier (raw line 33), but the ACH example repeats the same `accountId` for two entries with different account numbers and bank names (raw lines 177–200). The example does not establish that distinct bank accounts can safely be keyed by that repeated value.

## Detail locators

- Purpose, Test/Live v1 servers and redirect callback code: raw lines 5–22.
- Success response and regional identifier/party schema: raw lines 24–50.
- Error meanings and optional problem-body fields: raw lines 53–164.
- ACH, BSB, EFT and IBAN examples, including the duplicate ACH account ID: raw lines 166–325.

## Related

- [[adyen-business-accounts]] — Open Banking account-verification route.
- [[adyen]] — provider page.

## Raw Sources

- [[raw/adyen/api-explorer/open-banking/latest/get/accountVerification/reports/(code)/2026-11-07|Account verification report GET, captured 2026-11-07]]
