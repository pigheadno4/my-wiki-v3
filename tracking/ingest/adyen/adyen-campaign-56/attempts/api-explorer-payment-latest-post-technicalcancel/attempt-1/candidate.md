---
title: "Adyen Classic Payment API v68: POST /technicalCancel"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Payment/latest/post/technicalCancel"
raw_files:
  - "adyen/api-explorer/Payment/latest/post/technicalCancel/2026-09-15.md"
tags: [adyen, classic-payment-api, technical-cancel, api-reference]
---

## Overview

This captured [[adyen]] **Classic Payment API**, not Checkout API, reference describes `POST /technicalCancel`: request cancellation when the original payment's PSP reference is unavailable, identifying that payment by the merchant `reference` supplied in its payment request. The endpoint is labeled **inactive** and unsupported for new integrations; the page directs new integrations to Checkout `/cancels` and existing integrations to contact Adyen about migration. Its captured server is `https://pal-test.adyen.com/pal/servlet/Payment/v68`; the `latest` URL does not establish current latest or live availability.

## Key takeaways

- The request table requires `merchantAccount` and `originalMerchantReference`. The latter is the original payment's merchant reference, not an original `pspReference`. Optional `reference` identifies this **modification** in Customer Area and reports; keep it separate from the original merchant reference and from response `pspReference`.
- The shared modification request table also lists optional additional data, MPI data, platform fields and `modificationAmount`. Its amount description says the field is required for `/capture` and `/refund` and prohibited for `/cancel`; it does not explicitly establish a separate `/technicalCancel` amount rule. The shown technical-cancel request omits it.
- HTTP 200 means request success. The required response `response` field indicates that the modification request was **received for processing**; the example value is `[technical-cancel-received]`. This is an acknowledgement, not proof that the original authorization was cancelled, funds were released, or any downstream outcome completed. The required returned `pspReference` identifies the transaction/request; the page does not say it is the missing original payment PSP reference.
- The raw reference documents 400, 401, 403, 422 and 500 errors with generic response shapes. Its selected error examples are illustrative, not an exhaustive failure-code list. No later outcome mechanism is specified in this endpoint capture.

## Detail locators

- Purpose, original-reference route, inactive/migration warning and v68 TEST server: raw lines 5–22.
- Required original merchant reference and merchant account, distinct optional modification reference, and shared conditional fields: raw lines 26–62; illustrative request: lines 64–73.
- 200 acknowledgement and returned identifiers: raw lines 74–84; selected error schemas: lines 87–154; example bodies: lines 156–203.

## Related

- [[adyen-online-payments]] — provider-level online payment and migration routes.
- [[source-adyen-docs-online-payments-classic-integrations-modify-payments-cancel]] — Classic cancellation guide, including technical cancel.
- [[source-adyen-docs-online-payments-upgrade-your-integration-migrate-to-checkout-api]] — migration guidance.

## Raw Sources

- [[raw/adyen/api-explorer/Payment/latest/post/technicalCancel/2026-09-15|Classic Payment v68 POST /technicalCancel capture]]
