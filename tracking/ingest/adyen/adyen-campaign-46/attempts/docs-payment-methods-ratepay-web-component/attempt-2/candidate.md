---
title: "Ratepay Web Component | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ratepay/web-component"
raw_files:
  - "adyen/docs/payment-methods/ratepay/web-component/2026-09-15.md"
tags: [adyen, ratepay, web, components, open-invoice, direct-debit]
---

## Overview

This [[adyen|Adyen]] page, captured 2026-09-15 and marked last modified 2019-09-06, describes adding the Ratepay Component to an existing **Web Components** integration. It covers two distinct payment methods, **Ratepay Open Invoice** and **Ratepay Direct Debit**, along with shopper/order data, Ratepay device fingerprinting, request/result handling, invoice capture and modifications. See [[adyen-online-payments]]. It is historical captured documentation, not proof of current merchant or shopper availability.

## Key takeaways

- Build the Web Components integration and add Ratepay in the **test** Customer Area first (raw lines 28–33). For Web Components v6, the page shows a `RatePay` import (lines 35–41). Its `/paymentMethods` country/currency pairs are **AT/EUR, DE/EUR, NL/EUR (v3.22.1 or later), and CH/CHF**; the returned method types are `ratepay` for Open Invoice and `ratepay_directdebit` for Direct Debit (**v5.13.0 or later**) (lines 43–63). These are documented discovery pairs, not a live-eligibility guarantee.
- The Component collects payment-form details. Optional prefill and `visibility` settings differ by Open Invoice and Direct Debit; the raw gives property tables and defaults (lines 75–289). Before `/payments`, implement Ratepay device fingerprinting and send the calculated `deviceFingerprint`; the page says Ratepay uses it for risk evaluation (lines 21–25, 291–293). After valid Component `onSubmit`, pass `state.data` to the server for `/payments` (lines 295–299).
- Both request tables mark shopper name, telephone, email, date of birth, billing address, fingerprint and `lineItems` required; `deliveryAddress` is required only when different from billing (Open Invoice lines 301–314; Direct Debit lines 971–990). Open Invoice uses `paymentMethod.type: ratepay`. Direct Debit uses `ratepay_directdebit` and additionally requires bank country, IBAN and account-holder name; it is **not available for shoppers in Switzerland** (lines 971–990). The Direct Debit **curl** sample nevertheless sends `paymentMethod.type: ratepay` at lines 1012–1014, and its other language samples likewise retain `ratepay`; do not copy them as a validated Direct Debit request. Prefill labels `bankAccount.ibanNumber` (lines 127, 216), while the Direct Debit request table specifies `bankAccount.iban` (line 988); distinguish UI prefill data from the server request.
- The response section lists `resultCode`, `pspReference` and `merchantReference`; **Open Invoice only** also lists `additionalData.openinvoicedata.descriptor` for the bank-transfer purpose printed on the invoice (lines 2323–2341). The result table lists `Authorised`, `Cancelled` and `Refused` and actions for the shopper (lines 2343–2353). A sample `Authorised` response is authorisation evidence in the example, not capture, invoice delivery or settlement proof.
- The capture section explicitly applies **only to Open Invoice**: manually capture after sending goods even if automatic capture is enabled elsewhere; capture triggers the invoice to be sent (lines 2355–2359). Partial capture supplies the payment amount and `additionalData.openinvoicedata` item data; manually cancel any unclaimed remainder (lines 2361–2411). Multiple partial captures require Support setup and create a new invoice per capture (lines 2411–2413). Before capture, cancel; after capture, refund. Partial refunds use `modificationAmount`, `acquirerReference` if multiple partial captures are available, and Open Invoice item data only for Open Invoice (lines 2415–2459).
- Before live acceptance, the page says to request Ratepay in **live** Customer Area and provide Ratepay live credentials; test payment status can be checked in test Customer Area (lines 2461–2467). This does not establish that any account has live access or that a payment succeeded.

## Detail locators

- Purpose, shopper/order/fingerprint/capture prerequisites: raw lines 15–33; Web v6 import: 35–41.
- Country/currency, method types and Component setup: lines 43–73.
- Optional prefill and visibility by product: lines 75–289; `ibanNumber` prefill labels at 127 and 216.
- Fingerprint, Component submission and Open Invoice request table: lines 291–314; Open Invoice examples: 316–969.
- Direct Debit restriction, required bank fields and request examples: lines 971–2321; table type at 977 and curl sample type at 1012–1014.
- Response and `resultCode`: lines 2323–2353; Open Invoice manual/partial capture: 2355–2413.
- Cancel/refund and partial-refund detail: lines 2415–2459; test/live gate: 2461–2467.

## Related

- [[adyen-online-payments]] — provider online-payment integration concept.

## Raw Sources

- [[raw/adyen/docs/payment-methods/ratepay/web-component/2026-09-15|2026-09-15 Ratepay Web Component guide]]
