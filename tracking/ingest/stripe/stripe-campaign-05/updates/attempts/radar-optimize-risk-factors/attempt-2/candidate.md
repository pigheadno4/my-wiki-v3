---
title: "Stripe — Optimize Radar Risk Factors"
type: source
date_ingested: 2026-05-10
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/radar/optimize-risk-factors"
raw_files:
  - "stripe-radar-optimize-risk-factors-2026-11-07.md"
  - "stripe-radar-optimize-risk-factors-2026.md"
tags: [stripe, radar, fraud, risk-factors, stripe-js, customer-object, radar-sessions, advanced-risk-factors]
---

## Overview

The May 10 and November 7, 2026 guides distinguish factors Stripe automatically gathers from data the merchant supplies. Payment Links, Checkout, Elements and Stripe mobile SDKs gather signals such as device information and IP address. Stripe’s recommended integrations automatically collect the listed supporting data. Direct integrations typically send it explicitly. If your integration sends too little payment data, you can add customer email, name and billing address to the Customer and client IP address, user agent and checkout URL to the PaymentIntent. Direct integrations can use Radar Sessions for advanced signals.

## Stripe’s estimated model improvement

| Data | Estimated fraud model improvement |
| --- | --- |
| Advanced risk factors, including device characteristics and activity | 36% |
| IP address | 12% |
| Customer email | 11% |
| Customer name | 3% |
| Billing address | 1% |

The estimates apply to the provider’s fraud model. The captures give no additive result or measured improvement for a specific merchant or integration.

## Integration rows

The guide labels three rows **Recommended**. The completeness cells in both dated captures are blank. The list below follows document order.

- Payment Links (**Recommended**)
- Checkout (**Recommended**)
- Elements with customer risk factors (**Recommended**)
- Direct API with Radar Sessions and customer risk factors
- Direct API with client and customer risk factors
- Direct API with client risk factors
- Direct API with customer risk factors
- Direct API with no additional risk factors

## Customer and client practices

Reuse the Customer with an associated billing address and saved payment methods so Stripe can track patterns across methods. Give the email when creating the Customer and the name when tokenizing payment information. Collect and store the shipping address on the Customer when shipping physical goods. Handle declines when manually creating a PaymentIntent and track repeated attempts when reusing it.

Both guides recommend including Stripe.js on every page of the website. Stripe instructs merchants to always load it directly from Stripe’s hosted URL and excludes local copies. The May snippet and direct-loading instruction use `https://js.stripe.com/dahlia/stripe.js`. The November snippet and direct-loading instruction use `https://js.stripe.com/endive/stripe.js`. These are dated hosted-script instructions. The captures leave the deployed script, API version and any migration requirement unverified. The guides recommend disclosing Stripe’s device and behavior collection in the merchant privacy policy.

## Charges and charge-free setup

Radar operates per Charge. PaymentIntent retries can generate multiple Charges and therefore multiple scans. When a payment method is set up for future use without a charge, Radar does not scan by default. To opt into SetupIntent scanning, enable **Use Radar on payment methods saved for future use** in [Radar settings](https://dashboard.stripe.com/settings/radar). Scanning and a successful setup or payment are separate outcomes.

## Related

- [[stripe-radar]] — Radar capabilities and risk-factor guidance
- [[source-stripe-radar-how-it-works]] — overview and plan scope
- [[source-stripe-radar-sessions]] — advanced risk-factor collection for direct integrations
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-radar-optimize-risk-factors-2026-11-07|November 7, 2026 Radar risk factors guide]] — full capture with the Endive script and direct-loading instruction.
- [[raw/stripe-radar-optimize-risk-factors-2026|May 10, 2026 Radar risk factors guide]] — full capture with the Dahlia script and direct-loading instruction.
