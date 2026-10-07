---
title: "Braintree Fastlane Client-side Integration (Node route)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/fastlane/client-side/node"
raw_files:
  - "braintree/docs/guides/fastlane/client-side/node-2026-09-16.md"
tags: [braintree, paypal, fastlane, client-side, javascript, tokenization]
---

## Overview

This collected [[braintree]] webpage, at the exact `/braintree/docs/guides/fastlane/client-side/node` route, describes a browser-side HTML and JavaScript integration for [[paypal-fastlane]]. It connects same-version Braintree Web module initialization and device-data collection to email lookup, member authentication or guest fallback, address handling, payment-component rendering, and a payment-token plus device-data handoff to merchant-server processing. The route name is not evidence of a Node.js runtime implementation, and the snapshot does not establish current availability, merchant eligibility, direct PayPal Orders API behavior, or a successful transaction or Vault result.

## Key takeaways

- The page instructs merchants to load the Braintree client, Fastlane, and data-collector modules at the same version, `3.120.0` or greater; initialize a client and data collector; then create Fastlane with the client token, client instance, device data, and optional styling. It exposes identity, profile, and event handles from the created component.
- After email collection, `identity.lookupCustomerByEmail(email)` checks whether the email is associated with a Fastlane or PayPal member. The page says Fastlane profile information is available only after authentication; its example treats `authenticationState === "succeeded"` as the member experience and failed, cancelled, or no-profile cases as the guest experience. In Sandbox, only the documented `111111` or `222222` OTP values succeed.
- The page says certain countries and regulations require the Fastlane watermark when email is shared with Fastlane. It also identifies PayPal as a data controller and Business under the California Consumer Privacy Act, recommends rendering the Fastlane by PayPal logo and information tooltip, and directs compliance questions to legal advisors.
- A member profile may have no shipping address. The integration must handle that case, allow address selection where applicable, and send the shipping address in the server-side request. Guest users instead enter their information manually through the merchant experience.
- The Fastlane payment component is to be rendered for both members and guests. Guests enter the information needed to generate the payment token; members see their primary method and can switch saved cards. The example obtains the token on order submission and sends it with previously captured device data to the server. The page says the token can be used like a `paymentMethodNonce` to transact or vault, but provides no execution or outcome evidence.

## Detail locators

- **Page identity and snapshot metadata:** raw lines 5–10 give the title, `/docs/guides/fastlane/client-side/node/` slug, create time, and update time.
- **Module and Fastlane initialization:** raw lines 17–81 specify the same-version `3.120.0` minimum, script modules, client/data-collector creation, optional styles/locale/card brands, and identity/profile/event extraction.
- **Watermark and data-sharing notice:** raw lines 83–110 cover placement, the country/regulation qualification, PayPal's stated role, the recommendation and legal-advisor notice, plus the SDK render example.
- **Lookup, authentication, and guest fallback:** raw lines 114–169 cover email lookup, the member/profile-access condition, Sandbox OTP behavior, the authentication example, and the succeeded-versus-guest branches.
- **Member address handling:** raw lines 174–227 cover missing shipping addresses, server-side address submission, member-versus-form rendering, and `showShippingAddressSelector()` result handling.
- **Guest data entry:** raw lines 229–234 state that the guest manually enters information through billing address and card details.
- **Payment component and token acquisition:** raw lines 237–316 cover the always-render rule, guest/member component roles, optional shipping-address/style/field inputs, rendering, and `getPaymentToken()` plus device-data server handoff.
- **Downstream processing route:** raw lines 318–326 say to use the Fastlane payment token like a `paymentMethodNonce` for Transact or Vault and point to server-side integration; these links and statements do not prove a payment or vaulting outcome.

## Related

- [[braintree]]
- [[paypal-fastlane]]
- [[source-braintree-docs-guides-fastlane-reference|Braintree Fastlane Reference Types]]
- [[source-braintree-docs-guides-fastlane-advanced-option|Braintree Fastlane Advanced Options]]
- [[source-braintree-docs-guides-fastlane-flexible-payment|Braintree Fastlane Flexible Payment Integration]]

## Raw Sources

- [[raw/braintree/docs/guides/fastlane/client-side/node-2026-09-16|Braintree Fastlane Client-side Integration — Node route (2026-09-16 snapshot)]]
