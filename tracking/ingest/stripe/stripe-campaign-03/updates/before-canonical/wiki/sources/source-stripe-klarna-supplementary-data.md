---
title: "Stripe: Klarna Supplementary Purchase Data"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-klarna-supplementary-data-2025.md"
tags: [stripe, bnpl, klarna, supplementary-data, preview, verticals, fraud, acceptance-rates]
---

## Summary

Public preview feature for sending Klarna-specific industry vertical data to improve acceptance rates and fraud assessment. Covers 8 verticals, API parameter structure, and update semantics.

## Key Details

**Status**: Public preview — requires API version header `2025-11-17.preview`.

**Parameter**: `payment_method_options.klarna.supplementary_purchase_data` on create/update/confirm PaymentIntent.

**8 supported verticals**: events, insurance, vouchers, train, bus, ferry, organized trips/tours, marketplace sellers. (Travel — lodging/car/air — uses generic `industry-metadata` API instead.)

**Benefits**: higher acceptance rates, post-purchase transparency, fraud assessment, risk monitoring. No fee changes; no validation feedback provided.

**Update semantics**:
- Updating a vertical's array **fully replaces** it for that vertical
- Omitting a vertical in update preserves existing data
- Set vertical to `""` to unset it
- Set `supplementary_purchase_data: ""` to clear all

## Raw Sources

- [[stripe-klarna-supplementary-data-2025]] — verbatim webpage content (705 lines)
