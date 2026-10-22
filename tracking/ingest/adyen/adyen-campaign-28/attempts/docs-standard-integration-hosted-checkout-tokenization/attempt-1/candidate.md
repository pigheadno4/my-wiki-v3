---
title: "Adyen Standard Hosted Checkout tokenization"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/standard/integration/hosted-checkout/tokenization"
raw_files:
  - "adyen/docs/standard/integration/hosted-checkout/tokenization/2026-09-15.md"
tags: [adyen, standard-integration, hosted-checkout, tokenization, card-on-file]
---

## Overview

This 2026-09-15 [[adyen]] Standard **Hosted Checkout** guide describes storing a shopper's payment details as a token and reusing them for shopper-initiated one-click payments. Adyen's hosted page handles the payment UI; the merchant creates Sessions requests, obtains the token from a lifecycle webhook and associates it with its shopper reference. This is the hosted path within [[adyen-tokenization]], not a guide to merchant-initiated subscription charges (raw lines 15–26, 40–83).

## Key takeaways

- **Prerequisites and consent:** The guide lists Checkout webservice and Merchant Recurring API credential roles, a Recurring tokens life cycle events webhook, and payment methods supporting recurring payments (raw lines 28–38). Before a shopper pays, the merchant is told to ask consent to store details. The session's `storePaymentMethodMode` can be `askForConsent` (Hosted Checkout checkbox) or `enabled` (no checkout checkbox), so `enabled` does not remove the earlier consent instruction (raw lines 104–123).
- **Creation and token receipt:** For storage, create a Hosted Checkout session with `shopperInteraction: Ecommerce`, `recurringProcessingModel: CardOnFile` and a storage mode. A zero-value authorization can verify details without collecting payment, but some methods such as iDEAL require a positive minimum. The guide says token creation follows successful authorization; receive `recurring.token.created`, then store `storedPaymentMethodId` together with `shopperReference` (raw lines 112–179). The return redirect alone is not the token source.
- **One-click reuse:** Create another session with the shopper reference, direct the returning shopper to Hosted Checkout, let them choose the stored method, and obtain that payment's outcome via webhook (raw lines 181–225). The one-click parameter table says `shopperInteraction: Ecommerce` and `recurringProcessingModel: CardOnFile`, and says another recurring model is internally changed to CardOnFile (raw lines 185–193).
- **Source mismatch and SCA:** The one-click **example** instead sends `shopperInteraction: ContAuth` (raw lines 195–219), conflicting with the table's Ecommerce instruction; do not silently choose one as universally correct. The guide also notes that some issuers require SCA for ContAuth/CardOnFile under PSD2, without establishing an exemption or outcome (raw line 193). Test/live webhook setup is separate (raw lines 227–234).

## Detail locators

- Hosted product scope, hosted-page PCI/SAQ A claim and one-click limitation: raw lines 15–26.
- Role, webhook and supported-method prerequisites: raw lines 28–38.
- Consent and token-creation session fields, zero-value qualification and example: raw lines 104–155.
- Token lifecycle webhook payload and token/shopper association: raw lines 157–179.
- One-click table versus ContAuth example and webhook result: raw lines 181–225.
- Test and live lifecycle-webhook steps: raw lines 227–234.

## Evidence boundary

The page claims a simpler SAQ A validation route because the payment UI is Adyen-hosted (raw line 21); it is a dated provider statement, not an assessment of a particular merchant's PCI compliance. Shopper consent, supported payment method, successful authorization and token-created webhook are distinct conditions. A stored token or redirected browser is not proof of a later one-click authorization, capture or settlement. The one-click shopperInteraction table/example discrepancy remains unresolved.

## Related

- [[adyen-tokenization]] — shopper-linked token and reuse concepts.
- [[adyen-online-payments]] — Standard online-payment context.
- [[source-adyen-docs-standard-integration-hosted-checkout]] — Hosted Checkout session and result flow.

## Raw Sources

- [[raw/adyen/docs/standard/integration/hosted-checkout/tokenization/2026-09-15|Pinned Hosted Checkout tokenization guide, captured 2026-09-15]]
