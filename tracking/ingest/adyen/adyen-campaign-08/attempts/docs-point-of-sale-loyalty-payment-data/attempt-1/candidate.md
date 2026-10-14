---
title: "Card and shopper identifiers for loyalty use cases | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/loyalty/payment-data"
raw_files:
  - "adyen/docs/point-of-sale/loyalty/payment-data/2026-09-15.md"
tags: [adyen, point-of-sale, loyalty, terminal-api, shopper-identifiers]
---

## Overview

Adyen's POS loyalty guide, captured 2026-09-15, explains how a Terminal API integration can use card acquisition and payment responses to recognize a shopper, attach merchant-created identifiers to a consented back-end profile, and apply benefits before payment or update loyalty state after an AUTHORISATION webhook. Its scope is payment terminals with Terminal API; Adyen Support must check account configuration and the merchant must enable identifier return in Terminal API responses. The examples and returned IDs are not proof of current eligibility, customer consent, payment authorization, tokenized charging ability, or PCI/privacy compliance. See [[adyen]], [[adyen-pos-loyalty]], and [[adyen-terminal-api]].

## Key takeaways

- A **card alias** (`alias`) represents a card's PAN for recognition and is returned in `AdditionalResponse` for the card route; Adyen explicitly says it **cannot be used to make payments**. With `TokenRequestedType=Customer`, the guide also shows the alias in `PaymentToken.TokenValue`; that response placement does not make it a reusable payment credential. For an NFC wallet, the guide says a PAN/card alias is unavailable and points to `PaymentAccountReference` instead. That reference represents a linked payment account, not a guaranteed person identity or payment authorization.
- `shopperReference` is a merchant-defined, case-sensitive shopper ID of at least three characters, with no name/email or other PII in its value. `shopperEmail` is optional if collected. The merchant needs shopper consent to save a back-end profile and submit these identifiers with a payment. The initial `SaleToAcquirerData` payment carries `recurringProcessingModel=CardOnFile` so the reference/email can return in later card-acquisition and payment responses. This flag triggers terminal PIN authentication; Support can disable that prompt for cards without PIN, but the page warns against setting the flag on every transaction. This identifier-return condition does not itself authorize recurring charges.
- **Synchronous route:** first send `CardAcquisitionRequest`; its required `CardAcquisitionTransaction` object can be empty, with optional `TotalAmount` that can be omitted if unknown or changed in the later payment. Inspect `AdditionalResponse` (Base64-decode if needed) for stored shopper reference/email, alias, or the wallet's payment-account reference. Retain `POIData.POITransactionID.TimeStamp` and `TransactionID`; the subsequent Terminal API payment uses them in `PaymentData.CardAcquisitionReference`. A new shopper can consent and provide profile data by POS staff or terminal input; a recognized shopper can choose a benefit and the final `PaymentTransaction.AmountsReq.RequestedAmount` reflects any discount. Card acquisition/recognition is not a payment.
- **Estonian ID-card branch:** only in Estonia, `SaleToPOIData` carries the guide's Base64 smart-card operation, and the response example uses `LoyaltyAccount.LoyaltyAccountID.LoyaltyID` with `LoyaltyBrand` such as `estonian-id` or `estonian-id-cosmox`. This is a separate loyalty-identification example, not a card PAN, card alias, or general payment credential.
- **Asynchronous route:** create the profile, make the payment, wait for the standard `AUTHORISATION` webhook, then update the profile with returned identifiers, for example loyalty points. Adyen says this route cannot apply a discount or other benefit on the spot before that payment. An example `PaymentResponse` or webhook instruction is not evidence of a real transaction's result, settlement, consent record or loyalty update.

## Detail locators

- Purpose, Terminal API/Support prerequisites, alias/reference/email roles, consent and PIN flag: [[raw/adyen/docs/point-of-sale/loyalty/payment-data/2026-09-15#Requirements|Requirements]], [[raw/adyen/docs/point-of-sale/loyalty/payment-data/2026-09-15#Identifiers to save|Identifiers to save]], and [[raw/adyen/docs/point-of-sale/loyalty/payment-data/2026-09-15#Shopper consent and PIN entry|Shopper consent and PIN entry]] (raw lines 24–54). The page does not enumerate credential roles, session transport, PCI scope or a complete privacy policy.
- Pre-payment card acquisition and alias/wallet recognition: raw lines 56–195 under **Synchronous flow**, **Payment card check**; exact example IDs, amounts and 2020 timestamps are illustrative.
- Estonia-only national ID path and `LoyaltyID`: raw lines 197–323 under **Estonian ID card check**.
- Consented new profile/payment and subsequent response identifiers: [[raw/adyen/docs/point-of-sale/loyalty/payment-data/2026-09-15#Create a new customer profile and make a payment|Create a new customer profile and make a payment]] (raw lines 325–504). `SaleToAcquirerData` may be Base64 JSON or form-encoded pairs, and its format controls the returned `AdditionalResponse` format.
- Recognized-shopper benefit and final amount: [[raw/adyen/docs/point-of-sale/loyalty/payment-data/2026-09-15#Make a payment for a recognized shopper|Make a payment for a recognized shopper]] (raw lines 506–663). The example's requested amount is illustrative, not a discount guarantee.
- Webhook-driven after-payment loyalty update: [[raw/adyen/docs/point-of-sale/loyalty/payment-data/2026-09-15#Asynchronous flow|Asynchronous flow]] (raw lines 665–676).

## Related

- [[adyen-pos-loyalty]] — proposed primary loyalty concept route, pending coordinator creation.
- [[adyen-terminal-api]] — payment versus card-acquisition message boundary.
- [[adyen-tokenization]] — separate payment credential lifecycle; a loyalty alias is not a charge token.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/loyalty/payment-data/2026-09-15|Adyen card and shopper identifiers for loyalty, captured 2026-09-15]]
