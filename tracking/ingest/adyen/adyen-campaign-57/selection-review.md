# Adyen C57 API Explorer selection and execution plan

Status: **COMPLETE — all 50 exact approved sources ingested and validated**.

C56 committed and pushed as `888d4eab427b884a55da61e0c4532f46aac0d566`, origin/main exact SHA verified. C57 proposes **50 complete-body local API Explorer pages**, excluding all 27 title-only stubs: **balanceplatform 21, transfers 9, legalentity 6, Management 12, foreignexchange 2**. The selection follows Platforms balance resources and transfers, onboarding/legal entities, merchant management and FX references. API-family and resource contracts remain separate.

Mechanical size: **111,021 whitespace words, 12,636 raw lines, 721,278 bytes**. This is metadata/body-presence preflight, not semantic reading or ingestion. No raw facts beyond metadata are synthesized here. All hashes pinned, latest local snapshots, exact URL case preserved, `.md` transport suffix removed, and all source targets absent/unreferenced. These are available local pins, not complete upstream endpoint coverage.

Baseline **2612 = 2547 General Docs + 50 API Explorer + 15 GitHub**. If all fifty pass, expected **2662 = 2547 General Docs + 100 API Explorer + 15 GitHub**. API raw pages remaining unreferenced would decline **313 → 263**, including 27 excluded incomplete stubs (236 other complete-body pages). Other API families and General Docs remain out of scope. Reconcile concurrent work at activation and close.

Use ten shared rolling child slots (not ten workers plus ten reviewers), proposed gpt-6-sol medium workers and different high reviewers, mandatory full raw/schema/example reads, 3–5 located exact quotes, full independent initial reviews, max three attempts, coordinator-only concept-before-source promotion and aggregate close once. No size waiver. [Proposed authorization](dispatch-contract.md).

Fixed root audits: `api-explorer-balanceplatform-latest-overview`, `api-explorer-legalentity-latest-post-legalentities`, `api-explorer-transfers-latest-post-transfers`. Material partial/fail expands audits to all fifty. [100 fixed query prompts](proposed-queries.md). Exhaustive structural checks and existing touched-file typed validation at close.

| # | Pinned raw | Words | Lines |
| --- | --- | ---: | ---: |
| 1 | `raw/adyen/api-explorer/balanceplatform/latest/overview/2026-09-15.md` | 1,334 | 137 |
| 2 | `raw/adyen/api-explorer/balanceplatform/latest/delete/scaAssociations/2026-09-15.md` | 754 | 99 |
| 3 | `raw/adyen/api-explorer/balanceplatform/latest/get/cardorders/2026-09-15.md` | 1,585 | 204 |
| 4 | `raw/adyen/api-explorer/balanceplatform/latest/get/grantOffers/2026-09-15.md` | 1,574 | 210 |
| 5 | `raw/adyen/api-explorer/balanceplatform/latest/get/mandates/2026-09-15.md` | 1,287 | 126 |
| 6 | `raw/adyen/api-explorer/balanceplatform/latest/get/publicKey/2026-09-15.md` | 1,162 | 183 |
| 7 | `raw/adyen/api-explorer/balanceplatform/latest/get/registeredDevices/2026-09-15.md` | 1,668 | 215 |
| 8 | `raw/adyen/api-explorer/balanceplatform/latest/get/scaAssociations/2026-09-15.md` | 1,345 | 163 |
| 9 | `raw/adyen/api-explorer/balanceplatform/latest/patch/scaAssociations/2026-09-15.md` | 903 | 128 |
| 10 | `raw/adyen/api-explorer/balanceplatform/latest/post/accountHolders/2026-09-15.md` | 3,540 | 331 |
| 11 | `raw/adyen/api-explorer/balanceplatform/latest/post/balanceAccounts/2026-09-15.md` | 2,397 | 346 |
| 12 | `raw/adyen/api-explorer/balanceplatform/latest/post/paymentInstrumentGroups/2026-09-15.md` | 1,516 | 225 |
| 13 | `raw/adyen/api-explorer/balanceplatform/latest/post/paymentInstruments/2026-09-15.md` | 5,134 | 579 |
| 14 | `raw/adyen/api-explorer/balanceplatform/latest/post/paymentInstruments/reveal/2026-09-15.md` | 1,408 | 209 |
| 15 | `raw/adyen/api-explorer/balanceplatform/latest/post/pins/change/2026-09-15.md` | 1,194 | 190 |
| 16 | `raw/adyen/api-explorer/balanceplatform/latest/post/pins/reveal/2026-09-15.md` | 1,188 | 188 |
| 17 | `raw/adyen/api-explorer/balanceplatform/latest/post/registeredDevices/2026-09-15.md` | 1,508 | 204 |
| 18 | `raw/adyen/api-explorer/balanceplatform/latest/post/scaDevices/2026-09-15.md` | 1,297 | 152 |
| 19 | `raw/adyen/api-explorer/balanceplatform/latest/post/transactionRules/2026-09-15.md` | 7,303 | 654 |
| 20 | `raw/adyen/api-explorer/balanceplatform/latest/post/transferRoutes/calculate/2026-09-15.md` | 1,850 | 275 |
| 21 | `raw/adyen/api-explorer/balanceplatform/latest/post/validateBankAccountIdentification/2026-09-15.md` | 1,187 | 222 |
| 22 | `raw/adyen/api-explorer/transfers/latest/overview/2026-09-15.md` | 425 | 59 |
| 23 | `raw/adyen/api-explorer/transfers/latest/get/grants/2026-09-15.md` | 1,795 | 169 |
| 24 | `raw/adyen/api-explorer/transfers/latest/get/transactions/2026-09-15.md` | 2,154 | 273 |
| 25 | `raw/adyen/api-explorer/transfers/latest/get/transfers/2026-09-15.md` | 4,925 | 437 |
| 26 | `raw/adyen/api-explorer/transfers/latest/post/cashouts/2026-09-15.md` | 2,504 | 259 |
| 27 | `raw/adyen/api-explorer/transfers/latest/post/grants/2026-09-15.md` | 2,076 | 232 |
| 28 | `raw/adyen/api-explorer/transfers/latest/post/transfers/2026-09-15.md` | 8,584 | 930 |
| 29 | `raw/adyen/api-explorer/transfers/latest/post/transfers/approve/2026-09-15.md` | 1,525 | 145 |
| 30 | `raw/adyen/api-explorer/transfers/latest/post/transfers/cancel/2026-09-15.md` | 1,831 | 156 |
| 31 | `raw/adyen/api-explorer/legalentity/latest/overview/2026-09-15.md` | 647 | 85 |
| 32 | `raw/adyen/api-explorer/legalentity/latest/get/themes/2026-09-15.md` | 753 | 143 |
| 33 | `raw/adyen/api-explorer/legalentity/latest/post/businessLines/2026-09-15.md` | 2,771 | 304 |
| 34 | `raw/adyen/api-explorer/legalentity/latest/post/documents/2026-09-15.md` | 1,933 | 198 |
| 35 | `raw/adyen/api-explorer/legalentity/latest/post/legalEntities/2026-09-15.md` | 12,992 | 1,133 |
| 36 | `raw/adyen/api-explorer/legalentity/latest/post/transferInstruments/2026-09-15.md` | 1,693 | 270 |
| 37 | `raw/adyen/api-explorer/Management/latest/overview/2026-09-15.md` | 1,580 | 178 |
| 38 | `raw/adyen/api-explorer/Management/latest/get/companies/2026-09-15.md` | 1,788 | 208 |
| 39 | `raw/adyen/api-explorer/Management/latest/get/me/2026-09-15.md` | 1,633 | 148 |
| 40 | `raw/adyen/api-explorer/Management/latest/get/me/allowedOrigins/2026-09-15.md` | 1,222 | 126 |
| 41 | `raw/adyen/api-explorer/Management/latest/get/merchants/2026-09-15.md` | 2,428 | 432 |
| 42 | `raw/adyen/api-explorer/Management/latest/get/stores/2026-09-15.md` | 2,311 | 251 |
| 43 | `raw/adyen/api-explorer/Management/latest/get/terminals/2026-09-15.md` | 2,134 | 228 |
| 44 | `raw/adyen/api-explorer/Management/latest/post/me/allowedOrigins/2026-09-15.md` | 1,302 | 138 |
| 45 | `raw/adyen/api-explorer/Management/latest/post/me/generateClientKey/2026-09-15.md` | 1,186 | 126 |
| 46 | `raw/adyen/api-explorer/Management/latest/post/merchants/2026-09-15.md` | 1,594 | 177 |
| 47 | `raw/adyen/api-explorer/Management/latest/post/stores/2026-09-15.md` | 2,759 | 242 |
| 48 | `raw/adyen/api-explorer/Management/latest/post/terminals/scheduleActions/2026-09-15.md` | 1,875 | 279 |
| 49 | `raw/adyen/api-explorer/foreignexchange/latest/overview/2026-09-15.md` | 238 | 51 |
| 50 | `raw/adyen/api-explorer/foreignexchange/latest/post/rates/calculate/2026-09-15.md` | 1,229 | 219 |

Five preparation artifacts only, uncommitted; no runtime, workers, candidates or canonical sources created. Awaiting separate exact C57 ingestion approval. No collection or provider operations.

User approved exact C57 ingestion on 2026-10-30. Runtime activated after hash/count reconciliation; historical preparation statements above describe pre-approval state. No commit/push.

C57 close verified: 2663 = 2547 General Docs + 100 API Explorer + 16 GitHub. Historical preparation/activation figures above retain their original meaning. All 50 sources promoted, query/audit/structural/typed checks pass. No commit/push.
