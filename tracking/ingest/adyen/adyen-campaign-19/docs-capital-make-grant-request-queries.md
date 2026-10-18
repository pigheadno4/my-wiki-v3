# Retrieval probes — Capital grant request and disbursement

Q1. After a user selects a Capital grant offer, what is required to request the grant and choose its destination?

Forward route: [[adyen-index]] → [[adyen-capital]] → `## Sources` → [[source-adyen-docs-capital-make-grant-request]] → [[raw/adyen/docs/capital/make-grant-request/2026-09-15]].

Expected answer: The 2026-09-15 guide requires a Capital-enabled Platforms integration, designated Capital API roles, `getGrantOffers`/`receiveGrants` capabilities, supported-region/compliance prerequisites, selected offer and signed ToS. POST `/grants` with Adyen-provided `grantAccountId` and the selected `grantOfferId`; choose a receiving balance account or the account holder legal entity's transfer instrument per the parameter descriptions. If `balanceAccountId` is omitted, the guide says the account holder's primary balance account is used. It states one disbursement per grant. Raw locators: lines 19–37, 39–67; `## Requirements`, `## 1. Configure a grant`.

Q2. Does a `Requested` API response or the guide's booked-transfer example show an actual completed grant payout?

Forward route: [[adyen-index]] → [[adyen-capital]] → `## Sources` → [[source-adyen-docs-capital-make-grant-request]] → [[raw/adyen/docs/capital/make-grant-request/2026-09-15]].

Expected answer: No. POST `/grants` is asynchronous. Separate grants.created configuration from transfer-created/updated received, authorised and booked stages and transaction.created payout observation. The configured-grant sample still says Requested and zero balances. The test examples do not form a coherent actual trace: incoming transfers use positive amount and 2025 timestamps, while the transaction illustration uses a negative amount and 2023 booking/creation dates; no bank receipt is shown. Raw locators: lines 88–127, 129–160, 162–221, 224–305, 302–399, 397–435; `## 2. Get updates`.
