# Fixed queries — Platforms onboarding v4 changes

## Q1 — purpose, scope, and what must not be inferred

**Query:** What is this onboarding-v4 page for, and does it establish that an account holder passed verification or can process payments?

**Answer:** It catalogs changes in Adyen Platforms onboarding v4 and Legal Entity Management API validation for hosted and API-only paths, with country/entity and financial-product qualifications. It is historical guidance, not a completed onboarding, consent record, assigned role, capability state, current eligibility determination or payment outcome. The page points separately to onboarding versioning and the API diff tool. Raw: `raw/adyen/docs/platforms/onboard-users/onboarding-versions/onboarding-v4/2026-09-15.md:15-40,83-85`. Canonical route: `[[source-adyen-docs-platforms-onboard-users-onboarding-versions-onboarding-v4]]` → `[[adyen-platforms]]`.

## Q2 — central changes, prerequisites, and warnings

**Query:** Which v4 validation changes and scoped exceptions must an onboarding implementation handle?

**Answer:** Individuals cannot use PO boxes as residential addresses; organizations using a registered-address PO box need a physical principal-place address. The page says DELETE `/documents/{id}` now returns 404 and adds low-quality-ID upload and name/address validation, including verification-error handling. Users aged 13–18 require a legal representative only in particular regions; unincorporated partnerships began with v3 in selected regions and remain LEM-API-only. Organizations generally provide registration numbers before payment processing, with country-specific exceptions such as New Zealand absence reporting. DBA/principal-place rules, platform-model support contacts and country/entity-specific requirements must be applied narrowly. Issuing business-line/industry-code and business-account/issuing source-of-funds duties apply only to those products, and Adyen may request documents. None of these submitted fields proves verification or capability approval. Raw: `raw/adyen/docs/platforms/onboard-users/onboarding-versions/onboarding-v4/2026-09-15.md:41-61,83-85,199-246,250-412,414-489`. Canonical route: `[[source-adyen-docs-platforms-onboard-users-onboarding-versions-onboarding-v4]]` → `[[adyen-platforms]]`.
