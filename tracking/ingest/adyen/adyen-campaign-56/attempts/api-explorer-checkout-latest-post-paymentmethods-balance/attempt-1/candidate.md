---
title: "Adyen Checkout API v72: POST /paymentMethods/balance"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/post/paymentMethods/balance"
raw_files:
  - "adyen/api-explorer/Checkout/latest/post/paymentMethods/balance/2026-09-15.md"
tags: [adyen, checkout-api, gift-cards, balance-inquiry]
---

## Overview

Captured API Explorer reference for Checkout API `POST /paymentMethods/balance`: retrieve the remaining balance on a shopper's gift card by sending its details in `paymentMethod`. The page shows the test server at `https://checkout-test.adyen.com/v72`; `latest` in the URL does not establish a newer version or live availability. This is a balance inquiry, not evidence of payment authorization or capture. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The request table marks `amount`, `merchantAccount`, and `paymentMethod` required. The nested `amount.currency` and `amount.value` are marked required within `amount`; `paymentMethod` contains the method type and method-specific details. The page does not separately state whole-body requiredness. The request examples use Givex card details and show a EUR 10 request beside a EUR 100 not-enough example; examples are illustrative, not universal card-field rules.
- A 200 response has a required `balance` object with currency and minor-unit value and a required `resultCode`. `Success` means the balance check succeeded; `NotEnoughBalance` commonly means the card balance is below the requested amount or its currency differs; `Failed` means the check failed. Optional `transactionLimit` is the maximum spendable amount for one transaction for some gift cards. An HTTP 200 alone therefore does not mean enough balance or a completed payment.
- The response table calls `resultCode` the result of a "cancellation request" even though the endpoint title, description and enum explanations describe a balance check. Treat that label as an internal source inconsistency, not a cancellation operation. The optional `refusalReason` wording also discusses authorization; this reference alone does not establish authorization semantics for the balance inquiry.
- The documented non-200 cases are 400 unreadable request, 401 authentication required, 403 insufficient permissions, 422 validation error and 500 server processing failure. The listed error fields are optional in the schema.

## Detail locators

- Purpose, test v72 server and idempotency header: pinned raw lines 5–17.
- Full request schema, including conditional fields and nested requiredness: pinned raw lines 20–258. Gift-card examples: lines 260–292.
- 200 response schema and result values: pinned raw lines 293–316. Error schemas: lines 319–386. Response examples: lines 388–477.

## Related

- [[adyen-online-payments]] — provider online-payment concept and source route.
- [[adyen-pos-gift-cards]] — separate Terminal API gift-card context; its POS behavior does not govern this Checkout endpoint.

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/post/paymentMethods/balance/2026-09-15|Checkout API POST /paymentMethods/balance captured 2026-09-15]]
