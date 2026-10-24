---
title: "Adyen GCash iOS Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gcash/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/gcash/ios-drop-in/2026-09-15.md"
tags: [adyen, gcash, ios, drop-in, recurring-payments]
---

## Overview

This [[adyen]] guide describes GCash-specific additions to an **existing iOS Drop-in** integration, with separate Sessions and Advanced server-side flows. It supplies base-request and recurring-token instructions, not a complete iOS integration or proof of a payment/settlement. See [[adyen-online-payments]] and [[adyen-tokenization]]. Captured 2026-09-15; ingested 2026-10-25. See raw lines 15–23.

## Base flow

- **Sessions:** Requires an existing Sessions iOS Drop-in integration, Checkout API **v68 or later**, and GCash added in Customer Area. The ordinary `/sessions` request needs no extra GCash parameters, and no extra GCash Drop-in configuration is specified. These are method-specific omissions, not substitutes for the main integration. See raw lines 25–46.
- **Advanced:** Requires an existing Advanced iOS Drop-in integration, handling `action.type: redirect`, and GCash added in Customer Area. Its ordinary `/payments` request and Drop-in configuration need no extra GCash-specific parameters. This section does not restate the Sessions v68 minimum. See raw lines 298–320.
- The base no-extra-parameter statements do **not** apply to token creation or later token-funded `/payments` requests. The Sessions recurring subsection itself uses `/payments` while the base Sessions flow uses `/sessions`; keep the contexts separate. See raw lines 38–46, 48–85, 316–359.

## Recurring and outcome boundary

- GCash supports recurring transactions in this guide. To create a token, the merchant includes `storePaymentMethod: true` and a unique `shopperReference` of **at least three characters** in `/payments`; its server must receive recurring token lifecycle webhooks. **After the payment has settled**, `recurring.token.created` supplies the shopper reference, initial payment `pspReference` as `eventId`, and `storedPaymentMethodId`. Initial request or redirect handling is not token issuance or settlement proof. See raw lines 48–71 and 322–345.
- Later `/payments` uses the stored method ID from that webhook (or the stated `/listRecurringDetails` alternative), the same shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` for fixed-interval contracts or `UnscheduledCardOnFile` for non-fixed intervals. Sample `Subscription`/`PHP` calls are examples, not guarantees of success or universal eligibility. See raw lines 73–107 and 347–382.
- The server snippets use a Checkout **TEST** `/checkout/v68/payments` endpoint, API-key placeholders and TEST library settings. Node/Python/Ruby examples label specific library versions and show idempotency-key use. These are example scopes, not an iOS SDK minimum, live setup or observed token payment. See raw lines 87–284 and 361–558.
- The repeated testing section says successful **live** GCash payment testing needs a real mobile number registered with GCash; **test** payment status is checked in test Customer Area; and accepting **live** GCash payments requires first submitting a request in live Customer Area. These distinct statements do not establish that a request was approved or a real payment completed. This page has no explicit final authorization webhook contract for the initial redirect transaction. See raw lines 286–296 and 560–570.

## Detail locators

- **Sessions prerequisites/base request:** raw lines 25–46.
- **Advanced redirect prerequisite/base request:** raw lines 298–320.
- **Three-character shopper reference, token creation and settled-payment webhook:** raw lines 48–71 and 322–345.
- **Later token fields/model:** raw lines 73–85 and 347–359.
- **TEST server examples and library labels:** raw lines 87–284 and 361–558.
- **Testing/live request gate:** raw lines 286–296 and 560–570.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen-webhooks]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/gcash/2026-09-15|GCash overview]] — PH/PHP method scope, redirect lifetime and channel routes; separate from this iOS Drop-in add-on.

## Raw Sources

- [[raw/adyen/docs/payment-methods/gcash/ios-drop-in/2026-09-15|GCash iOS Drop-in — captured 2026-09-15]]
