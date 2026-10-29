---
title: "Adyen Zip iOS Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/zip/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/zip/ios-drop-in/2026-09-15.md"
tags: [adyen, zip, ios, drop-in, redirect, recurring, online-payments]
---

## Overview

This captured [[adyen]] guide adds Zip to an existing iOS Drop-in integration. It provides endpoint-specific request fields and examples, a `/payments` redirect action, versioned Drop-in configuration notes, and a recurring-token route. It assumes Zip has been added in the **test** Customer Area; the guide does not establish live account eligibility. [[adyen-online-payments]]

## Key takeaways

- **Flow and version scope:** The guide requires an existing iOS Drop-in integration and Zip setup in the test Customer Area. Its `/sessions` tab is described as the default for Drop-in v5.0.0 or later. The `/payments` tab is for an implemented additional use case. Both v5+ and v4.x.x configuration tabs say no Zip-specific Drop-in integration is required; that statement does not erase the server request, redirect, or account-setup steps elsewhere on the page (raw lines 15–34, 681–683, 1391–1399).
- **Request details:** Both endpoint tables list shopper name, email, birth date, phone, billing/delivery addresses, and line items, but their Required cells are blank. They allow an optional line-item `imageURL` for Zip's product page, limited to 500 characters. The `/payments` table makes `paymentMethod.clickAndCollect: true` conditional on pickup instead of delivery. Examples use Zip `paymentMethod.type: zip`, AU/AUD, amount 1000, item lines totaling 1000, an app-scheme `returnUrl`, and test API endpoints. These AU examples do not state this guide's complete regional availability (raw lines 32–101, 681–752).
- **Redirect action:** For the `/payments` path, the response example gives `resultCode: RedirectShopper` with a `zip` redirect `action`. The guide says to use the action object to redirect the shopper. This response is an intermediate action, not a completed-payment result; return handling and final outcome are not specified in this page and belong to the linked base integration/webhook guidance (raw lines 1375–1389, 1642–1646).
- **Recurring route:** The guide says Zip supports recurring transactions. To create a token, it asks for `storePaymentMethod: true` and a unique `shopperReference` in an initial `/payments` request. **After settlement**, the `recurring.token.created` webhook supplies `storedPaymentMethodId`, and the server must be set up to receive recurring-token lifecycle events. Later `/payments` uses that ID, the same shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` or `UnscheduledCardOnFile` (raw lines 1401–1434).
- **Examples and gates:** The `/payments` curl sample contains literal `{hint:...}{/hint}` markup inside JSON, so it is illustrative rather than copy-ready. The recurring Java sample uses `setRecurringDetailReference` and omits `shopperReference`, in tension with the adjacent prose specifying `storedPaymentMethodId` and shopper reference; follow the prose and version-appropriate API contract. Test accounts are obtained from Zip test credentials; live acceptance requires a request in live Customer Area (raw lines 698–722, 1424–1432, 1459–1487, 1634–1640).

## Detail locators

- Identity, prerequisites, Sessions tab and field table: pinned raw lines 15–44; Sessions examples: lines 46–679.
- Payments tab, conditional pickup and request examples: pinned raw lines 681–1373.
- Redirect action and Drop-in configuration: pinned raw lines 1375–1399.
- Recurring token lifecycle and request examples: pinned raw lines 1401–1632; test/live and related links: lines 1634–1646.

## Related

- [[adyen-online-payments]] — online payment architecture and method routes.
- [[source-adyen-docs-payment-methods-zip]] — captured Zip method overview; use this iOS page for the Drop-in details.
- [[adyen-tokenization]] — tokenization context; the Zip-specific settlement/webhook sequence is in this pinned guide.

## Raw Sources

- [[raw/adyen/docs/payment-methods/zip/ios-drop-in/2026-09-15|Zip iOS Drop-in integration, captured 2026-09-15]]
