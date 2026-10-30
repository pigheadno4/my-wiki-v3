---
title: "Adyen Classic Payment API v68: POST /capture"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Payment/latest/post/capture"
raw_files:
  - "adyen/api-explorer/Payment/latest/post/capture/2026-09-15.md"
tags: [adyen, classic-payment-api, capture, authorization]
---

## Overview

Captured Classic Payment API `POST /capture` reference for requesting capture of a payment authorization hold. The page lists the test server `https://pal-test.adyen.com/pal/servlet/Payment/v68`; `latest` in the URL is not evidence of a newer contract or live availability. The endpoint is labeled inactive and unsupported for new integrations: the page directs new integrations to Checkout API `POST /payments/{paymentPspReference}/captures` and existing integrations to migration guidance. This page does not supply that Checkout endpoint's schema. See [[adyen]] and [[adyen-payment-capture]].

## Key takeaways

- The request table marks `merchantAccount`, `modificationAmount`, and `originalReference` required. `originalReference` is the original payment's authorization `pspReference`, distinct from the reference returned for this capture request. `modificationAmount.currency` must match the authorization currency and its minor-unit `value` must not exceed the authorized amount. The table marks both nested amount fields required within that object; it does not separately declare whole-body requiredness.
- The introduction says capturing less than the full authorized amount cancels the remaining authorization balance. The related guide and concept separately document an enabled multiple-partial-capture mode that can retain the remainder; do not generalize this page's default statement to that separately configured mode. Automatically captured methods and immediate/delayed auto-capture ordinarily need no explicit request, and the page says submitting one on already auto-captured transactions does not double charge.
- A 200 response returns a required request `pspReference` and `response` indicating that the modification request was received for processing; its example is `[capture-received]`. Receipt is not final capture completion, settlement, or proof of funds. The related Classic capture guide describes subsequent webhook and possible later failure outcomes.
- The page lists 400 unreadable request, 401 authentication required, 403 insufficient permissions, 422 validation error and 500 server processing failure. Consult the full request table for conditional MPI, platform split and POS fields rather than applying them universally.

## Detail locators

- Purpose, auto-capture and inactive/Checkout migration boundary: pinned raw lines 5–22. Full request schema and conditional fields: lines 24–63. Request example: lines 65–78.
- 200 response and receipt identity: lines 79–89, example lines 161–171. Error response tables: lines 92–159; available error examples: lines 173–208.

## Related

- [[adyen-payment-capture]] — capture lifecycle and result boundary.
- [[source-adyen-docs-online-payments-classic-integrations-modify-payments-capture]] — Classic guide for webhook outcomes and multiple partial capture conditions.

## Related raw API references

- `Checkout/latest/post/payments/(paymentPspReference)/captures` — new-integration route named in this source; its endpoint contract must be read separately.

## Raw Sources

- [[raw/adyen/api-explorer/Payment/latest/post/capture/2026-09-15|Classic Payment API POST /capture captured 2026-09-15]]
