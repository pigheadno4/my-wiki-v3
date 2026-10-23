---
title: "Adyen card-scheme data for payment facilitators (historical guide)"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/payment-facilitators"
raw_files:
  - "adyen/docs/payment-methods/cards/payment-facilitators/2026-09-15.md"
tags: [adyen, cards, payment-facilitators, sub-merchants, online-payments, historical]
---

## Overview

This [[adyen]] card guide, last modified **2024-01-29** and captured 2026-09-15, describes sub-merchant data sent with a payment facilitator's Checkout **/payments authorization** for Visa, Mastercard and American Express scheme requirements. In this page's facilitated-transaction framing, the sub-merchant is considered **Merchant of Record** for those data points (raw lines 15–27). The statement does not establish the legal seller, payee, settlement or funds owner for a different model or transaction. A registered facilitator **using Adyen for Platforms** is explicitly sent to its separate Platforms guide (raw lines 19–21); this page's one-sub-seller parameter rule is qualified for facilitators **not using AfP** (raw line 45). The main route is [[adyen-online-payments]], with [[adyen-platforms]] as a distinct product path.

## Key takeaways

- For each authorization, the page requires a unique sub-merchant identifier, an accurate statement name and the sub-merchant's location as transaction location. Mastercard and American Express name handling includes an aggregator prefix, for which it directs the facilitator to Adyen Support (raw lines 27–32).
- Send `AdditionalDataSubMerchant` under `additionalData.subMerchant.subSeller1.[parameter]` in the initial **/payments** `additionalData`; the page fixes `subSellerNr` to **1** and says `numberOfSubSellers` must be **1** for facilitators not using AfP (raw lines 34–46). It says Adyen automatically populates sub-merchant details from the initial payment for later **cancellations, captures and refunds** (raw line 36). That describes metadata reuse, not successful modification or settlement.
- The table details ID, name, address/location, email and phone, with conditional Brazil CPF/CNPJ tax ID and MCC, and postal code specifically for Brazil, Canada, the US and domestic in-person payments in Ireland (raw lines 43–56). Consult the linked Checkout API for exact parameter formatting rather than treating this snapshot table as the complete current contract (raw line 38).
- **Source inconsistency:** the automatic-collection paragraph says there are **two** additional data points, then enumerates **three**: `paymentFacilitatorIds`, `amexCapnSubmitterId` and `aggregatorPrefix` (raw lines 58–66). It says not to submit those manually. The sample is a **test Checkout v72 /payments request** with raw card fields and placeholder sub-merchant data (raw lines 68–104); it is not proof of PCI scope, live enablement, authorization or capture. The sample omits the conditional Brazil tax/MCC fields and is not a universal country template.

## Detail locators

- Facilitator/product routing, card-scheme scope and scoped Merchant-of-Record wording: raw lines 15–27.
- Required transaction identity, statement name, location and Support prefix route: raw lines 27–32.
- Initial authorization, later-modification metadata reuse, parameter family and one-seller rules: raw lines 34–46.
- Region-conditional field table and automatic-field count/list conflict: raw lines 43–66.
- Test v72 raw-card request illustration: raw lines 68–104.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-platforms]]
- [[source-adyen-docs-platforms-online-payments-payment-facilitators]] — separate AfP online facilitator path.
- [[source-adyen-docs-payment-methods-cards]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/payment-facilitators/2026-09-15|Full pinned card payment-facilitator guide]]
