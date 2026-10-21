---
title: "Adyen Marketplace: Request payment methods"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/payment-methods/add-payment-methods"
raw_files:
  - "adyen/docs/marketplaces/payment-methods/add-payment-methods/2026-09-15.md"
tags: [adyen, marketplaces, platforms, payment-methods, customer-area]
---

## Overview

This 2026-09-15 Marketplace guide explains how a platform requests payment methods that its user can accept for a merchant account in the TEST or LIVE Customer Area. Adyen may contact the requester about additional requirements before adding a method. The guide describes a merchant-account request and later store-level webhook event, not proof that a method is already configured or usable. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- **Prerequisites and scope:** The guide requires an Adyen online-payments integration and checkout UI, the Customer Area **Change payment methods** role, and a **Payment method webhook** subscription. A method must support the relevant currency and integration. Its currency is set by default for that method type; contact Adyen Support if the implementation needs a different currency (raw lines 21–32).
- **Request path:** In the TEST or LIVE Customer Area, switch to the merchant account, open **Payments > Payment methods**, choose **Request payment methods**, filter by location/type, select methods, apply them to **This merchant account**, provide prompted information, review, and submit. Submission is a request; Adyen says external factors can delay availability and methods typically appear within a day, so it recommends requesting at least one day before opening (raw lines 19, 30–31, 35–48).
- **Asynchronous outcome:** The webhook section recommends Management webhooks because adding a method to the user's store is asynchronous; after addition it says Adyen sends `paymentMethod.created`. Its illustrative TEST Visa payload has `merchantId`, `storeId`, `data.result: SUCCESS`, and `type: visa`. The earlier requirements table calls for a “Payment method webhook,” while this section calls Management-webhook subscription a recommendation; the page does not resolve whether these names specify the same subscription setting (raw lines 28–29, 50–73).
- **Failure and retry boundary:** Correct an immediate submission error before resubmitting. The page separately warns that a rare post-submission failure may have no automated alert without webhook subscription, and says to wait 24 hours before trying again in that case. A submitted request or example success event does not demonstrate a specific account's payment-method availability or payment acceptance (raw lines 75–79).

## Detail locators

- Merchant-account purpose, prerequisites, support/currency limits and typical availability: pinned raw lines 17–32.
- TEST/LIVE Customer Area request sequence: pinned raw lines 35–48.
- Asynchronous store-level Management webhook and illustrative Visa payload: pinned raw lines 50–73.
- Immediate error versus later silent failure and 24-hour retry instruction: pinned raw lines 75–79.
- Related management paths: pinned raw lines 81–85.

## Related

- [[adyen-platforms]] — main marketplace/platform integration context.
- [[source-adyen-docs-marketplaces-payment-methods-manage-payment-methods-api]] — managing configured methods by Management API; a separate operation.
- [[adyen-webhooks]] — general event-handling route.

## Raw Sources

- [[raw/adyen/docs/marketplaces/payment-methods/add-payment-methods/2026-09-15|Add payment methods, captured 2026-09-15]]
