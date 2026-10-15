---
title: "Capture a recurring payment with Classic API | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/tokenization/capture-a-recurring-payment"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/capture-a-recurring-payment/2026-09-15.md"
tags: [adyen, classic-api, recurring-payments, capture, webhooks]
---

## Overview

Despite its placement under Classic tokenization, this 2026-09-15 guide describes capturing an **already authorized recurring payment** to collect reserved funds for methods that require a separate capture. It uses a Classic Payment API `/capture` modification, not a new `/authorise` call or a stored-detail update. Adyen marks this endpoint inactive and unsupported for new integrations, routing new builds and existing-integration migration to Checkout API. See [[adyen]], [[adyen-payment-capture]], and [[adyen-tokenization]].

## Key takeaways

- For payment methods requiring separate capture, the guide offers automatic capture, manual capture in Customer Area, or a server-side `/capture` call. The server request identifies the merchant account, a full or partial `modificationAmount`, and the earlier authorization's payment `pspReference` as `originalReference`. The examples also include a merchant modification reference.
- The illustrated `/capture` response has its own `pspReference` and `[capture-received]`. A syntactically valid request can receive this acknowledgment; it **does not mean the payment was captured**. Adyen sends the final capture result in a separate webhook event. This page does not specify that event's fields or prove any particular capture or settlement outcome.
- This is a dated Classic API snapshot. Its curl example uses a Payment API v46 test endpoint and the language-library examples use various historical versions. The page is not a modern Checkout API request schema or evidence that a particular method/account supports manual or partial capture.

## Detail locators

- Inactive endpoint and migration: lines 16–21.
- Capture need, methods, and authorization prerequisite: line 23.
- `/capture` request identity, amount, and original authorization reference: `Request`, lines 27–33; JSON example lines 35–47; dated curl/API-library examples lines 69–319.
- Syntax acknowledgment, `[capture-received]`, and separate final webhook: `Response`, lines 321–338.

## Related

- [[adyen-payment-capture]] — provider capture lifecycle and outcome route.
- [[adyen-tokenization]] — recurring stored-payment context.

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/capture-a-recurring-payment/2026-09-15|Classic recurring payment capture (2026-09-15)]]
