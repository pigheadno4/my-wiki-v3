---
title: "MoMo Web Drop-in integration"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/momo-wallet/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/momo-wallet/web-drop-in/2026-09-15.md"
tags: [adyen, momo, wallet, web, drop-in, recurring]
---

## Overview

This 2026-09-15 Adyen guide adds **MoMo** to an existing **Web Drop-in** integration. It separates Sessions and Advanced redirect prerequisites, ordinary request additions, a recurring-token sequence, and TEST/live steps. The page is an integration guide; its snippets and status-check directions do not show a completed payment or merchant enablement. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions base:** an existing Sessions-flow Web Drop-in, **Checkout API v68 or later**, redirect handling for `action.type: redirect`, and MoMo added in Customer Area are stated prerequisites. The ordinary `/sessions` creation step requires no MoMo-specific additional parameters. Importing `Redirect` alongside `AdyenCheckout` and `Dropin` is explicitly optional for tree shaking. (raw lines 25–54)
- **Advanced base:** an existing Advanced-flow Web Drop-in, redirect handling for `action.type: redirect`, and MoMo added in Customer Area are stated. The ordinary `/payments` step says no additional MoMo-specific parameters; unlike the Sessions prerequisite table, this section states no Checkout API minimum. Its integration-type link contains an encoded `{{getParameter('platform')}}` placeholder, while the redirect-handling link names `platform=Web`; verify the main Advanced Web guide rather than treating that malformed link as a new platform. Optional `Redirect` import is again shown. (raw lines 307–335)
- **Conditional recurring route in both sections:** to create a shopper token, the page says to send `storePaymentMethod: true` and a unique `shopperReference` in a `/payments` request. After the **initial payment has settled**, it says a `recurring.token.created` webhook carries `shopperReference`, `eventId` (initial `pspReference`) and `storedPaymentMethodId`; the server must receive recurring-token lifecycle webhooks. Later token payments use `paymentMethod.storedPaymentMethodId`, the same shopper reference, `shopperInteraction: ContAuth`, and `Subscription` for fixed-interval or `UnscheduledCardOnFile` for non-fixed contracts. These recurring fields are a separate conditional path, so the base “no additional parameters” sentences do not waive them. Token receipt and payment success are conditional, not observed here. (raw lines 56–93, 337–374)
- **Snippet and endpoint qualifications:** recurring examples are TEST-oriented and show `momo_wallet`, VND and placeholder keys/IDs. They use a v68 `/payments` URL in curl examples, which is not an independently stated Advanced minimum. The Java examples set `RecurringDetailReference` while the prose and other samples use `storedPaymentMethodId`; retain that field-name discrepancy for implementation review. The example amounts also vary (Java VND 15000 versus most samples VND 1000). (raw lines 95–292, 376–573)
- **TEST/LIVE boundary:** for TEST, the page points to a MoMo test app and scenario-specific test credentials, with desktop QR scanning versus a mobile-browser download path, and a Customer Area test-payment status list. Before live MoMo acceptance, it says to submit a request in **live Customer Area**. These directions do not prove a tested authorization, settled token creation, a subsequent recurring charge, or live merchant approval. (raw lines 294–305, 575–586)

## Detail locators

- Sessions prerequisites, no-extra-parameter statement and optional import: raw lines 25–54.
- Sessions recurring creation, webhook timing and later-token fields: raw lines 56–93.
- Sessions multi-language TEST examples: raw lines 95–292.
- Sessions TEST and live setup directions: raw lines 294–305.
- Advanced prerequisites, optional import and ordinary `/payments` wording: raw lines 307–335.
- Advanced recurring sequence and multi-language examples: raw lines 337–573.
- Advanced TEST and live setup directions: raw lines 575–586.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-momo-wallet]]
- [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/momo-wallet/web-drop-in/2026-09-15|Adyen MoMo Web Drop-in, 2026-09-15 snapshot]]
