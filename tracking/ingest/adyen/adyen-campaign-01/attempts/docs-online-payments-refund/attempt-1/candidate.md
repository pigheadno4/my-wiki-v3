---
title: "Adyen Online Payments Refund"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/refund"
raw_files:
  - "adyen/docs/online-payments/refund/2026-09-15.md"
tags: [adyen, online-payments, refunds, webhooks, refund-failed, refunded-reversed]
---

## Overview

This Adyen guide explains how to return a captured online payment to a shopper through the Customer Area or the Checkout API, then determine the asynchronous result from Standard webhooks. It covers referenced, partial, and approved unreferenced refunds, validation failures, later payment-method rejection, reversed refunds, test handling, and refund authorization.

## Key takeaways

- A payment can be refunded only after capture. Before capture, cancel it; if capture status is unknown, use Adyen's reversal route. Depending on the payment method, returning funds to the shopper can take up to 40 business days.
- For a referenced API refund, send `POST /payments/{paymentPspReference}/refunds` with the original payment PSP reference, merchant account, and amount. The refund currency must match the authorization currency; a partial-refund value must be below the captured amount, and multiple partial refunds cannot cumulatively exceed that amount. Partial refunds are supported only by some payment methods.
- The request response supplies the original payment reference and a separate refund-request `pspReference`; wait for the `REFUND` webhook to learn the validation outcome. Do not treat request receipt as final refund success.
- Unreferenced refunds require prior approval from Adyen Support or an Adyen contact. This snapshot documents unreferenced routes for cards, stored payment details, ACH Direct Debit, and IBAN bank transfer.

## Asynchronous outcomes and warnings

The `REFUND` webhook reports Adyen's refund-validation result. `success: false` means validation failed and includes a reason to review before correcting and resubmitting where possible. `success: true` means validation passed and the request was sent to the card scheme; it usually succeeds, but it is not a final guarantee.

A later `REFUND_FAILED` webhook is distinct from validation failure: the payment method or card scheme can reject a refund even days after `REFUND` reported `success: true`. Structured refusal details may appear in `additionalData`; do not expose refusal-reason details to shoppers.

A `REFUNDED_REVERSED` webhook is a different outcome. For some payment methods, funds from a previously refunded payment can return to Adyen and the merchant account, for example when the shopper's bank account is no longer valid. Contact the shopper about the bank-account status before retrying.

Refund authorization is automatic for the listed American Express, Discover, Mastercard, and Visa flows. Even when an issuer declines the refund authorization, the guide says Adyen still tries to process the refund.

## Detail locators

- `## Requirements` and `## Types of refunds` — integration prerequisites, required webhook event codes, Customer Area roles, capture/cancel/reversal boundary, partial-refund support, and unreferenced-refund definition (raw lines 27–48).
- `## Make a refund` — referenced endpoint, required request fields, amount/currency conditions, optional reason/reference fields, language examples with pinned SDK versions, response identifiers, and instruction to await the webhook (raw lines 50–301).
- `## Make an unreferenced refund` — approval requirement, supported route list, required fields, and examples for unencrypted/encrypted cards, stored details, ACH, and IBAN (raw lines 303–528).
- `## Test failed refunds` — test-only card setup and expected `REFUND_FAILED` event (raw lines 530–561).
- `## Webhooks for refunds` — asynchronous validation outcomes, common validation reasons, `REFUNDED_REVERSED`, later `REFUND_FAILED`, refusal fields, and shopper-disclosure warning (raw lines 563–729).
- `## Refund authorization` — automatic authorization, named card schemes, example decline causes, and continued-processing behavior (raw lines 731–751).

## Related

- Company: [[adyen]]
- Concept: [[adyen-refunds]]

## Raw Sources

- [[raw/adyen/docs/online-payments/refund/2026-09-15|2026-09-15 snapshot — referenced and unreferenced refund requests, asynchronous outcomes, and refund authorization]]
