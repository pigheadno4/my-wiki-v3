---
title: "Adyen MoMo Flutter Drop-in integration guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/momo-wallet/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/momo-wallet/flutter-drop-in/2026-09-15.md"
tags: [adyen, momo, flutter, drop-in, redirect, recurring]
---

## Overview

This [[adyen]] guide adds **MoMo** to an existing **Flutter Drop-in** integration under distinct **Sessions** and **Advanced** server-side flows. Both sections require handling a `redirect` action, then provide a separate merchant-server recurring-token path. It is an add-on to the main integration, not a complete independent Drop-in setup or proof of merchant enablement, payment, token creation or settlement. The examples use VND and TEST endpoints; those examples do not set merchant-wide currency or live eligibility. [[adyen-online-payments]]

## Key takeaways

- **Sessions setup:** The Sessions section calls for an existing Flutter Drop-in Sessions integration, **Checkout API v68 or later**, redirect handling, and contacting Adyen Support to add MoMo in Customer Area. Its embedded link for the Sessions integration-type row actually points to an **Advanced** guide; the heading and prose still say Sessions, so do not silently treat the link as authoritative Sessions instructions. For the base /sessions request it says no **additional MoMo parameters** are needed, and it says no extra MoMo configuration is needed. See raw lines 23–48.
- **Advanced setup:** The Advanced section calls for an existing Flutter Drop-in Advanced integration with redirect handling and says to add MoMo in Customer Area. It says no extra MoMo configuration or parameters for the **base** /payments call. The setup wording differs from the Sessions section's Support contact; this source does not resolve which route applies to a given merchant. See raw lines 299–321.
- **Recurring is a separate server route:** In both flow sections, token creation is described on **/payments** with `storePaymentMethod: true` and a shopper reference. Only **when the initial payment has settled** does the described `recurring.token.created` webhook provide a `storedPaymentMethodId`; the merchant server must receive recurring-token lifecycle events. Later /payments calls use that ID with the same shopper reference, `ContAuth`, and `Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed contracts. No-extra-parameters statements for the ordinary base requests do not cover this recurring route; this page does not spell out shopper consent. See raw lines 50–87 and 323–360.
- **Example qualification:** Curl, Java, PHP, C#, Node, Python and Ruby recurring examples use illustrative tokens, credentials, order IDs and VND/TEST values. The Java examples set `RecurringDetailReference` even though the surrounding prose and other examples say `storedPaymentMethodId`; the page does not reconcile those fields. Example library versions differ by language, and a sample call is not result verification. See raw lines 89–286 and 362–559.
- **Test/live gate:** Both flow sections describe MoMo's **test app and scenario credentials**, mobile-download versus desktop-QR test navigation, status lookup in TEST Customer Area, and a separate **live Customer Area request** before accepting live MoMo. They do not establish actual approval or an eventual authorization/capture/settlement result. See raw lines 288–297 and 561–570.

## Detail locators

- Sessions prerequisites, no-extra-base-parameter statements and recurring path: raw lines 23–87.
- Sessions example variations and test/live guidance: raw lines 89–297.
- Advanced prerequisites, base request, recurring path and examples: raw lines 299–559.
- Advanced test/live guidance: raw lines 561–570.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/momo-wallet/flutter-drop-in/2026-09-15|Adyen MoMo Flutter Drop-in snapshot]]
