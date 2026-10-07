---
title: "Braintree PINless Debit Optimized Routing: Test and Go Live"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/pinless-debit/optimized-debit-routing/test-and-go-live"
raw_files:
  - "braintree/docs/guides/pinless-debit/optimized-debit-routing/test-and-go-live-2026-09-16.md"
tags: [braintree, pinless-debit, optimized-debit-routing, sandbox-testing, auto-retry]
---

## Overview

This captured unversioned [[braintree|Braintree]] webpage describes Sandbox testing and the move toward a live environment for PINless debit optimized routing. It covers Sandbox enablement, documented test fixtures, amount- and merchant-category-code-dependent debit-network routing, and an optionally enabled retry path from an unsuccessful debit-network transaction to Visa or Mastercard. The snapshot does not establish current availability, account eligibility or enablement, exact SDK or runtime behavior, Production behavior, or a successful authorization, payment, settlement or funding outcome. [[braintree-payment-methods]]

## Key takeaways

- PINless debit is not automatically enabled in a Sandbox account; the page directs the merchant to a Technical account manager for enablement and recommends Sandbox testing before moving to a live environment. Neither the recommendation nor a Sandbox result proves Production readiness or behavior.
- The page supplies two test card values and says optimized routing selects one of STAR, STAR_ACCESS, ACCEL, NYCE or PULSE based on the transaction-sale amount and the merchant account's merchant category code. Those values are testing fixtures from the captured page, not general card data, a routing guarantee outside the stated setup, or evidence that a payment ran.
- If debit-network routing is unsuccessful, Braintree can retry over Visa or Mastercard, but auto-retries require separate enablement through the technical account manager. For a successful retry the page says the debit-network field is empty because the retry uses Visa or Mastercard; when the retry also fails, it describes retained original and subsequent retry transaction IDs.
- The Sandbox auto-retry fixture uses amount `2046` as a negative test: both the debit-network attempt and the Visa-or-Mastercard retry are described as failing. This synthetic failure path is not a Production test or proof of an actual transaction outcome.

## Detail locators

- **Sandbox enablement and before-live recommendation:** `Test and go live`, raw lines 17-22.
- **Test card values:** `Test and go live`, raw lines 22-27.
- **Optimized-routing networks and amount/MCC inputs:** raw line 28.
- **Auto-retry scope, enablement and successful/failed retry semantics:** `Auto-retry`, raw lines 29-35.
- **Displayed Java accessor list and illustrative successful/failed retry payloads:** raw lines 38-78.
- **Sandbox negative auto-retry amount and expected failures:** `Testing auto-retry`, raw lines 80-82.

## Related

- [[braintree]]
- [[braintree-payment-methods]] — main provider concept route for PINless debit optimized-routing documentation.
- [[source-braintree-docs-guides-pinless-debit-optimized-debit-routing-network-response-codes]] — supplemental debit-network response-value reference.

## Raw Sources

- [[raw/braintree/docs/guides/pinless-debit/optimized-debit-routing/test-and-go-live-2026-09-16|Braintree — PINless Debit Optimized Routing: Test and Go Live (2026-09-16 snapshot)]]
