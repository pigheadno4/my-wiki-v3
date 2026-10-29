---
title: "Adyen Scalapay overview"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/scalapay"
raw_files:
  - "adyen/docs/payment-methods/scalapay/2026-09-15.md"
tags: [adyen, scalapay, buy-now-pay-later, online-payments]
---

## Overview

This [[adyen]] overview describes Scalapay as a European buy now, pay later method that splits shopper payments into instalments. The captured table labels its flow Redirect, lists FR, IT, PT and ES with EUR, and marks selected modification features. It links to Web, iOS, Android and API-only integration routes. Use [[adyen-online-payments]] for the broader online checkout context; this overview does not supply the child routes' implementation steps or establish current merchant availability.

## Key takeaways

- **Captured scope:** The table lists France, Italy, Portugal and Spain, EUR, and a Redirect flow (raw lines 19–23). These are snapshot labels, not a guarantee that Scalapay can be enabled for a specific merchant or shopper.
- **Feature marks:** The table marks refunds, partial refunds, multiple partial refunds, separate captures, partial captures and multiple partial captures as supported; it marks recurring and chargebacks as unsupported (raw lines 21–23). Those marks do not establish a completed capture or refund for a transaction.
- **Integration chooser:** The page points to prebuilt UI routes for Web, iOS and Android, and an API-only route for a merchant-built UI on those platforms (raw lines 25–49). Consult the linked child guide for request fields, redirect return handling and payment outcome.

## Detail locators

- Method identity and purpose: pinned raw lines 15–19.
- Country, currency, flow and feature matrix: pinned raw lines 21–23.
- Web, iOS, Android and API-only guide links: pinned raw lines 25–49.

## Related

- [[adyen-online-payments]] — online payment architecture and payment-method retrieval context.
- [[source-adyen-docs-payment-methods]] — broader online payment-method catalog.

## Raw Sources

- [[raw/adyen/docs/payment-methods/scalapay/2026-09-15|Scalapay overview, captured 2026-09-15]]
