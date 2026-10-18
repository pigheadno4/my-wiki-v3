# Verify balances — retrieval probes

## Q1 — Report, account, currency and date grain

**Query:** How does this Platforms guide spot-check a user's balance on a chosen day, and can I add all rows sharing one PSP reference to get that user's available balance now?

**Expected answer:** The Balance Platform Balance Report provides opening and closing positions for a given date by account holder, balance account and currency, including liable-account rows. The Accounting Report guide illustrates an account filter and Balance (PC) sum, but interpreting an account-currency position at an as-of point also requires selecting the currency and relevant value-date/as-of period; never add different currencies, and include only entries whose value dates fall within the chosen as-of cutoff or defined period. Its EUR-only rows are not a full multi-currency, as-of-date reconciliation recipe. In the example, received and authorised entries have zero Balance (PC); the captured split appears on its later value date. One PSP reference has separate user, liable and fee-account rows with signed amounts, so combining them would mix account grains. These historical reports do not establish a later real-time available balance or a completed payout.

**Raw locators:** lines 19-26 (two methods); 28-43 (date/account/currency snapshots); 45-69 (Balance (PC), value date and split rows). **Canonical discovery route:** [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-platforms-reconciliation-use-cases-verify-balances]] → [[raw/adyen/docs/platforms/reconciliation-use-cases/verify-balances/2026-09-15]].

## Q2 — Negative balance and compensation

**Query:** What does the captured guide say happens to a balance account left negative, and does the warning webhook prove the liable account has already funded it?

**Expected answer:** The guide attributes negative balances to refunds or chargebacks and says payouts/transfers use available balance only. It describes month-end internal compensation from the platform liable account if an account has been negative for more than 30 days, visible in an Accounting Report entry and internal/internalTransfer webhooks. An optional warning webhook is described after over 20 days by default, with a scheduled compensation time; its TEST example is conditional on the amount still being uncompensated by then. A warning is notice of a possible future internal transfer, not evidence it booked. An account holder may separately top up on demand or via scheduled sweep before compensation; this is not bank payout proof.

**Raw locators:** lines 71-82 (negative-balance process and transfer grain); 84-122 (warning and threshold); 124-129 (top-up alternatives). **Canonical discovery route:** [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-platforms-reconciliation-use-cases-verify-balances]] → [[raw/adyen/docs/platforms/reconciliation-use-cases/verify-balances/2026-09-15]].
