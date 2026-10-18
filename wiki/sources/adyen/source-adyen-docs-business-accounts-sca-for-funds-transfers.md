---
title: "Adyen Business Accounts: SCA for funds transfers"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/sca-for-funds-transfers"
raw_files:
  - "adyen/docs/business-accounts/sca-for-funds-transfers/2026-09-15.md"
tags: [adyen, business-accounts, sca, funds-transfers, authentication]
---

## Overview

Adyen's 2022-modified, 2026-09-15-captured Business Accounts guide describes using its Authentication SDK to authenticate EEA users for funds transfers. It has two routes: authenticate the initiating user on `POST /transfers`, or authenticate a reviewer on `POST /transfers/approve` for one or more pending transfers. This is an SCA procedure for a balance-platform transfer, not evidence of account opening, completed settlement, or recipient bank receipt. [[adyen-business-accounts]] [[adyen]]

## Key takeaways

- Prerequisites in this captured guide are an installed Authentication SDK, a user device registered for SCA, and an API credential with the **TransferService Webservice Initiate role** (raw lines 26–31). Check device or browser availability first and pass its `sdkOutput` from the client to the server; the web example throws `SCA_UNAVAILABLE` if unsupported (raw lines 33–127).
- For authentication during initiation, the first `POST /transfers` uses a `WWW-Authenticate` header with realm `Transfer` and availability `sdkOutput` as `auth-param1`; the illustrated bank transfer identifies a source `balanceAccountId`, `amount`, and target `counterparty.bankAccount` (raw lines 140–155). The documented 401 challenge carries `auth-param1`; pass that to the SDK as `sdkInput`, then repeat `POST /transfers` with the authenticated `sdkOutput` and matching body parameters (raw lines 575–626, 1435–1452).
- For authentication during approval, create the transfer with `review.numberOfApprovalsRequired` and `review.scaOnApproval=true`, retain its returned `id`, and challenge `POST /transfers/approve` with realm `ApproveTransfers` and eligible `transferIds` (raw lines 628–644, 1110–1122). The documented 401 challenge provides SDK input; after authentication, repeat the approval request with the authenticated `sdkOutput` and matching body parameters. The page calls for HTTP 200 with authorised header and an authorised `balancePlatform.transfer.updated` webhook (raw lines 1321–1349, 1906–1917, 2117–2119).
- The page says the authentication and finalization window is **10 minutes**. It says the user must see amount and payee when authenticating; a push notification is recommended as one way to present them (raw lines 1351–1358). The SDK returns authenticated `sdkOutput` to send to the server (raw lines 1362–1424).
- Treat the examples cautiously: the initiation finalization table names `counterparty.balanceAccountId` while the initial request and final response use `counterparty.bankAccount` (raw lines 152, 1452, 1885–1895); several finalization code samples use category `internal` while the table and response say `bank` (raw lines 1447, 1740–1741, 1885). The prose says an authorised response header means request/authentication success, but its example response body remains `status: received` and `reason: pending` (raw lines 1872–1903). Do not infer settlement or bank receipt from that example.

## Detail locators

- Device and browser SDK availability examples: raw lines 39–127; authentication examples and cancellation/error branches: raw lines 1362–1424.
- Initiation route request and challenge: raw lines 140–155 and 575–626; approval route review fields, transfer ID, challenge: raw lines 628–644, 1110–1122, 1321–1349.
- Finalization request and response examples: raw lines 1435–1904 and 1906–2119. The captured snippets use TEST hosts and dated client-library versions; they do not establish current API or account eligibility.

## Related

- [[adyen-business-accounts]] — Business Accounts product and resource scope.
- [[source-adyen-docs-business-accounts-manage-access]] — API credential roles.
- [[source-adyen-docs-business-accounts-create-business-accounts]] — separate business-account creation flow.
- [[source-adyen-docs-platforms-transfer-transactions-track-webhooks]] — transfer lifecycle tracking beyond authentication.

## Raw Sources

- [[raw/adyen/docs/business-accounts/sca-for-funds-transfers/2026-09-15|Captured SCA for funds transfers guide]]
