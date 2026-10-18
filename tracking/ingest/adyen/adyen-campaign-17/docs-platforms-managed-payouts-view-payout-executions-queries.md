# Fixed retrieval checks: docs-platforms-managed-payouts-view-payout-executions

## Q1 — Purpose, access and proof boundary

**Query:** What is a managed payout execution, where can it be viewed, and does Sent or succeeded prove the user's bank was credited?

**Expected answer:** An execution is a payout initiated by a managed payout schedule on a user's balance account. In Customer Area, a user with Balance platform base and Configure scheduled payouts roles can open the account holder, balance account, managed schedule and Events timeline. A Configuration API credential with Bank Scheduled Payouts Merchant Role can GET `/balanceAccounts/{balanceAccountId}/payoutSchedules/{id}/executions`; the response holds `payoutScheduleExecutions`. Customer Area Sent means a payout was created and sent. A succeeded execution webhook carries a `transferId` for the resulting transfer. Neither a Sent/succeeded schedule result nor an estimated arrival time proves final bank receipt; follow the resulting Transfer webhooks and external evidence.

**Evidence locators:** `raw/adyen/docs/platforms/managed-payouts/view-payout-executions/2026-09-15.md:15-48`, `:49-65`, `:117-143`, `:230-234`. **Canonical route:** `[[adyen]]` → `[[adyen-platforms]]` → `[[source-adyen-docs-platforms-managed-payouts-view-payout-executions]]` → pinned raw.

## Q2 — Skips, failures and next evidence

**Query:** How should a platform interpret Not sent/skipped and Failed executions, and what cautions apply to the guide's sample events and test bank details?

**Expected answer:** Customer Area Not sent means an expected schedule execution was not triggered, for example because payout conditions such as available balance were unmet. The skipped-result table includes no balance, below-minimum amount, disabled configuration and Adyen manual block; no-action guidance in the Events table is tied to its low-balance example, not every skip. Failed means an execution error; possible causes include insufficient reserve funds, routing or counterparty/transfer-instrument problems, missing capabilities and amount/address limits. A failed bank-account or capability cause can recur until fixed. Subscribe to Configuration and Transfer webhooks: execution succeeded/skipped/failed events report schedule results and reasons, while a successful execution's `transferId` routes to transfer events for authorized, captured or eventual returned states. The sample skipped webhook inconsistently has `data.result: failed` with a skipped type/no-balance reason, and the failed sample's `counterpartyBlocked` differs from the table's `counterpartyAccountBlocked`; do not use them as normative result mappings. Bank details are TEST-only; the IR/IE and HU/`hkLocal` rows appear inconsistent and do not prove live eligibility. No schedule result alone establishes beneficiary bank credit or licenses a retry.

**Evidence locators:** `raw/adyen/docs/platforms/managed-payouts/view-payout-executions/2026-09-15.md:25-31`, `:49-57`, `:111-168`, `:172-228`, `:230-282`. **Canonical route:** `[[adyen]]` → `[[adyen-platforms]]` → `[[source-adyen-docs-platforms-managed-payouts-view-payout-executions]]` → pinned raw.
