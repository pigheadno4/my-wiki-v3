---
title: "Braintree PayPal Vaulted Payments for Android v5"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/vault/android/v5"
raw_files:
  - "braintree/docs/guides/paypal/vault/android/v5-2026-09-16.md"
tags: [braintree, paypal, vault, android, sdk-v5]
---

## Overview

This archived [[braintree]] website guide documents PayPal vaulted payments through the Braintree Android SDK v5. It describes creating a PayPal pre-approved payment so the merchant can charge the account later without requiring the customer to be present or re-authenticate, and routes the topic to [[paypal-vault]].

## Key takeaways

- Initialize `PayPalLauncher` in the Activity's `onCreate`, then configure `PayPalClient` with a tokenization key or client token and return URLs. After the customer selects PayPal, create a `PayPalVaultRequest`, request payment authorization, launch a ready request, and persist the pending request string when launch returns `Started`.
- On return, pass the persisted pending request and Intent to `PayPalLauncher.handleReturnToApp()`. A successful authorization result is then passed to `PayPalClient.tokenize()`; successful tokenization returns a nonce in `PayPalAccountNonce`. Cancellation/no-result and failure are distinct outcomes that the integration must handle.
- The snapshot carries a high-impact certificate warning: Braintree Mobile SDK certificates were set to expire on March 30, 2026, it directs Android integrations to 4.45.0+ or 5.0.0+, and says traffic on app versions left on older certificates will fail. This is a dated snapshot warning, not proof of current SDK status.
- Device-data collection is required when initiating non-recurring transactions from Vault records. The guide also says shipping addresses may or may not be collected during the Vault flow.
- The raw has an unresolved return-handling inconsistency: its prose says `onNewIntent()` applies when the Activity launch mode is `>SINGLE_TOP`, while the code comment says it is required only for `SINGLE_TOP`. The source is preserved as written; verify the intended Android launch-mode condition before implementation.
- The Vault flow does not display the transaction amount or currency to the customer; the merchant must display them elsewhere in checkout.

## Detail locators

- `Launch the flow` and `Invoking the Vault flow` (raw lines 55-140): dependency snippet, initialization, request launch, pending-request persistence, return handling, tokenization, and nonce result.
- `Complete Integration` (raw lines 193-280): consolidated Kotlin example.
- `Collecting device data` (raw lines 283-287): non-recurring Vault transaction requirement and `DataCollector` purpose.
- `Integrating App Switch` (raw lines 290-309): separate redirect-flow orientation and link to its implementation guide.
- `Shipping address`, `Country and language support`, and `Currency presentment` (raw lines 312-324): address handling, stated geographic reach, and merchant display responsibility.

## Related

- [[braintree]]
- [[paypal-vault]]

## Raw Sources

- [[raw/braintree/docs/guides/paypal/vault/android/v5-2026-09-16|Braintree PayPal Vaulted Payments — Android v5 (2026-09-16 snapshot)]]
