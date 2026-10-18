# Worker retrieval checks

Q1. Who uses this guide, for what central purpose, and with which prerequisites?

A1. A third-party AISP reads an account holder's consented Adyen business-account information, including account list/details, balances and transactions; this page does not initiate a payment (raw lines 15–26). It requires Adyen onboarding, an access token and the account holder's consent ID, passed with the request as shown by the test headers (raw lines 28–35, 38–51). Route: [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-aisp]] → [[raw/adyen/docs/business-accounts/aisp/2026-09-15]].

Q2. What consequential scope or conflict should an implementer preserve when reading account transactions?

A2. The transaction request filters on booking status and date range; balances appear in the transaction response only when consent includes them, and links paginate the records (raw lines 178–203, 259–265). The curl URL at line 197 omits `aisp` even though this section's account routes and returned link include `/obeu/aisp/v1/` (raw lines 47, 97, 133, 197, 261–264). The account-list prose calls the response an array, but the example wraps it as `{ "accounts": [...] }` (raw lines 53, 65–85). These examples do not prove a live account, current access, payment initiation or beneficiary-bank receipt. Route: [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-aisp]] → [[raw/adyen/docs/business-accounts/aisp/2026-09-15]].
