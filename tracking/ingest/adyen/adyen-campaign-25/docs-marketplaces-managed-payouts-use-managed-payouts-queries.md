# docs-marketplaces-managed-payouts-use-managed-payouts retrieval probes

## Q1 — How does a marketplace apply a managed payout schedule, and what must be in place?

Answer: An Adyen contact first configures the platform-level managed schedule. The platform can then apply it to a user balance account through Customer Area or Configuration API, or enable automatic application through its Adyen contact for new qualifying accounts. The API credential, Customer Area roles, Configuration/Scheduled payout webhooks, and user's `sendToTransferInstrument` capability are listed at raw lines 27–47. The one-per-currency/location limits are at lines 41–45. Automatic application and its eligibility, existing-legal-entity exclusion, pending retry behavior, and closing-time/rail validation are at lines 207–257. Manual/API application is at lines 258–406.

Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-managed-payouts-use-managed-payouts]] → [[raw/adyen/docs/marketplaces/managed-payouts/use-managed-payouts/2026-09-15]].

## Q2 — Does application mean payout or bank success, and how should deactivation/failure be read?

Answer: No. Configuration API HTTP 200 and created webhook demonstrate schedule application in the TEST scenarios (raw lines 651–659); managed schedules do not override the stated settlement delays (line 47). Automatic application may stay pending with later retry if eligibility conditions fail (lines 230–243), while closing-time/rail checks may fall back or fail (lines 245–257). The deactivation section says PATCH for temporary deactivation but its curl uses DELETE/HTTP 204, the same operation shown under deletion (lines 585–649); do not prescribe that example as safe temporary deactivation. Active schedules block `timeZone` changes until deletion; country mismatch fails (lines 660–661). The bank details table is TEST-only (lines 663–691).

Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-managed-payouts-use-managed-payouts]] → [[raw/adyen/docs/marketplaces/managed-payouts/use-managed-payouts/2026-09-15]].
