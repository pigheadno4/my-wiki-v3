---
title: "Stripe — Mail Order Telephone Order (MOTO)"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-moto-2026.md"
tags: [stripe, moto, sca, exemption, pci, payment-intent, setup-intent]
---

## Summary

MOTO (mail/telephone order) payments are out-of-scope for SCA. Flag via `moto` parameter on PaymentIntent or SetupIntent. Requires Stripe to verify PCI compliance first.

## Key Points

- **SCA exemption**: MOTO is out-of-scope for Strong Customer Authentication
- **PCI compliance required**: contact Stripe support to enable; Stripe must verify PCI compliance first
- **API**: flag via `moto` parameter on PaymentIntents and SetupIntents (card payments only)
- **Bank has final say**: if bank doesn't support MOTO exemption, customer must complete payment on website

## Related Pages

- [[stripe-3d-secure]] — concept page (SCA and exemptions)
- [[stripe-payment-intents]] — PaymentIntent API

## Raw Sources

- [[stripe-moto-2026]] — verbatim MOTO guide
