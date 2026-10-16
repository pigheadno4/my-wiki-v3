# Fixed queries — docs-account-manage-payout-account-details

## Q1 — purpose, scope, and what not to infer

**Question:** At what account level are Adyen payout bank details configured, and does submitting them prove approval or bank receipt?

**Expected answer:** Payout details are configured per merchant account; a merchant accepting multiple currencies may link multiple bank accounts. For a new live account, select bank country/region and supported payout currency, enter details, upload a bank statement, and submit for Adyen review. The submission is not an approved account or evidence of a payout reaching a bank. Current supported-country/currency combinations require the linked guide or account-specific check. Route: [[index]] → [[adyen-index]] → [[adyen-account-structure]] → [[source-adyen-docs-account-manage-payout-account-details]] → [[raw/adyen/docs/account/manage-payout-account-details/2026-09-15]]. Raw locators: opening lines 15–21; `Add your payout account > Live` lines 23–39.

## Q2 — central capability, prerequisites, and warnings

**Question:** How do live add, test setup, copy, view, edit, and remove differ in roles and approval state?

**Expected answer:** Add, copy, edit, and remove use Merchant manage bank accounts. A live new-account submission with a bank statement goes to Adyen review; edited details cannot be changed while pending approval and a submitted edit also goes for review. Only approved details may be copied to another merchant account under the same legal entity; the copy change is automatic without waiting for another approval. Viewing requires Merchant financial or Merchant admin. Removing with Close this account and Yes, close needs no Adyen approval. A test payout account is for reconciliation testing, which also requires automatic Settlement details report generation; it is not a live payout. Route: [[index]] → [[adyen-index]] → [[adyen-account-structure]] → [[source-adyen-docs-account-manage-payout-account-details]] → [[raw/adyen/docs/account/manage-payout-account-details/2026-09-15]]. Raw locators: `Add your payout account` lines 23–51; `Copy payout account details` lines 57–73; `Check payout account details` lines 75–87; `Edit your payout account` lines 89–103; `Remove a payout account` lines 105–119.
