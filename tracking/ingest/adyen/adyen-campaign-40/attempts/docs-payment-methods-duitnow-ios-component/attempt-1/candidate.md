---
title: "Adyen DuitNow iOS Component guide"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/duitnow/ios-component"
raw_files:
  - "adyen/docs/payment-methods/duitnow/ios-component/2026-09-15.md"
tags: [adyen, duitnow, ios, components, qr, malaysia]
---

## Overview

This 2026-09-15 captured Adyen guide adds DuitNow to an existing iOS Components integration, with Sessions and Advanced server-side prerequisites. It describes a `DuitNowComponent`, server-side `/payments`, a `Pending` response carrying QR-code action data, and a later payment outcome. This is an integration guide, not proof of present account enablement or a completed payment. See [[adyen]], [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-duitnow]] for the QR-only overview.

## Key takeaways

- Both server-side tabs require an existing Sessions or Advanced integration and ask the merchant to contact Adyen Support to add DuitNow in Customer Area. The method-discovery instructions specify `/paymentMethods` with `countryCode: MY`, `amount.currency: MYR`, and `channel: iOS`; decode the response and find type `duitnow`. The client constructs `APIContext` with client key and environment, then presents `DuitNowComponent` with a payment amount. The page does not pin an iOS SDK or minimum Checkout API version. Its `Environment.test` initialization and sample amount are examples, not a live-enablement or success guarantee.
- On Component `didSubmit`, send `data.paymentMethod` to the server and make `/payments`. The sample uses `paymentMethod.type: duitnow` and MYR. The illustrated response has `resultCode: Pending` and a `qrCode` action with `url` and `qrCodeData`; `Pending` is an intermediate state, not authorization, capture or settlement. The page says `action.url` downloads the QR image or `action.qrCodeData` can render it; the shopper scans it or uploads a screenshot to a bank app. No QR expiry or automatic completion rule is stated here.
- The opening sentence says the Component collects the shopper's selected bank, but the later setup and `/payments` examples show no bank field or bank-selection step. Preserve that mismatch rather than infer a required bank-selection payload. The QR section says "checkout page" despite this iOS Component scope.
- The result section says to use a `/payments/details` response `resultCode` on the frontend and also says the outcome arrives asynchronously by webhook. Its following table is headed as `resultCode` values but lists `AUTHORISATION` webhook `eventCode`/`success` pairs: `false` means failed and `true` means completed. The page does not show a required `/payments/details` call in its main QR path; it links an optional call for an additional use case. Reconcile implementation against the relevant Checkout API and webhook authority rather than treating the table as `/payments/details` result codes.
- The test section calls for real payment details and small amounts, Customer Area payment-list checks, and Support involvement to add DuitNow in the live Customer Area. Those instructions do not establish current eligibility or an executed test/live result.

## Detail locators

- Purpose, selected-bank statement, and Sessions/Advanced prerequisites: pinned raw lines 15–37.
- `/paymentMethods`, `APIContext`, and Swift `DuitNowComponent` setup: pinned raw lines 39–82.
- Component delegate and server `/payments` handoff: pinned raw lines 84–111; other language examples: lines 113–310.
- `Pending`, QR action fields, and shopper QR path: pinned raw lines 312–341.
- `/payments/details` wording, asynchronous webhook, `AUTHORISATION` table and optional-call link: pinned raw lines 342–355; testing and live Support steps: lines 357–363.

## Related

- [[adyen-online-payments]] — main online-payment and result-state concept
- [[source-adyen-docs-payment-methods-duitnow]] — DuitNow method overview and QR-only scope

## Raw Sources

- [[raw/adyen/docs/payment-methods/duitnow/ios-component/2026-09-15|DuitNow iOS Component guide, 2026-09-15]]
