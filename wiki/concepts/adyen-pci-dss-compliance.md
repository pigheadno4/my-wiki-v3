---
title: "Adyen PCI DSS Compliance"
type: concept
category: technology
tags: [adyen, pci-dss, cardholder-data, saq]
---

## Overview

Adyen's PCI DSS guidance maps merchant validation and cardholder-data responsibilities by integration type. Its 2026-09-15 PCI DSS v4.0.1 snapshot says Adyen's encrypted solutions can reduce merchant scope, but merchants retain responsibility before card data reaches Adyen and are not relieved of PCI scope. Adyen's SAQ/document routes are based on its risk profile and may differ from another acquirer's; the guide directs merchants to their acquirer or a Qualified Security Assessor for clarification. This source is guidance, not proof that a merchant integration is compliant.

## Sources

- [[source-adyen-docs-online-payments-pci-dss-compliance]] — 2026-09-15 online-payments PCI DSS v4.0.1 signpost for merchant responsibility, conditional SAQ A quarterly scanning, conditional non-SAQ A script-security measures, and the full-guide routes.


- [[source-adyen-docs-development-resources-pci-dss-compliance-guide-script-security]] — Adyen PCI DSS v4.0.1 Web payment-page script-security guidance (webpage snapshot, 2026-09-15) for SAQ D/AoC and partner contexts, CSP/SRI inventory and alerting recommendations, and SAQ A exclusion.


- [[source-adyen-docs-development-resources-pci-dss-compliance-guide]] — Adyen PCI DSS v4.0.1 guide for web, mobile, and in-person integration-specific merchant responsibilities and validation paths (webpage snapshot, 2026-09-15).
