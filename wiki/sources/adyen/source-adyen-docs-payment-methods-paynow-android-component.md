---
title: "Adyen PayNow Android Component guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paynow/android-component"
raw_files:
  - "adyen/docs/payment-methods/paynow/android-component/2026-09-15.md"
tags: [adyen, paynow, android, components, qr-code, online-payments]
---

## Overview

This 2026-09-15 Adyen page gives **PayNow-specific additions** to existing Android Components integrations, with separate Sessions and Advanced flow sections. It uses `InstantPaymentComponent` and, for Advanced, a QR-code action. It is not a complete base integration or evidence that a merchant is live-enabled or a bank payment completed. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions route:** The guide calls for an existing Android Components Sessions integration, Checkout API **v68 or later**, and PayNow added in Customer Area. It says no PayNow-specific `/sessions` parameters or configuration are needed. It imports the `instant` Android module, plus `components-compose` if using Jetpack Compose, and creates `InstantPaymentComponent` for the `paynow` method. In Compose, the example says a unique key is required for each different screen/session and a new key when resetting the Component. The module's `YOUR_VERSION` placeholder is not a specified SDK minimum. (raw lines 25–125)
- **Advanced route:** The guide calls for an existing Android Components Advanced integration, PayNow in Customer Area, and additional-action handling for **`action.type: qrCode`**. It gives Compose/non-Compose `InstantPaymentComponent` examples using the `paynow` method from `/paymentMethods`, and says no additional PayNow configuration or ordinary `/payments` parameters are needed. The no-extra wording concerns PayNow additions to the base flow; it does not remove base requests, QR-action handling or result verification. (raw lines 137–237)
- **Live and test warning:** Before accepting live payments, the page says to contact Adyen Support to add PayNow in the **live Customer Area**. It describes penny testing in that live area with small amounts and a **real banking app** scanning a test QR. It recommends against testing in the test Customer Area because bank transfers there **cannot be reversed** and funds will be deducted from the bank account. This is a consequential source warning, not a request to perform a real-money test, and neither a QR scan nor a status-list instruction proves final authorization, capture, refund or settlement. (raw lines 127–135, 239–247)
- **Scope and outcome limit:** The guide supplies Component imports/launch steps and a QR action prerequisite, but gives no QR expiry time, scan-to-result webhook/status sequence or completed-payment response on this page. Consult the base integration and PayNow QR lifecycle authority before interpreting a displayed code or shopper scan as a final payment outcome. (raw lines 19–23, 137–145, 233–247)

## Detail locators

- Sessions requirements, Checkout API minimum and ordinary no-extra fields: raw lines 25–41.
- Module imports, Compose key and Component launch: raw lines 43–125.
- Advanced QR-code action requirement and Component examples: raw lines 137–230.
- Advanced ordinary `/payments` no-extra statement: raw lines 233–237.
- Repeated live setup and consequential bank-transfer test warning: raw lines 127–135, 239–247.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-paynow]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paynow/android-component/2026-09-15|Adyen PayNow Android Component, 2026-09-15 snapshot]]
