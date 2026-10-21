# C26 payout-transfer details retrieval checks

## Q1 — Purpose and prerequisites

**Query:** How can a Marketplace operator inspect payout-related transfers, and which roles are needed?

**Answer:** Use Customer Area Balances > Transfers to list and search, or the Transfers API `GET /transfers` and `GET /transfers/{id}`; webhooks are recommended for recurring tracking (raw lines 19–34, 47–72, 475–496). The guide requires Adyen for Platforms, TransferService Webservice Retrieve for API reads, Balance platform base for Customer Area viewing, Download transfer confirmation letter for a letter, and View bank transfers PII for unmasked letter PII (raw lines 35–45, 754–762). Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-view-payout-transfers-details]] → [[raw/adyen/docs/marketplaces/view-payout-transfers-details/2026-09-15]].

## Q2 — List constraints and payout proof

**Query:** Can the sample list request be copied as valid, and does a booked transfer or confirmation letter prove beneficiary receipt?

**Answer:** The page's table sets a less-than-six-month `createdSince`/`createdUntil` separation and the prose requires at least one unique identifier, yet its example prose spans May 2025–May 2026 and its test curl omits an account identifier; verify an executable request against the versioned API reference (raw lines 74–98). The detailed response sample is an internal transfer, not a bank payout (raw lines 652–735). A bank transfer letter confirms Adyen sent the transfer instruction; it does not establish bank credit or beneficiary receipt (raw lines 738–740). Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-view-payout-transfers-details]] → [[raw/adyen/docs/marketplaces/view-payout-transfers-details/2026-09-15]].
