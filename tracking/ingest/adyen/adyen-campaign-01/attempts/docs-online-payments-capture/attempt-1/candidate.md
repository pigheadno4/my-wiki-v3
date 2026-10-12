---
title: "Capture | Adyen Docs"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/capture"
raw_files:
  - "adyen/docs/online-payments/capture/2026-09-15.md"
tags: [adyen, online-payments, capture, authorization, webhooks]
---

## Overview

This Adyen documentation page explains how an authorized online payment is captured. Immediate automatic capture is the default; for payment methods that support separate capture, merchants can configure delayed automatic capture or send a manual capture request after authorization.

## Key takeaways

- Separate capture is payment-method dependent. An individual payment's API capture setting overrides the merchant-account setting in Customer Area.
- A manual capture uses the authorization's `pspReference` as `paymentPspReference` in `POST /payments/{paymentPspReference}/captures`. The request identifies the merchant account and capture amount; the currency must match the authorized payment, and a partial amount must not exceed it.
- A single partial capture automatically cancels the unclaimed amount. Multiple partial captures retain the remaining balance but are disabled by default and require Adyen Support to enable them.
- A manual capture response with `status: received` acknowledges asynchronous processing rather than a completed transfer. The `CAPTURE` webhook reports whether the request was valid and submitted onward; a later `CAPTURE_FAILED` webhook can still report a rare scheme or issuer rejection.
- Capture refusal details can vary by payment method and region. Adyen warns merchants not to expose those refusal details to shoppers.

## Detail locators

- `Requirements` — roles, webhook event codes, payment-method limits, and multiple-partial-capture enablement.
- `Types of capture` — immediate, delayed automatic, manual, single partial, and multiple partial behavior.
- `Delayed automatic capture` — Customer Area and per-payment configuration, including precedence and webhook settings.
- `Manual capture` > `Capture a payment` — authorization reference, endpoint, required amount and merchant fields, response identifiers, and asynchronous status.
- `Webhooks for captures` — `CAPTURE` validity result, unsuccessful-request reasons, later `CAPTURE_FAILED` events, refusal fields, and test-environment guidance.

## Related

- Company: [[adyen]]
- Concept: [[adyen-payment-capture]]

## Raw Sources

- [[raw/adyen/docs/online-payments/capture/2026-09-15|2026-09-15 snapshot — Adyen Capture documentation]]
