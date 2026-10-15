---
title: "Adyen SAQ A Eligibility"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/pci-dss-compliance-guide/saq-a-eligibility"
raw_files:
  - "adyen/docs/development-resources/pci-dss-compliance-guide/saq-a-eligibility/2026-09-15.md"
tags: [adyen, pci-dss, saq-a, online-payments, script-security, vulnerability-scanning]
---

## Overview

This Adyen PCI DSS v4.0.1 page explains when an **online-payments integration** may use Self-Assessment Questionnaire A (SAQ A) to attest compliance, and how the 2025 SAQ A script-security change affects that route. It is a 2026-09-15 documentation snapshot, not an assessment of a specific merchant's integration or proof of PCI validation.

## Key takeaways

- SAQ A eligibility requires confirming **both** that all payment-page and form elements delivered to the customer's browser originate only and directly from a PCI DSS-compliant third-party service provider or payment processor, **and** that the merchant site is not susceptible to script attacks affecting its ecommerce systems. This page states criteria for an online-payments integration; it does not certify that a particular site meets them.
- The page says most responsibility for those controls sits with the providers, but an SAQ A merchant still must ensure provider-loaded payment-page elements and scripts across its integrations are PCI DSS compliant and apply measures against script attacks. It names regular vulnerability scans under SAQ A requirement 11.3.2. SAQ A eligibility and questionnaire submission are separate from carrying out and passing the scan; the linked vulnerability-scanning guide covers the approved scanning vendor (ASV) and report process. No scan result is established here.
- Adyen cites its annual PCI DSS Attestation of Compliance as assurance for **Adyen's products** and routes merchants to integration-specific security measures and scanning guidance. That AoC does not attest a merchant's whole ecommerce site or replace its own validation duties.
- According to the page, PCI DSS v4.0.1 SAQ A removed requirements 6.4.3 (payment-page scripts) and 11.6.1 (change/tamper detection), effective with the new SAQ A on 2025-03-31. The page says these requirements remain applicable for merchants required to submit SAQ D or an AoC for onsite assessment. Their removal from SAQ A does not remove the SAQ A eligibility confirmations or requirement 11.3.2.

## Detail locators

- `## Requirements` / `## Eligibility requirements` — online integration scope, the two confirmations and remaining merchant script/scanning duties.
- `## How Adyen can help` — Adyen product AoC and linked integration-specific and scanning guides.
- `## Changes to the SAQ A requirements` — 2025 effective date and scope of removed requirements versus SAQ D/onsite AoC.

## Related

- Company: [[adyen]]
- Provider PCI route: [[adyen-pci-dss-compliance]]
- Broader guide: [[source-adyen-docs-development-resources-pci-dss-compliance-guide]]
- Script-security route: [[source-adyen-docs-development-resources-pci-dss-compliance-guide-script-security]]

## Related raw API references

- [[raw/adyen/docs/development-resources/pci-dss-compliance-guide/vulnerability-scanning-regulation/2026-09-15|Separate 2026-09-15 vulnerability-scanning guide — ASV scope and report process]]

## Raw Sources

- [[raw/adyen/docs/development-resources/pci-dss-compliance-guide/saq-a-eligibility/2026-09-15|2026-09-15 Adyen SAQ A eligibility snapshot]]
