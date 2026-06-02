---
title: "Stripe Docs — A/B testing a payment method"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-a-b-testing-payment-methods-2025.md"
tags: [stripe, a-b-testing, dynamic-payment-methods, payment-element, checkout, conversion, experimentation]
---

## Summary

Complete guide for running A/B experiments on payment methods. Dashboard-only, no code required. Requires dynamic payment methods. Covers setup, metrics, statistical methodology, raw data, and Connect support.

## Key Facts

- **Requirements**: dynamic payment methods + Payment Element Web or Checkout (payment mode); Dashboard only
- **Default split**: 50/50; 80,000 sessions → 80% power to detect 100 BPS change at 5% significance
- **Randomization**: UserAgent + IP + date (daily session aggregation to avoid double-counting)
- **Limits**: 1 experiment per configuration; no PM changes mid-experiment; auto-ends at 180 days
- **35 supported PMs** in Payment Element; 9 unsupported for Connect (ACH, ACSS, BECS, Bacs, Alipay, FPX, Konbini, SEPA, WeChat)

## Statistical Method

z-test at 5% level; primary metric = average revenue per session. Results significant when < 5% probability of being random chance. Green = significant increase, yellow = decrease, gray = insufficient sessions.

## CDN Assets

- `raw/assets/stripe-ab-test-create-experiment.png` — create experiment Dashboard UI (112 KB)
- `raw/assets/stripe-ab-test-manage-experiment.png` — manage experiment page (164 KB)
- `raw/assets/stripe-ab-test-experiment-report.png` — experiment results page (432 KB)
- `raw/assets/stripe-ab-test-gray-indicator.png` — gray insignificance badge (433 KB)
- `raw/assets/stripe-ab-test-green-indicator.png` — green significance badge (433 KB)

## Related Pages

- [[stripe-ab-testing-payment-methods]] — concept page
- [[stripe-dynamic-payment-methods]] — dynamic payment methods (prerequisite)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-a-b-testing-payment-methods-2025]] — verbatim webpage content (174 lines)
