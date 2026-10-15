---
title: "Protecting your Adyen integration"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/security/integration-security"
raw_files:
  - "adyen/docs/development-resources/security/integration-security/2026-09-15.md"
tags: [adyen, integration-security, online-payments, point-of-sale, pci-dss]
---

## Overview

This 2026-09-15 snapshot of Adyen's integration-security page gives **general guidance** for both online and in-person payment integrations. It explicitly says the page is neither a complete security-measures list nor definitive advice. It does not assess a particular merchant's controls or prove PCI compliance or payment safety. See [[adyen]] and [[adyen-pci-dss-compliance]].

## Key takeaways

- For online payments, Adyen says flaws in merchant checkout/payment pages are a common attack route and that security of the merchant's own pages and apps is the merchant's responsibility, because Adyen has limited control in those environments. It directs readers to separate PCI DSS and identity/access guidance. Vulnerable third-party scripts can expose card data; the page points to separate ecommerce script-security recommendations under PCI DSS v4.0.1.
- For in-person payments, the page focuses on physical terminal tampering and terminal replacement. It recommends an inventory of active/inactive terminals, prompt software updates, monitored placement, planned/verified maintenance access, and PIN-observation safeguards. It says terminals **must** be inspected on receipt and at regular intervals.
- If using Adyen's P2PE solution, the page says to follow its advice **and** all requirements in the P2PE Instruction Manual. That conditional rule does not establish that a given merchant uses P2PE or meets its requirements.
- This page links to IP allowlisting and E2EE/P2PE comparison and points to PCI resources; it does not itself define transport TLS, Adyen API-key handling, webhook HMAC verification, audit evidence, or a merchant-specific compliance assessment. Consult those separate routes for their own scope and current requirements.

## Detail locators

- Purpose, guidance-only boundary and both online/POS applicability: lines 15–29.
- Merchant-controlled online pages/apps and linked PCI/IAM responsibilities: `Protect your online payments integration`, lines 31–36.
- Third-party script risk and PCI DSS v4.0.1 script-security route: lines 38–42.
- In-person tampering/replacement, inventory, and updates: `Protect your in-person payments integration`, lines 44–50.
- Terminal monitoring, inspection schedule, maintenance identity, and PIN protection: lines 52–63.
- Conditional P2PE Instruction Manual requirement: lines 65–67.
- Further navigation only: `See also`, lines 69–73.

## Related

- [[adyen-pci-dss-compliance]] — merchant integration and PCI scope.
- [[source-adyen-docs-development-resources-security-api-security]] — separate API authentication, transport, rate-limit, and security-testing guidance.

## Raw Sources

- [[raw/adyen/docs/development-resources/security/integration-security/2026-09-15|Protecting your Adyen integration (2026-09-15)]]
