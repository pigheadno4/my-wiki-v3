# Fixed-query audit: api-explorer-fund-latest-post-accountholdertransactionlist

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-fund-latest-post-accountholdertransactionlist.md` — https://docs.adyen.com/api-explorer/Fund/latest/post/accountHolderTransactionList
Pinned evidence: `raw/adyen/api-explorer/Fund/latest/post/accountHolderTransactionList/2026-09-15.md` (SHA-256 `2af465d0796823de63eea3fa0051b605a05959733b1e4db9225d24cf0e262ea2`).

## Q1

For `Fund/latest/post/accountHolderTransactionList`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** The Fund v6 TEST endpoint returns transactions for a Classic account holder's accounts (raw lines 5–10). `accountHolderCode` is required; `transactionListsPerAccount` and `transactionStatuses` are optional. If the account-list selector is omitted, the last 50 transactions for all holder accounts are included; within a supplied account selector, `accountCode` and `page` are required. Page 1 is newest, each page has 50 per account, and the page says to increment `page` for older transactions (lines 7, 14–21). Omitting the status filter includes all statuses; permitted values are listed at line 21. The schema shows no date-range request field. 401/403 describe authentication and permission gates (lines 144–158). Retrieve `wiki/sources/adyen/source-adyen-api-explorer-fund-latest-post-accountholdertransactionlist.md` at https://docs.adyen.com/api-explorer/Fund/latest/post/accountHolderTransactionList.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** A 200 says the request succeeded; a 202 says it was accepted for processing but processing is incomplete (raw lines 57–58, 94–95). Both schemas show optional per-account transaction lists, `hasNextPage`, and metadata including `creationDate`, references, source/destination account codes, `transactionStatus`, and transfer code (lines 60–128). Status values include pending, failed, reversed, `Payout`, and `PayoutReversed` (lines 21, 81, 118). A payout listing, payout reference, or destination bank details does not establish receiving-bank receipt; this endpoint does not report a bank confirmation. The page lists 400, 401, 403, 422, and 500 errors (lines 131–193). Its only listed server is Fund v6 TEST (lines 9–10), captured 2026-09-15 (line 2); it does not prove current live availability, account balances, verification approval, or a completed money movement. Retrieve `wiki/sources/adyen/source-adyen-api-explorer-fund-latest-post-accountholdertransactionlist.md` at https://docs.adyen.com/api-explorer/Fund/latest/post/accountHolderTransactionList.
