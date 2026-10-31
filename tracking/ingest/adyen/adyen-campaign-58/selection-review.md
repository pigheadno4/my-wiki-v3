# Adyen C58 API Explorer selection and execution plan

Status: **COMPLETE — all 50 exact approved sources ingested and validated**.

C57 committed and pushed as `b7ac94175088d5937cd72b4197019e88b6e8de2e`, origin/main exact SHA verified. C58 proposes **50 complete-body local API Explorer pages**, excluding all 27 title-only stubs: **Account 21, Fund 9, Payout 7, NotificationConfiguration 7, postfmapi 6**. The selection covers the complete available local pins for five Classic/legacy API families, including deprecated POS Terminal Management. Preserve each capture's version, inactive/deprecated/migration notices and domain; Account/Fund contracts do not fill newer Configuration/Transfers schemas, Classic Payout is distinct from modern payouts, and legacy POS management does not substitute for Management API. No live eligibility is inferred.

Mechanical size: **98,589 whitespace words, 9,775 raw lines, 628,977 bytes**. This is metadata/body-presence preflight, not semantic reading or ingestion. No raw facts beyond metadata are synthesized here. All hashes pinned, latest local snapshots, exact URL case preserved, `.md` transport suffix removed, and all source targets absent/unreferenced. These are available local pins, not complete upstream endpoint coverage.

Baseline **2663 = 2547 General Docs + 100 API Explorer + 16 GitHub**. If all fifty pass, expected **2713 = 2547 General Docs + 150 API Explorer + 16 GitHub**. API raw pages remaining unreferenced would decline **263 → 213**, including 27 excluded incomplete stubs (186 other complete-body pages). Other API families and General Docs remain out of scope. Reconcile concurrent work at activation and close.

Use ten shared rolling child slots (not ten workers plus ten reviewers), proposed gpt-6-sol medium workers and different high reviewers, mandatory full raw/schema/example reads, 3–5 located exact quotes, full independent initial reviews, max three attempts, coordinator-only concept-before-source promotion and aggregate close once. No size waiver. [Proposed authorization](dispatch-contract.md).

Fixed root audits: `api-explorer-account-latest-overview`, `api-explorer-account-latest-post-updateaccountholder`, `api-explorer-fund-latest-post-transferfunds`. Material partial/fail expands audits to all fifty. [100 fixed query prompts](proposed-queries.md). Exhaustive structural checks and existing touched-file typed validation at close.

| # | Pinned raw | Words | Lines |
| --- | --- | ---: | ---: |
| 1 | `raw/adyen/api-explorer/Account/latest/overview/2026-09-15.md` | 400 | 66 |
| 2 | `raw/adyen/api-explorer/Account/latest/post/checkAccountHolder/2026-09-15.md` | 973 | 155 |
| 3 | `raw/adyen/api-explorer/Account/latest/post/closeAccount/2026-09-15.md` | 1,021 | 155 |
| 4 | `raw/adyen/api-explorer/Account/latest/post/closeAccountHolder/2026-09-15.md` | 2,089 | 191 |
| 5 | `raw/adyen/api-explorer/Account/latest/post/closeStores/2026-09-15.md` | 741 | 127 |
| 6 | `raw/adyen/api-explorer/Account/latest/post/createAccount/2026-09-15.md` | 1,718 | 180 |
| 7 | `raw/adyen/api-explorer/Account/latest/post/createAccountHolder/2026-09-15.md` | 7,975 | 552 |
| 8 | `raw/adyen/api-explorer/Account/latest/post/deleteBankAccounts/2026-09-15.md` | 949 | 155 |
| 9 | `raw/adyen/api-explorer/Account/latest/post/deleteLegalArrangements/2026-09-15.md` | 1,095 | 226 |
| 10 | `raw/adyen/api-explorer/Account/latest/post/deletePayoutMethods/2026-09-15.md` | 949 | 155 |
| 11 | `raw/adyen/api-explorer/Account/latest/post/deleteShareholders/2026-09-15.md` | 945 | 155 |
| 12 | `raw/adyen/api-explorer/Account/latest/post/deleteSignatories/2026-09-15.md` | 931 | 144 |
| 13 | `raw/adyen/api-explorer/Account/latest/post/getAccountHolder/2026-09-15.md` | 10,318 | 516 |
| 14 | `raw/adyen/api-explorer/Account/latest/post/getTaxForm/2026-09-15.md` | 826 | 140 |
| 15 | `raw/adyen/api-explorer/Account/latest/post/getUploadedDocuments/2026-09-15.md` | 1,223 | 147 |
| 16 | `raw/adyen/api-explorer/Account/latest/post/suspendAccountHolder/2026-09-15.md` | 2,046 | 191 |
| 17 | `raw/adyen/api-explorer/Account/latest/post/unSuspendAccountHolder/2026-09-15.md` | 2,086 | 194 |
| 18 | `raw/adyen/api-explorer/Account/latest/post/updateAccount/2026-09-15.md` | 1,730 | 182 |
| 19 | `raw/adyen/api-explorer/Account/latest/post/updateAccountHolder/2026-09-15.md` | 12,453 | 926 |
| 20 | `raw/adyen/api-explorer/Account/latest/post/updateAccountHolderState/2026-09-15.md` | 2,148 | 199 |
| 21 | `raw/adyen/api-explorer/Account/latest/post/uploadDocument/2026-09-15.md` | 9,208 | 463 |
| 22 | `raw/adyen/api-explorer/Fund/latest/overview/2026-09-15.md` | 327 | 54 |
| 23 | `raw/adyen/api-explorer/Fund/latest/post/accountHolderBalance/2026-09-15.md` | 1,470 | 157 |
| 24 | `raw/adyen/api-explorer/Fund/latest/post/accountHolderTransactionList/2026-09-15.md` | 1,969 | 193 |
| 25 | `raw/adyen/api-explorer/Fund/latest/post/debitAccountHolder/2026-09-15.md` | 1,712 | 183 |
| 26 | `raw/adyen/api-explorer/Fund/latest/post/payoutAccountHolder/2026-09-15.md` | 1,322 | 147 |
| 27 | `raw/adyen/api-explorer/Fund/latest/post/refundFundsTransfer/2026-09-15.md` | 1,089 | 140 |
| 28 | `raw/adyen/api-explorer/Fund/latest/post/refundNotPaidOutTransfers/2026-09-15.md` | 978 | 127 |
| 29 | `raw/adyen/api-explorer/Fund/latest/post/setupBeneficiary/2026-09-15.md` | 970 | 129 |
| 30 | `raw/adyen/api-explorer/Fund/latest/post/transferFunds/2026-09-15.md` | 1,138 | 139 |
| 31 | `raw/adyen/api-explorer/Payout/latest/overview/2026-09-15.md` | 409 | 78 |
| 32 | `raw/adyen/api-explorer/Payout/latest/post/confirmThirdParty/2026-09-15.md` | 994 | 152 |
| 33 | `raw/adyen/api-explorer/Payout/latest/post/declineThirdParty/2026-09-15.md` | 996 | 152 |
| 34 | `raw/adyen/api-explorer/Payout/latest/post/payout/2026-09-15.md` | 3,605 | 284 |
| 35 | `raw/adyen/api-explorer/Payout/latest/post/storeDetail/2026-09-15.md` | 2,209 | 186 |
| 36 | `raw/adyen/api-explorer/Payout/latest/post/storeDetailAndSubmitThirdParty/2026-09-15.md` | 2,343 | 182 |
| 37 | `raw/adyen/api-explorer/Payout/latest/post/submitThirdParty/2026-09-15.md` | 1,617 | 155 |
| 38 | `raw/adyen/api-explorer/NotificationConfiguration/latest/overview/2026-09-15.md` | 276 | 52 |
| 39 | `raw/adyen/api-explorer/NotificationConfiguration/latest/post/createNotificationConfiguration/2026-09-15.md` | 1,661 | 170 |
| 40 | `raw/adyen/api-explorer/NotificationConfiguration/latest/post/deleteNotificationConfigurations/2026-09-15.md` | 738 | 121 |
| 41 | `raw/adyen/api-explorer/NotificationConfiguration/latest/post/getNotificationConfiguration/2026-09-15.md` | 1,160 | 146 |
| 42 | `raw/adyen/api-explorer/NotificationConfiguration/latest/post/getNotificationConfigurationList/2026-09-15.md` | 1,159 | 151 |
| 43 | `raw/adyen/api-explorer/NotificationConfiguration/latest/post/testNotificationConfiguration/2026-09-15.md` | 939 | 152 |
| 44 | `raw/adyen/api-explorer/NotificationConfiguration/latest/post/updateNotificationConfiguration/2026-09-15.md` | 1,616 | 179 |
| 45 | `raw/adyen/api-explorer/postfmapi/latest/overview/2026-09-15.md` | 366 | 58 |
| 46 | `raw/adyen/api-explorer/postfmapi/latest/post/assignTerminals/2026-09-15.md` | 1,042 | 212 |
| 47 | `raw/adyen/api-explorer/postfmapi/latest/post/findTerminal/2026-09-15.md` | 886 | 169 |
| 48 | `raw/adyen/api-explorer/postfmapi/latest/post/getStoresUnderAccount/2026-09-15.md` | 1,025 | 215 |
| 49 | `raw/adyen/api-explorer/postfmapi/latest/post/getTerminalDetails/2026-09-15.md` | 1,568 | 222 |
| 50 | `raw/adyen/api-explorer/postfmapi/latest/post/getTerminalsUnderAccount/2026-09-15.md` | 1,181 | 251 |

Five preparation artifacts only, uncommitted; no runtime, workers, candidates or canonical sources created. Awaiting separate exact C58 ingestion approval. No collection or provider operations.

User approved exact C58 ingestion on 2026-10-31. Runtime activated after hash/count reconciliation; historical preparation statements above describe pre-approval state. No commit/push.

C58 close verified: 2713 = 2547 General Docs + 150 API Explorer + 16 GitHub. Historical preparation/activation figures above retain their original meaning. All 50 sources promoted, query/audit/structural/typed checks pass. No commit/push.
