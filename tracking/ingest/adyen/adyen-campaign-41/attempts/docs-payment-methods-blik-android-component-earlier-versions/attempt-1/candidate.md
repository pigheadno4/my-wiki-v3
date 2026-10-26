---
title: "BLIK Android Component v4.x.x integration | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/blik/android-component/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/blik/android-component/earlier-versions/2026-09-15.md"
tags: [adyen, blik, android, components, earlier-versions, await-action]
---

## Overview

This Adyen earlier-versions page is headed BLIK Android Component v4.x.x and describes adding it to an existing Android Components integration. Its requirements say Components v3.8.0 or later and BLIK added in the test Customer Area. The procedure configures a BLIK Component, obtains the `blik` payment method from `/paymentMethods`, collects client state for a server `/payments` call, handles an `await` action and sends its details to the server for `/payments/details`. The page does not define the server payment request, result-code meanings, final webhook outcome or a One Click token flow (raw lines 15–26, 28–168).

## Key takeaways

- The setup snippets use `com.adyen.checkout:blik:<latest-version>`, `BlikConfiguration` with a client key and TEST environment, and `BlikView`. The title's v4.x.x scope and the separate v3.8.0 minimum should not be treated as proof of current/latest SDK behavior (raw lines 15–55).
- The guide says the client-side Component collects a **phone number** and receives updates as the shopper enters it, then sends valid `paymentComponentState.data.paymentMethod` to the server. That wording conflicts with its own BLIK-with-code TEST instruction to use `999000`, and with the linked [[source-adyen-docs-payment-methods-blik]] overview's six-digit-code shopper path. The page does not reconcile the phone-number versus code input (this raw lines 57–90, 158–164; overview raw lines 23–36).
- For an `await` action from `/payments`, the client deserializes the action, adds `com.adyen.checkout:await:<latest-version>`, builds an `AwaitConfiguration`, initializes `AwaitComponent`, and calls `handleAction`. The observer's `actionComponentData` is then passed to the merchant server for `/payments/details` (raw lines 94–147). The observer snippet spells the instance `awaitcomponent` after earlier initializing `awaitComponent`; treat the snippet as illustrative rather than copy-ready (raw lines 130–155).
- Navigation and example labels are inconsistent: the Components prerequisite link points to `/online-payments//`; the `/payments/details` link uses an Android **Drop-in** base guide, and See also points to a **Sessions** Components guide, while the collection/`/payments` links point to **Advanced** Components. These links do not establish a coherent Sessions implementation for this v4.x.x procedure (raw lines 25, 61, 98, 147, 170–174).
- TEST guidance says to use BLIK code `999000`, satisfy BLIK guidelines and test end to end. Live acceptance requires BLIK in the live Customer Area; neither step proves activation or payment success (raw lines 158–168).

## Detail locators

- v4.x.x scope, v3.8.0 minimum and test Customer Area gate: raw lines 15–26.
- BLIK Component dependency, configuration and view: raw lines 28–55.
- Phone-number wording, `blik` discovery and valid component-state handoff: raw lines 57–92.
- Await dependency, action handling, details handoff and example typo: raw lines 94–155.
- TEST code and live gate: raw lines 158–168.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-android-sdk]]
- [[source-adyen-docs-payment-methods-blik]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/blik/android-component/earlier-versions/2026-09-15|BLIK Android Component v4.x.x, fetched 2026-09-15]]
