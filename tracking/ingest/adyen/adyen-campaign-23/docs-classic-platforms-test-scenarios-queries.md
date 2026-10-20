# Retrieval checks — docs-classic-platforms-test-scenarios

Q1. How does the Classic Platforms guide create payout-state test account holders?

A1. Route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-test-scenarios]] → [[raw/adyen/docs/classic-platforms/test-scenarios/2026-09-15]]. The page is explicitly for Classic integrations (raw line 19). Individual and Business examples use Classic POST `/createAccountHolder` with `PASSED` city and bank-owner-city fields, `TestData` identity/business fields and at least one bank account (raw lines 26–38, 146–156). They then upload a passport/photo ID and bank statement through HOP or `/uploadDocument` (raw lines 89–144, 223–278). Photo-ID upload is described as setting a “limitless” high-KYC state (raw lines 97–103, 231–236); these are test fixtures, not proof of real verification or payout.

Q2. Which fixtures simulate failures or refund timing, and what limits or inconsistencies matter?

A2. Route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-test-scenarios]] → [[raw/adyen/docs/classic-platforms/test-scenarios/2026-09-15]]. `FRAUD` city values are used for `FAILED` KYC examples described as suspended with payouts blocked (raw lines 280–294, 345–356). `INVALIDDATA` marks invalid city/passport fields (raw lines 423–443), but that section says `bankAccount.ownerCity` while earlier examples say `bankAccountDetails.ownerCity` (raw lines 35, 152, 289, 350, 426). `INACTIVEDEADLINECITY` schedules `/refundNotPaidOutTransfers` for six weeks later, while `REFUNDDEADLINECITY` describes immediate performance (raw lines 445–455). The captured guide describes simulated states and does not establish a completed real refund or bank receipt.
