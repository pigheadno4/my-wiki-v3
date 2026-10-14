---
title: "Meal voucher payments in Brazil | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/alternative-payment-methods/brazil-vouchers"
raw_files:
  - "adyen/docs/point-of-sale/alternative-payment-methods/brazil-vouchers/2026-09-15.md"
tags: [adyen, point-of-sale, brazil, meal-vouchers, pat, terminal-api]
---

## Overview

This Adyen Docs guide describes in-person meal and food voucher acceptance in Brazil under the Worker Food Program (PAT). PAT vouchers are employer-funded prepaid benefit cards, sometimes co-branded with credit or debit. The page presents an Adyen terminal UI flow and, for POS-integrated terminals, a merchant UI flow using a Terminal API payment request. It states that Adyen terminals can accept major PAT voucher brands without a separate issuer contract or terminal per brand; that statement remains subject to the guide's merchant, software, and activation conditions. See [[adyen]], [[adyen-pos-alternative-payment-methods]], and [[adyen-terminal-api]].

## Key takeaways

- The guide requires a Terminal API integration with payment terminals or a standalone solution on specified terminal software: PCI PTS 5 LTS 1.120.11; PCI PTS 6 LTS 1.126.5 or 1.129 or later. Adyen Support must enable Brazilian meal-voucher functionality for the merchant account. The Adyen UI flow requires separate Support enablement at a chosen company, merchant, store, or terminal scope. These are stated prerequisites, not evidence that a particular account or terminal is enabled.
- With the Adyen UI enabled, the terminal asks the shopper to choose credit, debit, or voucher before card presentation. This path is available to integrated and standalone terminals. A merchant's own UI is only for a POS-integrated terminal; it collects the shopper's choice and sends `selectedAccountType` set to `MEAL_VOUCHER` in Base64-encoded JSON in `SaleData.SaleToPOIData` of a Terminal API `PaymentRequest`. A voucher balance below the amount due causes refusal in either flow.
- On successful integrated-terminal voucher payment, the guide says `AdditionalResponse` contains `fundingSource=PREPAID` and the voucher brand, for example `paymentMethodVariant=elo_voucher_br`. Its sample amount, IDs, encoded payload, and brand are examples, not guaranteed values. If both encoded `selectedAccountType` and `TransactionConditions.DebitPreferredFlag` are present, `selectedAccountType` takes precedence; the latter flag is described for debit/credit installment interactions.
- The MKE test-card route tests integration and reconciliation handling but does not simulate the terminal voucher flow. The raw test table supplies example brands, numbers, expiry dates, CVCs, and variants; the guide separately says a physical Visa voucher test card is obtainable by contacting Visa. Neither route proves a live transaction or current credential validity.
- PAT acceptance is conditional on a compatible CNAE main activity, applicable sanitary and nutritional rules, and an MCC in the guide's list. The MCC table includes Food, Culture, and Meal categories, while the text says an incompatible main economic activity makes the issuer decline a voucher transaction. Read the full table and confirm the merchant's eligibility; an MCC label alone does not prove approval.

## Detail locators

- `Meal voucher payments in Brazil`, pinned raw lines 15–23: PAT benefit-card identity, Adyen acceptance claim, and two UI approaches.
- `Requirements`, lines 25–35: integration and terminal-software versions, standalone limit, Support enablement and scope.
- `Ways to accept meal vouchers` / `Adyen UI`, lines 37–72: supported UI paths, insufficient-balance refusal, terminal selection, CVM/PIN condition, and successful integrated-terminal response fields.
- `Your own UI` / `Make a meal voucher payment`, lines 74–176: POS choice collection, Base64 `selectedAccountType` object, `SaleToPOIData` location, request fields and example, and response fields.
- `Interaction with installment parameters`, lines 178–187: `CHEQUE`, `CREDIT`, debit preference, and precedence when both fields are present.
- `Testing`, lines 189–206: MKE limitation, test-card table, and Visa physical-card route.
- `Merchant Category Codes`, lines 208–253: CNAE, sanitation/nutrition and MCC conditions, full category table, and issuer-decline warning.

## Related

- [[adyen-pos-alternative-payment-methods]] — provider hub for the in-person alternative-method family.
- [[adyen-terminal-api]] — POS-integrated payment-request context.
- [[adyen-payment-terminals]] — terminal hardware context; model/software eligibility here is snapshot-qualified.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/alternative-payment-methods/brazil-vouchers/2026-09-15|Adyen Brazil meal-voucher guide, fetched 2026-09-15]]
