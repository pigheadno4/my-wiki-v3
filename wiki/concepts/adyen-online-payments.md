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
