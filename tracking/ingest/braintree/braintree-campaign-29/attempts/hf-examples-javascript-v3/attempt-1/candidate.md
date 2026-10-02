---
title: "Braintree Hosted Fields Examples (JavaScript v3)"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/hosted-fields/examples/javascript/v3"
raw_files:
  - "braintree/docs/guides/hosted-fields/examples/javascript/v3-2026-09-16.md"
tags: [braintree, javascript-sdk, hosted-fields, examples, styling]
---

## Overview

This Braintree JavaScript v3 page is a gallery of Hosted Fields presentation examples. It illustrates styling and UI possibilities through linked CodePen samples; the examples are not guarantees of SDK support, field validation, tokenization or payment success.

## Key takeaways

- Braintree presents the gallery as a small selection of styling possibilities and recommends using merchant-owned CSS and JavaScript to make Hosted Fields fit the surrounding UI.
- The Bootstrap and Material Design entries demonstrate styled form and input presentations. Their external CodePen links are implementation routes, but the captured page does not contain or verify the linked code.
- The event-oriented example says Hosted Fields events can be used to detect card types and alter the UI while a customer enters information. This is an example of responsive presentation behavior, not evidence that input is valid or a transaction succeeds; use the dedicated events guide for the event-state integration route.
- The minimal example states that Hosted Fields inputs cannot use custom webfonts because of stated SAQ A server-asset regulations. It instead points to system fonts that might be installed on the customer's device and fallback fonts.
- The final example uses CSS transforms as a presentation technique for a distinctive form experience. No example on this page establishes current browser compatibility, merchant configuration or payment execution.

## Detail locators

- Gallery purpose and merchant-owned CSS/JavaScript recommendation: `# Examples`, line 16.
- Bootstrap-styled form description and CodePen route: `### Example: Bootstrap styled`, lines 19-23.
- Material Design input description and CodePen route: `### Example: Material Design styled`, lines 26-30.
- Card-type detection and UI-alteration example: `### Example: animating events`, lines 33-37.
- Custom-webfont restriction, system-font fallback guidance and CodePen route: `### Example: minimal`, lines 40-44.
- CSS-transform presentation example and CodePen route: `### Example: 3D transform`, lines 47-51.

## Evidence boundary

This is a fetched documentation snapshot, not evidence that the external CodePens are current or that any example renders, validates, tokenizes, authorizes or settles a payment in a merchant environment. Consult the dedicated styling and events guides for their version-qualified integration details.

## Related

- Company: [[braintree]]
- Concept: [[braintree-web-sdk]]
- Related source: [[source-braintree-hosted-fields-styling-javascript-v3]]
- Related source: [[source-braintree-hosted-fields-events-javascript-v3]]

## Raw Sources

- [[raw/braintree/docs/guides/hosted-fields/examples/javascript/v3-2026-09-16|Braintree JavaScript v3 Hosted Fields examples gallery]] - complete captured page with five example descriptions and external CodePen routes
