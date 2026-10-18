# C17 Balance Platform Accounting Report retrieval checks

## Q1 — Purpose, grain, and evidence boundary

Query: What does the Balance Platform Accounting Report cover, when is a row included, and does a booked bank-transfer row prove receipt in a user's bank account?

Expected route: `[[adyen-index]]` → `[[adyen-reporting]]` → `[[source-adyen-docs-platforms-reports-and-fees-balance-platform-accounting-report]]` → pinned raw via source Raw Sources. Answer: daily balance-platform report across liable and user balance accounts; interactive version permits manual date-range/account/event filters. Events enter by status-update day, with category/type/status and a CET selected-day Booking Date window. A `bank/bankTransfer/booked` row describes a balance-account debit/credit, and return states exist; it is not independent beneficiary-bank receipt or signed-off accounting proof. Raw locators: lines 19–40, 61–80, 216–220, 421–429.

## Q2 — IDs, signs, dates, and source warning

Query: How should pending and booked events, value dates, signed register columns, and example rows be interpreted without inventing a reconciliation formula?

Expected route: `[[adyen-index]]` → `[[adyen-reporting]]` → `[[source-adyen-docs-platforms-reports-and-fees-balance-platform-accounting-report]]` → pinned raw via source Raw Sources. Answer: pending transfer flow uses Transfer Id; booked balance transaction uses Transaction Id, with refund as a new transfer flow. Read Booking Date separately from Value Date and the row time-zone fields; Received/Reserved/Balance (PC) are signed register movements in Payment Currency whose direction depends on event category, status and account. Optional columns such as Exchange Rate and Platform Payment Split Type must be enabled, and `Issued Card Scheme Fee` is marked do-not-use. The top-up example's blank Transaction Id and nonzero register movements under `received` conflict with the general no-ID/no-movement statement; avoid deriving a universal formula from that example. Raw locators: lines 50–69, 200–210, 228–267, 323–347, 373–437.
