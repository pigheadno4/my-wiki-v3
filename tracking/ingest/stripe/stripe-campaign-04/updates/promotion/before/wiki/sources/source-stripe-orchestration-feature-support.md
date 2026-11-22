---
title: "Stripe — Orchestration: Supported Features"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-orchestration-feature-support-2026.md"
tags: [stripe, orchestration, multi-processor, adyen, braintree, worldpay, feature-support, private-preview]
---

## Summary

Feature support matrix for Stripe Orchestration across the three currently supported processors (Adyen, Braintree, Worldpay WPG). Documents error behavior for unsupported features and error protection opt-in.

## Error Behavior

Unsupported feature → HTTP 400 `orchestration_unsupported` (first unsupported feature included in error message).

**Error protection** (opt-in during onboarding): if feature unsupported → auto-route to Stripe instead; also applies during retries; ignored if original processor was Stripe (avoids duplicate attempt).

## Feature Support Matrix

| Feature | Adyen | Braintree | Worldpay WPG |
| --- | --- | --- | --- |
| Auto confirmation/capture | ✓ | ✓ | ✓ |
| Manual capture | ✓ | ✓ | ✓ |
| Full/partial refunds | ✓ | ✓ | ✓ |
| 3DS | ✓ | ✓ | ✓ |
| Statement descriptors | ✓ | ✓ | ✓ |
| Wallets (Apple Pay, Google Pay) | ✓ | ✓ | ✓ |
| Network tokens | ✓ | ✓ | ✗ |
| Recurring transactions | ✓ | ✓ | ✓ |

**Exceptions across all three**:
- Multicapture: unsupported
- `statement_descriptor_suffix_kanji`: unsupported
- `statement_descriptor_suffix_kana`: Adyen only
- 3DS + Apple Pay/Google Pay DPAN: unsupported; Google Pay FPAN: unsupported on Adyen
- Preemptive refund on `processing` status: submitted after payment succeeds, fails if payment fails

## Related Pages

- [[stripe-orchestration]] — concept page (updated with feature matrix)
- [[source-stripe-orchestration-retries]] — retry behavior

## Raw Sources

- [[stripe-orchestration-feature-support-2026]] — verbatim feature support guide (43 lines)
