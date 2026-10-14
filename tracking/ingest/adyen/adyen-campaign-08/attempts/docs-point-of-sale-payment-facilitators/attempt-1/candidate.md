---
title: "Adyen POS payment-facilitator sub-merchant data"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/payment-facilitators"
raw_files:
  - "adyen/docs/point-of-sale/payment-facilitators/2026-09-15.md"
tags: [adyen, point-of-sale, payment-facilitator, sub-merchant, merchant-of-record, terminal-api, management-api]
---

## Overview

This dated Adyen POS guide describes the **extra sub-merchant data a payment facilitator must supply with facilitated in-person transactions**. It says card schemes require that data because the **sub-merchant is considered Merchant of Record for a transaction facilitated by the payment facilitator**. Adyen automatically adds some sub-merchant data; the facilitator supplies the remainder. This is a transaction-data rule, not a description of the parties' broader contract, money flow, settlement account, split, payout or liability allocation. See [[adyen-pos-payment-facilitators]] for the bounded model, [[adyen-pos-store-management]] for store administration, and [[adyen-terminal-api]] for payment-message transport.

## Key takeaways

- The guide covers Terminal API integrations with payment terminals or Mobile solutions, plus standalone terminals. A Management API credential with **Management API—Stores read and write** role is required to add sub-merchant data to store configuration. Standalone supports **only** the store-configuration route. See raw § Requirements (lines 23–31).
- The facilitator can put the remaining sub-merchant data in a sub-merchant's **store configuration**, or in a **Terminal API request** for integrated terminals. Standalone requires store configuration; integrated terminals may use either or both. When both are supplied, **request fields override store configuration**. Adyen adds store-configured data before sending requests for authorization. See raw §§ Methods to add sub-merchant data and Add to the store configuration (lines 33–50).
- For request-supplied fields, the guide limits this to Terminal API **payment** and **referenced or unreferenced refund** requests. It says non-Terminal-API modifications, including manual capture and authorization adjustment, use the sub-merchant data from the initial payment. Do not infer a capture or adjustment request must repeat the Terminal API fields. See raw § Methods to add sub-merchant data (lines 42–44).
- Store configuration uses Management API create/update of a sub-merchant's store with `subMerchantData`. Its table marks `email`, `id`, `mcc` and `name` required, with `subMerchantData.id` (the facilitator's sub-merchant identifier, distinct from the platform store ID) alphanumeric and at most **15** characters; the name is at most **22** and may overwrite part of the shopper's bank-statement transaction description under scheme rules. The facilitator needs the platform store `id` for update; sample SDK snippets in the raw are examples, not proof every language sample is executable. See raw § Add to the store configuration (lines 52–66, 68–276).
- The Terminal API route creates an `additionalData` JSON object, Base64-encodes it, and passes that value in `PaymentRequest.SaleData.SaleToAcquirerData` in the payment example. The field list includes sub-merchant ID, address pieces, name, tax ID and four-digit MCC; its `subMerchantId` limit is **19** alphanumeric characters, unlike the store `id` limit. The Terminal API field table gives descriptions but **does not mark required fields**. The response does not echo the specified sub-merchant data, so a payment response alone does not verify the exact data transmitted. See raw § Add to the Terminal API request (lines 278–355).

## Detail locators

- Raw §§ Requirements and Methods to add sub-merchant data: supported integration families, credential role, standalone limit and request-over-store precedence (lines 23–44).
- Raw § Add to the store configuration: Management API store ID, `subMerchantData` table and create/update examples (lines 46–276).
- Raw § Add to the Terminal API request: field descriptions, Base64 encoding into `SaleToAcquirerData`, example PaymentRequest and non-echo response caveat (lines 278–355).

## Related

- [[adyen-pos-payment-facilitators]] — facilitator/sub-merchant role and data-path boundary.
- [[adyen-pos-store-management]] — Management API store identity and lifecycle.
- [[adyen-terminal-api]] — Terminal API payment and refund requests.
- [[adyen-mobile-pos]] — separate mobile in-person integration route.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/payment-facilitators/2026-09-15|Payment facilitators POS guide, fetched 2026-09-15]]
