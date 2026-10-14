---
title: "Recognizing customers | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/loyalty-program/recognize-customers"
raw_files:
  - "adyen/docs/unified-commerce/loyalty-program/recognize-customers/2026-09-15.md"
tags: [adyen, unified-commerce, loyalty, customer-recognition, card-alias, shopper-reference]
---

## Overview

This Adyen Docs guide describes **merchant-managed returning-customer recognition across online and physical stores** after a customer profile has been created. Online, the merchant compares shopper-supplied email with its stored `shopperEmail`; in store, it can compare a card-acquisition response's card `alias` with its own customer database and, conditionally, use a previously stored Adyen `shopperReference`. It then shows separate examples for a saved-card online checkout and a later POS payment. Recognition is merchant lookup logic, not proof of a shopper's identity, permission to save a card, or a completed payment. See [[adyen]], [[adyen-unified-commerce]], and [[adyen-pos-loyalty]].

## Key takeaways

- **Online recognition:** the shopper supplies an email before checkout; the merchant checks it against `shopperEmail` in its customer database. A match is treated by this guide as a returning-customer record, while a missing address can lead to profile creation. Email matching alone does not verify the human presenting it. The separate profile-creation guide is linked for storage and creation details; this page does not establish its consent, retention, uniqueness or security policy.
- **Saved card online:** only when the merchant already has an online store account and a card saved/tokenized from an earlier POS payment does the guide suggest retrieving `shopperReference` and `storedPaymentMethodId` from its database. A Checkout `/paymentMethods` request including `shopperReference` can return `storedPaymentMethods`; its `id` should match the stored token ID. Drop-in/Components show saved details and collect/encrypt card security code; API-only requires a merchant-built UI, with raw card-data submission described only for a fully PCI-compliant merchant. The later Checkout `/payments` example sends the token, shopper reference, security code, `shopperInteraction=ContAuth` and `recurringProcessingModel=CardOnFile`; sample `Authorised`/PSP reference is illustrative, not a guarantee or a current API-version contract. A stored token is not the POS card alias, Payment Account Reference, raw PAN or a loyalty account.
- **In-store recognition:** before the payment, a Terminal API `CardAcquisition` request yields `AdditionalResponse` as either Base64-encoded JSON to decode or form-encoded key/value data; the examples use form encoding. The merchant looks up the returned `alias` in its own profiles. `shopperReference` may also be returned **if previously stored with Adyen**. An unmatched alias does not prove the shopper is new: the guide explicitly notes a returning customer may use a new card. It suggests asking for email to match `shopperEmail`, then asking whether the shopper wants that new card saved before tokenizing it with the existing `shopperReference` in a payment. This is a specific card-saving choice, not blanket marketing consent.
- Card acquisition is a pre-payment identification step, not authorization. The POS later sends a distinct Terminal API `PaymentRequest` with the actual amount and a `PaymentData.CardAcquisitionReference` from the preceding acquisition. In the example, `PaymentResponse.Response.Result=Success` and its terminal payment transaction ID belong to the payment response, while the acquisition IDs and merchant sale reference have separate roles. The EUR amount, customer IDs, email, alias, token and transaction IDs are examples.
- This 2026-09-15 capture has a 2020 last-modified date. It provides no evidence that a card alias is stable across every card, wallet or channel; it does not describe PAR, wallet passes, card-network tokens, live identity-matching accuracy, current Checkout/API eligibility, privacy compliance, merchant-of-record/payee allocation or financial settlement. Payment-linked loyalty and cross-channel refunds are separate linked next steps.

## Detail locators

- `Recognizing customers`, pinned raw lines 15–21: profile prerequisite and online/store recognition scope.
- `Recognize returning customers online`, lines 23–30: shopper-supplied email and merchant `shopperEmail` lookup.
- `Showing a saved card in your online checkout`, lines 32–139: prior POS tokenization prerequisite, merchant database identifiers, `/paymentMethods`/`storedPaymentMethods`, CVC/PCI paths, `/payments` fields and illustrative result.
- `Recognize returning customers in store`, lines 140–230: CardAcquisition, `AdditionalResponse` encoding, alias/conditional shopper reference, new-card ambiguity and ask-before-save step.
- In-store payment continuation, lines 231–301: separate Terminal API PaymentRequest, card-acquisition reference, example amount and payment response.
- `Next steps`, lines 303–313: payment-linked loyalty and referenced-refund links are navigation only.

## Related

- [[adyen-unified-commerce]] — primary cross-channel merchant concept.
- [[adyen-pos-loyalty]] — POS recognition and card-alias context.
- [[adyen-terminal-api]] — CardAcquisition and Payment are distinct message categories.
- [[adyen-tokenization]] — saved payment method context; the identifier here is not the recognition alias.

## Raw Sources

- [[raw/adyen/docs/unified-commerce/loyalty-program/recognize-customers/2026-09-15|Adyen recognition guide, fetched 2026-09-15]]
