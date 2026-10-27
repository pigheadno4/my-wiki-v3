---
title: "Bank Transfer API-only integration | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bank-transfer/api-only"
raw_files:
  - "adyen/docs/payment-methods/bank-transfer/api-only/2026-09-15.md"
tags: [adyen, bank-transfer, api-only, virtual-bank-account, asynchronous, sepa-direct-debit]
---

## Overview

This 2026-09-15 Adyen API-only guide adds a merchant-built Bank Transfer checkout to an existing API-only integration. `/payments` supplies virtual-account details for the shopper to use when **they** initiate a bank transfer; the initial response does not move funds. The related [[source-adyen-docs-payment-methods-bank-transfer|Bank Transfer overview]] characterizes this as a shopper-initiated, asynchronous invoice/high-value option, distinct from a merchant-initiated direct debit (this raw lines 15–19, 71–117; overview raw lines 19–31).

## Key takeaways

- The page requires an existing API-only integration, standard webhooks and Support enablement in Customer Area. During setup, the merchant asks Support to configure the shopper's transfer reference as either a short PSP-reference form or the merchant's payment-request `reference`; the selection cannot be changed later. `/paymentMethods` uses EUR and a supported European `countryCode`, returns `bankTransfer_IBAN`, and the checkout obtains shopper contact details so the merchant can confirm completion (raw lines 21–40, 80). The overview's `International` table label does not establish a country list; the child guide points to the supported-country authority (overview raw lines 33–35; this raw lines 31–33).
- `/payments` requires `paymentMethod.type: bankTransfer_IBAN`, `countryCode` and `returnUrl`. `countryCode` selects localized virtual accounts for DE, FR or NL; other country codes default to an NL virtual account according to this snapshot. `returnUrl` is required by Checkout API but unused for this payment method: shoppers are **not** redirected to their bank and back. This is a virtual-account instruction flow, not a redirect checkout (raw lines 42–50).
- Save and display the response `action` details: beneficiary, IBAN/BIC, total amount and transfer reference. For EUR transfers the page says `beneficiary` is Adyen NV rather than the merchant DBA; a dynamic payment-request descriptor is ignored. Give shoppers clear instructions and explain confirmation/fulfillment timing (raw lines 71–111). The sample `/payments` response says `resultCode: Received`, but the transfer remains **Open** until funds reach the virtual bank account, then the status becomes **Settled** or **SettledAcquirer**. Check an `AUTHORISATION` webhook with matching `pspReference`, `bankTransfer_IBAN` and `success: true` before informing the shopper the payment is complete (raw lines 82–152). The example request is EUR 89600 while the webhook example says EUR 48600, so the samples are not a reconciled same-amount payment trace (raw lines 57–59, 85–101, 135–145).
- The guide says Bank Transfer supports tokenization for recurring transactions and **strongly recommends** explicit shopper permission. It then states that subsequent tokenized **EUR** transactions are processed as **SEPA Direct Debit**, requiring `paymentMethod.type: sepadirectdebit`; do not describe those later charges as repeated shopper-initiated bank transfers or infer the complete SEPA mandate procedure from this brief section. Follow the separate SEPA authority for debit prerequisites (raw lines 154–168). The overview's recurring feature mark says “See note” but gives no procedure (overview raw lines 33–35).
- TEST simulates funds arrival by **Promote this offer to sale** in the test Customer Area; the simulated settlement runs once daily. The instruction calls the event `AUTORISATION`, while the confirmation section spells it `AUTHORISATION`, a source typo to preserve. Live use requires Support to add Bank Transfer in the live Customer Area. Neither TEST promotion nor the webhook illustration proves live funds arrival or current merchant eligibility (raw lines 113–152, 170–180).

## Detail locators

- API-only/webhook/Support setup and EUR method discovery: raw lines 21–40.
- Required `/payments` fields, country behavior and unused return URL: raw lines 42–69.
- Transfer details, immutable reference preference and initial `Received`: raw lines 71–111.
- Open-to-funds status and confirming `AUTHORISATION` webhook: raw lines 113–152.
- Tokenized EUR subsequent SEPA debit and TEST/live boundary: raw lines 154–180.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-bank-transfer|Bank Transfer overview (shopper-initiated funds boundary)]]
- [[source-adyen-docs-payment-methods-sepa-direct-debit|SEPA Direct Debit overview (later tokenized EUR debit prerequisites)]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bank-transfer/api-only/2026-09-15|Bank Transfer API only, fetched 2026-09-15]]
