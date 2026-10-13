---
title: "Adyen Add POS Payment Methods"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/what-we-support/payment-methods/add-payment-methods"
raw_files:
  - "adyen/docs/point-of-sale/what-we-support/payment-methods/add-payment-methods/2026-09-15.md"
tags: [adyen, point-of-sale, payment-methods, merchant-account, stores, customer-area, management-webhooks]
---

## Overview

This Adyen guide describes how an in-person payments merchant requests additional payment methods in test or live Customer Area and observes their asynchronous addition to a store. It covers Customer Area role, request submission, a Management `paymentMethod.created` webhook, post-submission failure handling, and when terminal configuration picks up an added method. It is a 2026-09-15 webpage snapshot, not a merchant-specific approval, live availability catalog, or proof that a terminal has already updated.

## Key takeaways

- The guide says major global credit and debit cards are supported out of the box. Additional methods must be requested for the merchant account through **Payments > Payment methods > Request payment methods** in test or live Customer Area, filtering by location and type, providing any prompted information, reviewing and submitting. The requirement is a POS integration and the **Change payment methods** Customer Area role. The guide does not enumerate scheme, region, account-contract or terminal-model eligibility for each method; the filtered list and any prompted information are context-specific.
- Adding a method to a store is asynchronous. The requirements table says to subscribe to the **Payment method webhook**, and the Webhooks section recommends Management webhooks so `paymentMethod.created` can report that the method was added. The Visa JSON is explicitly an example with `environment: test`, a store ID and `result: SUCCESS`; it is not a result for the reader's request. An immediate submission error calls for correcting the entered information before resubmitting. In the guide's rare case where a request fails after submission and the merchant has no webhook failure alert, it says to wait **24 hours** before trying again; this is a condition-specific retry instruction, not permission to submit duplicates while a request is pending.
- External factors can delay availability. The guide says methods typically appear within a day and recommends requesting at least a day before opening; neither is a service guarantee. Payment-method currency defaults vary by method type, and the guide directs a merchant with different currency needs to Support.
- Once added, a terminal uses the method after its next configuration maintenance call, or after a manual configuration update for immediate use. Store addition and terminal readiness are separate transitions. This page does not itself describe terminal assignment or boarding, and no success should be inferred for an unboarded or offline terminal.

## Detail locators

- `## Requirements` — POS integration, Customer Area role, payment-method webhook subscription, timing/currency qualifications.
- `## Request payment methods` — test/live Customer Area route, merchant-account switch, location/type filters, prompted details, review and submit.
- `## Webhooks` — asynchronous store addition and `paymentMethod.created` example including test environment, merchant ID, store ID and result.
- `## Troubleshooting` — immediate validation error versus rare post-submission failure and its no-webhook 24-hour wait.
- `## When changes take effect` — terminal maintenance call versus manual configuration update.

## Related

- Company: [[adyen]]
- Store and terminal administration context: [[adyen-pos-store-management]]
- Variant identifiers and method-specific adding table: [[adyen-payment-method-variants]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/what-we-support/payment-methods/add-payment-methods/2026-09-15|2026-09-15 Adyen Add payment methods snapshot]]
