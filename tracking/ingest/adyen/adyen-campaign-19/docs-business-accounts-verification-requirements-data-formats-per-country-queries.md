# Retrieval probes — Business Accounts country data formats

Q1. What format does the captured Adyen reference give for a specific country, legal-entity category and ID or bank field, and does its row make that field universally required?

Forward route: [[adyen-index]] → [[adyen-business-accounts]] → `## Sources` → [[source-adyen-docs-business-accounts-verification-requirements-data-formats-per-country]] → [[raw/adyen/docs/business-accounts/verification-requirements/data-formats-per-country/2026-09-15]].

Expected answer: Look up the exact country heading and data-subject/field row in the dated table, preserving alternatives and examples. The reference covers Belgium (lines 29–39), France (41–52), Germany (54–64), Netherlands (66–76), Spain (78–89), UK (91–106) and US (108–119). It specifies accepted formats/examples; a row is not proof a field is required for every entity, that the country is currently Business Accounts eligible, or that KYC passed.

Q2. Are separator characters always accepted as optional, and does the page waive Business Accounts verification?

Forward route: [[adyen-index]] → [[adyen-business-accounts]] → `## Sources` → [[source-adyen-docs-business-accounts-verification-requirements-data-formats-per-country]] → [[raw/adyen/docs/business-accounts/verification-requirements/data-formats-per-country/2026-09-15]].

Expected answer: The opening says separator spaces/dashes/slashes/dots are optional in API requests, but Germany's organization tax-ID row explicitly says remove `/` before sending; follow the field-specific rule. Automatic verification may fail and require additional documents. The no-additional-preparations statement concerns this reference for Platforms/Issuing, not waiver of KYC or proof of account opening. Raw locators: lines 19–27, 54–64; `## Requirements`, `## Germany`.
