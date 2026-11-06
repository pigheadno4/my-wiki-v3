# Adyen C69 collected API Explorer ingestion selection

Status: **COMPLETE — all 47 sources approved and validated**. Prepared 2026-11-07.

Approved collection completed for all47 exact URLs: **47 HTTP200 substantive Markdown pages**, no failed, title-only or mismatched documents. Families: **47 pages across ten API families**. Every response body is preserved byte-for-byte after collection metadata in a new dated2026-11-07 raw file. All prior Adyen raw/wiki hashes are unchanged; concurrent unrelated work is recorded separately. These title/body/byte checks are collection screening, not full semantic reads. [Collection manifest](../../../collections/adyen/c69-collection-2026-11-07/manifest.md), [summary](../../../collections/adyen/c69-collection-2026-11-07/summary.json). Original proposal retained in [collection-selection-review.md](collection-selection-review.md).

Exact proposed ingestion: **47 source units**, **94 fixed answers**, **three predetermined distinct full-read audits**. All hashes, URL/target uniqueness, absent canonical targets and unreferenced pins verified. Size: **47,181 whitespace words, 6,007 raw lines, 305,279 bytes**. Source generation begins only after separate exact ingestion approval.

Current baseline **3,159 = 2,547 General Docs +596 API Explorer +16 GitHub**. Successful ingestion of all47 gives **3,206 = 2,547 General Docs +643 API Explorer +16 GitHub**. API Explorer now has670 local raw pages:596 ingested substantive pages,47 newly collected and27 excluded title-only stubs. Unreferenced local raw would decline74→27 after successful ingestion. The captured670-URL catalog has **0 URLs still without local raw**; the27 stub exclusions remain separate. This is captured-catalog coverage, not a current upstream completeness claim.

[Proposed provider authorization](dispatch-contract.md) retains ten shared rolling child slots, medium gpt-6-sol workers/different high initial reviewers, full numbered reads of every schema/example,3–5locatedquotes, concept audit first, max3attempts, coordinator-only serial approved concept-before-source promotion and aggregate close once. [94 original fixed prompts](proposed-queries.md) require actual independently checked answers. Full raw reads apply to every captured schema, authentication/security qualification and example, including minimal references.

Fixed coordinator audit jobs: `api-explorer-management-latest-get-merchants-merchantid-terminalthemes-id`, `api-explorer-transfers-latest-get-transfers-id`, `api-explorer-cloud-device-api-latest-get-merchants-merchantaccount-devices-deviceid-status`. Material partial/fail expands to all47. No ingestion runtime, dispatch, canonical wiki source generation, commit or push. Await separate exact C69 ingestion approval.

| # | Family | Operation | Words | Raw lines |
| --- | --- | --- | ---: | ---: |
| 1 | Webhooks | POST /REVERSAL | 389 | 32 |
| 2 | cloud-device-api | POST /merchants/{merchantAccount}/devices/{deviceId}/sync | 228 | 45 |
| 3 | cloud-device-api | POST /merchants/{merchantAccount}/devices/{deviceId}/async | 260 | 45 |
| 4 | cloud-device-api | GET /merchants/{merchantAccount}/devices/{deviceId}/status | 698 | 123 |
| 5 | cloud-device-api | GET /merchants/{merchantAccount}/connectedDevices | 709 | 133 |
| 6 | payments-app | POST /merchants/{merchantId}/generatePaymentsAppBoardingToken | 1,371 | 151 |
| 7 | payments-app | GET /merchants/{merchantId}/paymentsApps | 1,270 | 143 |
| 8 | payments-app | POST /merchants/{merchantId}/paymentsApps/{installationId}/revoke | 743 | 89 |
| 9 | payments-app | POST /merchants/{merchantId}/stores/{storeId}/generatePaymentsAppBoardingToken | 1,384 | 152 |
| 10 | payments-app | GET /merchants/{merchantId}/stores/{storeId}/paymentsApps | 1,283 | 144 |
| 11 | Management | GET /merchants/{merchantId}/terminalThemes/{id} | 502 | 147 |
| 12 | Management | POST /merchants/{merchantId}/terminalThemes | 549 | 192 |
| 13 | Management | POST /merchants/{merchantId}/terminalThemes/{id}/assets | 875 | 210 |
| 14 | Management | POST /merchants/{merchantId}/terminalThemes/{id}/assets/replace | 885 | 213 |
| 15 | Management | DELETE /merchants/{merchantId}/terminalThemes/{id}/assets | 457 | 129 |
| 16 | Management | PATCH /merchants/{merchantId}/terminalThemes/{id} | 463 | 171 |
| 17 | Management | POST /merchants/{merchantId}/terminalThemes/{id}/apply | 257 | 97 |
| 18 | Management | POST /merchants/{merchantId}/terminalThemes/unapply | 310 | 109 |
| 19 | Management | DELETE /merchants/{merchantId}/terminalThemes/{id} | 271 | 113 |
| 20 | Management | POST /stores/{storeId}/terminalThemes/{id}/apply | 252 | 97 |
| 21 | Management | POST /stores/{storeId}/terminalThemes/unapply | 298 | 109 |
| 22 | Management | POST /terminals/{terminalId}/terminalThemes/{id}/apply | 287 | 115 |
| 23 | Management | POST /terminals/{terminalId}/terminalThemes/unapply | 325 | 127 |
| 24 | BalanceControl | GET /balanceOverview/companies/{companyAccountCode}/balances | 1,138 | 168 |
| 25 | BalanceControl | GET /balanceOverview/merchants/{merchantAccountCode}/balances | 1,111 | 167 |
| 26 | transfers | POST /transfers/{transferId}/returns | 1,996 | 171 |
| 27 | transfers | GET /transfers/{id} | 5,236 | 363 |
| 28 | transfers | GET /transactions/{id} | 1,521 | 168 |
| 29 | transfers | GET /grants/{id} | 1,867 | 173 |
| 30 | transfers-api | GET /disputes/{disputeId}/attachments | 675 | 84 |
| 31 | transfers-api | POST /disputes/{disputeId}/attachments | 830 | 97 |
| 32 | transfers-api | GET /disputes/{disputeId}/attachments/{attachmentId} | 820 | 93 |
| 33 | transfers-api | DELETE /disputes/{disputeId}/attachments/{attachmentId} | 692 | 85 |
| 34 | transfers-api | GET /disputes/{id} | 3,374 | 164 |
| 35 | transfers-api | PATCH /disputes/{id} | 3,692 | 178 |
| 36 | capital | POST /dynamicOffers/{id}/calculate | 807 | 83 |
| 37 | capital | POST /dynamicOffers/{id}/grantOffer | 807 | 84 |
| 38 | capital | GET /grantOffers/{id} | 890 | 89 |
| 39 | capital | GET /grants/{grantId} | 865 | 86 |
| 40 | capital | GET /grants/{grantId}/disbursements | 899 | 90 |
| 41 | capital | GET /grants/{grantId}/disbursements/{disbursementId} | 944 | 93 |
| 42 | capital | PATCH /grants/{grantId}/disbursements/{disbursementId} | 1,024 | 101 |
| 43 | capital | GET /grantAccounts/{id} | 719 | 80 |
| 44 | open-banking | GET /accountVerification/reports/{code} | 2,017 | 325 |
| 45 | balanceplatform-webhooks | POST balancePlatform.balanceAccountSweepExecution.succeeded | 394 | 59 |
| 46 | balanceplatform-webhooks | POST balancePlatform.balanceAccountSweepExecution.failed | 397 | 60 |
| 47 | balanceplatform-webhooks | POST balancePlatform.balanceAccountSweepExecution.skipped | 400 | 60 |

User approved exact C69 ingestion on2026-11-07 after47hash/count checks. Historical preparation statements above retain their pre-approval meaning. No commit/push.

C69 closed: 3206 total sources; 643 API Explorer sources. Remaining 27 API raw pages are excluded title-only stubs. No commit/push.
