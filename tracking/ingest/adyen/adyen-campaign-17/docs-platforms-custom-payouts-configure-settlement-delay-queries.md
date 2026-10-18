# Configure settlement delay — retrieval probes

## Q1 — Purpose and money-flow boundary

**Query:** What does changing settlementDelayDays on a Platforms balance account do, and does a three-day setting mean the user's bank receives a payout after three days?

**Expected answer:** The merchant account has a default settlement delay; the guide allows a different delay per balance account. settlementDelayDays measures business days after funds in a settlement batch before they become available in that balance account. The three-day PATCH is illustrative. This page does not initiate a bank transfer or establish payout arrival, available-funds movement for a real account, or beneficiary bank receipt.

**Raw locators:** lines 15-19 (scope/default); 33-46 (POST/PATCH and business-day field); 48-64 (example); 268-292 (configuration response). **Canonical discovery route:** [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-custom-payouts-configure-settlement-delay]] → [[raw/adyen/docs/platforms/custom-payouts/configure-settlement-delay/2026-09-15]].

## Q2 — Prerequisites, limits and reset warning

**Query:** What must be in place to set a custom settlement delay, can a one-day delay coexist with a managed payout schedule, and what happens to an existing sales-day closing time during an update?

**Expected answer:** The captured guide requires a Configuration API credential with Balance Platform BCL role and Account Manager enablement of custom sales-day settlement delay. One day needs previous Adyen approval; custom delay cannot be used on a balance account with a managed payout schedule. Documented settlementDelayDays values are integers 1–20 or null default. If a specific salesDayClosingTime was previously configured, include it with every balance-account update or it resets to 00:00. The guide asks for Configuration webhooks and says balanceAccount.created/updated is sent after the new delay is applied; the sample TEST event is not production or settlement proof.

**Raw locators:** lines 21-31 (role, webhooks, approval, managed-schedule exclusion, enablement); 35-46 (API targets and closing-time reset); 294-322 (applied-configuration webhooks/test event). **Canonical discovery route:** [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-custom-payouts-configure-settlement-delay]] → [[raw/adyen/docs/platforms/custom-payouts/configure-settlement-delay/2026-09-15]].
