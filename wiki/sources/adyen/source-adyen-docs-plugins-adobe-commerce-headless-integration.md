---
title: "Adyen Adobe Commerce headless integration"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/adobe-commerce/headless-integration"
raw_files:
  - "adyen/docs/plugins/adobe-commerce/headless-integration/2026-09-15.md"
tags: [adyen, adobe-commerce, headless-checkout, graphql, rest, tokenization]
---

## Overview

This Adyen webpage guides a merchant-built Progressive Web Application storefront using a headless Adobe Commerce back end with the Adyen plugin installed and configured. The storefront sends checkout data through Adobe Commerce to Adyen and handles returned status or shopper actions. The page documents REST and GraphQL routes; GraphQL requires plugin v8.2.0 or later. It is an unversioned guide captured in 2026, with older last-modified metadata and version-specific notes. Use [[adyen-magento2]] for the separately version-qualified repository baseline, not as proof that this guide's examples ran on a particular merchant installation. [[adyen]]

## Key takeaways

- Before checkout integration, configure the Adyen Customer Area, Adobe Commerce plugin, payment methods, and headless settings. In-person setup is not required for the PWA storefront. The guide recommends Web Components for secure payment-data collection. Adobe Commerce authentication uses `self` routes for logged-in shoppers and `anonymous` routes for guests; it states a shopper Bearer customer token is used for logged-in requests, while the guest route uses a masked `card_id` without a token, as named in this page. It says an integration token is no longer required for these front-end requests.
- Retrieve session-available methods through the Adobe Commerce back end, which calls Adyen `/paymentMethods`. The REST `/payment-information` or `/shipping-information` response includes `adyen_payment_methods_response` as a JSON-encoded string; parse it for `paymentMethodsResponse` and plugin-added `paymentMethodsExtraDetails`. GraphQL uses `adyenPaymentMethods` through `/graphql`. Availability is filtered by the session's amount, currency, country or region and other context; example cards, wallets and alternative methods do not establish live account eligibility. `isOpenInvoice` is marked deprecated.
- The merchant storefront collects the selected method's required details, places an Adobe Commerce order that causes a back-end Adyen `/payments` request, checks `payment-status` or `adyenPaymentStatus`, and handles a nonempty `action` or later details response. REST and GraphQL payloads differ; GraphQL `placeAdyenOrder` combines `setPaymentMethodOnCart` and `placeOrder`. The guide's `cc_type` note says plugin v11.0.0 stores the card type in payment `ccType` rather than `additional_information.cc_type`; `brand_code` is marked only for v9.
- Status presentation is conditional: `Authorised` or `Received` is a success-page route in the guide, `PresentToShopper` presents a voucher or QR code, and `Cancelled`, `Refused`, `Error` or unhandled results require their stated handling. An `action` can still require shopper work; `isFinal` and a success-page redirect are checkout-state guidance, not proof of capture, final settlement, or bank receipt. The PayPal Component uses `handleAction` instead of the `createFromAction` method described for other methods. The plugin handles webhooks, while the storefront owns the described action flow.
- The separate REST `state-data` endpoint is supported from plugin v7.2.0 for flows unable to send `state.data` through `/payment-information`. It persists payment data and the guide warns of possible PCI-scope implications. GraphQL gift-card checkout adds balance-check, save/remove state-data, and redemption steps; whether to place the order as gift card or with another method depends on gift-card balance versus cart amount.
- Headless tokenization uses Adobe Commerce Vault after Vault setup. Alternative methods are tokenized only when enabled; cards require `enableStoreDetails: true` in the Card Component, which shows a shopper save checkbox. The guide maps stored token identifiers in `vault_payment_token` and directs server-side `POST /token/deactivate` with matching `customerId` for removal. These settings and example payloads do not establish shopper consent, actual stored-token creation, or a successful live payment.

## Detail locators

- Opening, `## Ecommerce checkout flow`, and `## Requirements`, lines 23–68: PWA/back-end scope, REST/GraphQL version floor, sequence, configured prerequisites, and shopper authentication.
- `## Step 1`, lines 70–263: REST/GraphQL payment-method routes, response parsing, session filters, added details, and deprecated `isOpenInvoice`.
- `## Step 2`, lines 264–279: merchant-built form, shopper detail collection, and Web Components recommendation.
- `## Step 3`, lines 280–501: REST/GraphQL order payloads, recurring model and v9/v11 field qualifications, `state-data` endpoint and PCI warning.
- `## Step 4` and `## Step 5`, lines 503–611: payment-status fields, conditional result/action handling, PayPal exception, details endpoints, and webhook note.
- `## Gift card payments`, lines 613–777: extra GraphQL balance, state-data, redemption and partial-payment conditions.
- `## Tokenization` and `## Troubleshooting`, lines 779–825: Vault, method-specific enablement, token removal, and plugin/PHP-library/API-version matching.

## Related

- [[adyen-magento2]] — Adyen Adobe Commerce plugin concept and exact-version repository evidence.
- [[source-github-adyen-magento2]] — separately version-qualified implementation baseline.
- [[adyen-tokenization]] — broader stored-payment-method context.

## Raw Sources

- [[raw/adyen/docs/plugins/adobe-commerce/headless-integration/2026-09-15|Adyen Adobe Commerce headless integration guide, fetched 2026-09-15]]
