---
title: "Stripe — Vault and Forward API"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-vault-and-forward-2026.md"
tags: [stripe, vault-and-forward, multiprocessor, card-forwarding, pci, adyen, braintree, worldpay, apple-pay, google-pay]
---

## Summary

Vault and Forward API: tokenize cards in Stripe's PCI vault and forward to 30+ supported third-party processors. Requires Stripe support access request.

## ForwardingRequest API

```js
stripe.forwarding.requests.create({
  payment_method: 'pm_xxx',
  url: 'https://destination/v1/payments',
  request: { headers: [...], body: '{"paymentMethod":{"number":"","expiryMonth":"","expiryYear":"","cvc":""}}' },
  replacements: ['card_number', 'card_expiry', 'card_cvc', 'cardholder_name']
})
```

## Replacement Fields

| Use case | Replacement fields |
| --- | --- |
| Standard cards | `card_number`, `card_expiry`, `card_cvc`, `cardholder_name` |
| Google Pay FPAN | Same as standard cards |
| Google Pay/Apple Pay DPAN | `network_token_number`, `network_token_cryptogram`, `network_token_expiry`, `network_token_electronic_commerce_indicator` |

## Key Rules

- Placeholder values must match destination JSON type (`""` string, `0` numeric)
- Stripe always returns 200; actual destination status code is in response body
- CVC expires after use; SetupIntent confirmation can consume CVC (contact Stripe for workarounds)
- Link payments NOT supported for forwarding
- Use new idempotency key when retrying or updating request body/headers
- API keys: Stripe only stores hashed+encrypted versions; encrypt with provided PGP key before sharing

## Wallet Support

- **Apple Pay**: DPAN only (not MPAN)
- **Google Pay**: FPAN (standard replacements) and DPAN (network token replacements)
- **Link**: NOT supported

## Supported Processors (partial list)

Adyen, Braintree, Checkout, CardPointe, Evervault, Fat Zebra, Fiserv, PaymentsOS, ProcessOut, Shift4, Spreedly, TabaPay, TokenEx, VGS, Worldpay, Xsolla, Basis Theory, PCI Vault + others.

## Restricted API Keys

`forwarding_request_write` (create) + `forwarding_request_read` (retrieve/list).

## Related Pages

- [[stripe-vault-and-forward]] — concept page
- [[stripe-payment-intents]] — PaymentMethod creation

## Raw Sources

- [[stripe-vault-and-forward-2026]] — verbatim Vault and Forward API guide (762 lines)
