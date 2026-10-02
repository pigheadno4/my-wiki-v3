---
title: "Braintree Hosted Fields Troubleshooting and FAQ (JavaScript v3)"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/hosted-fields/faq/javascript/v3"
raw_files:
  - "braintree/docs/guides/hosted-fields/faq/javascript/v3-2026-09-16.md"
tags: [braintree, javascript-sdk, hosted-fields, troubleshooting, faq]
---

## Overview

This Braintree JavaScript v3 troubleshooting and FAQ snapshot explains selected Hosted Fields integration behaviors and failure conditions: CVV-only verification for a vaulted card, iframe-relative styling and form-container behavior, expiration dropdowns, an iOS label-focus exception, valid field selectors, and restrictions encountered in third-party JavaScript sandbox sites. Its top-level Hosted Fields reference link is pinned to `braintree-web` 3.92.1; the snapshot is not current SDK-support, merchant-eligibility, browser-acceptance, or successful-payment evidence.

## Key takeaways

- To verify CVV for a vaulted card, configure Hosted Fields with only the `cvv` field. Tokenization produces a nonce containing only the CVV value; the guide says to use that nonce with the payment-method token for the customer's stored card to validate it. The linked server transaction examples are a separate implementation route, and this page does not prove a transaction, authorization, or settlement succeeded.
- Hosted Fields run inside iframes. Media queries injected into them use the iframe viewport, not the parent page, as their reference. The guide also explains that synthetic inputs are injected into merchant-page `<div>` containers to limit side effects.
- Hosted Fields supports dropdowns for expiration month and expiration year. The raw guide contains both callback and Promise configuration examples.
- On iOS, the guide says label-click focus behavior is disabled because of buggy behavior; it says the usual label focus applies on other browsers. This snapshot does not establish behavior for every current browser or SDK release.
- Each field declaration requires a valid CSS2 selector or DOM node. The guide also warns that aggressive iframe sandboxing on sites such as CodePen, JS Bin, and JSFiddle can restrict Hosted Fields functions, and recommends checking whether the behavior persists outside those sites.

## Detail locators

- CVV-only Hosted Fields configuration: `# Troubleshooting and FAQ` > `#### Can I verify the CVV when a customer uses or updates a vaulted card?`, lines 17-47; Callback example at lines 22-33 and Promise example at lines 35-46.
- Iframe-relative media-query behavior: `#### Why are media queries not being applied inside the frames?`, lines 50-52.
- Expiration-month and expiration-year dropdown support and examples: `#### Can I use a dropdown (<select>) for a field?`, lines 55-136.
- `<div>` containers, synthetic iframe inputs, and merchant styling: lines 138-145.
- iOS label-focus exception: `#### On iOS, why does clicking a label not focus the field?`, lines 148-150.
- Valid selector/DOM-node requirement and examples: `## Frequent errors` > `#### Selector does not reference a valid DOM node`, lines 153-187.
- Third-party JavaScript sandbox limitation and isolation advice: lines 189-193.

## Related

- Company: [[braintree]]
- Concept: [[braintree-web-sdk]]
- Related source: [[source-braintree-hosted-fields-events-javascript-v3]]
- Related source: [[source-braintree-credit-cards-client-javascript-v3]]

## Raw Sources

- [[raw/braintree/docs/guides/hosted-fields/faq/javascript/v3-2026-09-16|Braintree JavaScript v3 Hosted Fields troubleshooting and FAQ]] - complete captured FAQ covering selected configuration, iframe, styling, browser, selector, and sandbox-testing questions
