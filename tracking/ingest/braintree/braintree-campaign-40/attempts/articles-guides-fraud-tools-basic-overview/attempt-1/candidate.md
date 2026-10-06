---
title: "Braintree Basic Fraud Tools Overview"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/fraud-tools/basic/overview"
raw_files:
  - "braintree/articles/guides/fraud-tools/basic/overview-2026-09-16.md"
tags: [braintree, fraud-tools, basic-fraud-tools, avs, cvv, risk-threshold-rules]
---

## Overview

This 2026-09-16 Braintree website snapshot is a brief orientation to Basic Fraud Tools: customizable rules intended to protect a merchant account against carding attacks or other fraudulent activity. It routes merchants to AVS/CVV rules and risk-threshold rules and identifies the Control Panel as the place to adjust settings and manage the page's stated rejection-override route.

## Key takeaways

- The page labels Basic Fraud Tools as available at no extra cost to all merchants, regardless of size or processing volume, and says they require no developer work to set up. These are snapshot-scoped page statements, not proof of current availability, pricing, provisioning, account enablement, or effective fraud prevention for a particular merchant.
- The tools described here are merchant-configured rules: the page routes setup to AVS/CVV and risk-threshold rules and places settings changes in the Control Panel. It does not document a default enablement state, a complete automatic decision flow, or the detailed conditions and effects of any rejection action.
- AVS and CVV rules are limited here to credit-card transactions. Risk-threshold rules are stated to apply to credit cards and certain Google Pay transactions; the page does not establish applicability to every Google Pay transaction or to other payment methods.
- The overview says merchants can override fraud rejections for certain transactions within the Control Panel, but it does not define a single universal override mechanism. Use the dedicated rule guides for operational detail: their documented controls differ by tool, and this navigation page must not broaden them.

> [!warning] Basic-only scope
> This page is not evidence for Premium Fraud Management Tools, Fraud Protection, Fraud Protection Advanced, 3D Secure, chargeback protection, liability shift, processor authorization, settlement, funding, compliance, or a successful fraud outcome.

## Detail locators

- Basic Fraud Tools identity, stated purpose, snapshot availability/fee label and no-developer-work setup statement: `# Overview`, raw line 16.
- AVS/CVV and risk-threshold setup routes, Control Panel settings and page-level rejection-override wording: `# Overview`, raw line 18.
- Credit-card-only AVS/CVV scope and credit-card/certain-Google-Pay risk-threshold scope: `# Overview > **NOTE**`, raw lines 20-21.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-fraud-tools]]
- Control surface: [[braintree-control-panel]]

## Related raw API references

- [[raw/braintree/articles/guides/fraud-tools/basic/avs-cvv-rules-2026-09-16|Braintree AVS and CVV Rules guide]] - linked navigation for AVS/CVV configuration and behavior; not read as factual evidence for this source
- [[raw/braintree/articles/guides/fraud-tools/basic/risk-threshold-rules-2026-09-16|Braintree Risk Threshold Rules guide]] - linked navigation for risk-threshold configuration and behavior; not read as factual evidence for this source
- [[raw/braintree/articles/guides/payment-methods/google-pay-2026-09-16|Braintree Google Pay guide]] - linked navigation for the qualified Google Pay fraud-tools scope; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/articles/guides/fraud-tools/basic/overview-2026-09-16|Braintree Basic Fraud Tools overview]] - complete collected snapshot covering the Basic-tools purpose, snapshot availability and setup labels, Control Panel routing, and payment-method scope
