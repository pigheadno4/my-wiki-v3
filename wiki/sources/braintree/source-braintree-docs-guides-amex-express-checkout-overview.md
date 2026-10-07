---
title: "Braintree Amex Express Checkout Overview"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/amex-express-checkout/overview"
raw_files:
  - "braintree/docs/guides/amex-express-checkout/overview-2026-09-16.md"
tags: [braintree, amex-express-checkout, payment-methods, secure-remote-commerce]
---

## Overview

This 2026-09-16 Braintree website snapshot is an unversioned overview of the legacy Amex Express Checkout product. It describes a website checkout in which eligible American Express cardmembers use Amex credentials and American Express returns a merchant-specific card number linked to the physical card; Braintree stores that number in the Vault and gives the merchant a nonce for transaction creation.

The page says the product was available to most US-domiciled merchants and merchants processing Amex through a direct American Express account, while limiting cardmember eligibility to the US. Its setup route spans Control Panel configuration, a checkout-page client script, a server-integration adjustment, and testing/go-live guidance.

## Replacement and availability warning

> [!warning] Unresolved snapshot status
> The same page says Amex Express Checkout was replaced by Visa Secure Remote Commerce (SRC) and directs prior users to integrate with SRC, yet its legacy product description says Amex Express Checkout is "currently available" under the stated merchant conditions. The snapshot does not reconcile those statements. It also describes SRC as a limited release for eligible merchants, says its API is subject to change, names Android v2, iOS v4 and JavaScript v3 as the Client SDK generations in which SRC was introduced, and requires an access request.

## Scope and evidence boundary

This overview records historical product purpose, eligibility language, the Vault-and-nonce handoff, and navigation to separate client/server setup stages; it does not specify an environment or exact implementation and does not establish current Amex Express Checkout or SRC support, merchant access, runtime behavior, migration success, or payment outcome.

## Detail locators

- Replacement by SRC, limited-release eligibility, API-change warning, Client SDK generation labels and access request: `AVAILABILITY`, raw lines 17-18.
- Amex Express Checkout purpose and merchant/cardmember eligibility: raw lines 20-23.
- Merchant-specific card number, Vault storage and transaction nonce: `## How it works`, raw lines 24-28.
- Control Panel, client-side, server-side and testing/go-live route sequence: `## Setup`, raw lines 29-35.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]

## Raw Sources

- [[raw/braintree/docs/guides/amex-express-checkout/overview-2026-09-16|Braintree Amex Express Checkout overview — fetched 2026-09-16]]
