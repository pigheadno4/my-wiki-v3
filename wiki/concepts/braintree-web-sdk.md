---
title: "Braintree Web SDK"
type: concept
category: technology
tags: [braintree, javascript-sdk, checkout, hosted-fields, wallets, venmo, 3d-secure]
---

## Braintree Web SDK

Braintree Web is a modular browser SDK. A merchant creates a Braintree client from a tokenization key or client token, adds only the payment components needed by the checkout, receives a payment-method nonce from the browser flow, and sends that nonce to a Braintree server integration for transaction processing.

## Integration Model

The `braintree-web` package exposes separate components rather than a ready-made checkout UI. Hosted Fields provides merchant-styled card fields backed by Braintree-hosted iframes; Braintree Web Drop-in is a separate repository and product.

At `braintree-web@3.144.0`, the package exports 23 components covering:

- cards through Hosted Fields, 3D Secure, UnionPay, and American Express verification;
- PayPal Checkout, PayPal Checkout v6, Venmo, Fastlane, Apple Pay, and Google Pay;
- local payments, SEPA, US bank account verification, and Payment Request;
- data collection, vaulted-method management, preferred-method signals, and Payment Ready recommendations.

Component presence proves an SDK integration surface at this exact version. It does not prove merchant enablement, buyer eligibility, regional availability, or that a legacy component remains recommended.

## Card and Authentication Boundary

The collected JavaScript v3 credit-card guide distinguishes Hosted Fields from Card Fields: JavaScript v3 supports Hosted Fields but does not support Card Fields, while that guide lists client-side Card Fields only for Android v5 and iOS v7. Keep this boundary SDK- and version-qualified; the named native availability does not establish support in other versions. [[source-braintree-credit-cards-client-javascript-v3]]

Hosted Fields keeps sensitive card inputs inside injected Braintree frames while exposing styling, validation-state events, card-type changes, BIN availability, and tokenization to the merchant page. Direct card submission through the lower-level client API is a different PCI scope.

The retained `braintree-web@3.144.0` release updates its `credit-card-type` dependency to `10.2.0`. The independently retained standalone package is `credit-card-type@10.3.0`; its Troy addition must not be attributed to Braintree Web `3.144.0` without a newer exact dependency snapshot. See [[card-brand-detection]].

The same Braintree Web release pins `@braintree/uuid@2.0.0`. That utility uses global `crypto.randomUUID()`, falls back to `crypto.getRandomValues()` with explicit v4 and variant bits, and throws when no secure random source is available. It supplies internal identifiers rather than payment-resource creation or API idempotency. See [[source-github-uuid]].

The 3D Secure component verifies a card nonce and BIN, can collect device data, supports lookup inspection before challenge continuation, and returns liability-shift indicators. The merchant still decides whether a result without liability shift is acceptable.

## Wallet and PayPal Boundary

Wallet modules adapt external wallet SDKs or browser APIs into Braintree payment-method nonces. In particular:

- PayPal Checkout v6 loads PayPal Web SDK v6, creates one-time, Pay Later, checkout-with-vault, and billing-agreement sessions, checks eligible methods, and tokenizes approval data.
- Venmo supports mobile app switch plus optional desktop QR or desktop web-login paths. `paymentMethodUsage` distinguishes `single_use` from `multi_use`.
- Fastlane is a Braintree loader and initialization bridge; the delegated PayPal Fastlane runtime remains a separate evidence boundary.

These are Braintree processing paths. They must not be described as direct PayPal Orders API integrations.

## PayPal Checkout Changes in 3.144.0

The non-v6 `paypalCheckout` component adds View/Edit Funding Instrument for returning buyers with a vaulted Billing Agreement. The flow requires a Braintree client token generated with `preferredPaymentMethodToken`; the SDK exchanges its payment-method JWT for a billing-agreement JWT and supplies that token to PayPal `SavedPaymentMethods`. The edit flag applies to checkout, not vault creation.

The `paypalCheckoutV6` session path adds optional locale, landing-page type, user action, risk-correlation ID, and shipping-address controls. Checkout-with-vault can carry plan type and plan metadata. These fields establish an SDK request surface, not merchant or buyer eligibility.

Venmo component creation now treats failed incognito detection as an unknown, non-private result and continues setup. This avoids a detection failure becoming a checkout initialization failure; it does not establish private-browsing support.

## Historical Website SDK Lifecycle Policy

The collected 2026-09-16 JavaScript v3 deprecation-policy snapshot distinguishes four client-SDK states: one Active major is current, fully supported, and receives features; Inactive begins when a deprecation date is assigned and receives security updates only; Deprecated receives no updates while processing is stated to remain supported for one year after the deprecation date; and Unsupported receives neither developer nor Braintree Support support, with processing subject to suspension at any time. Braintree also reserves possible exceptions. The snapshot does not assign these states or dates to a particular retained `braintree-web` release and does not establish current browser or SDK support; keep the separately retained exact-version GitHub evidence independent. [[source-braintree-client-sdk-deprecation-policy-javascript-v3]]

## Versioned Evidence

The first retained baseline is `braintree-web@3.143.0` at SHA `bae582d791026c143abb91c3bdcada92b8c060f6`. Release `3.144.0` at SHA `41460fba05c1ea1222e795b36a10765a6699b8e7` adds PayPal funding-instrument editing, v6 session options, and the Venmo detection fallback. Release `3.145.0` at SHA `732ed094354d650605e678d98246ce6332952ad3` adds the checkout/recovery changes below. The latest retained release is `3.146.0` at SHA `893d4e786f4161c3b96c5d34425752c5b63ff84d`; all earlier baselines remain in the cumulative source and changelog.

## Checkout and Recovery Changes in 3.145.0

- PayPal Checkout v6 distinguishes billing-token-only vaulting from checkout-with-vault. The latter sends the billing token together with order/payment and payer identifiers. `implicitlyVaultedPaymentMethodToken` is exposed only if the gateway returns it; an upgrade does not guarantee vault success.
- Venmo desktop QR forwards requested billing/shipping-address flags through the modern `paymentMethodUsage` payment-context mutation. Requesting either flag requires `enrichedCustomerDataEnabled`; otherwise creation rejects with `VENMO_ECD_DISABLED`. The legacy QR mutation does not forward those flags. The refreshed QR modal adds rescan handling and custom fonts.
- Deferred client script loading retries once with forced reload after an initial load rejection. PayPal vault-initiated checkout and LocalPayment popup paths add suspend/resume observation and delayed close checking. Recovery analytics is not proof of tokenization, authorization, or settlement.
- FraudNet load failures become observable in analytics; Fastlane preserves underlying error detail. Dependencies change to `@braintree/asset-loader@2.1.0` and add `qrcode@1.5.4`.

These are changes in the Braintree adapter and retained browser implementation, not proof of changes in independently hosted PayPal/Fastlane runtimes. Source: [[source-github-braintree-web]]; release comparison: [[changelog-github-braintree-web]].

## Saved-Payment Editing and Hardening in 3.146.0

`braintree-web@3.146.0` adds v6 `createEditSavedPaymentSession()` for viewing/changing the funding instrument behind an existing PayPal Billing Agreement during checkout. This is distinct from the already-retained vault-initiated repeat-purchase flow and the non-v6 Edit FI path introduced in `3.144.0`. It requires a client token carrying the preferred vaulted payment-method context, a fresh client/adapter instance, and `<paypal-saved-payment-methods>` present before SDK loading. Approval still produces a nonce through tokenization, not a completed payment. See [[paypal-braintree-integration]] and [[source-github-braintree-web]].

The release also forwards `autoRedirect` and `fullPageOverlay` session-start options, blocks three dangerous property-path keys in Hosted Fields' EventedModel, and adds explicit frame targets to Payment Request, 3DS completion, and UnionPay. Payment Request adds domain verification; `framebus` changes from `6.1.0` to `6.2.0`. These are implementation changes, not proof of comprehensive security or browser acceptance. This latest retained release preserves all earlier versioned evidence above. [[changelog-github-braintree-web]]

## Related

- [[source-braintree-docs-reference-client-reference-javascript-v2-browser-support]] - historical JavaScript v2 browser-support snapshot covering tested desktop/mobile inventory, IE/TLS constraints, PayPal webview limitations and no-fix guidance, and the untested/undeveloped hybrid-runtime boundary; not current browser, package or runtime proof

- [[source-braintree-docs-reference-client-reference-javascript-v2-credit-cards]] - JavaScript v2 direct credit-card tokenization and 3D Secure UI reference covering the SAQ A field-hosting warning, three-hour nonce lifetime, validation responsibility and pre-modal lookup callback; not current SDK support or deprecation-status, PCI-certification, server-processing or payment-outcome evidence

- [[source-braintree-docs-deprecated-client-side-encryption-javascript-library]] - historical, deprecated Client-Side Encryption JavaScript library for encrypting marked client input before merchant-server forwarding; includes automatic form submission and multiple-handler ordering limits, not current SDK support, PCI/compliance, or payment-outcome evidence

- [[source-braintree-docs-guides-payment-request-setup-and-integration-javascript-v3]] - Braintree-hosted JavaScript v3 Payment Request setup guide covering browser/HTTPS fallback prerequisites, payment-method enablement, component tokenization and server nonce handoff, with Google Pay consent/vaulting cautions and an unresolved direct-link script mismatch; not current availability, merchant eligibility, transaction, settlement or exact-version implementation proof

- [[source-braintree-docs-guides-payment-request-overview]] - 2026-09-16 Braintree website overview of the JavaScript v3 Payment Request browser experience, Hosted Fields alternative framing, snapshot browser/payment-method matrix, and standalone Google Pay route

- [[source-braintree-docs-guides-paypal-paypal-sdk-migration-guide-javascript-v3]] - JavaScript v3 custom PayPal migration guide mapping `checkout.js` v4 to PayPal JS SDK v5 loading, rendering and Checkout/Vault callbacks, with explicit Drop-in and new-integration exclusions; not current package or v6 evidence

- [[source-braintree-docs-reference-client-reference-javascript-v2-configuration]] - historical Braintree.js JavaScript v2 `braintree.setup` configuration snapshot covering client authorization inputs, Drop-in/Custom conditions, readiness and tokenization callbacks, merchant-owned server handoff, and returned-detail eligibility limits; not current-support, runtime-enablement, payment-execution or exact-version GitHub evidence

- [[source-braintree-docs-reference-client-reference-javascript-v2-hosted-fields]] - historical JavaScript v2 Hosted Fields client reference for field events, iframe-internal CSS support and field configuration requirements, including the vaulted-card CVV-only exception; not tokenization, client/server processing, PCI certification, current lifecycle/support, environment availability or payment-outcome proof

- [[source-braintree-docs-reference-client-reference-javascript-v2-best-practices]] - historical Braintree.js JavaScript v2 client best-practices and troubleshooting snapshot covering DOM-order setup, readiness and teardown lifecycle, headless PayPal initiation, environment-split CSP locators, and form-handler bypass; not current SDK support, hosted behavior or exact-version GitHub evidence

- [[source-braintree-docs-reference-client-reference-javascript-v2-paypal]] - JavaScript v2 PayPal client-reference snapshot for Vault and Checkout option/callback routing, including version- and merchant-qualified controls; not current-support or payment-execution proof

- [[source-braintree-docs-guides-fastlane-reference]] - collected unversioned Braintree website reference for Fastlane create configuration, namespace identity/profile actions, card and payment component token interfaces, field locators and accessibility limits; not current hosted-runtime behavior, a comprehensive property inventory or exact-version adapter evidence
- [[source-braintree-hosted-fields-upgrading-from-custom-javascript-v3]] - sparse Custom-to-Hosted-Fields upgrade route whose JavaScript v3 path conflicts with its v2-only availability notice; not migration-procedure or current-support evidence
- [[source-braintree-start-hosted-fields]] - unversioned website start page orienting Hosted Fields' iframe card-entry role, direct client-to-Braintree data path, nonce substitution and integration routes
- [[source-braintree-hosted-fields-examples-javascript-v3]] - JavaScript v3 gallery of Hosted Fields styling and merchant-UI presentation possibilities; examples are not SDK-support or payment guarantees
- [[source-braintree-hosted-fields-styling-javascript-v3]] - JavaScript v3 guide for Hosted Fields styling configuration
- [[source-braintree-hosted-fields-faq-javascript-v3]] - JavaScript v3 Hosted Fields troubleshooting and FAQ snapshot covering CVV-only vaulted-card verification, iframe and form-container behavior, selector requirements, iOS label focus, and sandbox-site limitations
- [[source-braintree-client-sdk-migration-javascript-v3]] - historical JavaScript SDK v2-to-v3 migration route covering the breaking API change, modular client/component model, explicit Hosted Fields tokenization, and Kount Custom pre-migration warning; not current-support or exact-version implementation evidence
- [[source-braintree-paypal-checkout-with-vault-javascript-v3]] - JavaScript v3 Checkout with Vault guide covering request-mode matching, client tokenization, server `Transaction.sale`, the implicit vaulted token and the returning-customer One-time Payments path
- [[source-braintree-paypal-pay-later-offers-javascript-v3]] - JavaScript v3 Pay Later presentation guide covering the PayPal client-side prerequisite, messaging component and amount container, standalone Pay Later funding configuration, and per-button eligibility check

- [[source-braintree-upgrade]] - historical browser-integration routes from Transparent Redirect and old Braintree.js toward Drop-in or client SDK tokenization plus a server-side payment-method nonce handoff, with current lifecycle and availability left to current evidence

- [[source-braintree-tokenization-key-javascript-v3]] - JavaScript client initialization with static, reduced-privilege tokenization keys, including revocation, environment binding, and capability limits

- [[source-braintree-authorization-client-token]] - signed client-token purpose, server-to-client initialization roles, application-communication scope, and stated validity and invalidation boundaries

- [[source-braintree-authorization-overview]] - client-authorization guide comparing client tokens and tokenization keys, qualified capability differences, and selection guidance

- [[source-braintree-hosted-fields-events-javascript-v3]] - JavaScript v3 Hosted Fields event-driven UI state and `getState` field-validity retrieval route

- [[source-github-braintree-web]] — cumulative exact-SHA implementation evidence
- [[changelog-github-braintree-web]] — package-qualified release ledger
- [[braintree-web-drop-in]] - independently versioned prebuilt UI and migration boundary
- [[paypal-braintree-integration]] — PayPal v6 and Braintree nonce-processing boundary
- [[paypal-fastlane]] — delegated Fastlane product concept
- [[card-brand-detection]] - standalone detector behavior and validation boundary
- [[source-github-uuid]] - exact secure UUID generation and runtime boundary
