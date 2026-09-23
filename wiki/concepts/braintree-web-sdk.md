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

## Versioned Evidence

The first retained baseline is `braintree-web@3.143.0` at SHA `bae582d791026c143abb91c3bdcada92b8c060f6`. Release `3.144.0` at SHA `41460fba05c1ea1222e795b36a10765a6699b8e7` adds PayPal funding-instrument editing, v6 session options, and the Venmo detection fallback. The latest retained release is `3.145.0` at SHA `732ed094354d650605e678d98246ce6332952ad3`; both earlier baselines remain in the cumulative source and changelog.

## Checkout and Recovery Changes in 3.145.0

- PayPal Checkout v6 distinguishes billing-token-only vaulting from checkout-with-vault. The latter sends the billing token together with order/payment and payer identifiers. `implicitlyVaultedPaymentMethodToken` is exposed only if the gateway returns it; an upgrade does not guarantee vault success.
- Venmo desktop QR forwards requested billing/shipping-address flags through the modern `paymentMethodUsage` payment-context mutation. Requesting either flag requires `enrichedCustomerDataEnabled`; otherwise creation rejects with `VENMO_ECD_DISABLED`. The legacy QR mutation does not forward those flags. The refreshed QR modal adds rescan handling and custom fonts.
- Deferred client script loading retries once with forced reload after an initial load rejection. PayPal vault-initiated checkout and LocalPayment popup paths add suspend/resume observation and delayed close checking. Recovery analytics is not proof of tokenization, authorization, or settlement.
- FraudNet load failures become observable in analytics; Fastlane preserves underlying error detail. Dependencies change to `@braintree/asset-loader@2.1.0` and add `qrcode@1.5.4`.

These are changes in the Braintree adapter and retained browser implementation, not proof of changes in independently hosted PayPal/Fastlane runtimes. Source: [[source-github-braintree-web]]; release comparison: [[changelog-github-braintree-web]].

## Related

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
