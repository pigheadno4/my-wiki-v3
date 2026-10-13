---
title: "Adyen POS override of amount to tip on"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/tipping/tipping-from-terminal/change-amount-to-tip-on"
raw_files:
  - "adyen/docs/point-of-sale/tipping/tipping-from-terminal/change-amount-to-tip-on/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, tipping, gratuity, payment-amounts]
---

## Overview

This Adyen Docs guide shows how an integrated POS can change the **base amount used for a shopper's tip suggestion** while keeping the full purchase amount in the Terminal API payment request. By default, Customer Area tipping options apply to the total purchase amount. This override is for a Terminal API integration with payment terminals on software **1.103 or later**; the page says it is not supported for pay-at-table, including split checks. The merchant POS must decide when to apply it.

## Key takeaways

- Overriding the tip base also overrides Customer Area tipping options for that payment. The POS must pass the `AskGratuity` tender option in `SaleData.SaleToAcquirerData` and a Base64-encoded `Operation` object in `SaleData.SaleToPOIData`. Its `TipOptions` contains `AmountToTipOn` and `TipSuggestions`: up to three preset fixed amounts or percentages, with percentage numeric values no greater than 100, plus optional `TipCustom`. The terminal presents the adjusted base before the shopper adds a tip.
- `PaymentTransaction.AmountsReq.RequestedAmount` remains the **total purchase amount with decimals**. `AmountToTipOn` is the amount on which the tip choices are based; it does not replace the purchase amount or itself become the authorized total. The response's `PaymentResult.AmountsResp.TipAmount` is the selected tip and `AuthorizedAmount` is purchase plus tip. When no tip is added, `TipAmount` and the gratuity receipt entry are omitted.
- The worked example has EUR 20.00 purchase, EUR 15.00 tip base, 20% tip choice, EUR 3.00 tip, and EUR 23.00 authorized total. In `AdditionalResponse`, `posadditionalamounts.originalAmountValue`, `posAmountGratuityValue`, and `authorisedAmountValue` are described in **minor units**; receipt and `AmountsResp` values are shown as decimal amounts. This is a terminal payment authorization flow, not a separate capture or a transfer of the tip to a particular recipient.

## Detail locators

- Default Customer Area tip base, example motivations, merchant trigger logic, terminal display: `# Override the amount to tip on`, raw lines 15–25. Software and pay-at-table limits: `## Requirements`, lines 27–35.
- Override precedence, `AskGratuity`, encoded `Operation`, percentage/fixed-option limits: `## Specify amount to tip on in the payment request`, raw lines 37–70. Header/field table and request example: lines 72–137.
- Response receipt, `TipAmount`, `AuthorizedAmount`, minor-unit additional fields, and EUR 20/15/3/23 worked example: same section, raw lines 139–202. Linked broader tipping and tender-option routes: `## See also`, lines 204–211.

## Related

- [[adyen]] — provider context.
- [[adyen-terminal-api]] — payment/tipping amount boundary.
- [[source-adyen-docs-point-of-sale-tipping-tipping-from-terminal]] — broader terminal tipping flow and account setup.
- [Override tipping options](https://docs.adyen.com/point-of-sale/tipping/tipping-from-terminal/override-tipping-configuration) and [tender options](https://docs.adyen.com/point-of-sale/add-data/tender-options) — linked detailed navigation, not read as evidence here.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/tipping/tipping-from-terminal/change-amount-to-tip-on/2026-09-15|Adyen Docs: Override the amount to tip on (2026-09-15 snapshot)]]
