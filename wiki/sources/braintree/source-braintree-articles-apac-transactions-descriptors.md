---
title: "Braintree APAC Transaction Descriptors"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/apac/transactions/descriptors"
raw_files:
  - "braintree/articles/apac/transactions/descriptors-2026-09-16.md"
tags: [braintree, apac, transactions, descriptors, statements]
---

## Overview

This Braintree-hosted APAC-routed snapshot explains how transaction descriptors identify a purchase on a customer's statement and distinguishes soft, hard, and per-transaction dynamic descriptors. It is snapshot documentation for [[braintree]] descriptor behavior and administration, not proof of current regional or merchant-account eligibility, a bank's exact statement rendering, or successful payment execution. Use [[braintree-control-panel]] for the provider-level administration route.

## Key takeaways

- The customer's bank ultimately determines exactly how a descriptor appears. In this snapshot, a soft descriptor is shown after authorization while a charge is pending, a hard descriptor is shown permanently after the bank finalizes a settled transaction, and an API-supplied dynamic descriptor replaces both when passed with an individual transaction.
- Braintree says hard and soft descriptors were configured from information collected during the application process and routes changes through its contact path. This is account-configuration documentation, not evidence that a particular merchant has a requested descriptor or that the bank will display it unchanged.
- PayPal transaction descriptor updates use the PayPal console rather than the article's ordinary Braintree change route.
- A refund defaults to the dynamic descriptor supplied on the original transaction. This describes descriptor reuse, not refund completion or bank-posting timing.

## Detail locators

- Hard and soft descriptor fields and formatting restrictions: raw lines 33-64 under `Hard and soft descriptor requirements`.
- Dynamic merchant-name composition, lengths, characters, case, spacing, and examples: raw lines 67-85 under `Dynamic descriptor requirements` and `Merchant name`.
- Dynamic country-code handling and customer-service phone restrictions: raw lines 87-98.
- Per-transaction developer-documentation route and refund default: raw lines 100-104.

## Related

- [[braintree]]
- [[braintree-control-panel]]

## Raw Sources

- [[raw/braintree/articles/apac/transactions/descriptors-2026-09-16|Braintree APAC transaction descriptors snapshot (2026-09-16)]]
