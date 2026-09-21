---
title: "Braintree Client Token Generation (Node.js)"
type: source
date_ingested: 2026-09-19
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/request/client-token/generate/node"
raw_files:
  - "braintree/docs/reference/request/client-token/generate/node-2026-09-16.md"
tags: [braintree, node-js, client-token, client-sdk, drop-in, vault]
---

## Overview

This Braintree reference page documents Node.js client-token generation with `gateway.clientToken.generate()`. The returned client token contains the authorization and configuration information a client needs to initialize a Braintree client SDK.

## Key takeaways

- The page provides both callback and Promise forms of `gateway.clientToken.generate({})`; each reads the generated token from `response.clientToken`.
- For a customer already stored in the merchant's Braintree vault, the merchant can pass that customer's ID when generating the token. In this customer-scoped variant, Braintree says Drop-in can present the returning customer with saved payment methods.
- If the specified customer cannot be found, the response contains the message `Customer specified by customer_id does not exist`. The page does not characterize a broader failure type or promise other customer behavior.

## Detail locators

- Token purpose and client-SDK initialization role: `# Client Token: Generate`, lines 15-16.
- Empty-options callback and Promise calls, including `response.clientToken`: `### CallBack`, lines 17-22, and `### Promise`, lines 24-29.
- Customer-scoped Drop-in purpose and `customerId` examples: `## Examples > ### Specify a customer ID`, lines 34-51.
- Missing-customer message: immediately after the customer-ID Promise example, lines 53-54.

## Related

- Company: [[braintree]]
- Concept: [[braintree-server-sdk]]
- Related concept: [[braintree-web-drop-in]]
- Related source: [[source-braintree-get-started]]

## Raw Sources

- [[raw/braintree/docs/reference/request/client-token/generate/node-2026-09-16|Braintree Node.js client-token generation reference]] - complete page covering basic generation and the customer-ID variant
