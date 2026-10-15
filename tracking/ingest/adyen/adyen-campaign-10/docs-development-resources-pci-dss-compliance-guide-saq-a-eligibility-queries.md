# SAQ A eligibility retrieval checks

## Q1 — Purpose and scope

**Query:** Does this Adyen page prove my online integration is eligible for SAQ A or PCI compliant?

**Answer:** It states PCI DSS v4.0.1 SAQ A eligibility criteria for online-payments integrations. A merchant must confirm both that all browser-delivered payment-page/form elements originate only and directly from a PCI DSS-compliant TPSP or processor, and that its site is not susceptible to script attacks affecting ecommerce systems. The page and Adyen product AoC do not validate a particular merchant site or prove its compliance. **Raw locators:** `raw/adyen/docs/development-resources/pci-dss-compliance-guide/saq-a-eligibility/2026-09-15.md:15-19`, `:23-46`. **Canonical route:** [[source-adyen-docs-development-resources-pci-dss-compliance-guide-saq-a-eligibility]] → [[raw/adyen/docs/development-resources/pci-dss-compliance-guide/saq-a-eligibility/2026-09-15]]; [[adyen-pci-dss-compliance]].

## Q2 — Changed requirements and separate scan

**Query:** Did the 2025 SAQ A change remove all merchant script-security and scanning duties, and is SAQ A the same as a passing ASV scan?

**Answer:** No. The page says requirements 6.4.3 and 11.6.1 were removed from SAQ A when the new version took effect on 2025-03-31; they remain applicable for SAQ D and onsite-AoC cases. SAQ A merchants still need to ensure provider-loaded payment elements/scripts are compliant, protect against script attacks, and meet regular vulnerability scans under 11.3.2. SAQ A is an attestation route; the separate linked scanning guide describes ASV scans and the passing final report. Neither source proves a specific merchant has completed those steps. **Raw locators:** `raw/adyen/docs/development-resources/pci-dss-compliance-guide/saq-a-eligibility/2026-09-15.md:33-40`, `:53-64`; related scan guide `raw/adyen/docs/development-resources/pci-dss-compliance-guide/vulnerability-scanning-regulation/2026-09-15.md:21-21`, `:39-52`. **Canonical route:** [[source-adyen-docs-development-resources-pci-dss-compliance-guide-saq-a-eligibility]] → [[raw/adyen/docs/development-resources/pci-dss-compliance-guide/saq-a-eligibility/2026-09-15]]; [[adyen-pci-dss-compliance]].
