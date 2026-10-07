---
title: "Braintree In-Person EMV Receipt Reference"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/reference/emv-receipt-reference"
raw_files:
  - "braintree/in-person/reference/emv-receipt-reference-2026-09-16.md"
tags: [braintree, in-person, emv, receipts, reference]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website reference presents a merchant-varying example receipt with a visual overlay that identifies data elements in relation to EMV compliance. It tells receipt producers to include the information needed both for EMV compliance and for the customer, but it is an illustrative reference rather than a complete textual field specification or proof that a particular receipt is compliant.

## Key takeaways

- The page's central action is to use the overlaid example to understand the roles of receipt data elements when producing customer receipts.
- The page expressly says that the example varies by merchant. Its three embedded images are visual examples; the captured text does not enumerate or define their fields.
- For more information, the page routes readers to Receipt Data Handling Documentation. That linked page was not collected or read for this entry, so this source retains the link only as navigation and makes no claims about its contents.

## Material warnings

> [!warning] Example and compliance boundary
> The page calls its receipt example EMV compliant, while also stating that the example varies by merchant and directing producers to include all necessary information. The example and overlay do not by themselves establish that another merchant's receipt, implementation or transaction is compliant.

> [!warning] Snapshot and scope boundary
> This unversioned website snapshot does not establish current support or availability, applicable markets, card brands or networks, merchant/account eligibility, device or printer compatibility, Sandbox-versus-Production behavior, SDK/API schema, GitHub implementation parity, or any authorization, capture, printing, delivery, settlement or funding outcome.

## Detail locators

- Page purpose and overlaid-example identity: introductory sentence, line 16.
- Producer responsibility to include necessary EMV-compliance and customer information: `## EMV Compliant Receipt Overview`, line 21.
- Overlay purpose and Receipt Data Handling Documentation navigation: `## EMV Compliant Receipt Overview`, line 23.
- Merchant-variation qualification: `#### EMV Compliant Receipt Example (will vary by merchant)`, line 26.
- Three embedded example images: line 28.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]
- Related reviewed source: [[source-braintree-in-person-guides-receipt-printing-api]]

## Related navigation

- [Receipt Data Handling Documentation](https://developer.paypal.com/braintree/in-person/guides/making-a-transaction/receipt-data-handling/) - unread linked navigation; no behavioral claims retained

## Raw Sources

- [[raw/braintree/in-person/reference/emv-receipt-reference-2026-09-16|Braintree In-Person EMV Receipt Reference]] - complete collected reference page with its receipt-production guidance, merchant-varying example heading, visual-overlay description and embedded example images
