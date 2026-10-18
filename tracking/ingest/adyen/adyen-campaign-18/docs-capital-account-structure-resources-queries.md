# Capital account structure retrieval checks

Q1. Which user and Capital-specific resources serve distinct roles in Adyen's account structure?
Expected forward route: [[adyen-index]] → [[adyen-capital]] → ## Sources → [[source-adyen-docs-capital-account-structure-resources]] → [[raw/adyen/docs/capital/account-structure-resources/2026-09-15]]. Inspect raw lines 23–40 for Platforms prerequisite and legal entity, transfer instrument, supporting document, account holder and balance account; lines 42–59 for grant account's non-funds receivable and per-currency role; lines 65–73 for per-grant reference.

Q2. Does a CG grant account balance or GR reference's Active/Repaid state prove user funds or bank receipt?
Expected forward route: [[adyen-index]] → [[adyen-capital]] → ## Sources → [[source-adyen-docs-capital-account-structure-resources]] → [[raw/adyen/docs/capital/account-structure-resources/2026-09-15]]. Inspect raw lines 55–63 for non-funds CG account, one-currency rule and sample total; lines 65–73 for reference creation on payout, total/principal/fee, statuses and negative-to-zero example. These are resource descriptions and illustrations, not a live payout/bank receipt or independent debt-discharge record.
