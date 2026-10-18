# Payout amount calculation — retrieval checks

## Q1 — purpose, scope, and amount rule

**Query:** For an Adyen for Platforms user on a managed or custom payout schedule, how does Adyen calculate the maximum scheduled or on-demand payout amount? Is a calculated maximum evidence that the bank received the payout?

**Expected retrieval:** This dated Platforms guide calculates a maximum from the user's balance account before payout. Default maximum is available balance: current settled balance reduced by net negative future balance changes reflected in reserved and pending balances; nonnegative net future changes leave it at current balance. The examples show USD 100 current and USD -20 net future changes yielding USD 80 available. The prose's “subtracts future balance changes” wording is ambiguous for signed negative values, so preserve the example's result without treating literal subtraction of -20 as the formula. The alternative maximum is current settled balance after Adyen-contact setup and reserve sufficiency. One configuration applies to all balance accounts in the platform. This is a payout cap, not a successful request, booking, bank tracking, or beneficiary receipt.

**Raw locators:** lines 15–23 (purpose); 25–43 (requirements and two platform-wide choices); 47–93 (available-balance method and three examples); 95–104 (current-balance option).

**Canonical route:** [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-payout-amount]] → [[raw/adyen/docs/platforms/payout-amount/2026-09-15]].

## Q2 — collateral prerequisites, failure, and release

**Query:** What happens if a platform enables paying out a user's current balance when that exceeds available balance, and the reserve account cannot cover the difference? What happens to blocked collateral later?

**Expected retrieval:** Adyen contact and enough available platform reserve funds are prerequisites to the current-balance configuration. When current exceeds available, Adyen checks the reserve account: sufficient funds lead to a block equal to the difference as collateral and then payout processing; insufficient funds cause the payout to fail. The reserve account is separate from the user's balance account. Collateral is gradually unblocked as incoming funds compensate the negative available balance. If the balance remains negative for 30 days, Adyen transfers the remaining collateral from reserve to the user's balance account and sends an internal-fund-transfer webhook. The sample USD 1,000 current/USD 800 available/USD 200 block is illustrative; neither the request nor reserve block proves bank payout or receipt. Adyen recommends checking balance-account state before payout by API, Customer Area or balance webhooks.

**Raw locators:** lines 95–124 (enablement, reserve check and failure); 128–155 (illustrative block and balances); 157–224 (gradual release, 30-day transfer and webhook); 226–232 (recommended balance checks).

**Canonical route:** [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-payout-amount]] → [[raw/adyen/docs/platforms/payout-amount/2026-09-15]]; reserve context at [[source-adyen-docs-platforms-manage-reserve-account]].
