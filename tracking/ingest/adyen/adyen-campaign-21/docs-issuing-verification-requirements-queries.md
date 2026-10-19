# Retrieval checks — docs-issuing-verification-requirements

## Q1 — Main purpose and prerequisites

What determines verification data for an Issuing user? The dated guide says to collect and submit required verification information according to country/region of operation, legal-entity type and requested capability levels; card issuance also calls for a VAT number or, where there is no VAT system, tax ID (raw lines 19-27). It names both Adyen for Platforms and Issuing integrations (raw line 31), distinguishes the main contractual legal entity and linked associated individuals (raw lines 67-71), and routes exact country/entity fields to the detailed minimum-information reference (raw lines 33-37). Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-verification-requirements]] → [[raw/adyen/docs/issuing/verification-requirements/2026-09-15]].

## Q2 — Material boundary or conflict

May a platform infer a minor can be onboarded everywhere, or that the general VAT sentence completely specifies a sole proprietor's fields? No. Only Legal Entity Management API v3/v4 is described for minors, under-13s cannot be onboarded, and the table distinguishes EU/UK/NO/CH, AU/CA/US and HK/SG residency age ranges plus legal-representative/signatory conditions (raw lines 39-65). The general Issuing VAT/tax-ID wording at line 25 differs from the sole-proprietorship list's VAT-if-registered wording at lines 186-196. These dated requirements require country/entity confirmation; capability thresholds are per card/day and higher levels can trigger more checks (raw lines 204-213). Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-verification-requirements]] → [[raw/adyen/docs/issuing/verification-requirements/2026-09-15]].
