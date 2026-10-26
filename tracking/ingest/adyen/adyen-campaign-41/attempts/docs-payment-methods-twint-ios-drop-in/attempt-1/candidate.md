---
title: "TWINT iOS Drop-in integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/twint/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/twint/ios-drop-in/2026-09-15.md"
tags: [adyen, twint, ios, drop-in, online-payments, tokenization]
---

## Overview

This 2026-09-15 TWINT iOS Drop-in guide describes **method-specific additions** to an existing Sessions or Advanced integration. It distinguishes ordinary method addition, Advanced redirect handling, and a separate server-side recurring-token path. The page does not establish current account enablement or a successful payment outcome. [[adyen]] [[adyen-online-payments]] [[adyen-ios-sdk]]

## Key takeaways

- **Sessions:** use an existing iOS Drop-in Sessions flow with Checkout API **v68 or later**, and add TWINT in Customer Area before beginning. The page says no TWINT-specific parameters are needed when creating the ordinary `/sessions` payment session and no TWINT-specific Drop-in configuration is needed. See raw lines 25–46.
- **Advanced:** use an existing iOS Drop-in Advanced flow configured to handle `action.type: redirect`, and add TWINT in Customer Area. For the ordinary `/payments` route the page says no TWINT-specific extra request parameters or Drop-in configuration are needed. That general statement does **not** cover the separately specified recurring-token requests. See raw lines 97–119 and 121–160.
- **Recurring token creation:** for either flow's recurring path, the guide directs a `/payments` request with `storePaymentMethod: true` and a unique `shopperReference` of at least three characters. After details are stored, a `recurring.token.created` webhook carries `storedPaymentMethodId`; the merchant server must be able to receive the recurring-token lifecycle webhook. The page does not state that a mere initial request immediately yields a usable token. See raw lines 48–71 and 121–144. [[adyen-tokenization]]
- **Token reuse:** a later `/payments` request uses `paymentMethod.storedPaymentMethodId`, the same `shopperReference`, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` or `UnscheduledCardOnFile`. The page also points to `/listRecurringDetails` as another way to retrieve the stored-method ID. These are recurring-specific fields, not additions to the ordinary first-payment path. See raw lines 73–87 and 146–160.
- **TEST and LIVE:** test payment status is checked in the test Customer Area; to accept live TWINT payments the merchant must submit a TWINT request in live Customer Area. A request prerequisite is not proof that approval or activation has occurred. See raw lines 89–95 and 162–168.
- The raw repeats the same recurring-token instructions after the Advanced section (raw lines 170–207). Treat the repetition as the page's duplicated instructions, not a separate token lifecycle or an additional flow requirement.

## Detail locators

- Sessions prerequisite and ordinary request/configuration: raw lines 25–46.
- Sessions recurring creation and reuse: raw lines 48–87.
- Advanced redirect prerequisite and ordinary request/configuration: raw lines 97–119.
- Advanced recurring creation and reuse: raw lines 121–160; repeated block at 170–207.
- TEST status and LIVE request gate: raw lines 89–95 and 162–168.

## Related

- [[adyen-online-payments]] — main method-addition route.
- [[adyen-ios-sdk]] — native Drop-in context; the exact SDK baseline is separately versioned.
- [[adyen-tokenization]] — recurring-token concepts.
- [[source-adyen-docs-payment-methods-twint]] — TWINT method overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/twint/ios-drop-in/2026-09-15|TWINT iOS Drop-in, captured 2026-09-15]]
