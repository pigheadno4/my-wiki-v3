# C17 internal-transfer webhook retrieval checks

## Q1 — Scope and stage boundary

Query: Which webhooks identify an Adyen for Platforms internal transfer, and does an authorised event show that funds reached a bank account?

Expected route: `wiki/adyen-index.md` → `wiki/concepts/adyen-platform-internal-transfers.md` → `wiki/sources/adyen/source-adyen-docs-platforms-internal-fund-transfers-internal-transfer-webhooks.md` → pinned `raw/adyen/docs/platforms/internal-fund-transfers/internal-transfer-webhooks/2026-09-15.md`. Answer: Transfer-webhook `created` and `updated` events with category `internal`, type `internalTransfer`, and outgoing source/incoming target account views. `received` is initiation, `authorised` is reserved, and `booked` describes an internal balance-account push; none is an external user-bank payout or beneficiary-bank receipt. Raw locators: lines 19–54, 375–385, 515–524, 683–693.

## Q2 — IDs, signs, returns, and example warnings

Query: How should a consumer distinguish the two internal-transfer legs and a return modification without assuming one shared ID or retrying an unfinished operation?

Expected route: `wiki/adyen-index.md` → `wiki/concepts/adyen-platform-internal-transfers.md` → `wiki/sources/adyen/source-adyen-docs-platforms-internal-fund-transfers-internal-transfer-webhooks.md` → pinned `raw/adyen/docs/platforms/internal-fund-transfers/internal-transfer-webhooks/2026-09-15.md`. Answer: inspect `balanceAccountId`, `direction`, `counterparty.balanceAccountId`, status and signed received/reserved/balance fields per account. The examples have distinct top-level transfer and booked transaction IDs on outgoing versus incoming legs. A return appears under nested `events[].modification` with received, authorised and booked stages while the original top-level transfer can remain booked; the page gives no failure/retry algorithm. Request amount 10000 versus webhook 1000, malformed JSON, `valuDate`, and a mismatched return modification ID make examples unsuitable as an exact cross-leg join contract. Raw locators: lines 56–80, 375–511, 515–885, 905–918, 1033–1040, 1174–1459.
