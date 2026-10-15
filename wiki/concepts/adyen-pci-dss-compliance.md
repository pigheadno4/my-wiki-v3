---
title: "Adyen PCI DSS Compliance"
type: concept
category: technology
tags: [adyen, pci-dss, cardholder-data, saq]
---

## Overview

Adyen's PCI DSS guidance maps merchant validation and cardholder-data responsibilities by integration type. Its 2026-09-15 PCI DSS v4.0.1 snapshot says Adyen's encrypted solutions can reduce merchant scope, but merchants retain responsibility before card data reaches Adyen and are not relieved of PCI scope. Adyen's SAQ/document routes are based on its risk profile and may differ from another acquirer's; the guide directs merchants to their acquirer or a Qualified Security Assessor for clarification. This source is guidance, not proof that a merchant integration is compliant.

## Sources

- [[source-adyen-docs-development-resources-pci-dss-compliance-guide-vulnerability-scanning-regulation]] — 2026-09-15 PCI DSS v4.0.1 SAQ A ecommerce vulnerability-scan cadence, Adyen-page/Platforms scope, ASV and passing-scan report process; scan passage is not SAQ eligibility or overall compliance proof.


- [[source-adyen-docs-development-resources-pci-dss-compliance-guide-pci-with-qsa]] — 2020-modified Level 1 QSA/ISA assessment and QSA gap/onsite/RoC/AoC sequence, including submit-AoC-only warning (2026-09-15 snapshot).


- [[source-adyen-docs-development-resources-pci-dss-compliance-guide-merchant-levels]] — 2020-modified Adyen PCI merchant-level and validation table, scoped by annual transactions per acquiring region and scheme, with assessor, AoC/RoC handling, and conditional scan guidance (collected 2026-09-15).


- [[source-adyen-docs-development-resources-pci-dss-compliance-guide-saq-a-eligibility]] — 2026-09-15 Adyen PCI DSS v4.0.1 online-payments guide to SAQ A eligibility, remaining merchant script/scanning duties, and the limited removal of requirements 6.4.3 and 11.6.1.


- [[source-adyen-docs-development-resources-security-integration-security]] — 2026-09-15 general Adyen online/POS integration-security guidance for merchant-controlled web pages, third-party scripts, terminal tampering checks, and conditional P2PE manual duties; guidance only.


- [[source-adyen-docs-development-resources-e2ee-p2pe-comparison]] — 2026-09-15 Adyen POS-terminal E2EE/P2PE comparison for encryption coverage, device lists, PCI validation and merchant manual duties; V240m versus V240m Plus device-list conflict remains unresolved and SAQ statements are not merchant compliance proof.


- [[source-adyen-docs-online-payments-pci-dss-compliance]] — 2026-09-15 online-payments PCI DSS v4.0.1 signpost for merchant responsibility, conditional SAQ A quarterly scanning, conditional non-SAQ A script-security measures, and the full-guide routes.


- [[source-adyen-docs-development-resources-pci-dss-compliance-guide-script-security]] — Adyen PCI DSS v4.0.1 Web payment-page script-security guidance (webpage snapshot, 2026-09-15) for SAQ D/AoC and partner contexts, CSP/SRI inventory and alerting recommendations, and SAQ A exclusion.


- [[source-adyen-docs-development-resources-pci-dss-compliance-guide]] — Adyen PCI DSS v4.0.1 guide for web, mobile, and in-person integration-specific merchant responsibilities and validation paths (webpage snapshot, 2026-09-15).
