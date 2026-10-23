---
title: "Adyen Online Payments"
type: concept
category: technology
tags: [adyen, online-payments, checkout, webhooks]
---

## Overview

Adyen Online Payments is Adyen's documentation area for accepting card, wallet, and local payment methods on websites and mobile apps.

## Integration architecture

At overview level, the integration is divided among a payments server that calls Checkout API endpoints, a client website or app that collects shopper payment details and passes payment information to the server, and a webhook server that receives payment-status and other payments-related activity. The overview recommends API Libraries and Drop-in/Components; it does not state that those choices are mandatory. Library/API updates and the product lifecycle remain qualifications when applying the overview to a specific implementation.

## Web SDK 6.47.0 implementation qualifications

The exact-version repository evidence adds a suppressible warning when more than one Core instance has been constructed. `suppressConfigWarnings: true` suppresses this warning, not every configuration warning. The static counter is cumulative for that loaded Core class; it is not a live mounted-instance count, does not prevent creation, and has no decrement in the retained implementation. Prefer reusing the checkout instance rather than interpreting suppression as lifecycle cleanup. [[source-github-adyen-web]]

Card installments now accept plan configuration without numeric `values`: one-time, revolving and bonus choices can remain while the numeric selector is omitted; regular-only configuration without values renders no installment selector. Existing amount/funding-source gates and Sessions-owned configuration remain. Drop-in changes scroll anchoring, delayed overflow visibility and reduced-motion handling, suppresses mobile tap highlights, and changes stored-method confirmation button classes. These are code/CSS findings, not browser-tested behavior or merchant enablement. Earlier release evidence remains in [[changelog-github-adyen-web]].

## Sources

- [[source-adyen-docs-payment-methods-cards-web]] — 2019-modified, 2026-09-15-captured Web cards chooser linking Drop-in, Card Component and custom-card guides; this is navigation, not child implementation, PCI or payment-outcome authority.


- [[source-adyen-docs-payment-methods-cards-ios]] — 2026-09-15 iOS card integration chooser linking Drop-in, Components and custom-card guides; child guides own prerequisites and behavior.


- [[source-adyen-docs-payment-methods-cards-android]] — 2026-09-15 Android cards chooser linking Drop-in, Components and custom-integration guides; it is navigation, not authority for child prerequisites, PCI scope or payment outcomes.


- [[source-adyen-docs-payment-methods-cards-korean-cards-web]] — 2026-09-15 Korean Card Payments via redirect Web navigation page for Drop-in/Components child guides and Sessions/Advanced main integration prerequisites; no independent method-eligibility or payment-flow proof.


- [[source-adyen-docs-payment-methods-cards-korean-cards]] — 2026-09-15 Korean Card Payments via KCP-hosted redirect overview with KR/KRW capability marks and Web versus API-only child routes; listings do not prove merchant enablement or payment outcome.


- [[source-adyen-docs-payment-methods-cards-enhanced-scheme-data-car-rental]] — 2026-09-15-captured US domestic car-rental ESD guide for eligible MCCs, Checkout payment versus Classic capture routes and required fields; both routes' prose-versus-flat-field examples and a section wording error remain source-qualified.


- [[source-adyen-docs-payment-methods-cards-enhanced-scheme-data-amex]] — 2023-modified, 2026-09-15-captured US-domestic American Express ESD field guide for Level 2/3, lodging, car-rental and airline data, with Payment API `/capture` versus Checkout capture-route qualifications.


- [[source-adyen-docs-payment-methods-apple-pay-apple-pay-certificate]] — 2023-modified, 2026-09-15-captured Apple Pay certificate overview contrasting Adyen versus merchant-owned certificates for web and native mobile, with Adyen-certificate web prerequisites and links to separate own-certificate setup guides.


- [[source-adyen-docs-payment-methods-cards-card-receipts]] — 2022-modified, 2026-09-15-captured ecommerce card sale/refund receipt guideline for delivery and direct-link retention, required fields and prohibited card/PIN/CVC data; publication does not prove delivery or payment outcome.


- [[source-adyen-docs-payment-methods-cards-korean-cards-web-drop-in]] — 2026-09-15 Korean Card Payments via redirect Web Drop-in add-on for existing Sessions or Advanced flows, with flow-specific request and test/live PCI gates.


- [[source-adyen-docs-payment-methods-cards-korean-cards-web-component]] — 2026-09-15 Korean Card Payments via redirect Web Component guide for existing Sessions/Advanced flows, redirect setup and test/live gates; the initialization snippets contain an undefined unquoted method identifier.


- [[source-adyen-docs-payment-methods-cards-enhanced-scheme-data-lodging]] — 2023-modified, 2026-09-15-captured US Visa/Mastercard lodging ESD guide for eligible MCCs and Checkout payment versus Classic capture routes; prose/example field paths and copied industry labels conflict.


- [[source-adyen-docs-payment-methods-cards-payment-facilitators]] — 2024-modified, 2026-09-15-captured Checkout `/payments` card-facilitator sub-merchant data guide for the non-AfP route, with region-specific fields and an automatic-field count/list conflict.


- [[source-adyen-docs-payment-methods-apple-pay-handle-apple-pay-errors]] — 2023-modified, 2026-09-15-captured Apple Pay error guide for amount/token, processing certificate versus web identity CSR, merchant validation and versioned `/applePay/sessions` 422 diagnostics.


- [[source-adyen-docs-payment-methods-add-payment-methods]] — 2024-modified, 2026-09-15-captured Customer Area guide for merchant-account method requests in TEST/LIVE, role and webhook prerequisites, asynchronous store creation, conditional 24-hour retry, activation/country settings and 90-day inactive deletion; configuration is not eligibility or payment-outcome proof.


- [[source-adyen-docs-payment-methods-cards-enhanced-scheme-data-airline]] — 2023-modified, 2026-09-15-captured airline ESD guide for eligible MCCs and capture-mode-specific payment/capture fields; required-field table and example disagree on departure-airport spelling and issue-date presence.


- [[source-adyen-docs-payment-methods-apple-pay-api-only]] — 2025-modified, 2026-09-15-captured Apple Pay Advanced API-only web/iOS guide for certificate, web-only merchant validation, PCI-qualified token-decryption choice and server payment request; examples are not live outcome proof.


- [[source-adyen-docs-payment-methods-cards-click-to-pay]] — 2026-09-15 Click to Pay Web card guide for versioned Sessions/Advanced setup, shopper recognition and scheme sandbox tests; recurring is Mastercard-only in this snapshot and request snippets have syntax faults.


- [[source-adyen-docs-payment-methods-cards-enhanced-scheme-data]] — 2026-09-15-captured online card ESD overview for conditional fee/compliance purposes, Advanced-flow prerequisites, MCC eligibility/exclusions and capture-route limits; child ESD guides remain separate authority.


- [[source-adyen-docs-payment-methods-apple-pay-apple-pay-certificate-ios]] — 2023-modified, 2026-09-15-captured iOS merchant-owned Apple Pay payment-processing certificate setup and renewal guide, with separate test/live IDs, web-service-user upload and approximately four-hour certificate overlap.


- [[source-adyen-docs-payment-methods-apple-pay-api-only-apple-pay-token-decryption]] — 2024-modified, 2026-09-15-captured Apple Pay API-only token guide contrasting Adyen versus PCI-gated merchant decryption, channel-specific token encoding, certificate/key and replay checks, and CIT/MIT decrypted-field maps; sample masked PAN and conditional ECI wording require care, with no payment-outcome proof.


- [[source-adyen-docs-payment-methods-apple-pay-apple-pay-certificate-web]] — 2023-modified, 2026-09-15-captured own-certificate Apple Pay Web guide for separate TEST/LIVE identifiers, Adyen processing versus merchant identity certificates, renewal overlap and Salesforce plugin exceptions.


- [[source-adyen-docs-payment-methods-cards-korean-cards-api-only]] — 2026-09-15 Korean Card Payments via redirect API-only guide for existing integrations, KR/KRW discovery and conditional redirect/PCI setup; payment-parameter and card-field examples conflict.


- [[source-adyen-docs-payment-methods-cards-enhanced-scheme-data-l2-l3]] — 2026-09-15-captured US card Level 2/3 ESD guide for eligible Mastercard/Visa payment or capture requests and validation webhooks; dated scheme limits and conflicting request-field paths are retained in the source.


- [[source-adyen-docs-payment-methods-cards-name-validation]] — 2026-09-15-captured Visa/Mastercard zero-value name-validation guide for Advanced Checkout API v69+, with issuer/region/PCI limits and conflicting examples.


- [[source-adyen-docs-payment-methods-cards-raw-card-data]] — 2022-modified API-only raw-card guide for fully PCI-compliant merchant UI/server collection, co-badged choice, /payments outcome handling and token examples; SAQ D LIVE gate and example conflicts remain source-qualified.


- [[source-adyen-docs-payment-methods-cards-android-component-earlier-versions]] — Historical Android Card Component v4.x.x Advanced-flow guide for card collection, server payment, result and token examples; adjacent submit and storage-switch snippets conflict with prose, and live prerequisites remain conditional.


- [[source-adyen-docs-payment-methods-cards-credit-card-installments]] — 2022-modified, 2026-09-15-captured online credit-card installment guide for Brazil, Mexico and Japan, versioned Web/custom-UI setup, later-charge reconciliation and country funds timing; its older required-`values` table differs from the exact Web 6.47.0 code note above.


- [[source-adyen-docs-payment-methods-cards-flutter-drop-in]] — 2026-09-15 Flutter Drop-in card add-on for existing Sessions/Advanced integrations, optional debit/credit and token routes, with unresolved storage-setting/example differences and separate live PCI gate.


- [[source-adyen-docs-payment-methods-cards-ios-drop-in]] — 2026-09-15 iOS Card Drop-in guide for Sessions/Advanced setup, card form options, tokenization and live prerequisites; Advanced storage-checkbox and Sessions consent examples conflict.


- [[source-adyen-docs-payment-methods-cards-flutter-component]] — 2026-09-15 Flutter Cards Component guide for existing Sessions/Advanced integrations, optional card UI, token examples and pre-live PCI checklist; storage-field names and consent/example models conflict within the page, so test snippets are not production or payment-outcome proof.


- [[source-adyen-docs-payment-methods-cards-ios-component]] — 2026-09-15 iOS Card Component guide for existing Sessions/Advanced integrations, versioned form and card-token options, with a conflicting Advanced storage-checkbox snippet and separate live PCI/card-setup prerequisites.


- [[source-adyen-docs-payment-methods-cards-web-drop-in]] — 2023-modified, 2026-09-15-captured cards Web Drop-in guide for existing Sessions/Advanced integrations, optional client card controls and tokenized recurring examples; version, consent, test-fixture and PCI qualifications remain in the source.


- [[source-adyen-docs-payment-methods-cards-web-component]] — 2026-09-15-captured Card Component guide for existing Sessions or Advanced Web Components integrations, versioned card-form setup, brand/debit-credit display, tokenized recurring examples and test/live PCI gates; illustrative snippets include malformed stored-card and address-lookup code, and client readiness does not prove payment outcome.


- [[source-adyen-docs-payment-methods-cards-android-component]] — 2026-09-15 Adyen Android Card Component v5.0.0+ guide for Sessions/Advanced setup, card UI and tokenized examples; its Advanced storage-switch prose conflicts with the adjacent snippet.


- [[source-adyen-docs-payment-methods-cards-custom-card-integration]] — 2026-09-15 API-only encrypted-card guide for Web Custom Card iframes versus mobile app-side collection/encryption, server `/payments`, result/webhook and stored-card routes; PCI scope and snippets require architecture/version review.


- [[source-adyen-docs-payment-methods-apple-pay]] — 2026-09-15-captured Adyen Apple Pay overview for shopper authentication, channel routes, certificate split and conditional network/region support; overview marks are not merchant enablement or payment outcomes, and its 2023 modified metadata conflicts with a 2026 Eftpos date in the body.


- [[source-adyen-docs-payment-methods-cards]] — 2023-modified, 2026-09-15-captured Cards overview for conditional PCI/card-data paths, possible LIVE documents, default post-authorisation capture, co-badged regional note and channel-specific navigation; child links do not establish eligibility or payment outcomes.


- [[source-adyen-docs-payment-methods]] — 2023-modified, 2026-09-15-captured online Drop-in/Components/API-only payment-method catalog with country, currency, feature and integration filters and per-method guide routes; listings are navigation, not merchant enablement or payment-outcome proof.


- [[source-adyen-docs-standard-integration]] — 2026-09-15 Standard Hosted Checkout versus Drop-in chooser for domain/UI, merchant server/webhook ownership, Apple Pay certificate and option-specific feature marks; child guides own execution prerequisites/outcomes.


- [[source-adyen-docs-standard-integration-drop-in-customize-checkout]] — 2026-09-15 Standard Web Drop-in customization guide for dynamic/manual payment-method ordering, locale and translation fallbacks, separate RTL direction and CSS outside iframes; custom-locale example has a variable-name mismatch.


- [[source-adyen-docs-standard-integration-drop-in-optional-drop-in-configuration]] — 2026-09-15 Standard Web Drop-in optional client configuration for method imports, session/instance settings, submission callbacks and stored-method deletion; conditional requirements and example mismatch are qualified in the source.


- [[source-adyen-docs-standard-integration-drop-in-optional-server-configuration]] — 2026-09-15 Standard Drop-in optional server guide for server-authoritative session amount updates before an irreversible `payable: true` transition and an immutable session-result lookup; mixed v70/v72 examples do not prove compatibility or capture/settlement.


- [[source-adyen-docs-standard-integration-payment-method-setup]] — 2026-09-15 Standard integration payment-method setup checklist for Apple Pay certificate/domain paths, PayPal permission, local/Support gates and selected pricing/contract qualifiers; listing is not merchant/store/session availability proof.


- [[source-adyen-docs-standard-integration-drop-in-best-practices]] — 2026-09-15 Standard Web Drop-in guidance on single client-side mount, custom-button exceptions, LIVE HTTPS/redirect hosting, regional assets/SRI and real-device testing; snippets and CDN host examples need implementation verification.


- [[source-adyen-docs-standard-integration-hosted-checkout]] — 2026-09-15 Standard Hosted Checkout Sessions guide for Checkout API v72+, server-created hosted URL, return-result lookup and authoritative AUTHORISATION webhooks; the result snapshot is immutable and is not capture/settlement proof.


- [[source-adyen-docs-standard-integration-drop-in]] — 2026-09-15 Standard Web Drop-in Sessions guide for Checkout API v72+/Web v6.30.0+, server/client/webhook integration, redirects and authorization-outcome handling; session/client status is not capture or settlement proof.


- [[source-adyen-docs-standard]] — 2026-09-15 Standard online-payments integration checklist for a bounded single-request Drop-in or Hosted Checkout path; broader Adyen features outside its linked sections are not automatically available, and checklist routes do not prove execution.


- [[source-adyen-docs-industries-peak-season-online-payments]] — 2026-09-15 seasonal online-checkout readiness guide for early changes, local-method consideration and test-market/SCA/webhook/failure-path checks; proposed benefits and tests do not prove live availability or payment outcome.


- [[source-adyen-docs-industries-markets-india]] — 2026-09-15-captured Adyen domestic India overview for local-entity/integration and account-manager onboarding, card-data/recurring mandate conditions, conditional RuPay/UPI threshold and qualified BillDesk dispute route; provider snapshot, not current approval or legal-compliance proof.


- [[source-adyen-docs-account-manage-payments]] — 2026-09-15 Customer Area payment lookup and refund/cancel/capture/re-authorization action guide with role/state gates, re-authorization risk and request-versus-outcome boundary.


- [[source-adyen-docs-account-payments-lifecycle]] — 2026-09-15 Customer Area payment-status lifecycle catalog across offers, authorization, settlement, refunds, disputes, online payouts and stored value; status finality differs from merchant payout or shopper receipt.


- [[source-adyen-docs-online-payments-upgrade-your-integration-upgrade-to-checkout-api-v72]] — 2026-09-15 Checkout API v72 online-payments request-value validation checklist and credential/Customer Area roles; the `dateOfBirth` example caption has an unresolved year typo and the page gives no SDK or runtime migration proof.


- [[source-adyen-docs-online-payments-upgrade-your-integration-migrate-to-checkout-api-upgrade-api-library]] — Java API library v40.0.0-or-later guide for Checkout API v72, use-case migration and server examples (2026-09-15 snapshot).


- [[source-adyen-docs-online-payments-out-of-app-payments-on-ios]] — 2026-09-15 snapshot of a 2023-modified iOS app-to-browser payment guide for merchant Web or Adyen Hosted Checkout, with US App Store recommendation, setup roles, return path, and webhook outcome.


- [[source-adyen-docs-online-payments-instant-card-funding]] — 2025-modified, 2026-09-15-captured Checkout `/payments` card-funding guide for top-ups and P2P funding, gated by compliance/enablement and separate from outbound payout; data-validation and partial-authorization wording conflicts remain qualified.


- [[source-adyen-docs-development-resources-raw-acquirer-responses-visa-integrity-fees]] — 2026-09-15 Adyen Visa raw-refusal fee-category and retry mapping for merchant-built online retry logic; raw code `14` conflicts between no-retry and limited-retry rows.


- [[source-adyen-docs-development-resources-refusal-reasons]] — 2026-09-15 Adyen webpage snapshot cataloging online authorization refusal fields and codes, their HTTP-versus-payment meaning, shopper-disclosure warning and row-specific retry guidance.


- [[source-adyen-docs-development-resources-overview-response-handling]] — Adyen API response overview distinguishing HTTP request status, raw acquirer response, refusal reason and payment result code (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-client-side-encryption-cse-library-public-key-location-and-token]] — Classic CSE Customer Area procedure for distinct public key, library URL and token values, test-to-live change and phased-out Web scope (2026-09-15 snapshot).


- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-classic-google-pay]] — 2026-09-15 snapshot of inactive Classic Google Pay client tokenization, server-side `/authorise` token field, and separate live Customer Area/merchant-ID setup (page metadata last modified 2019; no response outcome documented).


- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-classic-gift-cards]] — 2026-09-15 snapshot of inactive Classic API gift-card `/authorise` payments, zero-value balance-field behavior, response boundaries, and separate Stored Value API operations (page metadata last modified 2021).


- [[source-adyen-docs-online-payments-classic-integrations-modify-payments-cancel]] — inactive Classic Payment API guide for cancelling uncaptured authorizations, including original-versus-modification references and asynchronous cancel outcomes (2026-09-15 webpage snapshot).


- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-client-side-encryption]] — 2026-09-15 Classic CSE guide for browser card encryption and server-side `/authorise`, Web phaseout, mobile exception, SRI/PCI conditions and unresolved encrypted-container naming discrepancy.


- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-classic-pix]] — existing Classic API `/authorise` Pix QR and asynchronous webhook guide for Brazil/BRL, with local-entity, expiry and amount-reconciliation conditions (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-classic-integrations-modify-payments]] — Classic integrations modification landing page for capture, cancel, refund, cancel-or-refund and authorization-adjustment routes; endpoint marked inactive for new integrations (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration]] — 2026-09-15 webpage snapshot of the inactive Classic Payment API raw-card `/authorise` integration, its PCI Level 1 or 2 condition, conditional authorization response, co-badged-card handling, and migration direction for existing integrations.


- [[source-adyen-docs-online-payments-classic-integrations]] — 2026-09-15 Adyen Docs navigation page for inactive Classic Ecommerce integrations, with new-build Checkout API and existing-integration migration routes.


- [[source-adyen-docs-online-payments-payments-india-compliance-guide]] — Adyen India local-acquiring guide for account setup, card-data limits, saved-card models, and recurring mandate and pre-debit steps (webpage snapshot, 2026-09-15; excludes cross-border payments).


- [[source-adyen-docs-online-payments-payments-india-compliance-guide-go-live-india]] — India-specific live account and endpoint checklist, following compliance and KYC steps, with real-payment testing and fee qualifications (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-analytics-and-data-tracking]] — 2026-09-15 Adyen webpage snapshot on Drop-in/Components telemetry, checkout attempt identifier, analytics version and configuration boundaries, privacy-policy counsel note, and optional separate Web fraud-data script.


- [[source-adyen-docs-online-payments-go-live-checklist]] — Adyen live-environment setup and real-payment testing checklist covering account, finance, risk, API, and webhook readiness (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-upgrade-your-integration]] — 2026-09-15 Adyen webpage upgrade hub for version policy, Drop-in/Components and Checkout API lifecycle, upgrade routes, and mobile compatibility matrices.


- [[source-adyen-docs-online-payments-upgrade-your-integration-upgrade-to-web-v6]] — Web Drop-in/Components v5-to-v6 migration guide (webpage snapshot, 2026-09-15) for Checkout API v69+, configuration, constructors, payment callbacks, and conditional method-specific upgrades.


- [[source-adyen-docs-online-payments-upgrade-your-integration-upgrade-to-web-v6-from-v4]] — v4-to-v6 Web Drop-in/Components migration guide for the Checkout API v69 minimum, import and initialization changes, event handling, and optional method or styling migrations (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-upgrade-your-integration-upgrade-to-web-v6-from-v3]] — 2026-09-15 Web Drop-in/Components v3.x.x-to-v6.0.0 migration guide covering Checkout API v69+, imports, configuration, constructors, callbacks, styling, and conditional method-specific changes.


- [[source-adyen-docs-online-payments-auto-rescue-sepa]] — 2026-09-15 SEPA Auto Rescue guide for AM04/MS03 chargeback-triggered shopper-not-present retries, two-attempt limit, and webhook, cancellation, test, and report routes; its title calls the case refused while the body starts from `AUTHORISED` then `CHARGEBACK`.


- [[source-adyen-docs-development-resources-error-codes]] — unversioned Adyen API error-code catalog for an online-payments integration, covering generic, Checkout, 3DS2, wallet, and network-token diagnostics (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-auto-rescue]] — 2026-09-15 Adyen Auto Rescue overview for retrying selected shopper-not-present card refusals and SEPA direct debit failures within a rescue window, with webhook setup required and a terminology difference in the SEPA navigation.


- [[source-adyen-docs-online-payments-donations]] — Adyen Giving online-donation guide covering campaign setup, shopper opt-in, eligible methods and currencies, and integration routes (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-online-payments-integration-checklist]] — unversioned Adyen website checklist routing test-account setup, payment lifecycle and state handling, testing, reconciliation, and approval-qualified go-live steps (webpage snapshot, 2026-09-15)

- [[source-adyen-docs-online-payments-accessibility]] — Adyen website accessibility and VPAT overview for Web Drop-in/Components, recording WCAG 2.1 test scope and Adyen's version-qualified `v5.49.0`-or-later Level AA statement (webpage snapshot, 2026-09-15)

- [[source-adyen-docs-online-payments-two-step-checkout]] — unversioned Advanced-flow Web Drop-in/Components guide for adding a pre-payment review page, retaining validated payment data server-side for up to one hour, and submitting `/payments` from the review step (webpage snapshot, 2026-09-15)

- [[source-adyen-docs-online-payments-build-your-integration-payment-result-codes]] — unversioned Adyen website guide to synchronous payment result codes, intermediate versus final state, and later webhook status (webpage snapshot, 2026-09-15)

- [[source-adyen-docs-online-payments-checkout-settings]] — Adyen Customer Area guide to per-merchant-account manual or dynamic payment-method ordering, checkout-session linkage, and analytics (webpage snapshot, 2026-09-15).

- [[source-adyen-docs-development-resources-response-handling]] — online-payments HTTP response semantics covering request processing versus payment execution, qualified retry/error handling, and diagnostic routes (webpage snapshot, 2026-09-15)

- [[source-adyen-docs-online-payments-web-best-practices]] — unversioned Web Drop-in/Components best-practices guide covering browser lifecycle, custom-button safeguards, secure hosting, embedding and testing (webpage snapshot, 2026-09-15)

- [[source-adyen-docs-online-payments-cancel]] — webpage guide for cancelling eligible authorized, uncaptured online payments through Customer Area or Checkout API, including PSP-reference versus merchant-reference routes and path-specific webhook outcomes (webpage snapshot, 2026-09-15)

- [[source-adyen-docs-online-payments-partial-authorizations]] — Adyen guide to issuer-approved partial card amounts, Advanced-flow requirements, response interpretation, and qualified follow-up routes (webpage snapshot, 2026-09-15)

- [[source-adyen-docs-online-payments-partial-payments]] — unversioned website guide to multi-method orders, rolling `orderData`, completion by final payment states plus `ORDER_CLOSED`, and cancellation paths (webpage snapshot, 2026-09-15)

- [[source-adyen-docs-online-payments-build-your-integration]] — server-side flow selection guide covering one-request Sessions, Sessions with additional methods, and three-request Advanced.

- [[source-adyen-docs-online-payments]] — Adyen website overview of online-payment use cases, integration roles, lifecycle guidance, and next-step routes (webpage snapshot, 2026-09-15)
