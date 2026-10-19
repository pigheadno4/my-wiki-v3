# Retrieval checks — docs-issuing-manage-liable-accounts

## Q1 — Account identity and funds

Which liable balance accounts does the guide identify, and whose funds do they hold? Both belong to the platform and hold platform funds (raw lines 19-22). The main account receives platform transaction commissions and can fund user transaction fees or transfers to users for corrections (raw lines 24-26). The reserved incorrect-splits account receives amounts that were split toward nonexistent or unable-to-receive balance accounts (raw lines 28-36). Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-manage-liable-accounts]] → [[raw/adyen/docs/issuing/manage-liable-accounts/2026-09-15]].

## Q2 — Failure and correction boundary

What makes a split destination unable to receive funds, and what is the stated correction? The guide lists a closed/suspended balance account, a closed/suspended account holder, or missing receive-funds capability; Adyen books the funds to the reserved incorrect-splits account and says the platform can later transfer internally to another balance account (raw lines 30-36). It does not say this transfer is automatic or prove any specific settlement/payout outcome. Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-manage-liable-accounts]] → [[raw/adyen/docs/issuing/manage-liable-accounts/2026-09-15]].
