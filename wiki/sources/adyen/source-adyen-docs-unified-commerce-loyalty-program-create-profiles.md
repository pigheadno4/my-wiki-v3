---
title: "Creating customer profiles | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/loyalty-program/create-profiles"
raw_files:
  - "adyen/docs/unified-commerce/loyalty-program/create-profiles/2026-09-15.md"
tags: [adyen, unified-commerce, customer-profiles, shopper-identifiers, tokenization, consent]
---

## Overview

Adyen's cross-channel profile guide asks the merchant to create a customer record in **its own CRM or database** before recognizing that customer online or at the point of sale. The record joins contact and payment-derived identifiers so the merchant can use it across sales channels. The guide explicitly says to ask for customer consent before storing personal information or tokenizing a card. This 2026-09-15 snapshot describes conditional integration steps and examples, not automatic identity matching, current account enablement, privacy compliance, or a completed payment. [[adyen]] [[adyen-unified-commerce]] [[adyen-pos-loyalty]]

## Key takeaways

- Receiving the needed response identifiers is an **enablement step**: ask an Adyen contact for card `alias` in both ecommerce and POS payment responses, and select **Recurring details** in Customer Area **Developers → Additional data** to receive shopper and recurring references. These instructions do not prove a particular merchant is enabled or that every response contains every identifier. See **Enable receiving identifiers**, pinned raw lines 23–35.
- **Online:** after obtaining the shopper's consent, the merchant collects contact details and chooses a unique `shopperReference` with at least three characters and no PII such as name or email. It sends `shopperEmail` and `shopperReference` in Checkout `/payments`; set `storePaymentMethod: true` only when the shopper chooses to save card details for future payments or a subscription. A successful, tokenizing example returns card `alias`, echoed shopper identifiers and a `storedPaymentMethodId`; the guide says `alias` is unavailable for NFC wallet transactions. Do not infer that an authorized payment always creates a token. See **Create profile from online payment**, pinned raw lines 36–109.
- **At the POS:** contact details may be entered by the shopper through terminal **GetText** input or given to staff for POS-app entry. The terminal input response carries the email in `Input.TextInput`; a later, separate Terminal API **PaymentRequest** passes `shopperReference` and `shopperEmail` in `SaleToAcquirerData`. Only if the shopper agrees to store payment details does the guide add `recurringContract=UnscheduledCardOnFile`; it says this stores the identifiers on Adyen's platform and creates a token for future online payments/subscriptions. The guide instructs asking for consent before storing personal information or saving payment details. See **Create profile from point-of-sale payment**, pinned raw lines 113–258.
- The merchant then saves `shopperEmail`, card `alias` or PAR, `shopperReference`, and the returned saved-method token (`tokenization.storedPaymentMethodId` or `recurring.recurringDetailReference`) in its CRM/database, readable and writable across its sales channels. A card alias is for **recognition**; a saved-method ID is the **token** used for later tokenized payments. The guide instructs one token per card under the same shopper reference when a customer has multiple cards, linked through email. It does not define raw PAN storage, a universal match between identifiers, token reuse permission, retention duration, or access-control roles. See **Store customer data**, pinned raw lines 282–300.
- **Example caveats:** the online prose says `additionalData` includes `shopperEmail` and `tokenization.*`, while its example puts `recurring.shopperEmail` in `additionalData` and `tokenization` at top level. The POS response example echoes `recurring.shopperReference=ShopperID-A16729` but shows `tokenization.shopperReference=12345`, unlike the request. Its GetText `InputRequest` has `MessageCategory: Payment`. Treat the snippets as illustrations and verify the actual response shape and shopper linkage before persisting a record or using a token. See pinned raw lines 80–105, 129–171 and 250–280.

## Detail locators

- **Creating customer profiles; Enable receiving identifiers** (pinned raw lines 15–35) — merchant CRM ownership, consent principle, Adyen alias enablement and Customer Area additional-data setting.
- **Create profile from online payment** (pinned raw lines 36–109) — consent checkbox, PII-free `shopperReference`, conditional `storePaymentMethod`, example response and NFC-wallet alias exception.
- **Create profile from point-of-sale payment** (pinned raw lines 113–280) — contact collection, GetText input, Terminal API PaymentRequest fields, conditional `recurringContract`, response and example inconsistencies.
- **Store customer data** (pinned raw lines 282–300) — CRM fields, per-card token handling and cross-channel read/write requirement.
- **Next steps** (pinned raw lines 302–312) — separate returning-customer recognition and payment-linked loyalty guides.

## Related

- [[adyen-unified-commerce]] — primary cross-channel customer-profile route.
- [[adyen-pos-loyalty]] — POS recognition and loyalty use cases drawing on merchant profile data.
- [[adyen-pos-shopper-engagement]] — terminal input surface; this guide's GetText example is not payment itself.
- [[adyen-tokenization]] — separate saved-payment-method lifecycle and permissions.

## Raw Sources

- [[raw/adyen/docs/unified-commerce/loyalty-program/create-profiles/2026-09-15|Creating customer profiles, fetched 2026-09-15]]
