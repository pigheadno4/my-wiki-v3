---
title: "Adyen PayNow Web Drop-in integration"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paynow/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paynow/web-drop-in/2026-09-15.md"
tags: [adyen, paynow, web, drop-in, qr-code, bank-transfer]
---

## Overview

This [[adyen]] guide adds PayNow to an **existing Web Drop-in** Sessions or Advanced integration. It gives PayNow-specific setup, request-field and QR-action requirements plus testing/live cautions; the main integration guides remain prerequisites. See [[adyen-online-payments]]. This 2026-09-15 snapshot does not establish current account enablement, a successful payment or transfer reversal.

## Key takeaways

- For **Sessions**, the page requires an existing Web Drop-in Sessions flow, **Checkout API v68 or later**, and PayNow added in Customer Area. It says no additional PayNow parameter is needed when creating `/sessions`. Optional individual `PayNow` import is for tree shaking/performance, not a required payment step. See raw lines 25–53.
- For **Advanced**, the page requires an existing Web Drop-in Advanced flow, PayNow in Customer Area, and handling of an additional action with `action.type: qrCode`. It says no additional PayNow parameter is needed in `/payments`; individual import is again optional. The Advanced base-guide URL contains an encoded, unresolved platform template, while the action-handling link explicitly names Web. Use this page's explicit Web scope and verify the prerequisite destination before implementation. See raw lines 67–95.
- Before accepting live payments, the page says to contact Adyen Support to add PayNow in the **live Customer Area**. It describes small-amount “penny” testing in **live** with a real banking app scanning a test QR and checking the live Customer Area payment list. This is a live banking action involving real funds, not a harmless sandbox exercise or proof that a particular transfer settled. See raw lines 55–65 and 97–107.
- The source **recommends against testing in the test Customer Area** because it says test-environment bank transfers cannot be reversed and funds will be deducted from the bank account. This warning applies to both flow sections and should remain visible alongside any testing directions. This guide gives no QR expiry duration or full asynchronous outcome/webhook procedure; a displayed QR or scan alone does not establish a completed payment. See raw lines 61–65 and 103–107.

## Detail locators

- **Sessions prerequisites, v68 gate and no-extra-fields statement:** raw lines 25–41.
- **Optional PayNow import:** raw lines 43–53 and 79–89.
- **Advanced prerequisite URL, QR action and no-extra-fields statement:** raw lines 67–95.
- **Live enablement, penny test, payment-list and nonreversible-test warning:** raw lines 55–65 and 97–107.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-paynow]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paynow/web-drop-in/2026-09-15|PayNow Web Drop-in guide — captured 2026-09-15]]
