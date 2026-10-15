---
title: "PCI DSS compliance | Adyen online payments"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/pci-dss-compliance"
raw_files:
  - "adyen/docs/online-payments/pci-dss-compliance/2026-09-15.md"
tags: [adyen, online-payments, pci-dss, saq, vulnerability-scanning, script-security]
---

## Overview

This Adyen online-payments page is a short PCI DSS v4.0.1 guidance route. It identifies cardholder-data security scope, points merchants to Adyen's fuller compliance guide, and highlights conditional ecommerce vulnerability-scanning and payment-page script-security topics. It does not determine a merchant's integration-specific SAQ or prove compliance.

## Key takeaways

- The page describes PCI DSS as applying to entities that collect, process, store, or transmit cardholder data and to entities involved in payment processing. Merchants remain responsible for the PCI DSS requirements that apply to their situation.
- For a merchant eligible to validate through SAQ A, the page says PCI DSS requires a quarterly vulnerability scan of part of the online-payments system in addition to SAQ A. Eligibility is a condition here; the page does not assign SAQ A to a particular integration.
- If a merchant is not eligible for SAQ A and certain conditions apply, the page says PCI DSS requires measures against risks from scripts and iframe elements on Web online-payment pages. It routes details to the separate script-security guide.
- The linked full compliance guide addresses requirements and documentation; this short page does not replace an integration-specific assessment or current compliance evidence.

## Detail locators

- Raw lines 15–21 — PCI DSS v4.0.1 framing, cardholder-data scope, and the full-guide route.
- Raw lines 23–29 — conditional SAQ A scanning, conditional non-SAQ A script/iframe protection, and merchant responsibility.
- `Next steps` — links to the full PCI DSS guide and dedicated vulnerability-scanning and script-security guides.

## Related

- Company: [[adyen]]
- Concept: [[adyen-pci-dss-compliance]]
- Detailed source: [[source-adyen-docs-development-resources-pci-dss-compliance-guide]]

## Raw Sources

- [[raw/adyen/docs/online-payments/pci-dss-compliance/2026-09-15|2026-09-15 snapshot — Adyen online-payments PCI DSS compliance]]
