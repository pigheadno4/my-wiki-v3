---
title: "Adyen Classic Platforms"
type: concept
category: technology
tags: [adyen, classic-platforms, marketplaces, sub-merchants]
---

## Definition

Adyen Classic Platforms is the older Adyen for Platforms integration for marketplace and other platform models. In the 2023-modified overview captured 2026-09-15, the platform onboards sellers, service providers or contractors as sub-merchants/account holders, accepts buyer payments on their behalf, can split payment funds among sub-merchants and deduct costs, move funds between its account and sub-merchant accounts, then schedule or initiate payouts. [[source-adyen-docs-classic-platforms]]

## Evidence boundary

The Classic overview explicitly directs a new implementation to a separate new-integration guide. Keep Classic account-holder/account and workflow terminology separate from the current [[adyen-platforms]] balance-platform/API model; this overview does not establish that their resources or endpoints are interchangeable. Its country list and point-of-sale country condition are dated snapshot guidance, not current eligibility. Descriptions of immediate acceptance after signup, held funds, transfers and payout options do not prove verification approval, an executed split, payment capture, settlement, payout or bank receipt for a particular sub-merchant.

## Sources

- [[source-adyen-api-explorer-notificationconfiguration-latest-post-getnotificationconfiguration]] — 2026-09-15-captured Notification v6 TEST configuration lookup by subscription ID, with event/HMAC/endpoint settings; request and response example IDs differ, and lookup does not prove delivery.


- [[source-adyen-api-explorer-notificationconfiguration-latest-post-createnotificationconfiguration]] — 2026-09-15-captured Classic Notification v6 TEST subscription-create reference for per-event endpoints, optional credentials/HMAC/SSL fields and configuration ID; create response is not delivery or receiver validation.


- [[source-adyen-api-explorer-notificationconfiguration-latest-post-updatenotificationconfiguration]] — 2026-09-15-captured Classic Notification API v6 test-host update reference for existing subscription IDs, full event-list replacement, HMAC/endpoint settings and a 200 configuration response distinct from actual delivery.


- [[source-adyen-api-explorer-notificationconfiguration-latest-post-testnotificationconfiguration]] — 2026-09-15-captured Notification API v6 TEST reference for probing an existing Classic notification subscription by ID and event types; its 200 example reports a non-2XX recipient response.


- [[source-adyen-api-explorer-notificationconfiguration-latest-post-getnotificationconfigurationlist]] — 2026-09-15-captured Notification API v6 test-server listing of the executing user's platform subscription configurations, with event selection and endpoint settings; listing does not prove delivery.


- [[source-adyen-api-explorer-notificationconfiguration-latest-post-deletenotificationconfigurations]] — 2026-09-15-captured Classic Notification API v6 TEST reference for deleting subscription configurations by integer ID; after deletion, delivery to the URL defined in that subscription stops, while the response example is only a request reference.


- [[source-adyen-api-explorer-notificationconfiguration-latest-overview]] — 2026-09-15-captured Classic Notification Configuration API v6 TEST catalog for creating, retrieving, updating, deleting and testing subscriptions, with authentication and live-credential boundaries.


- [[source-adyen-api-explorer-fund-latest-post-refundfundstransfer]] — 2026-09-15-captured Fund API v6 TEST refund-of-transfer reference requiring the original transfer PSP reference and amount; 202 is acceptance, not completed reversal.


- [[source-adyen-api-explorer-fund-latest-post-transferfunds]] — 2026-09-15-captured Classic Fund API v6 TEST transfer reference for same-platform accounts, account-holder status gates, required amount/codes and 200/202 request response; companion fund-transfer guide adds destination processing and webhook outcome gates.


- [[source-adyen-api-explorer-account-latest-post-updateaccountholder]] — 2026-09-15-captured Classic Account API v6 TEST reference for account-holder detail/tier updates and adding bank accounts or shareholders, including metadata replacement and 202 processing boundary.


- [[source-adyen-api-explorer-fund-latest-post-setupbeneficiary]] — 2026-09-15-captured Classic Fund API v6 test-server reference for beneficiary-account setup, current-balance/future-payment routing, four-beneficiary/no-cycle limit and incomplete 202 processing.


- [[source-adyen-api-explorer-fund-latest-post-payoutaccountholder]] — 2026-09-15-captured Classic Fund API v6 test-host reference for account-to-holder payout requests, holder-owned bank/payout-method destination codes and 200/202 response fields; final payout status requires the separate notification route.


- [[source-adyen-api-explorer-fund-latest-post-debitaccountholder]] — 2026-09-15-captured Fund API TEST v6 direct-debit request reference for holder bank account and split destinations; result webhook and `MarketPlace`/`Marketplace` spelling discrepancy qualify the sample.


- [[source-adyen-api-explorer-fund-latest-post-refundnotpaidouttransfers]] — 2026-09-15-captured Fund API v6 TEST reference for account-scoped refund requests since the last payout; other split recipients and fees remain, and 202 is pending.


- [[source-adyen-api-explorer-fund-latest-overview]] — 2026-09-15-captured Classic Fund API v6 overview for authentication, TEST server/version suffix, live-credential distinction and eight-operation catalog; endpoint table is not an operation contract.


- [[source-adyen-api-explorer-account-latest-post-uploaddocument]] — 2026-09-15-captured Classic Account API v6 document-upload reference for Base64 content, type and conditional owner links; 202 acceptance is incomplete processing, not KYC approval.


- [[source-adyen-api-explorer-fund-latest-post-accountholdertransactionlist]] — 2026-09-15-captured Fund API v6 TEST reference for paginated, per-account Classic transaction lists and status filters; a listed payout is not bank-receipt proof.


- [[source-adyen-api-explorer-fund-latest-post-accountholderbalance]] — 2026-09-15-captured Fund API v6 test-server account-holder balance lookup, separating per-account balances from holder totals and balance, on-hold and pending currency lists.


- [[source-adyen-api-explorer-account-latest-post-updateaccountholderstate]] — 2026-09-15-captured Account API v6 TEST reference for enabling or disabling a holder's payout or processing state; payout allowance remains an aggregate of other conditions, and 202 is pending.


- [[source-adyen-api-explorer-account-latest-post-createaccountholder]] — 2026-09-15-captured Classic Account API v6 test-server reference for creating a sub-merchant account holder, conditional entity details, default account creation and partial associated-bank-account failure.


- [[source-adyen-api-explorer-account-latest-post-updateaccount]] — 2026-09-15-captured Account API v6 TEST account update reference for description, bank/card payout routing, metadata replacement and payout schedule; 202 processing is incomplete.


- [[source-adyen-api-explorer-account-latest-post-unsuspendaccountholder]] — 2026-09-15-captured Classic Account API v6 test-server reference for moving an eligible holder from Suspended to Inactive; 202 is accepted for processing, not completion.


- [[source-adyen-api-explorer-account-latest-post-getuploadeddocuments]] — 2026-09-15-captured Account API v6 TEST reference for retrieving previously uploaded Classic account-holder document details; response metadata does not establish verification approval.


- [[source-adyen-api-explorer-account-latest-post-suspendaccountholder]] — 2026-09-15-captured Classic Account API v6 test-host reference for suspending a holder by `accountHolderCode`, with status, payout/processing-state and scheduled-event response fields; HTTP 202 is pending, while operational status effects are in the separate verification guide.


- [[source-adyen-api-explorer-account-latest-post-gettaxform]] — 2026-09-15-captured Account API v6 test-server reference for US account-holder tax-form requests by code, form type and year, with optional Base64 response content; eligibility and delivery conditions remain in the separate Classic guide.


- [[source-adyen-api-explorer-account-latest-post-getaccountholder]] — 2026-09-15-captured Account API Explorer TEST v6 `POST /getAccountHolder` retrieval reference for Classic holder/account identities, optional status and KYC views, and distinct payout versus processing state.


- [[source-adyen-api-explorer-account-latest-post-deletesignatories]] — 2026-09-15-captured Classic Account API v6 test endpoint for deleting selected signatories from an account holder; 202 acceptance does not establish completed deletion.


- [[source-adyen-api-explorer-account-latest-post-deleteshareholders]] — 2026-09-15-captured Classic Account API v6 shareholder deletion reference, scoped by account-holder and shareholder codes; 202 means processing is incomplete.


- [[source-adyen-api-explorer-account-latest-post-deletepayoutmethods]] — 2026-09-15-captured Account API v6 TEST reference for deleting account-holder payout methods by holder and method codes; a 202 receipt says processing is incomplete.


- [[source-adyen-api-explorer-account-latest-post-deletelegalarrangements]] — 2026-09-15-captured Classic Account API v6 TEST reference for deleting an account holder's legal arrangements or only listed entities; 202 means accepted, not completed.


- [[source-adyen-api-explorer-account-latest-post-deletebankaccounts]] — 2026-09-15-captured Account API v6 TEST `POST /deleteBankAccounts` reference for deleting specified bank-account UUIDs from a Classic account holder; 202 indicates processing is incomplete.


- [[source-adyen-api-explorer-account-latest-post-createaccount]] — 2026-09-15-captured Classic Account API v6 test-host `/createAccount` reference for additional holder accounts, conditional payout settings and response/error fields; the separate Classic creation guide requires `ACCOUNT_CREATED` before business logic even after HTTP 200.


- [[source-adyen-api-explorer-account-latest-post-closestores]] — 2026-09-15-captured Account API v6 TEST reference for closing stores associated with a Classic account holder; requires account-holder code and store list.


- [[source-adyen-api-explorer-account-latest-post-closeaccountholder]] — 2026-09-15-captured Account API v6 test-server reference for final Classic account-holder closure by code, including 200/202 response boundaries and liable-account routing for payments to a closed holder.


- [[source-adyen-api-explorer-account-latest-post-closeaccount]] — 2026-09-15-captured Account API Explorer TEST v6 `POST /closeAccount` reference for irreversible Classic account closure, liable-account routing of later payments, and 200 versus pending 202 responses.


- [[source-adyen-api-explorer-account-latest-post-checkaccountholder]] — 2026-09-15-captured Classic Account API v6 test endpoint for proactively triggering account-holder verification with `Processing` or `Payout` state and tier; 202 acceptance is not completed verification.


- [[source-adyen-api-explorer-account-latest-overview]] — 2026-09-15-captured Classic Account API v6 overview for account-related entity operations, authentication alternatives, versioned TEST server and endpoint directory; new implementations are directed to a separate guide.


- [[source-adyen-docs-classic-platforms-reconciliation-use-cases-transactions-scheduled-payouts]] — 2026-09-15 Classic scheduled-payout reconciliation example using account-holder/account Marketpay Payout rows; selected rows and initiated payouts are not bank-receipt proof.


- [[source-adyen-docs-classic-platforms-reports-and-fees-marketpay-balance-report]] — 2023-modified, 2026-09-15-captured Classic Marketpay Balance Report reference for CET, daily/weekly/monthly frequency and per-account/currency available/pending minor-unit balances; report rows are not payout or bank-receipt proof.


- [[source-adyen-docs-classic-platforms-reconciliation-use-cases-reconcile-accounts-receivable]] — 2023-modified, 2026-09-15-captured Classic Settlement details report example for batch net amount to platform accounts, `XASTransfer` and per-account ledger route; illustrative rows are not actual settlement or bank-receipt proof.


- [[source-adyen-docs-classic-platforms-tax-forms]] — 2023-modified, 2026-09-15-captured Classic US 1099-K retrieval guide for direct-payout/threshold scope, dated 2024 gross-volume threshold and server-side Base64-to-PDF delivery flow.


- [[source-adyen-docs-classic-platforms-reconciliation-use-cases-build-transactional-ledger]] — 2023-modified, 2026-09-15-captured Classic account-level accounting-ledger guide for split/liable rows, fees, balance comparison and aged-negative-balance compensation.


- [[source-adyen-docs-classic-platforms-split-configuration-for-stores]] — 2021-modified, 2026-09-15-captured Classic POS/partner-store automatic commission rules, liable fallback, API override, and asynchronous account-holder-store attachment.


- [[source-adyen-docs-classic-platforms-reconciliation-use-cases-understand-fees]] — 2021-modified, 2026-09-15-captured Classic liable-account fee reconciliation across settlement, marketplace and payment-accounting reports, with invoice and signed-debit example boundaries.


- [[source-adyen-docs-classic-platforms-platforms-for-partners]] — 2023-modified, 2026-09-15-captured Classic partner-arrangement ecommerce guide for direct scheme-linked sub-merchants, SAQ A/KYC and Active-store gates, allowed origins and single-store routing.


- [[source-adyen-docs-classic-platforms-reports-and-fees-marketpay-payout-report]] — 2026-09-15 Classic automatic-payout CSV reconciliation reference for account-holder/account/currency, rolling balances and version-qualified record types; payout rows do not prove bank receipt.


- [[source-adyen-docs-classic-platforms-platforms-for-pos]] — 2021-modified, 2026-09-15-captured Classic POS guide for Support-enabled store creation, Active webhook gate, terminal assignment, split override and CAPTURE outcome tracking.


- [[source-adyen-docs-classic-platforms-release-notes]] — 2018–2023 Classic release history captured 2026-09-15: v5 asynchronous outcomes and notification fields, v6 payout-method and webhook-field migrations, dated KYC/funds/report changes, `ownerDateOfBirth` deprecation, and the 2022 new-versus-existing integration boundary.


- [[source-adyen-docs-classic-platforms-reports-and-fees]] — 2023-modified, 2026-09-15-captured Classic report/fee selection hub distinguishing Adyen-account payment/invoice reports from account-holder/liable platform reports and scheduled-payout-only Marketpay Payout.

- [[source-adyen-docs-classic-platforms-reports-and-fees-marketplace-payments-accounting-report]] — 2023-modified, 2026-09-15-captured Classic account-entry ledger/report schema for pending and available balances, payout/fee record types, and dated column/label discrepancies.



- [[source-adyen-docs-classic-platforms-api]] — 2019-modified, 2026-09-15-captured Classic Platforms API Explorer directory for Account, Fund, notification configuration and delivery, and hosted onboarding references; new implementations are directed elsewhere.


- [[source-adyen-docs-classic-platforms-reconciliation-use-cases]] — 2021-modified, 2026-09-15-captured Classic reconciliation hub routing report preparation to accounts-receivable, ledger, scheduled-payout and fee guides; this page contains no worked rows or completed reconciliation.


- [[source-adyen-docs-classic-platforms-identify-account-holder-risk-configure-notifications-for-risk-signals]] — 2022-modified, 2026-09-15-captured Classic Score webhook setup for `SCORE_SIGNAL_TRIGGERED`, with Adyen activation step and conflicting create-example `active` values.


- [[source-adyen-docs-classic-platforms-payouts-payout-notifications]] — 2022-modified, 2026-09-15-captured Classic `ACCOUNT_HOLDER_PAYOUT` status reference for Initiated/Confirmed/Failed, possible post-confirmation bank return and scheduled-return recovery.


- [[source-adyen-docs-classic-platforms-kyc-action-required-snapshot-report]] — 2019-modified, 2026-09-15-captured Classic scheduled CSV for recently active sub-merchants with incomplete KYC, with notification preference and an entity-type list narrower than the creation guide.


- [[source-adyen-docs-classic-platforms-account-structure-example-structures]] — 2019-modified, 2026-09-15-captured Classic company/merchant/platform account illustration and one-to-one versus multiple account/bank-account payout mapping.


- [[source-adyen-docs-classic-platforms-notification-types]] — 2020-modified, 2026-09-15-captured Classic event-purpose catalog for account holders, payouts, transfers, refunds and liable-account compensation; request/Initiated labels are not completion or bank-receipt proof.


- [[source-adyen-docs-classic-platforms-account-holders-and-accounts-change-legal-entity]] — 2020-modified, 2026-09-15-captured Classic Account API v5+ legal-entity change guide preserving account codes/history, with migrate-versus-new-details verification and one-shareholder migration limit.


- [[source-adyen-docs-classic-platforms-onboard-users-hosted-onboarding-page-hop-appearance]] — 2026-09-15 Classic Customer Area HOP appearance guide for role-gated header, logo, background and FAQ controls with asset limits.


- [[source-adyen-docs-classic-platforms-payouts]] — 2023-modified, 2026-09-15-captured Classic scheduled-full-bank versus manual-partial-bank/eligible-card payout overview with tier, country, bank-count and currency limits; US example absent from table.


- [[source-adyen-docs-classic-platforms-onboard-users-hosted-onboarding-page-customize-experience]] — 2022-modified, 2026-09-15-captured Classic HOP customization guide for check/page selection, locale fallback, verified-data editing and return redirect; source flags `returnURL` versus companion `returnUrl` casing.


- [[source-adyen-docs-classic-platforms-configure-notifications-signing-notifications-with-hmac]] — 2023-modified, 2026-09-15-captured Classic Notifications v5+ HMAC guide for configuration, raw-body verification and key-rotation boundary; key-size and example-event text conflict.


- [[source-adyen-docs-classic-platforms-payouts-manual-payout]] — 2020-modified, 2026-09-15-captured Classic Customer Area/Fund API manual-payout guide for balance and role gates, asynchronous status, regional speed conditions and descriptor example conflict.


- [[source-adyen-docs-classic-platforms-top-up-accounts]] — 2023-modified, 2026-09-15-captured Classic Fund API direct-debit top-up guide: holder bank to merchant settlement to split credits, consent/rail/limit gates, asynchronous results and USD/EUR sample mismatch.


- [[source-adyen-docs-classic-platforms-prepare-reports]] — 2023-modified, 2026-09-15-captured Classic report configuration, download and reconciliation-join guide, including period/time-zone alignment and nonunique merchant-reference caveat.


- [[source-adyen-docs-classic-platforms-configure-notifications]] — 2021-modified, 2026-09-15-captured Classic Notification API setup, update/delete, acknowledgment, retry and test guide; examples conflict on API version, protocol and one configuration ID.


- [[source-adyen-docs-classic-platforms-identify-account-holder-risk]] — 2020-modified, 2026-09-15-captured Classic Score overview for account-holder risk signals, shared identity scores, review-led actions and default no payout/processing disablement.


- [[source-adyen-docs-classic-platforms-onboard-users-custom-onboarding]] — 2020-modified, 2026-09-15-captured Classic custom account-holder onboarding guide for upfront/staggered collection, Account API v6 updates, notification-gated verification and asynchronous documents.


- [[source-adyen-docs-classic-platforms-onboard-users-hosted-onboarding-page]] — 2021-modified, 2026-09-15-captured Classic HOP guide for enabled hosted verification, one-time redirect timing, session recovery and webhook result gates.


- [[source-adyen-docs-classic-platforms-payouts-scheduled-payout]] — 2020-modified, 2026-09-15-captured Classic daily/per-account payout schedules, HOLD/manual behavior, notification-confirmed updates and conditional regional same-day speed.


- [[source-adyen-docs-classic-platforms-fund-transfer]] — 2020-modified, 2026-09-15-captured Classic account-to-account transfer and full/partial reversal guide for Fund API/Customer Area, with account-status gates and asynchronous webhook outcomes.


- [[source-adyen-docs-classic-platforms-quick-start]] — 2021-modified, 2026-09-15-captured Classic TEST integration walk-through across onboarding, Checkout split, capture, payout, notifications and reports; basic fields predate later verification requirements.


- [[source-adyen-docs-classic-platforms-verification-process-check-verification-results]] — 2021-modified, 2026-09-15-captured Classic notification, Account API and Customer Area verification-result guide with per-check status, versioned payout-method type and conditional retry/document steps.


- [[source-adyen-docs-classic-platforms-test-scenarios]] — 2020-modified, 2026-09-15-captured Classic Account API/HOP test fixtures for payout, failed KYC and refund-timing states; the invalid-data owner-city field path differs from earlier examples.


- [[source-adyen-docs-classic-platforms-identify-account-holder-risk-review-and-manage]] — 2020-modified, 2026-09-15-captured Classic Score guide for role-gated identity review, manual/automated risk actions and permanent linked-KYC-value exclusion.


- [[source-adyen-docs-classic-platforms-onboard-users]] — 2020-modified, 2026-09-15-captured Classic account-holder verification guide for upfront versus staggered onboarding, payout-tier transitions, and the distinct Payout/Processing `/checkAccountHolder` prechecks.


- [[source-adyen-docs-classic-platforms-verification-process]] — 2023-modified, 2026-09-15-captured Classic account-holder verification/deadline guide for payout gates, inactive/suspended refunds, conditional unsuspension and final closure.


- [[source-adyen-docs-classic-platforms-payouts-track-payouts]] — 2026-09-15 Classic payout tracking guide for Initiated/Confirmed/Failed notifications, post-confirmation bank returns, timing estimates and manual versus scheduled recovery routes.

- [[source-adyen-docs-classic-platforms-payouts-manual-payout-payout-to-cards]] — 2021-modified, 2026-09-15-captured Classic manual payout-to-card guide with Support/PCI/eligibility gates, stored payout method and asynchronous update/payout notifications; request receipt does not prove card credit.



- [[source-adyen-docs-classic-platforms-verification-process-verification-codes]] — 2019-modified, 2026-09-15-captured Classic Platforms v5+ account-holder verification-code catalog for identity, document, bank and company errors, with internal-only descriptions and explicit no-retry cases.


- [[source-adyen-docs-classic-platforms-account-holders-and-accounts]] — 2021-modified, 2026-09-15-captured Classic Account API v6 guide to sub-merchant account-holder creation, automatic and optional accounts, asynchronous notification gates, and separate payment-versus-payout verification.


- [[source-adyen-docs-classic-platforms-processing-payments]] — 2021-modified, 2026-09-15-captured Classic split-payment, capture and refund guide for seller accountCode versus liable-account allocation and precedence.


- [[source-adyen-docs-classic-platforms-verification-process-accepted-data-format]] — 2023-modified, 2026-09-15-captured Classic identity, organization registration/TIN and payout-bank format reference with conditional verification inputs and country examples.

- [[source-adyen-docs-classic-platforms-verification-process-document-requirements]] — 2021-modified, 2026-09-15-captured Classic failed-verification document guide for individual ID, organization registration and bank evidence, with category-specific screenshot, age, page and size limits.



- [[source-adyen-docs-classic-platforms-verification-process-requirements-update]] — 2022-modified, 2026-09-15-captured Classic sub-merchant verification changes: shareholder/signatory identity, regional data, versioned Account API shapes, notifications and cohort-specific onboarding actions.


- [[source-adyen-docs-classic-platforms-verification-process-legal-arrangements]] — 2021-modified, 2026-09-15-captured Classic Account API v6 legal-arrangements verification guide for association, partnership, sole proprietorship and trust; conditional documents, asynchronous results and example/region conflicts.


- [[source-adyen-docs-classic-platforms-error-codes]] — 2019-modified, 2026-09-15-captured Classic Platforms response/notification error-code catalog, with separate general and account-holder lists and duplicated account-holder code `125`.


- [[source-adyen-docs-classic-platforms-account-structure]] — 2021-modified, 2026-09-15-captured Classic Platforms resource and money-flow guide for merchant accounts, sub-merchant account holders/accounts, liable pair, splits, verified-bank payouts and refunds.


- [[source-adyen-docs-classic-platforms]] — 2023-modified, 2026-09-15-captured Classic Platforms overview of sub-merchant onboarding, payment splitting, internal funds transfers, payouts, reconciliation and dated region scope.

- [[source-adyen-docs-classic-platforms-platforms-integration-checklist]] — 2021-modified, 2026-09-15-captured Classic test and go-live checklist for account-holder verification, split payments, payout prerequisites, asynchronous notifications and reconciliation; its payout-200 wording needs the final-result webhook boundary.


## Related

- [[adyen-platforms]] — newer Adyen for Platforms model and its separate integration guide.
- [[adyen]] — provider context.
