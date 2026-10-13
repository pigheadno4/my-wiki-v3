---
title: "Adyen POS SaleToAcquirerData sample collection"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/add-data/sale-to-acquirer-data"
raw_files:
  - "adyen/docs/point-of-sale/add-data/sale-to-acquirer-data/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, sale-to-acquirer-data, request-encoding, additional-data]
---

## Overview

This Adyen Docs page is a **sample collection** of data elements a merchant POS can place in `PaymentRequest.SaleData.SaleToAcquirerData` of a Terminal API payment request. Its stated scope is an integration with payment terminals or a Mobile solution. It illustrates Base64-encoded JSON and key-value representations, with categories such as application information, merchant metadata, recurring/shopper fields, store, tender options, and `additionalData`. It does not establish that every sample field is required, supported for every merchant, or sufficient to produce an authorization, capture, split payout, or other result.

## Key takeaways

- The JSON example has top-level `applicationInfo`, `metadata`, recurring and shopper fields, `store`, `tenderOption`, and an `additionalData` object. The nested examples include `authorisationType`, lodging, split, surcharge, tax-free, travel/entertainment, and `manualCapture` names. The key-value tab flattens names such as `applicationInfo.externalPlatform.name` and `additionalData.authorisationType`. These are examples to locate names and shape, not a full list of `additionalData` elements; the page explicitly says the list is long and growing.
- The tabs route to the parent add-data guide for Base64 JSON versus key-value encoding. That guide describes Base64 of a JSON object or form-encoded `key=value` pairs separated by `&`, and explains `AdditionalResponse` format selection. This sample page itself provides representation examples; it does not pin an API Explorer or SDK version. Example `applicationInfo` version strings describe a platform/app/device in the payload, not the Terminal API protocol version.
- Preserve a sample-level path discrepancy when implementing: JSON places `split.*` and `taxfree.indicator` inside `additionalData` (raw lines 76–89), while the key-value example lists `split.*` and `taxfree.indicator` without an `additionalData.` prefix (lines 118–131). `surchargeFee` appears in the JSON sample but is absent from the key-value sample. Follow the field-specific guides and current schema for an actual request rather than inferring equivalence or requiredness from this mixed collection.
- Before relying on additional response data, the Requirements section points to selecting what to receive. The example values `PreAuth`, `ReceiptHandler,AskGratuity`, `split.api=1`, `manualCapture=false`, and numeric split amounts do not by themselves prove those features are enabled, a split is accepted, funds are allocated, or a payment has reached a final state.

## Detail locators

- Purpose, terminal/Mobile scope, response-data setup, and non-exhaustive warning: `# SaleToAcquirerData`, `## Requirements`, and `## SaleToAcquirerData sample collection`, raw lines 15–29.
- Base64 JSON route, top-level application/shopper/tender fields, nested `additionalData`, and placeholder values: `### Tab: JSON object`, raw lines 31–95. Exact split, surcharge, tax-free, and manual-capture sample names: lines 64–93.
- Key-value route and flattened names: `### Tab: Key-value pairs`, raw lines 97–146. Compare lines 118–132 with JSON lines 76–89 for the split/tax-free path difference. More complete encoding and response rules belong to [[source-adyen-docs-point-of-sale-add-data]].

## Related

- [[adyen]] — provider context.
- [[adyen-terminal-api]] — Terminal API payment request boundary.
- [[source-adyen-docs-point-of-sale-add-data]] — parent guide for encoding and `AdditionalResponse` selection.
- [[source-adyen-docs-point-of-sale-add-data-tender-options]] — field-specific tender-option behavior.

## Related raw API references

- The page links an API Explorer Payment `additionalData` reference and detailed add-data/tender-option routes. Treat linked references as navigation; this source's raw sample does not independently verify their current field requirements or response behavior. See raw lines 29, 33, 99, and 148–152.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/add-data/sale-to-acquirer-data/2026-09-15|Adyen Docs: SaleToAcquirerData sample collection (2026-09-15 snapshot)]]
