# C17 sales-day closing-time retrieval checks

## Q1 — Configuration purpose and evidence boundary

Query: What does the Adyen for Platforms sales-day closing-time setting change, and does a successful setting response prove settlement or bank arrival?

Expected route: `wiki/adyen-index.md` → `wiki/concepts/adyen-platforms.md` → `wiki/sources/adyen/source-adyen-docs-platforms-settle-funds-configure-closing-time.md` → pinned `raw/adyen/docs/platforms/settle-funds/configure-closing-time/2026-09-15.md`. Answer: a new or existing balance account can set the local sales-day closing hour through Configuration API `platformPaymentConfiguration.salesDayClosingTime`, default 00:00 and allowed hourly through 07:00. API response and balance-account webhook describe the setting, not captured funds, an available settlement balance, payout, or bank receipt. Raw locators: lines 15–19, 33–47, 286–340.

## Q2 — Prerequisites, delay, and exceptions

Query: What must be checked before treating a configured cutoff as a settlement schedule for a specific platform balance account?

Expected route: `wiki/adyen-index.md` → `wiki/concepts/adyen-platforms.md` → `wiki/sources/adyen/source-adyen-docs-platforms-settle-funds-configure-closing-time.md` → pinned `raw/adyen/docs/platforms/settle-funds/configure-closing-time/2026-09-15.md`. Answer: Configuration API BCL role and Configuration-webhook subscription; returned balance-account time zone and closing-time value; separate `settlementDelayDays` merchant-default override (1–20 business days or null); Affirm and maestro_USA method-schedule exceptions. The sample prose mentions two business days but omits the delay field, and its webhook example uses 06:00 after a 01:00 request/response, so those examples do not establish one completed configuration or availability date. Raw locators: lines 21–47, 48–65, 286–340.
