---
title: "Braintree Amex Express Checkout Server-Side Implementation (Node Route)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/amex-express-checkout/server-side/node"
raw_files:
  - "braintree/docs/guides/amex-express-checkout/server-side/node-2026-09-16.md"
tags: [braintree, amex-express-checkout, nodejs, server-side, payment-methods]
---

## Overview

This 2026-09-16 snapshot is an unversioned Braintree website guide on the Node-routed server-side path for legacy Amex Express Checkout. It identifies the American Express client-callback value as a standard payment-method nonce that can be used by a merchant server and routes transaction creation to the separate transactions guide. It does not show a Node invocation or name a Node SDK package, version, runtime or environment.

The page says Amex Express Checkout was replaced by Visa Secure Remote Commerce (SRC) and directs previous users to integrate with SRC. Its own banner calls SRC a limited release for eligible merchants, says the API is subject to change, names Android v2, iOS v4 and JavaScript v3 Client SDK families, and gives an access-request route. Those client-family statements do not establish Node Server SDK behavior.

## Key takeaways

- The nonce returned to the client callback from American Express is described as a standard payment-method nonce usable on the merchant server like another nonce; the page supplies navigation, not a transaction request or successful payment result.
- Amex Express Checkout payment methods expose `card_member_expiry_date` and `card_member_number`, described respectively as the physical card's expiration and last four digits, for helping customers identify the card they used. The captured page does not establish that either field is present for a particular response.
- Detailed transaction behavior and generic payment-method behavior belong to the linked guides; this page's central scope is the legacy Amex nonce handoff plus its two additional response fields.

> [!warning] Replacement and current-availability conflict
> This page's replacement direction points former Amex Express Checkout users to SRC and describes SRC as a current limited release. The separately retained, fully read Braintree payment-method authority says Visa Click to Pay/SRC would no longer be supported effective January 20, 2026 while also calling SRC a current limited release. The snapshots do not resolve present Amex or SRC support, merchant eligibility or a safe executable migration path. See [[source-braintree-get-started-payment-methods]].

## Detail locators

- Amex replacement, SRC limited-release eligibility, API-change warning, Client SDK families and access request: opening `**AVAILABILITY**`, raw lines 17-18.
- Client callback nonce identity and server-use route: `## Performing actions with the nonce`, raw lines 21-25.
- Card-identification purpose and the two additional field definitions: `## Additional payment method fields`, raw lines 26-32.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Complementary browser client route: [[source-braintree-docs-guides-amex-express-checkout-client-side-javascript-v3]]
- Provider-wide authority carrying the unresolved SRC support conflict: [[source-braintree-get-started-payment-methods]]

## Raw Sources

- [[raw/braintree/docs/guides/amex-express-checkout/server-side/node-2026-09-16|Braintree Amex Express Checkout server-side Node route]] - fully read pinned website snapshot covering the replacement notice, nonce handoff and additional card-identification fields
