---
title: "Braintree Masterpass Client-Side Implementation (JavaScript v3)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/masterpass/client-side/javascript/v3"
raw_files:
  - "braintree/docs/guides/masterpass/client-side/javascript/v3-2026-09-16.md"
tags: [braintree, masterpass, javascript-v3, tokenization, secure-remote-commerce]
---

## Overview

This Braintree website snapshot documents the JavaScript v3 client-side flow for a legacy Masterpass component: create the Braintree client and Masterpass component, reveal the button after availability is reported, invoke tokenization from a customer action, and send the resulting nonce to the server to create a transaction. The page states that Masterpass has been replaced by Secure Remote Commerce (SRC), so it is historical integration evidence rather than proof of current availability, enablement, exact hosted or SDK behavior, or successful payment execution. [[braintree]] [[braintree-payment-methods]]

> [!warning] Unresolved SRC support conflict
> This snapshot directs former Masterpass users to limited-release SRC, while the separately retained SRC authority carries an end-of-support notice. The retained routes do not resolve present SRC support or establish a safe migration path; consult [[source-braintree-payment-methods-secure-remote-commerce]] before relying on this migration direction.

## Key takeaways

- The page says former Masterpass users need to integrate with SRC. It simultaneously describes SRC as a limited release for eligible merchants, says its API is subject to change, and directs merchants to contact Braintree to request access.
- Client setup uses either a tokenization key or a client token from the server. The page has the merchant create a Masterpass component and display the initially hidden button only after the component reports availability.
- To request payment, the page calls `masterpassInstance.tokenize` with `subtotal` and `currencyCode`; the Masterpass popup prompts the customer to authorize, and a successful `payload.nonce` is sent to the server to create the transaction.
- Because tokenization opens a popup, the guide requires the call to result from a customer action such as a button click; it cannot be invoked arbitrarily.

## Detail locators

- Replacement, SRC limited-release eligibility, API-change qualification and access request: raw lines 17–22.
- JavaScript v3 setup and the example `client.min.js` and `masterpass.min.js` URLs at version `3.88.1`: raw lines 27–35.
- Masterpass branding note plus the example button and initially hidden CSS: raw lines 37–59.
- Client authorization choices, component creation and availability-gated button display, with callback and Promise examples: raw lines 61–135.
- Tokenization inputs, popup authorization, successful nonce handoff and the optional-configuration reference: raw lines 137–144.
- Callback example, including the customer-action constraint and popup-closed error branch: raw lines 146–180.
- Promise example of the same tokenization flow and popup-closed error branch: raw lines 182–212.

## Related

- [[braintree]]
- [[braintree-payment-methods]]
- [[source-braintree-payment-methods-secure-remote-commerce]] - separate retained SRC authority for the unresolved support-status conflict

## Raw Sources

- [[raw/braintree/docs/guides/masterpass/client-side/javascript/v3-2026-09-16|Braintree Masterpass Client-Side Implementation — JavaScript v3 (2026-09-16 snapshot)]]
