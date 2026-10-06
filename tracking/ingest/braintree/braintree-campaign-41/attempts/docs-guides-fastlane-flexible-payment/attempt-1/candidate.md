---
title: "Braintree Fastlane Flexible Payment Integration"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/fastlane/flexible-payment"
raw_files:
  - "braintree/docs/guides/fastlane/flexible-payment-2026-09-16.md"
tags: [braintree, paypal, fastlane, web-sdk, client-side, guest-checkout, tokenization]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website guide describes the client-side Flexible Integration for PayPal Fastlane through the Braintree Web SDK. Compared with the guide's Quick Start path, the merchant takes responsibility for rendering member card details, integrating the saved-card selector, collecting a guest's billing address, and rendering the Card Component for guests or authenticated members without a saved card. The page documents token acquisition and a server handoff; it is not exact-version GitHub implementation evidence or proof of current availability, merchant eligibility, authorization, settlement, vault success or funding.

## Key takeaways

- Initialization requires the Braintree client, Fastlane and data-collector modules at the same version, with this snapshot stating `3.120.0` or greater. The client instance, device data and client token feed Fastlane initialization. This is website-guide setup, not evidence about the retained `braintree-web` repository snapshot or a guarantee that any later version is currently supported.
- After email lookup, a Fastlane or PayPal member must successfully complete the authentication flow before the integration uses returned profile data. A failed or cancelled authentication, or no matching profile, routes to the guest experience. The guide states fixed successful OTP values only for Sandbox; that fixture must not be carried into Production.
- Flexible Integration leaves more checkout UI and state handling with the merchant. For an authenticated member, the merchant renders returned shipping/card information, updates its site when a selector changes, sends the shipping address in the server-side request, and handles missing saved addresses or cards. When no saved card is available, the merchant renders the Card Component.
- For a guest, the merchant collects shipping and billing addresses and calls `getPaymentToken()` with the customer's name and billing address. For a member with a selected saved card, the returned card identifier supplies the payment token. The page says the resulting Fastlane payment token can be used like a `paymentMethodNonce` for a transaction or Vault request, but token generation and handoff are not authorization, settlement, vault completion or funding.
- Sharing an email with Fastlane can require the Fastlane watermark under applicable country or regulatory rules. The guide also directs the merchant to render the watermark with member shipping and card details. Exact regulatory applicability and the linked advanced guidance remain outside this fully read page.

> [!warning] Environment, eligibility and execution boundary
> The fixed OTP values on this page are expressly Sandbox-only. Member-profile access depends on successful authentication, and saved shipping/card data may be absent. This collected website snapshot does not prove current Fastlane availability, account enablement, Production eligibility or parity, or successful payment/vault execution. Treat the token as payment-method input passed to the merchant server, not as evidence that a transaction was authorized, submitted for settlement, settled or funded.

## Detail locators

- Flexible-versus-Quick-Start purpose and merchant-owned billing, card rendering/selection and token responsibilities: `# Flexible Integration > #### Quick Start vs Flexible Integration`, raw lines 14-34.
- Required Braintree Web modules, same-version condition and stated `3.120.0` minimum: `# Client-side Integration > #### Step 1`, raw lines 37-52.
- Client, data collector, device data, styling/locale/card-brand options, Fastlane initialization and exposed identity/profile/events: `#### Step 2`, raw lines 54-104.
- Email-sharing watermark condition and rendering example: `#### Step 3`, raw lines 106-131.
- Email lookup, member authentication, Sandbox-only OTP values, success condition and guest fallback: `#### Step 4`, raw lines 135-190.
- Member shipping rendering, missing-address handling, site update, server-side shipping-address instruction and address-selector example: `#### Step 5 > ##### Render Shipping Address`, raw lines 195-272.
- Missing-card fallback, member card rendering and card-selector state update: `#### Step 5 > ##### Card details` and `##### Card Selector`, raw lines 274-317.
- Guest shipping/billing collection, Card Component render condition and routine field/style examples: `#### Step 6` through `##### Render Card Component`, raw lines 319-384.
- Guest billing-address token call, selected-card token branch, server handoff and transaction/Vault navigation: `##### Generate Fastlane Payment Token`, raw lines 386-420.

## Related

- Company: [[braintree]]
- Main concept: [[paypal-fastlane]]
- Braintree browser SDK boundary: [[braintree-web-sdk]]

## Related raw API references

The page links to separate Fastlane Quick Start, reference, advanced-options, transaction-sale and payment-method-create pages. Those targets were not read as evidence for this entry; they provide navigation only and do not establish current configuration options, eligibility, regulatory applicability, request-schema completeness, or successful transaction or Vault execution.

## Raw Sources

- [[raw/braintree/docs/guides/fastlane/flexible-payment-2026-09-16|Braintree Fastlane Flexible Payment Integration]] - fully read pinned website snapshot covering the client-side Flexible Integration, member/guest responsibilities, authentication, Card Component token acquisition and server handoff
