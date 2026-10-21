# Q1 — purpose and prerequisites

**Question:** What does the Marketplace sales-day closing-time guide configure, and what access and route does it require?

**Answer:** It moves the local balance-account sales-day cutoff from midnight to an hourly value 00:00–07:00, so after-midnight business can remain in the prior sales day (raw lines 19, 45–48). It requires a Configuration API credential with Balance Platform BCL role and Configuration webhook subscription; use POST `/balanceAccounts` for a new account or PATCH `/balanceAccounts/{id}` for an existing one (lines 21–29, 36–43, 315–320). Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-settle-funds-configure-closing-time]] → [[raw/adyen/docs/marketplaces/settle-funds/configure-closing-time/2026-09-15]].

# Q2 — settlement and example limits

**Question:** Does the closing-time setting determine every method's settlement or prove a two-day delay and payout?

**Answer:** No. `settlementDelayDays` is separate and conditionally required when different from the merchant default, with 1–20 business days or null/default (raw lines 45–51). The Marketplace page lists Afterpay, alipay_sg_pos, Clearpay, maestro_USA and PayPal as following method schedules instead of the cutoff (lines 30–34). Its prose says the sample funds become available after two business days, but the test PATCH contains only `salesDayClosingTime=01:00`; a later webhook sample says 06:00 whereas request/response show 01:00 (lines 51, 58–68, 289–313, 333–335). These are settings examples, not proof of a specific settlement batch, payout or bank receipt. Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-settle-funds-configure-closing-time]] → [[raw/adyen/docs/marketplaces/settle-funds/configure-closing-time/2026-09-15]].
