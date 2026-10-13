---
title: "Adyen Docs: Quick chip"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/quick-chip"
raw_files:
  - "adyen/docs/point-of-sale/quick-chip/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, quick-chip, card-acquisition]
---

## Overview

Adyen's 2026-09-15 Quick Chip guide describes a United States Terminal API flow in which a shopper inserts and removes an EMV chip card before checkout knows the final purchase amount or receives an authorization response. The merchant POS first acquires card details with a placeholder amount, then sends a separate payment request with the final amount and a reference to that acquisition. Early card removal is not payment authorization or capture; the later payment response determines the payment result. [[adyen]] · [[adyen-terminal-api]]

## Key takeaways

- This guide limits Quick Chip to the **United States**, a Terminal API integration on payment-terminal software **1.95 or later**, and Support enablement. Merchants may separately ask Support to enable it for specific local payment methods. These are snapshot eligibility conditions, not proof that a particular terminal, scheme, account, or present software build has the feature enabled.
- The POS sends a Service/`CardAcquisition` request while the final amount is unknown. `CardAcquisitionTransaction` is required and may be empty or contain a placeholder `TotalAmount`. The shopper presents and removes the chip card; the POS processes the card-acquisition response in its system, then sends a Service/`Payment` request with the **final** `PaymentTransaction.AmountsReq.RequestedAmount`. The placeholder amount does not authorize or settle a payment.
- A successful acquisition response is checked for `CARD_ACQ_COMPLETED` in `AdditionalResponse`. The POS must retain **both** `POIData.POITransactionID.TimeStamp` and `TransactionID` from that acquisition response and put them in `PaymentData.CardAcquisitionReference` of the later payment request. The card alias is also available, but this guide's payment linkage is the acquisition reference, not an alias-based charge.
- Each Terminal API request has its own `ServiceID`, specified as unique within 48 hours for that terminal `POIID`; `SaleID` identifies the POS component. `SaleData.SaleTransactionID` is the merchant's payment reference, for which Adyen recommends a unique value per payment. The guide's repeated example ServiceID must not override the stated uniqueness rule.
- The raw examples are internally inconsistent: the acquisition response's transaction ID differs from the ID named in the payment prose/request, the sample payment request has `RequestedAmount` 24.98 while its response shows `AuthorizedAmount` 16.98, and the response also labels `EntryMode` Contactless despite the introduction describing EMV chip insertion. Use the prose/field instructions for the intended flow and verify actual test responses rather than reconciling these sample values as one successful transaction.

## Detail locators

- **Purpose and eligibility:** raw lines 17–29. The page states US-only, terminal software 1.95+, and Support setup; it does not list a compatible-terminal matrix or scheme guarantees.
- **Sequence:** “How it works,” lines 31–37. The shopper removes the card before the separate final-amount payment request; no authorization occurs merely from this sequence.
- **Acquisition request:** “Get the card details,” lines 39–62. See message-header fields (`MessageClass=Service`, `MessageCategory=CardAcquisition`, example `ProtocolVersion=3.0`), request IDs, `SaleTransactionID`, optional alias request, and required `CardAcquisitionTransaction` object.
- **Acquisition response:** lines 94–141. Check `CARD_ACQ_COMPLETED`, then retain the `POIData.POITransactionID` timestamp and ID for payment. Its JSON example contains fields and warnings that are not a replacement for the stated check or an authorization result.
- **Payment request and result:** “Make a payment request,” lines 143–171 and 214–264. `PaymentTransaction.AmountsReq.RequestedAmount` carries the final amount; `PaymentData.CardAcquisitionReference` carries the acquired response identifiers. The payment response, not card acquisition, reports the payment `Response.Result`; the sample fields and amounts conflict as noted above.
- The guide links Terminal API Explorer “latest” and shows `ProtocolVersion=3.0` in example message headers. It does not pin a client SDK version, live transaction outcome, capture mode, or settlement behavior.

## Related

- [[adyen-terminal-api]] — POS request/response architecture
- [[source-adyen-docs-point-of-sale-card-acquisition]] — general card-acquisition and payment-reference route

## Related raw API references

Linked Card Acquisition, Terminal API header, Payment, tender-option, currency, and tax-free-shopping pages were not read for this entry; they are navigation only.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/quick-chip/2026-09-15|Adyen Quick chip, fetched 2026-09-15]]
