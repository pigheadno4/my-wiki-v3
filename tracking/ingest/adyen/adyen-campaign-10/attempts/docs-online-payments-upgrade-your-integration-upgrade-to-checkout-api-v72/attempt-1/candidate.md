---
title: "Adyen Checkout API v72 request-value upgrade checks"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/upgrade-your-integration/upgrade-to-checkout-api-v72"
raw_files:
  - "adyen/docs/online-payments/upgrade-your-integration/upgrade-to-checkout-api-v72/2026-09-15.md"
tags: [adyen, online-payments, checkout-api, api-version, migration, validation]
---

## Overview

This 2026-09-15 Adyen guide is a **Checkout API v72 request-value validation checklist** for an online-payments integration using Checkout API. It says v72 introduces validation of values sent in API requests, so an upgrader must check the listed parameter values. The page does not name v71 as its only starting version, prescribe SDK-family migration steps, enumerate response error codes/actions, or prove a particular integration has upgraded or processed a payment successfully.

## Requirements and material checks

- The requirements table scopes the guide to an online-payments Checkout API integration. It lists the **Checkout webservice role** for the API credential and either **Merchant admin role** or **Manage API credentials** for the Customer Area user. These stated access prerequisites are not proof that an account has the roles or that a live request succeeds. See `Requirements`.
- `Validate the data that you send` lists exact per-parameter constraints. Examples include `captureDelayHours` at most **672** (28 days), `reference` at most **80** characters, `metadata` keys at most **20** and values at most **80** characters, and `returnUrl` in RFC 2396 format at most **1024** characters with required URL encoding for spaces/special letters. The table also covers address fields, `entityType`, `shopperEmail`, names, IP, social-security number and telephone number. Use the exact row in the raw snapshot for any implementation or validation decision.
- The `dateOfBirth` row states ISO-8601 date format `YYYY-MM-DD`, but its example `2005-03-01` is captioned March 1, **2025**. The mismatch is internal to this snapshot; do not treat the caption as the value's true year. See line 39.

## Evidence boundary

This page gives request-value constraints, not the v72 endpoint schema, a complete migration diff from a named previous version, SDK compatibility matrix, error-response contract, or hosted/provider runtime proof. Validation of local request construction cannot establish authorization, capture, webhook delivery, or live success. Related API-library or platform guides need their own evidence for those claims.

## Detail locators

- `Requirements`, lines 21–28: integration and role table.
- `Validate the data that you send`, lines 30–57: exact field lengths, formats, enum values and email rules; read the relevant row rather than assuming a constraint applies to another field.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-online-payments-upgrade-your-integration]]

## Raw Sources

- [[raw/adyen/docs/online-payments/upgrade-your-integration/upgrade-to-checkout-api-v72/2026-09-15|Adyen Checkout API v72 upgrade checks, 2026-09-15 snapshot]]
