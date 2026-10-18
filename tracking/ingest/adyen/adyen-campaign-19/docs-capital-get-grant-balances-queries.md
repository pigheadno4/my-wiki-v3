# Retrieval probes — Capital grant balances

Q1. How does a platform retrieve one account holder's grant references, one grant's balance/status, or its grant-account aggregate?

Forward route: [[adyen-index]] → [[adyen-capital]] → `## Sources` → [[source-adyen-docs-capital-get-grant-balances]] → [[raw/adyen/docs/capital/get-grant-balances/2026-09-15]].

Expected answer: Use GET `/grants` with `counterpartyAccountHolderId` for the receiving holder, GET `/grants/{grantId}` for one grant, and GET `/grantAccounts/{id}` for grant-account aggregate balances and limits. Keep grant, grant-account, offer, holder and receiving balance-account IDs distinct. Principal/fee/total are currency-specific grant balance fields; `renewal.minimumAmount` is conditional on eligible=true, and `renewsGrantId` only on a renewal grant. Requirements include Capital/Platforms and API roles, supported-region and prior offer/ToS/disbursement context. Raw locators: lines 19–38, 40–69, 120–148, 179–203; corresponding three GET headings.

Q2. Can the example balances and renewal links establish today's debt, a completed payout or a reliable grant-to-grant lineage?

Forward route: [[adyen-index]] → [[adyen-capital]] → `## Sources` → [[source-adyen-docs-capital-get-grant-balances]] → [[raw/adyen/docs/capital/get-grant-balances/2026-09-15]].

Expected answer: No. The dated examples lack an as-of balance timestamp or disbursement/repayment transaction. The list says grant 2 renews grant 1, while the single-grant sample says grant 1 renews grant 2; list status is an object but single status a string. The grant-account sample's negative limits are maximum-total-grant fields, not user cash. The `/grantAccounts/{id}` URL uses a path ID despite “query parameter” prose. Check actual responses and separate lifecycle/reconciliation evidence for real outcomes. Raw locators: lines 73–118, 152–177, 179–239; `## Get all grants`, `## Get details of a specific grant`, `## Get details of your grant account`.
