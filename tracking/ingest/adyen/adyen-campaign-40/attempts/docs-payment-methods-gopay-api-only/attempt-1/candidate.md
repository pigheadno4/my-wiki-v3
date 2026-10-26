---
title: "GoPay for API only"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gopay/api-only"
raw_files:
  - "adyen/docs/payment-methods/gopay/api-only/2026-09-15.md"
tags: [adyen, gopay, indonesia, wallet, api-only, online-payments, tokenization]
---

## Overview

This 2026-09-15 GoPay guide is a method-specific add-on to an existing **API-only Advanced-flow** integration, not a full base integration. The integration must handle a `redirect` action, and the merchant must add GoPay in Customer Area. The page covers discovery, a merchant-built payment form, a `/payments` redirect, and separate tokenized Subscription and CardOnFile continuations. [[adyen-online-payments]]

## Key takeaways

- To discover GoPay via `/paymentMethods`, the table specifies `countryCode: ID`, `amount.currency: IDR`, minor-unit `amount.value`, and a relevant `channel` such as Web, iOS or Android. A sample response has `type: gopay_wallet`. The method needs no additional shopper form field beyond the merchant's payment-method selection. The sample discovery request omits `channel` despite the table listing it. See raw lines 38–87.
- The `/payments` parameter table marks `paymentMethod.type: gopay_wallet`, `browserInfo`, and an applicable `channel` as required. The example `/payments` response has `RedirectShopper` and `action.type: redirect`; handle it through the base API-only redirect flow. The prose's “How it works” step says to include additional information about intended purchase items, but the dedicated request table and sample do not identify item fields. The sample also renders `browserInfo` as a quoted string containing a JSON-looking object and `channel: web` in lowercase, while the table's channel examples are title case. Treat these as documentation/sample inconsistencies, not as field-shape or casing guarantees. See raw lines 31–36 and 89–146.
- For token creation, the initial `/payments` request includes `storePaymentMethod: true`, a shopper-unique `shopperReference` of at least three characters, and `recurringProcessingModel`. **After the initial payment is settled**, the `recurring.token.created` webhook supplies the `storedPaymentMethodId`; the server needs the Recurring tokens life cycle events webhook. [[adyen-tokenization]] See raw lines 148–167.
- A later **Subscription** token payment uses the stored ID, shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription`. The response's `resultCode` can be shown to the shopper; the page identifies the processed payment's final status via an `AUTHORISATION` webhook. The examples show `gopay_wallet` and IDR amounts but do not define universal limits. See raw lines 169–392.
- A later **CardOnFile** token payment is different: the shopper must be redirected to GoPay for a PIN challenge. The request uses the stored ID, shopper reference, `ContAuth`, and `CardOnFile`; a `RedirectShopper` action supplies the URL. After return, call `/payments/details` with `redirectResult`, and use the later `AUTHORISATION` webhook for final status. Do not equate the redirect or the shopper's PIN entry with successful authorization. See raw lines 394–419.
- For TEST, the guide says to contact Adyen Support and refers to GoPay's knowledge base. Before accepting live GoPay payments, it says to submit a request in the live Customer Area. This source snapshot does not establish current enablement or an executed payment. See raw lines 421–427.

## Detail locators

- Existing API-only integration, redirect handling and Customer Area setup: raw lines 23–29.
- Discovery country/currency/channel table and illustrative `/paymentMethods` request/response: raw lines 38–87.
- Required `/payments` additions, sample request and redirect response: raw lines 89–146.
- Post-settlement token creation and webhook fields: raw lines 148–167.
- Subscription request examples and final-status webhook: raw lines 169–392.
- CardOnFile PIN challenge, return/details call and webhook: raw lines 394–419.
- TEST support and live request gate: raw lines 421–427.

## Related

- [[adyen-online-payments]] — API-only online integration context.
- [[adyen-tokenization]] — recurring token lifecycle context.
- [[source-adyen-docs-payment-methods-gopay]] — GoPay method overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/gopay/api-only/2026-09-15|GoPay API-only guide, captured 2026-09-15]]
