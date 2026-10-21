# Retrieval checks — docs-payouts-payout-service-balance-updates

Q1. What is this Payout Service-path Balance updates page for, and what setup and scope does it identify?

A1. It is a limited-availability/pilot balance-platform webhook overview for balance changes, not a payout-status webhook guide (raw lines 15–32). The process subscribes in Customer Area, gets a webhook ID and POSTs criteria through the Configuration API; targets are the platform, one account holder's accounts or one balance account (raw lines 34–47). Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-payouts-payout-service-balance-updates]] → [[raw/adyen/docs/payouts/payout-service/balance-updates/2026-09-15]].

Q2. Do inherited settings or this overview's “all conditions” line establish reliable compound-condition behavior or a completed payout?

A2. No. The page says broader settings are inherited and more granular settings override them, but the table also says the granular settings inherit higher-level settings without an exact merge rule (raw lines 49–57). It says all conditions match (raw line 47), while the linked configuration source's active row says any and its conditions row says all ([[source-adyen-docs-payouts-payout-service-balance-updates-configure-balance-webhook]], raw lines 88–90). A matching notification is not a funds move or beneficiary-bank receipt; payment/payout/refund examples only name possible balance-change causes (raw lines 24–32). Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-payouts-payout-service-balance-updates]] → [[raw/adyen/docs/payouts/payout-service/balance-updates/2026-09-15]].
