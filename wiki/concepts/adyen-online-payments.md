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

- [[source-adyen-docs-payment-methods-payme-web]] — 2019-modified, 2026-09-15-captured PayMe Web chooser linking Drop-in and Components child guides plus general Web docs; implementation and outcomes require child evidence.


- [[source-adyen-docs-payment-methods-payme-ios]] — 2019-modified, 2026-09-15-captured PayMe iOS chooser for Drop-in and Components child guides; versions, behavior and outcomes require child evidence.


- [[source-adyen-docs-payment-methods-payme-android]] — 2019-modified, 2026-09-15-captured PayMe Android chooser for Drop-in and Components child guides; versions, behavior and outcomes require child evidence.


- [[source-adyen-docs-payment-methods-alipay-plus-web]] — 2026-09-15 Alipay+ Web chooser linking Drop-in and redirect Components child guides plus Sessions/Advanced main Web guides; child requirements and payment outcomes remain separate evidence.


- [[source-adyen-docs-payment-methods-alipay-plus-android]] — 2026-09-15 Alipay+ Android chooser linking Drop-in, InstantPaymentComponent and Sessions/Advanced main guides; implementation and outcomes remain in child sources.


- [[source-adyen-docs-payment-methods-alipay-plus-ios]] — 2026-09-15 Alipay+ iOS chooser for Drop-in or `InstantPaymentComponent` child guides and the four Sessions/Advanced base routes; implementation and outcomes require linked guides.


- [[source-adyen-docs-payment-methods-online-banking-thailand-web]] — 2026-09-15 Thailand online-banking Web chooser for Drop-in or MolPayEBankingTH Components and four Sessions/Advanced base routes; implementation and outcomes require child evidence.


- [[source-adyen-docs-payment-methods-online-banking-thailand-android]] — 2026-09-15 Online Banking Thailand Android chooser linking Drop-in and `MolpayComponent` child guides plus four Sessions/Advanced base routes; child requirements and outcomes remain separate authority.


- [[source-adyen-docs-payment-methods-online-banking-thailand-ios]] — 2026-09-15 Thailand online-banking iOS chooser for Drop-in or InstantPaymentComponent and four Sessions/Advanced base guides; child implementation and outcomes are separate evidence.


- [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-web]] — 2026-09-15 FPX Malaysia Web chooser linking Drop-in/`MolPayEBankingMY` Components child guides and four Web Sessions/Advanced base routes; implementation and outcomes require child/base evidence.


- [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-android]] — 2026-09-15 FPX Online Banking Malaysia Android chooser linking Drop-in and InstantPaymentComponent children plus main Sessions/Advanced routes; child guides carry implementation requirements.


- [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-ios]] — 2026-09-15 FPX Malaysia iOS chooser linking Drop-in and Components child guides plus Sessions/Advanced main guides; child implementation and outcome details require child evidence.


- [[source-adyen-docs-payment-methods-online-banking-thailand-react-native-component]] — 2026-09-15 Thailand online-banking React Native Components Advanced redirect add-on; Sessions unsupported, separate live request, and a Components-label/Drop-in-link mismatch.


- [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-react-native-component]] — 2026-09-15 FPX React Native Components Advanced-only redirect add-on; Sessions unsupported, no method-specific fields/configuration stated, and the prerequisite Components label links to Drop-in.


- [[source-adyen-docs-payment-methods-online-banking-thailand-ios-drop-in]] — 2026-09-15 Thailand online-banking iOS Drop-in Sessions (Checkout API v68+) and Advanced redirect add-on, with no extra method fields/configuration and a separate live request.


- [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-ios-drop-in]] — 2026-09-15 FPX Malaysia iOS Drop-in Sessions (Checkout API v68+) and Advanced redirect add-on, with Component-linked issuer TEST guidance and a separate live request gate; no outcome proof.


- [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-android-drop-in]] — 2026-09-15 FPX Malaysia Android Drop-in add-on for existing Sessions (Checkout API v68+) and Advanced redirect flows, with method-specific no-extra-field guidance, test issuer reference, and separate live request.


- [[source-adyen-docs-payment-methods-online-banking-thailand-react-native-drop-in]] — 2026-09-15 Thailand online-banking React Native Drop-in Sessions/Advanced redirect add-on, with Sessions v68+, no extra method parameters and a misrouted Sessions prerequisite link.


- [[source-adyen-docs-payment-methods-online-banking-thailand-flutter-drop-in]] — 2026-09-15 Thailand online-banking Flutter Drop-in Sessions (Checkout API v68+) and Advanced redirect add-on; Sessions base-link and setup wording differ from Advanced and remain source-qualified.


- [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-react-native-drop-in]] — 2026-09-15 FPX Malaysia React Native Drop-in Sessions (Checkout API v68+) and Advanced redirect add-on with no extra method fields/configuration, test/live gates and a Sessions-to-Advanced prerequisite-link mismatch.


- [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-flutter-drop-in]] — 2026-09-15 FPX Malaysia Flutter Drop-in Sessions (Checkout API v68+) and Advanced redirect add-on, with differing setup routes and a separate live request; Sessions link targets Advanced flow.


- [[source-adyen-docs-payment-methods-alipay-plus-android-drop-in]] — 2026-09-15 Alipay+ Android Drop-in Sessions (Checkout API v68+) and Advanced redirect add-on, with optional submit-button configuration, no test environment, and unresolved Alipay-versus-Alipay+ live-request label.


- [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-web-drop-in]] — 2026-09-15 FPX Malaysia Web Drop-in Sessions/Advanced redirect add-on with optional `MolPayEBankingMY` import, test/live gates and a templated Advanced prerequisite link.


- [[source-adyen-docs-payment-methods-online-banking-thailand-android-drop-in]] — 2026-09-15 Thailand online-banking Android Drop-in Sessions (Checkout API v68+) and Advanced redirect add-on, with no method-specific request fields and a separate live request.


- [[source-adyen-docs-payment-methods-alipay-plus-ios-component]] — 2026-09-15 Alipay+ iOS InstantPaymentComponent Sessions (Checkout API v68+) and Advanced redirect add-on; no TEST environment, and Advanced base-link plus Alipay/Alipay+ live-request naming conflicts remain source-qualified.


- [[source-adyen-docs-payment-methods-payme-ios-drop-in]] — 2026-09-15 PayMe iOS Drop-in v4.0.0+ Sessions/Advanced add-on with v5 `/sessions` default, field-specific v70 SKU condition, sandbox outcome fixtures and a JavaScript example mislabeled Swift.


- [[source-adyen-docs-payment-methods-online-banking-thailand-ios-component]] — 2026-09-15 Thailand online-banking iOS Components Sessions (Checkout API v68+) and Advanced add-on with redirect, `InstantPaymentComponent` and separate live request; Advanced base-link label/target conflict retained in source.


- [[source-adyen-docs-payment-methods-payme-android-component]] — 2026-09-15 PayMe Android Redirect Component v4.0.0+ guide for HK/HKD discovery, redirect return and `/payments/details`, with return-URL casing and sample-language conflicts plus sandbox outcome fixtures.


- [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-ios-component]] — 2026-09-15 FPX Malaysia iOS InstantPaymentComponent add-on for Sessions (Checkout API v68+) and Advanced redirect flows, with separate live request gate; Advanced Components label links to Drop-in.


- [[source-adyen-docs-payment-methods-alipay-plus-web-drop-in]] — 2026-09-15 Alipay+ Web Drop-in Sessions (Checkout API v68+) and Advanced redirect add-on, with no stated test environment, live-request wording for “Alipay,” and a conflicting TEST-endpoint example.


- [[source-adyen-docs-payment-methods-alipay-plus-web-component]] — 2026-09-15 Alipay+ Web redirect Component add-on for existing Sessions (Checkout API v68+) and Advanced flows, with conditional browser info, live request wording, and unreconciled no-test-environment versus test-endpoint example.


- [[source-adyen-docs-payment-methods-payme-android-drop-in]] — 2026-09-15 Android Drop-in PayMe app-redirect guide (4.0.0+), with Advanced-flow prerequisites, redirect handoff and sandbox expiry mappings; examples conflict on channel and return-URL casing.


- [[source-adyen-docs-payment-methods-online-banking-thailand-web-drop-in]] — 2026-09-15 Web Drop-in Sessions/Advanced redirect add-on, with Sessions issuer configuration, optional import, test/live gates and a templated Advanced prerequisite link.


- [[source-adyen-docs-payment-methods-payme-ios-component]] — 2026-09-15 PayMe iOS Components v4+ add-on for Sessions/Advanced flows, with version-specific InstantPaymentComponent examples and sandbox outcome simulation.


- [[source-adyen-docs-payment-methods-online-banking-thailand-web-component]] — 2026-09-15 Thailand online-banking Web Components Sessions/Advanced redirect add-on using `MolPayEBankingTH`, with optional issuer UI configuration, Sessions Checkout API v68+ and separate live request.


- [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-web-component]] — 2026-09-15 FPX Malaysia Web Components add-on for Sessions (Checkout API v68+) and Advanced, with redirect, issuer configuration and separate test/live-request instructions.


- [[source-adyen-docs-payment-methods-payme-web-drop-in]] — 2026-09-15 PayMe Web Drop-in 5.56.0+ add-on for desktop QR/mobile app routing, Sessions/Advanced paths and sandbox outcome fixtures, with conflicting mobile example `channel` values.


- [[source-adyen-docs-payment-methods-payme-web-component]] — 2019-modified PayMe Web Components guide for desktop QR/mobile app redirect, 5.56.0+ support, versioned construction and sandbox expiry/result mappings; mobile channel examples disagree and live outcome is not shown.


- [[source-adyen-docs-payment-methods-alipay-plus-api-only]] — 2026-09-15 Alipay+ Advanced API-only aggregator/redirect guide: generic request versus wallet-specific details/webhook, channel-dependent entry, unsupported tokenization and no TEST environment; details-caller and examples conflict in source.


- [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-android-component]] — 2026-09-15 FPX Malaysia Android InstantPaymentComponent Sessions (Checkout API v68+) and Advanced redirect add-on, with test issuer IDs and separate live-request gate; outcome details remain base-flow authority.


- [[source-adyen-docs-payment-methods-alipay-plus-android-component]] — 2026-09-15 Alipay+ Android `InstantPaymentComponent` add-on for Sessions v68+ or Advanced redirect flows, with Compose/non-Compose setup, no test environment and an unresolved Alipay-versus-Alipay+ live-request label.


- [[source-adyen-docs-payment-methods-payme-api-only]] — 2019-modified, 2026-09-15-captured HK/HKD PayMe API-only desktop QR and mobile app-redirect guide (Checkout API v67+), with webhook-final authorization, sandbox expiry and sample request differences qualified.


- [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-api-only]] — 2026-09-15 FPX Malaysia Web API-only MY/MYR issuer-list and redirect guide; issuer/no-extra-parameter and PHP type/example conflicts remain qualified in source.


- [[source-adyen-docs-payment-methods-online-banking-thailand-api-only]] — 2026-09-15 Thailand online-banking Web API-only Advanced guide for TH/THB issuer selection, redirect/details handling and webhook-qualified pending results, with request prose/example conflicts.


- [[source-adyen-docs-payment-methods-payme]] — 2026-09-15 PayMe overview with Hong Kong entity and HK/HKD scope, QR/app handoff, capability matrix and Web/native/API-only guide routes; execution details require the linked guides.


- [[source-adyen-docs-payment-methods-alipay-plus]] — 2026-09-15 Alipay+ cross-border 11-wallet redirect-network overview with dated capability marks, wallet-specific onboarding review and a TrueMoney Support-form exception; no merchant or wallet-level enablement proof.


- [[source-adyen-docs-payment-methods-online-banking-thailand]] — 2026-09-15 RMS/MOLPay-partnered TH/THB online-banking redirect overview with asynchronous webhook-final result, historical negative capability marks and Web/native/API-only/Pay by Link routes.


- [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia]] — FPX Online Banking Malaysia overview (webpage, 2026-10-25): MY/MYR redirect, asynchronous webhook result and historical capability matrix.


- [[source-adyen-docs-payment-methods-napas-card-web]] — 2026-09-15 Napas card Web chooser for Drop-in and Components child guides plus general Web docs; version, payment flow, eligibility and outcomes require child evidence.


- [[source-adyen-docs-payment-methods-napas-card-ios]] — 2020-modified, 2026-09-15-captured Napas card iOS chooser linking Drop-in/Redirect Component child guides and general Sessions-flow guides; child versions, card/gateway handling and outcomes require separate evidence.


- [[source-adyen-docs-payment-methods-napas-card-android]] — 2026-09-15 Napas card Android chooser linking Drop-in, Redirect Component and general Sessions-flow guides; child implementation and outcomes require separate evidence.


- [[source-adyen-docs-payment-methods-payco-web]] — 2026-09-15 PAYCO Web chooser for Drop-in/`Redirect` Components child guides and Web Sessions/Advanced base routes; setup, eligibility and payment outcomes require child evidence.


- [[source-adyen-docs-payment-methods-payco-android]] — 2026-09-15 PayCo Android chooser linking Drop-in and InstantPaymentComponent children plus main Sessions/Advanced guides; implementation requirements remain child-guide evidence.


- [[source-adyen-docs-payment-methods-payco-ios]] — 2026-09-15 PayCo iOS chooser linking Drop-in and InstantPaymentComponent child guides plus Sessions/Advanced base routes; child setup, eligibility and outcomes require separate evidence.


- [[source-adyen-docs-payment-methods-rakutenpay-web]] — 2026-09-15 Rakuten Pay Web chooser linking Drop-in/Redirect Components child guides and four Sessions/Advanced main integration routes; child prerequisites and outcomes remain separate evidence.


- [[source-adyen-docs-payment-methods-rakutenpay-android]] — 2026-09-15 Rakuten Pay Android chooser for Drop-in or InstantPaymentComponent plus four main Sessions/Advanced integration routes; implementation and outcomes belong to child/base guides.


- [[source-adyen-docs-payment-methods-rakutenpay-ios]] — 2026-09-15 Rakuten Pay iOS chooser for Drop-in/`InstantPaymentComponent` child guides and four iOS Sessions/Advanced base routes; child setup, recurring eligibility and outcomes require separate authority.


- [[source-adyen-docs-payment-methods-bank-transfer-kcp-web]] — 2026-09-15 Bank Transfer via KCP Web chooser linking Drop-in and Redirect Components children plus main Web Sessions/Advanced guides; implementation requirements remain child-guide evidence.


- [[source-adyen-docs-payment-methods-bank-transfer-kcp-android]] — 2026-09-15 KCP bank-transfer Android chooser linking Drop-in and InstantPaymentComponent children plus four Sessions/Advanced base-guide routes; child requirements and outcomes remain separate evidence.


- [[source-adyen-docs-payment-methods-bank-transfer-kcp-ios]] — 2026-09-15 KCP bank-transfer iOS chooser linking Drop-in/InstantPaymentComponent child guides and four Sessions/Advanced main integration routes; child requirements and outcomes remain separate evidence.


- [[source-adyen-docs-payment-methods-napas-card-web-drop-in]] — 2026-09-15 Napas card Web Drop-in add-on with no extra method fields/configuration, four TEST scenario fixtures and a separate live Customer Area request.


- [[source-adyen-docs-payment-methods-napas-card-ios-drop-in]] — 2026-09-15 Napas card iOS Drop-in add-on with test Customer Area prerequisite, no extra method fields/configuration, Drop-in v5.0.0 `/sessions` default and separate live request; See-also link points to Components.


- [[source-adyen-docs-payment-methods-payco-ios-drop-in]] — 2026-09-15 PayCo iOS Drop-in Sessions (Checkout API v68+) and Advanced add-on, with redirect handling specified in Advanced requirements and Support-assisted testing guidance.


- [[source-adyen-docs-payment-methods-payco-android-drop-in]] — 2026-09-15 PayCo Android Drop-in Sessions (Checkout API v68+) and Advanced redirect add-on with no extra method fields/configuration and Support-assisted testing; no final outcome or live-enable procedure.


- [[source-adyen-docs-payment-methods-bank-transfer-kcp-ios-drop-in]] — 2026-09-15 KCP bank-transfer iOS Drop-in Sessions (Checkout API v68+) and Advanced redirect add-on with no method-specific request/configuration fields and no KCP testing credentials due to PIC authorization.


- [[source-adyen-docs-payment-methods-bank-transfer-kcp-android-drop-in]] — 2026-09-15 KCP bank-transfer Android Drop-in Sessions/Advanced add-on, with Sessions Checkout API v68+ and Advanced redirect prerequisites, no extra method parameters and no KCP test credentials.


- [[source-adyen-docs-payment-methods-rakutenpay-react-native-component]] — 2026-09-15 Rakuten Pay React Native Components guide explicitly excluding Sessions and covering Advanced redirect only, with review/application-gated recurring models and DGFT TEST simulator; the Advanced Components prerequisite URL points to Drop-in.


- [[source-adyen-docs-payment-methods-payco-web-drop-in]] — 2026-09-15 PayCo Web Drop-in Sessions (Checkout API v68+) and Advanced redirect add-on, with optional `Redirect` tree-shaking import, Support-assisted testing and an unresolved Advanced prerequisite URL template.


- [[source-adyen-docs-payment-methods-napas-card-android-drop-in]] — 2026-09-15 Napas card Android Drop-in v5.0.0 Sessions/Advanced add-on with no extra method fields/configuration, four TEST scenarios and live Customer Area request; no action or final-outcome procedure.


- [[source-adyen-docs-payment-methods-napas-card-android-component]] — 2026-09-15 Napas card Android Components v5.0.0 Sessions/Advanced add-on with no extra method fields/configuration, four TEST card scenarios and live Customer Area request; final redirect/authorization handling is outside this page.


- [[source-adyen-docs-payment-methods-napas-card-web-component]] — 2019-modified, 2026-09-15-captured Napas card Web Components add-on for Sessions/Advanced bases, versioned `momo_atm` Redirect/create snippets, TEST fixtures and separate live request; Napas title versus method identifier stays qualified in source.


- [[source-adyen-docs-payment-methods-payco-web-component]] — 2026-09-15 PayCo Web Components Sessions (Checkout API v68+) and Advanced redirect add-on using `Redirect`, with an unquoted `kcp_payco` sample and Support-assisted testing guidance.


- [[source-adyen-docs-payment-methods-bank-transfer-kcp-web-drop-in]] — 2026-09-15 KCP bank-transfer Web Drop-in Sessions (Checkout API v68+) and Advanced redirect add-on with optional `Redirect` import, no testing credentials due to certificate-based authorization and malformed Advanced platform URL.


- [[source-adyen-docs-payment-methods-napas-card-ios-component]] — 2026-09-15 Napas card iOS Components add-on with v5+ `InstantPaymentComponent` examples using `momo_atm`, generic v4 example, test scenarios and live Customer Area request; identifier scope and final outcomes remain source-qualified.


- [[source-adyen-docs-payment-methods-payco-ios-component]] — 2026-09-15 PAYCO iOS InstantPaymentComponent Sessions (Checkout API v68+) and Advanced redirect add-on, with no specific test credentials and a qualified Advanced Components/Drop-in prerequisite-link mismatch.


- [[source-adyen-docs-payment-methods-bank-transfer-kcp-web-component]] — 2026-09-15 KCP bank-transfer Web Components Sessions/Advanced redirect add-on, with Sessions Checkout API v68+ requirement, an illustrative unquoted-type snippet and no KCP test credentials.


- [[source-adyen-docs-payment-methods-rakutenpay-api-only]] — 2026-09-15 Rakuten Pay JP/JPY API-only redirect guide with conditional recurring-model approval and DGFT TEST simulator; purchased-item versus no-extra-field prose and mislabeled `/paymentMethods` sample require source-qualified review.


- [[source-adyen-docs-payment-methods-bank-transfer-kcp-ios-component]] — 2026-09-15 Bank Transfer via KCP iOS Components Sessions (Checkout API v68+) and Advanced redirect add-on using InstantPaymentComponent/`kcp_banktransfer`, with no KCP bank-transfer testing credentials; Advanced prerequisite link points to Drop-in.


- [[source-adyen-docs-payment-methods-rakutenpay-ios-drop-in]] — 2026-09-15 Rakuten Pay iOS Drop-in Sessions (Checkout API v68+) and Advanced redirect add-on with review/cadence-qualified card-on-file use, per-model application and DGFT TEST simulator.


- [[source-adyen-docs-payment-methods-rakutenpay-flutter-component]] — 2026-09-15 Rakuten Pay Flutter Components Sessions (Checkout API v68+) and Advanced redirect add-on with review/cadence-qualified recurring models and DGFT TEST simulator; both prerequisite links misroute to Flutter Drop-in.


- [[source-adyen-docs-payment-methods-rakutenpay-react-native-drop-in]] — 2026-09-15 Rakuten Pay React Native Drop-in Sessions/Advanced redirect guide with Sessions v68+, qualified recurring-model review/application restrictions, TEST DGFT simulator and Sessions/Advanced link mismatch.


- [[source-adyen-docs-payment-methods-rakutenpay-flutter-drop-in]] — 2026-09-15 Rakuten Pay Flutter Drop-in Sessions (Checkout API v68+) and Advanced redirect add-on with review-gated recurring model claims and DGFT TEST simulator; Sessions prerequisite link points to Advanced.


- [[source-adyen-docs-payment-methods-rakutenpay-web-drop-in]] — 2026-09-15 Rakuten Pay Web Drop-in Sessions (Checkout API v68+) and Advanced redirect add-on, with review/application-gated card-on-file models and DGFT TEST simulator; Advanced prerequisite URL has unresolved template text.


- [[source-adyen-docs-payment-methods-rakutenpay-android-drop-in]] — 2026-09-15 Rakuten Pay Android Drop-in Sessions/Advanced add-on, with flow-specific prerequisites, conditional card-on-file use and a DGFT TEST simulator path.


- [[source-adyen-docs-payment-methods-rakutenpay-web-component]] — 2026-09-15 Rakuten Pay Web Redirect Component add-on for Sessions (Checkout API v68+) and Advanced flows, with per-model recurring review/application restrictions and DGFT TEST simulator; unresolved unquoted `rakutenpay` sample remains qualified in source.


- [[source-adyen-docs-payment-methods-rakutenpay-ios-component]] — 2026-09-15 Rakuten Pay iOS Components Sessions (Checkout API v68+) and Advanced redirect add-on, with review/cadence-qualified card-on-file models and DGFT TEST simulator; Advanced prerequisite URL points to Drop-in.


- [[source-adyen-docs-payment-methods-payco-android-component]] — 2026-09-15 PayCo Android InstantPaymentComponent Sessions (Checkout API v68+) and Advanced redirect guide using `kcp_payco`, Compose/non-Compose examples and Support-assisted testing; no final outcome procedure.


- [[source-adyen-docs-payment-methods-bank-transfer-kcp-android-component]] — 2026-09-15 KCP bank-transfer Android Components Sessions (Checkout API v68+) and Advanced redirect add-on using InstantPaymentComponent/`kcp_banktransfer`, with no method-specific request fields and no KCP testing credentials due to PIC authorization.


- [[source-adyen-docs-payment-methods-rakutenpay-android-component]] — 2026-09-15 Rakuten Pay Android Components Sessions (Checkout API v68+) and Advanced redirect add-on, with review-gated recurring conditions and DGFT TEST simulator scope.


- [[source-adyen-docs-payment-methods-napas-card-android-drop-in-earlier-versions]] — 2026-09-15 snapshot of Napas card Android Drop-in v4.x.x Advanced guide for VN/VND discovery, redirect, details and webhook-qualified results; `momo_atm` samples and Sessions links conflict with its Napas/Advanced prose.


- [[source-adyen-docs-payment-methods-napas-card-api-only]] — 2019-modified, 2026-09-15-captured VN/VND NAPAS card API-only redirect guide with `/payments/details` and webhook outcome; its NAPAS title versus `momo_atm` method identifier conflict remains unresolved.


- [[source-adyen-docs-payment-methods-payco-api-only]] — 2026-09-15 PAYCO Web API-only Advanced guide for KR/KRW discovery, `kcp_payco` redirect payments and TEST setup; purchased-item prose versus no-extra-field examples remains qualified.


- [[source-adyen-docs-payment-methods-bank-transfer-kcp-api-only]] — 2026-09-15 Bank Transfer via KCP Web API-only add-on for KR/KRW method discovery and redirect handling, with an on-page item-parameter conflict and no KCP bank-transfer test credentials.


- [[source-adyen-docs-payment-methods-napas-card]] — 2023-modified, 2026-09-15-captured Vietnam Napas card overview via partner MoMo, with bank/gateway/PIN/OTP redirect journey, VN/VND capability row and channel links; refund “See note” is unresolved in the captured page.


- [[source-adyen-docs-payment-methods-bank-transfer-kcp]] — 2026-09-15 Bank Transfer via KCP KR/KRW Online Banking redirect overview with dated Korean merchant assurance claim, local-bank responsibility, capability marks and Web/native/API-only routes; no compliance or payment-outcome proof.


- [[source-adyen-docs-payment-methods-payco]] — 2026-09-15 PayCo overview: KCP-provided, card-linked KR/KRW redirect-wallet route, historical refund/capture/recurring capability marks and Web/native/API-only child links; no setup or outcome proof.


- [[source-adyen-docs-payment-methods-rakutenpay]] — 2026-09-15 Rakuten Pay JP/JPY redirect-wallet overview for Ecommerce/IPP and channel routes; positive capability marks repeatedly say “See note” without an explanatory note in the pinned page, so their conditions remain unresolved.


- [[source-adyen-docs-payment-methods-paynow-android]] — 2026-09-15 PayNow Android navigation chooser linking Drop-in and InstantPaymentComponent children plus main Sessions/Advanced guides; its “redirect” label is not an API action-type or payment-outcome specification.


- [[source-adyen-docs-payment-methods-grabpay-web]] — 2019-modified, 2026-09-15-captured GrabPay Web chooser for Drop-in and Components child guides plus general Web docs; flow requirements and outcomes belong to child evidence.


- [[source-adyen-docs-payment-methods-grabpay-ios]] — 2019-modified, 2026-09-15-captured GrabPay iOS chooser linking Drop-in/Components child guides and general iOS Sessions-flow guides; child versions, PayLater conditions and outcomes remain separate evidence.


- [[source-adyen-docs-payment-methods-touchngo-web]] — 2019-modified, 2026-09-15-captured Touch'n Go Web chooser for Drop-in or Components and general Web guides; implementation and outcome claims require child evidence.


- [[source-adyen-docs-payment-methods-grabpay-android]] — 2019-modified, 2026-09-15-captured Android GrabPay chooser linking Drop-in and Components child guides plus Sessions base guides; child prerequisites and outcomes are separate authority.


- [[source-adyen-docs-payment-methods-touchngo-ios]] — 2019-modified, 2026-09-15-captured Touch'n Go iOS chooser for Drop-in/Components child guides and Sessions-flow base links; implementation and outcomes remain child-guide authority.


- [[source-adyen-docs-payment-methods-paynow-web]] — 2026-09-15 PayNow Web chooser for Drop-in/Components child guides and Web Sessions/Advanced base routes; the page gives navigation, not QR implementation, eligibility or outcome semantics.


- [[source-adyen-docs-payment-methods-touchngo-android]] — 2019-modified, 2026-09-15-captured Touch'n Go Android chooser linking Drop-in/Components child guides and Sessions base routes; navigation only, with implementation and outcomes in the linked guides.


- [[source-adyen-docs-payment-methods-paynow-ios]] — 2026-09-15 PayNow iOS navigation chooser linking Drop-in, InstantPaymentComponent and four Sessions/Advanced base guides; child setup, QR behavior and outcomes require their own evidence.


- [[source-adyen-docs-payment-methods-boost-web]] — 2026-09-15 Boost Wallet Web chooser linking Drop-in/Components child guides and Web Sessions/Advanced main integrations; child prerequisites, redirect mechanics, TEST/live limits and outcomes remain separate evidence.


- [[source-adyen-docs-payment-methods-boost-android]] — 2026-09-15 Boost Wallet Android chooser for Drop-in or InstantPaymentComponent and their Sessions/Advanced base guides; child pages carry implementation and outcome limits.


- [[source-adyen-docs-payment-methods-touchngo-web-drop-in]] — 2026-09-15 Touch'n Go Web Drop-in Sessions/Advanced add-on with Support-gated setup, no extra method-specific API/configuration fields and separate live Support request; `/sessions` v5+ wording is a default, not a method minimum.


- [[source-adyen-docs-payment-methods-boost-ios]] — 2026-09-15 Boost Wallet iOS navigation chooser for Drop-in or InstantPaymentComponent child guides and Sessions/Advanced base guides; implementation and outcomes are separate authority.


- [[source-adyen-docs-payment-methods-touchngo-ios-drop-in]] — 2026-09-15 Touch'n Go iOS Drop-in add-on for Sessions/Advanced base integrations with Support setup, no extra method fields or version-tab configuration and a separate live Support gate; v5.0.0 is Drop-in, not Checkout API, and outcomes require other evidence.


- [[source-adyen-docs-payment-methods-touchngo-android-drop-in]] — 2026-09-15-captured Touch 'n Go Android Drop-in v5.0.0+ Sessions/Advanced add-on with no extra method-specific base fields/configuration and a live Support gate; redirect/result behavior remains separate evidence.


- [[source-adyen-docs-payment-methods-paynow-react-native-component]] — 2026-09-15 PayNow React Native Components guide: Sessions unsupported, Advanced `qrCode` action with no extra method fields/configuration, Components/Drop-in link mismatch and real-funds test warning.


- [[source-adyen-docs-payment-methods-touchngo-android-component]] — 2026-09-15 Touch'n Go Android Components v5.0.0 Sessions/Advanced add-on with Customer Area setup, no additional method fields/configuration and live Support gate; app-return and final outcomes remain outside this guide.


- [[source-adyen-docs-payment-methods-touchngo-web-component]] — 2019-modified, 2026-09-15-captured Touch 'n Go Web Components Sessions/Advanced add-on with v6 Redirect versus v5 create snippets, Support-gated live setup and no on-page webhook-outcome procedure.


- [[source-adyen-docs-payment-methods-grabpay-android-drop-in]] — 2026-09-15 GrabPay Android Drop-in v5.0.0 Sessions/Advanced add-on with no method-specific fields/configuration, test credential steps and live-request gate; Wallet/PayLater and final outcomes are not detailed.


- [[source-adyen-docs-payment-methods-grabpay-android-component]] — 2026-09-15 GrabPay Android Components v5.0.0 Sessions/Advanced add-on with Customer Area setup, no additional method fields/configuration stated, simulator testing and live request gate; its broad no-fields wording leaves PayLater scope unresolved against other GrabPay guides.


- [[source-adyen-docs-payment-methods-boost-ios-drop-in]] — 2026-09-15 Boost Wallet iOS Drop-in add-on for Sessions (Checkout API v68+) and Advanced redirect flows, with no method-specific extra fields and a no-TEST/live-penny-test warning; no final outcome procedure on this page.


- [[source-adyen-docs-payment-methods-boost-android-drop-in]] — 2026-09-15 Boost Wallet Android Drop-in Sessions (Checkout API v68+) and Advanced redirect add-on; no Boost TEST environment, with live penny-test guidance only and no payment-outcome proof.


- [[source-adyen-docs-payment-methods-boost-web-drop-in]] — 2026-09-15 Boost Wallet Web Drop-in Sessions/Advanced redirect add-on with Sessions Checkout v68+, optional `Redirect` import, malformed Advanced base-guide platform link and explicit no-TEST limit; no outcome proof.


- [[source-adyen-docs-payment-methods-touchngo-ios-component]] — 2026-09-15 Touch'n Go iOS Components Sessions/Advanced add-on with Support setup, no extra method fields, v5+ InstantPaymentComponent versus v4.x.x TouchnGoComponent examples and live Support gate; setup is not payment-result proof.


- [[source-adyen-docs-payment-methods-boost-web-component]] — 2026-09-15 Boost Wallet Web Components Sessions (Checkout API v68+) and Advanced redirect add-on; source examples have malformed placeholders, and the guide states no TEST environment.


- [[source-adyen-docs-payment-methods-paynow-ios-drop-in]] — 2026-09-15 PayNow iOS Drop-in Sessions (Checkout API v68+) and Advanced QR-action add-on, with Support-assisted live setup and real-funds/nonreversible TEST transfer warning.


- [[source-adyen-docs-payment-methods-paynow-android-drop-in]] — 2026-09-15 PayNow Android Drop-in Sessions (Checkout API v68+) and Advanced `qrCode` add-on, with Support-gated live setup and explicit real-funds/nonreversible TEST transfer warning.


- [[source-adyen-docs-payment-methods-paynow-react-native-drop-in]] — 2026-09-15 PayNow React Native Drop-in add-on for Sessions (Checkout API v68+) and Advanced (`qrCode` action), with live Support setup and nonreversible real-funds TEST warning; Sessions base URL and Advanced action anchor are qualified in source.


- [[source-adyen-docs-payment-methods-paynow-flutter-drop-in]] — 2026-09-15 PayNow Flutter Drop-in Sessions (Checkout API v68+) and Advanced (qrCode action) add-on, with live Support setup, Sessions guide-link conflict and explicit real-funds/nonreversible TEST warning.


- [[source-adyen-docs-payment-methods-boost-ios-component]] — 2026-09-15 Boost Wallet iOS InstantPaymentComponent Sessions/Advanced redirect guide, with Sessions Checkout v68+ prerequisite, an Advanced Components/Drop-in link mismatch and explicit no-TEST limit; no observed outcome.


- [[source-adyen-docs-payment-methods-paynow-web-drop-in]] — 2026-09-15 PayNow Web Drop-in Sessions (Checkout API v68+) and Advanced QR-action add-on with no extra method request fields, live Support gate and nonreversible test-transfer warning; Advanced prerequisite URL retains an encoded platform template.


- [[source-adyen-docs-payment-methods-paynow-ios-component]] — 2026-09-15 PayNow iOS Components Sessions (Checkout API v68+) and Advanced QR-action add-on, with live bank-app testing/reversibility warning and Advanced prerequisite-link mismatch.


- [[source-adyen-docs-payment-methods-paynow-web-component]] — 2026-09-15 PayNow Web Components Sessions/Advanced QR guide with v68+ Sessions prerequisite, flow-specific configuration, live Support enablement and consequential test bank-transfer warning; no observed outcome.


- [[source-adyen-docs-payment-methods-boost-android-component]] — 2026-09-15 Boost Wallet Android Components Sessions (Checkout API v68+) and Advanced redirect add-on using `InstantPaymentComponent`/`molpay_boost`; no TEST environment, with live penny-test guidance only.


- [[source-adyen-docs-payment-methods-paynow-android-component]] — 2026-09-15 PayNow Android `InstantPaymentComponent` add-on for Sessions (Checkout API v68+) and Advanced (`qrCode` action), with separate live Support setup and an explicit real-funds/nonreversible TEST warning; no QR outcome procedure on this page.


- [[source-adyen-docs-payment-methods-touchngo-android-component-earlier-versions]] — 2019-modified Touch 'n Go Android earlier-version Redirect Component guide for Advanced request/return-details flow, with Sessions-link conflict, blank discovery channel and v68/v72 example split qualified in source.


- [[source-adyen-docs-payment-methods-touchngo-android-drop-in-earlier-versions]] — 2026-09-15-captured earlier-version Android Drop-in Advanced-flow Touch'n Go guide for MY/MYR display, server payment/redirect/details handoff and test/live Support gates; Sessions links and return-URL casing differ from requirement prose/examples.


- [[source-adyen-docs-payment-methods-boost-api-only]] — 2026-09-15 Boost Wallet MY/MYR Advanced Web API-only add-on for method discovery and redirect; payment-request item-data and TEST/LIVE examples conflict with prose, with no observed final outcome.


- [[source-adyen-docs-payment-methods-grabpay-web-component]] — 2026-09-15 snapshot of GrabPay Web Components Sessions/Advanced guide for PayLater-only additional fields, MY/PH/SG method variants and v5/v6 mounting.


- [[source-adyen-docs-payment-methods-touchngo-api-only]] — 2019-modified, 2026-09-15-captured MY/MYR Touch'n Go API-only redirect guide with Support-gated setup, return `/payments/details`, pending/webhook outcome branches and separate TEST/live requirements; sample v68/v72 endpoints are not a stated minimum.


- [[source-adyen-docs-payment-methods-grabpay-ios-drop-in]] — 2026-09-15 GrabPay iOS Drop-in Sessions/Advanced add-on for Customer Area setup, PayLater delivery/item request data, no extra Drop-in-specific configuration and TEST/live gates; Web-version wording within the iOS guide remains source-qualified.


- [[source-adyen-docs-payment-methods-grabpay-web-drop-in]] — 2026-09-15 GrabPay Web Drop-in Sessions/Advanced guide distinguishing required PayLater address/items from recommended Wallet data, with v5+ `/sessions` versus conditional `/payments` routes and a live-request gate; examples have an unexplained amount/item mismatch.


- [[source-adyen-docs-payment-methods-boost]] — 2026-09-15 Boost Wallet overview: Adyen's RMS-mediated MY/MYR redirect-wallet route, refund-only positive capability mark and Web/iOS/Android/API-only navigation; matrix does not prove merchant enablement or outcome.


- [[source-adyen-docs-payment-methods-grabpay-ios-component]] — 2026-09-15 GrabPay iOS Components Sessions/Advanced guide with required PayLater address/items, v5/v4 native Component routes and qualified Web-version/example inconsistencies.


- [[source-adyen-docs-payment-methods-grabpay-android-drop-in-earlier-versions]] — 2026-09-15 earlier-version GrabPay Android Advanced Drop-in Wallet/PayLater guide for MY/SG/PH, with PH PayLater exclusion, PayLater-only extra fields and webhook-final pending states; Sessions navigation and return-URL examples are qualified.


- [[source-adyen-docs-payment-methods-grabpay-android-component-earlier-versions]] — 2019-modified, 2026-09-15-captured GrabPay Android Components v4.x.x Advanced guide for MY/SG/PH Wallet and qualified PayLater, redirect/details and asynchronous webhook outcomes; Sessions-link/API-example differences remain source-qualified.


- [[source-adyen-docs-payment-methods-grabpay-api-only]] — 2019-modified, 2026-09-15-captured GrabPay Web API-only Wallet/PayLater guide for MY/SG/PH method mapping, PH PayLater exclusion, redirect/details flow and webhook-qualified outcomes; TEST/live gates and mixed API examples remain source-qualified.


- [[source-adyen-docs-payment-methods-paynow]] — 2026-09-15 PayNow SG/SGD overview limiting Adyen integration to QR-code payments, with a historical capability row and Web/iOS/Android/React Native/Flutter child routes; QR lifecycle and outcomes require child evidence.


- [[source-adyen-docs-payment-methods-touchngo]] — 2022-modified, 2026-09-15-captured Touch'n Go MY/MYR redirect-wallet overview for desktop QR and mobile app/browser shopper routes, capability marks and Web/native/API-only links; no merchant setup or outcome proof.


- [[source-adyen-docs-payment-methods-grabpay]] — 2026-09-15 GrabPay overview for shopper redirect, Wallet/PayLater geography, Wallets capability matrix, refund-reference rule and channel routes; the matrix is Wallets-scoped, and shopper confirmation is not merchant payment-outcome proof.


- [[source-adyen-docs-payment-methods-momo-wallet-android]] — 2026-09-15 MoMo Android chooser linking Drop-in and redirect-oriented InstantPaymentComponent children plus four Sessions/Advanced base routes; child versions, eligibility and outcomes remain separate evidence.


- [[source-adyen-docs-payment-methods-momo-wallet-web]] — 2026-09-15 MoMo Web navigation chooser linking Drop-in/Redirect Components child guides and Sessions/Advanced main Web guides; child requirements and outcomes remain separate authority.


- [[source-adyen-docs-payment-methods-gcash-web]] — 2026-09-15 GCash Web chooser linking Drop-in/Components children and Sessions/Advanced main guides; navigation only, with child implementation and outcomes separate.


- [[source-adyen-docs-payment-methods-gcash-android]] — 2026-09-15 GCash Android chooser for Drop-in or InstantPaymentComponent child guides and the Android Sessions/Advanced main integration routes; child setup and outcomes require separate evidence.


- [[source-adyen-docs-payment-methods-dana-web]] — 2026-09-15 DANA Web navigation chooser linking Drop-in and Redirect Components child guides plus main Sessions/Advanced Web routes; child requirements and outcomes are separate evidence.


- [[source-adyen-docs-payment-methods-dana-android]] — 2026-09-15 DANA Android navigation chooser linking Drop-in, InstantPaymentComponent and Sessions/Advanced base guides; child setup and outcomes remain separate authority.


- [[source-adyen-docs-payment-methods-momo-wallet-ios]] — 2026-09-15 MoMo iOS chooser linking Drop-in and InstantPaymentComponent children plus four Sessions/Advanced base-guide routes; child versions, eligibility, token and outcome behavior remain separate evidence.


- [[source-adyen-docs-payment-methods-gcash-ios]] — 2026-09-15 GCash iOS navigation chooser for Drop-in and InstantPaymentComponent child guides plus main Sessions/Advanced iOS routes; child versions, setup and outcomes remain separate evidence.


- [[source-adyen-docs-payment-methods-dana-ios]] — 2026-09-15 DANA iOS navigation chooser linking Drop-in, InstantPaymentComponent and Sessions/Advanced main integration guides; child requirements and outcomes remain separate authority.


- [[source-adyen-docs-payment-methods-doku-doku-web]] — 2019-modified, 2026-09-15-captured DOKU Indonesia Web chooser linking Drop-in and Components guides for bank-transfer/convenience-store options; child variant, version, eligibility and outcome details remain separate.


- [[source-adyen-docs-payment-methods-momo-wallet-api-only]] — 2026-09-15 MoMo API-only add-on (linked Advanced Web base guide; discovery lists Web, iOS and Android channels) for VN/VND method discovery, redirect, settled-payment token route and TEST/live setup; generic form/fulfillment prose and example discrepancies are qualified in source.


- [[source-adyen-docs-payment-methods-doku-drop-in]] — 2019-modified, 2026-09-15-captured Indonesia DOKU Web Drop-in Sessions/Advanced add-on for bank-transfer virtual accounts and convenience-store vouchers, 48-hour default expiry, TEST route and live method request.


- [[source-adyen-docs-payment-methods-doku-component]] — 2019-modified, 2026-09-15-captured DOKU Indonesian Web Components guide for bank-transfer/convenience-store variants, local-entity restrictions, v5/v6 creation, 48-hour default account/voucher validity and TEST/live gates.


- [[source-adyen-docs-payment-methods-dana-react-native-component]] — 2026-09-15 DANA React Native Components Advanced-only redirect add-on with settled-payment recurring-token route; title, Drop-in prerequisite URL and TEST/live wording are qualified in source.


- [[source-adyen-docs-payment-methods-gcash-react-native-component]] — 2026-09-15 GCash React Native Components Advanced-only redirect add-on (Sessions unsupported), with base no-extra-fields, three-character token shopper reference and settlement-gated recurring webhook; prerequisite link misroutes to Drop-in.


- [[source-adyen-docs-payment-methods-momo-wallet-react-native-component]] — 2026-09-15 MoMo React Native Components Advanced-only redirect add-on (Sessions unsupported) with settlement-gated recurring-token route; title/base-guide link and Java example require source qualification.


- [[source-adyen-docs-payment-methods-gcash-api-only]] — 2026-09-15 GCash API-only Advanced redirect guide for PH/PHP method discovery and settled-payment recurring token route; form-details wording and discovery-example channel omission are qualified.


- [[source-adyen-docs-payment-methods-dana-api-only]] — 2026-09-15 DANA API-only Advanced Web redirect/discovery guide with 300 IDR minimum and settled-payment token route; the IN/INR table conflicts with ID/IDR examples, so eligibility is unresolved.


- [[source-adyen-docs-payment-methods-doku-doku-api-only]] — 2019-modified, 2026-09-15-captured Indonesia DOKU API-only guide for ID/IDR variant selection, merchant-owned form and server request, with voucher-specific asynchronous webhook states, 48-hour default validity and BCA/BRI entity caveats.


- [[source-adyen-docs-payment-methods-dana-ios-drop-in]] — 2026-09-15 DANA iOS Drop-in Sessions (Checkout API v68+) and Advanced add-on with a separate settlement-gated recurring-token route, Advanced redirect requirement and qualified TEST/live wording.


- [[source-adyen-docs-payment-methods-dana-android-drop-in]] — 2026-09-15 DANA Android Drop-in Sessions (Checkout API v68+) and Advanced add-on with Advanced redirect handling and settlement-gated recurring-token route; TEST/live wording and example amounts are qualified.


- [[source-adyen-docs-payment-methods-gcash-ios-drop-in]] — 2026-09-15 iOS Drop-in GCash Sessions/Advanced add-on: no extra base fields, Advanced redirect action, three-character token shopper reference and settlement-gated recurring token webhook; TEST/live scopes remain distinct.


- [[source-adyen-docs-payment-methods-gcash-android-drop-in]] — 2026-09-15 GCash Android Drop-in add-on for existing Sessions (Checkout API v68+) or Advanced flow, with settled-payment recurring-token route and qualified live-number versus test-status instructions.


- [[source-adyen-docs-payment-methods-dana-flutter-component]] — 2026-09-15 DANA Flutter Components Sessions/Advanced redirect add-on with a separate settlement-gated recurring-token route; both Components prerequisite links mistakenly target Drop-in pages.


- [[source-adyen-docs-payment-methods-dana-react-native-drop-in]] — 2026-09-15 DANA React Native Drop-in Sessions (Checkout API v68+) and Advanced add-on with redirect and settled-payment recurring-token route; Sessions prerequisite link and TEST/live wording are qualified.


- [[source-adyen-docs-payment-methods-dana-flutter-drop-in]] — 2026-09-15 DANA Flutter Drop-in Sessions (Checkout API v68+) and Advanced redirect add-on with settlement-gated token route; setup wording, Sessions prerequisite link and test/live wording need source qualification.


- [[source-adyen-docs-payment-methods-gcash-flutter-component]] — 2026-09-15 GCash Flutter Components add-on for existing Sessions (Checkout API v68+) and Advanced redirects, with separate post-settlement recurring-token route; Integration type URLs point to Drop-in and test/live wording remains qualified in source.


- [[source-adyen-docs-payment-methods-gcash-react-native-drop-in]] — 2026-09-15 GCash React Native Drop-in Sessions (Checkout API v68+) and Advanced redirect add-on with separate settlement-gated recurring-token route; Sessions guide-link and test/live wording remain source-qualified.


- [[source-adyen-docs-payment-methods-dana-web-drop-in]] — 2026-09-16 DANA Web Drop-in Sessions/Advanced redirect add-on: no extra base-request fields, separate recurring token `/payments` and post-settlement webhook, with TEST/live scope and an unresolved Advanced prerequisite URL template.


- [[source-adyen-docs-payment-methods-gcash-flutter-drop-in]] — 2026-09-15 GCash Flutter Drop-in Sessions (Checkout API v68+) and Advanced redirect add-on with settlement-gated recurring token route; Sessions link, setup paths and TEST/live wording are source-qualified.


- [[source-adyen-docs-payment-methods-gcash-web-drop-in]] — 2026-09-15 GCash Web Drop-in Sessions/Advanced add-on for redirect setup, optional import, settlement-gated recurring tokens and live request; its Advanced prerequisite URL has an encoded platform template.


- [[source-adyen-docs-payment-methods-momo-wallet-android-drop-in]] — 2026-09-15 MoMo Android Drop-in add-on for existing Sessions (Checkout API v68+) or Advanced flows, with a separate settlement-gated recurring-token route, test/live prerequisites and qualified Java example.


- [[source-adyen-docs-payment-methods-dana-web-component]] — 2026-09-15 DANA Web Redirect Component Sessions/Advanced add-on with a separate settled-payment recurring token route; unquoted `type:dana` snippets and base-versus-recurring request scope are qualified.


- [[source-adyen-docs-payment-methods-gcash-web-component]] — 2026-09-15 GCash Web Components Sessions (Checkout API v68+) and Advanced Redirect add-on with settlement-gated recurring token route; example syntax and TEST/live wording remain qualified.


- [[source-adyen-docs-payment-methods-momo-wallet-flutter-component]] — 2026-09-15 MoMo Flutter Components Sessions (Checkout API v68+) and Advanced redirect add-on with separate settled-payment token route; both prerequisite links point to Drop-in, and Java token example differs from prose.


- [[source-adyen-docs-payment-methods-momo-wallet-react-native-drop-in]] — 2026-09-15 MoMo React Native Drop-in method add-on for existing Sessions (Checkout API v68+) and Advanced flows, redirect handling and separate settlement-gated recurring-token route; base-guide link and Java token-field discrepancies remain qualified in source.


- [[source-adyen-docs-payment-methods-momo-wallet-flutter-drop-in]] — 2026-09-15 MoMo Flutter Drop-in Sessions (Checkout API v68+) and Advanced redirect add-on, with separate settlement-gated recurring-token route, TEST/live steps and source-qualified setup-link/example differences.


- [[source-adyen-docs-payment-methods-momo-wallet-web-drop-in]] — 2026-09-15 MoMo Web Drop-in Sessions (Checkout API v68+)/Advanced redirect add-on with separate settled-payment recurring-token route, TEST/live prerequisites and qualified example-field mismatch.


- [[source-adyen-docs-payment-methods-dana-ios-component]] — 2026-09-15 iOS Components DANA add-on for Sessions/Advanced redirect and InstantPaymentComponent, with separate post-settlement recurring-token webhook and TEST/live qualifications; Advanced prerequisite link mislabels the integration route.


- [[source-adyen-docs-payment-methods-momo-wallet-web-component]] — 2026-09-15 MoMo Web Redirect Component guide for Sessions/Advanced prerequisites, optional recurring tokens and TEST app/QR versus LIVE request boundaries.


- [[source-adyen-docs-payment-methods-gcash-ios-component]] — 2026-09-15 GCash iOS Components add-on for existing Sessions/Advanced integrations, redirect setup, settlement-gated recurring token route and live Customer Area request; the Advanced Components prerequisite links to a Drop-in URL.


- [[source-adyen-docs-payment-methods-momo-wallet-ios-component]] — 2026-09-15 MoMo iOS InstantPaymentComponent add-on for existing Sessions/Advanced flows, redirect handling and settled-payment recurring-token route; base-guide link and example-field qualifications remain in source.


- [[source-adyen-docs-payment-methods-dana-android-component]] — 2026-09-15 DANA Android Component Sessions/Advanced redirect add-on with a separate settlement-gated recurring-token route; base no-extra-fields wording excludes recurring fields.


- [[source-adyen-docs-payment-methods-gcash-android-component]] — 2026-09-15 GCash Android Components Sessions (Checkout API v68+) and Advanced method add-on, with redirect handling and settlement-gated recurring-token route; TEST/live wording and outcomes remain qualified.


- [[source-adyen-docs-payment-methods-momo-wallet-android-component]] — 2026-09-15 MoMo Android Components Sessions (Checkout API v68+) and Advanced redirect add-on, with separate settled-payment recurring-token route, TEST/live prerequisites and qualified Java token-field example.


- [[source-adyen-docs-payment-methods-doku]] — 2023-modified, 2026-09-15-captured Indonesia DOKU overview for expiring order-specific bank-transfer virtual accounts and convenience-store cash vouchers, with authorization-webhook-before-delivery flow, variant/local-entity caveats and Web/API-only navigation.


- [[source-adyen-docs-payment-methods-gcash]] — 2026-09-15 GCash PH/PHP redirect-wallet overview covering one-time versus recurring shopper journeys, default 30-minute redirect expiry, capability marks and channel routes; return/SMS and matrix marks do not prove transaction outcome or merchant eligibility.


- [[source-adyen-docs-payment-methods-momo-wallet]] — 2026-09-15 MoMo VN/VND redirect-wallet overview with desktop QR, mobile web and app shopper journeys, qualified capability marks and channel-guide routes; no merchant setup or payment-outcome proof.


- [[source-adyen-docs-payment-methods-dana]] — 2026-09-15 DANA ID/IDR wallet overview for shopper redirect, five-minute default redirect-page lifetime, 300-IDR display floor, capability matrix and channel child routes; redirect/result display is not merchant-side outcome proof.


- [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-in-app-payments-ios]] — 2020-modified, 2026-09-15-captured WeChat Pay in-app iOS chooser for Drop-in/Components child pages and Sessions base guides; child setup, app switch and outcomes are separate authority.


- [[source-adyen-docs-payment-methods-upi-web]] — 2026-09-15 UPI Web navigation chooser for Drop-in/Components child guides and Sessions/Advanced main Web guides; child requirements and payment outcomes remain separate authority.


- [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-in-app-payments-android]] — 2019-modified, 2026-09-15-captured WeChat Pay Android chooser for Drop-in/Components child guides and general Sessions-flow routes; child behavior, versions and outcomes remain separate evidence.


- [[source-adyen-docs-payment-methods-upi-android]] — 2026-09-15 UPI Android navigation chooser for Drop-in or redirect-oriented UPIComponent, plus four Android Sessions/Advanced base guides; child versions, method flows and outcomes require separate evidence.


- [[source-adyen-docs-payment-methods-upi-ios]] — 2026-09-15 UPI iOS chooser linking Drop-in/UPIComponent child guides and Sessions/Advanced main iOS integration routes; child prerequisites and outcome behavior are outside this navigation page.


- [[source-adyen-docs-payment-methods-kakaopay-web]] — 2026-09-15 KakaoPay Web navigation chooser linking Drop-in and Redirect Components child guides and main Web Sessions/Advanced integration routes; child requirements and outcomes remain separate evidence.


- [[source-adyen-docs-payment-methods-kakaopay-android]] — 2026-09-15 Android KakaoPay navigation chooser linking Drop-in, InstantPaymentComponent and Sessions/Advanced base guides; child setup, support and outcomes require their own sources.


- [[source-adyen-docs-payment-methods-kakaopay-ios]] — 2026-09-15 iOS navigation chooser linking KakaoPay Drop-in and InstantPaymentComponent children plus four Sessions/Advanced main integration routes; child requirements, versions, eligibility and outcomes are separate evidence.


- [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-mini-program]] — 2019-modified, 2026-09-15-captured Mini Program overview for API-only `wechatpayMiniProgram` and a typical WeChat shopper journey; shopper pays wallet CNY even if processing currency differs, with implementation and payment outcomes left to separate authority.


- [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-in-app-payments]] — 2026-09-15 WeChat Pay mobile-app overview for Android integration or WeChat mobile-SDK route, shopper app switch, historical capability matrix and iOS/Android/API-only child navigation; no provider-registration, device-version or payment-outcome procedure on this page.


- [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-desktop-qr-payments]] — 2019-modified, 2026-09-15-captured WeChat Pay website overview separating desktop QR, enrolled mobile-browser H5 redirect and native in-app flow, with a historical capability row and child-guide links but no QR-expiry or final-outcome procedure.


- [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-in-app-payments-enable-wechat-pay]] — 2020-modified, 2026-09-15-captured WeChat Pay in-app setup guide for WeChat developer/app registration, AppID/AppSecret handoff to Adyen Support and conditional own-integration mobile SDK steps; setup does not prove payment or settlement.


- [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-desktop-qr-payments-web-drop-in]] — 2020-modified, 2026-09-15-captured WeChat Pay Web Drop-in Sessions/Advanced add-on with separate desktop QR versus mobile-browser enrollment, v6 import guidance and live request gate; QR/outcome mechanics are not specified.


- [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-in-app-payments-android-drop-in]] — 2026-09-15 Android Drop-in WeChat Pay v5.0.0 guide: Sessions/Advanced base integrations and Customer Area setup, no additional method-specific fields/configuration, and historical no-TEST-platform/live-request gate; earlier versions and result mechanics have separate sources.


- [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-in-app-payments-android-component]] — 2026-09-15 WeChat Pay in-app Android Component v5.0.0 add-on for existing Sessions or Advanced flows, with no extra method-specific fields/configuration and a no-test-platform/live-request qualification; earlier-version app-switch details are separate.


- [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-desktop-qr-payments-web-component]] — 2019-modified, 2026-09-15-captured WeChat Pay Web Components guide under desktop-QR path, with distinct desktop QR/mobile-browser setup and v6/v5 mount routes; no QR payload, expiry or webhook-outcome mechanics.


- [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-in-app-payments-ios-drop-in]] — 2026-09-15 iOS in-app WeChat Pay Drop-in Sessions/Advanced add-on guide for WeChat/Xcode setup, version-qualified request/configuration scope, and no-test-platform plus live-request boundary.


- [[source-adyen-docs-payment-methods-upi-react-native-component]] — 2026-09-15 UPI React Native Components: Sessions unsupported; Advanced `await`, conditional Intent `appId` and TEST v72 example; QR is web-only in simulator checklist and AUTHORISED spelling conflicts with API-only AUTHORISATION outcome tables.


- [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-in-app-payments-ios-component]] — 2025-modified, 2026-09-15-captured in-app WeChat Pay iOS Components guide for app registration, Xcode schemes/SDK packaging, v5+ Sessions versus Advanced, no test platform and live request gate; app switch is not payment-outcome proof.


- [[source-adyen-docs-payment-methods-upi-flutter-drop-in]] — 2026-09-15 UPI Flutter Drop-in Sessions (Checkout v68+) and Advanced (`await`, Intent appId) add-on with TEST simulator instructions; Sessions URL, redirect-anchor and AUTHORISED/AUTHORISATION webhook wording differences are qualified in the source.


- [[source-adyen-docs-payment-methods-upi-react-native-drop-in]] — 2026-09-15 UPI React Native Drop-in Sessions (Checkout v68+) and Advanced add-on for conditional Intent `appId` and TEST simulator; Sessions base link, `await`/redirect contexts, Web-only QR wording and webhook spelling remain qualified in the source.


- [[source-adyen-docs-payment-methods-upi-android-drop-in]] — 2026-09-15 UPI Android Drop-in Sessions (Checkout v68+) and Advanced add-on with await action, Intent-only appId and TEST simulator guidance; Web-qualified QR step, Kotlin snippet and generic AUTHORISED checklist are source-qualified.


- [[source-adyen-docs-payment-methods-upi-android-component]] — 2026-09-15 UPI Android Components Sessions (Checkout v68+) and Advanced guide for await action, conditional Intent TPAP appId and TEST simulator/webhook checklist; QR text is web-scoped.


- [[source-adyen-docs-payment-methods-upi-ios-component]] — 2026-09-15 iOS Components guide for UPI Intent: Sessions v68+ and Smart Intent declared app schemes, Advanced `await` handling plus required Intent `appId`; simulator/web-only QR mention and webhook/Customer Area test checks do not prove an iOS QR/Collect flow or live result.


- [[source-adyen-docs-payment-methods-upi-web-drop-in]] — 2026-09-15 UPI Web Drop-in Sessions (Checkout v68+) and Advanced add-on for Intent/QR TEST simulator paths, conditional Advanced Intent `appId` and qualified action/webhook wording; Collect migration belongs to the separate API-only source.


- [[source-adyen-docs-payment-methods-upi-web-component]] — 2026-09-15 UPI Web Component Sessions (Checkout v68+) and Advanced guide with await action, Intent-only appId, TEST Intent/QR simulator and qualified webhook checks; sample `newUPI` and outcome wording need review.


- [[source-adyen-docs-payment-methods-kakaopay-react-native-component]] — 2026-09-15 KakaoPay React Native Components Advanced-only redirect add-on (Sessions unsupported) with settlement-gated recurring token route; title and Drop-in prerequisite-link mismatch remain qualified.


- [[source-adyen-docs-payment-methods-upi-ios-drop-in]] — 2026-09-15 iOS Drop-in UPI Intent guide: Sessions v68+, Smart Intent privacy-limited declared schemes, Advanced `await` and required Intent `appId`; QR is mentioned only for web testing, while webhook/Customer Area checks bound simulator outcomes.


- [[source-adyen-docs-payment-methods-kakaopay-api-only]] — 2026-09-15 KakaoPay API-only Advanced Web redirect guide for KR/KRW discovery, ordinary versus recurring fields and token-created webhook after settlement; conditional item text, versioned examples and mixed TEST/LIVE wording are qualified in the source.


- [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-mini-program-api-only]] — 2019-modified, 2026-09-15-captured WeChat Mini Program API-only guide for merchant-server Adyen calls, WeChat `prepay_id`, `wx.requestPayment()` and webhook-qualified results; details-request example and test/live tensions remain source-qualified.


- [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-in-app-payments-android-drop-in-earlier-versions]] — 2019-modified WeChat Pay earlier-version Android Drop-in Advanced app-switch guide (support stated from 3.5.0), with Pending/Received webhook-final outcome and no TEST platform; Sessions navigation links conflict.


- [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-desktop-qr-payments-api-only]] — 2019-modified, 2026-09-15-captured WeChat Pay web API-only redirect guide under a desktop-QR path; body gives `wechatpayWeb` request/return/webhook flow, not QR or expiry mechanics, and TEST/LIVE qualifications remain in the source.


- [[source-adyen-docs-payment-methods-kakaopay-flutter-drop-in]] — 2026-09-15 KakaoPay Flutter Drop-in Sessions/Advanced add-on, with conditional settled-payment recurring token/webhook route, differing setup/example wording and separate TEST/LIVE gates.


- [[source-adyen-docs-payment-methods-kakaopay-web-drop-in]] — 2026-09-15 KakaoPay Web Drop-in: existing Sessions/Advanced redirect flow, no extra base request parameters, but recurring token requests need shopper identity and storage fields; token creation follows settled initial payment/webhook, with separate TEST/live prerequisites.


- [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-in-app-payments-api-only]] — 2026-09-15 WeChat Pay in-app API-only guide for merchant-server `/payments`, WeChat mobile-SDK handoff, `/payments/details` and webhook-qualified outcome; TEST examples and details prose conflict with stated boundaries.


- [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-in-app-payments-android-component-earlier-versions]] — 2019-modified, 2026-09-15-captured WeChat Pay in-app Android Component v4.x.x/3.5.0+ Advanced guide for server `wechatpaySDK`, SDK app switch and webhook-qualified result handling; TEST examples/no-test-platform and Advanced/See-also Sessions tension are qualified in the source.


- [[source-adyen-docs-payment-methods-kakaopay-ios-drop-in]] — 2026-09-15 KakaoPay iOS Drop-in Sessions (Checkout v68+) and Advanced add-on with settlement-conditioned recurring-token webhook and later token payments; mixed live/test wording and example limits remain source-qualified.


- [[source-adyen-docs-payment-methods-kakaopay-android-drop-in]] — 2026-09-15 KakaoPay Android Drop-in Sessions (Checkout v68+)/Advanced add-on with conditional settled-payment recurring token webhook and qualified TEST/LIVE example scope.


- [[source-adyen-docs-payment-methods-kakaopay-flutter-component]] — 2026-09-15 Flutter Components guide: Sessions/Advanced redirect prerequisites and base no-extra-parameter claims, separate recurring /payments fields and post-settlement token webhook; the integration-type links misroute to Drop-in (and Sessions to Advanced), so follow flow-specific prose and verify the main guide.


- [[source-adyen-docs-payment-methods-kakaopay-react-native-drop-in]] — 2026-09-15 KakaoPay React Native Drop-in Sessions (Checkout v68+) and Advanced redirect add-on with settlement-conditioned recurring-token webhook and later token payments; Sessions link and live/test wording remain qualified in the source.


- [[source-adyen-docs-payment-methods-kakaopay-web-component]] — 2026-09-15 KakaoPay Web Components add-on for existing Sessions/Advanced redirect flows and settled-payment recurring-token route; unquoted method identifier and differing test amounts remain source-qualified.


- [[source-adyen-docs-payment-methods-kakaopay-android-component]] — 2026-09-15 KakaoPay Android Component Sessions/Advanced redirect add-on with separate settlement-gated recurring token route; base no-extra-fields wording excludes recurring fields.


- [[source-adyen-docs-payment-methods-upi-api-only]] — 2022-modified, 2026-09-15-captured India UPI API-only guide for INR Intent app redirects, QR display and legacy Collect VPA, with November 2025 new-merchant Collect cutoff, conditional validation and webhook-final outcomes; TEST checklist event spelling conflicts with webhook tables.


- [[source-adyen-docs-payment-methods-upi-upi-autopay]] — 2026-09-15 UPI Autopay recurring-mandate guide covering Collect/QR/mobile Intent signup, first-payment-dependent tokenization/cancellation, later PIN threshold and 2-INR free-trial refund path.


- [[source-adyen-docs-payment-methods-kakaopay]] — 2026-09-15 KakaoPay KR/KRW wallet-redirect overview for one-time QR and recurring login journeys, default 30-minute redirect expiry, capability marks and child integration routes; shopper steps do not prove mandate or payment outcome.


- [[source-adyen-docs-payment-methods-upi]] — 2026-09-15 UPI overview for India local-entity/integration prerequisite, Intent/QR/Collect routes and November 2025 Collect transition notice; recurring “See note” lacks an on-page mandate explanation.


- [[source-adyen-docs-payment-methods-wechat-pay]] — 2026-09-15 WeChat Pay overview: separate desktop QR/H5, in-app, Mini Program and POS routes; mobile-web initiation is limited to the WeChat app, some outcomes require webhook confirmation, and the matrix limits recurring/capture/chargeback while permitting refunds in this snapshot.


- [[source-adyen-docs-payment-methods-paypay-web]] — 2026-09-15 PayPay for Web chooser linking Drop-in, Redirect Component and main Sessions/Advanced Web integration guides; navigation only, with child requirements and outcomes separate.


- [[source-adyen-docs-payment-methods-paypay-android]] — 2026-09-15 PayPay Android chooser for Drop-in/Components and Sessions/Advanced main guides; it labels InstantPaymentComponent for redirect but leaves child behavior and outcomes to linked guides.


- [[source-adyen-docs-payment-methods-naverpay-web]] — 2026-09-15 NaverPay Web navigation chooser for Drop-in, Redirect Components and Sessions/Advanced main guides; child setup and outcomes remain separate authority.


- [[source-adyen-docs-payment-methods-alipay-web]] — 2026-09-15 Alipay Web navigation chooser linking Drop-in and Redirect Components child guides plus four main Web Sessions/Advanced integration routes; child behavior, version and merchant eligibility remain separate evidence.


- [[source-adyen-docs-payment-methods-alipay-android]] — 2026-09-15 Alipay Android chooser linking Drop-in, InstantPaymentComponent and main Sessions/Advanced Android integration guides; navigation only, with child conditions and outcomes left to their sources.


- [[source-adyen-docs-payment-methods-paypay-ios]] — 2026-09-15 PayPay iOS navigation chooser for Drop-in/Components and Sessions/Advanced main guides; its Components label contains an unresolved `None` placeholder.


- [[source-adyen-docs-payment-methods-alipay-ios]] — 2026-09-15 Alipay iOS navigation chooser for Drop-in, InstantPaymentComponent and Sessions/Advanced main guides; child version, redirect and outcome details remain separate authority.


- [[source-adyen-docs-payment-methods-naverpay-web-drop-in]] — 2026-09-15 NaverPay Web Drop-in add-on for existing Sessions (Checkout v68+) and Advanced redirect flows; no NaverPay-specific extra request fields and no test environment, with a qualified live-small-amount recommendation.


- [[source-adyen-docs-payment-methods-alipayhk-web]] — 2026-09-15 Alipay HK Web integration chooser linking Drop-in and Components child guides plus Web Sessions and Advanced base guides; no standalone method procedure.


- [[source-adyen-docs-payment-methods-alipayhk-android]] — 2026-09-15 Alipay HK Android chooser linking Drop-in, InstantPaymentComponent and main Sessions/Advanced Android integration guides; navigation only, without child-guide eligibility or outcome claims.


- [[source-adyen-docs-payment-methods-alipayhk-ios]] — 2026-09-15 Alipay HK iOS navigation chooser for Drop-in/Components and Sessions/Advanced main guides; its Components label contains an unresolved `None` placeholder.


- [[source-adyen-docs-payment-methods-alipayhk-react-native-component]] — 2026-09-15 React Native Alipay HK Component guide stating Sessions unavailable and Advanced redirect/no-extra-method-field setup, with TEST credentials/live request; Advanced Components label links to Drop-in.


- [[source-adyen-docs-payment-methods-paypay-react-native-component]] — 2026-09-15 PayPay React Native Components Advanced-only add-on (Sessions explicitly unsupported), with redirect/no-extra-method-fields, DGFT TEST simulator and LIVE app/Japan-IP conditions; title and Drop-in-link mismatches are qualified in the source.


- [[source-adyen-docs-payment-methods-alipay-react-native-component]] — 2026-09-15-captured Alipay React Native Components guide: Sessions unsupported, Advanced redirect plus Customer Area setup, no additional Alipay-specific fields, recommended live penny tests and separate live request gate; Integration type link points to Drop-in.


- [[source-adyen-docs-payment-methods-alipayhk-ios-drop-in]] — 2026-09-15 Alipay HK iOS Drop-in add-on for Sessions (Checkout v68+) and Advanced (explicit redirect) flows, no extra method-specific fields, test fixture and separate live request; no payment-outcome proof.


- [[source-adyen-docs-payment-methods-alipayhk-android-drop-in]] — 2026-09-15 Alipay HK Android Drop-in add-on for existing Sessions (Checkout v68+) and Advanced flows, with Advanced redirect wording, no extra method fields, test credentials and a separate live request.


- [[source-adyen-docs-payment-methods-alipayhk-api-only]] — 2026-09-15 Web Advanced API-only Alipay HK add-on for HK/HKD method discovery, redirect and TEST/live setup; high-level form/item wording requires qualification against specific no-extra-field sections, and TEST curl is incomplete.


- [[source-adyen-docs-payment-methods-alipay-ios-drop-in]] — 2026-09-15 Alipay iOS Drop-in add-on for existing Sessions (Checkout v68+) and Advanced redirect flows, with method-specific no-extra fields and distinct recommended live penny tests/live request.


- [[source-adyen-docs-payment-methods-alipay-android-drop-in]] — 2026-09-15 Alipay Android Drop-in add-on for Sessions (Checkout v68+) and Advanced (explicit redirect) flows, no extra method-specific fields and live request/penny-test guidance; no payment-outcome proof.


- [[source-adyen-docs-payment-methods-paypay-api-only]] — 2026-09-15 PayPay API-only add-on for JP/JPY discovery, redirect, TEST DGFT simulator and LIVE app/Japan-IP conditions; item-data prose conflicts with no-extra-parameters wording.


- [[source-adyen-docs-payment-methods-paypay-ios-drop-in]] — 2026-09-15 PayPay iOS Drop-in Sessions/Advanced add-on with Sessions-only Checkout v68+, Advanced redirect, no extra method fields, TEST DGFT simulator and LIVE activated-app/Japan-IP condition.


- [[source-adyen-docs-payment-methods-paypay-android-drop-in]] — 2026-09-15 PayPay Android Drop-in Sessions/Advanced add-on for Sessions-only Checkout v68+, Advanced redirect prerequisite, no extra PayPay fields, DGFT TEST simulator and LIVE activated-app/Japan-local-IP condition; outcome remains unproven.


- [[source-adyen-docs-payment-methods-naverpay-web-component]] — 2026-09-15 NaverPay Web Redirect Component add-on for existing Sessions (v68+) or Advanced flows; no test environment, live-small-amount recommendation and unquoted type example remain qualified.


- [[source-adyen-docs-payment-methods-alipayhk-flutter-drop-in]] — 2026-09-15 Alipay HK Flutter Drop-in add-on for Sessions (Checkout v68+) and Advanced redirect flows, no extra method-specific fields, test fixture and live request; Sessions integration-type URL points to Advanced.


- [[source-adyen-docs-payment-methods-alipayhk-flutter-component]] — 2026-09-15 Alipay HK Flutter Components add-on for existing Sessions (Checkout v68+) and Advanced redirects, with test/live gates and mismatched prerequisite URLs pointing to Drop-in.


- [[source-adyen-docs-payment-methods-alipayhk-react-native-drop-in]] — 2026-09-15 Alipay HK React Native Drop-in Sessions/Advanced redirect add-on with Sessions-only Checkout v68+, no extra method fields, TEST credentials and live request gate; Sessions requirement URL points to Advanced.


- [[source-adyen-docs-payment-methods-alipay-flutter-drop-in]] — 2026-09-15 Alipay Flutter Drop-in add-on for Sessions (v68+/redirect) and Advanced, with method-specific no-extra fields, live-request gate and malformed Advanced version/link text.


- [[source-adyen-docs-payment-methods-alipay-flutter-component]] — 2026-09-15 Alipay Flutter Components add-on for Sessions (Checkout v68+) and Advanced redirect flows, no extra method-specific fields, live request and penny-test guidance; integration-type URLs conflict with their labels.


- [[source-adyen-docs-payment-methods-alipay-react-native-drop-in]] — 2026-09-15 Alipay React Native Drop-in add-on for existing Sessions (Checkout v68+) and Advanced redirects, with no extra method parameters, live request gate and Sessions-link mismatch.


- [[source-adyen-docs-payment-methods-alipay-api-only]] — 2026-09-15 Web Advanced API-only Alipay add-on for country/currency-filtered discovery, redirect and live request/test guidance; form/item-field prose conflicts with specific no-extra-field sections and TEST curl has a continuation defect.


- [[source-adyen-docs-payment-methods-alipay-web-component]] — 2026-09-15 Alipay Web Redirect Component add-on for existing Sessions (Checkout v68+) and Advanced flows, with separate live request gate and inconsistent initialization snippets.


- [[source-adyen-docs-payment-methods-paypay-flutter-drop-in]] — 2026-09-15 PayPay Flutter Drop-in add-on for existing Sessions (v68+) or Advanced redirect flows, with TEST DGFT simulator and LIVE app/Japan-IP conditions; the Sessions prerequisite link is mismatched.


- [[source-adyen-docs-payment-methods-paypay-flutter-component]] — 2026-09-15-captured PayPay Flutter Components Sessions/Advanced add-on with redirect handling, no extra PayPay-specific fields, TEST DGFT simulator and LIVE activated-app/Japan-local-IP condition; Integration type links point to Drop-in and outcomes remain unproven.


- [[source-adyen-docs-payment-methods-paypay-react-native-drop-in]] — 2026-09-15 PayPay React Native Drop-in Sessions/Advanced add-on for redirect handling, method-specific parameter absence, TEST DGFT simulator and LIVE activated-app/Japan-local-IP gate; Sessions URL mismatch and outcome limits are qualified in the source.


- [[source-adyen-docs-payment-methods-alipayhk-web-drop-in]] — 2026-09-15 Alipay HK Web Drop-in add-on for existing Sessions/Advanced redirect flows, Sessions v68+ and separate TEST/LIVE setup; no full return or outcome procedure.


- [[source-adyen-docs-payment-methods-paypay-web-drop-in]] — 2026-09-15 PayPay Web Drop-in add-on for Sessions (Checkout v68+) and Advanced redirect flows, optional method import, DGFT TEST and LIVE app/IP instructions; Advanced guide URL has an unresolved template placeholder.


- [[source-adyen-docs-payment-methods-alipayhk-web-component]] — 2026-09-15 Alipay HK Web Redirect Component add-on for existing Sessions (Checkout v68+) and Advanced flows, with test/live gates and an unresolved unquoted type example.


- [[source-adyen-docs-payment-methods-alipay-web-drop-in]] — 2026-09-15 Alipay Web Drop-in Sessions/Advanced add-on for redirect, Sessions-only Checkout v68+ gate and live request/test steps; optional-import prose/snippet and Advanced URL conflict remain source-qualified.


- [[source-adyen-docs-payment-methods-paypay-web-component]] — 2026-09-15 PayPay Web Components add-on for Sessions (Checkout v68+) and Advanced redirect flows, TEST simulator and LIVE app/IP instructions; the unquoted `paypay` snippet and flow-specific version scope are qualified in the source.


- [[source-adyen-docs-payment-methods-alipay-ios-component]] — 2026-09-15 Alipay iOS InstantPaymentComponent add-on for Sessions/Advanced redirects, Sessions-only Checkout v68+ prerequisite and live request/test steps; Advanced integration link and sample have qualifications.


- [[source-adyen-docs-payment-methods-alipayhk-ios-component]] — 2026-09-15 iOS Alipay HK Components add-on for existing Sessions/Advanced redirect flows, with Sessions v68+ requirement, live Customer Area request gate and unresolved `None`/configuration snippet plus Advanced Drop-in link mismatch.


- [[source-adyen-docs-payment-methods-alipayhk-android-component]] — 2026-09-15 Alipay HK Android Component add-on for existing Sessions (Checkout API v68+) or Advanced flows, with redirect handling and separate test/live Customer Area steps; no payment-outcome proof.


- [[source-adyen-docs-payment-methods-alipay-android-component]] — 2026-09-15 Alipay Android Component add-on for existing Sessions (Checkout API v68+) and Advanced flows, redirect handling, InstantPaymentComponent and a live Customer Area request; payment outcomes remain in main guides.


- [[source-adyen-docs-payment-methods-paypay-android-component]] — 2026-09-15-captured PayPay Android Components Sessions/Advanced supplement for redirect handling, InstantPaymentComponent imports, TEST DGFT simulator accounts and LIVE activated-app/Japan-local-IP condition; no payment-outcome proof.


- [[source-adyen-docs-payment-methods-naverpay-api-only]] — 2026-09-15 NaverPay API-only Advanced-flow add-on for KR/KRW discovery and redirect response, with no NaverPay test environment; item-data/no-extra-parameters and incomplete-payment-example tensions are qualified in the source.


- [[source-adyen-docs-payment-methods-naverpay]] — 2026-09-15 NaverPay KR/KRW redirect-wallet overview with refund/capture/recurring matrix and Web/API-only child-guide routes; no onboarding or outcome procedure.


- [[source-adyen-docs-payment-methods-paypay]] — 2026-09-15 PayPay overview for JP/JPY wallet redirect, qualified capability matrix and Web/native/API-only routes; its unresolved “See note” markers and links do not establish live eligibility or payment outcome.


- [[source-adyen-docs-payment-methods-alipayhk]] — 2026-09-15 Alipay HK wallet overview for HK/HKD redirect, capability marks and Web/native/API-only navigation; child guides and payment outcomes remain separate.


- [[source-adyen-docs-payment-methods-alipay]] — 2026-09-15 Alipay overview for outside-China merchant processing boundary, 12-hour offer, refund/recurring/capture capability marks and Web/native/API-only/Pay by Link/POS routes; overview marks do not prove current eligibility or payment outcomes.


- [[source-adyen-docs-payment-methods-apple-pay-ios]] — 2026-09-15 Apple Pay for iOS chooser linking Drop-in, Component and general iOS integration pages; navigation only, with certificate, version and outcome questions left to child guides.


- [[source-adyen-docs-payment-methods-apple-pay-web]] — 2026-09-15 Apple Pay Web navigation chooser for Drop-in versus Component and their main Web integration guides; child prerequisites, browser support and outcomes remain separate authority.


- [[source-adyen-docs-payment-methods-paypal-web]] — 2020-modified, 2026-09-15-captured PayPal Web navigation page linking Web Drop-in and Components routes; it does not establish child-guide behavior, eligibility or payment outcome.


- [[source-adyen-docs-payment-methods-paypal-ios]] — 2026-09-15 PayPal for iOS chooser linking Drop-in, Redirect Component and general iOS integration pages; navigation only, with child prerequisites and outcomes left to their guides.


- [[source-adyen-docs-payment-methods-paypal-android]] — 2026-09-15 PayPal Android navigation chooser for Drop-in versus Redirect Component and their main Android guides; child setup, versions and outcomes are separate authority.


- [[source-adyen-docs-payment-methods-google-pay-web]] — 2026-09-15 Google Pay for Web chooser linking Web Drop-in, Web Component and general Web integration guides; navigation only, without child-guide prerequisites or outcome claims.


- [[source-adyen-docs-payment-methods-wallets-india-web]] — 2026-09-15 Wallets India Web navigation chooser linking Drop-in, WalletINElement Components, and Sessions/Advanced main-flow guides; child prerequisites and behavior remain separate authority.


- [[source-adyen-docs-payment-methods-wallets-india-web-drop-in]] — 2026-09-15 Wallets India Web Drop-in add-on for existing Sessions/Advanced flows, Sessions v68+ and live-request/no-test-platform limits; optional import names conflict.


- [[source-adyen-docs-payment-methods-google-pay-android]] — 2026-09-15 Android Google Pay chooser linking Drop-in/Component children and Sessions/Advanced base guides; navigation alone supplies no eligibility, version or payment outcome.


- [[source-adyen-docs-payment-methods-wallets-india]] — 2026-09-15 Wallets India overview for India local-entity/integration prerequisites, IN/INR capability matrix, wallet-page redirect and Web/API-only/Pay by Link routes; marks are not current eligibility or transaction proof.


- [[source-adyen-docs-payment-methods-samsung-pay-enable-samsung-pay]] — 2019-modified, 2026-09-15-captured Samsung Pay enablement guide for Adyen CSR/role setup, Samsung developer gateway/SDK setup and Support-configured schemes; setup is not live processing proof.


- [[source-adyen-docs-payment-methods-wallets-india-web-component]] — 2026-09-15 Wallets India Web Component add-on for existing Sessions/Advanced flows, with Sessions-only v68+ wording, no stated method-specific request fields, no test platform and a live Customer Area request gate; snippets conflict with import/config prose.


- [[source-adyen-docs-payment-methods-apple-pay-flutter-component]] — 2026-09-15 Flutter Apple Pay Component Sessions/Advanced add-on for own iOS certificate, client configuration and TEST/LIVE gates; raw prerequisite links and snippets have qualified defects, with no recurring flow specified here.


- [[source-adyen-docs-payment-methods-paypal-paypal-troubleshooting]] — 2026-09-15 PayPal Web Drop-in/Components `/payments` troubleshooting for overlay action, details callback, required smart button and currency/intent/merchant-ID errors; console errors leave an open offer.


- [[source-adyen-docs-payment-methods-google-pay-api-only-google-pay-token-decryption]] — 2026-09-15 API-only PCI-gated merchant Google Pay token-decryption guide for signature/expiry validation and FPAN/DPAN card-field mapping; overview PCI level and malformed sample requests remain qualified.


- [[source-adyen-docs-payment-methods-apple-pay-flutter-drop-in]] — 2026-09-15 Flutter Apple Pay Drop-in Sessions/Advanced guide for own-certificate setup, native merchant configuration and live credential role; table-versus-Dart merchant-ID spelling and payment-outcome limits are qualified in the source.


- [[source-adyen-docs-payment-methods-paypal-setup-paypal-direct-merchants]] — 2026-09-15-captured direct-merchant PayPal test/live sandbox, Customer Area and seven-day permission-link setup guide, with default capture/recurring configuration and stated Active-status timing; account status is not shopper consent, token or payment-outcome proof.


- [[source-adyen-docs-payment-methods-apple-pay-react-native-component]] — 2026-09-15 Advanced React Native Apple Pay Component guide for merchant-owned iOS certificate, client configuration and recurring display/token route; test/live and snippet qualifications remain.


- [[source-adyen-docs-payment-methods-google-pay-react-native-component]] — 2026-09-15 React Native Google Pay Component guide for Android activity handoff, wallet configuration, TEST/live setup and recurring-token navigation; environment value and code-fence discrepancies are source-qualified.


- [[source-adyen-docs-payment-methods-google-pay-flutter-drop-in]] — 2026-09-15 Google Pay Flutter Drop-in add-on for existing Sessions/Advanced flows, required wallet environment config, optional wallet settings and TEST/LIVE gates; snippets and outcomes remain qualified.


- [[source-adyen-docs-payment-methods-google-pay-flutter-component]] — 2026-09-15 Flutter Google Pay Component guide for existing Sessions/Advanced integrations, separate Google/Adyen environments, TEST/LIVE gates and incomplete/mismatched configuration snippets.


- [[source-adyen-docs-payment-methods-apple-pay-ios-drop-in]] — 2023-modified, 2026-09-15-captured Apple Pay iOS Drop-in Sessions/Advanced guide for own-certificate setup, versioned native configuration, recurring tokenization handoff and TEST/LIVE limits; code examples require version-aware review.


- [[source-adyen-docs-payment-methods-apple-pay-ios-component]] — 2023-modified, 2026-09-15-captured Apple Pay iOS Component guide for Sessions/Advanced prerequisites, v5.3/v5.0/v4 client configuration, recurring token route and live certificate/role gates; snippets have version-specific gaps.


- [[source-adyen-docs-payment-methods-google-pay-web-component-express-checkout]] — 2025-modified, 2026-09-15-captured Google Pay Web Component express guide for Advanced-only Web flow, v6 express flag, merchant-owned total validation and callback handoff; Android exclusion and inconsistent snippets are qualified in the source.


- [[source-adyen-docs-payment-methods-samsung-pay-samsung-pay-api]] — 2026-09-15 Samsung Pay API-only guide for CSR/developer/SDK/gateway and scheme setup, complete SDK-token server handoff, and distinct TEST/LIVE and result-code boundaries.


- [[source-adyen-docs-payment-methods-apple-pay-web-component-express-checkout]] — 2023-modified, 2026-09-15-captured Apple Pay Advanced Web Components v6 express add-on for contact/shipping callbacks and browser/live gates; client total and wallet authorization events are not server amount or payment-outcome proof.


- [[source-adyen-docs-payment-methods-wallets-india-api-only]] — 2019-modified, 2026-09-15-captured v68+ API-only Wallets India issuer discovery and redirect guide; TEST/no-test-platform, example issuer and v68/v72 differences remain qualified in the source.


- [[source-adyen-docs-payment-methods-google-pay-android-drop-in]] — 2026-09-15 Android Google Pay Drop-in guide for existing Sessions (Checkout API v69+) or Advanced flows, optional wallet settings, test-wallet scenarios and live role/Merchant-ID prerequisites; no payment-outcome proof.


- [[source-adyen-docs-payment-methods-google-pay-web-drop-in]] — 2023-modified, 2026-09-15-captured Google Pay Web Drop-in guide for v5+ Sessions versus Payments configuration, optional wallet/3DS/iframe settings, test/live gates and shopper funding limits; wallet approval is not authorization or payment-outcome proof.


- [[source-adyen-docs-payment-methods-paypal-android-component]] — 2021-modified, 2026-09-15-captured PayPal Android Redirect Component guide for server payment/return, webhook outcome, conditional risk/recurring setup and capture-dependent refunds; request examples conflict with Android channel/return URL guidance and contain field/encoding errors.


- [[source-adyen-docs-payment-methods-google-pay-web-component]] — 2019-modified, 2026-09-15-captured Google Pay Web Component guide for v5+ Sessions/default versus direct payments, v6/v5 mounting, optional wallet settings, recurring route and TEST/LIVE gates; callback naming and snippets need version review.


- [[source-adyen-docs-payment-methods-google-pay-android-component]] — 2026-09-15 Android Google Pay Component guide for existing Sessions/Advanced flows, optional wallet configuration and TEST/LIVE gates; v69+ is stated for Sessions, and component readiness is not payment-outcome proof.


- [[source-adyen-docs-payment-methods-google-pay-api-only]] — 2023-modified, 2026-09-15-captured Google Pay API-only gateway-token guide for Web/Android with Checkout v67+, server handoff, 3DS, TEST and LIVE prerequisites; examples and results have stated limits.


- [[source-adyen-docs-payment-methods-apple-pay-web-drop-in]] — 2026-09-15-captured, metadata-2021 Apple Pay Web Drop-in guide for Sessions/Advanced, certificate and browser/iframe gates, recurring/tracking callbacks and live domains; later-version prose and snippet faults remain qualified.


- [[source-adyen-docs-payment-methods-apple-pay-web-component]] — 2019-modified, 2026-09-15-captured Apple Pay Web Component Sessions/Advanced guide for certificate-dependent validation, browser/iframe and version gates, recurring configuration and live domains; example callback/snippet inconsistencies remain source-qualified.


- [[source-adyen-docs-payment-methods-paypal-api-only]] — 2026-09-15 Adyen PayPal API-only Advanced Web add-on for method discovery, conditional risk data, redirect/webhook outcome, capture/refund and settled-payment token lifecycle; HUF/list and code-example conflicts remain in the source.


- [[source-adyen-docs-payment-methods-paypal]] — 2023-modified, 2026-09-15-captured Adyen PayPal wallet overview for Web direct/mobile redirect, versioned PayPal buttons, narrower Venmo US/USD Web support, conditional risk data and child-guide routes; capability marks are not merchant enablement or transaction proof.


- [[source-adyen-docs-payment-methods-google-pay]] — 2023-modified, 2026-09-15-captured Google Pay wallet overview for conditional network/region support, DPAN/FPAN and 3DS/liability wording, express and channel routes; capability marks are not merchant or outcome proof.


- [[source-adyen-docs-payment-methods-paypal-android-drop-in]] — 2021-modified, 2026-09-15-captured PayPal Android Drop-in redirect guide for server request/return details, webhook-final outcome, conditional risk and recurring/refund setup; code-example conflicts remain source-qualified.


- [[source-adyen-docs-payment-methods-paypal-ios-component]] — 2026-09-15 PayPal iOS Redirect Component guide for v5 Sessions/Advanced setup, conditional risk data, webhook-led outcome, recurring tokens and capture-dependent refunds; snippets contain material conflicts.


- [[source-adyen-docs-payment-methods-paypal-web-drop-in]] — 2026-09-15 PayPal Web Drop-in Sessions/Advanced guide for setup, conditional risk fields, client buttons, webhook-led outcome, token gates and capture-dependent refunds; see source for material refund-prose/example conflicts.


- [[source-adyen-docs-payment-methods-paypal-web-component]] — 2019-modified, 2026-09-15-captured PayPal Web Component guide for versioned Sessions/Payments setup, conditional Fraudnet/risk fields, webhook-final outcomes, recurring token gates and capture-sensitive refunds; table/example callback and field-placement conflicts remain in the source.


- [[source-adyen-docs-payment-methods-paypal-web-component-express-checkout]] — 2026-09-15-captured PayPal Web Component v5.59.0+ Express guide for Sessions/Advanced order updates, latest paymentData, Advanced-only review and token exceptions; examples and 2023 metadata conflict need qualification.


- [[source-adyen-docs-payment-methods-samsung-pay]] — 2022-modified, 2026-09-15-captured Samsung Pay wallet overview for ecommerce payment-sheet and NFC POS routes, conditional device/region/issuer support, feature marks and child-guide navigation.


- [[source-adyen-docs-payment-methods-express-checkout]] — 2026-09-15 express-checkout overview for product/cart buttons, method/platform/flow Component-version matrix and separate faster-checkout alternatives; child guides own setup and outcomes.


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
