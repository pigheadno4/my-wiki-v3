# Adyen C69 bounded API Explorer collection

Collection approved2026-11-07; collection completed. No ingestion or publication.

- status: COLLECTION_COMPLETE_AWAITING_INGESTION_APPROVAL
- selected: 47
- outcomes: {'new_complete_body_raw': 47}
- complete_body_pages: 47
- http_200: 47
- new_raw_sha256_verified: 47
- response_bytes_preserved: 47
- existing_adyen_raw_and_wiki_unchanged: True
- concurrent_unrelated_wiki_changes: []
- original_title_only_stubs_still_excluded: 27
- runtime_initialized: False
- ingestion_executed: False
- publication_executed: False

Body presence and identity screens are mechanical, not full semantic source reads. Every selected URL has a terminal outcome; per-attempt status/headers/body/hash retained. Server-set cookies omitted. Every accepted response body is byte-exact after collection metadata; prior accepted raw/wiki untouched.

| Item | Catalog operation | Outcome | New raw |
| --- | --- | --- | --- |
| c69-01 | POST /REVERSAL | new_complete_body_raw | `raw/adyen/api-explorer/Webhooks/latest/post/REVERSAL/2026-11-07.md` |
| c69-02 | POST /merchants/{merchantAccount}/devices/{deviceId}/sync | new_complete_body_raw | `raw/adyen/api-explorer/cloud-device-api/latest/post/merchants/(merchantAccount)/devices/(deviceId)/sync/2026-11-07.md` |
| c69-03 | POST /merchants/{merchantAccount}/devices/{deviceId}/async | new_complete_body_raw | `raw/adyen/api-explorer/cloud-device-api/latest/post/merchants/(merchantAccount)/devices/(deviceId)/async/2026-11-07.md` |
| c69-04 | GET /merchants/{merchantAccount}/devices/{deviceId}/status | new_complete_body_raw | `raw/adyen/api-explorer/cloud-device-api/latest/get/merchants/(merchantAccount)/devices/(deviceId)/status/2026-11-07.md` |
| c69-05 | GET /merchants/{merchantAccount}/connectedDevices | new_complete_body_raw | `raw/adyen/api-explorer/cloud-device-api/latest/get/merchants/(merchantAccount)/connectedDevices/2026-11-07.md` |
| c69-06 | POST /merchants/{merchantId}/generatePaymentsAppBoardingToken | new_complete_body_raw | `raw/adyen/api-explorer/payments-app/latest/post/merchants/(merchantId)/generatePaymentsAppBoardingToken/2026-11-07.md` |
| c69-07 | GET /merchants/{merchantId}/paymentsApps | new_complete_body_raw | `raw/adyen/api-explorer/payments-app/latest/get/merchants/(merchantId)/paymentsApps/2026-11-07.md` |
| c69-08 | POST /merchants/{merchantId}/paymentsApps/{installationId}/revoke | new_complete_body_raw | `raw/adyen/api-explorer/payments-app/latest/post/merchants/(merchantId)/paymentsApps/(installationId)/revoke/2026-11-07.md` |
| c69-09 | POST /merchants/{merchantId}/stores/{storeId}/generatePaymentsAppBoardingToken | new_complete_body_raw | `raw/adyen/api-explorer/payments-app/latest/post/merchants/(merchantId)/stores/(storeId)/generatePaymentsAppBoardingToken/2026-11-07.md` |
| c69-10 | GET /merchants/{merchantId}/stores/{storeId}/paymentsApps | new_complete_body_raw | `raw/adyen/api-explorer/payments-app/latest/get/merchants/(merchantId)/stores/(storeId)/paymentsApps/2026-11-07.md` |
| c69-11 | GET /merchants/{merchantId}/terminalThemes/{id} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/terminalThemes/(id)/2026-11-07.md` |
| c69-12 | POST /merchants/{merchantId}/terminalThemes | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes/2026-11-07.md` |
| c69-13 | POST /merchants/{merchantId}/terminalThemes/{id}/assets | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes/(id)/assets/2026-11-07.md` |
| c69-14 | POST /merchants/{merchantId}/terminalThemes/{id}/assets/replace | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes/(id)/assets/replace/2026-11-07.md` |
| c69-15 | DELETE /merchants/{merchantId}/terminalThemes/{id}/assets | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/delete/merchants/(merchantId)/terminalThemes/(id)/assets/2026-11-07.md` |
| c69-16 | PATCH /merchants/{merchantId}/terminalThemes/{id} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/terminalThemes/(id)/2026-11-07.md` |
| c69-17 | POST /merchants/{merchantId}/terminalThemes/{id}/apply | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes/(id)/apply/2026-11-07.md` |
| c69-18 | POST /merchants/{merchantId}/terminalThemes/unapply | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes/unapply/2026-11-07.md` |
| c69-19 | DELETE /merchants/{merchantId}/terminalThemes/{id} | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/delete/merchants/(merchantId)/terminalThemes/(id)/2026-11-07.md` |
| c69-20 | POST /stores/{storeId}/terminalThemes/{id}/apply | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/stores/(storeId)/terminalThemes/(id)/apply/2026-11-07.md` |
| c69-21 | POST /stores/{storeId}/terminalThemes/unapply | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/stores/(storeId)/terminalThemes/unapply/2026-11-07.md` |
| c69-22 | POST /terminals/{terminalId}/terminalThemes/{id}/apply | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/terminals/(terminalId)/terminalThemes/(id)/apply/2026-11-07.md` |
| c69-23 | POST /terminals/{terminalId}/terminalThemes/unapply | new_complete_body_raw | `raw/adyen/api-explorer/Management/latest/post/terminals/(terminalId)/terminalThemes/unapply/2026-11-07.md` |
| c69-24 | GET /balanceOverview/companies/{companyAccountCode}/balances | new_complete_body_raw | `raw/adyen/api-explorer/BalanceControl/latest/get/balanceOverview/companies/(companyAccountCode)/balances/2026-11-07.md` |
| c69-25 | GET /balanceOverview/merchants/{merchantAccountCode}/balances | new_complete_body_raw | `raw/adyen/api-explorer/BalanceControl/latest/get/balanceOverview/merchants/(merchantAccountCode)/balances/2026-11-07.md` |
| c69-26 | POST /transfers/{transferId}/returns | new_complete_body_raw | `raw/adyen/api-explorer/transfers/latest/post/transfers/(transferId)/returns/2026-11-07.md` |
| c69-27 | GET /transfers/{id} | new_complete_body_raw | `raw/adyen/api-explorer/transfers/latest/get/transfers/(id)/2026-11-07.md` |
| c69-28 | GET /transactions/{id} | new_complete_body_raw | `raw/adyen/api-explorer/transfers/latest/get/transactions/(id)/2026-11-07.md` |
| c69-29 | GET /grants/{id} | new_complete_body_raw | `raw/adyen/api-explorer/transfers/latest/get/grants/(id)/2026-11-07.md` |
| c69-30 | GET /disputes/{disputeId}/attachments | new_complete_body_raw | `raw/adyen/api-explorer/transfers-api/latest/get/disputes/(disputeId)/attachments/2026-11-07.md` |
| c69-31 | POST /disputes/{disputeId}/attachments | new_complete_body_raw | `raw/adyen/api-explorer/transfers-api/latest/post/disputes/(disputeId)/attachments/2026-11-07.md` |
| c69-32 | GET /disputes/{disputeId}/attachments/{attachmentId} | new_complete_body_raw | `raw/adyen/api-explorer/transfers-api/latest/get/disputes/(disputeId)/attachments/(attachmentId)/2026-11-07.md` |
| c69-33 | DELETE /disputes/{disputeId}/attachments/{attachmentId} | new_complete_body_raw | `raw/adyen/api-explorer/transfers-api/latest/delete/disputes/(disputeId)/attachments/(attachmentId)/2026-11-07.md` |
| c69-34 | GET /disputes/{id} | new_complete_body_raw | `raw/adyen/api-explorer/transfers-api/latest/get/disputes/(id)/2026-11-07.md` |
| c69-35 | PATCH /disputes/{id} | new_complete_body_raw | `raw/adyen/api-explorer/transfers-api/latest/patch/disputes/(id)/2026-11-07.md` |
| c69-36 | POST /dynamicOffers/{id}/calculate | new_complete_body_raw | `raw/adyen/api-explorer/capital/latest/post/dynamicOffers/(id)/calculate/2026-11-07.md` |
| c69-37 | POST /dynamicOffers/{id}/grantOffer | new_complete_body_raw | `raw/adyen/api-explorer/capital/latest/post/dynamicOffers/(id)/grantOffer/2026-11-07.md` |
| c69-38 | GET /grantOffers/{id} | new_complete_body_raw | `raw/adyen/api-explorer/capital/latest/get/grantOffers/(id)/2026-11-07.md` |
| c69-39 | GET /grants/{grantId} | new_complete_body_raw | `raw/adyen/api-explorer/capital/latest/get/grants/(grantId)/2026-11-07.md` |
| c69-40 | GET /grants/{grantId}/disbursements | new_complete_body_raw | `raw/adyen/api-explorer/capital/latest/get/grants/(grantId)/disbursements/2026-11-07.md` |
| c69-41 | GET /grants/{grantId}/disbursements/{disbursementId} | new_complete_body_raw | `raw/adyen/api-explorer/capital/latest/get/grants/(grantId)/disbursements/(disbursementId)/2026-11-07.md` |
| c69-42 | PATCH /grants/{grantId}/disbursements/{disbursementId} | new_complete_body_raw | `raw/adyen/api-explorer/capital/latest/patch/grants/(grantId)/disbursements/(disbursementId)/2026-11-07.md` |
| c69-43 | GET /grantAccounts/{id} | new_complete_body_raw | `raw/adyen/api-explorer/capital/latest/get/grantAccounts/(id)/2026-11-07.md` |
| c69-44 | GET /accountVerification/reports/{code} | new_complete_body_raw | `raw/adyen/api-explorer/open-banking/latest/get/accountVerification/reports/(code)/2026-11-07.md` |
| c69-45 | POST balancePlatform.balanceAccountSweepExecution.succeeded | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweepExecution.succeeded/2026-11-07.md` |
| c69-46 | POST balancePlatform.balanceAccountSweepExecution.failed | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweepExecution.failed/2026-11-07.md` |
| c69-47 | POST balancePlatform.balanceAccountSweepExecution.skipped | new_complete_body_raw | `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweepExecution.skipped/2026-11-07.md` |

Full evidence: page-results.json, summary.json and responses/. Separate exact ingestion approval required.
