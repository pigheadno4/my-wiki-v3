---
title: "Adyen Classic Payment API v68 POST /cancel — Cancel an authorisation"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Payment/latest/post/cancel"
raw_files:
  - "adyen/api-explorer/Payment/latest/post/cancel/2026-09-15.md"
tags: [adyen, classic-payment-api, cancellation, authorisation]
---

## Overview

This captured Classic Payment API v68 reference documents `POST /cancel` for requesting cancellation of a payment's authorisation hold. It applies after authorisation only to payment methods with distinct authorisations and captures. The endpoint is marked inactive and unsupported for new integrations; the page points new integrations to Checkout API `/payments/{paymentPspReference}/cancels`, and existing users to migration. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The request body table requires `merchantAccount` and `originalReference`, the original payment PSP reference from an authorisation response or notification. Optional `reference` is the merchant's modification reference, not the original payment reference. `originalMerchantReference` is also optional.
- The 200 response returns a new `pspReference` for the cancellation request and a `response` indicating that the modification request was received for processing. It does not itself establish that the authorisation hold has been cancelled. Confirm the asynchronous modification outcome through the relevant notification route in [[source-adyen-docs-online-payments-classic-integrations-modify-payments-cancel]].
- The broad request schema also lists optional `additionalData`, `mpiData`, platform chargeback logic, `splits`, and POS identifiers with their own conditional field descriptions. These table entries should not be converted into blanket cancellation prerequisites. Error tables list 400, 401, 403, 422, and 500.
- The `latest` page captured on 2026-09-15 lists the test server `https://pal-test.adyen.com/pal/servlet/Payment/v68`. It does not establish the current API version or a Checkout endpoint contract.

## Detail locators

- Cancellation scope, inactive status and Checkout migration: raw lines 5–20.
- Request identities and optional/conditional schema: raw lines 24–58.
- Example request: raw lines 60–69.
- 200 acknowledgement and errors/examples: raw lines 70–189.

## Related

- [[source-adyen-docs-online-payments-classic-integrations-modify-payments-cancel]] — Classic cancellation guide and asynchronous outcome.
- [[source-adyen-docs-online-payments-cancel]] — Checkout cancellation guide.

## Raw Sources

- [[raw/adyen/api-explorer/Payment/latest/post/cancel/2026-09-15|Captured Classic Payment API POST /cancel reference]]
