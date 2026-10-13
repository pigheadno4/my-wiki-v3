---
title: "Adyen Terminal API point-of-sale refund overview"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/basic-tapi-integration/refund-payment"
raw_files:
  - "adyen/docs/point-of-sale/basic-tapi-integration/refund-payment/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, refunds, reversals]
---

## Overview

This Adyen Docs overview compares two **point-of-sale Terminal API** refund routes after an approved payment: a referenced refund using `ReversalRequest` tied to the original payment's tender and/or PSP reference, and an unreferenced refund using `PaymentRequest` with `PaymentType: Refund` for a card presented at the terminal. A merchant may implement one or both, subject to the payment method and transaction-routing limits below. Customer Area is an alternate route for merchants that refund POS payments infrequently. This is not the Checkout API online-payment refund, capture, or cancellation guide.

## Key takeaways

- Referenced refunds connect to the original transaction and simplify reconciliation; the comparison table says they support PSP-reference omnichannel refunds and QR-code wallets. Unreferenced refunds are manually reconciled, can return an amount to a presented card without the original shopper, and carry greater duplicate/wrong-amount risk. QR-code wallet and omnichannel refunds are not supported on the unreferenced route. Initiating a refund deducts the amount from the merchant's in-process funds.
- Referenced refunds are **always asynchronous**: the Terminal API response confirms receipt of the request, not the processing result. The result comes through refund webhooks, and funds can take up to 40 business days to reach the shopper depending on payment method. Unreferenced refunds can be synchronous or asynchronous depending on card scheme and country/region; only when synchronous does `acquirerResponseCode` in the response indicate approval. Do not treat a request acknowledgment or an example response as settlement proof.
- BankAxept refunds require an additional scheme contract and are possible only at stores where the shopper purchased. Dankort and Interac support only unreferenced refunds in this guide. A debit card's routing, not its funding source alone, determines whether a referenced refund is allowed: some debit networks are single-messaging. Retain `paymentMethodVariant` for routed network and `fundingSource` for credit/debit/prepaid card type.
- Refund authorization is an automatic issuer validity check for American Express, Discover, Mastercard, and Visa. An issuer decline of this check does **not** end processing; Adyen says it still tries to process the refund. The page links separate guides for refund-webhook outcomes and canceling an unreferenced refund **before completion**; those linked procedures are not established by this overview.

## Detail locators

- Terminal API refund identities, Customer Area alternative, and in-process funds: `# Refund a payment`, raw lines 15–33.
- Reconciliation/risk/QR/omnichannel comparison and timing/response interpretation: `## Referenced and unreferenced refunds`, raw lines 35–49.
- Scheme and routing restrictions, `paymentMethodVariant` versus `fundingSource`: `## Allowed refund method`, raw lines 51–71. Issuer refund authorization and declined-check continuation: `## Refund authorization`, raw lines 73–93.
- Linked detailed refund, cancellation, and webhook-result routes: `## Next steps`, raw lines 95–111; read those pages before asserting their request fields, partial/split handling, or cancellation mechanics.

## Related

- [[adyen]] — provider context.
- [[adyen-terminal-api]] — POS Terminal API message ownership and payment/refund boundary.
- [[adyen-refunds]] — separate online-payment Checkout API refund concept; its captured-payment and webhook lifecycle must not be applied wholesale to this POS Terminal API overview.
- [Referenced POS refund](https://docs.adyen.com/point-of-sale/basic-tapi-integration/refund-payment/referenced), [unreferenced POS refund](https://docs.adyen.com/point-of-sale/basic-tapi-integration/refund-payment/unreferenced), [cancel an unreferenced refund](https://docs.adyen.com/point-of-sale/basic-tapi-integration/refund-payment/cancel-unreferenced), and [refund webhooks](https://docs.adyen.com/point-of-sale/basic-tapi-integration/refund-payment/refund-webhooks) — linked next-step navigation; not read as evidence here.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/basic-tapi-integration/refund-payment/2026-09-15|Adyen Docs: Refund a payment (2026-09-15 snapshot)]]
