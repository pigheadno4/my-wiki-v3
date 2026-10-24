---
title: "UPI API-only payments"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/upi/api-only"
raw_files:
  - "adyen/docs/payment-methods/upi/api-only/2026-09-15.md"
tags: [adyen, upi, india, api-only, redirects, qr]
---

## Overview

This 2022-modified, 2026-09-15-captured [[adyen]] **India UPI API-only** guide describes a merchant-built checkout form and three one-off paths: UPI **Intent** app redirect, **QR** scan and legacy **Collect** UPI ID/VPA. It routes through [[adyen-online-payments]]. The body also contains a November 2025 UPI Collect change, so the old metadata date is not a reliable freshness marker. A `Pending` request result, app launch, QR display or VPA validation is not final payment evidence.

## Key takeaways

- The stated prerequisite is an existing **API-only Advanced Web** integration and adding the payment method in **test Customer Area**. The examples use INR in minor units and TEST Checkout URLs, with **v72** for Intent, **v68** for QR and Collect, and a **v71** validation example. These are example endpoint versions, not a common minimum version or proof of current live eligibility.
- **UPI Intent:** the `/payments` request specifies `paymentMethod.type: upi_intent`, an `appId` for the chosen third-party UPI app, and INR amount. The page lists app IDs including gpay, phonepe, bhim, paytm, amazonpay and others at the raw locator. It recommends Intent for mobile shoppers and screen-size detection; the response's `Pending` and `action.url` direct a mobile app switch. Android may offer compatible apps; iOS chooses a default. The recommended iOS/Android browser containers for GET redirects are advice, not a guarantee of safe return or successful debit.
- **UPI QR:** the `/payments` request uses `paymentMethod.type: upi_qr` and INR amount. `action.qrCodeData` is rendered at checkout for a shopper to scan in a UPI app; the page recommends QR for desktop/tablet and a five-minute **reminder timer**, without asserting a five-minute transaction expiry. The illustrative response shows `Pending`, `qrCode`, `details` and `redirect` data; its fields are example output, not a complete universal contract.
- **UPI Collect:** the page says NPCI informed partners in **November 2025** of planned Collect deprecation, and Adyen would stop offering Collect to **new merchant integrations** while strongly recommending that existing custom Checkout API/UI Collect merchants migrate toward Intent/QR. It does not say existing Collect transactions had already ended. Collect requests use `paymentMethod.type: upi_collect`, shopper-entered `virtualPaymentAddress` and INR; `action.type: await` means to await the webhook.
- Optional `/validateShopperId` can check Collect VPA format/current recognition only on **Adyen Direct**, not legacy Billdesk/PayU. It does **not guarantee a later debit**. The table allows `valid` or technical `unknown` to proceed and blocks explicit `invalid`; the prose says HTTP 4xx/5xx validation failures should also proceed rather than block. A successful VPA check is not authorization.
- Intent, QR and Collect instruct the merchant to use **AUTHORISATION** webhook success/failure for payment outcome after shopper action; `Pending` means the final status is unavailable. A recommended five-minute waiting/countdown screen and subsequent shopper redirect/presentation depend on that asynchronous result. The repeated TEST simulator checklist instead spells the eventCode **AUTHORISED**, conflicting with the guide's **AUTHORISATION** webhook tables; retain this mismatch rather than treating either spelling as established from the test example. Simulator selections, Customer Area listing and recommended modification tests are instructions, not observed outcomes.

## Detail locators

- [[raw/adyen/docs/payment-methods/upi/api-only/2026-09-15|Pinned raw]], lines 14–23: API-only/India scope and prerequisite; lines 25–99: Intent fields, app list, TEST v72 example, Pending/action URL and app redirect.
- Same raw, lines 101–139: recommended browser/waiting UI, AUTHORISATION webhook and TEST simulator checklist with differing `AUTHORISED` spelling.
- Same raw, lines 141–251: QR fields, TEST v68 example, QR render/wait, webhook status and repeated simulator checklist.
- Same raw, lines 253–325: dated Collect change, optional VPA validation, Adyen Direct/legacy split and invalid versus technical-error handling.
- Same raw, lines 327–425: Collect TEST v68 example, await/webhook outcome and repeated simulator guidance; code samples include placeholders and should not be treated as a production implementation.

## Related

- [[adyen-tokenization]] — separate token lifecycle context; this page concerns the UPI one-off flows, not AutoPay mandates.

## Raw Sources

- [[raw/adyen/docs/payment-methods/upi/api-only/2026-09-15|UPI API only]]
