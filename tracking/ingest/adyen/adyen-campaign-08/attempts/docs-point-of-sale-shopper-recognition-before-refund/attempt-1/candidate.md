---
title: "Card identification before refunding | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/shopper-recognition/before-refund"
raw_files:
  - "adyen/docs/point-of-sale/shopper-recognition/before-refund/2026-09-15.md"
tags: [adyen, point-of-sale, card-recognition, unreferenced-refunds, terminal-api]
---

## Overview

Adyen's card-identification-before-refund guide (last modified 2021-05-06; captured 2026-09-15) describes an optional same-card check before a **Terminal API unreferenced refund**. The POS first makes a Refund-type card acquisition for the presented card, compares its returned card alias and refund amount with locally stored purchases, then either sends a distinct Refund payment request referencing that acquisition or cancels the acquisition. This card check is not proof of a person's identity, consent, merchant refund eligibility, or a completed refund. See [[adyen]], [[adyen-card-recognition]], and [[adyen-terminal-api]].

## Key takeaways

- The setup assumes a Terminal API integration with payment terminals, unreferenced refunds enabled under their separate requirements, and card-alias return configured in Terminal API responses. Adyen Support must enable **single tap** if a contactless card should not need a second tap at refund time. This snapshot does not establish current scheme, account, card-entry, terminal-software, permission, or regional support.
- The `alias` represents the card's PAN for recognition and is returned in `AdditionalResponse`; it **cannot be used to make payments**. `TokenRequestedType=Customer` optionally adds the same alias to `PaymentToken.TokenValue`, without turning it into a refund/payment credential. Save purchase aliases in the merchant back end and compare the acquisition alias **and refund amount** against stored purchases. The guide does not define a hashing algorithm, cross-store/account stability, wallet fallback, legal identity test, or a guarantee that an alias match proves the original purchase is refundable.
- Send a Terminal API `CardAcquisitionRequest` with `CardAcquisitionTransaction.TotalAmount` set to the proposed refund amount and `PaymentType=Refund`. The terminal shows the amount as negative and prompts for the card. Keep `CardAcquisitionResponse.POIData.POITransactionID.TimeStamp` and `TransactionID` for the follow-up request. The acquisition response's `Success` and alias identify that card-interaction stage; they are not a refund payment.
- If the merchant chooses to proceed, send a separate Terminal API `PaymentRequest` with `PaymentData.PaymentType=Refund`, `PaymentTransaction.AmountsReq` containing currency and refund amount, and `PaymentData.CardAcquisitionReference` containing **the acquisition response's** POI transaction timestamp and ID. This does **not** reference the original purchase transaction. The guide's sample acquisition and refund requests use different literal `POIID` serials; treat them as illustrative, not a validated same-device request pair.
- A refund-request response with `Result=Success` and terminal approval confirms the request was received in this guide. Adyen says refunds are processed asynchronously and directs the merchant to wait for the `REFUND_WITH_DATA` webhook for the result. Do not treat the immediate response as funds delivered, or repeat a pending refund solely because its final webhook has not arrived. If not proceeding with the presented card, cancel the completed card acquisition before asking for another card.

## Detail locators

- Scope, prerequisites and single-tap setup: [[raw/adyen/docs/point-of-sale/shopper-recognition/before-refund/2026-09-15#Requirements|Requirements]] (raw lines 19–33). The linked unreferenced-refund guide owns its exact enablement/eligibility conditions.
- Alias semantics and no-charge boundary: [[raw/adyen/docs/point-of-sale/shopper-recognition/before-refund/2026-09-15#Card alias|Card alias]] (raw lines 35–43).
- Refund-type card acquisition fields, response identifiers, alias/amount lookup: [[raw/adyen/docs/point-of-sale/shopper-recognition/before-refund/2026-09-15#Make a Refund card acquisition request|Make a Refund card acquisition request]] (raw lines 45–156). The sample JSON's `{hint:...}` markers are documentation annotations, not literal API property names; consult the current Terminal API schema.
- Refund payment request, acquisition-reference fields, immediate acknowledgment and webhook result: [[raw/adyen/docs/point-of-sale/shopper-recognition/before-refund/2026-09-15#Continue with a refund|Continue with a refund]] (raw lines 158–287).
- Decline this card and cancel acquisition: [[raw/adyen/docs/point-of-sale/shopper-recognition/before-refund/2026-09-15#Continue in a different way|Continue in a different way]] (raw lines 289–293).

## Related

- [[adyen-card-recognition]] — primary same-card use-case hub.
- [[adyen-terminal-api]] — card acquisition and Payment request/response mechanics.
- [[adyen-tokenization]] — separate stored payment credentials; alias recognition does not create one.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/shopper-recognition/before-refund/2026-09-15|Adyen card identification before refunding, captured 2026-09-15]]
