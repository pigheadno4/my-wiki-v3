---
title: "Adyen DuitNow iOS Drop-in guide"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/duitnow/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/duitnow/ios-drop-in/2026-09-15.md"
tags: [adyen, duitnow, ios, drop-in, qr, malaysia]
---

## Overview

This 2026-09-15 captured Adyen guide adds DuitNow to an existing iOS Drop-in integration using a Sessions or Advanced server-side flow. Drop-in renders the method and generates a QR code for the shopper to pay with a participating-bank app. The guide also describes server `/payments`, a proposed `/payments/details` result path and asynchronous webhook outcomes. It does not prove present merchant enablement or a completed payment. See [[adyen]], [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-duitnow]] for the QR-only method overview.

## Key takeaways

- Both requirement tabs ask for an existing Sessions or Advanced integration and Support involvement in Customer Area, although their setup cells say only "add in your Customer Area" without naming DuitNow. `/paymentMethods` should specify `countryCode: MY`, `amount.currency: MYR` and `amount.value`. On `didSubmit`, pass `data.paymentMethod` from the client to the server for `/payments`; the sample request uses `paymentMethod.type: duitnow` and MYR. The sample v72 endpoint is an example, not a stated minimum Checkout API version; the page does not pin an iOS SDK version.
- The page says Drop-in generates the QR code. It does not show the `/payments` response, QR action fields, expiry, or an iOS QR presentation callback here; use the pinned raw and authoritative iOS Drop-in integration guidance for those details rather than importing a sibling guide's behavior.
- Its payment-result section says to use `state.data` from `onAdditionalDetails` for success or `onError` for unsuccessful/timed-out payments, then send `state.data.details` and `state.data.paymentData` to server `/payments/details`. These are Web-style callback/data names embedded in an iOS Drop-in page; the guide does not establish that they are the native iOS event API. Its example `details.redirectResult` also sits awkwardly beside this QR method. Treat the precise native result handoff as unresolved against the iOS Drop-in authority.
- The illustrated `/payments/details` response labels `Authorised` or `Refused` as payment results and uses `authorisedAmountCurrency: THB`, conflicting with the guide's MYR method-discovery and payment examples. Do not infer THB eligibility for DuitNow from this example. The page also says outcomes arrive asynchronously by webhook. Its following table is introduced as `resultCode` values but actually lists `AUTHORISATION` webhook `eventCode`/`success` pairs; those are not `/payments/details` result codes. A later sentence frames a details call as an additional-use-case option, in tension with the earlier step-by-step details call. This source does not settle the exact required iOS completion sequence.
- The test section calls for real payment details and small amounts, Customer Area payment-list checks, and Support involvement to add DuitNow in the live Customer Area. These instructions are not proof of current eligibility or an executed test/live payment.

## Detail locators

- iOS Drop-in purpose, QR app description, and Sessions/Advanced prerequisites: pinned raw lines 15–37.
- MY/MYR `/paymentMethods`, `didSubmit` and `/payments` handoff: pinned raw lines 39–78; other server-language examples: lines 80–277.
- Drop-in QR statement and Web-style `state.data` result-handler instructions: pinned raw lines 279–302.
- `/payments/details` response and THB/MYR example conflict: pinned raw lines 304–322 versus 45–47 and 68–75.
- Asynchronous webhook, mislabeled result table and additional-use-case details link: pinned raw lines 324–337; test/live steps: lines 339–345.

## Related

- [[adyen-online-payments]] — main online-payment and result-state concept
- [[source-adyen-docs-payment-methods-duitnow]] — DuitNow method overview and QR-only scope

## Raw Sources

- [[raw/adyen/docs/payment-methods/duitnow/ios-drop-in/2026-09-15|DuitNow iOS Drop-in guide, 2026-09-15]]
