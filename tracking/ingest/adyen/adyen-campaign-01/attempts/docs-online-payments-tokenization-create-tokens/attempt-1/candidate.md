---
title: "Adyen Docs: Create tokens"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/tokenization/create-tokens"
raw_files:
  - "adyen/docs/online-payments/tokenization/create-tokens/2026-09-15.md"
tags: [adyen, tokenization, stored-payment-methods, recurring-payments, webhooks]
---

## Overview

This Adyen guide explains how an [[adyen-tokenization|Adyen online-payments integration creates tokens]] while a shopper pays, through a zero-value authorization, through Checkout API v70-or-later `/storedPaymentMethods`, or by importing stored details from another provider. For payment-session and payment-request flows, successful tokenization is tied to authorization and the guide directs the merchant to the asynchronous `recurring.token.created` lifecycle webhook for the token used in subsequent payments.

The page is a documentation snapshot, not proof of current account eligibility, payment-method support, successful authorization, webhook delivery, or production token creation.

## Key takeaways

- Before storing details, the merchant must ask for the shopper's consent and disclose the payment schedule and amount. The integration also needs the documented credential roles, supported recurring payment methods, and the Recurring tokens life cycle events webhook; applicable PSD2 SCA rules depend on the implementation and business model.
- Token creation is supported through `/sessions`, `/payments`, and Checkout API v70-or-later `/storedPaymentMethods`. The first two attach tokenization parameters to an authorization flow. `/storedPaymentMethods` can create a token without authorization, but Adyen recommends authorization (and specifically a zero-value authorization in that tab) so the payment details have been validated and are linked to an active, chargeable account.
- `/sessions` can create tokens for all documented recurring-payment types, but subsequent `Subscription` and `UnscheduledCardOnFile` charges must use `/payments`. The required request fields and the storage flag differ by endpoint and Checkout API version; `shopperReference` must not contain personally identifiable information.
- In `/sessions` and `/payments` flows, the token is created after successful authorization. A pending payment is not tokenized yet, and asynchronous authorization responses do not include a token, so the guide recommends listening for `recurring.token.created`. Depending on `recurringProcessingModel`, SCA can be required; the initial `Subscription` and `UnscheduledCardOnFile` payment requires it, while regulations and scheme rules can require it for `CardOnFile`.
- Adyen says it is no longer developing the legacy `RECURRING_CONTRACT` webhook and strongly recommends the Recurring tokens life cycle events webhook instead; existing `RECURRING_CONTRACT` integrations remain available.
- Existing recurring contracts can be migrated by importing stored payment details, avoiding collection of those shopper details again. The output file from a successful migration provides parameters for future token payments.

## Detail locators

- **Requirements** — integration type, credential roles, lifecycle-webhook subscription, the `/sessions` subsequent-payment limitation, supported-method setup, and SCA preparation.
- **How it works** — consent, the three token-creation endpoints, authorization recommendation, and `recurring.token.created` handoff.
- **Enable the webhook** — lifecycle event fields and types, token-to-shopper association, and the legacy `RECURRING_CONTRACT` warning.
- **Create a token → Tab: `/sessions`** — version-specific storage flags, zero-value authorization caveat, authorization timing, SCA, and asynchronous token delivery.
- **Create a token → Tab: `/payments`** — tokenization parameters, Checkout API v69-or-earlier automatic-tokenization toggle, zero-value authorization caveat, result-code behavior, SCA, and webhook handling.
- **Create a token → Tab: `/storedPaymentMethods`** — Checkout API v70-or-later boundary, authorization recommendation and exception, server request fields, PCI qualification for raw card data, and direct token ID response.
- **Import stored payment details** — migration purpose and output-file handoff.
- **Test and go live** — tokenization testing route, live lifecycle-webhook enablement, and end-to-end checklist.

## Related

- [[adyen]]
- [[adyen-tokenization]]
- [[recurring-payments]]

## Raw Sources

- [[raw/adyen/docs/online-payments/tokenization/create-tokens/2026-09-15|Adyen Docs — Create tokens (2026-09-15)]]
