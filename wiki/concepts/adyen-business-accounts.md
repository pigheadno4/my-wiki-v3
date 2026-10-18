---
title: "Adyen Business Accounts"
type: concept
category: technology
tags: [adyen, business-accounts, platforms, financial-products]
---

## Definition

Adyen Business accounts are a separate Adyen for Platforms financial product for eligible platform users' business-related incoming/outgoing third-party transfers and direct receipt of platform payouts into an Adyen account. The 2023-modified overview describes API or Hosted Onboarding integration and calls the feature in development. These are dated product descriptions, not evidence that a specific user has an opened account or that any transfer settled. [[source-adyen-docs-business-accounts]]

## Evidence boundary

The captured overview conditions eligibility on user entity type, supported operating region, associated UBO/individual residence wording, and additional verification information. It lists US, mainland UK and Eurozone contexts with exclusions and US-specific onboarding detail, but those dated descriptions do not establish current regional availability, account approval, legal ownership, live balance, transfer completion or bank receipt. Keep Business accounts distinct from Capital grants and external-bank payouts; use child guides for verification, roles, consent and lifecycle.

## Sources

- [[source-adyen-docs-business-accounts-verification-requirements-reference-additional-products-brand-specific-industry-codes]] — 2026-09-15-captured Business Accounts brand-specific IC/MCC classification and conditional approval-contact reference; the captured page omits its promised accepted-value list.


- [[source-adyen-docs-business-accounts-verification-requirements-reference-additional-products-industry-codes]] — 2026-09-15-captured Business Accounts IC/MCC selection and prior-approval reference; the captured page lacks its promised accepted-code list and leaves footnotes unanchored.


- [[source-adyen-docs-business-accounts-piisp]] — 2026-09-15 third-party PIISP Open Banking funds-confirmation guide for a consented Business Account holder; the amount-specific boolean is not a funds reservation, payment instruction or settlement proof.


- [[source-adyen-docs-business-accounts-compliance-guidelines-keeping-records]] — 2024-modified, 2026-09-15-captured Business Accounts service-record guide with at-least-five-year retention after offering termination, example categories and UK/Ireland-only vulnerability recording; not legal advice or retention/delivery proof.


- [[source-adyen-docs-business-accounts-implement-sca]] — 2022-modified, 2026-09-15-captured Business Accounts SCA overview of selected actions, Authentication SDK/device route and unresolved EEA-or-UK opening versus EEA-only install callout.


- [[source-adyen-docs-business-accounts-install-auth-sdk]] — 2022-11-30-modified, 2026-09-15-captured Platforms Authentication SDK installation guide for Android, iOS and web, including dated versions and LIVE iOS build restriction; installation is not device binding, SCA completion or a financial operation.


- [[source-adyen-docs-business-accounts-compliance-guidelines-reporting-to-adyen]] — 2024-modified, 2026-09-15-captured Business Accounts event notification, daily Accounts/Issuing fraud and quarterly complaints guidance, with UK/Ireland vulnerable-user totals; not legal advice or proof of reporting.


- [[source-adyen-docs-business-accounts-compliance-guidelines-eu-depositor-info-sheet]] — 2026-09-15 Adyen N.V. EU depositor sheet on Dutch guarantee limits, aggregation, exceptions, joint-group treatment and dated euro reimbursement; it does not establish coverage or payment for a specific account.


- [[source-adyen-docs-business-accounts-compliance-guidelines]] — 2022-10-26-modified, 2026-09-15-captured Business Accounts compliance-guidelines overview linking UI, communication, support, complaints, pricing, reporting and record topics, with conditional material pre-approval and France requirements; expressly not legal advice.


- [[source-adyen-docs-business-accounts-pisp]] — 2026-09-15 open-banking PISP guide for third-party payment initiation, separate payment-status and SCA-authorization lookups; consent, finalised SCA and submitted payment do not establish creditor settlement.


- [[source-adyen-docs-business-accounts-consent]] — 2026-09-15 TPP guide to Business Accounts Open Banking consent status, separate SCA authorization status, scoped/expiring access and revocation; TPP DELETE wording conflicts with the listed termination/revocation status labels.


- [[source-adyen-docs-business-accounts-compliance-guidelines-french-intermediary]] — 2026-09-15 France-qualified Business Accounts ORIAS intermediary-registration guideline for France-registered platforms serving French users, with director capacity, mandate, approval-dependent disclaimer and annual renewal; opening Capital wording conflicts with the Business Accounts body, and this is not legal advice or registration proof.


- [[source-adyen-docs-business-accounts-use-transfer-limits]] — 2026-09-15-captured Business Accounts overview of platform/account-level outgoing transfer-limit configuration, status, conditions and decline signals; detailed account guidance narrows default override to matching scope/type.


- [[source-adyen-docs-business-accounts-compliance-guidelines-customer-complaints]] — 2024-modified, 2026-09-15-captured Business Accounts path for Adyen's financial-products complaints guideline, including identification, escalation and UK/Ireland additions; body mirrors the Platforms path and expressly is not legal advice.


- [[source-adyen-docs-business-accounts-accept-direct-debits-uk]] — 2019-modified, 2026-09-15-captured limited-availability UK Bacs direct-debit and mandate guide for Business Accounts, covering capability/account/balance checks and externally confirmed mandate changes; distinct from the SEPA route.


- [[source-adyen-docs-business-accounts-compliance-guidelines-pricing-and-eligibility]] — 2024-modified, 2026-09-15-captured pricing/eligibility compliance guide with Business Accounts/Issuing, EU/US/UK and UK-questionnaire scopes; Capital opening-copy mismatch and no-legal-advice boundary.


- [[source-adyen-docs-business-accounts-open-banking]] — 2026-09-15-captured TPP open-banking overview for Business Account information, payment initiation and funds checks, with licensing/QWAC onboarding and holder-consent boundary; its EU-only prose conflicts with UK API/availability rows.


- [[source-adyen-docs-business-accounts-use-transfer-limits-balance-platform]] — 2026-09-15 Business Accounts Configuration API guide for platform-wide outgoing-external transfer limits, condition/date lifecycle, readback and deletion/override; setup examples do not prove live enforcement or fund delivery.


- [[source-adyen-docs-business-accounts-compliance-guidelines-customer-service-support]] — 2024-modified, 2026-09-15-captured first/second-line support guide with critical-query intake, qualified retention trigger and UK/Ireland vulnerable-customer measures; not legal advice or proof of actual service performance.


- [[source-adyen-docs-business-accounts-receive-funds]] — 2022-modified, 2026-09-15-captured third-party incoming-credit and separate SEPA direct-debit guide, requiring receiveFromThirdParty allowed and enabled; priority/account-detail tables contain dated and inconsistent labels.


- [[source-adyen-docs-business-accounts-aisp]] — 2026-09-15 third-party AISP guide to consented Business Account information reads (accounts, balances and transactions), with account-list shape and transaction-path example mismatches; access is not payment initiation or bank receipt.


- [[source-adyen-docs-business-accounts-transactions-transaction-webhooks]] — 2026-09-15 transaction-webhook guide for booked balance-account debit/credit events across external/internal transfers, with broader Platforms/Issuing/Payouts prerequisite scope and unresolved example amount/account-role conflicts.


- [[source-adyen-docs-business-accounts-how-sca-works]] — 2022-modified, 2026-09-15-captured Business Accounts API SCA overview for SDK eligibility, HTTP 401 challenge exchange and endpoint-specific HTTP 2xx finalization; its authenticate-user section uses device-registration calls, so setup is not proof of per-action authentication or funds movement.


- [[source-adyen-docs-business-accounts-view-available-limits]] — 2025-modified, 2026-09-15-captured balance-account amount/count available-limit readout; its rule-restriction and aggregation exclusions, Issuing hierarchy link and authorization/capture wording limit inference about effective transfer controls or settlement.


- [[source-adyen-docs-business-accounts-compliance-guidelines-marketing-user-communication]] — 2023-modified, 2026-09-15-captured collateral review and EU/UK/US Business Accounts disclosure matrix; opening copy mislabels Capital, and the dated guidance is not legal advice or approval for specific material.


- [[source-adyen-docs-business-accounts-compliance-guidelines-user-interface]] — 2023-modified, 2026-09-15-captured financial-products UI compliance guide with general consent/provider disclosure, Business Accounts fields and conditional EU, UK and US rows; expressly not legal advice or current eligibility proof.


- [[source-adyen-docs-business-accounts-oauth-flow]] — 2026-09-15 third-party-provider open-banking OAuth and separate account-holder consent-ID flow for Business Accounts, with five-minute code, rotating refresh token and approval boundary; distinct from Partner OAuth and external-individual account verification.


- [[source-adyen-docs-business-accounts-transaction-rules-create-and-manage]] — 2021-modified, 2026-09-15-captured Configuration API guide for outgoing Business Accounts external-transfer rule creation, readback, entity-specific override/bypass and activation; internal transfers excluded, and the PATCH example has a restriction-nesting mismatch.


- [[source-adyen-docs-business-accounts-compliance-guidelines-vulnerable-users]] — 2026-09-15 UK/Ireland Adyen partner staff guide for recognizing and supporting potentially vulnerable Business Accounts users, including staff coverage, support methods, consent and factual recordkeeping; it is not legal advice.


- [[source-adyen-docs-business-accounts-transfer-funds-internally]] — 2026-09-15-captured Business Accounts internal-direct-debit guide for prerequisites, source/target balance-account roles, request fields and two-sided received-to-booked webhooks; TEST examples do not prove live movement.


- [[source-adyen-docs-business-accounts-compliance-guidelines-account-statements]] — 2023-modified, 2026-09-15-captured EU/US bank-account, UK Business Account and Issuing statement-template guidelines, with unchanged API data, Adyen approval, regional conditions and branch-wording conflict; not legal advice.


- [[source-adyen-docs-business-accounts-send-funds-transfer-routes]] — 2023-modified, 2026-09-15-captured Business Accounts Configuration API pre-transfer route calculation by country or counterparty, with returned priority/currency/requirements; sample routes and limits are not live availability or bank-receipt proof.


- [[source-adyen-docs-business-accounts-transactions]] — 2023-modified, 2026-09-15-captured Transfers API transaction-query guide for scope/filter/pagination, signed amounts, pending/booked status and booking/value dates; endpoint also covers Platforms, Issuing and Payouts contexts, and booked is not beneficiary bank receipt.


- [[source-adyen-docs-business-accounts-transaction-rules]] — 2022-modified, 2026-09-15-captured pilot overview of outgoing third-party transfer rule criteria, blocklist/velocity/bypass scope and hardBlock decline; its authorization/capture limit wording does not establish transfer settlement behavior.


- [[source-adyen-docs-business-accounts-register-sca-devices]] — 2022-modified, 2026-09-15-captured Business Accounts SCA device eligibility and registration guide for client SDK/server initiation, two-factor user step and server finalization; device setup is not proof of later user authentication or financial operation.


- [[source-adyen-docs-business-accounts-sca-for-transaction-history]] — 2022-modified, 2026-09-15-captured Transfers API transaction-history SCA guide for Platforms or Classic, covering SDK challenge, 10-minute completion and dated example limits; authentication is not transaction or bank-receipt proof.


- [[source-adyen-docs-business-accounts-send-funds-approve-cancel-transfers]] — 2020-modified, 2026-09-15-captured Business Accounts guide to additional transfer-review approval/cancellation, SCA choice and webhook review states; approval continues processing rather than proving settlement.


- [[source-adyen-docs-business-accounts-view-transfers-details]] — 2019-modified, 2026-09-15-captured Customer Area/Transfers API guide to list and inspect Business Accounts transfer states and download instruction-confirmation letters; list examples conflict with stated query constraints, and a letter is not bank-receipt proof.


- [[source-adyen-docs-business-accounts-send-funds]] — 2022-modified, 2026-09-15-captured outbound third-party bank-transfer guide for priorities, location/currency/format limits and cut-offs, with conflicting SEPA/US timing and cross-border priority wording; no beneficiary-receipt proof.


- [[source-adyen-docs-business-accounts-third-party-transfer-webhooks]] — 2026-09-15 Business Accounts Transfer-webhook examples for third-party incoming funds, direct debit requests and outgoing bank transfers, including accounting versus tracking states, ETA/tracing, refusal, failure and return boundaries.


- [[source-adyen-docs-business-accounts-send-funds-verify-counterparty]] — 2026-09-15 Business Accounts EU/UK domestic outgoing-transfer recipient name-check guide; API role, response/user-confirmation flow and test simulation are distinct from transfer execution or bank receipt.


- [[source-adyen-docs-business-accounts-manage-sca-devices]] — 2022-modified, 2026-09-15-captured Business Accounts SCA device list, challenge-based payment-instrument association and per-business-account deregistration guide; requires Bank SCA Webservice Role and does not prove a user authenticated.


- [[source-adyen-docs-business-accounts-business-account-statement]] — 2026-09-15 CAMT.053 Business Account statement setup, webhook download, XML/code mapping and optional summarized-file reference; statements support reconciliation but do not prove a specific account's funds or user-facing statement delivery.


- [[source-adyen-docs-business-accounts-send-funds-ideal-integration]] — 2025-08-22-modified, 2026-09-15-captured Netherlands iDEAL A2A issuer integration guide for paying from Business Accounts, with SCA, redirect/QR and confirm/cancel boundaries; integration examples and return links do not prove live funds movement.


- [[source-adyen-docs-business-accounts-use-transfer-limits-balance-accounts]] — 2026-09-15-captured Configuration API guide for outgoing external transfer limits on Business Account linked balance accounts, with SCA, lifecycle, override, readback and example conflicts.


- [[source-adyen-docs-business-accounts-send-funds-make-transfer-request]] — 2026-09-15-captured Business Accounts third-party bank transfer request guide for requirements, optional validation/review, request fields and webhook status; successful submission does not prove settlement or bank receipt.


- [[source-adyen-docs-business-accounts-sca-for-funds-transfers]] — 2022-modified, 2026-09-15-captured Authentication SDK SCA guide for EEA Business Accounts transfers, with initiation and reviewer-approval routes, 10-minute window and example inconsistencies; authentication evidence is not settlement proof.


- [[source-adyen-docs-business-accounts-account-structure-resources-platform-account-structure]] — 2026-09-15 platform-versus-user resource map and distinct liable/user/instrument-linked balance-account roles; its multiple-Business-Accounts-per-balance-account statement conflicts with the captured one-number/one-bankAccount-instrument creation guides.


- [[source-adyen-docs-business-accounts-manage-access]] — 2023-modified, 2026-09-15-captured Business accounts Customer Area user and web-service credential role guide, including sole-proprietor IBAN PII and Transfers API v1 scope; roles do not prove access or operations.


- [[source-adyen-docs-business-accounts-verification-requirements]] — 2023-modified, 2026-09-15-captured Business Accounts additional verification-data and US onboarding-disclosure guide, with country/entity/conditional document scope and a linked US FATCA/CRS exception; data collection is not KYC or account-opening proof.


- [[source-adyen-docs-business-accounts-integration-checklist]] — 2023-modified, 2026-09-15-captured Business Accounts integration/go-live checklist for platform prerequisites, resource/credential/webhook setup, added verification and separately replicated live configuration with end-to-end checks; checklist steps are not live-operation proof.


- [[source-adyen-docs-business-accounts-verification-overview-capabilities]] — 2024-modified, 2026-09-15-captured Business Accounts account-holder capability guide for issueBankAccount and third-party flow permissions, requested/allowed/enabled flags, and pending/invalid verification deadline exceptions; flags do not prove an opened account.


- [[source-adyen-docs-business-accounts-onboard-users]] — 2024-modified, 2026-09-15-captured Business accounts API-only onboarding and v4 source-of-funds/country-data guidance; submission starts verification, not account opening.


- [[source-adyen-docs-business-accounts-manage-balance-accounts]] — 2026-09-15-modified Configuration API guide to create, view, update and permanently close account-holder-linked balance accounts; zero balance gates closure, while TEST resource/status/currency examples are not funded or usable Business Account proof.


- [[source-adyen-docs-business-accounts-verification-requirements-data-formats-per-country]] — 2024-modified, 2026-09-15-captured country/entity data-format tables for verification inputs across Platforms and Issuing; rows are examples, not Business Accounts eligibility or KYC approval.


- [[source-adyen-docs-business-accounts-verification-requirements-reference-additional-products]] — 2023-modified, 2026-09-15-captured FATCA/CRS, industry-code and SOF information guide for Business accounts (SOF also Issuing), with US exception, approval gates and field-path inconsistency; not KYC approval proof.


- [[source-adyen-docs-business-accounts-create-business-accounts]] — 2024-modified, 2026-09-15-captured Business Accounts guide for the verified-account-holder bankAccount payment-instrument creation flow, dated NL/US currency constraints and one-number-per-balance-account limit; examples are not live account or funds proof.


- [[source-adyen-docs-business-accounts-verification-overview]] — 2023-modified, 2026-09-15-captured Business Accounts KYC/capability process for asynchronous checks, data-review triggers, LEM-v3/v4 verification deadlines and permission loss.


- [[source-adyen-docs-business-accounts-verification-overview-data-review-process]] — 2023-modified, 2026-09-15-captured legal-entity periodic-review guide for deadline/capability webhooks, onboarding-v3/v4 proactive requests and user confirmation plus error resolution; request/confirmation is not KYC approval.


- [[source-adyen-docs-business-accounts-verify-account-holder]] — 2026-09-15 Open Banking/AISP route and report guide for an unregistered external individual's bank-account verification across Platforms, Marketplaces or Classic; it is not registered account-holder capability verification or Business Account opening proof.


- [[source-adyen-docs-business-accounts-kyc-verification-codes-remediating-actions]] — 2021-modified, 2026-09-15-captured KYC remediating-action code catalog for verificationErrors/subErrors, with conditional entity/field messages and duplicate `2_198` mapping; action codes do not prove approval or authorize retries.

- [[source-adyen-docs-business-accounts-kyc-verification-codes]] — 2021-modified, 2026-09-15-captured account-holder capability verification-code overview for Platforms/Issuing scope, three code layers, channels, roles and problems-array location; action availability is conditional and codes do not prove verification.



- [[source-adyen-docs-business-accounts-onboard-users-terms-of-service]] — 2026-09-15 Business Accounts onboarding ToS flow for webhook requirement, test/live document types, generated document IDs, authorized individual signer and acceptance-record readback.


- [[source-adyen-docs-business-accounts-kyc-verification-codes-general-verification-errors]] — 2023-modified, 2026-09-15-captured general verificationErrors code catalog under Business accounts KYC, also naming Platforms/Issuing scope and linking suberror/action references; not account-approval proof.


- [[source-adyen-docs-business-accounts-verification-requirements-document-requirements]] — 2023-modified, 2026-09-15-captured Business accounts document-upload reference for conditional KYC evidence by person/entity/bank, onboarding-v4 selfie, country/age/format exceptions and unresolved photo-ID file-count conflict.


- [[source-adyen-docs-business-accounts-manage-legal-entities]] — 2024-modified, 2026-09-15-captured LEM API v3/Customer Area guide to create, view, patch and type-change legal-entity resources for Business accounts onboarding, with PII role and verification-rerun limits; resource creation is not account-opening proof.


- [[source-adyen-docs-business-accounts-manage-account-holders]] — 2023-modified, 2026-09-15-captured Configuration API/Customer Area guide for legal-entity-linked account holders, capability/verification flags, zero-balance ordered closure and KYC roles; mixed capability examples and missing suspension section limit procedure inference.


- [[source-adyen-docs-business-accounts-kyc-verification-codes-sub-errors]] — 2023-modified, 2026-09-15-captured verification suberror family/table reference for Platforms or Issuing integrations, with code-specific remediating-action links and a setup-stop affiliation row.


- [[source-adyen-docs-business-accounts-account-structure-resources]] — 2021-modified, 2026-09-15-captured Business accounts resource map for regional balance platform, account holder/legal entity, balance accounts and bankAccount payment instrument; two-account prose conflicts with a one-account example, and setup is not account-opening proof.

- [[source-adyen-docs-business-accounts-account-structure-resources-legal-entity-management]] — 2026-09-15-captured Business Accounts LEM resource overview for legal entities, payout transfer instruments and supporting documents as verification inputs; resource creation is not verification, account-opening or payout proof.



- [[source-adyen-docs-business-accounts-get-started]] — 2022-modified, 2026-09-15-captured Business Accounts onboarding route for Platforms enablement, authentication, child implementation topics, test validation and separate live configuration; not proof of an opened account or transfer.


- [[source-adyen-docs-business-accounts]] — 2023-07-06-modified Business accounts landing page captured 2026-09-15 for product purpose, development warning, dated eligibility and child routes.

## Related

- [[adyen-financial-products]] — financial-products umbrella.
- [[adyen-platforms]] — platform integration context.
