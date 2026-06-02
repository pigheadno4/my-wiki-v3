---
title: "PayPal Expanded Checkout: Chargeback Protection"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-expanded-checkout-chargeback-protection.md"
  - "paypal-expanded-checkout-chargeback-protection-integrate.md"
tags: [paypal, expanded-checkout, chargeback-protection, chargebacks, fraud-protection, risk-management, disputes]
---

## PayPal Expanded Checkout: Chargeback Protection

Overview of PayPal's Chargeback Protection Tool — a distinct alternative to FPA that waives eligible chargeback fees and removes holds on disputed amounts in exchange for providing delivery evidence.

Source URL: <https://developer.paypal.com/docs/checkout/advanced/customize/chargeback-protection/>

Last updated: 2025-10-28

## Key Takeaways

### What it is

The Chargeback Protection Tool uses PayPal's ML fraud analysis to approve/decline transactions in real time. Unlike FPA, the merchant does **not** control filters or review queued transactions — all decisions are automated. In exchange, PayPal waives eligible chargeback fees and removes holds on disputed amounts when the merchant can prove delivery.

### Eligibility

- PayPal business account required
- Requires existing Expanded Checkout (ACDC) integration
- Available in: **US, CA, AU, MX, FR, IT, ES, UK, DE** (9 countries)

### Mutual exclusivity with FPA

> When you use Fraud Protection tools, you must deactivate the Chargeback Protection Tool.

FPA and Chargeback Protection **cannot be used simultaneously**.

### FPA vs Chargeback Protection — feature comparison

| Feature | FPA | Chargeback Protection |
| ------- | --- | --------------------- |
| ML fraud detection | Yes | Yes |
| Premade fraud filters | Yes | No |
| Custom fraud filters | Yes | No |
| Block/allow lists | Yes | No |
| Manual review queue | Yes | No |
| Eligible chargeback fees waived | No | Yes |
| Holds removed on disputed amount | No | Yes |
| Evidence required for unauthorized chargebacks | N/A | Yes (proof of delivery/shipment) |

### How it works

- All decisions happen **in real time** — no manual review, no override for declined transactions
- Low-risk → payment processed; high-risk → payment declined (no bypass option)
- Declined transactions appear on Transaction Details page but cannot be reviewed or overridden

### Chargeback handling

When a chargeback case opens:

1. PayPal notifies the merchant
2. Merchant submits evidence (proof of delivery/shipment) via:
   - Disputes API (`/v1/customer/disputes`)
   - PayPal Resolution Center
3. PayPal waives fees and resolves dispute up to the **monthly loss cap**

Note: Acquiring bank and card network chargeback fees are **not** waived — only PayPal's fees.

### Activation

Two paths (same as FPA activation):

1. Business Tools → Manage Risk → Fraud Tools → select Chargeback Protection Tool → Activate
2. Account Settings → Payment preferences → Manage fraud → Choose a fraud tool → select Chargeback Protection Tool → Activate

### Integration: mandatory API fields

**Create order:**

| Field | Priority |
| ----- | -------- |
| `payer.name` | Recommended |
| `purchase_units.shipping.address` | Mandatory (recommended for intangible goods) |

**Capture order:**

| Field | Priority |
| ----- | -------- |
| `payment_source.card.number` | Mandatory |
| `payment_source.card.name` | Mandatory |
| `payment_source.card.attributes.customer.email_address` | Mandatory |
| `payment_source.card.attributes.customer.phone` | Recommended |
| `payment_source.card.billing_address` | Mandatory |
| `PayPal-Client-Metadata-Id` header | Mandatory (device/risk ID, 1–36 chars) |

**Google Pay / Apple Pay** — fields passed through JS SDK instead of Orders API:

- Buyer credit card (DPAN + hash), cardholder name, buyer email — Mandatory
- Buyer name, buyer phone, Xclick item info — Recommended
- Buyer billing address (`address_line1` + `address_city` non-blank) — Mandatory
- Buyer shipping address — Mandatory for tangible goods, recommended for intangible
- RDA key (risk data identifier) — Mandatory
- Auto-submit evidence (shipping/tracking ID) — Recommended

### Integration: submit evidence for protected disputes

Webhook-driven flow:

1. Subscribe to `CUSTOMER.DISPUTE.CREATED` webhook → receive `dispute.id`
2. Retrieve dispute details; check `response.adjudications.reason.PROTECTION_POLICY_APPLIES` to confirm coverage
3. If protected, submit evidence via `request.evidence-file` path (Disputes API)

**Integration Health Dashboard**: <https://www.paypal.com/cbp-tool-dashboard/integration>

## Raw Sources

- [[paypal-expanded-checkout-chargeback-protection]] — verbatim webpage content with FPA vs CBP comparison table, activation screenshots
- [[paypal-expanded-checkout-chargeback-protection-integrate]] — integration guide: mandatory API fields for create/capture order, Google/Apple Pay fields, evidence submission webhook flow

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-expanded-checkout]] — Expanded Checkout concept page
- [[source-paypal-expanded-checkout-fraud-protection]] — basic Fraud Protection (simpler, no-integration)
- [[source-paypal-expanded-checkout-fraud-protection-advanced]] — FPA: self-serve ML tool (mutually exclusive with Chargeback Protection)
- [[source-paypal-expanded-checkout-customize-overview]] — full customization catalog (14 features)
