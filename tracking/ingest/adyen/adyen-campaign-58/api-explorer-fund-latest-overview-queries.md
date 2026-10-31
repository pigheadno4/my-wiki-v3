# Fixed retrieval audit — api-explorer-fund-latest-overview

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-fund-latest-overview.md` — https://docs.adyen.com/api-explorer/Fund/latest/overview
Pinned raw: `raw/adyen/api-explorer/Fund/latest/overview/2026-09-15.md`

## Q1

**Prompt:** For `Fund/latest/overview`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** The page is the Classic Platforms **Fund API v6** overview for managing funds in platform accounts. It gives transfer, payout-to-account-holder, and balance retrieval as examples, and catalogs eight POST endpoints: `/accountHolderBalance`, `/accountHolderTransactionList`, `/debitAccountHolder`, `/payoutAccountHolder`, `/refundFundsTransfer`, `/refundNotPaidOutTransfers`, `/setupBeneficiary`, and `/transferFunds`. It says an Adyen contact supplies a credential/API key; `X-API-Key` and basic username/password authentication are shown as alternatives. New web-service-user credentials are needed for live access. This overview supplies no individual operation fields or specific permission roles. See canonical source Overview, Key takeaways, Detail locators; raw lines 5–29 and 42–54.

## Q2

**Prompt:** What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** This is a catalog and setup overview, without operation-specific request/response schemas, status/error tables, idempotency, lifecycle, deletion effects, propagation, webhook outcomes, or money-movement evidence. Its version suffix example and listed server are TEST Fund `/v6`; `latest` is only in the documentation route. The page explicitly calls this the Classic integration and sends new implementations to a separate guide, so its account-holder/account identifiers cannot be mapped by assumption to newer balance-platform Transfers API objects. Live credentials must be newly generated; the capture does not establish current production availability, eligibility, an executed transfer or payout, or bank receipt. See canonical source Overview and Key takeaways; raw lines 5–11, 29–40, 42–54.
