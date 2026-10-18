# Capital disbursement management — retrieval probes

## Q1 — Purpose, identifiers and proof

**Query:** Does this page create or prove a Capital disbursement, and what IDs are needed to inspect one?

**Expected answer:** It assumes a grant was already disbursed and documents GET /grants/{grantId}/disbursements and a specific-disbursement GET. A disbursement ID is distinct from grant ID, account-holder ID and receiving balance-account ID. The response includes amount, fee, balances, repayment basis points and fundsCollections, but TEST examples are not evidence of any live funding, bank receipt or final debt.

**Raw locators:** lines 15–19, 21–38, 40–110 and 193–236. **Canonical discovery route:** [[adyen-index]] → [[adyen-capital]] → [[source-adyen-docs-capital-manage-disbursements]] → [[raw/adyen/docs/capital/manage-disbursements/2026-09-15]].

## Q2 — Configuration and repayment limitations

**Query:** What can PATCH change, what prerequisites/regions apply, and is fundsCollections IBAN a grant payout destination?

**Expected answer:** The dated guide requires Capital-enabled Platforms access, specified Balance Platform API roles, account-holder capabilities, supported region, signed Terms and at least one existing disbursed grant. It states one disbursement per grant and Europe/UK/US availability for unscheduled repayment. PATCH on grantId plus disbursementId can alter repayment basis points for the share of incoming net volume deducted; its table marks the path IDs required while showing the repayment request object without a required marker. GET on the specific disbursement can return an UnscheduledRepayment fundsCollections bank identifier for the user to pay back the grant. That IBAN is not a grant payout destination, and no example proves an update or booked repayment.

**Raw locators:** lines 21–38, 112–191 and 193–236. **Canonical discovery route:** [[adyen-index]] → [[adyen-capital]] → [[source-adyen-docs-capital-manage-disbursements]] → [[raw/adyen/docs/capital/manage-disbursements/2026-09-15]].
