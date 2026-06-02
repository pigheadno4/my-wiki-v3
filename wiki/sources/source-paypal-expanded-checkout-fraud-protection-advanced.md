---
title: "PayPal Expanded Checkout: Fraud Protection Advanced (FPA)"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-expanded-checkout-fraud-protection-advanced.md"
  - "paypal-expanded-checkout-fpa-getting-started.md"
  - "paypal-expanded-checkout-fpa-activate.md"
  - "paypal-expanded-checkout-fpa-upgrade.md"
  - "paypal-expanded-checkout-fpa-disable.md"
  - "paypal-expanded-checkout-fpa-filters.md"
  - "paypal-expanded-checkout-fpa-lists.md"
  - "paypal-expanded-checkout-fpa-review.md"
  - "paypal-expanded-checkout-fpa-monitoring.md"
tags: [paypal, expanded-checkout, fraud-protection, fpa, risk-management, machine-learning, filters, ppcp, pricing]
---

## PayPal Expanded Checkout: Fraud Protection Advanced (FPA)

Detailed overview of Fraud Protection Advanced — PayPal's self-serve, ML-powered fraud tool for PPCP/Advanced Checkout merchants. Covers capabilities, required API fields for optimal performance, country/pricing eligibility, and the activation flow.

Source URL: <https://developer.paypal.com/docs/checkout/advanced/customize/fraud-protection/fraud-protection-advanced/>

Last updated: 2025-08-28

## Key Takeaways

### FPA vs basic Fraud Protection

| Aspect | Fraud Protection (FP) | Fraud Protection Advanced (FPA) |
| ------ | --------------------- | -------------------------------- |
| Configuration | Pre-configured out-of-the-box filters | Self-serve, fully customizable |
| Risk scoring | Not mentioned | ML risk score 0–100 |
| Filters | Basic | Custom filters + allowlists/blocklists/reviewlists |
| Manual review | No | Yes — review queue with filter context |
| Audit trail | No | Yes — full activity log |
| Pricing | Included | Per-screened-transaction fee |

### Core capabilities

- **ML risk score**: 0–100 (0 = no risk, 100 = high risk); analyzes card details, buyer info, purchasing patterns, device intelligence
- **Fraud profile identification**: initial strategies customized on historical risk patterns; continuously adjusted post-onboarding
- **Filters**: rules to approve, reject, or flag transactions — enable/adjust/create your own
- **Lists**: allowlists (trusted customers), blocklists (known bad actors), reviewlists (manual review queue)
- **Review queue**: manually approve or reject flagged transactions; shows triggering filters, timestamp, risk score
- **Activity trail**: full audit log of filter/list/case changes with user attribution

### Optimal performance: required API fields

Pass these fields in Orders v2 API requests. JS SDK integration passes Device ID and Customer IP automatically.

**Create order — header:**

| Field | Notes |
| ----- | ----- |
| `PayPal-Client-Metadata-Id` | Device ID (1–36 chars). Auto-passed by JS SDK. For API-only: integrate Fraudnet (browser) or Magnes (app), or pass directly. |

**Create order — body:**

| Field | Notes |
| ----- | ----- |
| `payment_source.card.attributes.customer.email_address` | Buyer email (3–254 chars). Required for Guest Processing; optional otherwise. |
| `payment_source.card.attributes.customer.phone` | Buyer phone; `phone.phone_number` supports `national_number` only. |
| `payment_source.card.billing_address` | Supports `address_line_1/2`, `admin_area_1/2`, `postal_code`, `country_code`. |
| `purchase_units.shipping.address` | Same fields as billing address. |
| `purchase_units.items` | Line items array. |
| `purchase_units[].supplementary_data.risk.customer.ip_address` | IPv4/IPv6 (7–39 chars). Auto-passed by JS SDK; send manually for API-only. |

**Capture order — body:**

| Field | Notes |
| ----- | ----- |
| `payment_source.card.name` | Cardholder name (1–300 chars). |
| `payment_source.card.number` | PAN (13–19 chars). |

### Pricing (per FPA-screened transaction)

35 supported markets. Selected prices:

| Country | Price |
| ------- | ----- |
| US | $0.07 USD |
| CA | $0.09 CAD |
| AU | $0.10 AUD |
| GB | £0.06 GBP |
| DE / FR / ES / IT / AT / IE / etc. | €0.06 EUR |
| SG | $0.10 SGD |
| HK | $0.60 HKD |

Full table in raw file. Available for both direct merchants and marketplaces (PPCP).

### Activation flow

Two discovery paths:

1. Business Tools → Manage Risk → Fraud Tools
2. Account Settings → Payment preferences → Manage fraud → Choose a fraud tool

Activation steps: Choose DIY → Select FPA → Set up auto bank debit → Launch dashboard.

Dashboard shows fraud metrics for the past **180 days**.

### FPA sub-pages (further reading)

After onboarding, merchants configure FPA through four areas:

- **Filters** — create and set up custom rules (approve/reject/flag)
- **Lists** — manage allowlists, blocklists, and reviewlists
- **Review** — manually approve/reject queued transactions
- **Monitoring** — track FPA activity and audit trail

Two onboarding paths exist:

- **Activate** — net-new merchants who have never used FPA
- **Upgrade** — merchants on basic Fraud Protection Standard upgrading to FPA

## Raw Sources

- [[paypal-expanded-checkout-fraud-protection-advanced]] — verbatim webpage content with full API field table, pricing table, and dashboard screenshots
- [[paypal-expanded-checkout-fpa-getting-started]] — navigation/index page listing FPA sub-pages (activate, upgrade, filters, lists, review, monitoring)
- [[paypal-expanded-checkout-fpa-activate]] — step-by-step activation walkthrough for direct merchants via Business Tools or Account Settings; includes comparison chart note (FP vs FPA vs Chargeback Protection)
- [[paypal-expanded-checkout-fpa-upgrade]] — upgrade flow from basic Fraud Protection to FPA via Account Settings → Change fraud tool
- [[paypal-expanded-checkout-fpa-disable]] — disable FPA flow: account icon → Disable FPA → confirm; warning: leaves account with NO fraud protection
- [[paypal-expanded-checkout-fpa-filters]] — filters setup: create (Add Filter → name/description/conditions → Test+Save), enable (pencil → toggle On → Save), edit; decision labels: Approve/Reject/Review; all recommendations disabled by default
- [[paypal-expanded-checkout-fpa-lists]] — lists management: 11 default attributes (Billing/Shipping Country/ZIP/Address, Card Hash, Email, Email Domain, Phone, Cardholder Name); add via CSV or comma-separated; adding to list does NOT auto-wire filter — must create filter separately
- [[paypal-expanded-checkout-fpa-review]] — review queue: select Transaction ID → review details → Submit decision; 30-day review window per transaction
- [[paypal-expanded-checkout-fpa-monitoring]] — Activity tab: full audit log of filter/list/case review changes with user attribution; expand icon for detail; Advanced Search for targeted audit queries

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-expanded-checkout]] — Expanded Checkout concept page
- [[source-paypal-expanded-checkout-fraud-protection]] — basic Fraud Protection (simpler, no-integration version)
- [[source-paypal-expanded-checkout-customize-overview]] — full customization catalog (14 features)
