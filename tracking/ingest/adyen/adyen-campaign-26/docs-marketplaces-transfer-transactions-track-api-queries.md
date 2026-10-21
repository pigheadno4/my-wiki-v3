# docs-marketplaces-transfer-transactions-track-api retrieval probes

## Q1 — How do Marketplace transaction queries scope and page balance-account ledger entries?

Answer: The Transfers API exposes GET `/transactions` for platform, account-holder or balance-account scope (raw lines 15–19). The guide lists Adyen for Platforms/Issuing/Payouts integration, **TransferService Webservice Retrieve role**, and transfers enabled on the source account (lines 21–27). Supply at least one platform/holder/account identifier and ISO 8601 `createdSince`/`createdUntil`; optional paging/filter fields include `limit`, `sortOrder`, `cursor`, and `paymentInstrumentId` (lines 38–54). Follow `_links` cursor for further pages or GET `/transactions/{id}` for one row (lines 226–229, 354).

Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-transfer-transactions-track-api]] → [[raw/adyen/docs/marketplaces/transfer-transactions/track-api/2026-09-15]].

## Q2 — What do signed booked rows prove, and which examples conflict?

Answer: Positive `amount.value` is incoming to the balance account, negative is outgoing. Pending incoming is not yet added; pending outgoing is reserved; booked records balance-account addition/deduction. `bookingDate` and `valueDate` distinguish recorded reservation from availability/deduction (raw lines 356–368, 539–548). A booked payout debit is not independent beneficiary-bank receipt (lines 370–416). The list examples pair EUR-suffixed transaction IDs with USD amounts and show internal outgoing -10000 versus incoming +1000 with different transfer IDs (lines 231–352), so do not treat them as one reconciled transfer. The TEST curl has a bare `accountHolder` fragment and date-only values despite date-time parameter guidance (lines 44–66); verify request shape against the current contract.

Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-transfer-transactions-track-api]] → [[raw/adyen/docs/marketplaces/transfer-transactions/track-api/2026-09-15]].
