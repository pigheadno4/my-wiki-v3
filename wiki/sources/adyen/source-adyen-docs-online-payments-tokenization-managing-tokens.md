---
title: "Adyen Docs: Manage tokens"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/tokenization/managing-tokens"
raw_files:
  - "adyen/docs/online-payments/tokenization/managing-tokens/2026-09-15.md"
tags: [adyen, tokenization, stored-payment-methods, recurring-payments, webhooks]
---

## Overview

This Adyen guide explains how an online-payments integration manages stored-payment tokens through the Checkout API: listing a shopper's stored details, updating eligible stored card details, deleting a token, and receiving recurring-token lifecycle webhooks. It extends [[adyen-tokenization|Adyen tokenization]] from token creation into ongoing lifecycle operations.

The page is a 2026-09-15 documentation snapshot, not proof of current merchant eligibility, Adyen-side configuration, webhook delivery, successful updates or deletion, or production payment execution.

## Key takeaways

- The documented prerequisites are an online-payments integration, the Checkout webservice, Merchant Recurring, and API tokenise payment details credential roles, token creation setup, and subscription to Recurring tokens life cycle events webhooks.
- `GET /storedPaymentMethods` lists details for a `merchantAccount` and `shopperReference`. Its response supplies each stored method's `id` and the recurring-processing models it supports; those values are the guide's route for selecting a token for later use or deletion.
- Merchant-initiated updates apply only to tokens stored with `recurringProcessingModel: CardOnFile`. On Checkout API v70 and later, API-based updates also require additional Adyen-side configuration and an eligibility discussion with Support.
- The update flow uses a zero-value `/payments` request and can retain the existing stored-payment-method identifier for the documented expiry, holder-name, and billing-address changes. A new card number instead requires storing new payment details and receiving a new identifier.
- The update section has an internal request-shape gap: it names `billingAddress` as updateable, but the later table headed "Also include at least one of the fields you want to update" lists only `expiryMonth`, `expiryYear`, and `holderName`. Use the API reference or Adyen Support rather than inferring the omitted field shape from this page.
- Deletion uses `DELETE /storedPaymentMethods/{storedPaymentMethodId}` with the merchant account and shopper reference. After deleting details held by Adyen, the merchant must also delete any remaining shopper details from its own servers. The lifecycle webhook reports this outcome as `recurring.token.disabled`; the same event can also result from a third party disabling the details.
- Card-network updates follow a separate Account Updater path: the Real Time service updates card details automatically while retaining the token, whereas the Batch service returns updated details that the merchant applies through a zero-value transaction.

## Detail locators

- **Requirements** — integration type, credential roles, lifecycle-webhook subscription, and prior token creation: raw lines 21-32.
- **How it works** — list, update, and delete operations plus update/delete webhook notification: raw lines 34-42.
- **List stored payment details** — request parameters, stored token ID, and supported recurring-processing models: raw lines 44-84.
- **Update stored details** — CardOnFile scope, Checkout API v70-or-later eligibility configuration, retained-ID fields, new-card-number behavior, zero-value request fields, and the `billingAddress` table gap: raw lines 86-142.
- **Updates from card networks** — Real Time and Batch Account Updater handling: raw lines 144-150.
- **Delete stored payment details** — token selection, DELETE endpoint parameters, versioned language examples, and required cleanup of remaining shopper details on merchant servers: raw lines 151-322.
- **Receive token lifecycle webhooks** — enablement, event fields and types, third-party disablement, and the example disabled event: raw lines 324-363.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-tokenization]]
- Cross-cutting concept: [[recurring-payments]]

## Raw Sources

- [[raw/adyen/docs/online-payments/tokenization/managing-tokens/2026-09-15|Adyen Docs — Manage tokens (2026-09-15)]]
