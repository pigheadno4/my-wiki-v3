---
title: "Stripe — Dispute Reason Code Categories"
type: source
date_ingested: 2026-05-09
original_format: webpage
raw_files:
  - "stripe-disputes-categories-2026.md"
tags: [stripe, disputes, chargebacks, dispute-categories, reason-codes, evidence, visa, mastercard, amex, discover, klarna, paypal, cash-app-pay]
---

## Summary

Stripe organizes all payment method dispute reason codes into 8 standardized categories. Provides evidence guidelines per category and product type (physical / digital / offline service). Covers Visa, Mastercard, Amex, Discover, Klarna, PayPal, and Cash App Pay.

## 8 Stripe Dispute Categories

| Category | What it means | Visa-only? |
| --- | --- | --- |
| `credit_not_processed` | Customer entitled to refund but hasn't received it | No |
| `duplicate` | Duplicate charge or paid by other means | No |
| `fraudulent` | Unauthorized transaction / fraud | No |
| `general` | Authorization issues, technical errors, other | No |
| `product_not_received` | Goods/services not delivered | No |
| `product_unacceptable` | Not as described, defective, counterfeit | No |
| `subscription_canceled` | Recurring billing after cancellation | No |
| `unrecognized` | Cardholder doesn't recognize the charge | No |
| `noncompliant` | Transaction doesn't conform to Visa network rules (C0xx codes) | Visa only |

## Payment Method Coverage

| Payment Method | Categories covered |
| --- | --- |
| Visa | All 8 + Noncompliant (C0xx codes) |
| Mastercard | All 8 (no Noncompliant) |
| American Express | All 8 (no Noncompliant) |
| Discover | 6 of 8 (no Product unacceptable, no Unrecognized) |
| Klarna | 6 of 8 |
| PayPal | All 8 |
| Cash App Pay | 6 of 8 |

## Evidence by Product Type

Evidence requirements differ by product type:

| Product type | Key differences |
| --- | --- |
| Physical product | Shipping/tracking proof; proof of delivery; customer in possession of item |
| Digital product/service | Usage logs, login records, download confirmation; no shipping data |
| Offline service | Cancellation policy critical; evidence of advance purchase terms |

## Key API Evidence Fields

| Field | Used for |
| --- | --- |
| `refund_policy` | Text/screenshot of refund policy |
| `refund_policy_disclosure` | How/where policy was shown to customer |
| `refund_refusal_explanation` | Why customer isn't entitled to refund |
| `cancellation_policy` | Text of cancellation terms |
| `cancellation_policy_disclosure` | How/where cancellation terms were shown |
| `cancellation_rebuttal` | Why customer isn't entitled to cancellation |
| `customer_communication` | Screenshots/PDFs of communication with customer |
| `uncategorized_text` / `uncategorized_file` | General supporting argument or document |
| `shipping_carrier`, `shipping_tracking_number` | Physical delivery proof |
| `customer_name`, `billing_address`, `shipping_address` | Required for Visa CE 3.0 (pre-populated by Stripe if eligible) |

## Fraudulent Dispute Evidence (Visa CE 3.0 — code 10.4)

Stripe pre-populates required CE 3.0 fields if eligible. Do not edit pre-populated fields. Key required fields: `customer_name`, `billing_address`, `shipping_address`, `shipping_carrier`, `shipping_tracking_number`. For liability shift disputes, Stripe auto-populates ECI and 3DS data.

## Prevention Guidance by Category

- **Credit not processed**: clear refund/cancellation policy disclosed before purchase; honor promptly
- **Duplicate**: idempotency keys; check for recent payments before retrying
- **Fraudulent**: collect billing address + CVC; use 3DS; Radar fraud rules
- **Product not received**: tracking numbers; delivery confirmation; realistic delivery timelines
- **Product unacceptable**: accurate product descriptions; quality control
- **Subscription canceled**: clear cancellation flow; honor cancellations promptly; send confirmation
- **Unrecognized**: clear statement descriptor; send purchase receipts

## Related Pages

- [[disputes]] — concept page (updated with category framework)
- [[source-stripe-disputes-responding]] — evidence submission process
- [[source-stripe-disputes-how-disputes-work]] — full dispute lifecycle
- [[stripe-3d-secure]] — 3DS liability shift for fraudulent disputes

## Raw Sources

- [[stripe-disputes-categories-2026]] — verbatim Stripe dispute categories + evidence guidelines (1009 lines)
