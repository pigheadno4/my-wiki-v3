---
title: "Adyen Stored Value API gift-card status change"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gift-cards/stored-value-api/change-status"
raw_files:
  - "adyen/docs/payment-methods/gift-cards/stored-value-api/change-status/2026-09-15.md"
tags: [adyen, gift-cards, stored-value, change-status, activation, deactivation]
---

## Overview

This Adyen page, **last modified 2020-11-17** and captured 2026-09-15, describes Stored Value API `/changeStatus` for activating or deactivating a gift card or other stored-value card, with optional loading during activation. It is a dated operational guide, not evidence that any status change or value movement was executed. See [[adyen]], [[adyen-online-payments]], and the cross-channel overview [[source-adyen-docs-payment-methods-gift-cards]].

## Key takeaways

- **Activation:** `status: active` makes stored funds available to the shopper. Virtual cards are activated automatically on issue and need no activation call. Plastic cards may be activated with or without a load amount; if funds were preloaded at issuance, specify no amount or exactly the preloaded amount. A later `/load` call is described for activation without an amount. Supported currencies differ by provider. These are source conditions, not a universal load option. See raw lines 19–25 and 49–62.
- **Deactivation:** `status: inactive` is described for cases such as suspected fraud or a lost/stolen card. The page calls it an **end state**: the deactivated card cannot be used again and any remaining value is unavailable to the shopper. This is a consequential irreversible status in this guide. The separate See also `/void` link describes undoing a previous Stored Value API transaction from the last 24 hours but does not say it reverses a deactivation; do not infer a reactivation path. See raw lines 27–29 and 273–278.
- **Provider/channel matrix:** for **online**, Activate and Activate+load are crossed for Givex, SVS, Fiserv/ValueLink and Intersolve; Deactivate without amount is checked for **Givex only**. For **in-person**, Activate and Activate+load are checked for all four, while Deactivate without amount is again checked only for Givex. The following activation example uses SVS and a store ID; it does not override the online matrix or prove a channel-specific operation succeeded. Apply the matrix as this dated source's provider/channel state, not current merchant entitlement. See raw lines 31–47 and 100–118.
- An activation request specifies `status: active`, merchant account, card `paymentMethod.type`/number and conditional security code, plus a unique merchant reference; `amount` and in-person `store` are optional as described. The activation type list includes Givex, SVS, ValueLink and Intersolve-supported types, whereas deactivation type lists contain **Givex, SVS and ValueLink** only. The no-token deactivation identifies the card by number; the tokenized path instead uses `recurringDetailReference`, `shopperReference`, `shopperInteraction` and card type. `store` remains an in-person field. See raw lines 49–98 and 143–250.
- Responses describe `currentBalance`, `pspReference`, and `resultCode`; **Success** means the requested status change was carried out, while other result codes require their own interpretation. The activation sample `Success`/USD 10 balance is illustrative. On deactivation, a reported remaining balance is **not available to the shopper**. A request or sample response alone does not establish that a real card was changed or that funds are usable. See raw lines 120–141, 207–215 and 253–261.

> [!warning] Contradiction in online SVS activation matrices
> This status-change page, last modified 2020-11-17, crosses online Activate and Activate+load for all four providers, including SVS (raw lines 33–39). The Stored Value API overview, last modified 2022-05-10, instead checks SVS for both online operations while crossing the other providers (see [[source-adyen-docs-payment-methods-gift-cards-stored-value-api]] and its raw lines 52–58). Both were captured 2026-09-15; neither resolves the discrepancy. Keep the two dated scopes distinct and verify current provider/channel support before relying on either matrix.

## Detail locators

- Operation purpose, activation/preload conditions and irreversible deactivation: raw lines 15–29.
- Historical provider/channel operation matrix: raw lines 31–47.
- Activation request fields and sample: raw lines 49–118.
- Activation response and result-code meaning: raw lines 120–141.
- No-token and tokenized deactivation request paths: raw lines 143–250.
- Deactivation responses and related load/balance/void navigation: raw lines 253–278.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-gift-cards]]
- [[adyen-pos-gift-cards]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/gift-cards/stored-value-api/change-status/2026-09-15|Fully read Stored Value API change-status raw]]
