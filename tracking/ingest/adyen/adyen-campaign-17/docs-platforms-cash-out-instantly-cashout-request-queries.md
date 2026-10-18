# C17 cashout request retrieval checks

## Q1 — Cashout purpose and payout boundary

Query: Does a successful Adyen for Platforms `/cashouts` response mean funds reached the user's bank, and what changes if no transfer-instrument ID is supplied?

Expected route: `[[adyen-index]]` → `[[adyen-platforms]]` → `[[source-adyen-docs-platforms-cash-out-instantly-cashout-request]]` → pinned raw via source Raw Sources. Answer: the cashout makes pending funds available in the user's balance account; adding `counterparty.transferInstrumentId` requests payout to that instrument, while omitting it leaves funds in the balance account. Processing is asynchronous, and a created response/transfer IDs are not bank receipt. Raw locators: lines 15–19, 106–118, 153–216.

## Q2 — Preconditions, fee limits, and failure

Query: What gates and checks precede a cashout request, and how should a confirmed instrument-payout failure be handled?

Expected route: `[[adyen-index]]` → `[[adyen-platforms]]` → `[[source-adyen-docs-platforms-cash-out-instantly-cashout-request]]` → pinned raw via source Raw Sources. Answer: Adyen for Platforms integration, Transfers and Configuration API credential roles, user receive/send balance-account capabilities, conditional transfer-instrument send capability, Support enablement and sales-day settlement. Route calculation and pending-available balance checks are recommended. Fee amount is bounded by cashout amount and cashout-plus-fee by pending available balance, with matching currency. A successful request followed by failed instrument payout is reversed, returning amount and user fee to pending available balance; a retry after confirmed failure is a new POST, not a blind repeat of a pending request. The dated EUR/USD/GBP/AUD and one-unit limits require current verification. The request/response sample has conflicting fee values. Raw locators: lines 21–35, 48–104, 110–122, 124–206, 225–326.
