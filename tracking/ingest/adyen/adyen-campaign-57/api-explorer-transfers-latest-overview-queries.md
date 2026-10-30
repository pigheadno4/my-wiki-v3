# Fixed retrieval answers: api-explorer-transfers-latest-overview

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-transfers-latest-overview.md` — https://docs.adyen.com/api-explorer/transfers/latest/overview

## Q1: For `transfers/latest/overview`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

The captured **Transfers API v4** overview covers funds transfers for platform/marketplace payouts to transfer instruments, Business Account users' third-party sends, Capital grant-offer payouts, and transaction/grant-balance reads. Each request needs an API key in `X-API-Key`; the key-generation context differs for Platforms/Marketplace versus Issuing. An additional credential role is required, and transfers must be enabled on the source balance account; an Adyen contact sets up roles/permissions. The page supplies an endpoint catalog, not endpoint body fields or named role identifiers. [Raw lines 5–26, 43–59.]

## Q2: What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

The overview contains no endpoint response/error schemas or executed examples. It says Transfers API v1/v2 are deprecated and shows version suffix `vXX`, captured v4 test base `/btl/v4`, and a separate live-key/live-base setup path. Its GET/POST grants, transactions, transfers, approve/cancel/return and cashout rows are navigation; they do not establish exact fields, transfer approval, deletion, webhook propagation, funds booking, settlement, bank receipt, current availability or a specific account's eligibility. [Raw lines 5–7, 28–41, 43–59.]
