---
title: "Adyen POS card acquisition"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/card-acquisition"
raw_files:
  - "adyen/docs/point-of-sale/card-acquisition/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, card-acquisition, shopper-identifiers]
---

## Overview

Adyen's Terminal API card acquisition flow lets a POS obtain card and shopper identifiers from a payment terminal before a payment or outside a payment flow. The acquisition is a separate terminal interaction: the POS decides whether to follow it with a Terminal API payment referencing the acquired data or to cancel and discard that data. The page does not establish that acquiring identifiers alone authorizes or captures a payment.

## Key takeaways

- This flow requires a Terminal API integration with payment terminals. Set up receipt of identifiers in Terminal API responses before using them. QR-code wallet details and one-time numeric-code details cannot be obtained by card acquisition. The returned card alias can identify a shopper, but cannot itself be used to make payments. Availability of particular response fields depends on request options or enabling their receipt; see `## Requirements` and the response-parameter table in the raw.
- A card acquisition request uses a Service-class `CardAcquisition` message. After the shopper presents an instrument, a successful response carries `CARD_ACQ_COMPLETED` in `AdditionalResponse`. For a subsequent payment, retain the acquisition response's `POIData.POITransactionID` timestamp and transaction ID and place them in `PaymentData.CardAcquisitionReference` of a separate Payment request. The final payment amount is supplied in that payment request. See the request/response tables and `## Finish with a payment` in the raw.
- To finish a completed acquisition without payment, send `EnableServiceRequest` with `TransactionAction: AbortTransaction`; the terminal discards the acquired data. A later payment referring to that canceled acquisition fails with `No prior card acquisition data available`. To stop an acquisition while the terminal is still prompting for a card, send an `AbortRequest` referencing the in-progress acquisition and verify the terminal prompt disappears and the card acquisition response reports `Failure`/`Aborted`.
- With contactless, the shopper needs to tap again when the acquisition omitted an amount or its amount differs from the payment amount. Adyen says to ask Support to enable single tap to avoid the second tap; do not assume it is enabled for a merchant.

## Detail locators

- Identity, use cases, prerequisites and limits: `# Card acquisition`, raw lines 15–39. The autonomous-store, refund-check, loyalty, and tax-free cases under `## Scenarios` are examples, not a general authorization/capture guarantee.
- Acquisition request fields, identifiers, and response conditions: `## Make a card acquisition request`, raw lines 90–269. `SaleData.TokenRequestedType: Customer` requests an alias in `TokenValue`; the alias is also stated to appear in `AdditionalResponse`.
- Payment reference and amount fields: `## Finish with a payment`, raw lines 270–438. The prose and field table require the acquisition response's `POIData.POITransactionID` values (lines 223 and 295–297). The Java sample instead sets `CardAcquisitionReference` from a local `transactionID` variable (lines 373–377); verify that sample before implementation.
- Completed cancellation and its invalidated reference: `## Finish with a cancellation`, raw lines 440–572. In-progress abort and response check: `## Stop an in-progress card acquisition`, raw lines 574–678.

## Related

- [[adyen]] — provider context.
- [[adyen-terminal-api]] — Terminal API message and payment boundary. This website guide has separate provenance from versioned GitHub Postman examples or SDK implementations.
- [Receive card and shopper identifiers](https://docs.adyen.com/point-of-sale/card-acquisition/identifiers) — linked setup and field detail; navigation only, not read as evidence for this entry.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/card-acquisition/2026-09-15|Adyen Docs: Card acquisition (2026-09-15 snapshot)]]
