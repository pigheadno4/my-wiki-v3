---
title: "Adyen DANA Flutter Component guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/dana/flutter-component"
raw_files:
  - "adyen/docs/payment-methods/dana/flutter-component/2026-09-15.md"
tags: [adyen, dana, flutter, components, recurring]
---

## Overview

This 2026-09-15 [[adyen]] page gives **DANA-specific additions** to existing **Flutter Components** integrations, separated into Sessions and Advanced server-side flows, with a further recurring-token route. It relies on linked main guides for base Component construction and redirect return handling; this page supplies no DANA-specific Flutter widget or SDK-version example. It does not establish current merchant eligibility, a completed shopper return, authorization, capture or settlement. [[adyen-online-payments]] [[adyen-tokenization]]

## Key takeaways

- **Sessions base flow:** The text requires an existing Sessions Flutter Components integration, **Checkout API v68 or later**, `action.type: redirect` handling, and DANA added in Customer Area. It says no additional DANA-specific `/sessions` parameters or Component configuration are needed. The main integration still supplies its normal request and return handling. See raw lines 23–46.
- **Advanced base flow:** The text requires an existing Advanced Flutter Components integration, redirect handling and DANA in Customer Area. It says no additional DANA-specific Component configuration or **ordinary** `/payments` parameters. The Advanced requirement table does not independently restate the Sessions v68+ condition. See raw lines 296–318.
- **Recurring token route:** Token creation adds `storePaymentMethod: true` and a unique `shopperReference` to **`/payments`**. The guide says `recurring.token.created` provides `storedPaymentMethodId` **when the initial payment has settled**, and the server must receive recurring-token lifecycle webhooks. Later token payments use that stored ID, the shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed intervals. A redirect or immediate request is not the stated token-creation event. See raw lines 48–85 and 320–357.
- **TEST/LIVE boundary:** The page says a real mobile number registered with a DANA account is needed to test successful **live** DANA payments; it also points to TEST Customer Area for test-payment status and says to request DANA in LIVE Customer Area before accepting live payments. This mixed wording and the TEST snippets do not prove a tested or enabled merchant account. IDR in recurring request examples does not by itself define eligibility; the [[source-adyen-docs-payment-methods-dana]] overview has separate ID/IDR and method-display conditions. See raw lines 87–294 and 359–566.

> [!warning] Contradiction
> Both **Flutter Components** prerequisite rows point to **Flutter Drop-in** URLs: Sessions' row points to an **Advanced Drop-in** page (raw line 31), and Advanced's row to an **Advanced Drop-in** page (raw line 304). Nearby redirect and request links point to Components flows (raw lines 33, 40, 305, 318). Treat the prerequisite URLs as mismatched navigation, not evidence that this guide is for Drop-in or that Sessions requires Advanced.
>
> The base-flow “no additional parameters” statements (raw lines 40 and 318) cannot cover the recurring sections, which expressly require `/payments` token fields (raw lines 59–85 and 331–357). The recurring examples differ: Java uses IDR 15000 where the other languages use 1000; curl/Node/Python/Ruby omit `returnUrl` while Java/PHP/C# include it (raw lines 89–283 and 361–555). Do not use a single snippet as universal request authority.

## Detail locators

- Sessions prerequisites, no-extra-fields/configuration statement: raw lines 23–46.
- Sessions token creation, settlement-gated webhook and later token payments: raw lines 48–85.
- Sessions examples and test/live statements: raw lines 87–294.
- Advanced prerequisites and no-extra-fields/configuration statement: raw lines 296–318.
- Advanced recurring section, examples and test/live statements: raw lines 320–566.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-dana]] — DANA overview for ID/IDR and method-display conditions.
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/dana/flutter-component/2026-09-15|Adyen DANA Flutter Component snapshot]]
