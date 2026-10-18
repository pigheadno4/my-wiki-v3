# Retrieval probes — Capital grant renewal

Q1. Can a partially repaid Capital grant be renewed, and what gates apply before the subsequent grant is configured or paid out?

Forward route: [[adyen-index]] → [[adyen-capital]] → `## Sources` → [[source-adyen-docs-capital-renew-grant]] → [[raw/adyen/docs/capital/renew-grant/2026-09-15]].

Expected answer: The 2026-09-15 guide describes a limited-availability pilot. Observe prior grant `renewal.eligible` and `renewal.minimumAmount`, apply separate renewal eligibility, obtain a dynamic/static offer meeting that minimum and the page's 150%-of-outstanding-balance rule, account for weekly recalculation/seven-day expiry, obtain re-acceptance of new ToS, then POST a subsequent grant using the selected offer, Adyen-provided grant account and `renewsGrantId` of the prior grant. Only one disbursement per grant is supported in the snapshot. The guide says full subsequent amount is disbursed and prior principal reserved for repayment; reservation is not demonstrated repayment. Raw locators: lines 19–46, 58–66, 109–120, 125–140; `## Requirements` through `## 4`.

Q2. Does a `Requested` POST response or the guide's sample grant/transfer statuses prove a user received renewal funds?

Forward route: [[adyen-index]] → [[adyen-capital]] → `## Sources` → [[source-adyen-docs-capital-renew-grant]] → [[raw/adyen/docs/capital/renew-grant/2026-09-15]].

Expected answer: No. POST `/grants` is asynchronous. Distinguish `grants.created` configuration, transfer received/authorised/booked events, `transaction.created` payout observation, and later grant-updated repayment. A sample status or booked transfer does not prove bank receipt or actual prior-principal settlement. The test examples conflict as a single renewal trace: minimum amount 9440625 versus transfer amount 1850000, plus varying outer/nested grant IDs; use actual identifiers and records. Raw locators: lines 90–105, 173–209, 213–245, 249–317, 391–488, 523–555; `## 5. Get updates`.
