---
title: "MoMo iOS Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/momo-wallet/ios-component"
raw_files:
  - "adyen/docs/payment-methods/momo-wallet/ios-component/2026-09-15.md"
tags: [adyen, momo, ios, components, online-payments, recurring-payments]
---

## Overview

This [[adyen]] guide, captured 2026-09-15, adds MoMo wallet to an **existing iOS Components integration**. It separates Sessions and Advanced flow instructions, uses `InstantPaymentComponent` for the `momo_wallet` method, and includes a recurring-token route and test/live setup. It is a method-specific add-on, not a complete iOS integration or proof of current Vietnam/VND merchant eligibility, successful authorization, capture, settlement, refund or token creation. See [[adyen-online-payments]] and raw lines 15–23.

## Key takeaways

- **Sessions:** Existing iOS Components Sessions flow, Checkout API **v68 or later**, redirect handling for `action.type: redirect`, and Customer Area method addition are prerequisites. No extra `/sessions` or MoMo configuration parameters are stated. The Swift sample checks for `.other("momo_wallet")` in session payment methods, creates `InstantPaymentComponent`, sets the **session** as delegate, and initiates payment. See raw lines 25–69.
- **Advanced:** Existing Advanced iOS Components flow, redirect handling and Customer Area method addition are listed, with no extra MoMo configuration or `/payments` parameters. Its Swift sample checks `momo_wallet`, creates the same Component, sets **self** as delegate and initiates payment. The Advanced requirement text says iOS Components but its integration-type link points to `integration=Drop-in`; follow the Components-specific steps and verify that base-guide link before using it as implementation authority. The Advanced section does not separately state the Sessions v68 minimum. See raw lines 321–364.
- The page says MoMo supports recurring transactions through creating a shopper token, then using it later. For token creation it calls for `storePaymentMethod: true` and a unique `shopperReference` in `/payments`; it says a `recurring.token.created` webhook with `storedPaymentMethodId` arrives **when the initial payment has settled**, and requires the merchant server to receive token lifecycle webhooks. These instructions appear under **both** server-flow sections, including Sessions, yet the Sessions subsection specifically describes a `/payments` request; treat that request route as page wording rather than assuming every Sessions integration calls `/payments` directly. The page does not state shopper-consent handling. See raw lines 72–95 and 366–389.
- Subsequent token payments use the received `paymentMethod.storedPaymentMethodId` (or a value retrieved through `/listRecurringDetails`), the same `shopperReference`, `shopperInteraction: ContAuth`, and `Subscription` for fixed-interval or `UnscheduledCardOnFile` for non-fixed-interval contracts. The TEST examples use `momo_wallet` and VND, which do not establish actual token creation, future authorization or current country/currency support. The Java examples use `setRecurringDetailReference` where the prose and other examples use `storedPaymentMethodId`; do not copy across library versions without checking the intended field. See raw lines 97–163 and 391–457.
- For testing, the page points to MoMo's test app and scenario-specific test credentials and directs checking payment status in Adyen's **test** Customer Area. It separately says a request in the **live** Customer Area is needed before live MoMo acceptance. The test instructions mention mobile-browser app download and desktop QR scanning as testing context; this iOS Component guide does not thereby become a desktop-QR integration guide. Neither a redirect/app return nor a test status lookup by itself proves final payment outcome. See raw lines 310–319 and 604–613.

## Detail locators

- Sessions prerequisites, no extra request/configuration, iOS Component initialization and delegate: raw lines 25–69.
- Sessions recurring requirements and TEST request/library examples: raw lines 72–308. cURL uses Checkout `/v68/payments` and VND as an example; the page's stated v68 minimum belongs to its Sessions prerequisites (lines 33–34).
- Advanced prerequisites, Drop-in-link mismatch, Component initialization and no extra request fields: raw lines 321–364.
- Advanced recurring instructions and repeated language examples: raw lines 366–603. Java `setRecurringDetailReference` versus stated `storedPaymentMethodId`: raw lines 395–403, 446–449.
- Test app, test credentials, Customer Area status and separate live request: raw lines 310–319 and 604–613.

## Related

- [[adyen-online-payments]]
- [[adyen-ios-sdk]]
- [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/momo-wallet/ios-component/2026-09-15|MoMo iOS Component guide — captured 2026-09-15]]
