# Q1 — purpose and prerequisites

**Question:** What does the Marketplace transaction-fees guide enable, and what prerequisite does it state?

**Answer:** It routes Adyen-calculated post-request transaction fees to the marketplace liable balance account by default and describes split instructions to book eligible payment-related fee types to a user's balance account. The stated prerequisite is an already payment-processing platform; the page says no further requirements for this feature. Processing/3DS aggregate costs and tiered-pricing discounts cannot be assigned to individual user payments through these requests. See raw lines 19, 21–37, 39–53. Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-transaction-fees]] → [[raw/adyen/docs/marketplaces/transaction-fees/2026-09-15]].

# Q2 — boundary, fallback and example conflict

**Question:** How do fee split priority and fallback work, and which example claims cannot be treated as one confirmed transaction?

**Answer:** `PaymentFee` is all fees, while `AcquiringFees` and `AdyenFees` are aggregates; more granular fee-type instructions override only their corresponding aggregate portion (raw lines 43–69). With no fee-booking instruction, Adyen inserts `PaymentFee` and books fees to liable (lines 53, 1450). The request/prose show EUR 80.00 but the illustrative authorization response EUR 400.00 (lines 97–102, 137–140, 795–800). The Adyen-fee tab says user while the request and transfer identify liable (lines 99–102, 168–172, 1137–1167), and later payload account/transfer/transaction IDs also conflict (lines 1008–1011, 1097–1133, 1384–1439). Thus example payloads do not establish a coherent captured/ booked ledger trace, payout, or bank receipt. Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-transaction-fees]] → [[raw/adyen/docs/marketplaces/transaction-fees/2026-09-15]].
