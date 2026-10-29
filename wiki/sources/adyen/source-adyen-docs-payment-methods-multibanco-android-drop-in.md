---
title: "Multibanco Android Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/multibanco/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/multibanco/android-drop-in/2026-09-15.md"
tags: [adyen, multibanco, android, drop-in, voucher, portugal]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Multibanco to an existing Android Drop-in** integration using Sessions or Advanced server-side flow. It says no Multibanco-specific request or configuration parameters are needed, but the Advanced flow must handle a voucher action. It also describes test Customer Area offer promotion and live setup. This add-on is not a full base integration or proof that a voucher has been redeemed or a live merchant is enabled. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions:** use an existing Android Drop-in Sessions integration with Checkout API **v68 or later** and add Multibanco in Customer Area. The guide says no extra Multibanco parameters are needed when creating `/sessions`, and no extra configuration is needed. “No extra” is relative to the existing base integration, not a claim that an API request can omit base fields (raw lines 25–46).
- **Advanced:** use an existing Android Drop-in Advanced integration configured to handle `action.type: voucher`, and add Multibanco in Customer Area. The guide says no extra Multibanco parameters are needed for `/payments` or configuration; it does not override the base flow's required request fields (raw lines 67–87).
- **Test and live:** request Multibanco in **test Customer Area** before testing. To simulate a paid test payment, the guide instructs a user to select the pending offer's PSP reference under **Payments > Offers** and choose **Promote offer to sale**; then test reconciliation. Paid offers appear under **Payments > Payment list**. A separate request in **live Customer Area** is required before accepting live payments. Test promotion is simulation, not evidence that a shopper redeemed a real voucher (raw lines 50–65, 89–104).
- The separate [[source-adyen-docs-payment-methods-multibanco|Multibanco overview]] explains that the shopper receives a voucher with payment reference, entity number, amount and expiry, then pays at an ATM or through online banking. It labels the method **PT/EUR** and gives capability indicators. Thus creating the voucher is not itself payment completion; this Android child guide does not restate those method-level voucher fields or redemption rules (overview pinned raw lines 23–36).

## Detail locators

- Add-on scope and Sessions requirements/no-extra-parameter/configuration statements: raw lines 15–46.
- Sessions test Customer Area promotion/reconciliation and live request: raw lines 50–65.
- Advanced requirements, voucher action and no-extra statements: raw lines 67–87.
- Advanced test/live instructions: raw lines 89–104.
- Method-level voucher fields, redemption and PT/EUR matrix: [[source-adyen-docs-payment-methods-multibanco]] and its pinned raw lines 23–36; this entry's raw_files remains child-only.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-multibanco]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/multibanco/android-drop-in/2026-09-15|Multibanco Android Drop-in guide, captured 2026-09-15]]
