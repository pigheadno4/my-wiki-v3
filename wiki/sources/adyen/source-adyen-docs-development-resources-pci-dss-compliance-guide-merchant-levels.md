---
title: "PCI compliance levels | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/pci-dss-compliance-guide/merchant-levels"
raw_files:
  - "adyen/docs/development-resources/pci-dss-compliance-guide/merchant-levels/2026-09-15.md"
tags: [adyen, pci-dss, merchant-levels, validation, saq, roc]
---

## Overview

This Adyen merchant-levels page was collected on 2026-09-15 but its raw metadata says last modified 2020-02-24, and its See also section links a PCI DSS v3.2.1 RoC template. It explains how its stated transaction-volume levels and an Account Data Compromise event relate to PCI DSS validation documents. Its thresholds are dated provider guidance, not a current card-scheme determination, legal conclusion, or proof that a merchant has validated or achieved compliance. See [[adyen]], [[adyen-pci-dss-compliance]], and the separate [[source-adyen-docs-development-resources-pci-dss-compliance-guide]] for the v4.0.1 guidance snapshot.

## Key takeaways

- The page says card-accepting merchants validate PCI DSS compliance annually. Its level calculation uses a 12-month transaction count **per acquiring region, per scheme**, rather than an unqualified total across all regions and schemes. It does not identify a particular merchant's level or assign scheme-specific program responsibilities.
- In this dated table, Level 1 covers more than 6 million annual transactions in that region/scheme unit or a prior breach resulting in an Account Data Compromise event. The other stated bands are Level 2 at 1–6 million, Level 3 at 20,000–1 million, and Level 4 below 20,000. The source uses 'between' at adjacent ranges without clarifying exact boundary treatment; use the raw table and current assessor/acquirer guidance before applying a threshold.
- The table marks RoC for Level 1 and RoC or SAQ for Levels 2–4. The text describes external QSA or internal security-resource assessment for an RoC; when an ISA assesses, it specifies PCI SSC ISA training and annual accreditation. For an RoC path, submit the AoC summary to Adyen and do not share the full RoC with Adyen because it contains detailed cardholder-data-environment infrastructure.
- An Approved Scanning Vendor quarterly network scan is conditional on the integration in this page. Which SAQ/RoC and scan requirements apply to a real merchant needs its integration and current acquiring/scheme context; this snapshot records guidance, not completed validation.

## Detail locators

- `## Validation requirements`: SAQ, RoC, QSA/internal assessor and ISA qualifications; AoC submission, full-RoC confidentiality, and conditional ASV scan.
- `## Determine your PCI compliance level`: four dated volume bands, ADC exception, document table, and integration-dependent scan column.
- `## See also`: related Adyen and PCI SSC links, including the v3.2.1 RoC template that dates this page's context.

## Related

- [[adyen]]
- [[adyen-pci-dss-compliance]]
- [[source-adyen-docs-development-resources-pci-dss-compliance-guide]] — separate 2026-09-15 snapshot discussing PCI DSS v4.0.1 and integration-specific merchant responsibility.

## Raw Sources

- [[raw/adyen/docs/development-resources/pci-dss-compliance-guide/merchant-levels/2026-09-15|Adyen PCI merchant levels, 2026-09-15]]
