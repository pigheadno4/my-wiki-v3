---
title: "Adyen card-based identification with Terminal API acquisition"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/shopper-recognition/identification"
raw_files:
  - "adyen/docs/point-of-sale/shopper-recognition/identification/2026-09-15.md"
tags: [adyen, point-of-sale, card-recognition, card-acquisition, card-alias, terminal-api]
---

## Overview

Adyen's card-based identification guide, captured 2026-09-15, illustrates a **Terminal API payment-terminal** parking journey: acquire a card at arrival, save an alias and arrival data in the merchant backend, cancel that acquisition flow, acquire the card again at departure, match its alias to the merchant record, calculate the fee, then make a **separate payment**. The page belongs to [[adyen-card-recognition]]. Its use of “identify the customer” means matching a presented card in this example; it does not prove a person's civil identity or a completed payment.

## Key takeaways

- The relevant identifier is the **card alias** (`alias`) in `AdditionalResponse`, described as a value representing the card number (PAN) so the merchant can recognize the presented card later. It **cannot be used for making payments**. If the optional `TokenRequestedType=Customer` is included, the same alias can also appear as `PaymentInstrumentData.CardData.PaymentToken.TokenValue`; that field's name does not make the alias a chargeable payment token. The page does not define PAR, a PSP payment reference, cross-card-person linkage, mobile-wallet alias stability or a general privacy/PCI policy.
- In the parking example, the merchant sends an **amount-free CardAcquisition** at arrival, saves `alias` and optionally presentation time/terminal `POIID` in its own backend, then cancels the **card-acquisition flow** using an `EnableService` request with `AbortTransaction` to the **same terminal**. A custom `DisplayOutput` can avoid a confusing default “Canceled” screen. This cancellation is of the pre-payment acquisition flow, not a reversal or refund of a financial payment.
- At departure, a second amount-free CardAcquisition returns the alias and `POIData.POITransactionID.TimeStamp`/`TransactionID`. The merchant uses the alias to find the earlier record and calculates the amount from its recorded times or other use-case details. The later `PaymentRequest` supplies the calculated `AmountsReq` and a `PaymentData.CardAcquisitionReference` built from the **second** acquisition's `POIData.POITransactionID`, not from the arrival acquisition or the merchant `SaleTransactionID`. The page does not show a payment response or prove authorization/settlement.
- Setup calls for card-alias delivery in Terminal API responses and Adyen Support enablement of **single tap**. For contactless acquisition followed by payment, single tap prevents the terminal from asking the shopper to tap again for that payment; it does not turn acquisition into payment. The parking and toll examples are possible merchant applications, not guaranteed recognition of the same person when a card is shared or changed. The guide specifies no consent, data-retention or account/store-sharing rule; any handling of stored aliases and location/time records needs its own policy and evidence.

## Detail locators

- Raw `# Card-based identification`, `## Requirements` and `## Card alias` (lines 15–47): example journey, Terminal API scope, alias-response setup, Support-enabled single tap, alias/PAN meaning and no-payment limit.
- Raw `## Identify the customer` (lines 49–195): first amount-free acquisition, alias in `AdditionalResponse` or optional Customer `TokenValue`, merchant backend record, same-terminal `EnableService` cancellation and optional display wording. Sample `Result: Success` is acquisition success, not payment success.
- Raw `## Recognize the customer` (lines 197–294): second amount-free acquisition, alias lookup and second `POIData.POITransactionID` values. The example card alias, PAN fragment and terminal IDs are illustrative, not a universal match promise.
- Raw `## Make a payment` (lines 296–347): merchant fee calculation, amount/currency and CardAcquisitionReference from second acquisition. `## See also` (lines 349–352) links the separate acquisition and card/shopper-identifier guides; unread linked identifier types are navigation, not claims of this page.

## Related

- [[adyen-card-recognition]] — primary card-recognition concept.
- [[adyen-terminal-api]] — acquisition, enable-service and payment message boundary.
- [[adyen-tokenization]] — separate stored-credential payment topic; alias here is not chargeable.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/shopper-recognition/identification/2026-09-15|Card-based identification, fetched 2026-09-15]]
