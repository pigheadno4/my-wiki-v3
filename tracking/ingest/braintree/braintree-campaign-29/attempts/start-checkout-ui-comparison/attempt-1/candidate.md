---
title: "Braintree Checkout UI Comparison"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/start/checkout-ui-comparison"
raw_files:
  - "braintree/docs/start/checkout-ui-comparison-2026-09-16.md"
tags: [braintree, checkout-ui, drop-in, hosted-fields, mobile-sdk]
---

## Overview

This 2026-09-16 Braintree website snapshot is a selection-oriented comparison between the ready-made Drop-in UI and a merchant-built custom checkout UI. It compares presentation control, platform routes, PCI self-assessment wording, translations, payment-method listings and fraud-tool coverage. It is a navigation and product-selection source, not proof of current SDK support, merchant eligibility, PCI compliance, payment-method availability, successful tokenization or payment processing.

## Key takeaways

- The page presents Drop-in as Braintree's ready-made payment form with customization options, while the Custom UI path gives the merchant control over the form's colors and layout. This is a product-shape distinction, not a recommendation or a guarantee that either route fits a particular merchant.
- In the captured comparison, Drop-in covers desktop and mobile web plus iOS and Android apps. The Custom UI column identifies Hosted Fields for desktop and mobile web and mobile SDKs for native apps. These are snapshot-scoped integration routes; the page does not assign SDK versions or establish present compatibility.
- Both columns use qualified wording that they "typically" qualify for SAQ A; the Custom UI statement is conditional on Hosted Fields and mobile SDKs. This wording must not be converted into a PCI-compliance guarantee or an assessment of a merchant's implementation.
- Drop-in is described as having translations available in up to 23 languages, whereas the Custom UI path leaves translations to the merchant. The table also lists payment methods and says both paths support Basic and Premium Fraud Management Tools, but it does not establish account enablement, buyer eligibility, regional availability or successful payment execution.
- The captured payment-method row has flattened formatting around its asterisk and "Mobile only" note. Use the exact raw row for method-level comparison rather than inferring which qualifiers attach to which entries.

> [!warning] Snapshot and lifecycle boundary
> This page presents Drop-in as an available choice in a 2026-09-16 snapshot. Separately retained website and exact-version repository evidence contains conflicting Drop-in lifecycle dates. Do not use this comparison to establish current support; consult [[braintree-web-drop-in]] and verify current official status before implementation or migration planning.

## Detail locators

- Ready-made Drop-in versus custom checkout framing: `# Checkout UIs`, lines 16-18.
- Platform comparison for web and native apps: `# Checkout UIs` table, lines 20-24.
- Customizability, qualified SAQ A wording and translation responsibility: `# Checkout UIs` table, lines 25-27.
- Payment-method listings and the flattened mobile-only note: `# Checkout UIs` table, lines 28-31.
- Fraud-tool row and the Drop-in, Hosted Fields and mobile SDK navigation routes: `# Checkout UIs` table, lines 32-33. Linked guides remain navigation unless independently read.

## Related

- Company: [[braintree]]
- Prebuilt checkout concept and lifecycle boundary: [[braintree-web-drop-in]]
- Modular browser SDK and Hosted Fields boundary: [[braintree-web-sdk]]

## Raw Sources

- [[raw/braintree/docs/start/checkout-ui-comparison-2026-09-16|Braintree Checkout UIs comparison]] - complete captured comparison table and selection routes
