---
title: "Adyen Classic pre-authorisation and authorisation adjustment"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/modify-payments/adjust-authorisation"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/modify-payments/adjust-authorisation/2026-09-15.md"
tags: [adyen, online-payments, classic-api, pre-authorization, authorization-adjustment, capture]
---

## Overview

This 2026-09-15 snapshot of an Adyen Classic Payment API guide describes pre-authorising a payment, adjusting its authorised amount, and manually capturing the final amount. The page says the endpoint is inactive and unsupported for new integrations: new integrations should use Checkout API, while existing users should contact Adyen about migration. The page's `last_modified` metadata is 2020-11-11; its flow and availability statements are snapshot evidence, not current account eligibility.

## Key takeaways

- The default card authorisation type is final and cannot be adjusted. An eligible existing Classic integration can choose `PreAuth` in the payment request or arrange a merchant-account default; it retains the original pre-authorisation `pspReference` for later adjustments and capture. Payment-method, scheme, merchant-category-code, and issuer support limit availability. See `Authorisation types`, `Step 1`, and `Availability`.
- `/adjustAuthorisation` uses `originalReference` equal to that original pre-authorisation PSP reference. `modificationAmount` is the **new total authorised amount in minor units**, including the initial amount and all increments, rather than an incremental charge; zero-value adjustment is prohibited. An adjustment response has its own PSP reference, distinct from the original. See `Step 2: (Optional) Modify the authorisation`, both adjustment tabs.
- The asynchronous path uses the original PSP reference across adjustment and capture requests. Its `[adjustAuthorisation-received]` response only acknowledges receipt; a webhook establishes whether the new amount was authorised. The synchronous path requires Support enablement and passing the latest `adjustAuthorisationData` blob from each step to the next; its `Authorised` response indicates the new amount is authorised. Omitting the blob at any stage switches that payment permanently to asynchronous adjustment. Capture success still requires a webhook. See `Asynchronous or synchronous adjustment`, `Requirements`, `Optional Configure your account`, and both adjustment tabs.
- After the last intended adjustment, `/capture` specifies the original pre-authorisation reference and the final total in minor units. Its `[capture-received]` response is separate from the later `CAPTURE` webhook outcome. The guide also describes a qualified multiple-partial-capture sequence in which adjustment follows a partial capture. See `Step 3: Finalize the pre-authorised payment`.
- An expired pre-authorisation cannot be adjusted. Adyen's default 28-day expiration for global schemes and each card scheme's own validity rules are separate; the guide warns that capture after scheme-side expiry can fail and incur fees or chargeback risk. Extension uses the current authorised balance as the adjustment amount, but Visa supports only the asynchronous extension flow, and a refused Visa or American Express extension can terminate the original authorisation. See `Extend the authorisation`, `Availability`, and `Expiration of authorizations`.

## Detail locators

- `Use cases`: hotel charges and preorder validity examples; stored-card late charges are a separate new payment.
- `Requirements` and `(Optional) Configure your account`: payment integration, webhook setup, Support-enabled synchronous mode, and pre-authorisation scheme-fee note.
- `Step 2`: request/response examples, original versus adjustment PSP references, new-total arithmetic, latest-blob encoding detail, and conditional extension behavior.
- `Availability` and `Expiration of authorizations`: method/MCC table and scheme-specific validity tables; consult those qualified rows rather than applying one universal period.

## Related

- [[adyen]]
- [[adyen-authorization-adjustment]]
- [[adyen-payment-capture]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/modify-payments/adjust-authorisation/2026-09-15|Adyen Classic authorisation adjustment, 2026-09-15 snapshot]]
