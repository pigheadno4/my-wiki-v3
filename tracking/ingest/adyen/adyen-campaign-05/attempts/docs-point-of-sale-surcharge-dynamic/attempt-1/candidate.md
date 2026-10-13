---
title: "Adyen Docs: Dynamic POS surcharge"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/surcharge/dynamic"
raw_files:
  - "adyen/docs/point-of-sale/surcharge/dynamic/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, surcharge, card-acquisition]
---

## Overview

This Adyen Docs webpage describes **dynamic surcharge**: the merchant or a third-party service calculates a surcharge and supplies `surchargeFee` in an **in-person Terminal API payment request**. Its stated integration requirement is Terminal API with payment terminals running software **1.118 or later**. The calculation and compliance decision remain with the merchant; this guide links to separate general surcharge and compliance guidance. See [[adyen-surcharging]], [[adyen-terminal-api]], and [[adyen]].

## Key takeaways

- **Configuration and disclosure:** Adyen's terminal surcharge-confirmation screen can be shown or hidden through Management API `/terminalSettings` at company, merchant, store, or terminal level using `surcharge.askConfirmation`. Configuring it requires an API credential/key and Terminal-settings read and read/write roles; live terminal-settings endpoints have rate limits. If the screen is hidden, another form of surcharge disclosure is required. The page also says a Mobile solution must provide another disclosure form, but its requirements name Terminal API with payment terminals; do not infer Mobile dynamic-surcharge support from that sentence. Single tap is recommended and requires Support enablement. [Raw: Requirements; How it works; Show or hide the confirmation screen]
- **Card data and applicability:** the guide recommends a Terminal API `CardAcquisitionRequest` to obtain amount/currency, card brand, funding source, and issuer-country details for merchant or third-party calculation; issuer-country data must be enabled in responses. It says Australia can consider skipping card acquisition and Mobile solutions currently do not support it. The later worked payment path nevertheless requires a `PaymentData.CardAcquisitionReference`; the page does not resolve how that reference is supplied if acquisition is skipped. Assess region, method, card funding, maximum permitted fee, and disclosure through the linked surcharge-compliance guidance before applying an amount. [Raw: Requirements; How it works; 1. Make a card acquisition request]
- **Request amounts and response:** after calculation, submit `surchargeFee` in `SaleData.SaleToAcquirerData` as either a Base64-encoded JSON string or a key-value string. The surcharge uses the transaction currency's ordinary units, **not minor units**; the JSON example uses a string value. `PaymentTransaction.AmountsReq.RequestedAmount` is the original goods/services amount before surcharge, gratuity, or adjustment. The worked request references the card acquisition's `POITransactionID` timestamp and ID. On an accepted payment, the guide describes `PaymentResult.AmountsResp.TotalFeesAmount` as the surcharge and `AuthorizedAmount` as original plus surcharge; `AdditionalResponse.surchargeAmount` and `posAuthAmountValue` are in minor units. Example amounts and IDs are illustrative. [Raw: 2. Add a surcharge to the payment request]
- **Boundary:** this page does not specify a universal surcharge cap, eligible method/region matrix, or refund mechanics; its general surcharge and compliance pages are linked navigation. It recommends Standard webhooks with surcharge amount in `AUTHORISATION` and does not establish account enablement, compliant fee calculation, successful payment, or refund handling for a given merchant. [Raw: Requirements; See also]

## Detail locators

- Raw `Requirements` holds terminal-software, role, webhook, rate-limit, identifier, and Support setup qualifications.
- Raw `How it works` and `Show or hide the confirmation screen` distinguish optional Adyen confirmation screen from required alternative disclosure.
- Raw `1. Make a card acquisition request` locates card data, optional identifier enablement, and `POITransactionID` used in the worked payment path.
- Raw `2. Add a surcharge to the payment request` locates the two encodings, units, required request reference in the worked path, and response fields. Its examples contain sample values, not a validated production request or a fee limit.
- Raw `See also` points to separate compliance, configuration-based surcharge, card acquisition, and terminal-management guidance; these links were not read as behavioral evidence for this entry.

## Related

- [[adyen-surcharging]] — existing provider surcharge concept and compliance boundary
- [[adyen-terminal-api]] — in-person request architecture
- [[adyen]] — company and knowledge-status page

## Raw Sources

- [[raw/adyen/docs/point-of-sale/surcharge/dynamic/2026-09-15|Dynamic surcharge — Adyen Docs snapshot, 2026-09-15]]
