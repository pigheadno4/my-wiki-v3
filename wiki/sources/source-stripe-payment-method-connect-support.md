---
title: "Stripe Docs — Payment method support for platforms and marketplaces"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-payment-method-connect-support-2025.md"
tags: [stripe, connect, payment-methods, platforms, marketplaces, capabilities, merchant-of-record]
---

## Summary

Comprehensive Connect-specific reference for 31 payment methods. Covers capability names, merchant of record / statement descriptor behavior by charge type, cloning rules, and notable restrictions for each PM.

## Common Pattern

Most PMs follow this pattern:
1. Request capability (e.g., `billie_payments`, `scalapay_payments`) on platform + connected accounts
2. Descriptor source depends on charge type: Direct → connected account; Destination/Separate → platform; with `on_behalf_of` → connected account

## Notable PM-Specific Connect Rules

| PM | Key Connect Restriction |
| --- | --- |
| **ACH Direct Debit** | Mandate cloning supported; app fee auto-refunded on failed destination charges; settlement control by account type |
| **Alipay** | Direct + `on_behalf_of` private preview only |
| **Alma** | Online marketplaces only (not platforms like Shopify/Squarespace); Destination + Separate charges only; requires Dashboard onboarding request |
| **Bank transfers** | `on_behalf_of` not supported |
| **Cash App Pay** | Cannot clone PMs across connected accounts when connected account is business of record |
| **iDEAL** | Connected account name must map to actual business (regulatory compliance) |
| **Indonesian bank transfers** | `on_behalf_of` not supported; no cross-border flows (e.g., Indonesian platform + non-Indonesian connected account) |
| **PayPal** | Online marketplaces only (Destination + Separate charges); no Direct or `on_behalf_of`; requires Dashboard onboarding request |
| **Pix** | Eligibility determined by MoR's country — charge type determines whether platform or connected account is MoR |
| **WeChat Pay** | Direct + `on_behalf_of` private preview only |

## Capability Name Reference

| PM | Capability |
| --- | --- |
| ACH Direct Debit | `us_bank_account_ach_payments` |
| Affirm | `affirm_payments` |
| Alipay | `alipay_payments` |
| Billie | `billie_payments` |
| BLIK | `blik_payments` |
| Cash App Pay | `cashapp_payments` |
| Klarna | `klarna_payments` |
| Kriya | `kriya_payments` |
| MB WAY | `mb_way_payments` |
| MobilePay | `mobilepay_payments` |
| Mondu | `mondu_payments` |
| Multibanco | `multibanco_payments` |
| Pay by Bank | `pay_by_bank_payments` |
| PayNow | `paynow_payments` |
| PayTo | `payto_payments` |
| Pix | `pix_payments` |
| Scalapay | `scalapay_payments` |
| SEPA Direct Debit | `sepa_debit_payments` |
| SeQura | `sequra_payments` |
| Sunbit | `sunbit_payments` |
| TWINT | `twint_payments` |
| WeChat Pay | `wechat_pay_payments` |

## Related Pages

- [[stripe-payment-methods]] — payment methods concept page
- [[source-stripe-payment-method-support]] — product + API support matrices (non-Connect)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-payment-method-connect-support-2025]] — verbatim webpage content (518 lines)
