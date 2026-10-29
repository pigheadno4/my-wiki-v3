---
title: "Cash App Pay iOS Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cash-app-pay/ios-component"
raw_files:
  - "adyen/docs/payment-methods/cash-app-pay/ios-component/2026-09-15.md"
tags: [adyen, cash-app-pay, ios, components, tokenization]
---

## Overview

This 2026-09-15 guide adds **Cash App Pay** to an existing Adyen iOS Components integration, with Sessions and Advanced paths, app return handling, payment results, and optional recurring token use. Cash App Pay here is the wallet method described in [[source-adyen-docs-payment-methods-cash-app-pay]], distinct from Cash App Afterpay. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Both flow requirement tables state an iOS Components minimum of **5.2.0**, require the **Recurring tokens life cycle events** webhook, and say to add Cash App Pay in Customer Area using a Cash App client ID, then enable **Recurring details** under Developer → Additional data → Payment. The Swift Package Manager installation section separately says choose Adyen iOS version **at least v5.42.0** and include `AdyenCashAppPay`; CocoaPods uses `Adyen/CashAppPay`. Preserve the two version statements as separately scoped guide text, not a single inferred minimum. See raw lines 18–57.
- The API reference says there are no **additional Cash App Pay-specific** fields to send for the base `/sessions` or `/payments` integration. For both UI paths the guide configures a redirect URL, creates `CashAppPayComponent`, and presents its view. Sessions sets `AdyenSession` as delegate. In Advanced, the shopper authorizes in the Cash App Pay app; on return, `didSubmit` supplies `data.paymentMethod` for the server, while `didFail` is the client error callback. This does not mean no base request or callback work. See raw lines 59–120.
- Show the result from `/payments/details` and reconcile with the asynchronous payment webhook. **Received** means the shopper completed their step but the final result is still unknown; an **AUTHORISATION** webhook follows when status updates. **Authorised** is successful, with manual capture still needed when configured. **Cancelled**, **Error**, and **Refused** are separate outcomes. Do not fulfill solely from Received. See raw lines 131–143.
- Cash App Pay tokenization supports future recurring or card-on-file payments; the guide strongly recommends explicit shopper permission. In Sessions, `storedPaymentMethodMode` has `disabled` (default), `askForConsent`, and `enabled` choices, with `shopperReference` conditions for the latter two. In Advanced, token creation passes the client `data.storePaymentMethod` plus unique `shopperReference` in `/payments`. Tokenized later payments use the submitted `data.paymentMethod`; a `recurring.token.disabled` webhook indicates shopper-deleted stored details and calls for removing the unusable token. See raw lines 145–169, 181–206, and 250–284.
- The guide recommends obtaining the shopper's **$cashtag** for recognizable recurring payments. It comes from `/payments/details` additional data after enabling **Token information for digital wallets**; the token-created webhook lacks the $cashtag. Sessions users who want that data for recurring payments are told to switch to Advanced and implement `/payments/details` and `/payments`. Including `paymentMethod.cashtag` on a later token payment is optional. See raw lines 171–175 and 208–263.
- Test with the Cash App Pay test environment and sandbox magic values, inspect test payments in Customer Area, and add Cash App Pay in the **live Customer Area** before going live. These instructions are not proof of live enablement or payment execution. See raw lines 287–291.

> [!warning] Configuration names and examples
> The optional configuration table names `showsStorePaymentField` and `storePaymentMethod` (raw lines 122–129), while later Advanced token text uses `showsStorePaymentMethodField` (lines 185–192); Sessions text refers to `storedPaymentMethod` (lines 165–169). Preserve each spelling and check the versioned SDK before copying token configuration. The `/payments/details` response example at lines 227–248 includes a misspelled `merchantRreference` key and is an example, not a complete schema. The linked method overview labels Cash App Pay “Direct” (overview raw lines 23–27), while this child describes an iOS app authorization/return using a redirect URL (child lines 72–108); do not infer that “Direct” means no app switch.

## Detail locators

- Flow requirements and library versions: raw lines 18–57.
- API scope, Component configuration and callbacks: raw lines 59–120.
- Payment result codes and asynchronous webhook: raw lines 131–143.
- Token settings, cashtag retrieval, later token payments and disabled-token event: raw lines 145–284.
- Test and live setup: raw lines 287–291.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-cash-app-pay]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cash-app-pay/ios-component/2026-09-15|Cash App Pay iOS Component, captured 2026-09-15]]
