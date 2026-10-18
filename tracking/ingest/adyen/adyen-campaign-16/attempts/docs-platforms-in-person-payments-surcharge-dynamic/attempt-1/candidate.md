---
title: "Dynamic in-person surcharge | Adyen for Platforms"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/in-person-payments/surcharge/dynamic"
raw_files:
  - "adyen/docs/platforms/in-person-payments/surcharge/dynamic/2026-09-15.md"
tags: [adyen, platforms, in-person-payments, surcharge, terminal-api, split-payments]
---

## Overview

This [[adyen]] for Platforms guide explains dynamic **in-person** surcharging: the platform or a third-party service calculates a surcharge from transaction and card details, then sends the amount in a Terminal API payment request with split instructions that book the surcharge to one of its user's balance accounts. It is a dated integration guide, not evidence of account enablement, compliant pricing, authorization, booking, payout, or bank receipt. See [[adyen-platforms]] and [[adyen-surcharging]]; the online card pilot and general point-of-sale guides are separate routes.

## Key takeaways

- **Scope and prerequisites.** The page requires a Terminal API integration with payment terminals on software **1.118 or later**, in addition to its linked Platforms in-person and surcharge requirements. Before starting, it says to enable issuer-country/region identifiers in API responses and webhooks and ask Adyen Support to enable single tap. It recommends Standard webhooks with surcharge data in `AUTHORISATION`; live Management API terminal-settings calls have rate limits. These requirements do not prove a specific account's support or eligibility. [Raw: Requirements, lines 23–35]
- **Calculation and disclosure.** A Terminal API card-acquisition response supplies details such as brand, funding source, issuer country and transaction amount/currency for the platform's or third party's calculation. The guide recommends card acquisition, says an Australian flow can consider skipping it, and says Mobile solutions currently do not support card acquisition. Its worked payment path nevertheless requires a `PaymentData.CardAcquisitionReference`; it does not explain how to satisfy that reference when acquisition is skipped. The customer can accept the Adyen surcharge confirmation screen or cancel; when it is hidden or a Mobile solution is used, another form of disclosure is required. Check applicable country, scheme and legal requirements; this snapshot is not a current surcharge-permission determination. [Raw: How it works, lines 37–65; Show or hide the confirmation screen, lines 67–95; 1. Make a card acquisition request, lines 97–234]
- **Payment and booking.** `SaleData.SaleToAcquirerData` carries both split instructions and `surchargeFee`. Add a `Surcharge` split item directed to the `balanceAccountID` of **one** of the user's balance accounts; the page says the surcharge cannot be split across several balance accounts. `surchargeFee` is separate from the split fields and uses ordinary currency units, **not minor units**. The guide accepts an ampersand-separated key-value string or Base64-encoded JSON; the JSON example uses a string for the fee. `PaymentTransaction.AmountsReq.RequestedAmount` remains the goods/services amount before surcharge, gratuity or other adjustment. The worked request references the card-acquisition response's `POIData.POITransactionID`. [Raw: 2. Add a surcharge and book it to your user, lines 236–261, 311–343, 354–378]
- **Keep amounts and evidence distinct.** In the worked USD 620 goods/services plus USD 6 surcharge example, `split.totalAmount` is 62000 minor units and does not add the payment-fee or surcharge split; `surchargeFee` is `6.00`. The example books USD 600 sale and USD 6 surcharge to a user's balance account, USD 20 commission to the platform's liable account, and deducts the payment fee from the user sale. These are illustrative instructions, not observed bookings. For an accepted payment, the guide maps `TotalFeesAmount` to surcharge and `AuthorizedAmount` to original plus surcharge, while `AdditionalResponse.surchargeAmount` and `posAuthAmountValue` use minor units. The sample payment-request timestamp at raw line 410 starts `026-` while the acquisition response uses `2026-`; use the specified response timestamp/ID fields rather than copying that sample as a validated payload. [Raw: lines 263–270, 419–480]

## Detail locators

- Raw `Requirements` and `How it works` (lines 23–65): integration/version, identifiers, single tap, calculation, Mobile and disclosure boundaries.
- Raw `Show or hide the confirmation screen` (lines 67–95): `surcharge.askConfirmation`, Management API scope and credential roles.
- Raw `1. Make a card acquisition request` (lines 97–234): Terminal API `CardAcquisitionRequest`, card details and response identifiers; missing identifiers route to the linked receive-identifiers guide.
- Raw `2. Add a surcharge and book it to your user` (lines 236–481): surcharge split destination, units/encodings, amount arithmetic, response fields and illustrative payloads.

## Related

- [[adyen-platforms]] — platform/user balance-account context
- [[adyen-surcharging]] — surcharge methods and compliance boundary
- [[adyen-terminal-api]] — Terminal API message architecture
- [[source-adyen-docs-point-of-sale-surcharge-dynamic]] — separate general POS dynamic-surcharge guide
- [[source-adyen-docs-platforms-online-payments-surcharge]] — separate Platforms online-card pilot

## Raw Sources

- [[raw/adyen/docs/platforms/in-person-payments/surcharge/dynamic/2026-09-15|Adyen Platforms dynamic in-person surcharge — collected 2026-09-15]]
