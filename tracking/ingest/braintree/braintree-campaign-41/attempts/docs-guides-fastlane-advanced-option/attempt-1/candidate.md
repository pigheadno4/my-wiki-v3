---
title: "Braintree Fastlane Advanced Options"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/fastlane/advanced-option"
raw_files:
  - "braintree/docs/guides/fastlane/advanced-option-2026-09-16.md"
tags: [braintree, fastlane, javascript, payment-token, shipping, vaulting]
---

## Overview

This collected Braintree Fastlane advanced-options page combines browser/component configuration with a flexible checkout template. Its central payment path selects an authenticated member's saved card when one is available, otherwise renders `FastlaneCardComponent`; the browser obtains a `paymentToken` and sends it with previously captured device data to the merchant server to complete checkout. The token handoff is not itself processor authorization, capture, settlement or funding.

This is a 2026-09-16 website snapshot. It does not establish current Fastlane availability, merchant enablement, buyer eligibility, SDK compatibility, successful component rendering or successful payment execution. The Braintree server examples on this page use Braintree gateway routes and must not be restated as the direct PayPal Orders API pattern documented for another Fastlane integration.

## Key takeaways

- The flexible template branches on both successful member authentication and a saved card. In that branch it renders the selected card, Fastlane watermark and card-change control; guests, failed authentications and profiles without a card instead render Fastlane card fields. Card selection returns a `paymentToken` through the selected card's `id`, while the card component calls `getPaymentToken` with a billing address. In both cases the merchant must still send the token and device data to its server for checkout processing.
- The page's shipping heading says "Only supports US addresses," but its body is narrower: Fastlane availability is limited to US billing addresses, while the shipping address may be any destination the merchant site supports. A newly entered address must be sent in the server-side `transaction.sale()` request. Do not turn the heading into a US-only shipping restriction.
- Store pickup requires the transaction's shipping method to be `pickupInStore` or `shipToStore`; the stated purpose is to avoid creating buyer profiles with the merchant store's address as the buyer's shipping address.
- Vaulting is optional, not an automatic consequence of receiving a Fastlane `paymentToken`. The page offers two server-side routes: `store_in_vault_on_success` on `transaction.sale()` for transact-and-vault, or customer/payment-method creation to vault first and transact later. Neither route guarantees vault success or a later successful payment.
- PayPal members without a Fastlane profile need no additional integration branch according to this page: the client SDK returns a `customerContextId`, presents an opt-in call to action during authentication, and returns either normal `profileData` after consent or an empty object that the merchant handles as a guest. This is client-flow behavior from the snapshot, not proof that a particular buyer will be eligible or consent.

> [!warning] Client token and payment outcome boundary
> A Fastlane `paymentToken` obtained from a selected card or `FastlaneCardComponent` is an input to subsequent merchant-server processing. It is not a processor authorization, capture, settlement or funding result, and optional vaulting requires a separate server-side action.

> [!warning] Snapshot and integration-family boundary
> This captured Braintree guide does not prove current product availability, account enablement, SDK support or live execution. Keep its Braintree `transaction.sale()` and customer/payment-method routes distinct from direct PayPal Orders API Fastlane examples.

## Detail locators

- Content Security Policy instruction, Hosted Card Fields exception and exact PayPal/Braintree allowlist directives: `##### Configure your Content Security Policy`, raw lines 16-35.
- Locale setting after Fastlane initialization and the page's exact language values: `##### Specify locale`, raw lines 36-51.
- Watermark variants, `includeAdditionalInfo`, render target and progressive tooltip behavior: `#### Rendering Fastlane Watermark`, raw lines 54-103.
- Optional but strongly recommended watermark preloading and exact asset examples: `##### Optimization: Preload watermark assets`, raw lines 104-113.
- US-billing versus merchant-supported shipping scope, reference navigation and newly added address handoff to `transaction.sale()`: `### Shipping Address Guidelines`, raw lines 115-124.
- Saved-card/member-authentication branch, guest/failure/no-card branch, card-field option examples and rendering: `**Flexible Integration Template**`, raw lines 126-178.
- Card-selector result handling, selected-card `id`, `getPaymentToken` billing-address call and token/device-data server handoff: flexible-template JavaScript, raw lines 180-218.
- Recommended server request fields and linked field references: `**Recommended Fields for server-side API call**`, raw lines 220-226.
- Store-pickup shipping-method safeguard: `### Store pick-up Integration`, raw lines 229-235.
- Optional transact-and-vault versus vault-and-transact routes: `### Vaulting`, raw lines 236-246.
- Client SDK handling of PayPal members without a Fastlane profile, including opt-in and guest dismissal outcomes: `## PayPal Members without a Fastlane Profile`, raw lines 247-256.

## Related

- Company: [[braintree]]
- Main concept: [[paypal-fastlane]]
- Braintree browser adapter boundary: [[braintree-web-sdk]]

## Related raw API references

- [[raw/braintree/docs/guides/fastlane/best-practices-2026-09-16|Braintree Fastlane best practices]] - linked navigation only; not read as behavioral evidence for this entry
- [[raw/braintree/docs/guides/fastlane/reference-2026-09-16|Braintree Fastlane reference]] - linked navigation only; not read as behavioral evidence for this entry

## Raw Sources

- [[raw/braintree/docs/guides/fastlane/advanced-option-2026-09-16|Braintree Fastlane advanced options]] - complete collected snapshot for browser/component options, the flexible token handoff template, shipping and store-pickup conditions, optional vaulting and no-profile handling
