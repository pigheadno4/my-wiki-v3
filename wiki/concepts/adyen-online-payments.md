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
