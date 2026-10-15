---
title: "Adyen guide to engaging a PCI Qualified Security Assessor"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/pci-dss-compliance-guide/pci-with-qsa"
raw_files:
  - "adyen/docs/development-resources/pci-dss-compliance-guide/pci-with-qsa/2026-09-15.md"
tags: [adyen, pci-dss, qsa, isa, roc, aoc]
---

## Overview

This Adyen PCI guide describes a dated **Level 1** assessment choice and the workflow for using an external Qualified Security Assessor (QSA). It says a Level 1 compliance assessment can be performed by an external QSA or the merchant's Internal Security Assessor (ISA), and suggests considering a QSA when moving from Level 2 to Level 1. The raw page says last modified 2020-02-24 and was captured 2026-09-15; it is guidance, not evidence that a merchant currently qualifies for a level or has passed an assessment. See [[adyen]] and [[adyen-pci-dss-compliance]].

## Key takeaways

- If the merchant chooses an **internal ISA** for the Level 1 assessment, the page says that person must complete PCI SSC ISA training and pass annual accreditation. If it chooses a QSA, the page points to the PCI SSC-approved assessor list. These are alternative assessor routes in this snapshot, not a claim that an unaccredited staff member can sign off compliance.
- The QSA sequence described is **gap analysis** of existing and missing controls, **on-site assessment** with interviews and technical/operational evidence, and **remediation assistance** with feedback and retesting guidance. If corrective actions were performed and reassessed during the assessment, the page says to document them as **Items Noted For Improvement (INFI)**.
- Only after the merchant meets the eligible PCI DSS requirements and the audit is complete does the QSA write the compliance status in a **Report on Compliance (RoC)**. After review/finalization, the QSA provides an **Attestation of Compliance (AoC)** summarizing the assessment. The page instructs submitting the **AoC to Adyen**, and explicitly warns **never to share the full RoC with Adyen** because it contains detailed cardholder-environment infrastructure information.
- This QSA process page does not assign a merchant to SAQ D, establish onsite-AoC or script-security applicability for a particular Web integration, or replace the separate PCI DSS v4.0.1 integration/SAQ and ecommerce script-security guides. It also does not establish a current legal or card-scheme rule, merchant eligibility, completed audit, or actual compliance.

## Detail locators

- Lines 19–27: first-time Level 1 context, QSA versus ISA choice, ISA training/accreditation and approved-QSA list.
- `## Assessment process by a QSA` steps 1–3 (lines 29–41): gap, onsite evidence/interviews, remediation/retest and conditional INFI.
- Step 4 (lines 43–47): RoC then AoC sequence, submit AoC and withhold detailed RoC from Adyen.
- Lines 49–52: navigation to general PCI DSS and merchant-level guides.

## Related

- [[adyen-pci-dss-compliance]] — provider PCI concept and reciprocal source route.
- [[source-adyen-docs-development-resources-pci-dss-compliance-guide]] — integration-specific PCI validation/SAQ guidance.
- [[source-adyen-docs-development-resources-pci-dss-compliance-guide-script-security]] — separate ecommerce script-control applicability.

## Raw Sources

- [[raw/adyen/docs/development-resources/pci-dss-compliance-guide/pci-with-qsa/2026-09-15|Engaging a Qualified Security Assessor, captured 2026-09-15]]
