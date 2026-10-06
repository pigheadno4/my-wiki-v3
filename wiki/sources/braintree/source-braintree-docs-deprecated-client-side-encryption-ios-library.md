---
title: "Braintree Deprecated Client-Side Encryption iOS Library"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/deprecated/client-side-encryption/ios-library"
raw_files:
  - "braintree/docs/deprecated/client-side-encryption/ios-library-2026-09-16.md"
tags: [braintree, ios, deprecated, client-side-encryption, credit-cards]
---

## Overview

This 2026-09-16 website snapshot documents Braintree's deprecated legacy iOS client-side-encryption library. The legacy SDK combined a credit-card payment form with client-side encryption, but the page says the components could be used independently and required a web server using a Braintree server-side client library; the iOS SDK did not interact with the gateway directly. This snapshot is historical integration evidence, not evidence of current SDK or GitHub support.

## Key takeaways

- The page explicitly marks the integration method deprecated and directs readers to Braintree SDK upgrade guidance. It should not be treated as a current iOS integration recommendation.
- For the manual-entry save-card callback described here, the app receives both raw card information and an encrypted dictionary. The page directs the app to send the encrypted dictionary to its server, which then sends it to Braintree; this client-side encryption does not itself establish PCI compliance, payment authorization, Vault success, or transaction success.
- Configuration uses a client-side-encryption public key obtained from either the Braintree production gateway or Braintree sandbox. The page describes asymmetric encryption in which Braintree can decrypt the value but the client cannot, after which the value can pass through the merchant's servers for use by a Braintree server client library. The page distinguishes the two key sources but does not prove that either environment is configured or that encryption succeeded.
- Payment-form, networking, Vault, error-display, and encryption snippets are examples rather than guarantees. In particular, a displayed success branch depends on the example server response after valid card data is added to the Vault; the page does not prove that a payment was authorized or processed.

## Detail locators

- Deprecation notice and upgrade route: raw lines 17-18.
- Legacy SDK components and mandatory merchant-server boundary: `## Overview`, raw lines 21-29.
- Payment-form initialization and modal presentation example: `## Payment form`, raw lines 30-52.
- Manual-entry save-card callback, raw-versus-encrypted dictionaries, and server handoff: `### Save card flow`, raw lines 57-69.
- Stored Venmo Touch card callback and payment-method-code example: `### Use card flow`, raw lines 71-77.
- Example client-to-server-to-gateway method, Vault-success branch, cleanup, and omitted networking boilerplate: `### Putting it all together`, raw lines 79-94.
- Example decline/error conditions: `### Error handling`, raw lines 95-103.
- Production-gateway versus sandbox key retrieval, public-key initialization, asymmetric-encryption behavior, and server-client-library handoff: `## Encryption > ### Configuration`, raw lines 106-120.
- Credit-card-number/CVV use-case description and complete Objective-C sample: `## Encryption > ### Example`, raw lines 121-152.

## Related

- [[braintree]]
- [[braintree-ios-sdk]]

## Raw Sources

- [[raw/braintree/docs/deprecated/client-side-encryption/ios-library-2026-09-16|Braintree deprecated client-side encryption iOS library (2026-09-16 snapshot)]]
