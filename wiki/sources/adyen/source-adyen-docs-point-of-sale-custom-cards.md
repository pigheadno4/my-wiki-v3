---
title: "Adyen POS custom-card acquisition"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/custom-cards"
raw_files:
  - "adyen/docs/point-of-sale/custom-cards/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, custom-cards, card-acquisition, magstripe]
---

## Overview

This dated guide explains how a merchant uses an Adyen payment terminal to **read its own custom magnetic-stripe card** (for example, an employee benefit card) through Terminal API card acquisition and pass the returned data to the merchant POS. The merchant then processes any card transaction through **the issuer of that custom card**; the page does not describe Adyen authorizing, capturing or settling that issuer-side transaction. This is separate from Adyen-managed POS gift-card `StoredValue` payment flows and QR or code alternative payment methods. See [[adyen]], [[adyen-terminal-api]], [[adyen-pos-gift-cards]] and [[adyen-pos-alternative-payment-methods]].

## Key takeaways

- The page requires a Terminal API integration, a custom card with a **magnetic stripe**, and Adyen Support enablement for reading custom cards on the merchant's terminals. **Swipe** is the only entry method stated for this custom-card path. The source does not establish current account or issuer eligibility.
- Send a Terminal API `CardAcquisition` service request to the intended terminal. Its `CardAcquisitionTransaction` object is required but can be empty; `TotalAmount` is optional and may be an initial placeholder. The guide's amount in a sample is not evidence of an Adyen payment. `ServiceID` is documented as 1–10 alphanumeric characters, unique for the terminal (`POIID`) over the previous 48 hours; the sample `ServiceID` appears longer, so use the stated field rule rather than copying that fixture.
- A successful acquisition has `message=CARD_ACQ_COMPLETED` in `Response.AdditionalResponse` and supplies the custom card's **PAN** and raw magnetic-track number/value under `PaymentInstrumentData.CardData.SensitiveCardData`. `TokenRequestedType=Customer` can request an alias; the page does not make that alias a payment token for the external issuer. PAN and track data are sensitive payloads to route to the issuer under the merchant's own controls. This page does not specify a storage policy, BIN/whitelist rule, PIN flow, or PCI exemption for the merchant.
- After reading, send a separate Terminal API `EnableService` request with `TransactionAction=AbortTransaction` to end the **card-acquisition flow**. Otherwise its loading screen continues until timeout. The request frees the terminal for other transactions and makes it discard card data; it is not a refund or cancellation of an issuer-side payment. Optional `DisplayOutput` can replace the basic example's canceled message/icon.

## Detail locators

- `## Requirements`, `## How it works`: magstripe, Support enablement, swipe-only entry and external issuer processing boundary.
- `## Make a card acquisition request`: Terminal API header fields, terminal-scoped `ServiceID`, optional `TotalAmount`, response message and sensitive PAN/track locations. The sample's 11-character `ServiceID` conflicts with the stated 1–10-character rule.
- `## Complete the card acquisition`: `EnableService`/`AbortTransaction`, terminal loading-screen effect, card-data discard and optional display customization.

## Related

- [[adyen-terminal-api]] — primary Terminal API card-acquisition route.
- [[adyen-pos-gift-cards]] — separate Adyen POS stored-value payment path.
- [[adyen-pos-alternative-payment-methods]] — separate terminal code and QR payment paths.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/custom-cards/2026-09-15|Adyen Custom cards, captured 2026-09-15]]
