---
title: "Braintree Node PayPal Payee Advanced Options"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/paypal-advanced-options/payee/node"
raw_files:
  - "braintree/docs/reference/general/paypal-advanced-options/payee/node-2026-09-16.md"
tags: [braintree, paypal, node, transactions, payee, routing]
---

## Overview

This 2026-09-16 snapshot of a [[braintree]] Node-routed PayPal advanced-options reference describes supplying `payee_id` or `payee_email` on a PayPal transaction sale request to route the payment to a different PayPal account owned by the merchant. It is a Braintree website reference route within [[paypal-braintree-integration]], not direct PayPal API, current account-eligibility, exact SDK-version, or successful-payment evidence.

## Key takeaways

- Without a payee override, Braintree sends the PayPal payment to the PayPal business account linked in the Braintree Control Panel. With `payee_id` or `payee_email`, the specified PayPal account receives all transaction funds as though the transaction were processed entirely on that account; the linked Control Panel account does not see that transaction in its account or reporting.
- The page limits the routing use case to different PayPal accounts the merchant owns. `payee_id` is the receiving account's Merchant account ID and is described as preferable because that identifier cannot be changed; `payee_email` uses the receiving account's email. The captured NOTE between the two variants has missing identifiers, so its parameter/method restrictions cannot be reconstructed safely from this raw.
- Depending on the processing setup, the receiving PayPal accounts may need additional permissions or configuration. Neither payee parameter controls currency: choose a Braintree `merchant_account_id` configured for the required currency and with PayPal payments enabled.
- Refunds use the ordinary Braintree refund path without supplying either payee parameter; Braintree withdraws the funds from the PayPal account that received the original transaction.
- The payee parameters are not exposed in Braintree Control Panel transaction reporting. The page directs merchants that need separate reporting to ask for a unique `merchant_account_id` for each planned payee ID and email.

## Detail locators

- Normal linked-account flow and callback/Promise sale examples: raw lines 23-47.
- Dynamic receiver effect: raw lines 49-54.
- `payee_id` meaning, preference, examples, and the damaged restriction note: raw lines 55-92.
- `payee_email` meaning and examples: raw lines 95-128.
- PayPal-permission and multi-currency setup, including callback/Promise examples: raw lines 130-173.
- Refund and Control Panel reporting behavior: raw lines 175-184.

## Related

- [[paypal-braintree-integration]]
- [[braintree-server-sdk]]
- [[braintree-control-panel]]
- [[braintree-currencies]]

## Raw Sources

- [[raw/braintree/docs/reference/general/paypal-advanced-options/payee/node-2026-09-16|Braintree Node PayPal Payee advanced-options reference (2026-09-16)]]
