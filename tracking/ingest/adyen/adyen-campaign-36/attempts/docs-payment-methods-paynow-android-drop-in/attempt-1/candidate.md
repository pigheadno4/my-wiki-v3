---
title: "Adyen PayNow Android Drop-in guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paynow/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paynow/android-drop-in/2026-09-15.md"
tags: [adyen, paynow, android, drop-in, qr-code, bank-transfer]
---

## Overview

This [[adyen]] PayNow Android Drop-in add-on, captured 2026-09-15, gives method-specific requirements for **existing** Sessions or Advanced Android Drop-in integrations. Its Advanced section names an additional action of `qrCode`; both sections distinguish Customer Area method setup from a **Support** step for live acceptance and warn that test-environment bank transfers deduct real funds and cannot be reversed. See [[adyen-online-payments]]. This is a historical implementation guide, not proof of enabled merchant eligibility, successful QR scanning, final authorization, capture or settlement. See raw lines 15–34 and 50–90.

## Key takeaways

- **Sessions:** The page requires an existing Sessions Android Drop-in integration with Checkout API **v68 or later**, and says to add PayNow in Customer Area. It says the base `/sessions` request and PayNow-specific configuration need no additional parameters. This section does not itself state a Sessions action type or QR expiry/result-handling procedure. See raw lines 25–46.
- **Advanced:** The page requires an existing Advanced Android Drop-in integration, an additional-action handler for `action.type: qrCode`, and PayNow added in Customer Area. Its action-handling link uses a `#handle-the-redirect` anchor, but the stated action type here is **QR code**; do not recast it as a wallet redirect. It says no extra PayNow configuration or ordinary `/payments` parameters are needed, beyond whatever the base integration requires. See raw lines 60–80.
- **Live and testing boundary:** Before accepting live payments, the merchant must contact Adyen Support to add PayNow in live Customer Area. The page suggests small live penny tests with a real banking app scanning a test QR and checking payment status in live Customer Area. It **recommends against test Customer Area payments**, saying bank transfers there cannot be reversed and funds will be deducted from the bank account. These are consequential real-funds and irreversibility warnings, not evidence any test was performed or that a transaction completed. See raw lines 48–58 and 82–90.
- This page does not enumerate country/currency eligibility, QR lifetime, an asynchronous final-result webhook, refund or recurring behavior. Follow the main integration and outcome references for those questions; no such behavior can be inferred solely from these omissions. See raw lines 15–90.

## Detail locators

- Sessions prerequisites, request and configuration: raw lines 25–46.
- Advanced prerequisites, QR action, request and configuration: raw lines 60–80.
- Support live enablement, live penny-test wording, live status check and nonreversible test-transfer warning: raw lines 48–58 and 82–90.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-paynow]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paynow/android-drop-in/2026-09-15|PayNow Android Drop-in — captured 2026-09-15]]
