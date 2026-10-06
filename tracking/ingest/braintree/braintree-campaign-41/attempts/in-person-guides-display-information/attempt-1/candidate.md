---
title: "Braintree In-Person Display Information"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/guides/display-information"
raw_files:
  - "braintree/in-person/guides/display-information-2026-09-16.md"
tags: [braintree, in-person, card-reader, information-display, graphql]
---

## Overview

This 2026-09-16 snapshot of an unversioned [[braintree]] website guide documents GraphQL requests that put caller-supplied plain text or line-item information on a Braintree card-reader screen and cancel an information display by its returned in-store context ID. These are reader-display actions: a request, returned context, sample reader status or displayed content is not proof that an actual reader presented the content, collected customer data, or completed a checkout or payment.

## Key takeaways

- Information displays do not block later reader interactions. The guide permits repeated display requests without first cancelling the previous display and says a `requestChargeFromInStoreReader` call made while information is displayed transitions the reader into checkout. That transition is separate from the display request and is not evidence that a charge was authorized, captured, settled or funded.
- A display request response includes a context ID that can be supplied to the cancellation mutation. The page says a display remains for 120 seconds unless it is cancelled or overwritten by a subsequent reader interaction. Treat request acceptance, reader presentation, cancellation and any later checkout as separate actions and states.
- The text-display mutation accepts caller-supplied text and the page states a 255-character limit. It qualifies `title`, `alignment`, `waitForNextRequest` and `displayTimeout` support as of version 5.2.0. The rendered example targets a supplied `readerId` and shows a sample `PENDING` response; it does not establish the deployed API or reader version, final display state or device compatibility.
- The line-item mutation is intended to be called as POS software adds items. For every update, the POS must resend all cart items and new running totals. The page allows up to 249 displayed items and says the POS must perform all calculations.
- `displayItems` are formatting data only: the guide says they are neither passed to processors nor saved in relation to the transaction. Do not treat a displayed cart, total or message as transaction data, processor submission, storage, card/customer data collection, order validation or payment proof.
- The cancellation example takes an `inStoreContextId` and describes returning the reader to its screensaver. It is a cancellation request/example, not evidence of cancellation on an actual device. The snapshot does not state an offline-mode behavior or name supported reader models, firmware, account enablement or environments; its sample reader names and statuses do not establish those conditions or current support.

> [!warning] Display and payment boundary
> Information-display requests are presentation operations. Even though the guide says a later charge request can replace the display and transition into checkout, display request/context status and displayed fields do not establish customer input, transaction submission, authorization, capture, settlement, funding or any payment outcome.

> [!warning] Snapshot, version and device boundary
> The page qualifies four text-display fields as supported as of version 5.2.0 but does not identify what component that version labels. It provides no offline-mode rule and no supported model, firmware or merchant-eligibility matrix. Treat the embedded P400 sample name and sample `ONLINE`/`PENDING` values as examples, not compatibility or execution proof. The captured Text Display reference link also points to a `RequestPrintFromInStoreReaderInput` anchor despite its label, so use current GraphQL reference material rather than inferring an exact schema from that link target.

## Detail locators

- Display purpose and example business uses: `## Getting Started`, raw lines 19-21.
- Nonblocking repeated displays and transition to checkout after a separate charge request: `## Getting Started`, raw line 23.
- Returned context ID for cancellation: `## Getting Started`, raw line 25.
- 120-second duration and cancellation/overwrite conditions: `## Getting Started` note, raw lines 27-28.
- Text-display purpose, captured GraphQL-reference link target and formatting navigation: `## Request Text Display`, raw lines 31-33.
- Text limit and version-5.2.0-qualified fields: `## Request Text Display` notes, raw lines 35-39.
- Rendered text mutation, `readerId` variables and sample response: raw line 41.
- Line-item running-cart purpose, scrolling behavior and full-cart/running-total resend requirement: `## Request Line Item Display`, raw lines 42-48.
- 249-item limit, display-only processor/storage boundary and POS-owned calculations: `## Request Line Item Display` notes, raw lines 50-54.
- Rendered item kinds, totals and sample response: raw line 56.
- Cancellation purpose, context-ID input and sample cancelled response: `## Cancel Information Display`, raw lines 57-61.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]

## Raw Sources

- [[raw/braintree/in-person/guides/display-information-2026-09-16|Braintree In-Person Display Information guide (2026-09-16 snapshot)]] - complete collected guide for text and line-item display requests, replacement/cancellation behavior, version-qualified fields and display-only data boundaries
