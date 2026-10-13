---
title: "Adyen POS tender options"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/add-data/tender-options"
raw_files:
  - "adyen/docs/point-of-sale/add-data/tender-options/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, tender-options, sale-to-acquirer-data, receipts]
---

## Overview

This unversioned Adyen website guide, captured on 2026-09-15, explains **per-payment Terminal API tender options** in `PaymentRequest.SaleData.SaleToAcquirerData`. These parameters change how a tender is processed; for example, `AskGratuity` prompts the shopper for a tip. The stated integration is Terminal API with payment terminals. For a standalone solution, the page instead directs the merchant to Support for account configuration. See [[adyen-terminal-api]] and the broader [[source-adyen-docs-point-of-sale-add-data]] field/encoding guide.

## Key takeaways

- The named options in this snapshot are `AllowPartialAuthorisation`, `AskGiving`, `AskGratuity`, `ForcedDecline`, `MOTO`, `ReceiptHandler`, and `SkipAIDPriority`. Their table describes possible actions: permit a lower approved amount, prompt donation or tip, force a decline, initiate terminal MOTO as a card-not-present transaction, transfer receipt handling to the POS app, or skip configured application priority to let the shopper choose an application. A listed option does not establish account, device, card-method or regional eligibility.
- `ReceiptHandler` has a consequential omission default: without it, the terminal **must print** the receipt. If the terminal lacks a built-in printer, the transaction fails. When included, the POS app handles printing or email delivery. This is receipt ownership, not evidence that a particular terminal/printer or email delivery is configured.
- Supply one or more comma-separated option values **without spaces** in a payment request's `SaleToAcquirerData`. The guide shows either a Base64-encoded JSON object `{"tenderOption":"AskGratuity,ReceiptHandler"}` or a `tenderOption=AskGratuity,ReceiptHandler` key/value pair. It says `AdditionalResponse` follows the selected request format. The response example shows a tip added to the authorized amount and `TipAmount` separately; its `OnlinePIN` value is one example, not a general CVM rule.
- Tender options can share `SaleToAcquirerData` with other data such as application information or shopper-recognition data; use the separate add-data guide for combination rules. A **transaction condition** is another mechanism that can force a card-entry method or payment method for one transaction, with MKE and Brazil examples. Adyen Support can configure default tender options/conditions for every payment. These are distinct from merely listing `MOTO` or `SkipAIDPriority` in this page's option table.
- This page does not define tender options for offline processing or token creation and does not establish those flows from the response example. It also gives no terminal-software version or generic card-method/CVM permission rule; follow each linked feature guide and current account configuration before using an option.

## Detail locators

- Standalone Support boundary, tender purpose, request field and terminal integration: raw lines 15-33.
- Seven names and their action descriptions, especially `ReceiptHandler` failure condition: raw `## Tender options`, lines 35-47.
- Comma-separated JSON/Base64 versus key/value serialization and response-format rule: raw `## Specify tender options`, lines 49-64; Terminal API request and illustrative tip/PIN response: lines 66-180.
- Coexistence with other data and route to the broader add-data guide: raw `## Combining tender options and other data elements`, lines 182-186.
- Per-payment transaction conditions versus Support-configured defaults: raw `## Other ways to change transaction processing`, lines 188-193.
- MKE, add-data and response-handling links: raw `## See also`, lines 195-199; use these as navigation.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-terminal-api]]
- Broader request-data source: [[source-adyen-docs-point-of-sale-add-data]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/add-data/tender-options/2026-09-15|Adyen POS tender options]] — full captured option and serialization guide
