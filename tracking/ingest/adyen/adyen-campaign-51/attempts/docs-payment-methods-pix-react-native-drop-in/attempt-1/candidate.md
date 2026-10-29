---
title: "Adyen Pix React Native Drop-in"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pix/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/pix/react-native-drop-in/2026-09-15.md"
tags: [adyen, pix, react-native, drop-in, qr-code, brazil, asynchronous-payments]
---

## Overview

This 2026-09-15-captured Adyen guide adds Pix-specific steps to an **existing React Native Drop-in** integration, separately for Sessions and Advanced server-side flows. It covers request additions, a QR-code action in Advanced flow, refund timing, and a test-only way to simulate settlement. See [[adyen]] and [[adyen-online-payments]]. Its BR/BRL examples and test instructions do not establish current merchant eligibility or a successful live payment.

## Key takeaways

- **Sessions:** Use an existing React Native Drop-in Sessions integration, Checkout API **v68 or later**, and Pix added in Customer Area. The Pix-specific /sessions table marks **amount** required; shopperName, socialSecurityNumber (CPF/CNPJ), shopperStatement and line-item fields are unmarked. It states a **140-character** maximum for shopperStatement. The BR/BRL and app-scheme return URL are examples; the shown 2021 sessionValidity is a dated sample value. No extra Pix configuration is stated. See raw lines 25–50, 52–92 and 507–511.
- **Advanced:** Use an existing React Native Drop-in Advanced integration that handles **action.type qrCode**, with Pix added in Customer Area. The /payments table marks **paymentMethod** from front-end onSubmit state.data.paymentMethod and **amount** required. It calls shopperName and socialSecurityNumber optional but advises sending both so the shopper can identify the payment. The Advanced shopperStatement guidance says to keep a provided value **under 60 characters**, distinct from the Sessions 140-character limit. Optional sessionValidity is the Pix payment expiration; its stated default is **1 hour with Checkout API v71 or earlier** and **24 hours with v72 or later**. The Advanced requirements table does not state a Checkout API minimum; a v72 example is not a new minimum. No extra Pix configuration is stated. See raw lines 532–567.
- **Outcome and test boundary:** The illustrated Advanced response is **Pending** with a **qrCode** action and qrCodeData; QR creation is not paid status. Pix is asynchronous. In the **test** Customer Area, the guide says a pending offer can be promoted to sale and used to test reconciliation; paid test offers then appear in Payment list. Live acceptance requires a separate Pix request in live Customer Area. None of these instructions proves a real payment was made. See raw lines 1055–1075 and 1081–1094.
- **Refunds:** The guide says a Pix payment can be refunded within **90 days after payment** through Customer Area or API. It does not show an executed refund. See raw lines 513–515 and 1077–1079.

## Source cautions

- The **Sessions** prerequisite names React Native Drop-in Sessions but its link points to **Advanced flow**; the later create-session link points to Sessions. Verify the correct base guide before using that link. See raw lines 33 and 41.
- The **Advanced** qrCode action-handling requirement links to an anchor named **handle-the-redirect**. Do not infer from the anchor that the Pix action is a redirect; the stated action type and example are qrCode. See raw lines 540–541 and 1055–1075.
- The /sessions example includes paymentMethod.type pix even though this method-specific Sessions field table only marks amount required; do not promote an example field into a universal Sessions requirement. Example sessionValidity dates predate the capture and are not current expiry instructions. See raw lines 43–50, 71–75, 286–290, 563 and 597.

## Detail locators

- Sessions prerequisites and parameter requiredness: pinned raw lines 25–50.
- Sessions BR/BRL examples and no-extra-configuration: pinned raw lines 52–511.
- Advanced prerequisites, request fields, versioned expiry and optional identity data: pinned raw lines 532–567.
- Advanced examples, Pending QR action, refund rule and test/live process: pinned raw lines 569–1094.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/pix/react-native-drop-in/2026-09-15|Fully read Pix React Native Drop-in raw]]
