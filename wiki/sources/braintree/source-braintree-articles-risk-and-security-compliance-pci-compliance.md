---
title: "Braintree PCI Compliance Guidance"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/risk-and-security/compliance/pci-compliance"
raw_files:
  - "braintree/articles/risk-and-security/compliance/pci-compliance-2026-09-16.md"
tags: [braintree, pci-dss, compliance, saq, securitymetrics]
---

## Overview

This collected Braintree article describes PCI DSS, the merchant's annual Self-Assessment Questionnaire (SAQ) responsibility, volume-based compliance levels, and optional SecurityMetrics assistance for eligible Braintree merchants. It is provider guidance captured from an unversioned webpage, not current legal or card-network authority, a merchant-specific assessment, or proof of PCI compliance or certification.

## Key takeaways

- The page states that PCI DSS applies to businesses that handle, process, or store credit cards regardless of size or location. It also carries a dated notice saying assessments from March 31, 2024 onward must follow PCI DSS 4.0. Treat these as Braintree's collected statements: the snapshot does not establish current law, current PCI Security Standards Council or card-brand rules, or how they apply to a particular merchant.
- The merchant must complete an SAQ annually, and the page says the correct SAQ depends on both the merchant's PCI compliance level and how it integrates with Braintree. It describes four compliance levels and attributes classification to Visa based on aggregate Visa credit, debit, and prepaid transaction volume over 12 months under the registered Doing Business As name.
- Braintree's secure storage and processing of card data does not automatically satisfy the merchant's PCI obligations. The page warns that failure to complete the annual SAQ could lead to substantial fines and suspension of the ability to accept credit cards; this is captured provider guidance, not evidence that either consequence has occurred for an account.
- After a Braintree application is approved, merchants may receive an email offering optional SecurityMetrics assistance. For Braintree Direct, the page says level 3 and 4 merchants are set up with SecurityMetrics at no cost, while level 1 and 2 merchants who choose that service are subject to SecurityMetrics' enterprise-level account fees. Those terms are product-, level-, account-, and snapshot-qualified rather than a universal entitlement or current price guarantee.
- SecurityMetrics enrollment requires the Merchant Account Number supplied by email. The page distinguishes it from the merchant account ID and merchant ID, says it is not displayed in the Control Panel, and directs an authorized signer who no longer has the email to request it by email because Braintree will not provide it by phone. The enrollment questionnaire is used to determine which SAQ to complete.

> [!warning] Responsibility and evidence boundary
> Integration with Braintree does not itself establish PCI compliance. Neither this collected guidance nor completion of the documented enrollment steps proves that a merchant selected the correct SAQ, completed an assessment, met applicable requirements, or obtained certification.

> [!warning] Suspected compromise
> The page directs merchants who believe their Braintree integration may have been compromised to contact Braintree for assistance. That is a captured escalation route, not proof that an incident was investigated or resolved.

## Detail locators

- Dated PCI DSS 4.0 assessment notice: `# PCI Compliance > IMPORTANT`, raw lines 17-18.
- PCI DSS audience and PCI Security Standards Council orientation: introductory paragraph, raw line 22.
- Annual SAQ requirement and integration-dependent SAQ selection: `## PCI Self-Assessment Questionnaires`, raw lines 25-29.
- Four compliance levels and Visa-volume classification method: `## PCI compliance levels`, raw lines 32-34.
- Braintree-versus-merchant responsibility and stated non-completion consequences: `## Your requirements`, raw lines 37-43.
- QSA role and SecurityMetrics assistance, approval and level/fee qualifications: `## How we can help`, raw lines 48-58.
- Merchant Account Number identity, retrieval restriction, authorized-signer condition and enrollment questionnaire: `### Enrolling with SecurityMetrics`, raw lines 63-73.
- SecurityMetrics enrollment steps: `### Enrolling with SecurityMetrics > To enroll`, raw lines 75-82.
- Suspected-integration-compromise contact route: final `IMPORTANT`, raw lines 85-86.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Umbrella navigation: [[source-braintree-articles-risk-and-security-overview]]

## Raw Sources

- [[raw/braintree/articles/risk-and-security/compliance/pci-compliance-2026-09-16|Braintree PCI Compliance]] - complete collected snapshot for Braintree's dated PCI DSS and SAQ guidance, merchant responsibility, compliance-level description, optional account-qualified SecurityMetrics assistance, enrollment conditions, and suspected-compromise route
