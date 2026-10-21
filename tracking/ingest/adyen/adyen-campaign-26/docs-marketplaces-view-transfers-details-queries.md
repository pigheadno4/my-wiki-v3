# docs-marketplaces-view-transfers-details retrieval probes

## Q1 — How can a Marketplace inspect transfers, and what access is required?

Answer: With an Adyen for Platforms integration, the API needs **TransferService Webservice Retrieve role** and Customer Area viewing needs **Balance platform base role** (raw lines 35–43). Customer Area **Balances → Transfers** filters one balance platform at a time; PSP payment reference can find related payment transfers (lines 45–69). GET `/transfers` lists matching transfers with date/account filters and pagination (lines 71–83, 264–270), while GET `/transfers/{id}` returns a specific transfer's amount, direction, events, reference and status (lines 476–497, 643–651). Webhooks are the recommended recurring tracking route (lines 19–33).

Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-view-transfers-details]] → [[raw/adyen/docs/marketplaces/view-transfers-details/2026-09-15]].

## Q2 — What conflicts limit the list-query example, and does booked bank status prove receipt?

Answer: The parameter prose requires `createdSince`/`createdUntil` to be less than six months apart and says at least one unique identifier must be supplied (raw lines 77–83). Its explanatory example spans May 2025–May 2026, while curl uses May 2026 on both dates and no account/holder ID (lines 85–100). Treat those as conflicting examples, not a ready request. The illustrative bank transfer is `booked` but includes `reason: counterpartyAccountNotFound` and estimated arrival tracking (lines 273–390); no beneficiary-bank receipt is established. A specific-transfer response is recorded status/event detail, not an independent bank outcome (lines 643–737).

Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-view-transfers-details]] → [[raw/adyen/docs/marketplaces/view-transfers-details/2026-09-15]].
