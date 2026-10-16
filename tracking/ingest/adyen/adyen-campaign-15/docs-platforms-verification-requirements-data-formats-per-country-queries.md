# Fixed retrieval queries — Adyen platform data formats by country

## Q1 — Purpose, scope, and what it does not infer

**Question:** What is this country/region data-format reference for, and what outcome does it not prove?

**Answer:** It lists accepted example formats for legal-entity address, bank, identification, registration and tax data by operating country/region and entity type, for Adyen for Platforms or issuing. The page says those integrations have no additional requirements, limitations or preparations in this reference. Adyen may still require additional documents if automatic verification fails, so a syntactically matching value is not proof of identity, verification approval, onboarding, account eligibility or fund movement. Canonical route: [[index]] → [[adyen-index]] → [[adyen-platforms]] (c9w01 foundation pending) → [[source-adyen-docs-platforms-verification-requirements-data-formats-per-country]]. Raw: `raw/adyen/docs/platforms/verification-requirements/data-formats-per-country/2026-09-15.md`, lines 5–27.

## Q2 — Central capability, prerequisites, and warnings

**Question:** How should a platform use the country tables without flattening entity or format exceptions?

**Answer:** Select the operating country/region, legal-entity row, identifier or bank-field type and any onboarding-version column together, then consult the exact table entry and example. General API separators are optional, but Sweden’s individual-number dash is mandatory, Germany says remove the organizational Steuernummer slash, and Singapore bank account numbers exclude separators/whitespace. Canada requires a registration document without a Business Incorporation Number; Cyprus expects English equivalents of Greek registry prefixes; Italy can verify CCIAA/REA only with a CCIAA document. Those conditions and the dated 2024-modified snapshot do not establish current legal or account eligibility or verification success. Raw lines 19–27, 29–44, 79–91, 104–120, 179–189, 262–279, 426–439 and 476–490. Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-verification-requirements-data-formats-per-country]].
