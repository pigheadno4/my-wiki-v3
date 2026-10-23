---
title: "Manage payment methods in your account"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/add-payment-methods"
raw_files:
  - "adyen/docs/payment-methods/add-payment-methods/2026-09-15.md"
tags: [adyen, payment-methods, customer-area, merchant-account, management-webhooks]
---

## Overview

This 2024-modified, 2026-09-15-captured [[adyen]] Customer Area guide describes requesting, viewing, activating, deactivating and changing country/region settings for **merchant-account payment methods**. It routes through [[adyen-online-payments]]. A request or configured status is separate from Adyen's later store-level creation event and from an actual payment outcome.

## Key takeaways

- Before requesting a method, the page calls for an Adyen **online payments integration and checkout UI**, the Customer Area **Change payment methods** role, and a Payment method webhook subscription in its requirements table. Its later webhook section phrases Management webhook subscription as a recommendation for the asynchronous add-to-store process. Preserve that wording difference rather than assuming a completed subscription or that one notification proves payment capability.
- In **test or live Customer Area**, switch to the merchant account, select methods, apply them to **This merchant account**, supply prompted information, review and submit the request. Adyen may contact the merchant about additional requirements before adding the method. Availability can be delayed by external factors; “typically within a day” and requesting at least one day before opening are estimates/recommendation, not a service guarantee. Default currencies depend on method type; a different currency implementation is routed to Support.
- The page says `paymentMethod.created` is sent **after the method has been added to a user's store**. Its Visa example reports `result: SUCCESS`, `merchantId`, `storeId`, method type and `environment: test`. That example is not proof that a particular merchant account, store, channel, country or live checkout has the method enabled, nor proof of authorization/capture/settlement.
- An immediate **Submit request** error calls for correcting information before resubmitting. In the rare post-submission failure described by the page, an unsubscribed merchant gets no automated failure alert, and the page says to wait **24 hours** before retrying. This is a conditional retry instruction, not evidence that a request failed or succeeded.
- Customer Area also lists configured merchant-account methods, supports **Activate/Deactivate**, and lets users edit country/region including **ANY** for no selected regional restriction. A method marked **Inactive** and unused for **90 days** is automatically deleted. Activation or ANY selection changes configuration; it does not establish actual method eligibility, shopper presentation or successful payment.

## Detail locators

- [[raw/adyen/docs/payment-methods/add-payment-methods/2026-09-15|Pinned raw]], lines 15–31: purpose, prerequisites, role/webhook wording, availability and currency caveat.
- Same raw, lines 34–47: separate test/live Customer Area request and merchant-account application sequence.
- Same raw, lines 49–71: asynchronous store addition and example `paymentMethod.created` payload.
- Same raw, lines 74–78: immediate versus post-submission error and 24-hour retry boundary.
- Same raw, lines 80–109: viewing configured methods, activate/deactivate, 90-day deletion and country/region edit.

## Related

- [[source-adyen-docs-payment-methods]] — catalog/navigation of methods and filters.
- [[adyen-payment-method-variants]] — method type/variant context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/add-payment-methods/2026-09-15|Manage payment methods in your account]]
