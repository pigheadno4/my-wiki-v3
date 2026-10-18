---
title: "Adyen for Platforms"
type: concept
category: technology
tags: [adyen, platforms, onboarding, split-payments, payouts]
---

## Definition

Adyen for Platforms is Adyen's current platform-integration overview for commerce, ordering/POS, retail-management and SaaS businesses that process online and/or in-person payments on behalf of their users. The 2026-09-15 snapshot routes to user onboarding and Adyen verification, split payment processing, managed/custom payouts, risk, and reports. It points to a separate marketplace integration guide when that model fits better. [[source-adyen-docs-platforms]]

## Evidence boundary

The landing page does not define the detailed legal-entity/account-holder/balance/liable/reserve/transfer-instrument model, API roles, verification capabilities or status transitions. A platform and its users are distinct actors, but “on behalf of” does not identify a merchant of record, legal seller, payee or fund owner for a particular transaction. Country and acquiring-region lists are dated and distinct; the Channel Islands and Isle of Man are excluded for in-person payments and store creation. Issuing, business accounts and Capital are separate optional products with additional availability and verification. The page is not proof of onboarding approval, payment authorization, split execution, payout or bank receipt.

## Sources

- [[source-adyen-docs-platforms-transfer-transactions]] — 2026-09-15 balance-platform transaction tracking hub for transfer status meanings, webhook/API routes and failed/refused/returned handling; booked source debit is not bank receipt.


- [[source-adyen-docs-platforms-balance-updates-use-cases]] — 2026-09-15 pilot Balance webhook TEST examples for platform-wide, account-holder and per-balance-account thresholds; JPY 1,000 prose versus 100000 example value needs verification, and sample events do not show balanceAccountId.


- [[source-adyen-docs-platforms-top-up-balance-account]] — 2026-09-15 Platforms overview defining user/liable balance-account top-ups as incoming external transfers and routing scheduled, on-demand and webhook detail; initiation is not booked-credit proof.


- [[source-adyen-docs-platforms-payout-reconciliation]] — 2026-09-15 payout-reconciliation method and availability matrix across managed, custom scheduled, on-demand and cashout routes.


- [[source-adyen-docs-platforms-cash-out-instantly]] — 2020-modified, 2026-09-15-captured Platforms CashOut overview for pending-balance funding, optional instant-payout/fee legs, settlement repayment, bank-return limits and reporting routes.


- [[source-adyen-docs-platforms-balance-updates-manage-balance-webhook]] — 2026-09-15-captured pilot Configuration API guide for viewing, PATCHing, deactivating and deleting Balance webhook settings; a PATCH must retain wanted conditions, and removing the last one broadens alerts to all target balance changes.


- [[source-adyen-docs-platforms-settle-funds]] — 2026-09-15 Platforms sales-day net-settlement guide for captured-batch timing, contract/custom delays, pass-through deprecation and 30-day reversal; settled balance is not bank receipt.


- [[source-adyen-docs-platforms-settle-funds-pass-through-settlement]] — 2025-modified, 2026-09-15-captured deprecated Platforms settlement guide for scheme/method-dependent batches, weekday timing, adjustment dates and payment-level reconciliation; no payout or bank-receipt proof.


- [[source-adyen-docs-platforms-quickstart-guide-payouts]] — 2026-09-15 Platforms quickstart for user balance-account settlement, verified-bank payout choices, fund-availability timing and missed-payout investigation; ETA and balance credit are not bank-receipt proof.


- [[source-adyen-docs-platforms-custom-payouts-configure-settlement-delay]] — 2026-09-15 Platforms Configuration API guide to per-balance-account settlement-delay override, approval and managed-schedule limits, and conditional sales-day closing-time preservation.


- [[source-adyen-docs-platforms-custom-payouts-scheduled-payouts-view-custom-payout-executions]] — 2026-09-15 Configuration API/Customer Area guide for custom-schedule execution records, success-to-transfer ID, skip/failure reasons and disabling; execution is not bank receipt.


- [[source-adyen-docs-platforms-balance-updates-configure-balance-webhook]] — 2026-09-15-captured pilot Balance webhook setup for platform, account-holder or balance-account targets, role and 20-by-20 limits, and conflicting all-versus-any condition wording; alert configuration is not funds-movement proof.

- [[source-adyen-docs-platforms-balance-updates]] — 2026-09-15 pilot Balance webhook overview for scoped balance-change notifications and platform-to-account-holder-to-account inheritance.



- [[source-adyen-docs-platforms-quickstart-guide-reporting]] — 2026-09-15 Platforms quickstart routing user-facing dashboard components, balance-account reports and payment-processing report reconciliation with BPPR/BPAR limitations.


- [[source-adyen-docs-platforms-managed-payouts-view-payout-executions]] — 2026-09-15 Platforms guide to scoped managed-schedule execution reads, Sent/Not sent/Failed and success/skipped/failed webhooks, then separate transfer lifecycle and bank-return tracking.


- [[source-adyen-docs-platforms-top-up-balance-account-scheduled-top-ups]] — 2026-09-15 Platforms Configuration API pull-sweep guide for verified-bank threshold top-ups, default-active creation and later transfer-webhook tracking; no booked-credit or bank-receipt proof.


- [[source-adyen-docs-platforms-transfer-transactions-track-api]] — 2026-09-15 Transfers API transaction-query guide for platform/account-holder/balance-account scope, internal/external signed rows, pending/booked dates and pagination; sample identifiers conflict and rows are not bank-receipt proof.


- [[source-adyen-docs-platforms-custom-payouts-on-demand-payouts-approve-cancel-payouts]] — 2020-modified, 2026-09-15-captured Transfers API review guide for pending on-demand payout approval/cancellation, 30-day expiry, batch endpoints and webhook states; approval is not bank receipt.


- [[source-adyen-docs-platforms-payout-amount]] — 2026-09-15-captured payout-cap guide for default available versus platform-wide current-balance configuration, reserve-collateral checks/failure and later release or 30-day transfer; calculations are not bank-receipt proof.


- [[source-adyen-docs-platforms-custom-payouts-transfer-routes]] — 2023-modified, 2026-09-15-captured Platforms Configuration API guide to calculate bank-payout route priorities and requirements by country or counterparty before a separate payout request.


- [[source-adyen-docs-platforms-top-up-balance-account-on-demand-top-ups]] — 2026-09-15 Platforms user-funded Checkout `/payments` top-up guide for verified-bank or other-method funding, TopUp split booking, capability/direct-debit gates and asynchronous status tracking.


- [[source-adyen-docs-platforms-top-up-balance-account-top-up-webhooks]] — 2026-09-15 Platforms scheduled/on-demand top-up webhook guide for separate incoming credit and outgoing fee legs, status stages and booked-event matching; no external debit finality or bank-receipt proof.


- [[source-adyen-docs-platforms-cash-out-instantly-cashout-webhooks]] — 2026-09-15-captured Platforms cashout webhook guide for four transfer legs, subscription and status tracking, optional instant bank payout, and test-example envelope conflicts; booked balance-account debit is separate from payout credited tracking and bank receipt.

- [[source-adyen-docs-platforms-cash-out-instantly-cashout-request]] — 2026-09-15-captured Platforms `/cashouts` request guide for pending-balance cashout with optional transfer-instrument payout, capability/route/fee checks, asynchronous outcome and failure reversal; request success is not bank-receipt proof.



- [[source-adyen-docs-platforms-payout-descriptions]] — 2026-09-15 Platforms descriptor guide for scheduled placeholders, static on-demand text, originator-name setup and rail-specific accepted versus visible characters; submitted text is not bank-display or payout proof.


- [[source-adyen-docs-platforms-managed-payouts-use-managed-payouts]] — 2026-09-15 Platforms Configuration API/Customer Area guide to applying and managing managed payout schedules, conditional fallbacks and configuration evidence; not bank-receipt proof.


- [[source-adyen-docs-platforms-custom-payouts]] — 2024-modified, 2026-09-15-captured Platforms custom-payout overview for scheduled/on-demand user-bank transfers, capability/role and route constraints, cutoffs and TEST scenarios; request or booking is not bank receipt.


- [[source-adyen-docs-platforms-custom-payouts-scheduled-payouts]] — 2022-modified, 2026-09-15-captured Platforms balance-account sweep scheduling guide for user-bank transfer-instrument destinations, conditions, routes and distinct configuration/execution webhooks; no bank-receipt proof.


- [[source-adyen-docs-platforms-custom-payouts-on-demand-payouts]] — 2020-modified, 2026-09-15-captured Transfers API/Customer Area guide to off-schedule user bank payouts, capability/role gates, priority fallback, review/future-date failure and returned-bank-account limits; request or booking is not bank-receipt proof.


- [[source-adyen-docs-platforms-managed-payouts]] — 2022-modified, 2026-09-15-captured Platforms managed-payout schedule overview for local same-location/currency balance-account payouts, Adyen-contact configuration, settlement-delay limits and estimated ETAs.


- [[source-adyen-docs-platforms-in-person-payments-split-transactions-split-refunds]] — 2024-modified, 2026-09-15-captured POS referenced-refund method hub for explicit versus original split, partial-refund cap and child procedure routes; request choice is not outcome proof.


- [[source-adyen-docs-platforms-multi-pay-in]] — 2026-09-15 multi pay-in service overview for third-party partner proceeds, Adyen-held source account, 24-hour allocation, split default and partner-side customer refunds; no financial-outcome proof.


- [[source-adyen-docs-platforms-quickstart-guide-payments]] — 2026-09-15 Platforms payments quickstart for online/POS store-to-balance flow, payment-method routes, request-over-profile split precedence and settlement batches; no completed funds movement is shown.

- [[source-adyen-docs-platforms-settle-funds-configure-closing-time]] — 2026-09-15 Platforms balance-account sales-day closing-time configuration guide for local hourly 00:00–07:00 cutoffs, conditional business-day settlement delay and method-schedule exceptions; response/webhook is settings evidence, not payout proof.



- [[source-adyen-docs-platforms-multi-pay-in-receive-funds]] — 2026-09-15 guide to allowlisted partner bank payouts into an Adyen-held multi pay-in account and incoming credit webhooks; account credit precedes separate user allocation.


- [[source-adyen-docs-platforms-in-person-payments-split-transactions]] — 2024-modified, 2026-09-15-captured Platforms POS split overview for store/profile precedence, Terminal authorization/refund versus Checkout capture formats, liable-account fallback and split types; operation outcomes require separate evidence.


- [[source-adyen-docs-platforms-payment-methods-customer-area]] — 2026-09-15 Platforms Customer Area guide for merchant/store payment-method requests, account-holder receivePayments gating, country edits and 90-day inactive deletion.


- [[source-adyen-docs-platforms-online-payments-split-transactions]] — 2024-modified, 2026-09-15-captured Platforms online split-transaction overview for store-profile versus API-request precedence, liable-account default, lifecycle request routes and split-type field navigation.


- [[source-adyen-docs-platforms-in-person-payments-donations-in-person]] — 2026-09-15 Platforms in-person Giving implementation guide for user account-holder campaigns, distinct sale/donation transactions, terminal receipt lookup and donation-outcome webhook.


- [[source-adyen-docs-platforms-in-person-payments-payment-facilitators]] — 2026-09-15 Platforms Terminal API/standalone guide for payment-facilitator user data, store versus request routes and combined split encoding; no account or funds-movement proof.


- [[source-adyen-docs-platforms-in-person-payments-tipping]] — 2023-modified, 2026-09-15-captured Terminal API guide to whole-tip user-balance booking through a Tip split item, with liable default, receipt/standalone limits and illustrative payload inconsistencies.


- [[source-adyen-docs-platforms-quickstart-guide-terminals]] — 2026-09-15 Platforms terminal-offering quickstart for software/hardware, architecture, logistics, onboarding, store assignment, fleet service and cost reconciliation; recommendations do not prove live configuration or payments.


- [[source-adyen-docs-platforms-online-payments-payment-facilitators]] — 2026-09-15 online Checkout facilitator guide for scheme-required sub-merchant data, scoped user Merchant-of-Record wording, pre-live IDs and shopper descriptors; examples do not prove eligibility or funds flow.


- [[source-adyen-docs-platforms-in-person-payments-surcharge]] — 2023-modified, 2026-09-15-captured Platforms POS surcharge guide for configuration/dynamic methods, liable/user booking, compliance and DCC limits, and per-split webhook/report reconciliation.


- [[source-adyen-docs-platforms-in-person-payments-surcharge-configuration]] — 2026-09-15 Platforms in-person Management API configuration-based surcharge guide, with rule and device limits plus Terminal API instructions to book the calculated amount to one user balance account.


- [[source-adyen-docs-platforms-in-person-payments-surcharge-dynamic]] — 2026-09-15-captured Platforms Terminal API guide to calculated in-person surcharge, user balance-account split, disclosure and response fields; no payment or fund-movement proof.


- [[source-adyen-docs-platforms-automatic-split-configuration]] — 2026-09-15 Platforms automatic-split overview for store-linked rule matching, hierarchy, liable-account fallback, per-request override and capture-time reevaluation; configuration is not financial-outcome proof.


- [[source-adyen-docs-platforms-in-person-payments-split-transactions-split-refunds-refund-original-split]] — 2024-modified, 2026-09-15-captured referenced Terminal API full-refund example inheriting original request splits, with asynchronous outcome and inconsistent fee/amount samples.


- [[source-adyen-docs-platforms-in-person-payments-split-transactions-split-refunds-refund-split-instructions]] — 2024-modified, 2026-09-15-captured Terminal API referenced-refund split guide for partial/full reversal fields, original split references and asynchronous outcome; response is not refund completion.


- [[source-adyen-docs-platforms-online-payments-transaction-fees]] — 2023-modified, 2026-09-15-captured online/POS platform fee split hierarchy, liable-account default and transfer/report reconciliation; worked examples contain account-destination and currency contradictions.


- [[source-adyen-docs-platforms-multi-pay-in-top-up-multi-pay-in]] — 2026-09-15 multi pay-in internal top-up guide from platform liable balance account to multi pay-in account, with Transfers API request fields and two-sided booked-event tracking; not a bank deposit or user allocation proof.


- [[source-adyen-docs-platforms-in-person-payments-transaction-fees]] — 2023-modified, 2026-09-15-captured Terminal API fee-allocation guide for aggregate/granular split precedence, liable-account default and report/webhook tracking; illustrative fee-account payloads conflict.


- [[source-adyen-docs-platforms-payment-methods-api]] — 2026-09-15 Platforms Management API guide for store payment-method requests, reads and updates, with account-holder capability gating and 60-/90-day removal boundaries; examples are not activation or transaction proof.

- [[source-adyen-docs-platforms-payment-methods]] — 2026-09-15 Platforms per-store ecommerce/POS payment-method and variant catalog with method-specific country, currency, approval, parameter and payment-facilitator notes; listed support is not store activation.


- [[source-adyen-docs-platforms-online-payments-donations-online]] — 2026-09-15 Platforms API-only Giving route for user-store donation campaigns, original-payment token and separate nonprofit donation transaction with DONATION-webhook outcome.


- [[source-adyen-docs-platforms-in-person-payments-split-transactions-split-payments-at-capture]] — 2023-modified, 2026-09-15-captured Terminal API delayed/separate-capture split guide, including amount-change and invalid-balance liable-account fallbacks, unsupported split types and webhook stages.


- [[source-adyen-docs-platforms-online-payments-checkout-components]] — 2026-09-15 Platforms Web Components/Sessions checkout guide for payment-server, client and webhook roles, versioned UI setup and test-to-live conditions; UI events are not financial-outcome proof.


- [[source-adyen-docs-platforms-in-person-payments-split-transactions-split-payments-at-authorization]] — 2023-modified, 2026-09-15-captured Terminal API per-payment split-format/units guide, standalone exclusion, fee fallback and invalid-target liable booking; webhooks distinguish booking states.


- [[source-adyen-docs-platforms-online-payments-surcharge]] — 2023-modified, 2026-09-15-captured pilot API-only online-card surcharge guide for compliance gating, displayed amount, user/liable split booking and webhook/report reconciliation; examples are not enablement or bank-receipt proof.


- [[source-adyen-docs-platforms-online-payments-split-transactions-split-payments-at-authorization]] — 2026-09-15 Platforms online authorization-time split guide for user/liable balance accounts, capability and destination fall-backs, per-split webhooks and capture-time override; instructions are not booking or payout proof.


- [[source-adyen-docs-platforms-multi-pay-in-refunds]] — 2026-09-15 third-party multi pay-in refund guide for Adyen balance deductions, authorization-split fallback, asynchronous webhooks and partner-owned customer return; no shopper-receipt proof.


- [[source-adyen-docs-platforms-automatic-split-configuration-create-split-configuration]] — 2026-09-15 Platforms guide to role-gated conditional split-profile creation and store/balance-account linking, fee/refund/DCC/tip booking and no-instructions liable fallback; examples are test-only and include discrepancies.


- [[source-adyen-docs-platforms-online-payments-split-transactions-split-refunds]] — 2026-09-15 Platforms Checkout refund split-booking guide covering explicit debits, authorization-ratio fallback, liable-account fallback and asynchronous refund/transfer evidence.


- [[source-adyen-docs-platforms-multi-pay-in-payments]] — 2026-09-15 third-party multi pay-in payment-allocation guide for per-payment Checkout requests, split destinations/fee default, transfer/transaction event legs, accounting-report reconciliation and later payout routing; examples do not prove funds movement.


- [[source-adyen-docs-platforms-online-payments-split-transactions-split-payments-at-capture]] — 2023-modified, 2026-09-15-captured Platforms guide to capture-time online-payment split override, partial-capture rules, liable-account fallback and per-split webhook tracking; test examples do not prove booked funds.


- [[source-adyen-docs-platforms-online-payments-split-transactions-split-chargebacks]] — 2023-modified, 2026-09-15-captured online-platform chargeback booking guide for liable/user/ratio allocation, payment-versus-capture precedence, target-account fallback and split-grain movement events.


- [[source-adyen-docs-platforms-in-person-payments]] — 2023-modified, 2026-09-15-captured Platforms POS/Terminal API and Mobile prerequisites, split precedence, liable-account default and standalone profile-only limit; diagram values are illustrative, not financial outcomes.


- [[source-adyen-docs-platforms-online-payments]] — 2023-modified, 2026-09-15-captured Platforms online-payments overview for capability-gated user/liable balance allocation, split precedence and illustrative booking-to-payout flow; no transaction-outcome proof.


- [[source-adyen-docs-platforms-process-payments]] — 2023-modified, 2026-09-15-captured Platforms online/POS processing overview with request-over-profile split precedence, liable-account default and illustrative balance-account/payout flow; examples are not financial proof.


- [[source-adyen-docs-platforms-financial-products]] — 2023-modified, 2026-09-15-captured platform product hub orienting business accounts, Capital, Issuing and Payouts; product-specific eligibility and activation belong to their guides.


- [[source-adyen-docs-platforms-verification-requirements-reference-additional-products-brand-specific-industry-codes]] — 2026-09-15 brand-specific IC/MCC classification and conditional approval-contact guide for Platforms business accounts; the pinned export has no accepted-code list or eligibility proof.


- [[source-adyen-docs-platforms-verification-requirements-reference-additional-products-industry-codes]] — 2026-09-15 Platforms IC/MCC selection and approval-contact reference; captured code table is absent and does not prove industry or business-account eligibility.


- [[source-adyen-docs-platforms-onboard-users-onboarding-steps]] — 2026-09-15 onboarding-step filter export with hosted/on-invite/v4 selected but Location and entity-type filters missing; no concrete step result is present.


- [[source-adyen-docs-platforms-account-structure-resources-legal-entity-management]] — 2026-09-15 Platforms LEM resource orientation naming legal entities, transfer instruments, supporting documents and business lines for user verification; creation is not approval or payout proof.


- [[source-adyen-docs-platforms-manage-access]] — 2023-modified, 2026-09-15-captured Platforms Customer Area/team-access overview for admin email activation, role-assigned users and separate payments/balance/financial-product credential routes; no operation-level permission proof.


- [[source-adyen-docs-platforms-manage-reserve-account]] — 2026-09-15 Platforms reserve-account guide for liable-holder-linked collateral against transfer-caused negative user balances, distinct from refund/chargeback reserved compensation; request and block are not payout proof.


- [[source-adyen-docs-platforms-manage-liable-accounts]] — 2026-09-15 guide to platform-owned main, incorrect-splits and compensation liable balances, including conditional negative-balance handling; not account-specific fund or bank-receipt proof.


- [[source-adyen-docs-platforms-kyc-verification-codes]] — 2021-modified, 2026-09-15-captured Platforms/Issuing verification-code taxonomy and account-holder capability problems retrieval route; actions are conditional suggestions, not verification outcomes.


- [[source-adyen-docs-platforms-quickstart-guide-customer-area]] — 2026-09-15 Platforms Customer Area quickstart for operational views, company/merchant-account access and user-role hygiene; UI visibility does not prove financial outcomes.


- [[source-adyen-docs-platforms-manage-access-webservice-roles]] — 2023-modified, 2026-09-15-captured Balance Platform API credential role catalog for configuration, optional Issuing, and Transfers API permissions, including BCL PCI sensitivity and v1-only transfer-initiation role; no actual grant or operation proof.


- [[source-adyen-docs-platforms-verification-overview-verification-types]] — 2026-09-15 Platforms guide comparing upfront verification with payment-facilitator-only staggered verification, tier-change payout conditions and country-specific tier currencies.


- [[source-adyen-docs-platforms-account-structure-resources-financial-products]] — 2026-09-15 Platforms example separating regional platform accounts, liable/grant resources and user account holders, balance accounts, payment instruments, transfer instruments, legal entities and business lines; examples do not prove product grants or money movement.


- [[source-adyen-docs-platforms-account-structure-resources-platform-structure]] — 2026-09-15 Adyen for Platforms payment-facilitator structure example separating platform and user merchant, balance, liable, legal-entity and transfer-instrument resources, with an illustrative split-to-payout path.


- [[source-adyen-docs-platforms-account-structure-resources]] — 2021-modified, 2026-09-15-captured current Platforms account-resource map for company/merchant/store, region-specific balance platforms, user account-holder/balance/legal-entity links and platform liable resources; it does not prove account or fund state.


- [[source-adyen-docs-platforms-quickstart-guide]] — 2026-09-15 Platforms quickstart orienting Adyen team roles, account/balance/legal-entity resources and next-step guides; not operational or financial-outcome proof.


- [[source-adyen-docs-platforms-account-holder-status]] — 2026-09-15 Platforms guide to active/suspended/closed account-holder state, Adyen-initiated inheritance and post-settlement split routing by pay-in capability; status guidance is not verification, settlement or payout proof.


- [[source-adyen-docs-platforms-verification-requirements-upload-bank-document]] — 2026-09-15 limited-availability Hosted Onboarding bank-document upload/feedback guide with name, file and manual-review conditions; upload acceptance is not verification approval.


- [[source-adyen-docs-platforms-manage-account-holder-risk]] — 2026-09-15-captured Platforms Score guide for role-gated account-holder cases, risk rules/actions, payout controls, irreversible identity exclusions and conditional risk webhooks; flags are not fraud or payout proof.


- [[source-adyen-docs-platforms-identify-account-holder-risk]] — 2026-09-15 Score overview for platform-user risk signals, weighted scores, linked-account grouping, platform-selected controls and limited device-data pilot.


- [[source-adyen-docs-platforms-manage-balance-accounts]] — 2026-09-15 Configuration API/Customer Area guide to account-holder-linked balance-account creation, viewing, description update and permanent zero-balance closure; examples do not prove funded state or payout.

- [[source-adyen-docs-platforms-balance-types]] — 2026-09-15 Platforms per-currency balance-type definitions, viewing routes and examples, including an unresolved Available and Pending available formula-versus-example conflicts.



- [[source-adyen-docs-platforms-manage-access-api-credentials-web-service]] — 2023-modified, 2026-09-15-captured balance-platform web service/LEM credential, role, test/live, rotation and deactivation guide; possession does not prove permission or operation.


- [[source-adyen-docs-platforms-onboard-users]] — 2024-modified, 2026-09-15-captured Platforms hosted/invite/API-only onboarding overview, with entity/country and capability gates; data collection is not verification approval.


- [[source-adyen-docs-platforms-onboard-users-onboarding-versions]] — dated onboarding-version overview and v2-to-v4 Hosted/API-only migration conditions; its v4 stable statement conflicts with a later v3 stable reference.


- [[source-adyen-docs-platforms-verification-requirements-reference-additional-products]] — 2023-modified, 2026-09-15-captured Platforms additional-capabilities data reference for conditional financial-account FATCA/CRS, business-account industry codes and business-account/issuing source of funds; no eligibility or enabled-capability proof.


- [[source-adyen-docs-platforms-kyc-verification-codes-general-verification-errors]] — 2023-modified, 2026-09-15-captured general KYC verification-error code mapping for Adyen for Platforms and Issuing, with possible suberrors, missing-data/contract categories, and illustrative error-object shape; no verification or eligibility proof.


- [[source-adyen-docs-platforms-quickstart-guide-support]] — 2026-09-15 Platforms support quickstart assigning user-facing support to the platform and Adyen escalation to its business, with KYC/payout troubleshooting and ticket routes; examples and typical timing are not response or financial-outcome guarantees.


- [[source-adyen-docs-platforms-kyc-insights]] — 2026-09-15 Customer Area balance-platform KYC analytics guide for dated onboarding cohorts, verification metrics and historical errors; aggregate trends are not individual current-eligibility proof.


- [[source-adyen-docs-platforms-verification-overview]] — 2023-modified, 2026-09-15-captured Platforms verification overview for capability requests, data-change/review checks, version-qualified deadlines and asynchronous status; a deadline or request is not capability approval.


- [[source-adyen-docs-platforms-verification-overview-data-review-process]] — 2023-modified, 2026-09-15-captured periodic user-data review process: webhook/deadline, optional v3/v4 proactive request, hosted/API-only confirmation, and subsequent valid/invalid verification results; no account-specific outcome proof.


- [[source-adyen-docs-platforms-verification-overview-capabilities]] — 2024-modified, 2026-09-15-captured account-holder capability guide for requested/allowed/enabled settings, verification statuses, product-specific capability tables and deadline exceptions.


- [[source-adyen-docs-platforms-onboard-users-pci-forms]] — 2026-09-15 Platforms guide to sales-channel-dependent user SAQs, hosted/custom-UI signing and Legal Entity Management API document/status routes; submission is not independent PCI or capability approval.


- [[source-adyen-docs-platforms-onboard-users-customize-hosted-onboarding]] — 2024-modified, 2026-09-15-captured Platforms/Issuing hosted-onboarding theme, link-setting, test and debug guide; UI controls do not establish verification approval.


- [[source-adyen-docs-platforms-quickstart-guide-onboarding-and-kyc]] — 2026-09-15 Platforms user-onboarding/KYC quickstart for hosted and API-only methods, conditional verification, Terms/PCI and support; guidance does not prove capability activation or payout.


- [[source-adyen-docs-platforms-onboard-users-terms-of-service]] — 2026-09-15 Adyen for Platforms Terms guide for main-entity document generation, individual or authorized-signatory acceptance, test/live type differences and acceptance-info retrieval; examples do not prove actual legal consent or capability enablement.


- [[source-adyen-docs-platforms-kyc-verification-codes-remediating-actions]] — 2021-modified, 2026-09-15-captured Platforms/Issuing verification remediation-code catalog with parent/suberror placement, object-specific messages, conditional missing-data codes and duplicated `2_198` wording.


- [[source-adyen-docs-platforms-onboard-users-components]] — 2026-09-15 Adyen Platforms transfer-instrument Onboarding components guide for LEM v3/v4 entities, server-scoped session roles, bank-data entry/management and user-flow events; submission and status display do not prove verification or payout.


- [[source-adyen-docs-platforms-manage-stores]] — 2025-modified, 2026-09-15-captured Platforms Customer Area/Management API store guide for legal-entity business-line linking, country/role prerequisites, optional splits and irreversible store closure.


- [[source-adyen-docs-platforms-verification-requirements-onboarding-guidelines]] — 2026-09-15 in-development Platforms onboarding guide for general KYC and selected country/entity-specific ID, organization and bank-document conditions; dated guidance does not prove current eligibility or granted capabilities.


- [[source-adyen-docs-platforms-manage-transfer-instruments]] — 2023-modified, 2026-09-15-captured Legal Entity Management API/Customer Area guide distinguishing user bank-account instruments from liable-account company payout accounts, verification state and deletion effects.


- [[source-adyen-docs-platforms-verification-requirements-document-requirements]] — 2023-modified, 2026-09-15-captured conditional document-upload reference for platform verification, with entity, country, business-account/issuing and onboarding-v4 limits; submission is not verification approval.


- [[source-adyen-docs-platforms-manage-account-holders]] — 2023-modified, 2026-09-15-captured Configuration API/Customer Area guide for platform account-holder creation, status, closure and capabilities; legal entities and balance accounts remain distinct.


- [[source-adyen-docs-platforms-manage-legal-entities]] — 2024-modified, 2026-09-15-captured Adyen for Platforms Legal Entity Management API v3 guide for creating, viewing and updating legal entities, with role, region and verification-rerun boundaries.


- [[source-adyen-docs-platforms-verification-requirements]] — 2023-modified guide captured 2026-09-15 for platform user-verification inputs by country, legal-entity type and financial product, with minor-user, business-account, issuing and Capital qualifications; requirements do not prove verification or capability approval.


- [[source-adyen-docs-platforms-onboard-users-onboarding-versions-onboarding-v4]] — 2025-modified, 2026-09-15-captured Platforms onboarding v4 change guide for hosted/API-only legal-entity validation, country/entity exceptions and separate issuing/business-account source-of-funds requirements; historical rules do not prove verification or capability activation.


- [[source-adyen-docs-platforms-verification-requirements-data-formats-per-country]] — 2024-modified, 2026-09-15-captured country/entity data-format reference for Adyen for Platforms and issuing, with onboarding-version and document-verification exceptions.


- [[source-adyen-docs-platforms-get-started]] — 2022-modified, 2026-09-15-captured Platforms onboarding overview from Adyen contact/design through test integration, live application and separately replicated live setup; no activation or money-movement proof.


- [[source-adyen-docs-platforms-integration-checklist]] — 2023-modified, 2026-09-15-captured Adyen for Platforms resource, API, onboarding, splits, payout, reporting and go-live checklist; test examples and steps do not prove verified capabilities or financial outcomes.


- [[source-adyen-docs-platforms]] — 2026-09-15 current Adyen for Platforms landing page for platform/user model, verification, split-payments and payout routes, regional lists and separate optional financial products.

- [[source-adyen-docs-platforms-payout-webhooks]] — 2026-09-15 Platforms Transfer webhook guide distinguishing payout request, balance booking, bank tracking/credit, failure and return states.

- [[source-adyen-docs-platforms-view-transfers-details]] — 2026-09-15 Platforms Customer Area/Transfers API guide for listing and inspecting payment, bank and internal transfer records, with status and example limits.

- [[source-adyen-docs-platforms-transfer-transactions-track-webhooks]] — 2026-09-15 Transaction webhook guide for balance-account debit/credit events across external and internal transfers, distinct from Transfer webhook status changes.



- [[source-adyen-docs-platforms-view-payout-transfers-details]] — 2026-09-15 Platforms Customer Area and Transfers API list/detail guide with role-gated confirmation letters that prove instruction sent, not beneficiary-bank receipt.



## Related

- [[adyen-payments]] — general channel orientation.
- [[adyen-mirakl]] — connector using Adyen for Platforms; distinct from the platform overview.
- [[adyen-reporting]] — reporting route.
- [[adyen]] — provider profile.
