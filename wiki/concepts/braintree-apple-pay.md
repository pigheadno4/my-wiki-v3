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

The page says Apple Pay cards can be vaulted and used for recurring billing and split shipment transactions. Separately, it says vaulting Apple Pay cards should only be used when the customer consents during checkout to future merchant-initiated transactions. It warns against using the vaulted card for a future transaction when the customer is present and can authorize the payment, saying that use results in declines. Setup requires Apple Pay certificates and Merchant IDs configured with Braintree and Apple, an iOS and/or JavaScript v3 client integration, and a server integration. For Braintree's iOS client SDK, the page gives the Apple Pay certificate a 25-month expiry and requires keeping it current. Exact device, iframe, processing, liability, fraud-tool and renewal details remain in the source's raw locators. [[source-braintree-payment-methods-apple-pay]]

## Sources

- [[source-braintree-docs-guides-apple-pay-configuration-ios-v7]] - 2026-09-16 captured Braintree iOS v7 configuration route for Apple Merchant ID, payment processing certificate, separate sandbox/production provisioning, renewal, and Xcode setup, with a dated mobile-SDK certificate warning and enterprise-provisioning exclusion

- [[source-braintree-docs-guides-apple-pay-client-side-ios-v7]] - 2026-09-16 captured Braintree iOS v7 custom Apple Pay client flow from PassKit request through Braintree nonce handoff, with Drop-in exclusion, a dated certificate warning and qualified MPAN guidance

- [[source-braintree-docs-reference-response-apple-pay-card-node]] - 2026-09-16 collected Node.js website response reference for Apple Pay Card product-ID metadata and its code-to-name table; not native-client or direct-Apple authority, current availability, authentication, acceptance or payment-lifecycle proof
- [[source-braintree-graphql-integration-guides-apple-pay]] - 2026-09-16 unversioned Braintree website GraphQL guide to Apple Pay environment accounts, web-domain setup, authorized single-use payment-method charging and qualified Vault routes; distinct from exact-version SDK/schema evidence, current enablement or execution proof

- [[source-braintree-payment-methods-apple-pay]] - Braintree Apple Pay identity and DPAN model, conditional availability and platform scope, vaulting consent guidance, integration roles and certificate renewal
