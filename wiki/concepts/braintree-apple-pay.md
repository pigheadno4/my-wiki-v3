---
title: "Braintree Apple Pay"
type: concept
category: technology
tags: [braintree, apple-pay, digital-wallets, mobile-payments, web-payments, vaulting]
---

## Braintree Apple Pay

Braintree's collected payment-method guide describes Apple Pay for mobile and web purchases using a credit or debit card associated with a supported Apple mobile device. Apple replaces the card number with an encrypted device-specific DPAN that Braintree and processing banks use for transactions. This is a Braintree-specific retrieval route; keep it distinct from [[paypal-apple-pay]] and from exact-version SDK implementation evidence. [[source-braintree-payment-methods-apple-pay]]

## Availability and platform boundary

The guide makes merchant availability conditional on business location and processing settings, with separate card-brand and American Express-account qualifications. It says eligible merchants can accept customers from Apple Pay-supported countries and regions, but the merchant must also be domiciled where Braintree onboarding and Apple Pay compatibility apply. For desktop web, its collected requirements include an iPhone, iPad, Apple Watch, or Mac that can authorize the payment, macOS Sierra 10.12 or later, and Safari; it also describes the latest Apple Pay SDK as enabling non-Safari browsers. Treat these as page-scoped snapshot statements, not proof of current merchant, customer, device, browser or card eligibility. [[source-braintree-payment-methods-apple-pay]]

## Vaulting and setup boundary

The broader collected payment-method guide describes setup as configuring Apple Pay certificates and Merchant IDs with Braintree and Apple before completing an iOS and/or JavaScript v3 client integration plus a server integration. The captured JavaScript v3 and iOS v7 website configuration routes, which are version-family documentation rather than exact SDK/package evidence, qualify that umbrella wording by platform: this captured JavaScript v3/web route says merchants do not generate or upload a Payment Processing Certificate because Braintree processes web transactions with its shared certificate, while the separately captured native iOS v7 route says use on a real device requires configuring an Apple Pay Merchant ID and Apple Pay payment processing certificate in Apple's Developer Center, generating the certificate with Braintree's CSR, and uploading it to the Braintree Control Panel. These are platform-scoped 2026-09-16 snapshot instructions, not proof of current enablement, completed provisioning or domain verification, or payment execution. [[source-braintree-payment-methods-apple-pay]] [[source-braintree-docs-guides-apple-pay-configuration-javascript-v3]] [[source-braintree-docs-guides-apple-pay-configuration-ios-v7]]

The page says Apple Pay cards can be vaulted and used for recurring billing and split shipment transactions. Separately, it says vaulting Apple Pay cards should only be used when the customer consents during checkout to future merchant-initiated transactions. It warns against using the vaulted card for a future transaction when the customer is present and can authorize the payment, saying that use results in declines. Setup requires Apple Pay certificates and Merchant IDs configured with Braintree and Apple, an iOS and/or JavaScript v3 client integration, and a server integration. For Braintree's iOS client SDK, the page gives the Apple Pay certificate a 25-month expiry and requires keeping it current. Exact device, iframe, processing, liability, fraud-tool and renewal details remain in the source's raw locators. [[source-braintree-payment-methods-apple-pay]]

## Sources

- [[source-braintree-docs-guides-apple-pay-configuration-android-v5]] - 2026-09-16 captured Braintree Apple Pay configuration page at an Android v5 route whose body provides no Android configuration and instead directs readers to iOS or JavaScript SDK v3; snapshot navigation only, not native Android support, current platform or SDK availability, environment enablement, completed configuration, or payment-execution proof

- [[source-braintree-docs-guides-apple-pay-provision-for-decrypted-node]] - 2026-09-16 captured Braintree Apple Pay decrypted-processing provisioning page at a Node route whose body says API provisioning is available only through the linked Ruby SDK route; no Node procedure, decryption mechanics, current account eligibility or enablement, completed provisioning, or payment-execution proof

- [[source-braintree-docs-reference-request-apple-pay-unregister-domain-node]] - 2026-09-16 captured Node request-reference route titled Apple Pay: Unregister Domain; the body documents no Node request object, method, route body, or result and says only the PHP and Ruby SDKs currently support managing Apple Pay web domains through the API

- [[source-braintree-docs-reference-request-apple-pay-registered-domains-node]] - 2026-09-16 captured Node.js request-reference route titled "Registered Domains" whose body only identifies PHP and Ruby SDK support for managing Apple Pay web domains through the API; no Node.js method, request body, returned-domain result, current availability, completed domain configuration, or payment-execution proof

- [[source-braintree-docs-reference-response-apple-pay-options-node]] - 2026-09-16 Braintree Node.js-routed Apple Pay Options response-reference stub whose captured availability note says only the PHP and Ruby SDKs support API-based web-domain management; it exposes no response fields or Node runtime behavior and is not current-support, configuration-completion or payment-execution proof

- [[source-braintree-docs-reference-request-apple-pay-register-domain-node]] - 2026-09-16 captured Node-routed request-reference stub for registering an Apple Pay web domain; its body limits API domain management to the PHP and Ruby SDKs and provides no Node request object, method, body schema, response schema, or example; not current-support, successful-registration, eligibility, or payment-execution proof

- [[source-braintree-docs-guides-apple-pay-client-side-android-v5]] - 2026-09-16 captured Android v5 website route whose body directs Apple Pay client integration to iOS v5 or JavaScript SDK v3 and preserves a dated mobile-certificate warning; no Android Apple Pay procedure, current support, exact-package status, or payment-execution proof


- [[source-braintree-docs-guides-apple-pay-overview]] - 2026-09-16 captured Braintree website overview routing iOS SDK in-app and JavaScript SDK v3 Safari web-checkout paths; a snapshot navigation route, not current availability, exact-package history, complete client/server lifecycle, or payment-execution proof

- [[source-braintree-docs-guides-apple-pay-testing-go-live]] - 2026-09-16 captured unversioned Braintree Apple Pay testing and go-live webpage for sandbox and production validation boundaries and launch checks

- [[source-braintree-docs-guides-apple-pay-configuration-javascript-v3]] - 2026-09-16 captured Braintree JavaScript v3/web configuration route for environment-matched iCloud testing accounts, sandbox and production domain registration, the web shared-certificate qualification, and production domain-association-file verification conditions

- [[source-braintree-docs-guides-apple-pay-configuration-ios-v7]] - 2026-09-16 captured Braintree iOS v7 configuration route for Apple Merchant ID, payment processing certificate, separate sandbox/production provisioning, renewal, and Xcode setup, with a dated mobile-SDK certificate warning and enterprise-provisioning exclusion

- [[source-braintree-docs-guides-apple-pay-client-side-ios-v7]] - 2026-09-16 captured Braintree iOS v7 custom Apple Pay client flow from PassKit request through Braintree nonce handoff, with Drop-in exclusion, a dated certificate warning and qualified MPAN guidance

- [[source-braintree-docs-reference-response-apple-pay-card-node]] - 2026-09-16 collected Node.js website response reference for Apple Pay Card product-ID metadata and its code-to-name table; not native-client or direct-Apple authority, current availability, authentication, acceptance or payment-lifecycle proof
- [[source-braintree-graphql-integration-guides-apple-pay]] - 2026-09-16 unversioned Braintree website GraphQL guide to Apple Pay environment accounts, web-domain setup, authorized single-use payment-method charging and qualified Vault routes; distinct from exact-version SDK/schema evidence, current enablement or execution proof

- [[source-braintree-payment-methods-apple-pay]] - Braintree Apple Pay identity and DPAN model, conditional availability and platform scope, vaulting consent guidance, integration roles and certificate renewal
