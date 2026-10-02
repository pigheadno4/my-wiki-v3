---
title: "Braintree Hosted Fields Styling (JavaScript v3)"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/hosted-fields/styling/javascript/v3"
raw_files:
  - "braintree/docs/guides/hosted-fields/styling/javascript/v3-2026-09-16.md"
tags: [braintree, javascript-sdk, hosted-fields, styling, css]
---

## Overview

This Braintree JavaScript v3 guide explains how styling responsibility is divided between merchant-supplied Hosted Fields containers and the text inside the hosted fields. Its linked supported-property reference is version-qualified to `braintree-web` 3.92.1.

## Key takeaways

- The merchant page controls container layout, width, height and outer presentation through its own stylesheets. Hosted Fields requires an explicit container height rather than relying on an input's usual font-size and line-height calculation.
- Text inside the hosted field is styled through the JavaScript `styles` configuration. The exact supported properties belong to the linked `braintree-web` 3.92.1 reference and should not be projected onto unspecified SDK versions.
- The guide's examples target all inputs, a specific field, focus/valid/invalid states and iframe-scoped media queries. It says custom web fonts are unsupported and only system-installed fonts should be used; the media query applies to the iframe, not the root window.
- Hosted Fields toggles focused, invalid and valid classes on the corresponding merchant container so the page's stylesheet can reflect field state. The raw table contains the precise event descriptions, and the following CSS is an example rather than a guarantee of validation or payment success.
- CSS transitions may be configured for allowed properties. Use the callback and Promise examples in the raw guide for the captured syntax.

## Detail locators

- Container-owned layout and outer styling: `# Styling`, line 16.
- Explicit container-height requirement: `# Styling`, line 18.
- JavaScript-owned internal text styling and version-qualified supported-property reference: `# Styling`, line 20.
- Callback styling example, including the custom-font and iframe-media-query qualifications: `# Styling` > `### Callback`, lines 23-63; Promise equivalent at lines 65-105.
- Container state classes and their event descriptions: `##### Custom classes`, lines 107-117; merchant-stylesheet example at lines 119-143.
- Allowed-property transition statement and examples: lines 144-191.

## Evidence boundary

This is a fetched documentation snapshot, not evidence of current support, merchant eligibility, hosted rendering, tokenization, validation acceptance or payment execution. The raw Markdown is not a rendered-page capture; a rendered label or control missing from the snapshot would not establish that the corresponding option is absent.

## Related

- Company: [[braintree]]
- Concept: [[braintree-web-sdk]]
- Related source: [[source-braintree-hosted-fields-events-javascript-v3]]

## Raw Sources

- [[raw/braintree/docs/guides/hosted-fields/styling/javascript/v3-2026-09-16|Braintree JavaScript v3 Hosted Fields styling guide]] - complete styling guide and callback/Promise examples
