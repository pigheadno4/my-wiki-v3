---
title: "Braintree PayPal Vaulted Payments for iOS v7"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/vault/ios/v7"
raw_files:
  - "braintree/docs/guides/paypal/vault/ios/v7-2026-09-16.md"
tags: [braintree, paypal, vault, ios, sdk-v7]
---

## Overview

This collected [[braintree]] website guide documents PayPal vaulted payments through the Braintree iOS v7 documentation route. It describes tokenizing a PayPal vault request to obtain a payment-method nonce for server-side transaction creation, so the PayPal account can be charged later without the customer being present or re-authenticating. This Braintree nonce flow is routed under [[paypal-vault]] without treating it as direct PayPal Payment Method Tokens or Orders API vaulting. The snapshot does not establish current SDK support, merchant enablement, buyer eligibility or successful payment execution.

## Key takeaways

- The Swift example creates `BTPayPalVaultRequest`, optionally supplies a billing-agreement description, and calls `BTPayPalClient.tokenize`. A successful result exposes a nonce that the example directs the integration to send to its server to create a transaction; errors and buyer cancellation are separate outcomes.
- The page carries a dated mobile-certificate warning: it says certificates were set to expire on March 30, 2026, directs iOS integrations to SDK `6.17.0+`, and says traffic from app versions left on older certificates will fail. This iOS-v7-routed snapshot was fetched after that stated date; it preserves the warning as captured rather than proving current certificate or SDK status.
- Device-data collection is required when initiating a non-recurring transaction from a Vault record. The linked Premium Fraud Management Tools route is iOS v6; it is navigation, not evidence read for this entry.
- The brief Vault page says that after `tokenize` the SDK attempts App Switch when the PayPal app is installed and the user meets eligibility requirements, with `ASWebAuthenticationSession` fallback when the switch cannot be completed. This does not mean every vault tokenization automatically attempts App Switch: the fully read dedicated [[source-braintree-docs-guides-paypal-app-switch-ios-v7]] beta/setup guide requires a `BTPayPalVaultRequest` to opt in with `enablePayPalAppSwitch: true` and `userAuthenticationEmail`, and its dated eligibility section limits the feature to US merchants, US customers and custom client-side integrations. That dedicated source is the authority for setup detail; neither page establishes current availability, environment operability, enablement or execution. The Vault page's own App Switch link literally routes to iOS v6 and remains unread navigation.
- Shipping addresses may or may not be collected during the Vault flow. The transaction amount and currency are not displayed in the Vault flow, so the merchant must display them elsewhere in checkout.

## Detail locators

- `Launch the flow` (raw lines 53-60): optional user-authentication email on `BTPayPalVaultRequest`.
- `Invoking the Vault flow` (raw lines 62-93): `BTPayPalClient` authorization, request construction, tokenization, nonce handoff, error and cancellation branches.
- `Collecting device data` (raw lines 95-97): device-data requirement for non-recurring transactions initiated from Vault records and the linked iOS v6 guide route.
- `App Switch` (raw lines 100-123): the Vault page's broad installed-app/user-eligibility attempt statement, `ASWebAuthenticationSession` fallback, app-load initialization note and literal iOS v6 navigation link; not evidence that all tokenizations attempt App Switch. For iOS v7 beta opt-in and eligibility conditions, use [[source-braintree-docs-guides-paypal-app-switch-ios-v7]] (`ELIGIBILITY`, its raw lines 29-40; `Opt In to The App Switch Flow`, its raw lines 203-205).
- `Shipping address`, `Country and language support`, and `Currency presentment` (raw lines 126-138): optional address collection, captured geographic statement, and merchant responsibility to display amount and currency.

## Related

- [[braintree]]
- [[braintree-ios-sdk]]
- [[paypal-vault]]
- [[source-braintree-docs-guides-paypal-app-switch-ios-v7]]

## Raw Sources

- [[raw/braintree/docs/guides/paypal/vault/ios/v7-2026-09-16|Braintree PayPal Vaulted Payments — iOS v7 (2026-09-16 snapshot)]]
