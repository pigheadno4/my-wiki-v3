# Fixed retrieval checks: docs-platforms-internal-fund-transfers-return-transfers

## Q1 — Return purpose, scope and identity

**Query:** What does this Platforms return-transfer guide return, and how does it differ from a new internal transfer or bank payout?

**Expected answer:** The 2020-modified, 2026-09-15-captured guide covers returning mistakenly moved funds from the recipient balance account to the sender's original source balance account. This route only applies when the original internal transfer was a **push** transfer. The return is handled as a modification of that original transfer, using its original incoming transfer ID; it is not a new internal transfer, an external payout to a bank, or proof of legal ownership. The return request receives its own ID while `transferId` remains the original incoming transfer ID. An `authorised` response is not proof that both balance-account legs are booked or that any bank received funds.

**Evidence locators:** `raw/adyen/docs/platforms/internal-fund-transfers/return-transfers/2026-09-15.md:15-21`, `:39-43`, `:293-314`. **Canonical route:** `[[adyen-index]]` → `[[adyen-platform-internal-transfers]]` → `[[source-adyen-docs-platforms-internal-fund-transfers-return-transfers]]` → pinned raw.

## Q2 — Requirements, exact request and outcome tracking

**Query:** What must be true before returning an internal push transfer, what must the POST contain, and how is its outcome checked?

**Expected answer:** The server must accept webhooks and have Transfer webhooks configured; Support must enable transfers for the balance account **where funds are returned from**. The credential needs Transfers API access and TransferService Webservice Initiate role. If the two balance accounts belong to different account holders, the holder of the returning account needs `sendToBalanceAccount` and the holder of the original source/return destination needs `receiveFromBalanceAccount`. POST `/transfers/{transferId}/returns` uses the original incoming transfer ID and a required amount whose currency and value match the original transfer; a unique return `reference` is optional in the page's table. The response separates return-request `id` from original `transferId`. `Declined` **can** indicate a wrong URL ID, but the page does not make that the only possible cause. Use actual return webhooks and their failure updates, or Customer Area, then the internal-transfer webhook guide for booked return modifications on both accounts; test examples and `authorised` status alone do not prove completed funds movement or establish a retry rule.

**Evidence locators:** `raw/adyen/docs/platforms/internal-fund-transfers/return-transfers/2026-09-15.md:23-50`, `:52-70`, `:293-314`. **Canonical route:** `[[adyen-index]]` → `[[adyen-platform-internal-transfers]]` → `[[source-adyen-docs-platforms-internal-fund-transfers-return-transfers]]` → pinned raw.
