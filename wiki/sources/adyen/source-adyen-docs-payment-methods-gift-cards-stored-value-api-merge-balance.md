---
title: "Merge gift-card balance with Stored Value API"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gift-cards/stored-value-api/merge-balance"
raw_files:
  - "adyen/docs/payment-methods/gift-cards/stored-value-api/merge-balance/2026-09-15.md"
tags: [adyen, gift-cards, stored-value, merge-balance, valuelink]
---

## Overview

This 2026-09-15-captured Adyen Stored Value API guide describes `/mergeBalance`, which transfers the **full stored value** from a source gift/stored-value card to a target card **of the same provider/type**. It gives channel/provider support marks, target-card details with and without a token, and the response fields. This is an operation guide, not evidence that a merge was executed, that a provider is currently enabled, or that a sample balance belongs to a particular card. See [[adyen]], [[adyen-online-payments]] and the [[source-adyen-docs-payment-methods-gift-cards|gift-card overview]].

## Key takeaways

- **Provider/channel restriction:** the captured matrix marks online merge supported only for **Fiserv (formerly ValueLink)** among Givex, SVS, Fiserv and Intersolve. It marks merge unsupported for all four in the **in-person** row. Both source and target must be from the **same gift-card provider**; the request field accepts target `paymentMethod.type: valuelink`. This snapshot does not establish present account/provider enablement or an in-person route merely because an optional `store` field is documented (raw lines 15–33, 75–79, 174–178).
- **Without token:** POST `/mergeBalance` with `merchantAccount`, source card number and target `paymentMethod` type/number. If either card has a PIN/security code, obtain it from the shopper and include that card's `securityCode`; source/target expiry and holder name are optional. `store` is optional for in-store-flagged transactions (maximum **16 characters**), while `reference` identifies the transaction (maximum **80 characters**, hyphens separating multiple references). These are request-field descriptions, not a guarantee the in-person matrix supports merge (raw lines 35–119).
- **With token:** the **source** still uses `sourcePaymentMethod.number` and any applicable security code, but the **target** is identified by `paymentMethod.type: valuelink`, `recurringDetailReference` returned when target card was tokenized, and the corresponding `shopperReference`. `shopperInteraction` accepts Ecommerce, ContAuth, Moto or POS, with Ecommerce described as default for online; these accepted enum values do not override the channel/provider support matrix (raw lines 145–178).
- **Token example caveat:** the tokenized-target example assigns `recurringDetailReference` a card-number-looking value identical to the target number mentioned in its introductory sentence. The field description explicitly calls for the **token returned on tokenization**; do not treat the example as a rule that a raw card number can replace that token (raw lines 174–198).
- **Response and lifecycle:** both paths describe `currentBalance` as currency/value in minor units, plus a 16-character `pspReference` and `resultCode` indicating request state. The sample shows `Success`, but the text does **not identify whether `currentBalance` is the source or target card's post-merge balance**. Follow the linked Stored Value API result-code guidance for status meaning; this captured sample does not prove a transaction occurred or specify all failure/reversal behavior (raw lines 122–143, 200–221). The page's next-step links to status, balance and load operations are navigation, not part of a completed merge (raw lines 223–241).

## Detail locators

- Full-value, same-provider operation and provider/channel matrix: raw lines 15–33.
- Untokenized target request fields and reference limits: raw lines 35–119.
- Untokenized response fields and sample: raw lines 122–143.
- Tokenized target fields, shopper interaction and sample-token mismatch: raw lines 145–198.
- Tokenized response and unassigned currentBalance meaning: raw lines 200–221.
- Adjacent operation and Stored Value API routes: raw lines 223–241.
- Gift-card overview provider/onboarding and channel caveats: [[source-adyen-docs-payment-methods-gift-cards]] and its pinned raw lines 19–45; this entry's raw_files remains child-only.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-gift-cards]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/gift-cards/stored-value-api/merge-balance/2026-09-15|Stored Value API merge-balance guide, captured 2026-09-15]]
