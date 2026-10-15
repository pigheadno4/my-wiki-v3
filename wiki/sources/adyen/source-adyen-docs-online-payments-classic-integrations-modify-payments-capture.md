---
title: "Adyen Classic API capture"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/modify-payments/capture"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/modify-payments/capture/2026-09-15.md"
tags: [adyen, online-payments, classic-api, capture, payment-modifications, webhooks]
---

## Overview

This dated Adyen guide describes completing an authorized online payment through capture on the Classic Payment API route. It distinguishes immediate or delayed automatic capture from an explicit manual `POST /capture` request for payment methods that support separate authorization and capture. The page labels the Classic endpoint inactive and unsupported for new integrations, directing new work to Checkout API and existing merchants to migration guidance. The raw page reports `last_modified: 2020-12-01` and was captured 2026-09-15; its settings and lifecycle statements are snapshot evidence.

## Key takeaways

- Immediate automatic capture is the default in this guide. Merchant-account capture delay can be configured in Customer Area by a user with the Merchant admin role; the listed fixed delay is 1–7 days. Automatic capture does not ordinarily generate a separate `CAPTURE` webhook, though delayed automatic capture can be configured to do so through Support. See **Automatic capture** and **Capture delay**.
- Manual capture can be enabled at the merchant account, or `captureDelayHours` can schedule capture from a payment request. The latter does not ordinarily generate a separate `CAPTURE` webhook unless enabled through Support. See **Manual capture**.
- Explicit `POST /capture` uses `merchantAccount`, `modificationAmount`, and `originalReference`, where the original reference is the authorization's payment `pspReference`; an optional modification `reference` can aid reconciliation. The returned capture `pspReference` identifies this modification, distinct from the original payment. The `[capture-received]` response acknowledges receipt, not final success. See **Capture a payment**.
- After processing an explicit request, a `CAPTURE` webhook connects the authorization `originalReference` to the capture `pspReference`. `success: true` means the request was valid and submitted onward, while `success: false` reports request failure with a reason. Even after `success: true`, a rare later scheme rejection can produce `CAPTURE_FAILED`, sometimes days later. See **CAPTURE webhook** and **Failed capture**.
- Partial capture depends on the payment method. In single partial capture the unclaimed balance is automatically cancelled; multiple partial captures retain it and require separate account enablement through Support. A requested partial amount must be below the authorized amount. See **Partial capture**.
- Failure reasons can include generic and raw refusal fields, with values varying by payment method and region. The page warns against exposing refusal details to shoppers. See **Failed capture**.

## Detail locators

- **Capture delay** — merchant-level setting, Merchant admin role, immediate versus listed 1–7 day delays, and conditional webhook enablement.
- **Manual capture** — Customer Area selection, `captureDelayHours`, and separate webhook behavior.
- **Capture a payment** — required Classic modification fields, amount ceiling, original authorization reference, optional reconciliation reference, and distinct capture reference.
- **CAPTURE webhook** — authorization/capture reference pairing, `success` semantics, and request failure reason.
- **Partial capture** — payment-method qualification, single versus multiple remaining-balance handling, and Support enablement.
- **Failed capture** — later `CAPTURE_FAILED` possibility, refusal fields, merchant handling, and shopper disclosure warning.
- **Testing failed captures** — test-environment fixture and asynchronous processing note; it does not prove a live decline outcome.

## Related

- [[adyen]]
- [[adyen-payment-capture]]
- [[source-adyen-docs-online-payments-capture]] — Checkout API capture guide for newer integrations.

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/modify-payments/capture/2026-09-15|Classic API capture (2026-09-15 snapshot)]]
