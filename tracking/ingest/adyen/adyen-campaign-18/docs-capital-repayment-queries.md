# Fixed retrieval checks — Capital repayment

Q1. What does this source cover, and which debt or payment conclusions are unsupported?
- Expected: A 2026-09-15 Capital guide for default scheduled, sale-volume-linked repayment and optional unscheduled repayment toward an outstanding grant. Both modes are described for UI components and API-only integrations, but unscheduled use has region and component-version conditions. It does not identify any user's actual grant terms, amount owed, bank transfer receipt, booked repayment, principal/fee allocation or fully repaid status.
- Raw locators: `raw/adyen/docs/capital/repayment/2026-09-15.md:15-23`, `:33-50`.
- Canonical route (provider-index `[[adyen-capital]]` link was missing at worker audit and is coordinator-owned): `wiki/index.md` → `wiki/adyen-index.md` → `[[adyen-capital]]` → `wiki/sources/adyen/source-adyen-docs-capital-repayment.md` → `[[raw/adyen/docs/capital/repayment/2026-09-15]]`.

Q2. How do scheduled and unscheduled repayment mechanics and qualifications differ?
- Expected: Scheduled repayment reserves a fixed percentage of net captured volume (captured minus refunded/charged back) immediately on capture and deducts the reserve from the user's balance account at sales-day end; negative net captured volume releases that day's reserve and triggers no repayment. Adyen calculates a minimum expected amount per 30-day period, and falling below it **may** prompt unspecified additional steps. Unscheduled repayments allow early payoff/missed-payment cover but, in the snapshot, only for users operating in Europe, UK or US. A user transfers from a verified bank account/transfer instrument to dedicated bank details assigned per disbursement. API-only platforms retrieve/share those details; components expose active-grant details from library 1.4.0. Neither path proves settlement or debt closure.
- Raw locators: `raw/adyen/docs/capital/repayment/2026-09-15.md:19-31`, `:33-44`.
- Canonical route (subject to coordinator index repair): `wiki/index.md` → `wiki/adyen-index.md` → `[[adyen-capital]]` → `wiki/sources/adyen/source-adyen-docs-capital-repayment.md` → `[[raw/adyen/docs/capital/repayment/2026-09-15]]`.
