---
title: "Adyen Stored Value API gift-card balance inquiry"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gift-cards/stored-value-api/check-balance"
raw_files:
  - "adyen/docs/payment-methods/gift-cards/stored-value-api/check-balance/2026-09-15.md"
tags: [adyen, gift-cards, stored-value, balance, tokenization]
---

## Overview

This 2026-09-15-captured Adyen guide describes Stored Value API `/checkBalance` for viewing the remaining balance of a gift card or other stored-value card. It has card-number and tokenized-card request paths plus provider/channel marks. A balance response is an inquiry result, not a payment, load, reserve or proof of currently spendable value. See [[adyen]], [[adyen-online-payments]], and the cross-channel [[source-adyen-docs-payment-methods-gift-cards]].

## Key takeaways

- The **online** and **in-person** matrices both check balance inquiry for Givex, SVS, Fiserv/ValueLink and Intersolve. Yet both request-path `paymentMethod.type` lists call **Givex “only for in-person payments”**. This captured page does not reconcile the online Givex check with its type restriction. Do not promise online Givex balance inquiry from either line alone; provider/channel support needs verification. See raw lines 21–33, 55 and 129.
- **Without a token:** POST `/checkBalance` with `merchantAccount`, optional `store` only for in-store flagged transactions, a `paymentMethod` card type and number, conditional security code if the card has one, optional expiry/holder fields, and a transaction `reference` (maximum 80 characters; multiple references separated by hyphens). The type list names Givex with the in-person limit, SVS, ValueLink and Intersolve-supported types. See raw lines 35–79.
- **With a token:** the request uses `paymentMethod.type`, `recurringDetailReference` returned at tokenization, the matching `shopperReference`, `shopperInteraction` (Ecommerce default for online, ContAuth, Moto or POS options), merchant account and reference; `store` is optional for in-store flagged transactions. This path identifies the stored card by token and shopper identity rather than a card number. The guide ties it to a payment previously tokenized; it does not say an arbitrary card can be queried by inventing a token. See raw lines 117–148.
- Both response sections list `currentBalance.currency` and total `value` **in minor units**, `pspReference`, and a `resultCode` whose value must be interpreted using Stored Value API result codes. The sample `Success`/EUR 5600 response illustrates a successful inquiry, not an actual payment, future available spending limit, or an executed balance check for this task. See raw lines 96–115 and 150–169.
- The no-token example calls its card **SVS** but uses number `603628672882001915092` and code `5754`, which the separate Stored Value API overview's simulator table labels **Givex**. Treat the example brand/number pairing as inconsistent, not a provider test credential. See raw lines 81–94 and [[raw/adyen/docs/payment-methods/gift-cards/stored-value-api/2026-09-15|Stored Value API overview simulator table, lines 108–116]]. The page's load, merge, issue, status and void links are separate operations, not effects of balance inquiry. See raw lines 171–189.

## Detail locators

- Purpose and historical online/in-person provider marks: raw lines 15–33.
- No-token card-number request and SVS-labeled sample: raw lines 35–94.
- No-token response fields and sample: raw lines 96–115.
- Tokenized-card request and sample: raw lines 117–148.
- Tokenized response fields and sample: raw lines 150–169.
- Separate operation navigation: raw lines 171–189.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-gift-cards]]
- [[adyen-pos-gift-cards]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/gift-cards/stored-value-api/check-balance/2026-09-15|Fully read Stored Value API check-balance raw]]
