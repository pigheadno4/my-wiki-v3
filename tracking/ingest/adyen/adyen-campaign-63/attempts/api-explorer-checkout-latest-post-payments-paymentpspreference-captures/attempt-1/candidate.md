---
title: "Adyen Checkout API POST /payments/{paymentPspReference}/captures"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/captures"
raw_files:
  - "adyen/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/captures/2026-11-02.md"
tags: [adyen, checkout-api, capture, online-payments]
---

## Overview

The 2026-11-02 snapshot of the Checkout API `latest` reference documents `POST /payments/{paymentPspReference}/captures` on the listed `https://checkout-test.adyen.com/v72` server. It submits a full or partial capture of an authorised payment and returns a distinct capture-request reference. The path `paymentPspReference` identifies the payment; response `pspReference` identifies the capture request. This TEST v72 snapshot does not establish current or live availability. [[adyen]] [[adyen-payment-capture]]

## Key takeaways

- Required inputs are the original payment's `paymentPspReference` path parameter and body `amount` (`currency` and `value`) plus `merchantAccount`. Currency must match authorisation; value is in minor units and cannot exceed the authorised amount. The optional `Idempotency-Key` header is a unique message identifier of at most 64 characters; the page recommends a UUID but does not specify retry semantics. Optional capture `reference` has an 80-character maximum. See raw lines 20–37 and 153–159.
- By default, unclaimed authorisation after a partial capture is cancelled. The exception requires both account enablement for multiple partial captures and a payment method that supports them. Automatic capture is the default for most methods, for which manual capture requests are unnecessary; the page says a request against an automatically captured payment does not double charge. See raw lines 7–13.
- The `201 Success` response has `status: received`, the captured `amount`, `merchantAccount`, original `paymentPspReference`, and capture-request `pspReference`; `reference` is optional. `received` acknowledges this request, while the outcome arrives asynchronously in a `CAPTURE` webhook. It does not prove capture or settlement finality. See raw lines 271–325 and response example at 416–433.

> [!warning] Schema wording in this capture endpoint's optional `lineItems` request and response rows describes "refunded items" and says they are required for certain partial refunds. Those rows refer to refunds despite this page's capture operation. Do not convert that wording into a capture requirement without separate endpoint-specific evidence. See raw lines 126–152 and 282–308.

## Detail locators

- Optional `enhancedSchemeData` structures, including conditional nested required fields and per-field limits: raw lines 60–125. Optional `applicationInfo`: lines 38–59.
- Optional `splits` and `platformChargebackLogic`: raw lines 154–166. Split `type` is required within an included split; `account`, `amount`, and `reference` have integration- and type-specific conditions. Balance Platform and Classic Platforms types differ. Their request examples are at lines 201–270; response fields are at 311–344.
- Optional `subMerchants` contains fields whose prose adds registered-payment-facilitator conditions, with required nested address and amount fields when those objects apply: raw lines 167–185; response lines 326–344.
- HTTP error sections: raw lines 347–414 for 400, 401, 403, 422, and 500 with optional error fields; example payloads at lines 512–573. These examples do not establish a capture-specific failure lifecycle.
- Request examples: raw lines 187–270. Response examples: lines 416–510.

## Related

- [[adyen-payment-capture]] — capture modes and asynchronous outcome boundary.
- [[source-adyen-docs-online-payments-capture]] — separate capture guide; apply its claims only from its own dated source.
- [[source-adyen-api-explorer-webhooks-latest-post-capture]] — separate `CAPTURE` notification reference.

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/captures/2026-11-02|Checkout API capture endpoint raw snapshot (2026-11-02)]]
