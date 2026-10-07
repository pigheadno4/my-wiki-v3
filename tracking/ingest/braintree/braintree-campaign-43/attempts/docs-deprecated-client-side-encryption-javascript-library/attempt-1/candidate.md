---
title: "Braintree Deprecated Client-Side Encryption JavaScript Library"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/deprecated/client-side-encryption/javascript-library"
raw_files:
  - "braintree/docs/deprecated/client-side-encryption/javascript-library-2026-09-16.md"
tags: [braintree, javascript, client-side-encryption, deprecated]
---

## Overview

This historical Braintree website snapshot describes the deprecated Client-Side Encryption JavaScript library. The documented flow encrypts sensitive payment input on the client with the public key of an asymmetric key pair, sends the encrypted values to the merchant server, and has a Braintree client library forward them to the gateway, where the corresponding private key is stored for decryption and ordinary gateway processing. The page directs readers to an upgrade route rather than presenting this method as a current integration.

## Key takeaways

- The page names card number, CVV, and expiration date as payment-method information that should be encrypted.
- Its client/server split has the client collect input, encrypt it with the Braintree client-side encryption library, and send ciphertext over HTTPS to the merchant server; the merchant server then forwards the encrypted request through a Braintree client library and returns gateway response information.
- `onSubmitEncryptForm` installs a form submit handler that encrypts fields carrying `data-encrypted-name` and then submits the form to its configured action. An optional callback runs after encryption, including for an AJAX submission path.
- The page explicitly says there is no cross-browser guarantee that multiple submit handlers run in the intended order. `encryptForm` is the lower-level path for a custom pre-encryption submit callback and immediately encrypts every marked field in the selected form.

## Material limitations

- Braintree labels the entire integration method deprecated and links to an SDK upgrade route. This snapshot does not establish current support, browser compatibility, merchant eligibility, or availability.
- The submit helpers mutate marked form fields before submission, and the documented multiple-handler ordering limitation can matter when validation or other form logic is attached.
- This historical description is not evidence of PCI scope, compliance, security certification, successful tokenization, authorization, payment processing, settlement, or any other payment outcome.

## Detail locators

- `How it works` and the asymmetric encryption/gateway flow: raw lines 21-29.
- Fields named for encryption: raw lines 30-36.
- Client and merchant-server responsibilities: raw lines 39-57.
- `create` and its encryption-key argument: raw lines 58-65.
- `onSubmitEncryptForm`, marked fields, callback timing, and handler-order warning: raw lines 66-75.
- Immediate marked-field encryption through `encryptForm`: raw lines 76-85.
- Single-string `encrypt` compatibility/customization method: raw lines 86-93.

## Related

- [[braintree]]
- [[braintree-web-sdk]] - provider concept for the modular browser SDK, historical lifecycle policy, and exact-version evidence boundaries
- [[source-braintree-upgrade]] - upgrade route linked by this deprecated page

## Raw Sources

- [[raw/braintree/docs/deprecated/client-side-encryption/javascript-library-2026-09-16|pinned Braintree Client-Side Encryption JavaScript library snapshot]]
