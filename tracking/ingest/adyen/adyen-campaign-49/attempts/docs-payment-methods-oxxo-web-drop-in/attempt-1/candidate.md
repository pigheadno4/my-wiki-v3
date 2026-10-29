---
title: "Adyen OXXO Web Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/oxxo/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/oxxo/web-drop-in/2026-09-15.md"
tags: [adyen, oxxo, web, drop-in, voucher, webhooks, online-payments]
---

## Overview

This 2026-09-15-captured Adyen guide adds OXXO to an existing Web Drop-in integration. It separates Sessions and Advanced method-specific requirements and explains the offline voucher status and webhook sequence, test simulation, and live request gate. It is a supplement to [[adyen-online-payments]], not a complete base integration or evidence of an executed OXXO payment. [[adyen]]

## Key takeaways

- **Sessions flow:** Start with an existing Web Drop-in Sessions integration, Checkout API **v68 or later**, and OXXO added in Customer Area. The page says no extra OXXO-specific `/sessions` parameters are needed. Importing `Oxxo` individually is optional tree shaking; the example imports `AdyenCheckout`, `Dropin`, and `Oxxo`. This does not waive base session requirements. [Raw: lines 25–53]
- **Advanced flow:** Start with an existing Web Drop-in Advanced integration able to handle `action.type: voucher` and with OXXO added in Customer Area. The page says no extra OXXO-specific `/payments` parameters are needed, and `Oxxo` can again be optionally imported. It states no Advanced Checkout API minimum. Its Advanced integration link contains an unresolved encoded `platform` template, and its voucher action requirement points to a generic “handle the redirect” base anchor; follow the explicit voucher action rather than treating that anchor as a redirect action. [Raw: lines 80–108]
- **Voucher versus payment state:** OXXO is offline. On voucher creation, Customer Area shows an offer with **Open** status; a method-specific `PENDING` webhook is received only if configured. The page says webhooks are needed to follow voucher status. After the shopper actually pays at an OXXO store, the offer becomes a sale with **Received** status, and the final payment result comes through an `AUTHORISATION` webhook. Voucher issue, Open state, or optional PENDING notification is not final payment. [Raw: lines 57–65, 112–120]
- **Test and live:** In test Customer Area, manually promote a pending OXXO offer to a sale under **Payments > Offers** using its PSP reference; paid or promoted test vouchers appear under **Payment list**, and this can test reconciliation. Before live acceptance, submit a request to add OXXO in the live Customer Area. The page describes automatic transition after shopper payment in live, but the manual promotion is a test simulation, not evidence of a live sale. [Raw: lines 67–78, 122–133]
- **Overview context:** The separately approved [[source-adyen-docs-payment-methods-oxxo]] overview says OXXO confirmation typically arrives within one business day, possibly longer, and gives an unpaid due-date/seven-day open-then-expiry statement. This child guide does not restate that timing; use the overview as the source for it. [Overview raw: lines 29–31]

## Detail locators

- Sessions prerequisites, no extra fields, optional import: pinned raw lines 25–53.
- Advanced voucher action, no extra fields and link defects: pinned raw lines 80–108.
- Offline Open/Received offer states and conditional PENDING/final AUTHORISATION webhooks: pinned raw lines 57–65 and 112–120.
- Test promotion and live method request: pinned raw lines 67–78 and 122–133.

## Related

- [[adyen-online-payments]] — provider integration and method routes.
- [[source-adyen-docs-payment-methods-oxxo]] — approved overview for cash-voucher shopper journey and delayed confirmation/expiry timing.

## Raw Sources

- [[raw/adyen/docs/payment-methods/oxxo/web-drop-in/2026-09-15|OXXO Web Drop-in guide, captured 2026-09-15]]
