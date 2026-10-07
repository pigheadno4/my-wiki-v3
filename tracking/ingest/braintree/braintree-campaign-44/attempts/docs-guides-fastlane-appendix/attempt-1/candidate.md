---
title: "Braintree Fastlane Appendix"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/fastlane/appendix"
raw_files:
  - "braintree/docs/guides/fastlane/appendix-2026-09-16.md"
tags: [braintree, paypal, fastlane, profile-data, payment-token, vault]
---

## Overview

This collected [[braintree]] Fastlane appendix for [[paypal-fastlane]] records profile-data priority and short FAQs about a client-returned `paymentToken`, Braintree server-side vaulting through `transaction.sale()`, allowed shipping locations, and checkout-page reload authentication. It is an unversioned 2026-09-16 website snapshot, updated on the page in 2026, that names browser-side `braintree.fastlane.create()` and `triggerAuthenticationFlow()` calls but no exact SDK version or environment; it does not establish current availability, merchant or payer eligibility, hosted behavior, token acceptance, vault success, or payment execution.

## Key takeaways

- To create a Fastlane profile, the table puts phone number and email in the UI only. Billing and shipping addresses give the API first priority and UI tokenization second priority; first and last names are derived from their corresponding billing-address fields.
- The page states that a `paymentToken` is valid for three hours from issuance. Treat that as this snapshot's token-lifetime statement, not evidence that a token remains usable or was accepted.
- For shipping eligibility, the page says the initial `braintree.fastlane.create()` call can receive an allowed-location list through `addressOptions`; the exact object shape is routed to the separate Reference Types documentation.
- As a best practice when the checkout page reloads, the page directs the client to call `triggerAuthenticationFlow()` again. It says SDK logic decides between another OTP challenge and session restoration, and that either path returns `authenticatedCustomerResult` with a new `paymentToken`. This is page-stated behavior without an identified SDK version.

> [!warning] Vault ordering is internally unclear in the captured text
> The FAQ first says the client-returned token can be vaulted before creating a server transaction, then says vaulting is supported only by setting `store_in_vault_on_success` in `transaction.sale()` and that creating a `customer` or `payment_method` before a transaction is unsupported. Preserve this inconsistency; do not infer a supported pre-transaction customer or payment-method creation flow from the first clause.

## Detail locators

- Required Fastlane profile data and UI/API priority: `##### Fastlane profile data priority`, raw lines 17-29.
- Client token, server transaction and vault-ordering statements: `##### Will Fastlane work if I save payer’s payment methods?`, raw lines 35-37.
- `paymentToken` three-hour lifetime: `##### How long is a paymentToken valid for?`, raw lines 38-40.
- Allowed shipping locations through `addressOptions` on initial creation: raw lines 41-43.
- Checkout-reload best practice, SDK-controlled OTP-versus-session decision, and returned replacement token: raw lines 44-46.

## Related

- Company: [[braintree]]
- Main concept: [[paypal-fastlane]]
- Browser integration route: [[source-braintree-docs-guides-fastlane-client-side-node]]
- Braintree server processing route: [[source-braintree-docs-guides-fastlane-server-side-node]]
- Broader troubleshooting route: [[source-braintree-docs-guides-fastlane-faq]]
- Reference-object route: [[source-braintree-docs-guides-fastlane-reference]]

## Raw Sources

- [[raw/braintree/docs/guides/fastlane/appendix-2026-09-16|Braintree Fastlane appendix (collected 2026-09-16)]] - fully read pinned snapshot covering profile-data priority, vaulting limitations, token lifetime, shipping-location input and reload authentication guidance
