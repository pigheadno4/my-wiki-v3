---
title: "Pix iOS Drop-in"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pix/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/pix/ios-drop-in/2026-09-15.md"
tags: [adyen, pix, ios, drop-in, qr-code, asynchronous-payments]
---

## Overview

This 2026-09-15-captured Adyen add-on describes Pix in an existing iOS Drop-in integration, with separate Sessions and Advanced flows. It covers request fields, the Advanced QR-code action, asynchronous test reconciliation, refund timing and live setup. See [[adyen]] and [[adyen-online-payments]]. This is a dated documentation snapshot, not evidence of current account eligibility or a completed Pix payment.

## Key takeaways

- Sessions requires an existing iOS Drop-in Sessions integration, Checkout API v68 or later, and Pix setup in Customer Area. Its /sessions table marks amount required; shopperName, socialSecurityNumber (CPF/CNPJ shown on the Pix form), shopperStatement (maximum 140 characters), and lineItems.id/amountIncludingTax are unmarked optional additions. The BR/BRL 10000 example has an app-style returnUrl and a 2021 sessionValidity value; it is sample data, not a reusable expiration setting. No additional Pix configuration is required. See raw lines 25–90 and 506–510.
- Advanced requires an existing iOS Drop-in Advanced integration, action handling for action.type qrCode, and Pix setup. Its /payments table marks paymentMethod and amount required; shopperName, socialSecurityNumber, shopperStatement, sessionValidity and line-item fields are unmarked optional. Sending shopperName and socialSecurityNumber is advice, not a requirement. The Advanced shopperStatement rule says a supplied value must be under 60 characters, distinct from the Sessions table's 140-character maximum. See raw lines 535–570.
- In Advanced, sessionValidity is described as Pix payment expiration: default one hour for Checkout API v71 or earlier and 24 hours for v72 or later. The response example has resultCode Pending and action.type qrCode plus pix.expirationDate in additionalData. QR-code presentation and an expiration value do not establish paid/final status; the page does not define a separate QR display lifetime. See raw lines 566 and 1058–1078.
- The page calls Pix asynchronous. In test, a pending offer can be promoted to sale in the test Customer Area; paid/promoted payments then appear in Payment list, and the page recommends using this to test reconciliation. It says a paid payment can be refunded within 90 days via Customer Area or API, and live Pix requires a request in the live Customer Area. These are documentation instructions, not performed operations. See raw lines 512–533 and 1080–1101.

> [!warning] iOS example and link qualifications
> The Advanced request table describes paymentMethod as state.data.paymentMethod from an onSubmit front-end event (raw line 561), wording to verify against the iOS Drop-in base integration. Its qrCode action-handling link points to a handle-the-redirect anchor (raw line 544). The Sessions sample sessionValidity is in 2021 and Advanced samples use 2025-10-01, both before this 2026 capture (raw lines 70, 600 and repeats); do not reuse those dates. The example pix.expirationDate describes the Pix payment response, not an independently documented QR display timer.

## Detail locators

- Sessions prerequisites and field table: raw `## Sessions flow Drop-in`, lines 25–49.
- Sessions BR/BRL sample, app returnUrl and historical sessionValidity: raw lines 51–90.
- Sessions configuration, refund and test/live guidance: raw lines 506–533.
- Advanced prerequisites and fields, including versioned expiration/default and flow-specific statement length: raw lines 535–570.
- Advanced sample request and historical validity: raw lines 572–612 and repeated language examples through 1056.
- Pending QR-code response and payment expiration field: raw lines 1058–1078.
- Advanced refund and test/live instructions: raw lines 1080–1101.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-classic-pix]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/pix/ios-drop-in/2026-09-15|Pix iOS Drop-in, captured 2026-09-15]]
