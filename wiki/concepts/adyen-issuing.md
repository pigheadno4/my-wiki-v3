---
title: "Adyen Issuing"
type: concept
category: technology
tags: [adyen, issuing, cards, balance-platform]
---

## Definition

Adyen Issuing is a platform-facing card program for creating virtual and physical cards for users. The 2023-modified overview captured 2026-09-15 describes a balance-platform model with an `accountHolder`, a funds-holding `balanceAccount`, and a card `paymentInstrument` associated with that balance account. It also describes platform-side authorization decisions or optional automatic transaction rules, plus a company liable balance account for loading cards and balance transfers. [[source-adyen-docs-issuing]]

## Evidence boundary

The overview says an Issuing integration must accept and handle webhooks for asynchronous events, including payments, captures and refunds. Its EEA, UK and US support list is a dated snapshot; the page does not establish current availability, a particular platform's eligibility, PCI scope for a particular use case, an active issued card, successful authorization, capture or settled funds. Keep Issuing separate from Business accounts and Capital; their own guides govern those products.

## Sources

- [[source-adyen-docs-issuing-components-overview-after-payment]] — 2026-09-15-captured after-payment component route linking the Transactions filter/export/detail guide; this page itself is navigation only.


- [[source-adyen-docs-issuing-components-overview-before-payment]] — 2026-09-15 Issuing before-payment component index: account-holder legal-entity verification context and Transfer Instrument bank-account/verification UI, with links to detailed guides.


- [[source-adyen-docs-issuing-report-types-balance-platform-accounting-report-cash-management]] — 2026-09-15-captured Accounting Report cash-management guide for balance columns, bank/internal-transfer classification and internal-transfer example rows; internal-transfer reference-matching prose differs from the shown two-account table.


- [[source-adyen-docs-issuing-report-types-balance-platform-accounting-report-authorization-rate]] — 2026-09-15-captured Issuing Accounting Report field note for acquirer-sent context used in authorization-refusal investigation; no rate formula or measured outcome.


- [[source-adyen-docs-issuing-report-types]] — 2022-modified, 2026-09-15-captured Issuing report index for accounting, balances, instruments and received payments with CSV/TSV formats; dedicated Received Payments guide marks that report deprecated.


- [[source-adyen-docs-issuing-add-manage-funds-process-payments-make-a-payment]] — 2026-09-15 Issuing guide for online/Terminal API payments from customers whose revenue can fund issued cards; distinguishes channel-specific setup and amount units, and flags unlabeled split data in its example.


- [[source-adyen-docs-issuing-balance-updates]] — 2026-09-15 Issuing pilot overview for scoped Balance webhook subscription, settings and inheritance; its all-conditions statement conflicts with an any-condition row in the linked configuration guide.


- [[source-adyen-docs-issuing-settle-funds]] — 2026-09-15-captured merchant-account-to-balance-platform settlement guide for configurable delay, net payable batches and configured balance accounts; hotel example has a SEK/EUR currency error.


- [[source-adyen-docs-issuing-components-overview]] — 2026-09-15 Issuing-path UI component catalog for Transfer Instrument and Transactions, server-created role-bearing sessions and client initialization, with Adyen for Platforms-linked region wording.


- [[source-adyen-docs-issuing-add-manage-funds-top-ups]] — 2020-modified, 2026-09-15-captured recurring top-up overview: bank-source direct-debit request into balance account, fixed/target amount, schedule/threshold checks and source-instrument ID; captured schedule requiredness and threshold equality wording need care.


- [[source-adyen-docs-issuing-report-types-payment-instrument-report]] — 2022-modified, 2026-09-15-captured Issuing Payment Instrument Report guide for scheduled/manual card-inventory snapshots, point-in-time statuses and account-holder/balance-account link fields; sample columns vary by platform settings.


- [[source-adyen-docs-issuing-add-manage-funds-process-payments]] — 2026-09-15-captured Enterprise Issuing acquired-payment funding route: merchant account after fees to net settlement batches and configured balance account, with batch-level webhook/report reconciliation and a hotel-example currency inconsistency.


- [[source-adyen-docs-issuing-raise-disputes-attach-supporting-information]] — 2026-09-15 Issuing dispute-evidence attachment guide for Base64 upload, retrieval, list and deletion; preserves pre-submission recommendation, per-file limits and possible retention after delete.


- [[source-adyen-docs-issuing-balance-updates-use-cases]] — 2026-09-15-captured pilot balance-webhook examples for platform, account-holder and balance-account thresholds; JPY numeric example and account-targeted event identity need care.


- [[source-adyen-docs-issuing-webhook-types]] — 2020-modified, 2026-09-15-captured Issuing webhook-family catalog for configuration, balance, transfer, dispute and report events; payment webhooks deprecated, with second-chargeback naming/mapping differences from the related dispute guide.


- [[source-adyen-docs-issuing-balance-updates-manage-balance-webhook]] — 2026-09-15-captured pilot guide for Issuing balance-webhook setting lookup, PATCH condition replacement/deactivation and DELETE; removing the last condition widens notifications to all balance changes in scope.


- [[source-adyen-docs-issuing-balance-updates-configure-balance-webhook]] — 2026-09-15-captured pilot Balance webhook subscription and Configuration API settings guide for balance-change notifications; prose and curl example differ on endpoint path.


- [[source-adyen-docs-issuing-add-manage-funds-funds-transfers]] — 2020-modified, 2026-09-15-captured Issuing guide for external-bank funding and same-platform balance-account push/pull transfers, with source-role prerequisites and later completion tracking; its linked webhook guide is bank-transfer scoped and does not establish an internal-transfer event sequence.


- [[source-adyen-docs-issuing-report-types-received-payments-report]] — 2021-modified, 2026-09-15-captured deprecated card-payment report guide; points to the Accounting Report and qualifies selected-day status by a two-week generation recommendation.


- [[source-adyen-docs-issuing-raise-disputes-manage-disputes]] — 2026-09-15 guide to draft-only raised-dispute edits and submitted/closed transitions; closure prevents editing, submission or reopening, and updated webhooks record state changes rather than outcomes.


- [[source-adyen-docs-issuing-report-types-balance-platform-accounting-report-payment-lifecycle]] — 2022-modified, 2026-09-15-captured Accounting Report row examples for issued-card capture, partial capture/expiry, cancellation, adjustment and refund; cancellation prose conflicts with its captured row.


- [[source-adyen-docs-issuing-add-manage-funds-external-bank-transfer]] — 2026-09-15 Issuing push-funding guide: onboarded external bank account to Adyen funding account, then booking to the account holder's primary balance account after matching; verification and booked-webhook availability gates.


- [[source-adyen-docs-issuing-add-manage-funds-top-ups-sign-terms-of-service]] — 2026-04-28-modified, 2026-09-15-captured guide to `directDebit` top-up contract Terms of Service acceptance through Legal Entity Management API, with main-entity/individual-signatory roles and Customer Area wizard alternative.


- [[source-adyen-docs-issuing-raise-disputes-fraud]] — 2026-09-15 Issuing cardholder fraud-dispute guide: card closure, transaction-linked draft/review/submission, report-only option and ARN-linked outcome tracking; source leaves no-transaction reporting versus required transactionId unresolved.


- [[source-adyen-docs-issuing-webhook-types-network-tokens-events]] — 2026-03-16-modified, 2026-09-15-captured issuer-side wallet-network-token created/updated webhook guide; created is inactive even with approval, later updated confirms active or closed lifecycle states.


- [[source-adyen-docs-issuing-raise-disputes]] — 2026-09-15 Issuing guide for cardholder dispute reasons, 35-dispute limit, reason-specific 120-day windows, draft/closed/submitted lifecycle and chargeback versus won outcomes.


- [[source-adyen-docs-issuing-3d-secure-oob-auth-sdk-authenticate-cardholders]] — 2023-modified, 2026-09-15-captured Issuing OOB Authentication SDK challenge guide: relayed webhook, SDK output, ACS finalization deadlines and outcome webhook; flags the troubleshooting guide's broad no-webhook conflict.


- [[source-adyen-docs-issuing-transactions]] — 2020-modified, 2026-09-15-captured Transfers API guide for platform/account-holder/balance-account transaction queries, pagination and incoming/outgoing booked-funds interpretation; examples span more than issued-card payments.


- [[source-adyen-docs-issuing-raise-disputes-duplicate]] — 2026-09-15 duplicate-charge dispute guide for same-card or two Adyen-issued-card charges, matched transaction IDs/amounts, draft evidence and irreversible submission, followed by status and ARN reconciliation. Sample boolean/type discrepancies require schema verification.


- [[source-adyen-docs-issuing-tokens-digital-wallet]] — 2026-09-15-captured Issuing digital-wallet network-token provisioning guide for prerequisites, inactive creation, risk-based activation/authentication or closure, and related webhooks.


- [[source-adyen-docs-issuing-add-manage-funds-top-ups-top-up-webhooks]] — 2020-modified, 2026-09-15-captured Issuing recurring top-up Configuration, Transfer and Transaction webhook guide; accepted API responses are asynchronous, and its examples conflict on direct-debit transfer direction.


- [[source-adyen-docs-issuing-webhook-types-fund-transfers-webhooks]] — 2020-modified, 2026-09-15-captured Issuing bank-transfer webhook guide: outgoing and incoming balance-account states, later transaction events and possible post-booking outgoing failure.


- [[source-adyen-docs-issuing-tokens-digital-wallet-authentication-data]] — 2023-modified, 2026-09-15-captured Issuing guide for phone/email authentication data and OTP during digital-wallet card addition; its creation-time wording is qualified by the later card-update route.


- [[source-adyen-docs-issuing-3d-secure-oob-auth-sdk-register-devices]] — 2023-modified, 2026-09-15-captured iOS/Android OOB SCA device-registration flow, server POST/SDK/PATCH completion, Adyen-side configuration and one-device-per-card replacement boundary.


- [[source-adyen-docs-issuing-raise-disputes-not-delivered]] — 2026-09-15 Issuing non-delivery dispute guide: merchant-contact/refund checks, draft evidence and cardholder review, irreversible submission, and later webhook/ARN reconciliation; examples do not prove outcome.


- [[source-adyen-docs-issuing-report-types-balance-platform-accounting-report]] — 2026-09-15-captured Balance Platform Accounting Report guide for transfer/transaction reconciliation, CET report window and column definitions; `cancelled` rows can have a Transaction Id without money movement.


- [[source-adyen-docs-issuing-add-manage-funds-top-ups-manage-recurring-top-ups]] — 2026-09-15-captured Issuing guide to Configuration API/Customer Area viewing, updating and deleting recurring balance-account top-up schedules; includes transfer-instrument capability, no on-demand support and immutable funding-source boundary.


- [[source-adyen-docs-issuing-tokens-digital-wallet-apple-pay-provisioning]] — 2023-modified, 2026-09-15-captured work-in-progress SDK guide for issuer-app and direct-Wallet Apple Pay card provisioning, activation data and extension time limits.


- [[source-adyen-docs-issuing-add-manage-funds-top-ups-create-recurring-top-ups]] — 2026-09-15-captured Issuing recurring direct-debit top-up setup and tracking guide; EUR/USD and capability/Terms limits, with unresolved threshold-equality and payload-example differences.


- [[source-adyen-docs-issuing-components-overview-before-payment-transfer-instrument-component]] — 2026-09-15 Issuing-path Transfer Instrument Configuration/Management component guide for bank-account onboarding, scoped sessions, user events, and verification/payout outcome boundaries.


- [[source-adyen-docs-issuing-3d-secure-oob-auth-sdk-manage-devices]] — 2022-modified, 2026-09-15-captured Issuing guide for SCA device lookup, authenticated card association and per-card deregistration; flags conflicting GET SDK snippets.


- [[source-adyen-docs-issuing-manage-network-tokens]] — 2026-09-15-captured Issuing guide for card-linked digital-wallet network-token lookup, asynchronous status updates and example transaction rules; flags path/type inconsistencies and the authorization-rule versus token-count-limit ambiguity.


- [[source-adyen-docs-issuing-webhook-types-payment-events]] — 2020-modified, 2026-09-15-captured Issuing payment-event webhook guide for transfer states, scheme advice, capture variants including forced capture, expiry and unlinked refunds.


- [[source-adyen-docs-issuing-network-tokens]] — 2026-09-15-captured Issuing overview of wallet and merchant card-on-file network tokens for Adyen-issued cards, prerequisites and inactive/active/suspended/permanently closed lifecycle.


- [[source-adyen-docs-issuing-balance-types]] — 2026-09-15-captured Issuing-path balance-type definitions, per-currency lookup routes and worked examples; printed formulas conflict with example values.


- [[source-adyen-docs-issuing-add-manage-funds]] — 2026-09-15-captured Issuing funding-routes overview: verified external bank transfer, internal balance-platform transfer, and conditional booking of Adyen-acquired payment revenue.


- [[source-adyen-docs-issuing-verification-requirements-reference-additional-products-brand-specific-industry-codes]] — 2026-09-15 Issuing-path brand-specific IC/MCC selection note; captured page omits the promised accepted-values list and gives a conditional pre-onboarding approval contact.


- [[source-adyen-docs-issuing-verification-requirements-reference-additional-products-industry-codes]] — 2026-09-15-captured Issuing industry-code guidance; the accepted-code list is absent from the raw snapshot, leaving its footnotes unanchored.


- [[source-adyen-docs-issuing-onboard-users-onboarding-steps]] — 2026-09-15 Issuing verification-requirements selector; hosted v4 is selected, but location and entity type are missing, so the capture contains no concrete checklist.


- [[source-adyen-docs-issuing-manage-access]] — 2026-09-15-captured Issuing Customer Area and team-access overview; initial admin verification, dashboard functions, role links and a web-service-user terminology conflict with the API-credential guide.


- [[source-adyen-docs-issuing-manage-liable-accounts]] — 2026-09-15 Adyen guide distinguishing the platform-owned main liable balance account from the reserved incorrect-splits account and its internal-transfer correction route.


- [[source-adyen-docs-issuing-3d-secure-oob-auth-sdk]] — 2023-modified, 2026-09-15-captured issuer-side OOB Authentication SDK overview for device registration and SCA factors; source notes companion installation guide's Adyen for Platforms integration requirement.


- [[source-adyen-docs-issuing-manage-access-webservice-roles]] — 2022-modified, 2026-09-15-captured Balance Platform credential role catalog for configuration, PAN/CVV response access, SCA device registration, risk rules and Transfers API, with Platforms/key and v1 limits.


- [[source-adyen-docs-issuing-3d-secure-troubleshooting]] — 2024-modified, 2026-09-15-captured Issuing 3D Secure failure, card-block and soft-decline guide; its broad no-webhook statement conflicts with the OTP guide's authentication-outcome webhook.


- [[source-adyen-docs-issuing-account-holder-status]] — 2026-09-15-captured account-holder status, Adyen-initiated suspension/closure inheritance and split routing; its inactive-card table conflicts with create/manage-cards guidance.


- [[source-adyen-docs-issuing-authorisation]] — 2023-modified, 2026-09-15-captured Issuing authorization flow: mandatory Adyen checks, optional platform transaction rules and relayed decisions with a 2000 ms response window/fallback, followed by possible scheme-advice precedence.


- [[source-adyen-docs-issuing-3d-secure-oob-auth-sdk-install-sdk-mobile]] — 2023-modified, 2026-09-15-captured mobile issuer-side OOB Authentication SDK installation and device/build prerequisites; Issuing-path page specifies Adyen for Platforms support.


- [[source-adyen-docs-issuing-3d-secure]] — 2026-09-15 Issuing 3D Secure card-enrollment guide for conditional EEA/UK scope, OTP/OOB issuer authentication, acquirer-related exemptions and later authorisation boundary.


- [[source-adyen-docs-issuing-payment-stages-authorisation-holds]] — 2026-09-15-captured Issuing guide to merchant-only reversals, Visa/Mastercard hold expiry and capture after expiry.


- [[source-adyen-docs-issuing-kyc-verification-codes]] — 2024-modified, 2026-09-15-captured overview of Issuing/Platforms verification code structure, account-holder capability `problems` retrieval and separate general/suberror/remediating-action catalogues.


- [[source-adyen-docs-issuing-account-structure-resources-issuing-enterprise]] — 2026-09-15 Enterprise Issuing account-structure guide for organization-funded employee cards, acquiring versus verified-bank top-ups, conditional regional/stores rules, and merchant-to-balance-account settlement mapping.


- [[source-adyen-docs-issuing-authorisation-scheme-advice]] — 2026-09-15-captured Issuing guide to post-initial scheme authorization advice, final status/reserved-balance precedence, additional transfer webhooks, Customer Area history and additive accounting rows.


- [[source-adyen-docs-issuing-verification-overview]] — 2023-modified, 2026-09-15-captured Issuing verification overview for capability checks, re-verification, version-qualified deadlines and status/webhook boundaries.


- [[source-adyen-docs-issuing-verification-requirements-reference-additional-products]] — 2026-09-15 Issuing-path business-line industry-code and source-of-funds reference; its Issuing no-additional-requirements claim conflicts with the card-issuing SOF section, and its processed-funds field paths differ.


- [[source-adyen-docs-issuing-authorisation-transaction-rules-examples]] — 2022-modified, 2026-09-15-captured illustrative Issuing rule payloads for channel, MCC/country, velocity, scoped limits and scores; time-window prose/JSON differ and some payloads are incomplete.


- [[source-adyen-docs-issuing-payment-stages]] — 2019-modified, 2026-09-15-captured Issuing payment-stage guide for reserved authorisation, merchant capture, scheme advice, forced-capture liabilities and refund-request webhooks.


- [[source-adyen-docs-issuing-validation-checks]] — 2021-modified, 2026-09-15-captured Issuing validation-result/type and refusal-reason catalog, including conditional relayed-authorisation stand-in fallback.


- [[source-adyen-docs-issuing-manage-balance-accounts]] — 2026-09-15-captured Issuing Configuration API and Customer Area guide for creating, viewing and updating user balance accounts, with a zero-balance prerequisite for permanent closure.


- [[source-adyen-docs-issuing-manage-access-api-credentials-web-service]] — 2026-09-15-captured balance-platform web-service/LEM credential lifecycle; Issuing-path page with an Adyen for Platforms-only requirements table.


- [[source-adyen-docs-issuing-verification-overview-capabilities]] — 2024-modified, 2026-09-15-captured Issuing-path account-holder capability catalog, verification statuses, allowed/enabled controls and per-card/day levels.


- [[source-adyen-docs-issuing-authorisation-transaction-rules-view-available-limits]] — 2025-modified, 2026-09-15-captured guide to card-level available-limit lookup, supported rule restrictions and authorization-based counters; flags example timezone-field mismatch.


- [[source-adyen-docs-issuing-kyc-insights]] — 2026-09-15-captured Customer Area KYC analytics guide for role-gated balance-platform onboarding cohorts, verification attempts/time, historical error categories and daily refresh.


- [[source-adyen-docs-issuing-onboard-users-customize-hosted-onboarding]] — 2026-09-15-captured hosted-onboarding theme, locale, settings, test-bank and debug guide shared by Issuing and Adyen for Platforms; debug reports contain sensitive data.


- [[source-adyen-docs-issuing-kyc-verification-codes-general-verification-errors]] — 2021-modified, 2026-09-15-captured code catalog for broad Issuing/Platforms `verificationErrors`, possible suberrors and remediating-action links; includes capability-disallowed, missing-data, contract and review cases.


- [[source-adyen-docs-issuing-3d-secure-password-otp]] — 2021-modified, 2026-09-15-captured Issuing guide for cardholder password and SMS/email OTP authentication data, separate authorisation, and outcome webhooks.


- [[source-adyen-docs-issuing-verification-requirements]] — 2021-modified, 2026-09-15-captured Issuing/Platforms guide to country, legal-entity and capability-level verification factors, including dated minor-onboarding and UBO conditions; VAT wording differs from the sole-proprietorship list.


- [[source-adyen-docs-issuing-kyc-verification-codes-remediating-actions]] — 2021-modified, 2026-09-15-captured Issuing-path remediation action-code catalog for verification errors/suberrors; source flags conditional messages and duplicate `2_198`.


- [[source-adyen-docs-issuing-payment-stages-check-details-payment]] — 2019-modified, 2026-09-15-captured guide to Transfers API/Customer Area payment-detail lookup and webhook tracking, with a Platforms-integration requirement and conflicting list-query examples.


- [[source-adyen-docs-issuing-authorisation-transaction-rules]] — 2022-modified, 2026-09-15-captured Issuing transaction-rule concepts: scope, limits, outcomes, hierarchy and relayed-authorisation ordering; condition logic conflicts with the companion creation guide.

- [[source-adyen-docs-issuing-authorisation-relayed-authorisation]] — 2023-modified, 2026-09-15-captured platform webhook decision guide with 2000 ms response/fallback wording, endpoint/configuration requirements, and response-shape example conflict; validation-checks separately says 1500 ms stand-in.



- [[source-adyen-docs-issuing-onboard-users-terms-of-service]] — 2026-09-15 Issuing-path Terms of Service guide for determining required document types, presenting them and recording acceptance by an individual or organizational signatory; its requirements table says Adyen for Platforms and its test-type response conflicts with its example.


- [[source-adyen-docs-issuing-manage-legal-entities]] — 2026-09-15-captured Issuing guide to API legal-entity creation and API, Customer Area, or Hosted onboarding viewing and updating, including verification and main-entity type-change boundaries.

- [[source-adyen-docs-issuing-account-structure-resources-legal-entity-management]] — 2026-09-15-captured Issuing account-structure reference defining legal entity, verified payout transfer instrument, supporting document, and business line resources for user verification.



- [[source-adyen-docs-issuing-onboard-users-components]] — 2026-09-15-captured Issuing-path Transfer Instrument Configuration/Management component guide; LEM v3/v4, Adyen for Platforms and scoped session prerequisites, with verification and payout outcome boundaries.

- [[source-adyen-docs-issuing-onboard-users]] — 2023-modified, 2026-09-15-captured hosted versus API-only user onboarding guide, with dated location/feature limits and v4 issuing business-line/source-of-funds requirements; prose/table differ on the Adyen-processed-funds field path.



- [[source-adyen-docs-issuing-create-cards]] — Adyen Issuing create-cards guide (captured 2026-09-15): virtual versus physical `paymentInstrument` responses, manufacturing and authorized-user requirements.


- [[source-adyen-docs-issuing-manage-account-holders]] — 2023-modified, 2026-09-15-captured Issuing account-holder management guide for creation, capability verification, status transitions, close order, and KYC views.


- [[source-adyen-docs-issuing-kyc-verification-codes-sub-errors]] — 2021-modified, 2026-09-15-captured Issuing-path KYC suberror catalog for granular causes, linked action codes and the `1_5052` setup stop condition.


- [[source-adyen-docs-issuing-authorisation-transaction-rules-create-and-manage]] — 2025-modified, 2026-09-15-captured Issuing guide for creating, viewing, overriding, skipping, updating and activating transaction rules; source flags payout/card and sample-response conflicts.


- [[source-adyen-docs-issuing-verification-requirements-document-requirements]] — 2023-modified, 2026-09-15-captured Issuing verification document-upload requirements after automatic verification fails, including document categories and section-specific conditions.


- [[source-adyen-docs-issuing-test-verification-errors]] — 2026-09-15 Adyen test-environment guide for forcing legal-entity, document and transfer-instrument verification suberrors, reading account-holder/GET results, and simulating remediation; excludes hosted onboarding.


- [[source-adyen-docs-issuing-account-structure-resources-issuing-embedded]] — 2026-09-15-captured account-structure guide for embedded Issuing with acquiring versus verified-transfer-instrument top-ups, platform/user resource ownership and separate user-funds/card-linked balance accounts; salon example has a food-and-delivery wording mismatch.


- [[source-adyen-docs-issuing-account-structure-resources]] — 2026-09-15-captured Issuing account-structure guide for enterprise versus embedded funding roles, merchant-account connection, and user/liable balance-platform resources.


- [[source-adyen-docs-issuing-integration-checklist]] — Adyen Issuing integration and go-live checklist (captured 2026-09-15): test setup, account-holder verification, card/payment checks and separate live transition.


- [[source-adyen-docs-business-accounts-compliance-guidelines-account-statements]] — 2023-modified, 2026-09-15-captured statement-template guidelines including Issuing's pre-issuance sample review and EU UI versus UK durable-download rule; not legal advice.


- [[source-adyen-docs-issuing-get-started]] — Adyen Issuing get-started webpage (captured 2026-09-15): contact-led design, test integration, and separate live-account setup.

- [[source-adyen-docs-issuing-manage-cards]] — 2019-modified, 2026-09-15-captured card-management guide for inactive-only balance-account reassignment, activation, reversible suspension, irreversible closure, and Customer Area payment viewing.


- [[source-adyen-docs-issuing-verification-requirements-data-formats-per-country]] — 2024-modified, 2026-09-15-captured country/region format reference for Issuing and Platforms verification data, including field-specific format exceptions and document conditions.



- [[source-adyen-docs-issuing]] — 2023-modified, 2026-09-15-captured Issuing overview for card-program purpose, core balance-platform resources, authorization options, webhooks and conditional PCI scope.

## Related

- [[adyen-financial-products]] — umbrella product family.
- [[adyen-platforms]] — platform context.
- [[adyen]] — provider context.
