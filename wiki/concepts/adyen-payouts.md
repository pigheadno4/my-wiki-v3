---
title: "Adyen Payouts"
type: concept
category: technology
tags: [adyen, payouts, disbursements]
---

## Overview

The 2023-modified, 2026-09-15-captured [[source-adyen-docs-payouts]] landing page defines a broader Payouts umbrella: a Payments-combined Payout Service for an Adyen merchant of record paying a beneficiary not onboarded with Adyen, and a separate Adyen for Platforms route for payouts of processed payments to platform merchants or sub-merchants. This umbrella and its Payout Service child are distinct from the legacy Online Payout API material documented here; do not infer that API's integration, approval or staged-review rules for Payout Service from the landing page. The child routes own their distinct eligibility, APIs and payout lifecycle; the landing-page “real time” headline is not a completion guarantee.


Adyen's payout documentation covers outbound disbursements to suppliers, partners, or customers. The 2026-09-15 Online payouts snapshot describes a legacy Payout API with instant card and staged bank/PayPal-wallet paths, but says Adyen no longer accepts new Payout API integrations. New integrations are directed to the Transfers API; existing Payout API users are directed to their Adyen contact for migration information. Legacy Payout API use requires Adyen approval and configuration, and staged payouts require a separate reviewer to confirm and check each payout.

## Sources

- [[source-adyen-api-explorer-webhooks-latest-post-payout-expire]] — 2026-09-15-captured deprecated PAYOUT_EXPIRE incoming webhook reference for legacy Payout API users; event-scoped success and HTTP acceptance are separate from payout completion.


- [[source-adyen-api-explorer-webhooks-latest-post-payout-thirdparty]] — 2026-09-15-captured deprecated PAYOUT_THIRDPARTY webhook result contract, with legacy payout event fields, event-scoped success, HTTP receipt, and Transfer Webhooks migration route.


- [[source-adyen-api-explorer-webhooks-latest-post-payout-decline]] — 2026-09-15-captured deprecated legacy `PAYOUT_DECLINE` notification reference; `success=true` in the example is the decline event outcome, while HTTP status acknowledges receipt and neither means recipient credit.


- [[source-adyen-api-explorer-webhooks-latest-post-paidout-reversed]] — 2026-09-15-captured deprecated legacy `PAIDOUT_REVERSED` notification for institution rejection, with a promised funds return distinct from a booked return or recipient receipt; new integrations route to Transfer Webhooks.


- [[source-adyen-api-explorer-payout-latest-post-submitthirdparty]] — 2026-09-15-captured deprecated Payout API v68 TEST stored-detail submission reference; `payout-submit-received` identifies request receipt before separate confirm/decline, not settlement.


- [[source-adyen-api-explorer-payout-latest-post-storedetailandsubmitthirdparty]] — 2026-09-15-captured deprecated Payout API v68 test-server reference for storing details while submitting a third-party payout; reviewer/API confirmation or decline remains necessary, and `payout-submit-received` is a submission receipt.


- [[source-adyen-api-explorer-payout-latest-post-storedetail]] — 2026-09-15-captured deprecated Payout API v68 test-host `/storeDetail` reference for storing bank/card details under `PAYOUT` and returning a token for a separate later `/submitThirdParty`; `Success` is storage, not payout completion.


- [[source-adyen-api-explorer-payout-latest-post-declinethirdparty]] — 2026-09-15-captured deprecated Payout API v68 test-server decline reference for a previously submitted third-party payout, with original submission reference, request acknowledgement and a bracketed response-example discrepancy.


- [[source-adyen-api-explorer-payout-latest-post-confirmthirdparty]] — 2026-09-15-captured deprecated Payout API TEST v68 confirmation reference for an earlier `/submitThirdParty` PSP reference; received response is not payout completion, and example brackets differ from the schema label.


- [[source-adyen-api-explorer-payout-latest-overview]] — 2026-09-15-captured deprecated Payout API v68 overview with new-integration migration direction, separate submit versus confirm/decline credentials, TEST/LIVE host distinction and six-operation catalog; endpoint summaries do not prove payout results.


- [[source-adyen-docs-payment-methods-mobilepay-react-native-component]] — 2026-09-15 React Native Components guide's experimental `/payments` payout-token path, recurring lifecycle webhook and `/transfers` handoff; no completed payout is shown.


- [[source-adyen-docs-payment-methods-mobilepay-flutter-component]] — 2026-09-15 Flutter Components guide's experimental `/payments` payout-token creation, recurring lifecycle webhook and `/transfers` handoff; it does not document a completed payout.


- [[source-adyen-docs-payment-methods-mobilepay]] — 2026-09-15 MobilePay overview's experimental Transfers API route for payouts to linked cards, with a payout-only token generated through `/payments`; the legacy Payout API does not support this feature.


- [[source-adyen-docs-payouts-payout-service-top-up-balance-accounts]] — 2020-modified, 2026-09-15-captured Payout Service recurring direct-debit funding overview for balance accounts, with fixed/target amounts, account-timezone trigger checks and bank-instrument source; linked setup/status guides govern consent, capability and credited-funds evidence.


- [[source-adyen-docs-payouts-payout-service-transfer-transactions-transaction-webhooks]] — 2026-09-15 Payout Service-path booked balance-account transaction-webhook guide for external bank/card and internal movement, distinct from transfer-status webhooks; TEST bank request/event amounts conflict and booked debit is not bank receipt.


- [[source-adyen-docs-payouts-payout-service-top-up-balance-accounts-sign-terms-of-service]] — 2026-04-modified, 2026-09-15-captured Payout Service direct-debit top-up Terms guide for authorized-signatory/API-only presentation and LEM acceptance readback, with conditional multiple documents; not schedule or debit proof.


- [[source-adyen-docs-payouts-payout-service-transfer-transactions]] — 2023-modified, 2026-09-15-captured Transfers API transaction lookup for Platforms/Issuing/Payouts, signed balance-account booking and distinct transaction/transfer IDs; sample bank-payout ID/currency conflict and booked debit is not bank receipt.


- [[source-adyen-docs-payouts-payout-service-top-up-balance-accounts-top-up-webhooks]] — 2020-modified, 2026-09-15-captured Payout Service recurring-top-up configuration, direct-debit transfer and credited-transaction webhook guide; booked/negative-state examples and direction mismatch limit finality inferences.


- [[source-adyen-docs-payouts-payout-service-transaction-rules-create-and-manage]] — 2021-modified, 2026-09-15-captured Payout Service Configuration API guide to external-bank-payout hard-block rules, entity overrides, bypass, and active/inactive lifecycle; internal transfers are excluded.


- [[source-adyen-docs-payouts-payout-service-pay-out-to-bank-accounts-manage-bank-details]] — 2023-modified, 2026-09-15-captured Payout Service Checkout zero-auth bank-detail tokenization for later third-party bank payouts, with company credential/feature gates, local/cross-border limits and no account validation or receipt proof.


- [[source-adyen-docs-payouts-payout-service-pay-out-to-bank-accounts-transfer-routes]] — 2023-modified, 2026-09-15-captured Payout Service Configuration API preflight for country or counterparty bank routes, priorities and route requirements; calculation is separate from a payout request or bank receipt.


- [[source-adyen-docs-payouts-payout-service-transaction-rules]] — 2022-modified, 2026-09-15-captured limited-pilot Payout Service-path rule guide for scoped blocklist/velocity/bypass evaluation and hard-block decline evidence; rule decision and authorised-limit accounting are not booked payout or recipient proof.


- [[source-adyen-docs-payouts-payout-service-top-up-balance-accounts-manage-recurring-top-ups]] — 2020-modified, 2026-09-15-captured Payout Service recurring top-up schedule GET/PATCH/DELETE guide with role/capability gates, immutable funding source and sample pagination-path and funding-source-ID conflicts; schedule changes do not prove debit reversal or mandate revocation.


- [[source-adyen-docs-payouts-payout-service-pay-out-to-bank-accounts-bank-payout-request]] — 2023-modified, 2026-09-15-captured Payout Service Transfers API request guide for third-party bank payouts, one-off/token counterparty, priority fallback, optional approval and future one-attempt execution; HTTP 2XX is not bank receipt.


- [[source-adyen-docs-payouts-payout-service-pay-out-to-bank-accounts-approve-cancel-payouts]] — 2020-modified, 2026-09-15-captured Payout Service optional bank-transfer review guide for role-gated approve/cancel batches of up to 500, 30-day expiry and review webhooks; approval precedes processing and bank receipt.


- [[source-adyen-docs-payouts-payout-service-top-up-balance-accounts-create-recurring-top-ups]] — 2020-modified, 2026-09-15-captured enterprise-payouts guide for role/capability/terms-gated recurring EUR/USD direct-debit top-ups into balance accounts; API versus Customer Area threshold and fixed-field examples conflict, and a schedule is not credit proof.


- [[source-adyen-docs-payouts-payout-service-view-transfers-details]] — 2019-modified, 2026-09-15-captured Payout Service-path Customer Area/Transfers API list, detail and bank confirmation-letter guide; explicitly requires Platforms integration, has inconsistent list-query examples, and sent instruction is not bank receipt.


- [[source-adyen-docs-payouts-payout-service-pay-out-to-bank-accounts-verify-counterparty]] — 2026-09-15 enterprise-payouts domestic EU/UK bank-recipient name-check guide with distinct lookup role, response-driven user confirmation and synthetic TEST fixtures; verification is not transfer authorization or bank receipt.


- [[source-adyen-docs-payouts-payout-service-pay-out-to-cards-payout-webhooks]] — 2023-modified, 2026-09-15-captured Payout Service card-payout Transfer webhook guide for initiation, reservation, nonfinal booking, internal review, scheme acceptance and post-booking failure; sample bank wording and EUR amount figures remain unresolved.


- [[source-adyen-docs-payouts-payout-service-pay-out-to-cards-funds-disbursement]] — 2023-modified, 2026-09-15-captured Payout Service Transfers API guide for third-party Mastercard/Visa card payouts using PCI-gated raw data or CardOnFile/Subscription tokens, with future-date one-attempt and webhook-booking boundaries.


- [[source-adyen-docs-payouts-payout-service-pay-out-to-cards]] — 2023-modified, 2026-09-15-captured Payout Service guide for one-off/recurring third-party Mastercard/Visa payouts via Transfers API, with region/currency matrix, optional zero-auth and PCI-dependent tokenization; 30-minute availability is issuer-dependent, not guaranteed.


- [[source-adyen-docs-payouts-payout-service-pay-out-to-bank-accounts]] — 2023-modified, 2026-09-15-captured Payout Service Transfers API third-party bank-payout route, country/currency/priority/cut-off/statement-text tables, screening and unresolved local-currency/instant-support wording conflicts; no bank-receipt proof.


- [[source-adyen-docs-payouts-payout-service-manage-access]] — 2026-09-15 Payout Service Customer Area team-access overview for signup admin roles and routes to users, API credentials, webhooks and reports; role listing is not live authorization or payout proof.


- [[source-adyen-docs-payouts-payout-service-manage-access-webservice-roles]] — 2023-modified, 2026-09-15-captured Payout Service-path, Platforms-prerequisite Balance Platform API credential role map for Transfers API v1-only bank initiation and separate TransferService Initiate/Retrieve actions; no actual grant or transfer proof.


- [[source-adyen-docs-payouts-payout-service-getting-paid-payout-amount]] — 2026-09-15 Payout Service available-balance guide for existing versus future-value-date booked changes; negative-total wording conflicts with its USD 100/−20 → USD 80 example, so no formula or payout outcome is established.


- [[source-adyen-docs-payouts-payout-service-enterprise-accounts]] — 2026-09-15 Payout Service enterprise-account overview for balance-account-linked account details, merchant-proceeds settlement and third-party transfer routes, with Adyen-contact setup and conditional EMI/PI license gate.


- [[source-adyen-docs-payouts-payout-service-account-structure-resources]] — 2026-09-15 Payout Service merchant-account/balance-platform resource guide for payment settlement into the business's balance account before own-bank or third-party bank/card transfer requests; example topology is not Platforms user/liable ownership or receipt proof.


- [[source-adyen-docs-payouts-payout-service-balance-updates-use-cases]] — 2026-09-15 Payout Service pilot balance-webhook threshold examples for balance-platform, holder and account scope; JPY narrative, numeric setting and sample event conflict and need unit clarification.


- [[source-adyen-docs-payouts-payout-service-balance-updates-manage-balance-webhook]] — 2026-09-15 pilot Payout Service Balance webhook Configuration API lifecycle for reading, PATCHing, deactivating and deleting settings; dropping the last condition broadens notifications.


- [[source-adyen-docs-payouts-payout-service-getting-paid-scheduled-payouts]] — 2022-modified, 2026-09-15-captured Payout Service Customer Area guide for role/capability-gated custom balance-account sweeps to a verified bank instrument; a configured or triggered schedule is not debit or bank-receipt proof.


- [[source-adyen-docs-payouts-payout-service-integration-checklist]] — 2026-09-15 Payout Service resource, TEST credential/webhook, payout/report and separate LIVE setup checklist; setup and GET 200 are not payout or bank-receipt proof.


- [[source-adyen-docs-payouts-payout-service-payout-lifecycle]] — 2026-09-15 Payout Service Transfers API lifecycle separating received/authorised/booked accounting events from optional review, post-booking screening, bank/card tracking and bank returns; distinct from the legacy Payout API.


- [[source-adyen-docs-payouts-payout-service-getting-paid-transfer-statement]] — 2026-09-15 Payout Service recipient-bank statement description/reference matrix, separating accepted characters from bank-visible characters by currency and priority, including zero-visibility routes.


- [[source-adyen-docs-payouts-payout-service-getting-paid]] — 2024-modified, 2026-09-15-captured Payout Service guide for merchant proceeds to company balance/payout account, scheduled/on-demand routes, irreversible instrument deletion, regional priorities and TEST fixtures; separate from legacy Payout API.


- [[source-adyen-docs-payouts-payout-service-get-started]] — 2026-09-15 Payout Service Transfers API onboarding overview for Adyen-contact design, TEST credentials/build/test and separately configured LIVE account; distinct from the legacy Payout API.


- [[source-adyen-docs-online-payments-online-payouts-payouts-to-a-bank-account]] — Adyen legacy Payout API bank-account request examples for SEPA and US recipients, with Transfers API migration direction (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-online-payouts-payout-webhook]] — legacy Payout API webhook guide separating staged bank/wallet request acknowledgement and review events from instant-card payout events and financial-institution reversal (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-online-payouts-payouts-to-bank-accounts-and-wallets]] — unversioned legacy Payout API guide to staged bank/PayPal-wallet payouts, separate submitter/reviewer roles, seven-day review expiry, and recipient-region limits (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-online-payouts]] — Adyen Online payouts overview of the legacy Payout API, migration direction, payout paths, review requirement, and method-specific recipient-region table (webpage snapshot, 2026-09-15).
