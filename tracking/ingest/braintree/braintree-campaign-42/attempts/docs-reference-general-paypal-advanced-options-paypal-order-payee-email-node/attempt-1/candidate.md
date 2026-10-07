---
title: "Braintree PayPal Order Payee Email (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/paypal-advanced-options/paypal-order/payee-email/node"
raw_files:
  - "braintree/docs/reference/general/paypal-advanced-options/paypal-order/payee-email/node-2026-09-16.md"
tags: [braintree, paypal, paypal-order, payee-email, node, vault]
---

## Overview

This 2026-09-16 Braintree-hosted Node.js reference explains how a merchant can set `payee_email` while creating a payment method for a PayPal Order so transactions processed against that payment method route to a different merchant-owned PayPal account instead of the PayPal account linked in the Braintree Control Panel. It is a captured documentation route, not proof of current account eligibility, configuration, payment execution, settlement, or reporting results. See [[braintree]] and [[paypal-braintree-integration]].

## Key takeaways

- Without `payee_email`, Braintree sends funds from transactions against the created payment method to the PayPal account linked in the Control Panel. With `payee_email`, the specified merchant-owned PayPal account receives all funds for all transactions processed against that payment method, and the linked Control Panel account does not see those transactions in its account or reporting.
- The Node examples place `payeeEmail` under `options.paypal` in `gateway.customer.create` and `gateway.customer.update`, with callback and Promise variants. These examples show request shape; their illustrated `result.success` comments are not a guarantee of a successful operation.
- Depending on the processing setup, the receiving PayPal accounts may need additional configuration for `payee_email`. The page does not establish that a particular account is configured or eligible.
- `payee_email` does not select transaction currency. The captured multi-currency sentence says a Braintree item must be configured for the currency but omits the item's noun; it separately says the specified `merchant_account_id` must have PayPal payments enabled. Do not reconstruct the missing term from this snapshot.
- Refunds use the normal Braintree refund path without supplying `payee_email`; Braintree says it withdraws the funds from the same PayPal account that received the original transaction. The parameter is not exposed in Control Panel transaction reporting; the page directs merchants needing separate reporting to request a unique `merchant_account_id` for each planned `payee_email`.

## Detail locators

- **Purpose, ownership condition, and routing target:** opening paragraph, lines 14–21.
- **Default versus payee-email transaction and reporting behavior:** `How it works`, lines 22–38.
- **New-customer request shapes:** `Create new customer with payment method and payee email`, lines 42–90.
- **Existing-customer update shapes and captured missing-method text:** `Update existing customer with new payment method and payee email`, lines 92–126. The page identifies a not-found error when the customer cannot be found, but its following alternative-operation sentence is incomplete in the capture.
- **PayPal configuration and multi-currency qualifications:** `Setup`, lines 127–138.
- **Refund account behavior:** `Refunds`, lines 139–142.
- **Control Panel reporting limitation and separate-reporting route:** `Reporting in the Braintree Control Panel`, lines 143–147.

## Related

- [[paypal-braintree-integration]] — Braintree-specific PayPal integration and server-boundary retrieval hub; keep this page distinct from direct PayPal Orders API authority.

## Raw Sources

- [[raw/braintree/docs/reference/general/paypal-advanced-options/paypal-order/payee-email/node-2026-09-16|Braintree PayPal Order payee-email Node page (2026-09-16)]]
