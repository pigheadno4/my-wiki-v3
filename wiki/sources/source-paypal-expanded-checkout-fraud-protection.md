---
title: "PayPal Expanded Checkout: Fraud Protection"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-expanded-checkout-fraud-protection.md"
tags: [paypal, expanded-checkout, fraud-protection, risk-management, machine-learning, chargebacks]
---

## PayPal Expanded Checkout: Fraud Protection

Overview page for PayPal's fraud protection feature — a dashboard-activated ML risk toolkit requiring no code integration beyond sending buyer contact fields.

Source URL: <https://developer.paypal.com/docs/checkout/advanced/customize/fraud-protection/>

Last updated: 2025-05-13

## Key Takeaways

### What it is

Fraud protection is a **no-integration** risk management toolkit for merchants using Expanded Checkout (advanced card payments). It uses an adaptive ML engine that monitors card transactions and learns new fraud patterns over time.

### No additional integration required

> Fraud protection is available through your PayPal business account and requires no additional onboarding or integration.

Activation is entirely through the PayPal business account dashboard — no SDK changes, no API calls.

### Capabilities

- Out-of-the-box filters tuned per business
- Simulated filter impact (test before activating)
- Real-time actionable filter recommendations
- Dashboard and visualization

### How to enable

1. Log in to [PayPal business account](https://www.paypal.com)
2. App Center → Manage Risk → Fraud Protection → Get Started
3. Select **Enable Fraud Protection**

### Optimize performance: send buyer contact data

The only integration touch point is including buyer contact fields in the Orders API payload:

- `payer.phone` — buyer's phone number
- `payer.email_address` — buyer's email

These fields are already part of the standard Orders v2 `payer` object; sending them gives the ML engine more signal.

## Raw Sources

- [[paypal-expanded-checkout-fraud-protection]] — verbatim webpage content

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-expanded-checkout]] — Expanded Checkout concept page
- [[source-paypal-expanded-checkout-customize-overview]] — full customization catalog (14 features)
