---
title: "Adyen Make Token Payments"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/tokenization/make-token-payments"
raw_files:
  - "adyen/docs/online-payments/tokenization/make-token-payments/2026-09-15.md"
tags: [adyen, tokenization, recurring-payments, card-on-file]
---

## Overview

This [[adyen|Adyen]] guide explains how an online-payments integration can reuse an already-created token for a returning shopper's one-click payment, a subscription charge, or an unscheduled card-on-file charge such as an automatic top-up. Shopper-initiated `CardOnFile` payments can use `/sessions` or `/payments`; merchant-initiated `Subscription` and `UnscheduledCardOnFile` payments use `/payments`. It belongs with [[adyen-tokenization]].

## Key takeaways

- The integration needs the Checkout webservice and Merchant Recurring API credential roles, support for recurring payments on the selected payment method, stored shopper details, and a subscription to Recurring tokens life cycle events.
- One-click is shopper-initiated and uses `CardOnFile`. The request includes the token and the same shopper reference used when creating it; with `/payments`, the guide sets `shopperInteraction` to `ContAuth` and `recurringProcessingModel` to `CardOnFile`.
- Subscription and unscheduled card-on-file charges are merchant-initiated. The server sends `/payments` with the stored-payment-method token, matching shopper reference, `ContAuth`, and the corresponding `Subscription` or `UnscheduledCardOnFile` processing model. The guide states that `/sessions` cannot be used to make these subsequent charges.
- Payment outcome evidence comes from the `AUTHORISATION` webhook; for merchant-initiated charges, the `/payments` response is also an outcome route. Example responses and an `Authorised` result do not prove a real transaction succeeded.
- Some issuers can require SCA for `ContAuth` plus `CardOnFile`. For card one-click payments through `/payments`, the CVC is conditional on account setup; the guide explicitly says not to store it because doing so violates PCI compliance rules.
- Before live use, enable Recurring tokens life cycle events in the live Customer Area and complete the tokenization end-to-end testing checklist.

## Detail locators

- `Requirements` — integration type, credential roles, lifecycle webhook, `/sessions` limitation, recurring-payment-method setup, and PSD2/SCA preparation.
- `How it works` — definitions and high-level routes for one-click, subscription, and unscheduled card-on-file payments.
- `Make a one-click payment` → `Tab: /sessions` and `Tab: /payments` — server request fields, stored-method presentation, CVC/PCI warning, SCA qualification, versioned examples, and outcome webhook.
- `Make a subscription or unscheduled card-on-file payment` — `/payments` fields, API-version qualification, examples, response fields, and webhook outcome.
- `Test and go live` — testing route, live lifecycle-webhook enablement, and go-live checklist.

## Evidence boundary

This is a webpage snapshot fetched 2026-09-15 whose metadata says it was last modified 2023-07-28. Its examples name specific Checkout API and language-library versions and use test endpoints; confirm current API versions, roles, payment-method support, regional/SCA obligations, account configuration, and production eligibility before implementation. The snapshot documents request patterns and expected routes, not current availability or successful authorization, capture, settlement, or funding.

## Related

- [[adyen-tokenization]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/online-payments/tokenization/make-token-payments/2026-09-15|Adyen Docs — Make token payments (2026-09-15)]]
