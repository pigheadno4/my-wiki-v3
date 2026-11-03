# Adyen C64 collected API Explorer ingestion selection

Status: **COMPLETE — all 50 sources approved and validated**. Prepared2026-11-02.

Approved collection completed for all50 exact URLs: **50 HTTP200 complete-body pages**, no failed, title-only or mismatched responses. Family counts: **Checkout2 + Balance Platform48**. Every new response body is preserved byte-for-byte after collection metadata in a dated2026-11-02 raw file. All prior Adyen raw/wiki hashes unchanged. These mechanical title/body/byte checks are collection validation, not full semantic source reads. [Collection manifest](../../../collections/adyen/c64-collection-2026-11-02/manifest.md), [summary](../../../collections/adyen/c64-collection-2026-11-02/summary.json). Earlier collection proposal retained in [collection-selection-review.md](collection-selection-review.md).

Exact proposed ingestion: **50 source units**, **100 fixed answers**, **three predetermined distinct full-read audits**. All hashes, URL/target uniqueness, absent canonical targets and unreferenced raw pins verified. Size: **97,938 whitespace words, 10,780 raw lines, 615,096 bytes**. Source generation begins only after separate exact ingestion approval.

Current baseline **2,909 = 2,547 General Docs +346 API Explorer +16 GitHub**. Successful ingestion of all50 gives **2,959 = 2,547 General Docs +396 API Explorer +16 GitHub**. API Explorer now has423 local raw pages:346 ingested complete-body,50 newly collected complete-body and27 excluded stubs. Unreferenced local raw would decline77→27 after successful ingestion. The captured670-URL catalog has **247 URLs still without local raw** after this collection; the27 stub exclusions remain separate. This is captured-catalog coverage, not current upstream completeness.

[Exact proposed provider authorization](dispatch-contract.md) retains ten shared rolling child slots, medium gpt-6-sol workers/different high initial reviewers, full numbered raw reads of every schema/example,3–5locatedquotes, concept audit first, max3attempts, coordinator-only serial approved concept-before-source promotion and aggregate close once. [100 original fixed prompts](proposed-queries.md) require actual independently checked answers.

Fixed coordinator audit jobs: `api-explorer-balanceplatform-latest-get-balanceplatforms-id`, `api-explorer-balanceplatform-latest-patch-paymentinstruments-id`, `api-explorer-checkout-latest-post-verifyshoppertaxidentification`. Material partial/fail expands to all50. No runtime, dispatch, wiki source generation, commit or push. Unrelated work preserved. Await separate exact C64 ingestion approval.

| # | Family | Operation | Words | Raw lines |
| --- | --- | --- | ---: | ---: |
| 1 | Checkout | POST /verifyShopperTaxIdentification | 685 | 105 |
| 2 | Checkout | POST /calculateTax | 915 | 120 |
| 3 | balanceplatform | GET /balancePlatforms/{id} | 1,362 | 208 |
| 4 | balanceplatform | GET /balancePlatforms/{id}/accountHolders | 2,418 | 270 |
| 5 | balanceplatform | GET /balancePlatforms/{id}/transactionRules | 3,153 | 245 |
| 6 | balanceplatform | PATCH /accountHolders/{id} | 3,675 | 336 |
| 7 | balanceplatform | GET /accountHolders/{id} | 2,880 | 301 |
| 8 | balanceplatform | GET /accountHolders/{id}/balanceAccounts | 1,933 | 258 |
| 9 | balanceplatform | GET /accountHolders/{id}/taxForms | 1,684 | 248 |
| 10 | balanceplatform | GET /accountHolders/{id}/taxFormSummary | 236 | 60 |
| 11 | balanceplatform | GET /accountHolders/{id}/transactionRules | 3,153 | 245 |
| 12 | balanceplatform | PATCH /balanceAccounts/{id} | 2,235 | 257 |
| 13 | balanceplatform | GET /balanceAccounts/{id} | 1,903 | 237 |
| 14 | balanceplatform | GET /balanceAccounts/{id}/paymentInstruments | 2,653 | 297 |
| 15 | balanceplatform | GET /balanceAccounts/{id}/transactionRules | 3,153 | 245 |
| 16 | balanceplatform | POST /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings | 2,045 | 217 |
| 17 | balanceplatform | PATCH /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings/{settingId} | 2,029 | 254 |
| 18 | balanceplatform | GET /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings/{settingId} | 1,550 | 174 |
| 19 | balanceplatform | GET /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings | 1,581 | 195 |
| 20 | balanceplatform | DELETE /balancePlatforms/{balancePlatformId}/webhooks/{webhookId}/settings/{settingId} | 1,308 | 138 |
| 21 | balanceplatform | GET /balancePlatforms/{balancePlatformId}/payoutSchedules | 1,561 | 130 |
| 22 | balanceplatform | GET /balancePlatforms/{balancePlatformId}/payoutSchedules/{id} | 1,462 | 123 |
| 23 | balanceplatform | POST /balanceAccounts/{balanceAccountId}/payoutSchedules | 2,074 | 181 |
| 24 | balanceplatform | GET /balanceAccounts/{balanceAccountId}/payoutSchedules | 1,803 | 173 |
| 25 | balanceplatform | GET /balanceAccounts/{balanceAccountId}/payoutSchedules/{id} | 1,515 | 145 |
| 26 | balanceplatform | PATCH /balanceAccounts/{balanceAccountId}/payoutSchedules/{id} | 2,030 | 172 |
| 27 | balanceplatform | DELETE /balanceAccounts/{balanceAccountId}/payoutSchedules/{id} | 888 | 99 |
| 28 | balanceplatform | GET /balanceAccounts/{balanceAccountId}/payoutSchedules/{id}/executions | 1,246 | 148 |
| 29 | balanceplatform | POST /balanceAccounts/{balanceAccountId}/sweeps | 3,829 | 383 |
| 30 | balanceplatform | PATCH /balanceAccounts/{balanceAccountId}/sweeps/{sweepId} | 3,677 | 282 |
| 31 | balanceplatform | GET /balanceAccounts/{balanceAccountId}/sweeps | 2,678 | 266 |
| 32 | balanceplatform | GET /balanceAccounts/{balanceAccountId}/sweeps/{sweepId} | 2,519 | 249 |
| 33 | balanceplatform | DELETE /balanceAccounts/{balanceAccountId}/sweeps/{sweepId} | 1,313 | 192 |
| 34 | balanceplatform | GET /balanceAccounts/{balanceAccountId}/sweeps/{sweepId}/executions | 1,419 | 156 |
| 35 | balanceplatform | POST /paymentInstruments/{paymentInstrumentId}/authorisedCardUsers | 1,018 | 171 |
| 36 | balanceplatform | GET /paymentInstruments/{paymentInstrumentId}/authorisedCardUsers | 1,006 | 171 |
| 37 | balanceplatform | PATCH /paymentInstruments/{paymentInstrumentId}/authorisedCardUsers | 1,019 | 173 |
| 38 | balanceplatform | DELETE /paymentInstruments/{paymentInstrumentId}/authorisedCardUsers | 502 | 88 |
| 39 | balanceplatform | POST /balanceAccounts/{balanceAccountId}/recurringTopUps | 2,246 | 318 |
| 40 | balanceplatform | GET /balanceAccounts/{balanceAccountId}/recurringTopUps | 1,618 | 233 |
| 41 | balanceplatform | PATCH /balanceAccounts/{balanceAccountId}/recurringTopUps/{topUpId} | 2,059 | 294 |
| 42 | balanceplatform | DELETE /balanceAccounts/{balanceAccountId}/recurringTopUps/{topUpId} | 1,473 | 224 |
| 43 | balanceplatform | PATCH /paymentInstruments/{id} | 4,646 | 370 |
| 44 | balanceplatform | GET /paymentInstruments/{id} | 3,221 | 286 |
| 45 | balanceplatform | GET /paymentInstruments/{id}/reveal | 1,425 | 218 |
| 46 | balanceplatform | GET /paymentInstruments/{id}/networkTokens | 1,641 | 210 |
| 47 | balanceplatform | GET /paymentInstruments/{id}/transactionRules | 3,265 | 305 |
| 48 | balanceplatform | GET /paymentInstruments/{id}/networkTokenActivationData | 1,366 | 196 |
| 49 | balanceplatform | POST /paymentInstruments/{id}/networkTokenActivationData | 1,448 | 202 |
| 50 | balanceplatform | GET /paymentInstrumentGroups/{id} | 1,420 | 212 |

User approved exact C64 ingestion on2026-11-02 after50hash/count checks. Historical preparation statements above retain their pre-approval meaning. No commit/push.

C64 closed: 2959 total sources; 396 API Explorer sources. Remaining 27 API raw pages are excluded title-only stubs. No commit/push.
