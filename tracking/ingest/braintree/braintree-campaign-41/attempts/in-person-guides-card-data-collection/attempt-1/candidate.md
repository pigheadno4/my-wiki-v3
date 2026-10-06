---
title: "Braintree In-Person Card Data Collection"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/guides/card-data-collection"
raw_files:
  - "braintree/in-person/guides/card-data-collection-2026-09-16.md"
tags: [braintree, in-person, card-reader, card-data, magstripe, graphql]
---

## Overview

This 2026-09-16 snapshot of an unversioned [[braintree]] website guide describes using a Braintree card reader to collect raw track data from non-PCI-scoped, ISO 7813-formatted magstripe cards, such as qualifying third-party gift cards or closed-loop private-label cards. The API caller controls the reader flow and is responsible for sending collected data to any applicable third-party issuer and displaying the outcome. This is a data-collection flow, not Braintree transaction processing, authorization, vaulting, capture, settlement, funding, or proof of any payment outcome.

## Key takeaways

- Before use, Braintree must configure the merchant gateway account with the applicable non-PCI card BIN ranges through a Braintree Solutions Engineer or Integration Engineer. The guide separately says Sandbox testing requires the full test-card numbers or at least their first eight digits; it does not establish production enablement, account eligibility, current availability, or a safe channel for exchanging those values.
- The documented mutation initializes a reader for a swipe and allows caller-controlled prompt text and an optional post-swipe processing screen. Braintree checks the read card against known PCI BIN ranges and the merchant account's configured non-PCI BIN ranges before allowing retrieval of track 1 and track 2 data. The page states that Braintree will not return PCI card data when a PCI-scoped card is swiped. Use the raw locator for request fields and examples rather than treating the rendered sample as exact current GraphQL schema.
- After initialization, the application waits for a swipe and polls the returned context ID with a node query at the page-stated two-second interval to observe the `InStoreContext.status` and retrieve available track data. A displayed `COMPLETE` context and sample track values demonstrate the documented collection response only; they do not prove authorization, transaction processing, vault creation, capture, settlement, funding, or a real reader interaction. Returned track content can vary with card formatting, and the page says Braintree returns whatever data is retrievable.
- The collected page says Card Data Collection is unavailable for offline processing, requires ISO 7813 formatting, rejects conflicts with known PCI-scoped BIN ranges, and depends on configured merchant BIN ranges. Context-linked response data is described as retrievable for about ten minutes and deleted after the first successful retrieval. Treat collection completion, data availability, and data retrieval as separate lifecycle facts.
- Braintree does not process the external-card transaction in this flow. The caller may use `requestTextDisplay` to show a customized result and is advised to avoid customer PII in that display. The guide routes to a separate Braintree sub-processors page for entities that may contact collected data, but this snapshot does not enumerate those entities or provide a complete security, consent, retention, PCI, issuer-processing, or regulatory implementation standard. It also names Braintree card readers generally without establishing model, firmware, location, or deployed-reader compatibility.

> [!warning] Raw-data and lifecycle boundary
> This flow exposes raw non-PCI magstripe track data to the API caller after card and account-range checks. Preserve the page's non-PCI, ISO 7813, configured-BIN, online-only, short retrieval-window, and delete-after-first-successful-retrieval conditions. Do not infer issuer approval, customer consent, secure downstream handling, vaulting, payment authorization, or transaction success from a request, context state, sample response, or caller-displayed message.

## Detail locators

- Feature identity, examples, caller control and third-party issuer responsibility: `## Feature Overview`, raw lines 19-24.
- Gateway-account BIN configuration and Sandbox test-number condition: `## Setup and Configuration`, raw lines 27-32.
- Reader initialization, prompt variables, PCI/non-PCI checks and configured-range gate: `## Initiate a request to collect card data`, raw lines 35-39.
- Rendered request fields, two-second context polling, sample response and variable track-data qualification: raw lines 40-48.
- Caller-owned result display and the suggestion to avoid customer PII: `## Displaying the transaction result`, raw lines 51-56.
- Offline exclusion, ISO 7813 and BIN-range conditions, approximate ten-minute availability and delete-after-first-successful-retrieval behavior: `## Tips when Integrating Card Data Collection`, raw lines 59-77.
- Separate sub-processor navigation for entities that may contact collected data: `## Data Processing`, raw lines 82-84.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]

## Raw Sources

- [[raw/braintree/in-person/guides/card-data-collection-2026-09-16|Braintree In-Person Card Data Collection guide (2026-09-16 snapshot)]]
