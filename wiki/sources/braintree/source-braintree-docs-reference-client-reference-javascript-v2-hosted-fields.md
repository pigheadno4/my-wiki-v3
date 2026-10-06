---
title: "Braintree JavaScript v2 Hosted Fields Client Reference"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/client-reference/javascript/v2/hosted-fields"
raw_files:
  - "braintree/docs/reference/client-reference/javascript/v2/hosted-fields-2026-09-16.md"
tags: [braintree, javascript-v2, hosted-fields, client-reference, card-fields]
---

## Overview

This collected [[braintree]] website snapshot is a JavaScript v2 client-reference page for Hosted Fields events, iframe-internal styling, and configuration options. It documents field state and browser-side configuration for the historical v2 surface; it does not itself document tokenization or the client-to-server nonce handoff, establish PCI certification or comprehensive security, assign a current SDK lifecycle state, prove Sandbox or Production availability, or show successful authorization, capture, settlement, or funding. Use [[braintree-web-sdk]] for the broader integration boundary and separately qualified lifecycle and exact-version evidence.

## Key takeaways

- `onFieldEvent` can receive `focus`, `blur`, and `fieldStateChange` events. The event object exposes field-state signals such as empty, focused, potentially valid and valid, plus a field key and detected card data. These signals describe input and UI state; even `isValid` is only whether the associated input is fully qualified for submission, not proof of tokenization or a payment result.
- A `fieldStateChange` can return a card type for the current input. The value is `null` when information is insufficient or data is invalid; the card metadata includes display/type values, security-code metadata and expected card-number lengths. The page says Hosted Fields uses the separate `credit-card-type` library internally, but this website snapshot is not exact-version package evidence.
- The internal-styling section limits configuration inside the Hosted Fields iframes to its listed CSS properties. Unsupported properties fail and produce a console warning. The two tap-highlight properties are qualified as supported only in versions 2.18.0 and above; this does not make the whole snapshot evidence for another v2 release or for JavaScript v3.
- The top-level configuration table marks card number and expiration date as required, but its footnote narrows that requirement to creating, saving, or using card information not already stored in the Vault. For verification of an already vaulted card, the page says only CVV can be collected. Keep that field-specific exception distinct from general payment-method, verification, or transaction requirements.
- Each configured field has a required DOM `selector` and an optional `placeholder`. The page's selectors and callback code are configuration examples and reference details, not evidence that an iframe loaded, tokenization occurred, server processing ran, or a payment completed.

## Detail locators

- **Events, lines 17-57** — `onFieldEvent` subscription; focus, blur and `fieldStateChange`; callback example; event-state properties, container target, field keys and card object.
- **Card type, lines 60-72** — nullable card detection, code-friendly and display names, brand-specific security-code metadata, expected card-number lengths and the `credit-card-type` navigation link.
- **Internal styling properties, lines 75-156** — iframe-internal CSS allowlist, unsupported-property console warning and the v2.18.0-or-later qualification for tap-highlight properties.
- **Options > Top-level options, lines 162-211** — styles and event callback options; number, expiration, CVV and postal-code fields; combined-versus-split expiration fields; and the Vault-specific required-field footnote.
- **Options > Field-level options, lines 212-238** — applicable field set, required container selector examples and optional placeholder.

## Related

- Company: [[braintree]]
- Concept: [[braintree-web-sdk]]
- [[source-braintree-start-hosted-fields]] — broader Hosted Fields orientation route.
- [[source-braintree-client-sdk-migration-javascript-v3]] — separately collected v2-to-v3 migration route.
- [[source-braintree-client-sdk-deprecation-policy-javascript-v3]] — separately collected lifecycle-policy route; this v2 reference does not establish its own current status.

## Raw Sources

- [[raw/braintree/docs/reference/client-reference/javascript/v2/hosted-fields-2026-09-16|Braintree JavaScript v2 Hosted Fields client-reference snapshot (2026-09-16)]]
