---
title: "Adyen BACS Direct Debit API-only integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bacs/api-only"
raw_files:
  - "adyen/docs/payment-methods/bacs/api-only/2026-09-15.md"
tags: [adyen, bacs, direct-debit, api-only, advanced-flow, ui-certification, tokenization]
---

## Overview

This 2026-09-15 Adyen guide adds BACS Direct Debit to an **existing Web API-only Advanced-flow** integration. It covers method discovery, merchant-built UI, payment request, recurring tokens and test/live setup. The [[source-adyen-docs-payment-methods-bacs]] overview supplies DDI/mandate, clearing, advance-notice and chargeback context. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **API-only UI access risk:** Adyen strongly recommends Drop-in or Component because it says BACS Direct Debit **must certify the shopper-facing UI**. Without those solutions, the payment method **may be disabled** and shoppers may file chargebacks. This is a source-stated risk, not proof that any merchant has passed certification or that API-only is categorically forbidden. The API-only guide assumes an existing integration with handling labeled `action.type: Direct` and BACS added in Customer Area. (raw lines 15–31)
- **Method discovery and form:** The merchant builds its own payment form and includes BACS among available methods. To obtain BACS in `/paymentMethods`, the page specifies `countryCode: GB` and `amount.currency: GBP`; the illustrated request is test Checkout API **v72**, not a stated minimum API version or present eligibility guarantee. A high-level step speaks of additional purchased-item information, but the dedicated payment-field table instead lists shopper email and bank details; do not infer a BACS-specific item payload from that prose. (raw lines 33–73, 330–353)
- **Payment request:** The `/payments` table marks `shopperEmail`, `paymentMethod.type: directdebit_GB`, `holderName`, `bankAccountNumber` and `bankLocationId` required; it describes the last as the bank routing number. The test v72 sample uses GB/GBP. Both displayed curl examples omit a line continuation after `-X POST`, so they are field illustrations rather than copy-ready commands. (raw lines 343–381)
- **Response/outcome conflict:** The prose says the response includes `action.type: Direct`; the immediately following “successful payment” JSON instead shows `resultCode: Received`, `action.type: voucher` and a `PDF_MANDATE_URL`. The page does not reconcile these shapes. It later says a successfully **received** payment has `Received` and a `pspReference`, with payment success tracked through webhooks. Thus this example does not establish the action contract, a completed DDI, a cleared debit or settled funds. (raw lines 714–727, 780)
- **Recurring and notice:** The guide recommends tokenizing for a recurring/subscription model. The initial `/payments` token step adds a unique `shopperReference` and `storePaymentMethod: true`; **when** `recurring.token.created` arrives, save `storedPaymentMethodId`. Later `/payments` use that stored ID or `recurringDetailReference` (the text qualifies it “for API v49 and above”), same shopper reference and `shopperInteraction: ContAuth`. It strongly recommends explicit shopper permission and notice before each debit, and separately says a changed collection date or amount **must** be notified in advance under the Direct Debit Guarantee. The method overview has additional advance-notice timing and nondefendable chargeback risk. (raw lines 729–780; [[source-adyen-docs-payment-methods-bacs]])
- **Test/live gate:** The guide gives a test account name, account number and sort code and points to test Customer Area status. Before live BACS acceptance it requires a request in the **live** Customer Area. Neither historical sample nor test data establishes live approval. (raw lines 782–792)

## Detail locators

- API-only UI certification risk, prerequisites and merchant-built form: pinned raw lines 15–43.
- GB/GBP `/paymentMethods` filters, v72 example and `directdebit_GB` response: pinned raw lines 45–73 and 330–341.
- Required `/payments` fields, bank routing ID and v72 sample: pinned raw lines 343–381.
- `Direct` prose versus `voucher`/mandate-URL sample, and `Received`/webhook boundary: pinned raw lines 714–727 and 780.
- Token creation/reuse and notice language: pinned raw lines 729–780.
- Test account and live request: pinned raw lines 782–792. DDI, four-to-six-day clearing and chargeback risks: [[source-adyen-docs-payment-methods-bacs]].

## Related

- [[adyen-online-payments]] — provider online-payment context
- [[adyen-tokenization]] — recurring token context
- [[source-adyen-docs-payment-methods-bacs]] — method-level DDI, clearing, notice and chargeback authority
- [[adyen]] — provider

## Raw Sources

- [[raw/adyen/docs/payment-methods/bacs/api-only/2026-09-15|BACS Direct Debit API-only, 2026-09-15]]
