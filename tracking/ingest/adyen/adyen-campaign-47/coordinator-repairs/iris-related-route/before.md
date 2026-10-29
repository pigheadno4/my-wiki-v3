---
title: "Adyen IRIS API-only integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/iris/api-only"
raw_files:
  - "adyen/docs/payment-methods/iris/api-only/2026-09-15.md"
tags:
  - adyen
  - iris
  - api-only
  - greece
  - redirect
  - qr-code
---

## Overview

This captured Adyen guide explains how to add IRIS to an existing API-only online payment integration for Greece and EUR. It covers issuer redirect and QR-code flows, required setup, API actions, result handling, testing, and live onboarding. It is a source for [[adyen]] and [[adyen-online-payments]]; the captured instructions do not establish a merchant's current eligibility, activation, live operation, or receipt of funds.

## Key takeaways

- **Prerequisites:** An existing API-only integration must handle additional actions of type **redirect** and **qrCode**. Add IRIS in Customer Area. Before live use, request IRIS from a Greek bank and Adyen with the DIAS code, merchant account, and associated stores; complete bank onboarding and enable IRIS for the live merchant account. [Raw: lines 25–29, 1372]
- **Discovery and geography:** Request available methods with countryCode **GR** and currency **EUR**. The returned IRIS issuer list may include the six banks named in the captured example; treat the response as the available list rather than a fixed roster. [Raw: lines 44–70, 339–378]
- **Choose a flow explicitly:** For issuer redirect, pass **paymentMethod.type=iris**, **paymentMethod.issuer** from the shopper's selected bank, and **returnUrl**. The response contains a redirect URL; after the shopper returns, send the URL-decoded **redirectResult** to **/payments/details**. This flow applies to mobile and desktop. [Raw: lines 35–40, 380–388, 712–740, 980–992]
- **QR flow:** Omit **paymentMethod.issuer** to receive **action.type=qrCode** and **qrCodeData**. The field table says **returnUrl** is not required for QR, even though QR examples include it. Render the code, show the shopper the 10-minute completion window as recommended, and await the result webhook. QR is intended for desktop; the guide does not recommend it on mobile because the scanning app may be on the same device. [Raw: lines 35–40, 380–388, 994–1017, 1312–1338, 1361]
- **Outcome boundary:** **Pending** or **Received** means the final result is unknown; an **AUTHORISATION** webhook supplies it. QR requires webhook confirmation. Redirect also requires the webhook when the shopper fails to return. **Authorised** says the shopper completed payment and it was sent to the bank for processing; the guide says funds arrive in most cases, not that settlement is guaranteed. [Raw: lines 1340–1361]
- **Test versus live:** The Adyen test simulator offers Successful, Refused, and Cancelled outcomes. Its hosted page is reached via the redirect link or URL encoded in the QR code. Live acceptance additionally requires Greek-bank onboarding and live Customer Area enablement. [Raw: lines 1363–1372]

> [!WARNING] Redirect examples disagree with the field table
> The field table says **paymentMethod.issuer** is required for issuer redirect and omission selects QR. Several code examples under the issuer-redirect heading omit **issuer** (Java, PHP, C#, Go, and TypeScript). Do not infer that those requests produce an issuer redirect; use the documented flow selector and verify the returned action. [Raw: lines 388, 439–447, 478–488, 522–534, 597–607, 695–705]

> [!WARNING] Related method overview limits
> The separately captured IRIS overview says Adyen acts as a gateway and refunds and cancellations are handled with the contracted Greek bank, rather than through Adyen. Its capability matrix labels the flow Redirect, while this API-only guide also documents a QR branch. Read the overview's matrix as a summary, not an exclusion of the QR branch. The API-only guide does not document an Adyen refund or cancellation operation. [Related raw: raw/adyen/docs/payment-methods/iris/2026-09-15.md, lines 23–41]

## Detail locators

- Requirements and two flows: raw lines 15–42.
- IRIS issuer discovery and GR/EUR request: raw lines 44–70 and 339–378.
- Payment field table and flow selector: raw lines 380–388.
- Issuer redirect examples, returned action, and return handling: raw lines 390–992.
- QR examples, action payload, timer, and rendering: raw lines 994–1338.
- Result codes, webhooks, test simulator, and live setup: raw lines 1340–1372.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[raw/adyen/docs/payment-methods/iris/2026-09-15|IRIS method overview raw]] — bank contracting and refund/cancellation boundary.

## Raw Sources

- [[raw/adyen/docs/payment-methods/iris/api-only/2026-09-15]]
