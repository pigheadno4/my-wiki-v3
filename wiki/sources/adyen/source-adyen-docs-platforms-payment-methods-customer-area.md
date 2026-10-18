---
title: "Manage payment methods in Customer Area | Adyen for Platforms"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/payment-methods/customer-area"
raw_files:
  - "adyen/docs/platforms/payment-methods/customer-area/2026-09-15.md"
tags: [adyen, platforms, payment-methods, customer-area, account-holders]
---

## Overview

This 2026-09-15-last-modified [[adyen]] for Platforms guide explains how a platform requests and manages payment methods for users' stores through Customer Area under a merchant account. It distinguishes method request/addition and enabled configuration from the account holder's ability to use the method. After Adyen enables a method, the page says its variants are accepted by default, subject to method, currency, integration and account-holder conditions. This snapshot is not proof of a live method grant, authorized payment, legal seller or merchant-of-record role, or funds movement. [[adyen-platforms]]

## Requirements and request state

- The stated prerequisites are an Adyen online or point-of-sale integration, the Customer Area **Change payment methods** role, a payment-method webhook subscription, and an already-created business line and user store. A method must be supported for the currency and integration; some, such as SEPA Direct Debit, may only be available through the Management API. These conditions do not establish a given merchant/store's actual eligibility. See raw lines 29–43.
- In test or live Customer Area, the operator switches to the merchant account, chooses **Payments > Payment methods**, filters and selects a method, applies it to a user's store, supplies prompted details and submits the request. Addition is asynchronous. The `paymentMethod.created` Management webhook follows when a method has been added to the store; the sample `SUCCESS` event is a test example, not evidence of the user's usable acceptance state. The guide says availability typically appears within a day and recommends requesting at least a day before opening, rather than promising activation by then. See raw lines 45–83 and 38–41.
- If **Submit request** immediately shows an error, the page says to correct the information before resubmitting. In the rare case of a post-submission failure without webhook subscription, no automated failure alert arrives; in that case it instructs waiting **24 hours** before retrying. This is a conditional retry instruction, not a general request delay or a guarantee of success. See raw lines 85–89.

## Usability, management and removal

- A requested payment method is enabled for the user by default, but only verified account holders can use configured methods. For `receivePayments`, the page requires `verificationStatus: valid`, `enabled: true` and `allowed: true`; it also says a user cannot use a requested method when `allowed` is not true. A legal-entity or account-holder update after verification may disable methods until reverification. Check the account holder through GET `/accountHolders/{id}` or `balancePlatform.accountHolder.updated`; sample account-holder payloads are test examples. See raw lines 91–201.
- The Customer Area list is at merchant-account scope and supports filtering/table columns and a method detail panel. The operator can select methods and **Activate** or **Deactivate** them. Methods marked **Inactive** and unused for **90 days** are automatically deleted; methods linked to a closed store become Inactive and are deleted after 90 days. See raw lines 203–220.
- The page's introduction lists currency updates, but its detailed Customer Area edit steps only change **Country/Region**, including an **ANY** choice without a country restriction. Its requirements text says to contact Support when a nondefault currency is needed. Do not infer an in-page currency edit or universal country/method eligibility from the country selector. See raw lines 21–27, 38–43 and 221–233.

## Detail locators

- **Variant default, page scope, role/webhook and store/business-line prerequisites:** raw lines 19–43.
- **Merchant-account request steps, asynchronous addition and test `paymentMethod.created` example:** raw lines 45–83.
- **Immediate error versus conditional 24-hour retry:** raw lines 85–89.
- **Account-holder `receivePayments` states, reverification and GET/webhook status routes:** raw lines 91–201.
- **Merchant-scope listing, activation/deactivation, 90-day deletion and country/region edit:** raw lines 203–233.

## Related

- [[adyen-platforms]]
- [[source-adyen-docs-platforms-payment-methods-api]] — separate Management API route with its own request/status rules

## Raw Sources

- [[raw/adyen/docs/platforms/payment-methods/customer-area/2026-09-15|Adyen Platforms Customer Area payment-method guide — collected 2026-09-15]]
