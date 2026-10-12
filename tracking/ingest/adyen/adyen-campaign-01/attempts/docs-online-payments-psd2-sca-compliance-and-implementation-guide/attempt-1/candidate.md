---
title: "Adyen docs: PSD2 SCA compliance guide"
type: source
date_ingested: 2026-10-11
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/psd2-sca-compliance-and-implementation-guide"
raw_files:
  - "adyen/docs/online-payments/psd2-sca-compliance-and-implementation-guide/2026-09-15.md"
tags: [adyen, psd2, sca, 3d-secure, online-payments, compliance]
---

## Overview

This Adyen guide introduces PSD2 strong customer authentication for merchants using an online payments integration and routes implementation through 3D Secure. It frames the legal obligation as applying to issuing banks while explaining the transaction-refusal risk that makes merchant compliance consequential. The page is supplementary provider guidance, not legal advice.

## Key takeaways

- Adyen recommends 3D Secure for applying SCA to affected transactions and identifies both 3D Secure 1 and 3D Secure 2 as compliant methods. The snapshot does not by itself establish compliance, successful authentication, authorization, or current issuer behavior for a particular payment.
- The guide says PSD2 applies to banks rather than merchants: issuing banks must refuse non-compliant transactions under applicable domestic law, while merchants need compliant transactions to reduce refusal risk.
- The stated scope test is bilateral: both the acquiring processing entity and the customer's issuer processing entity must be in the EEA, Monaco, Switzerland, or the UK. Merchant location alone is therefore not the complete test.
- For a business located in Switzerland, the guide treats the acquiring processing entity as being in the EEA because Adyen's Netherlands entity acquires the funds.

> [!warning] Legal and snapshot boundary
> Adyen expressly says this guide is not legal advice and supplements domestic regulatory guidance, card-scheme rules, and EMVCo 3D Secure 2 specifications. Treat its region list and routing statements as retained 2026-09-15 provider guidance, not a universal or current legal determination.

## Detail locators

- Non-legal-advice warning and external authorities: introduction (raw lines 19-23).
- Required integration type: `Requirements` (raw lines 25-31).
- PSD2 purpose, regulated actor, issuer refusal and merchant risk: `What is PSD2?` (raw lines 33-37).
- SCA and 3D Secure implementation route: `What do I need to do to comply with PSD2 SCA?` (raw lines 39-43).
- Bilateral processing-entity scope test, country/region list and Switzerland acquiring treatment: `Are my payments affected?` (raw lines 45-87).
- Business-location decision routes: `Is my business located in one of the in-scope countries/regions for SCA compliance?` (raw lines 89-103).

## Related

- Company: [[adyen]]
- Provider concept: [[adyen-psd2-sca-and-3d-secure]]
- Implementation options: [[source-adyen-docs-online-payments-psd2-sca-compliance-and-implementation-guide-sca-options]]

## Raw Sources

- [[raw/adyen/docs/online-payments/psd2-sca-compliance-and-implementation-guide/2026-09-15|Adyen — PSD2 SCA compliance guide (2026-09-15)]]
