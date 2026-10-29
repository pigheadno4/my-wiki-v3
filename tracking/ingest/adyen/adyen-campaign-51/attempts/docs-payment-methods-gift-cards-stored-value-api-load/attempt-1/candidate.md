---
title: "Adyen Stored Value API load funds"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gift-cards/stored-value-api/load"
raw_files:
  - "adyen/docs/payment-methods/gift-cards/stored-value-api/load/2026-09-15.md"
tags: [adyen, gift-cards, stored-value, load, online-payments]
---

## Overview

This 2026-09-15-captured Adyen guide describes Stored Value API `POST /load` for adding funds to a gift card or other stored-value card, with separate card-number and tokenized-card request paths. It reports online and in-person provider support and describes `Success`/balance response fields. It is API documentation, not evidence that any card was activated, funded, refunded, or operated in this session. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Operation and activation boundary:** `/load` adds stored value; the funds are available to the shopper only if the card is activated. The page says virtual cards are activated automatically when issued, while physical cards need a separate activation. `/load` is unrelated to a payment and **cannot be used for a payment refund**; use the linked online or in-person refund routes instead. [Raw: lines 15–27]
- **Provider/channel scope:** The captured table checks load amount for **Givex, SVS, Fiserv (formerly ValueLink), and Intersolve** in both online and in-person channels. This is a capability matrix in a dated page, not proof of provider onboarding, card validity or a particular merchant's enabled currencies. [Raw: lines 29–41]
- **Without-token request:** POST to `/load` with amount currency/value (supported currencies vary by provider), merchantAccount, paymentMethod type/number and a unique reference. A securityCode is supplied if the card has a PIN/security code. `loadType` defaults to `load`; `merchandiseReturn` identifies funds arising from returned goods, but is still a load operation, not a refund of an original payment. Optional `store` applies to in-store flagged transactions (maximum 16 characters); expiry month/year and holder name are also optional. The reference maximum is 80 characters, with hyphens for multiple references. The listed card types are givex, svs, valuelink and Intersolve-supported types. [Raw: lines 43–91]
- **With-token request:** For a previously tokenized card, POST `/load` with amount, merchantAccount, paymentMethod.type, `recurringDetailReference` token, the same `shopperReference` used when tokenizing, `shopperInteraction` and unique reference. The page lists Ecommerce (online default), ContAuth, Moto and POS values; optional store and the same loadType behavior apply. The EUR/valuelink example is illustrative, not proof that any token or merchant can load that currency. [Raw: lines 136–173]
- **Response semantics:** Both paths describe `currentBalance` as the card's currency and total stored value, `pspReference` as the request reference, and `resultCode` as request state; **Success** means the amount was added. Merchant additional-data settings may add response fields. This is a documented response contract, not an observed account balance. [Raw: lines 113–134, 175–196]
- **Captured example conflicts:** The non-token example prose calls a `merchandiseReturn` load a “refund” (line 93), conflicting with the explicit “Not for refunds” rule (lines 21–27); treat it as a returned-goods load, not an original-payment refund. The response prose says USD 30 and EUR 40 balances, while the corresponding sample `currentBalance.value` fields are 30000 and 40000 (lines 123–133, 185–195). The text and payload are numerically inconsistent unless an unstated representation explains them; do not infer a verified shopper balance from these samples.

> [!WARNING] Do not use load as a payment refund
> The endpoint adds stored value and is not related to a payment. The example's “refunds USD 20” wording is in tension with the page's explicit refund prohibition. Use the separate refund route for refunding an original payment. [Raw: lines 19–27, 91–110]

## Detail locators

- Load purpose, activation and refund boundary: pinned raw lines 15–27.
- Supported providers/channels and non-token fields: pinned raw lines 29–91.
- Non-token example/response and amount inconsistency: pinned raw lines 93–134.
- Tokenized fields, example and response: pinned raw lines 136–196.
- Next-step links to status, balance, issue, merge and void: pinned raw lines 198–213; these are navigation, not operations performed here.

## Related

- [[adyen-online-payments]] — provider online-payment and payment-method route.

## Raw Sources

- [[raw/adyen/docs/payment-methods/gift-cards/stored-value-api/load/2026-09-15|Stored Value API load guide, captured 2026-09-15]]
