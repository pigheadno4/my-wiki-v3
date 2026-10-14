---
title: "Adyen Docs: Make a gift card payment at point of sale"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/alternative-payment-methods/gift-cards-terminal-api/payment"
raw_files:
  - "adyen/docs/point-of-sale/alternative-payment-methods/gift-cards-terminal-api/payment/2026-09-15.md"
tags: [adyen, point-of-sale, gift-cards, terminal-api, partial-authorizations]
---

## Overview

This Adyen Terminal API guide describes a point-of-sale payment with an activated gift card that has a loaded balance. It presents two ways to cover a purchase: request a partial authorization when the balance is unknown, or inquire about the balance first and request no more than that balance. A remaining amount can be paid through a further card request or cash. The page was last modified in 2022 and captured on 2026-09-15; it does not establish current gift-card-provider support, merchant eligibility, or payment success. [[adyen]] [[adyen-pos-gift-cards]] [[adyen-pos-alternative-payment-methods]]

## Key takeaways

- The stated prerequisites are a Terminal API integration with payment terminals, adding the payment method to the Adyen account, completing provider onboarding, and an activated card with a loaded balance. This is a POS guide, separate from Adyen's online checkout gift-card flows. See pinned raw lines 19–29.
- **Unknown balance:** make a gift-card payment request for the full purchase amount with `AllowPartialAuthorisation` in `SaleData.SaleToAcquirerData`. The page accepts Base64-encoded JSON or a key-value tender option and says the chosen format also determines the `AdditionalResponse` format. The response can be `Success` for full authorization or `Partial`; read `AuthorizedAmount` rather than assuming the requested amount was covered. See **How it works** and **1. Make the initial payment**, pinned raw lines 33–40, 84–105 and 229–236.
- **Known balance:** inquire first, then request the full due amount if covered or an amount that does not exceed the balance, and collect any remainder using a regular payment request or cash. The EUR amounts in the guide are examples, not an authorization or availability guarantee. See **How it works** and **Alternative flow with the balance check**, pinned raw lines 40–47 and 367–429.
- The payment request uses the `StoredValue` instrument with `GiftCard` account type, a provider identifier, and card-entry-specific details. Scanning supplies card number and expiry in the request; swipe and manual key entry leave the `StoredValueID` present but without a value for terminal collection. The listed providers are examples. The optional `ssc` is described specifically as an SVS secondary security code; this page does not establish a universal PIN rule. See **1. Make the initial payment → PaymentInstrumentData**, pinned raw lines 107–126.
- To split a purchase, subtract `AuthorizedAmount` from `RequestedAmount` (or use the original/authorized values in `AdditionalResponse`), then request only the remainder. `SaleReferenceID` links the partial authorizations as a merchant order, while `SaleTransactionID.TransactionID` is recommended unique and `ServiceID` must be unique on the terminal for 48 hours. These identifiers are not a promise of idempotent retry or final payment outcome; check each response before continuing. See pinned raw lines 73, 81–84, 229–234 and 294–365.
- For manual key entry longer than 24 digits, the page offers `maxLength` and `cardMask`. It says `*` makes entered digits visible and `x` hides them; handle that display choice deliberately. See **Gift card payment - MKE**, pinned raw lines 183–187.

## Detail locators

- **Requirements** (pinned raw lines 21–29) — integration, account setup, and provider onboarding.
- **How it works** (pinned raw lines 31–47) — unknown-balance partial flow versus balance-first flow.
- **1. Make the initial payment** (pinned raw lines 49–128) — entry mode, request header, transaction/order references, partial tender option, currency/amount, and stored-value instrument.
- **Gift card payment - Scanned / MKE** (pinned raw lines 130–227) — illustrative request payloads and manual-entry display options. Example IDs and amounts are not safe reusable request identities; the balance-first sample at lines 381–427 also contains JSON punctuation defects.
- **PaymentResponse** (pinned raw lines 229–292) — `Success` or `Partial`, authorized amount, `AdditionalResponse`, and order reference.
- **2. (Optional) Make a follow-up payment** (pinned raw lines 294–365) — remainder calculation, new sequence reference, and response check.
- **Alternative flow with the balance check** (pinned raw lines 367–463) — balance inquiry, bounded gift-card amount, and remaining tender.

## Related

- [[adyen-pos-gift-cards]] — gift-card POS lifecycle and payment route.
- [[adyen-pos-alternative-payment-methods]] — umbrella for POS alternative method families.
- [[adyen-terminal-api]] — terminal message architecture.

## Related raw API references

These are navigation targets named in the guide; their behavior is not evidence reviewed for this entry:

- Activate a gift card — https://docs.adyen.com/point-of-sale/gift-cards-terminal-api/activate
- Check a gift-card balance — https://docs.adyen.com/point-of-sale/gift-cards-terminal-api/query-the-balance
- Partial authorizations — https://docs.adyen.com/point-of-sale/partial-authorizations/
- Standard Terminal API payment request — https://docs.adyen.com/point-of-sale/basic-tapi-integration/make-a-payment

## Raw Sources

- [[raw/adyen/docs/point-of-sale/alternative-payment-methods/gift-cards-terminal-api/payment/2026-09-15|Adyen POS gift-card payment guide, fetched 2026-09-15]]
