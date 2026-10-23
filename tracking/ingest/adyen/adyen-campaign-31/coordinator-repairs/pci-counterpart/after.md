---
title: "Adyen PCI DSS Compliance Guide"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/pci-dss-compliance-guide"
raw_files:
  - "adyen/docs/development-resources/pci-dss-compliance-guide/2026-09-15.md"
tags: [adyen, pci-dss, compliance, cardholder-data, saq]
---

## Overview

This Adyen PCI DSS v4.0.1 guidance snapshot maps Adyen web, mobile in-app, and in-person integration types to Adyen's stated merchant validation documents and security responsibilities. It is guidance, not a definitive compliance ruling: Adyen tells merchants to consult their acquirer or a Qualified Security Assessor (QSA), and its validation requirements can differ from those of other acquirers.

## Key takeaways

- The guide says PCI DSS applies to the people, processes, and technology handling cardholder data and calls compliance an ongoing process with annual validation. It directs assessments to PCI DSS v4.0.1 documents, while saying an already completed v4.0 document remains valid until expiry. These are statements in the 2026-09-15 snapshot, not a current assessment or certification.
- Encrypted Adyen integrations outsource much cardholder-data handling, but do not eliminate the merchant's PCI scope. Adyen describes its responsibility as beginning when data reaches the relevant Adyen payment interface; the merchant remains responsible for protecting the data before that point and, depending on integration, meeting storage requirements.
- For web, the guide routes Drop-in/Components/plugins and Hosted Checkout to SAQ A subject to SAQ A eligibility. Pay by Link has no PCI documentation submission required by Adyen in this guide, but the merchant must still remain compliant and Adyen may request documentation based on risk. A raw-card-data API-only integration is routed to SAQ D and quarterly Approved Scanning Vendor scans; the guide separately identifies a Custom Card Component exception routed to SAQ A. JWE client-side encryption is described as potentially eligible for SAQ A with eligibility checks despite a merchant-served form and extra controls. Do not infer that encryption alone determines a merchant's actual SAQ.
- For mobile, the guide routes Drop-in/Components to SAQ A with eligibility and raw-card-data API-only integrations to SAQ D. For in-person payments, it distinguishes E2EE, with SAQ B-IP submission to Adyen above one million annual card-present transactions, from P2PE, which calls for SAQ P2PE and implementation of the P2PE Instruction Manual. Terminal tampering remains a physical-security concern.
- Legacy Client-Side Encryption (CSE) Web integrations are being phased out: the guide says Adyen no longer develops or accepts new CSE Web integrations, directs users toward newer Web integrations, and calls for Subresource Integrity modification for PCI v4.0.1. It expressly says mobile integrations are unaffected.
- Outsourcing cardholder-data functions to service providers does not transfer the merchant's ultimate PCI responsibility. The guide calls for identifying outsourced functions, obtaining provider compliance evidence, and ongoing oversight.

> [!warning] Contradiction
> The related [[source-adyen-docs-payment-methods-cards-custom-card-integration]] ends with a broad SAQ A submission instruction across its Web and mobile tabs (its pinned raw lines 21–27, 2754–2766). This PCI guide's 2026-09-15 snapshot instead routes Web Custom Card Component through an SAQ A exception and raw-card API-only Web and mobile integrations to SAQ D; SAQ A remains subject to eligibility. The custom guide's mobile client-encryption examples are not classified by that closing sentence or explicitly mapped here. Determine the actual card-data collection architecture and SAQ eligibility, then confirm the assessment with the acquirer or a QSA. See this guide's raw lines 27, 67, 73–79, 135–155 and 213–259.

## Detail locators

- Opening through `## Ensuring compliance with PCI DSS v4.0.1` (raw lines 15–61): version guidance, non-definitive disclaimer, annual validation, Adyen/merchant responsibility boundary, and integration routes.
- `## Online payments integration` (raw lines 63–212): Adyen risk-profile qualification, web SAQ/document paths, SAQ A eligibility, Pay by Link submission distinction, raw-card API-only risk and scans, JWE qualifications, and deprecated CSE Web treatment.
- `## Mobile in-app online payments integration` (raw lines 213–266): native Drop-in/Components and raw-card API-only routes, their SAQ paths and risk controls.
- `## In-person payments integration` (raw lines 267–329): E2EE versus P2PE, annual-volume threshold for B-IP submission, P2PE manual, terminal risks, and linked references.
- `## Service Providers` (raw lines 330–354): merchant diligence, attestations, outsourced-function disclosure, and ongoing responsibility.
- `## PCI DSS Glossary` and `## See also` (raw lines 356–390): terminology and related guidance links.

## Related

- Company: [[adyen]]
- Concept: [[adyen-pci-dss-compliance]]
- Related concept: [[adyen-card-encryption]]

## Raw Sources

- [[raw/adyen/docs/development-resources/pci-dss-compliance-guide/2026-09-15|2026-09-15 Adyen PCI DSS v4.0.1 guidance snapshot]]
