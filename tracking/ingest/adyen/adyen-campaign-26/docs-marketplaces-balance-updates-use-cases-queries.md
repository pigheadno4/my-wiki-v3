# Retrieval checks — docs-marketplaces-balance-updates-use-cases

Q1. What threshold-alert scopes does this Marketplace Balance webhook use-case page illustrate, and what feature prerequisite applies?

A1. It is explicitly limited-availability/pilot guidance (raw lines 15–24). The TEST examples configure a platform-wide current balance below USD 5,000 using `balancePlatform`/`balance`/`lessThan`, a particular user's accounts at or below USD 5,000 using `accountHolder`/`lessThanOrEqual`, and a separate `balanceAccount` setting for each of six foreign-currency accounts' available balances (raw lines 26–45, 97–116, 169–188). Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-balance-updates-use-cases]] → [[raw/adyen/docs/marketplaces/balance-updates/use-cases/2026-09-15]].

Q2. Can the JPY 100000 example be copied as a verified JPY 1,000 threshold, or can its sample event identify the exact account?

A2. No. The page labels the case as below JPY 1,000 but sends `value: 100000` and shows `available: 95000` (raw lines 173, 184–188, 203–210, 219–234); the Adyen currency reference says JPY has zero decimal minor units ([[source-adyen-docs-development-resources-currency-codes]], raw lines 164–172). The account-targeted TEST event has `accountHolderId` but no `balanceAccountId` in its displayed data (raw lines 221–237). Verify current API units and actual event/setting identity before using those examples operationally. Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-balance-updates-use-cases]] → [[raw/adyen/docs/marketplaces/balance-updates/use-cases/2026-09-15]].
