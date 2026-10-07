---
title: "Braintree Elo Client-Side Implementation (JavaScript v3)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/elo/client-side/javascript/v3"
raw_files:
  - "braintree/docs/guides/elo/client-side/javascript/v3-2026-09-16.md"
tags: [braintree, elo, javascript-v3, credit-cards]
---

## Overview

This 2026-09-16 snapshot is a Braintree JavaScript v3 client-side Elo checkout guide with separate server-processing notes. At capture, the page described Elo as a limited release for select merchants using the latest JavaScript v3 and server SDK families and directed merchants to request access. The snapshot does not identify a current exact package release, environment, merchant configuration, coverage window, or payment outcome.

## Key takeaways

- Some Elo cards also carry the Discover brand and can use either network; for a business based outside Brazil, the page says card-network rules require those dual-branded transactions to use Discover.
- The page characterizes Elo cards as credit-only, requires CVV and expiration date in the checkout form, and says the server transaction may use immediate settlement submission or a separate later submission call.
- The setup section shows a JavaScript v3 client script example. Its pinned `3.94.0` URL is a captured example, not evidence that this is the current, universally required, or merchant-enabled package version.

## Detail locators

- Limited-release and SDK-family condition — `AVAILABILITY` (line 18)
- Dual-branded Elo/Discover routing — `Checkout form` → `Dual-branded cards` (lines 21–29)
- Credit-only form and settlement choices — `Checkout form` → `Card capabilities` (lines 30–36)
- Client script example — `Setup` → `HTML` (lines 41–47)

## Related

- [[braintree]] — provider context
- [[braintree-payment-methods]] — provider-wide eligibility and regional card-routing boundaries
- [[braintree-web-sdk]] — JavaScript client SDK family and client/server integration boundary

## Raw Sources

- [[raw/braintree/docs/guides/elo/client-side/javascript/v3-2026-09-16|Braintree Elo client-side JavaScript v3 guide (2026-09-16 snapshot)]]
