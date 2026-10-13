---
title: "Partial authorizations for POS | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/partial-authorizations"
raw_files:
  - "adyen/docs/point-of-sale/partial-authorizations/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, partial-authorizations, split-tender]
---

## Overview

Adyen's POS Terminal API partial-authorizations guide explains asking the issuer to approve the card's available amount when it cannot cover the requested purchase amount, then collecting the remainder with another card or cash. This is an in-person Terminal API flow, distinct from [[source-adyen-docs-online-payments-partial-authorizations|online Checkout API partial authorizations]]. The pinned webpage was fetched 2026-09-15 and reports `last_modified` 2023-09-08; it does not establish current issuer or merchant eligibility, or success of any particular authorization. [[adyen]] [[adyen-terminal-api]]

## Key takeaways

- A Terminal API integration is required. Issuer support is **not guaranteed**. The guide asks merchants to consider delayed capture; a partial authorization can appear approved on the terminal while displaying only a warning that less than the purchase amount was paid. The POS app must alert staff and track the outstanding amount so the shopper does not leave with an unpaid balance. A capture delay may give time to cancel an authorization before capture if the shopper abandons the purchase; this is easier than refunding afterward, but the page does not promise automatic cancellation.
- Set `AllowPartialAuthorisation` in `SaleData.SaleToAcquirerData` on the initial `PaymentRequest`. The guide gives Base64-encoded JSON and form key/value formats and says the chosen format also determines the returned `AdditionalResponse` format. When the issuer supports it and available funds are below the request, the response may have `Response.Result: Partial`; `Success` indicates full authorization. Read `PaymentResult.AmountsResp.AuthorizedAmount` and the original/authorized amount values in `AdditionalResponse`, rather than treating the terminal's approved display as payment of the full order.
- Compute the remainder as requested minus authorized amount, then optionally make another Terminal API payment request for that remainder or accept cash. Use related `SaleReferenceID` values to tie installments to the same merchant order for reconciliation; use a fresh `ServiceID`, while a distinct `SaleTransactionID.TransactionID` per payment is recommended. Check the follow-up response rather than assuming the remainder was paid. The guide's test flow uses an amount ending in `139` to simulate an authorization one currency unit short; it is a test instruction, not a production issuer guarantee.
- The stated `MessageHeader.ServiceID` rule is a unique 1–10 character alphanumeric ID within 48 hours for that `POIID`; the guide also recommends a distinct `SaleTransactionID.TransactionID` per payment. **The initial and follow-up JSON examples reuse the same `ServiceID` and `TransactionID`**, so their sample values should not override those identity rules.
- This POS page describes card/cash remainder collection and the capture-delay/cancel-before-capture consideration. It does not specify supported card schemes, regional eligibility, account enablement, refund mechanics, or a general POS capture API contract. The online partial-authorization page has separate Checkout API conditions and should not be read as this POS flow's eligibility rule.

## Detail locators

- Terminal API requirement, issuer limitation, optional capture-delay preparation, and staff warning: pinned raw, `## Requirements` and `## Risk with partial authorizations` (lines 21–39).
- Tender option, amount tracking, and reconciliation: pinned raw, `## How it works` (lines 41–51).
- Initial request identities and `SaleToAcquirerData` formats: pinned raw, `## Make the initial payment` (lines 53–133); unique `ServiceID` at line 67 and `SaleTransactionID` recommendation at lines 75–76.
- `Partial` versus `Success`, authorized amount, `AdditionalResponse`, and related `SaleReferenceID`: pinned raw, initial response (lines 135–200).
- Optional outstanding-balance request and example ID reuse: pinned raw, `## (Optional) Make a follow-up payment` (lines 202–273), especially lines 219, 249, and 255–259.
- Simulated test amount and expected response: pinned raw, `## Test partial authorizations` (lines 275–306).

## Related

- [[adyen-terminal-api]] — in-person Terminal API message and payment architecture.
- [[source-adyen-docs-online-payments-partial-authorizations]] — separate online Checkout API partial-authorization guide.
- [[adyen]] — provider hub.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/partial-authorizations/2026-09-15|POS partial authorizations — 2026-09-15 snapshot]]
