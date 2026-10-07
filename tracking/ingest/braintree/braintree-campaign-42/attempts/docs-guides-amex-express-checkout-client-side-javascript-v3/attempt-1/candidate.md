---
title: "Braintree Amex Express Checkout Client-Side Implementation (JavaScript v3)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/amex-express-checkout/client-side/javascript/v3"
raw_files:
  - "braintree/docs/guides/amex-express-checkout/client-side/javascript/v3-2026-09-16.md"
tags: [braintree, amex-express-checkout, javascript, client-sdk, payment-methods]
---

## Overview

This 2026-09-16 Braintree website snapshot is the JavaScript v3 client-side implementation guide for the legacy Amex Express Checkout flow. It documents loading the Braintree and American Express browser scripts, inserting and configuring the Amex button, receiving an American Express nonce through a global callback, and optionally passing that nonce to the Braintree SDK to retrieve cardmember profile data. The nonce can be sent to a separate server-side transaction path; client setup, callback receipt, nonce creation or profile retrieval is not proof of transaction creation, authorization, settlement or funding.

The page says Amex Express Checkout has been replaced by Visa Secure Remote Commerce (SRC) and directs previous users to integrate with SRC, but it also says SRC is limited to eligible merchants, subject to change and access-requested. This snapshot does not establish current support for either product, merchant eligibility or enablement.

## Key takeaways

- The integration relies on Braintree's JavaScript SDK and specifically the `american-express` component. The page separately requires the American Express script and shows `amex:init`, `amex:buy` and a target container for inserting the checkout button. Merchant client identifiers/keys are obtained from the Braintree Control Panel; exact markup and navigation remain in the raw locator.
- For Amex's QA environment, the page directs merchants to change the `amex:init` `env` parameter from `production` to `qa`. It also lists `theme` and `button_color` presentation values and directs all website implementers to review American Express Brand Requirements before going live. These are captured setup directions, not evidence that an account is enabled or that a checkout succeeds.
- The callback must be on `window` scope and be available before the Amex JavaScript executes. The captured sentence after "defined in a" is incomplete, so this entry does not infer the omitted container or file type. The callback's returned nonce is described as a standard payment-method nonce usable for a separate server transaction.
- To request cardmember details, the page passes the American Express nonce to Braintree's client/`americanExpress` SDK flow and provides callback and Promise examples. A missing profile is represented as a payload containing status `404` and `Profile not found`; the page says this appears in the payload argument rather than the direct error argument because it is an American Express error.
- The profile contains one `amexExpressCheckoutCards` item. The raw table is the authority for its fields and examples: some marked fields require American Express approval for the merchant's specific implementation, and caret-marked fields may be unavailable for some customers.

> [!warning] Replacement, release and snapshot boundary
> The captured page calls Amex Express Checkout replaced and directs prior users to SRC, while describing SRC as a limited release for eligible merchants whose API is subject to change. Preserve all qualifications; do not infer current SRC or Amex support, account access, SDK-package behavior or successful payment execution from this stored page. The separately collected SRC source also preserves its own unresolved support-status conflict.

> [!warning] Profile-data and capture-quality boundary
> Profile retrieval is optional data lookup, not payment completion. Merchant approval and per-customer availability qualify the returned fields. The raw callback paragraph is visibly incomplete after "defined in a"; only its explicit window-scope and execution-order statements are retained.

## Detail locators

- Amex replacement, SRC limited-release eligibility, API-change and access-request qualifications, and named SDK generations: `# Client-Side Implementation > AVAILABILITY`, raw line 17.
- Braintree JavaScript SDK and `american-express` component prerequisite: `## Include Braintree.js`, raw line 22.
- American Express script, button markup, merchant client credential locations and QA `env` change: `## Include the American Express script`, raw lines 25-41.
- Button `theme` and `button_color` values plus pre-live Brand Requirements direction: raw lines 45-55.
- Global callback, execution order, nonce identity and separate server-transaction route, including the incomplete captured sentence: `## Create the global callback handler`, raw lines 58-66.
- Cardmember profile request purpose and legacy/client-component callback and Promise examples: `## Retrieve cardmember details`, raw lines 69-85.
- Missing-profile payload shape and payload-versus-error-argument explanation: raw lines 86-93.
- Profile array cardinality, field inventory/examples, merchant-approval and per-customer availability qualifiers: `### Profile payload`, raw lines 96-120.
- Billing-address field inventory and availability qualification: `### Billing address fields`, raw lines 123-135.
- American Express component reference route: raw line 139.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Replacement-product source and unresolved support-status boundary: [[source-braintree-payment-methods-secure-remote-commerce]]
- Browser SDK context: [[braintree-web-sdk]]

## Raw Sources

- [[raw/braintree/docs/guides/amex-express-checkout/client-side/javascript/v3-2026-09-16|Braintree Amex Express Checkout client-side implementation for JavaScript v3]] - complete collected page covering the replacement notice, scripts and button setup, nonce callback, optional profile retrieval and qualified profile fields
