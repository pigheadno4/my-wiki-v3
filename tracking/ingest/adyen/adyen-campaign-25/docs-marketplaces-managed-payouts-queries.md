# C25 query checks — docs-marketplaces-managed-payouts

## Q1 — Purpose and prerequisites
Q: What is a Marketplace managed payout schedule, and where can it be applied?
A: It automates payouts from users' balance accounts; an Adyen contact helps configure the schedule. Each schedule supports one location/currency and applies to balance accounts of the same location/currency, with one managed schedule per currency on each account. It supports local same-country/same-currency payouts; other currency or bank-country routes use custom payouts. See raw/adyen/docs/marketplaces/managed-payouts/2026-09-15.md:19-37.
Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-managed-payouts]] → [[raw/adyen/docs/marketplaces/managed-payouts/2026-09-15]].

## Q2 — Timing and outcome boundary
Q: Does an accelerated managed schedule shorten all payment settlement delays or prove funds reached the user's bank by its ETA?
A: No. The source says managed schedules do not change pass-through or sales-day-payout settlement at T+7 or longer; those funds pay out once settled. Standard/Accelerated and weekday/weekly/monthly choices are schedule parameters, while ETA is explicitly estimated from location/currency cutoffs and contract terms. The US USD 200/100 and 9 AM example is illustrative; this page routes to separate execution evidence and contains no bank-receipt result. See raw/adyen/docs/marketplaces/managed-payouts/2026-09-15.md:33-49, :51-75, :89-102.
Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-managed-payouts]] → [[raw/adyen/docs/marketplaces/managed-payouts/2026-09-15]].
