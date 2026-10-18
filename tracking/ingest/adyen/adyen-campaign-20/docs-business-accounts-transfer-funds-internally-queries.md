# Business Accounts internal direct debit retrieval checks

## Q1 — Which balance account initiates the debit, and what must be ready?

**Answer:** The initiating source balance account sends a debit request to the target counterparty balance account. The platform liable account can pull a user's fee; the page also covers two users' balance accounts. The server must receive Transfer webhooks, the Customer Area must subscribe to them, Support must enable transfers for the account debited, and the initiating and request-receiving account holders need `sendToBalanceAccount` and `receiveFromBalanceAccount`, respectively. `POST /transfers` uses the source and target balance account IDs, amount, `category: internal`, and `type: internalDirectDebit` for this operation. The table does not mark `type` required even though the instruction says to set it. The table limits `referenceForBeneficiary` to alphanumeric characters, but its request examples contain hyphens; do not infer the examples' value is accepted, and check the current API reference for implementation.

**Evidence:** `raw/adyen/docs/business-accounts/transfer-funds-internally/2026-09-15.md:17-47,68-73,99-104,221-227`; especially 19, 23-30, 34-47, 71, 103 and 225. **Forward route:** `[[index]]` → `[[adyen-index]]` → `[[adyen-business-accounts]]` → `[[source-adyen-docs-business-accounts-transfer-funds-internally]]` → `[[raw/adyen/docs/business-accounts/transfer-funds-internally/2026-09-15]]`.

## Q2 — Does an authorised response prove the funds were moved or a bank received them?

**Answer:** No. The response's `status` and `reason` describe the transfer result, while separate webhook series for the source/outgoing and target/incoming legs track `received`, `authorised` (funds reserved), and `booked` (internal funds pulled from target to source), or failure. This is movement between balance accounts on one balance platform, not bank receipt. The published payloads are TEST examples, and the target booked JSON has a missing comma before `sequenceNumber`.

**Evidence:** `raw/adyen/docs/business-accounts/transfer-funds-internally/2026-09-15.md:373-447,758-764,858-863,943-952`. **Forward route:** `[[index]]` → `[[adyen-index]]` → `[[adyen-business-accounts]]` → `[[source-adyen-docs-business-accounts-transfer-funds-internally]]` → `[[raw/adyen/docs/business-accounts/transfer-funds-internally/2026-09-15]]`.
