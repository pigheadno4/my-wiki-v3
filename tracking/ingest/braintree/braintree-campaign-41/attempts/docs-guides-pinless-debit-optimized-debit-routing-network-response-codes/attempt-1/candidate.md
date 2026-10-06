---
title: "Braintree PINless Debit Optimized Routing Network Response Codes"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/pinless-debit/optimized-debit-routing/network-response-codes"
raw_files:
  - "braintree/docs/guides/pinless-debit/optimized-debit-routing/network-response-codes-2026-09-16.md"
tags: [braintree, pinless-debit, debit-routing, response-codes]
---

## Overview

This unversioned Braintree website reference under the PINless Debit optimized-routing route identifies network response code and text fields that some transaction objects may include. It maps raw response values for Accel, NYCE, Pulse, Star/Star Access and Maestro. [[braintree]] [[braintree-payment-methods]]

## Key takeaways

- Network response values are raw responses that the card network may return, and their meanings are network-specific.
- When present, these values can add detail about why a request was approved or declined, but they are supplemental: the processor response code is the source of truth.
- A network table label must not be treated by itself as proof of settlement, funding or final transaction success, or transferred to a different response field, API, actor, SDK version or environment. This snapshot documents the Braintree website route and does not establish those separate outcomes or scopes.

## Detail locators

- Field relationship and interpretation warning: raw lines 14-20.
- Network navigation: raw lines 23-28.
- Accel code table: raw lines 29-98.
- NYCE code table: raw lines 99-158.
- Pulse code table: raw lines 159-253.
- Star / Star Access code table: raw lines 255-360.
- Maestro code table: raw lines 361-401.

## Related

- [[braintree]]
- [[braintree-payment-methods]]

## Raw Sources

- [[raw/braintree/docs/guides/pinless-debit/optimized-debit-routing/network-response-codes-2026-09-16|Braintree PINless Debit optimized routing network response codes (2026-09-16 snapshot)]]
