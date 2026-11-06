# Adyen C69 API Explorer collection-first preparation

Status: **AWAITING EXACT COLLECTION APPROVAL — no ingestion-ready manifest**. Prepared 2026-11-07 after C68 publication `e40a2886f63e40cfd77d13c4cd00fa9b08eaecbd`.

C68 ingested all 50 Management pages. Current totals: **3,159 sources = 2,547 General Docs + 596 API Explorer + 16 GitHub**. All locally collected complete-body API Explorer pages are ingested. The only 27 unreferenced local raw pages are excluded title-only stubs, retried in C63 and still title-only. No repeated stub retries proposed here.

## Pinned catalog reconciliation

The official API Explorer catalog captured 2026-11-02 contains **670 distinct normalized documentation URLs** (623 operation references and 47 overview references). Exact-URL reconciliation on 2026-11-07 finds 623 local raw URLs: 596 with ingested raw and 27 excluded title-only stubs. **47 catalog URLs have no local raw**. All 623 local URLs occur in the pinned catalog. [Complete reconciliation](catalog-reconciliation.json) retains its SHA256 and all missing URLs.

This is reconciliation against an immutable captured catalog, not a refreshed upstream inventory or a claim about present page availability. No network requests or semantic reads of the proposed pages were made. Titles and paths identify navigation scope only.

## Exact next collection proposal

Propose **47 exact official Markdown URLs**: all 47 remaining uncollected references across the catalog families in captured order. Metadata scope covers the remaining references; family counts are recorded in the proposal. All navigation labels are listed below for inspection. No behavior is inferred from these names. Every selected URL has a pinned catalog-line locator; the documented duplicated API Explorer prefix is collapsed, retaining official case and parenthesized parameters. Every raw directory and provisional source target is absent and all URLs/targets are unique. [Exact 47-target proposal](collection-proposal.json).

Approval authorizes documentation collection for these 47 URLs only. Stage each response, retain status/headers/body/hash and final URL, omit server-set cookies from published metadata, and classify substantive/failed/title-only results separately. Preserve substantive body bytes verbatim in new dated immutable raw snapshots. No whole-corpus refresh, code/rule/validator changes, General Docs, GitHub, stub retries, provider/account/security/device/payment operations, automatic ingestion or further publication. Endpoint action names describe documentation targets, not authorized API calls.

After all 47 selected URLs reach recorded outcomes, reconcile results and prepare an exact ingestion manifest only from recovered complete-body evidence: raw SHA256 pins, actual fixed query prompts, three distinct audit samples and explicit provider review authorization. Obtain separate ingestion approval per rules/psp-collection.md. Do not pad failed or incomplete results or waive body/schema presence. If all 47 collect successfully, zero captured-catalog URLs would still lack raw; source counts rise only after approved ingestion.

C69 is **PREPARED ONLY / awaiting approval**. No runtime, dispatch, candidates, raw collection or canonical sources created. Publishing this proposal does not authorize execution.

| Item | Family | Catalog label | Exact Markdown URL |
| --- | --- | --- | --- |
| c69-01 | Webhooks | POST /REVERSAL | `https://docs.adyen.com/api-explorer/Webhooks/latest/post/REVERSAL.md` |
| c69-02 | cloud-device-api | POST /merchants/{merchantAccount}/devices/{deviceId}/sync | `https://docs.adyen.com/api-explorer/cloud-device-api/latest/post/merchants/(merchantAccount)/devices/(deviceId)/sync.md` |
| c69-03 | cloud-device-api | POST /merchants/{merchantAccount}/devices/{deviceId}/async | `https://docs.adyen.com/api-explorer/cloud-device-api/latest/post/merchants/(merchantAccount)/devices/(deviceId)/async.md` |
| c69-04 | cloud-device-api | GET /merchants/{merchantAccount}/devices/{deviceId}/status | `https://docs.adyen.com/api-explorer/cloud-device-api/latest/get/merchants/(merchantAccount)/devices/(deviceId)/status.md` |
| c69-05 | cloud-device-api | GET /merchants/{merchantAccount}/connectedDevices | `https://docs.adyen.com/api-explorer/cloud-device-api/latest/get/merchants/(merchantAccount)/connectedDevices.md` |
| c69-06 | payments-app | POST /merchants/{merchantId}/generatePaymentsAppBoardingToken | `https://docs.adyen.com/api-explorer/payments-app/latest/post/merchants/(merchantId)/generatePaymentsAppBoardingToken.md` |
| c69-07 | payments-app | GET /merchants/{merchantId}/paymentsApps | `https://docs.adyen.com/api-explorer/payments-app/latest/get/merchants/(merchantId)/paymentsApps.md` |
| c69-08 | payments-app | POST /merchants/{merchantId}/paymentsApps/{installationId}/revoke | `https://docs.adyen.com/api-explorer/payments-app/latest/post/merchants/(merchantId)/paymentsApps/(installationId)/revoke.md` |
| c69-09 | payments-app | POST /merchants/{merchantId}/stores/{storeId}/generatePaymentsAppBoardingToken | `https://docs.adyen.com/api-explorer/payments-app/latest/post/merchants/(merchantId)/stores/(storeId)/generatePaymentsAppBoardingToken.md` |
| c69-10 | payments-app | GET /merchants/{merchantId}/stores/{storeId}/paymentsApps | `https://docs.adyen.com/api-explorer/payments-app/latest/get/merchants/(merchantId)/stores/(storeId)/paymentsApps.md` |
| c69-11 | Management | GET /merchants/{merchantId}/terminalThemes/{id} | `https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/terminalThemes/(id).md` |
| c69-12 | Management | POST /merchants/{merchantId}/terminalThemes | `https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes.md` |
| c69-13 | Management | POST /merchants/{merchantId}/terminalThemes/{id}/assets | `https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes/(id)/assets.md` |
| c69-14 | Management | POST /merchants/{merchantId}/terminalThemes/{id}/assets/replace | `https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes/(id)/assets/replace.md` |
| c69-15 | Management | DELETE /merchants/{merchantId}/terminalThemes/{id}/assets | `https://docs.adyen.com/api-explorer/Management/latest/delete/merchants/(merchantId)/terminalThemes/(id)/assets.md` |
| c69-16 | Management | PATCH /merchants/{merchantId}/terminalThemes/{id} | `https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/terminalThemes/(id).md` |
| c69-17 | Management | POST /merchants/{merchantId}/terminalThemes/{id}/apply | `https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes/(id)/apply.md` |
| c69-18 | Management | POST /merchants/{merchantId}/terminalThemes/unapply | `https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes/unapply.md` |
| c69-19 | Management | DELETE /merchants/{merchantId}/terminalThemes/{id} | `https://docs.adyen.com/api-explorer/Management/latest/delete/merchants/(merchantId)/terminalThemes/(id).md` |
| c69-20 | Management | POST /stores/{storeId}/terminalThemes/{id}/apply | `https://docs.adyen.com/api-explorer/Management/latest/post/stores/(storeId)/terminalThemes/(id)/apply.md` |
| c69-21 | Management | POST /stores/{storeId}/terminalThemes/unapply | `https://docs.adyen.com/api-explorer/Management/latest/post/stores/(storeId)/terminalThemes/unapply.md` |
| c69-22 | Management | POST /terminals/{terminalId}/terminalThemes/{id}/apply | `https://docs.adyen.com/api-explorer/Management/latest/post/terminals/(terminalId)/terminalThemes/(id)/apply.md` |
| c69-23 | Management | POST /terminals/{terminalId}/terminalThemes/unapply | `https://docs.adyen.com/api-explorer/Management/latest/post/terminals/(terminalId)/terminalThemes/unapply.md` |
| c69-24 | BalanceControl | GET /balanceOverview/companies/{companyAccountCode}/balances | `https://docs.adyen.com/api-explorer/BalanceControl/latest/get/balanceOverview/companies/(companyAccountCode)/balances.md` |
| c69-25 | BalanceControl | GET /balanceOverview/merchants/{merchantAccountCode}/balances | `https://docs.adyen.com/api-explorer/BalanceControl/latest/get/balanceOverview/merchants/(merchantAccountCode)/balances.md` |
| c69-26 | transfers | POST /transfers/{transferId}/returns | `https://docs.adyen.com/api-explorer/transfers/latest/post/transfers/(transferId)/returns.md` |
| c69-27 | transfers | GET /transfers/{id} | `https://docs.adyen.com/api-explorer/transfers/latest/get/transfers/(id).md` |
| c69-28 | transfers | GET /transactions/{id} | `https://docs.adyen.com/api-explorer/transfers/latest/get/transactions/(id).md` |
| c69-29 | transfers | GET /grants/{id} | `https://docs.adyen.com/api-explorer/transfers/latest/get/grants/(id).md` |
| c69-30 | transfers-api | GET /disputes/{disputeId}/attachments | `https://docs.adyen.com/api-explorer/transfers-api/latest/get/disputes/(disputeId)/attachments.md` |
| c69-31 | transfers-api | POST /disputes/{disputeId}/attachments | `https://docs.adyen.com/api-explorer/transfers-api/latest/post/disputes/(disputeId)/attachments.md` |
| c69-32 | transfers-api | GET /disputes/{disputeId}/attachments/{attachmentId} | `https://docs.adyen.com/api-explorer/transfers-api/latest/get/disputes/(disputeId)/attachments/(attachmentId).md` |
| c69-33 | transfers-api | DELETE /disputes/{disputeId}/attachments/{attachmentId} | `https://docs.adyen.com/api-explorer/transfers-api/latest/delete/disputes/(disputeId)/attachments/(attachmentId).md` |
| c69-34 | transfers-api | GET /disputes/{id} | `https://docs.adyen.com/api-explorer/transfers-api/latest/get/disputes/(id).md` |
| c69-35 | transfers-api | PATCH /disputes/{id} | `https://docs.adyen.com/api-explorer/transfers-api/latest/patch/disputes/(id).md` |
| c69-36 | capital | POST /dynamicOffers/{id}/calculate | `https://docs.adyen.com/api-explorer/capital/latest/post/dynamicOffers/(id)/calculate.md` |
| c69-37 | capital | POST /dynamicOffers/{id}/grantOffer | `https://docs.adyen.com/api-explorer/capital/latest/post/dynamicOffers/(id)/grantOffer.md` |
| c69-38 | capital | GET /grantOffers/{id} | `https://docs.adyen.com/api-explorer/capital/latest/get/grantOffers/(id).md` |
| c69-39 | capital | GET /grants/{grantId} | `https://docs.adyen.com/api-explorer/capital/latest/get/grants/(grantId).md` |
| c69-40 | capital | GET /grants/{grantId}/disbursements | `https://docs.adyen.com/api-explorer/capital/latest/get/grants/(grantId)/disbursements.md` |
| c69-41 | capital | GET /grants/{grantId}/disbursements/{disbursementId} | `https://docs.adyen.com/api-explorer/capital/latest/get/grants/(grantId)/disbursements/(disbursementId).md` |
| c69-42 | capital | PATCH /grants/{grantId}/disbursements/{disbursementId} | `https://docs.adyen.com/api-explorer/capital/latest/patch/grants/(grantId)/disbursements/(disbursementId).md` |
| c69-43 | capital | GET /grantAccounts/{id} | `https://docs.adyen.com/api-explorer/capital/latest/get/grantAccounts/(id).md` |
| c69-44 | open-banking | GET /accountVerification/reports/{code} | `https://docs.adyen.com/api-explorer/open-banking/latest/get/accountVerification/reports/(code).md` |
| c69-45 | balanceplatform-webhooks | POST balancePlatform.balanceAccountSweepExecution.succeeded | `https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweepExecution.succeeded.md` |
| c69-46 | balanceplatform-webhooks | POST balancePlatform.balanceAccountSweepExecution.failed | `https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweepExecution.failed.md` |
| c69-47 | balanceplatform-webhooks | POST balancePlatform.balanceAccountSweepExecution.skipped | `https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountSweepExecution.skipped.md` |
