---
title: "Adyen Multibanco iOS Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/multibanco/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/multibanco/ios-drop-in/2026-09-15.md"
tags: [adyen, multibanco, ios, drop-in, voucher, online-payments]
---

## Overview

This 2026-09-15-captured Adyen guide adds Multibanco to an existing iOS Drop-in integration. It gives separate Sessions and Advanced flow requirements and describes test offer promotion and live setup. It supplies only Multibanco-specific additions, not the entire base integration. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions flow:** Start with an existing iOS Sessions-flow Drop-in integration using Checkout API v68 or later, and add Multibanco in Customer Area. The page says no additional Multibanco parameters are needed for `/sessions` and no additional Drop-in configuration is needed. These are method-specific statements; the underlying session request and SDK setup still follow the base guide. [Raw: lines 25–46]
- **Advanced flow:** Start with an existing iOS Advanced-flow Drop-in integration that handles `action.type: voucher`, and add Multibanco in Customer Area. The page says no extra Multibanco configuration or `/payments` parameters are needed. It does not state an Advanced-specific Checkout API minimum or reproduce the base request. [Raw: lines 67–89]
- **Voucher and payment state:** The Advanced action is a voucher, consistent with the approved [[source-adyen-docs-payment-methods-multibanco]] overview's description of a shopper paying later at an ATM or through online banking. This iOS guide does not say that rendering the voucher completes payment; its test procedure begins from a **pending** Multibanco payment. Treat offer-to-sale promotion as a test simulation, not an automatic live capture or proof of shopper payment. [Child raw: lines 75–76, 95–106; overview source: raw lines 23–32]
- **Test and live gates:** Before testing, submit a request for Multibanco in test Customer Area. The documented test simulation selects the pending payment's PSP reference under **Payments > Offers** and **Promote offer to sale**; promoted test offers appear in **Payment list**, and the page recommends using this to test reconciliation. Before live acceptance, submit a separate request in live Customer Area. These steps appear in both Sessions and Advanced sections. [Raw: lines 50–65, 93–108]

## Detail locators

- Sessions integration/version, setup, no-extra-parameter/configuration statements: pinned raw lines 25–46.
- Sessions test simulation and live gate: pinned raw lines 48–65.
- Advanced voucher action, no-extra-parameter/configuration statements: pinned raw lines 67–89.
- Advanced test simulation and live gate: pinned raw lines 91–108.

## Related

- [[adyen-online-payments]] — provider integration and method routes.
- [[source-adyen-docs-payment-methods-multibanco]] — approved overview for voucher contents, subsequent shopper payment, and PT/EUR method context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/multibanco/ios-drop-in/2026-09-15|Multibanco iOS Drop-in guide, captured 2026-09-15]]
