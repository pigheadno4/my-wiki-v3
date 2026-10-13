---
title: "Adyen Docs: Tokenize a POS payment for later online charges"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/recurring-payments"
raw_files:
  - "adyen/docs/point-of-sale/recurring-payments/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, tokenization, recurring-payments]
---

## Overview

This Adyen Docs webpage explains how a merchant using **Terminal API with payment terminals** can ask for shopper consent, tokenize an initial in-person payment, and use the resulting stored-payment token for a later **online** card-on-file or recurring charge. The later charge goes directly to Adyen's backend through Checkout `/payments`; it is not another Terminal API request to the terminal or its cloud endpoint. See [[adyen-tokenization]], [[adyen-terminal-api]], and [[adyen]].

## Key takeaways

- **Consent and authentication:** ask the shopper to opt in for specific future payments before the initial POS request. The page says PSD2 SCA applies to the initial transaction where relevant and describes PIN as usual for POS, with digital-wallet and low-value contactless cases where the terminal will not ask for PIN. Additional business-model SCA requirements and other regulations may apply; the page directs readers to separate guidance and Support for a configured PIN prompt. It does not establish the merchant's regional or regulatory eligibility. [Raw: Requirements; Cardholder consent and authentication]
- **Versioned request boundary:** from terminal software **1.85**, use `recurringProcessingModel` (`CardOnFile`, `Subscription`, or `UnscheduledCardOnFile`) and a unique `shopperReference` in `SaleData.SaleToAcquirerData`. The shopper reference has a minimum of three characters and should exclude PII such as name or email. The older `recurringContract` system remains backward-supported, but old and new tokenization parameters cannot be mixed in one payment request. [Raw: Tokenization parameters; Migration from old tokenization parameters; Make the initial payment]
- **Token capture and identity:** enable recurring details in Customer Area additional data to receive the relevant identifiers. In the initial `PaymentResponse.AdditionalResponse`, `tokenization.store.operationType` reports `created`, `alreadyExisting`, or `updated`; save `recurring.recurringDetailReference` / `tokenization.storedPaymentMethodId` as the token and the paired shopper reference in the backend. The separate `PaymentToken.TokenValue` is a card alias for recognition, **not** a usable later-payment token. Optional email, alias, and PAR details have separate purposes. [Raw: Enable receiving tokenization details; Make the initial payment]
- **Later charge:** authenticate a backend Checkout `POST /payments` with an API key; submit the stored-payment token as `storedPaymentMethodId` and the same `shopperReference`. The guide directs one-off, subscription, and auto top-up details to separate online-payment instructions and says to check the response for `resultCode: Authorised`. A cloud Terminal API integration may reuse its existing API key. Token management is also an online API operation requiring an API credential with API key. [Raw: Make a recurring online payment; Token management]

## Detail locators

- Raw `Make the initial payment` includes consent collection options, two `SaleToAcquirerData` encodings, an illustrative request/response, and the exact token-versus-card-alias warning.
- Raw `Cardholder consent and authentication` and `Requirements` carry the conditional SCA, integration-type, and software-version constraints.
- Raw `Make a recurring online payment` gives the API and response boundary. Its linked online token-payment instructions are navigation targets, not evidence read for this entry.
- This snapshot describes token use, not merchant collection of raw card data or a PCI DSS compliance determination; use dedicated PCI guidance for that question.

## Related

- [[adyen-tokenization]] — provider concept hub for saved payment methods and account-scope boundaries
- [[adyen-terminal-api]] — POS message architecture and Checkout API boundary
- [[adyen]] — company page

## Raw Sources

- [[raw/adyen/docs/point-of-sale/recurring-payments/2026-09-15|POS tokenization — Adyen Docs snapshot, 2026-09-15]]
