---
title: "Adyen Docs: Override terminal tipping options per payment"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/tipping/tipping-from-terminal/override-tipping-configuration"
raw_files:
  - "adyen/docs/point-of-sale/tipping/tipping-from-terminal/override-tipping-configuration/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, tipping, gratuity]
---

## Overview

This Adyen guide explains how a merchant POS using Terminal API can override Customer Area default tipping options in an individual payment request so the shopper sees different choices on the terminal. It covers trigger logic, terminal-software-specific `Operation` formats, request placement, and original/tip/authorized response amounts. The guide does not establish merchant enablement, current software compatibility beyond its stated versions, or a successful payment in a reader's environment.

## Key takeaways

- The merchant defines default tipping options in Customer Area, but must implement its own POS logic for when a payment should present different options; an override is supplied with that payment request rather than changing the stored default configuration. The low-value coffee example explains a possible business rule, not a required threshold. See **Override configured tipping options** and **Requirements**.
- The terminal can offer either up to three fixed tip amounts or up to three percentages of the original purchase amount, optionally a custom tip; **No tip** remains available. Percentage suggestions must not exceed 100. This is shopper selection on the terminal, not a staff-selected gratuity or an automatic charge. See **Tipping options** and **Specify tipping options in the payment request**.
- Terminal software 1.97 or later is stated for this Terminal API feature. Versions 1.97–1.100 use the older `Operation` format with `Variant: TipSuggestions`, `Data`, and `Percent1`–`Percent3`; 1.101+ uses `TipOptions.TipSuggestions` and `Percentage1`–`Percentage3`. Choose the format for the terminal's software version; the versioned examples do not establish behavior for another release. See **Requirements** and **Specify tipping options in the payment request**.
- To request the override, include the `AskGratuity` tender option in `SaleData.SaleToAcquirerData` and Base64-encode the version-appropriate `Operation` JSON into `SaleData.SaleToPOIData`. `PaymentTransaction.AmountsReq.RequestedAmount` is the original purchase amount, not a precomputed purchase-plus-tip total. See **Specify tipping options in the payment request**.
- After shopper selection, `PaymentResult.AmountsResp.TipAmount` is the selected tip and `AuthorizedAmount` is original purchase amount plus tip. Receipt data includes original/tip/total; when no tip is added, the tip field/receipt gratuity is omitted. Additional-response amount fields are in minor units and its encoding depends on account settings. The EUR 10 plus 20% tip example shows EUR 12 authorized, but its request and response examples have different `ServiceID` values, so do not treat those payloads as a coherent matched transaction or proof of capture/settlement. See **Specify tipping options in the payment request → PaymentResponse**.

## Detail locators

- **Override configured tipping options** — Customer Area defaults, request-specific override and merchant trigger-logic example.
- **Requirements** — Terminal API and software 1.97+ condition.
- **Tipping options** — fixed versus percentage choices, custom and no-tip options.
- **Specify tipping options in the payment request → Software version 1.101 and later** — new `TipOptions.TipSuggestions` structure and example.
- **Specify tipping options in the payment request → Software version 1.97 to 1.100** — older `Variant`/`Data` structure and example.
- **Specify tipping options in the payment request** — Base64 `Operation`, `AskGratuity`, request header, original purchase amount and illustrative EUR 10 request.
- **Specify tipping options in the payment request → PaymentResponse** — selected tip and authorized-total fields, receipt/AdditionalResponse details, and illustrative response; request/response sample `ServiceID` mismatch is at lines 148 and 202 of the raw.

## Related

- [[adyen]]
- [[adyen-terminal-api]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/tipping/tipping-from-terminal/override-tipping-configuration/2026-09-15|Adyen Docs — Override configured tipping options (2026-09-15)]]
