---
title: "DANA React Native Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/dana/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/dana/react-native-drop-in/2026-09-15.md"
tags: [adyen, dana, react-native, drop-in, wallets]
---

## Overview

Adyen's 2026-09-15 DANA React Native Drop-in page describes method-specific additions to an existing React Native Drop-in integration, split by Sessions and Advanced server-side flow. The linked base integration guides supply the general request, redirect, and payment-result handling. This snapshot does not prove current DANA eligibility, token issuance, or a completed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions:** The page requires an existing React Native Drop-in Sessions integration, Checkout API v68 or later, handling `action.type: redirect`, and adding DANA in Customer Area. It says no DANA-specific extra `/sessions` parameters or Drop-in configuration are needed. Its Sessions requirement text links to an **Advanced** React Native Drop-in URL, while the redirect and create-session links point to Sessions; follow the named flow, and treat the prerequisite URL as a source inconsistency. [Raw lines 25–48]
- **Advanced:** The page requires an existing React Native Drop-in Advanced integration, redirect handling, and DANA in Customer Area. It says no DANA-specific extra configuration or ordinary `/payments` parameters are needed. This ordinary-payment statement does not erase the separate recurring request fields below. [Raw lines 298–320]
- **Recurring:** For token creation, the page instructs `storePaymentMethod: true` and a unique `shopperReference` in `/payments`. After the initial payment settles, a `recurring.token.created` webhook contains `storedPaymentMethodId`; the merchant server needs to receive recurring-token lifecycle webhooks. Later token payments use that ID, the shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` for fixed intervals or `UnscheduledCardOnFile` otherwise. Redirect return or initial request is not token issuance or final settlement. [Raw lines 50–87, 322–359]
- **TEST/live:** Example recurring requests use `paymentMethod.type: dana`, IDR amounts, and TEST endpoints or clients, which are examples rather than an eligibility matrix or execution proof. The page says live payment testing needs a real mobile number registered with DANA, test payments can be checked in Customer Area, and a DANA request in live Customer Area precedes live acceptance. The phrase “test successful DANA live payments” mixes TEST/live wording; do not infer a TEST simulator from it. [Raw lines 89–285, 288–296, 361–568]

## Detail locators

- Server-side recurring `/payments` samples in curl, Java, PHP, C#, Node, Python, and Ruby: raw lines 89–285 and 361–557. The explicit Checkout API v68+ gate is under Sessions only; no React Native SDK version is stated here.
- Redirect completion, payment authorization/capture/settlement beyond the token-created timing, and failure outcomes require the linked base flow and status evidence.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/dana/react-native-drop-in/2026-09-15|DANA React Native Drop-in (2026-09-15)]]
