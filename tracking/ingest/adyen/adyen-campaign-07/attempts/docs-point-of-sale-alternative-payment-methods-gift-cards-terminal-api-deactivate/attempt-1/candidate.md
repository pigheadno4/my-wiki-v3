---
title: "Adyen POS gift card cashback and deactivation"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/alternative-payment-methods/gift-cards-terminal-api/deactivate"
raw_files:
  - "adyen/docs/point-of-sale/alternative-payment-methods/gift-cards-terminal-api/deactivate/2026-09-15.md"
tags: [adyen, point-of-sale, gift-cards, terminal-api, cashback, deactivation]
---

## Overview

This Adyen Terminal API guide distinguishes two point-of-sale gift-card actions: a cashback request removes value and returns it to the shopper, while a deactivation request disables a Givex card without cashing it out. Cashing out the full remaining balance also leaves the card inactive. The page's last-modified field is 2019-10-01 and the raw was captured 2026-09-15; it is historical integration evidence, not proof of current provider support or completed funds movement. [[adyen]] [[adyen-pos-gift-cards]] [[adyen-pos-alternative-payment-methods]]

## Key takeaways

- The guide assumes a Terminal API integration with payment terminals, that the gift-card method has been added to the Adyen account, and provider onboarding. Cashback availability and amount depend on provider, scheme rules, and applicable law. When permitted, full-balance cashout is usual; the guide allows some Givex partial-cashback cases. Removed value can be handed to the shopper as cash, or transferred to a credit/debit card through a separate **unreferenced refund** route. A cashback request itself is not a general refund or payment void.
- First determine card entry method and check the balance. For cashback, send a Terminal API `PaymentRequest` with `MessageCategory=Payment`, `SaleData.SaleToAcquirerData` carrying `redemptionType=cashback`, `AmountsReq.Currency` and `RequestedAmount`, `PaymentType=Normal`, and a `StoredValue` instrument with `GiftCard` account identity. The tender option can be Base64 JSON or a key-value pair; that choice also controls `AdditionalResponse` format. Check `PaymentResponse.Response.Result=Success`, the transaction ID and receipt data rather than inferring success from the request.
- Givex-only deactivation uses a different Terminal API `StoredValueRequest` with `MessageCategory=StoredValue`, `StoredValueTransactionType=Unload`, `ItemAmount=0` and the card currency. Check `StoredValueResponse` for `Unload`, `Response.Result=Success`, and `StoredValueAccountStatus.CurrentBalance=0`. Zero amount here is a deactivation action, not a cashback amount or shopper payout.
- Scanned cards supply the number and expiry in the request. For swipe or manual key entry, the terminal prompts after the request; the two action sections give entry-specific fields in their own tables. The page states no general PIN rule. Use a `ServiceID` unique for that terminal for the prior 48 hours and a sale transaction reference recommended unique; `SaleReferenceID` is optional for linking cashback transactions to an order. Sample IDs, card numbers, amounts and currencies are illustrations, not reusable values.
- The deactivation section's account-detail table lists `givex`, `svs` and `valuelink`, yet both its explicit limitation and deactivation introduction say **Givex only**. Its response bullet says `Unload` plus `Success` indicate funds were “loaded,” contradicting the deactivation explanation and zero-balance example. Keep the narrower Givex scope and inspect the actual action/result; do not generalize deactivation to the other listed providers or interpret that typo as loading value.

## Detail locators

- Raw `# Deactivate or cash out a gift card` and `## Requirements` (lines 15–34): action distinction, full-balance consequence, Givex-only limitation and setup.
- Raw `## Cash back a gift card` (lines 35–111): provider/law conditions, shopper payout options, card entry, balance check, Terminal API request fields, cashback tender option and stored-value identity.
- Raw cashback examples and response (lines 112–291): illustrative JSON/Java, response ID, receipt and `Success`; the scanned JSON example has malformed `EntryMode` quoting and should not be copied as a valid payload.
- Raw `## Deactivate a gift card` (lines 292–365): Givex condition, card entry and `StoredValueRequest` fields, `Unload`, zero amount and currency.
- Raw deactivation examples and response (lines 366–488): illustrative Givex request, response checks, zero balance and contradictory “loaded” wording. The sample request and response show different terminal IDs and card-entry/card-number values; do not treat them as one matching transaction.

## Related

- [[adyen-pos-gift-cards]] — POS gift-card lifecycle and provider-specific actions.
- [[adyen-pos-alternative-payment-methods]] — umbrella for in-person alternative methods.
- [[adyen-terminal-api]] — terminal request/response architecture.

## Related raw API references

Navigation named in this guide, not additional reviewed evidence:

- Balance inquiry — https://docs.adyen.com/point-of-sale/gift-cards-terminal-api/query-the-balance
- Unreferenced gift-card refund — https://docs.adyen.com/point-of-sale/gift-cards-terminal-api/refund-gift-cards#make-an-unreferenced-refund
- Terminal API PaymentRequest — https://docs.adyen.com/api-explorer/terminal-api/latest/post/payment
- Terminal API StoredValueRequest — https://docs.adyen.com/api-explorer/terminal-api/latest/post/storedvalue

## Raw Sources

- [[raw/adyen/docs/point-of-sale/alternative-payment-methods/gift-cards-terminal-api/deactivate/2026-09-15|Deactivate or cash out a gift card, fetched 2026-09-15]]
