---
title: "Currency conversion for Adyen for Platforms online payments | Adyen Docs"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/online-payments/currency-conversion"
raw_files:
  - "adyen/docs/platforms/online-payments/currency-conversion/2026-09-15.md"
tags: [adyen, platforms, online-payments, currency-conversion, foreign-exchange]
---

## Overview

This Adyen for Platforms online-payments hub introduces a limited-availability currency-conversion pilot. It says API requests can be adapted so a transaction is accepted in one currency and settled in another when a platform's user and customer use different currencies. It routes separately to payment-conversion and refund-conversion guides. The webpage was fetched 2026-09-15 and reports `last_modified` 2023-11-21; this short hub does not establish current pilot access, supported currencies, a rate or fee, request schema, a specific user's settlement setup, or a completed funds movement. [[adyen]] [[adyen-platforms]] [[adyen-currencies-and-fx]]

## Key takeaways

- The page is explicitly marked **Limited availability** and describes currency conversion as a pilot whose processes and documentation may change; interested platforms are directed to their Adyen contact.
- Its central distinction is the currency in which the customer's transaction is accepted versus the currency in which the user's transaction is settled. The hub presents modifying API requests as the route to that conversion, without supplying the fields, calculations, split allocation or eligibility conditions needed to implement it.
- The **Next steps** links separate payment and refund conversion. Use those child guides for transaction-specific instructions and qualifications; this hub alone does not prove that a refund mirrors a payment's rate or balance-account allocation.

## Detail locators

- Limited-availability pilot status and Adyen-contact route: pinned raw lines 15–20.
- Platform/user/customer and accepted-versus-settled currency framing: pinned raw lines 24–26.
- Separate payment and refund guide navigation: pinned raw lines 28–36 (`## Next steps`).

## Related

- [[adyen-currencies-and-fx]] — provider currency and FX context.
- [[source-adyen-docs-platforms-online-payments-currency-conversion-payments]] — linked child guide for payment conversion; its details are separate evidence.
- [[source-adyen-docs-platforms-online-payments-currency-conversion-refunds]] — linked child guide for refund conversion; its details are separate evidence.
- [[adyen-platforms]] — platform/user context.

## Raw Sources

- [[raw/adyen/docs/platforms/online-payments/currency-conversion/2026-09-15|Online currency-conversion hub — 2026-09-15 snapshot]]
