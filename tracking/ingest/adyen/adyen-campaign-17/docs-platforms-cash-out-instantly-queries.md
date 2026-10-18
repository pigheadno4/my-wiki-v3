# Cash out pending funds instantly — retrieval probes

## Q1 — Money flow and proof boundary

**Query:** Does an Adyen Platforms CashOut always send funds instantly to a user's bank, and what happens later at settlement?

**Expected answer:** CashOut is a user-requested way to make pending available funds available early. The guide describes a Cashout Funding credit to the user's balance account. It describes an instant payout to the user's transfer instrument only if that instrument is specified in the request; a fee debit to the platform liable balance account is optional. When the captured payments settle, Adyen debits the cashout amount from the user's balance account as Cashout Repayment. The illustrative chronology is inconsistent: January 1 sales with a two-day delay are said to become available January 3, but the repayment step labels settlement January 1; do not infer an exact repayment date from it. If the receiving bank does not support instant payout, funds are returned and the cashout amount is restored to the source account's pending available balance. None of this overview proves bank receipt for a particular request.

**Raw locators:** lines 19-23 (pending funds/optional later payout); 29-46 (amount, fee and four legs); 48-50 (bank support/return). **Canonical discovery route:** [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-cash-out-instantly]] → [[raw/adyen/docs/platforms/cash-out-instantly/2026-09-15]].

## Q2 — Limits, eligibility and reporting

**Query:** What limits or exclusions does this CashOut overview give, and why might a user have no Payout report on a full-cashout day?

**Expected answer:** The captured support table lists AU/AUD, EEA/EUR, US/USD and UK/GBP, subject to the receiving bank's instant-payout support; Australia may see ANZ rail delays. The minimum is 0.01, the rolling 24-hour per-balance-account maximum is configured at platform level with Adyen approval, and same-account requests cool down until the prior successful request is processed (usually about one minute, up to ten). Pass-through-settlement payment proceeds are not in pending available and cannot be cashed out. The page says a full cashout leaves no scheduled payout, so no Payout report is generated for that balance account that day; use Statement reporting and transfer webhooks for their respective evidence grains. TEST bank details and described failures do not establish current account eligibility or production success.

**Raw locators:** lines 48-69 (support and limits); 71-87 (reports/webhooks); 89-99 (TEST and failure scenarios). **Canonical discovery route:** [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-cash-out-instantly]] → [[raw/adyen/docs/platforms/cash-out-instantly/2026-09-15]].
