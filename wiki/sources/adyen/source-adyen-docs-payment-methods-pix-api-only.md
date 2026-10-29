---
title: "Pix API-only integration"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pix/api-only"
raw_files:
  - "adyen/docs/payment-methods/pix/api-only/2026-09-15.md"
tags: [adyen, pix, api-only, qr-code, brazil, asynchronous-payments]
---

## Overview

This 2026-09-15-captured Adyen guide describes **Pix additions to an existing API-only online payment integration**: obtaining availability for BR/BRL, collecting shopper identity data, submitting a Pix payment, presenting its QR-code action, and following asynchronous payment status. It also documents payment expiration, refunds, and test/live setup. See [[adyen]], [[adyen-online-payments]], and the method-level [[source-adyen-docs-payment-methods-pix]] for the Brazil-local-entity and capability context. A request example or QR display is not proof of payment.

## Key takeaways

- **Prerequisites and availability:** the page assumes an existing API-only Advanced-flow integration that handles the additional `action.type: qrCode`, and Pix added in Customer Area (raw lines 23–29). To request Pix in `/paymentMethods`, specify `countryCode: BR` and `amount.currency: BRL` (raw lines 52–59). The returned `type: pix` example is an example of availability, not a guarantee for every account (raw lines 337–348).
- **Shopper data and request fields:** the form section says to collect first/last name and CPF or CNPJ, pass both to the server, and show them beside the QR code for identification (raw lines 39–48). The later `/payments` table marks `paymentMethod` and `amount` with required checkmarks, leaves `shopperName` and `socialSecurityNumber` unmarked, then advises sending both for shopper identification (raw lines 350–365). Preserve this tension: do not reclassify the unmarked table fields as universally mandatory or omit the form prose. The same table lists optional `shopperStatement` (under 60 characters if supplied), `sessionValidity`, and line-item fields; use the raw table for exact descriptions/limits.
- **Payment expiration:** `sessionValidity` is described as the Pix **payment** expiration date; its stated default is **1 hour for Checkout API v71 or earlier** or **24 hours for v72 or later** (raw line 361). The response example includes `additionalData.pix.expirationDate`, but the captured guide does not establish a separate QR display/countdown expiry rule (raw lines 853–873). The request examples use a fixed 2025 date and are illustrative, not a current expiration value (for example raw lines 371–407).
- **Asynchronous result and amount caveat:** the example `/payments` response is `resultCode: Pending` with a `qrCode` action, `qrCodeData` and a payment expiration timestamp (raw lines 853–873). A separate test webhook example shows `AUTHORISATION` and `success: true` (raw lines 875–940). Its amount and `pix.originalAmountValue` are **100000 BRL minor units**, whereas the illustrated `/payments` request amount is **10000** (raw lines 377–380, 885–900); the source supplies no reconciliation explanation or overpayment rule connecting those examples. Do not treat Pending/QR issuance as paid, infer an overpayment feature from the mismatch, or use an example success webhook as live proof.
- **Refund and test/live boundaries:** the guide says refunds are available within **90 days after payment** through Customer Area or Refund API (raw lines 958–960). It calls Pix asynchronous and describes test-only promotion of a pending offer to sale, test reconciliation, paid offers in Payment list, and a request in **live Customer Area** before accepting live Pix (raw lines 962–975). Test promotion is not a production settlement operation.
- **Capture wording caveat:** the high-level `How it works` list says “capture the payment” (raw lines 31–37), while the method overview matrix marks **separate, partial and multiple partial captures** unavailable. The API-only page gives no distinct Pix capture endpoint recipe; do not infer support for those capture variants from this generic step.

## Detail locators

- Existing API-only, QR-action and Customer Area prerequisites: raw `## Requirements`, lines 23–29.
- Form identity collection and BR/BRL availability request: raw lines 39–59; multi-language `/paymentMethods` examples and response: raw lines 61–348.
- `/payments` field requiredness, optional descriptions and versioned payment-expiration defaults: raw lines 350–365; multi-language examples: raw lines 367–851.
- Pending QR action, expiration field and separate success webhook example: raw lines 853–940; optional payer-info notification settings: raw lines 944–956.
- Refund window and asynchronous test/live instructions: raw lines 958–975.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-pix]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/pix/api-only/2026-09-15|Pix API-only guide, captured 2026-09-15]]
