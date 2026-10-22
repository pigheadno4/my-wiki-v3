---
title: "Tokenization | Adyen Standard Drop-in"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/standard/integration/drop-in/tokenization"
raw_files:
  - "adyen/docs/standard/integration/drop-in/tokenization/2026-09-15.md"
tags: [adyen, standard-integration, drop-in, tokenization, card-on-file]
---

## Overview

This 2026-09-15 [[adyen]] **Standard Drop-in** guide covers creating a shopper-linked stored-payment token during a payment or zero-value authorization, then offering that stored method for a shopper-initiated one-click payment. Drop-in handles sensitive details within a payment session; the page claims a reduced PCI DSS scope and SAQ A eligibility, but this source is not a merchant's PCI assessment or live enablement evidence. See [[adyen-tokenization]] for the main token route and [[adyen-online-payments]] for the bounded Standard checkout route. [Raw: lines 15–26]

## Key takeaways

- The guide requires a Standard integration, **Checkout webservice** and **Merchant Recurring** credential roles, a **Recurring tokens life cycle events** webhook subscription, and payment methods that support recurring payments. These prerequisites precede storing or reusing details; a listed method is not proof of this merchant's enablement. [Raw: lines 28–38]
- Before storage, ask the shopper for consent. For the tokenization session, the guide sets `shopperInteraction: Ecommerce`, `recurringProcessingModel: CardOnFile`, and `storePaymentMethodMode` to either `askForConsent` (checkbox shown) or `enabled` (no checkbox). Choosing `enabled` does not erase the separate prior-consent instruction. A zero-value authorization can verify/store without collecting a payment, but some methods such as iDEAL need an amount above zero. [Raw: lines 105–126]
- The flow says authorization precedes token creation. The `recurring.token.created` webhook supplies `storedPaymentMethodId`; persist it with `shopperReference` so the token remains associated with the correct shopper. This token event is distinct from the later one-click payment-outcome webhook. The TEST session example and token webhook are illustrative; they do not prove a real authorization or stored token for a specific shopper. [Raw: lines 40–103, 128–178]
- For returning-shopper one-click use, the server creates a new `/sessions` request with the shopper reference and `CardOnFile`; the shopper selects a stored method in Drop-in and a webhook supplies the payment outcome. The one-click parameter table says `shopperInteraction: Ecommerce`, but its subsequent curl example sets `ContAuth` and the adjacent SCA note discusses ContAuth. This unresolved within-page mismatch must not be silently normalized into a required value; validate the intended flow against the relevant current API guide before implementation. The table also says a non-CardOnFile recurring model is internally changed to CardOnFile. [Raw: lines 180–220]
- For go-live, the guide calls for tokenization testing and enabling the recurring-token lifecycle webhook in **live** Customer Area. It does not establish that a test token, merchant credential or payment method is live-ready. [Raw: lines 222–229]

## Detail locators

- Standard tokenization identity and provider PCI-scope claim: raw lines 15–26.
- Roles, webhook subscription and recurring-method prerequisite: raw lines 28–38.
- Store/one-click flow separation and shopper-consent step: raw lines 40–111.
- Session tokenization fields, checkbox modes and zero-value limitation: raw lines 113–154.
- Authorization-gated token webhook and token/shopper pair: raw lines 154–178.
- One-click session table versus ContAuth example/SCA note: raw lines 180–220.
- Test versus live webhook setup: raw lines 222–229.

## Related

- [[adyen-tokenization]] — main stored-token concept
- [[adyen-online-payments]] — Standard Drop-in context
- [[source-adyen-docs-standard]] — bounded Standard checklist
- [[source-adyen-docs-standard-integration-drop-in]] — parent Drop-in Sessions path

## Raw Sources

- [[raw/adyen/docs/standard/integration/drop-in/tokenization/2026-09-15|Pinned Standard Drop-in tokenization guide]]
