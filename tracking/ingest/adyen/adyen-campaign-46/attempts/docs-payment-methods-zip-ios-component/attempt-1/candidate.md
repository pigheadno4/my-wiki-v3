---
title: "Adyen Zip iOS Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/zip/ios-component"
raw_files:
  - "adyen/docs/payment-methods/zip/ios-component/2026-09-15.md"
tags: [adyen, zip, ios, components, redirect, tokenization, recurring]
---

## Overview

This [[adyen|Adyen]] page, fetched and marked last modified 2026-09-15, adds the Zip redirect payment method to an existing **iOS Components** integration. It covers Sessions as the default for Components v5.0.0 or later, a `/payments` path for an additional use case, version-specific Component setup, and a recurring-token path. See [[adyen-online-payments]]. The examples are TEST requests and do not establish current merchant eligibility or a completed payment.

## Key takeaways

- **Prerequisites and API branches:** Build the base iOS Components integration and add Zip in the **test** Customer Area first. The `/sessions` tab is the default with Components v5.0.0+; `/payments` is presented for an additional use case. Both API parameter tables list shopper name, email, birth date, phone, billing and delivery addresses, and line items with blank **Required** cells. Treat those as documented parameters, not as a claim that every field is mandatory. A line item may include an `imageURL` up to 500 characters for the Zip product page. Only the `/payments` table adds `paymentMethod.clickAndCollect: true` for pickup rather than delivery.
- **Examples and redirect:** The examples show TEST Checkout `/sessions` v71 and `/payments` v72 with AU/AUD and an iOS app-scheme `returnUrl` of `my-app://adyen`. These are examples, not a complete market matrix or a reusable app scheme. The `/payments` example response contains `resultCode: RedirectShopper` and `action.type: redirect`; its action is used to redirect the shopper. The return URL or redirect response is not proof of authorization, capture, or settlement.
- **Component versions:** For iOS Components v5.0.0+, the guide checks for payment method type `zip`, creates `InstantPaymentComponent`, assigns the session as delegate in Sessions or the app's delegate in Advanced, then calls `initiatePayment()`. Its v4.x.x example uses the older generic `Component` and presents it. It says there is no Zip-specific Component configuration.
- **Recurring token path:** The page says Zip recurring transactions are supported. To create a token, send `storePaymentMethod: true` and `shopperReference` in an initial `/payments` request; after the payment has settled, consume the `recurring.token.created` webhook and its `storedPaymentMethodId`, with the server configured for recurring-token lifecycle events. A subsequent `/payments` request uses that stored ID, the same shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` or `UnscheduledCardOnFile`. Token creation is not synchronous with the redirect or initial request. The older Java recurring example uses `recurringDetailReference` while prose and current curl use `storedPaymentMethodId`; follow the versioned API model rather than copying across SDK generations.
- **Sample and live boundaries:** The `/payments` curl sample embeds an unrendered `{hint:...}` marker in JSON around `clickAndCollect`, so it is not copy-ready. Some recurring examples use an HTTPS web `returnUrl` despite this iOS guide's app-scheme examples; configure return handling for the actual app and flow. Testing uses Zip test accounts and Adyen test Customer Area status; live acceptance requires a separate request for Zip in the **live** Customer Area.

## Detail locators

- Identity and requirements: pinned raw lines 15–26. `/sessions` table and v71 AU/AUD request: lines 32–101; language SDK examples: lines 103–679.
- `/payments` field table, pickup flag and v72 AU/AUD sample: lines 681–755; language SDK examples and redirect action: lines 757–1389.
- iOS Components v5 Sessions/Advanced and v4 code: lines 1391–1446. Recurring token creation, webhook, future payment fields and examples: lines 1448–1679. TEST and live setup: lines 1681–1693.

## Related

- [[adyen-online-payments]] — provider integration concept

## Raw Sources

- [[raw/adyen/docs/payment-methods/zip/ios-component/2026-09-15|Zip iOS Component guide, fetched 2026-09-15]]
