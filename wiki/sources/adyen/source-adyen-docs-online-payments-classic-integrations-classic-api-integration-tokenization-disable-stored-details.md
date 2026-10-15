---
title: "Adyen Classic API: disable stored recurring details"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/tokenization/disable-stored-details"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/disable-stored-details/2026-09-15.md"
tags: [adyen, classic-api, recurring-payments, tokenization, stored-details, disable]
---

## Overview

This dated Classic Recurring API `/disable` guide addresses stopping reuse of previously stored payment details, including when a shopper's subscription ends. Its stated request scope is a merchant account, shopper reference, and `ONECLICK` or `RECURRING` contract, with an optional `recurringDetailReference` to select one detail. The endpoint is marked inactive and unsupported for new integrations; Adyen directs new builds to Checkout API and existing users to migration guidance. [[adyen-tokenization]] [[adyen]]

## Key takeaways

- The request prose says to include `merchantAccount`, `shopperReference`, and a contract type; provide `recurringDetailReference` to disable a particular stored detail, or omit that detail reference to disable all recurring details for the specified shopper. This is shopper-scoped, not a claim about every merchant token or another shopper's details.
- The page's example labeled as disabling **all** details conflicts with that prose: it still includes `recurringDetailReference` and omits `contract`. Treat the example as inconsistent with the stated selector rule; check the linked `/disable` API reference before applying it to a real stored-detail set.
- The `/disable` response has a string `response`: `[detail-successfully-disabled]` for one detail or `[all-details-successfully-disabled]` for all details. The documented effect is preventing new charges with those previously stored details. It does not establish a refund or reversal of prior payments, removal from the merchant's own systems, or legal erasure of all personal data.

## Detail locators

- Opening notice — inactive Classic endpoint and migration direction.
- `Request` — subscription-termination purpose, per-detail versus all-details prose, one-click example, and contradictory all-details example.
- `Response` — single-detail and all-details success strings.

## Related

- [[adyen-tokenization]] — provider tokenization concept and current integration routes.
- [[adyen]] — provider overview.

## Related raw API references

The linked `/disable` API reference and Checkout migration pages are navigation from this source, not evidence read for this entry.

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/disable-stored-details/2026-09-15|Adyen disable stored details, fetched 2026-09-15]]
