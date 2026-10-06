---
title: "Braintree In-Person Custom Prompts Guide"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/guides/custom-prompts"
raw_files:
  - "braintree/in-person/guides/custom-prompts-2026-09-16.md"
tags: [braintree, in-person, custom-prompts, graphql, card-reader]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website guide describes the Custom Prompts API suite in Braintree In-Person. It lets an API caller create interactive flows on a payment reader outside payment collection, using multiple-choice, text, amount, signature, or confirmation prompts. The guide is a documentation snapshot: it does not establish current availability, merchant enablement, reader compatibility, exact GraphQL schema, successful prompt completion, or successful payment execution.

## Key takeaways

- The caller sends the applicable GraphQL mutation for a reader, receives an `InStoreContext.Id`, and then polls the context with a node query for the prompt-specific result. Displayed requests and `COMPLETE` responses are examples, not guarantees of acceptance, completion, or current schema compatibility.
- Multiple-choice presents up to 15 buttons and requires either one selection or cancellation. Text prompts support alphanumeric, sensitive alphanumeric, numeric, and sensitive numeric input; amount prompts collect a reader-entered amount; signature prompts return base64-encoded PNG data; confirmation prompts return a boolean selection. Use the raw locators for fields, enum values, limits, and displayed response shapes.
- The captured page explicitly requires a PayPal/Braintree Solutions Engineer or Integration Engineer to enable multiple-choice, text, and amount prompts in both Sandbox and Production. It identifies firmware 5.4.0 for the multiple-choice mutation and 5.2.0 for text and amount mutations; the signature and confirmation sections separately describe additions as of versions 4.0.0 and 5.2.0. These statements do not prove enablement or compatibility on a particular deployed reader.
- `waitForNextRequest: true` can suppress the processing-spinner transition between prompts, but that transition has a hardcoded 120-second timeout. An in-progress prompt can be canceled with `requestTextDisplay` and `displayTimeout` set to `0`, or with `requestCancelContext` only while the reader has not submitted data.
- Custom Prompt mutations are not supported for offline processing. For text and amount prompts, the page says context-linked response data is retrievable for about 10 minutes and is deleted after the first successful retrieval. The alphanumeric virtual keyboard is limited to the M400; other described input types and amount entry use the reader number pad.

> [!warning] Environment, hardware, data and lifecycle boundaries
> Treat Sandbox and Production enablement separately, retain the prompt-specific firmware/version and M400 qualifications, and do not infer that an example request completed. Cancellation eligibility changes once reader data is submitted, and text/amount result retrieval is time-limited and destructive after the first successful retrieval. The page also routes readers to the Braintree sub-processors page for entities that may contact collected data; this snapshot does not itself enumerate or verify that separate page.

## Detail locators

- Suite purpose and the five prompt families: `## Custom Prompts Overview`, lines 19-36.
- Multiple-choice behavior, limits, enablement, firmware and mutation/polling examples: `## Request Multiple Choice Prompt`, lines 41-53.
- Text input types, optional format enforcement, M400 qualification and mutation/polling examples: `## Request Text Prompt`, lines 54-94.
- Amount collection, decimal-place values, enablement, firmware and mutation/polling examples: `## Request Amount Prompt`, lines 95-107.
- Signature collection, version-qualified changes, response example and base64 PNG handling: `## Request Signature Prompt`, lines 108-121.
- Confirmation display, version-qualified changes and boolean-result polling example: `## Request Confirmation Prompt`, lines 124-137.
- Multi-prompt transition behavior and 120-second timeout: `## Create a seamless flow with multiple Custom Prompts`, lines 138-140.
- Physical-button mappings and conditional cancellation routes: `## Physical Button Behavior (X, &lt;, O)` through `## Canceling an in-progress Custom Prompt`, lines 143-150.
- Offline exclusion, timeout, hardware/input qualifications, and text/amount result retention and deletion: `## Tips when integrating with Custom Prompts`, lines 153-174.
- Separate sub-processor navigation for collected data: `## Data Processing`, lines 179-181.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person-custom-prompts]]

## Raw Sources

- [[raw/braintree/in-person/guides/custom-prompts-2026-09-16|Braintree In-Person Custom Prompts guide]] - complete collected website page for reader prompts, result polling, environment and device qualifications, cancellation, offline exclusion and result-retention behavior
