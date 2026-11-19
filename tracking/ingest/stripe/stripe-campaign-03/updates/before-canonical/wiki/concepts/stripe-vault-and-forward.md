---
title: "Stripe Vault and Forward API"
type: concept
category: technology
tags: [stripe, vault-and-forward, multiprocessor, card-forwarding, pci, adyen, braintree, worldpay]
---

## Overview

Vault and Forward API: store card details in Stripe's PCI-compliant vault and forward to 30+ supported third-party processors. **Requires access request via Stripe support** (not self-serve).

## Use Cases

- Use Payment Element across multiple processors
- Use Stripe as primary card vault across processors
- Route to own PCI-compliant token vault

## ForwardingRequest Flow

1. Collect card details → PaymentMethod created (stored in Stripe vault)
2. Create `ForwardingRequest` with: `payment_method`, `url`, `request.body` (blank card fields), `replacements`
3. Stripe inserts card data into body and forwards to destination
4. Stripe returns 200; actual destination status is in response body

## Replacement Fields

| Use case | Fields |
| --- | --- |
| Standard cards + Google Pay FPAN | `card_number`, `card_expiry`, `card_cvc`, `cardholder_name` |
| Google Pay DPAN / Apple Pay DPAN | `network_token_number`, `network_token_cryptogram`, `network_token_expiry`, `network_token_electronic_commerce_indicator` |

## Key Rules

- Placeholder values must match destination JSON type (`""` string, `0` numeric)
- CVC expires after use; SetupIntent confirmation can consume CVC
- **Link payments excluded** from forwarding
- Use new idempotency key when retrying or modifying request
- Third-party API keys: encrypt with Stripe's PGP key before sharing; Stripe stores only hashed+encrypted versions

## Wallet Support

- **Apple Pay**: DPAN only (MPAN not supported)
- **Google Pay**: FPAN (standard fields) and DPAN (network token fields)
- **Link**: NOT supported

## Supported Processors (30+)

Accertify, Adyen, Basis Theory, Braintree, CardPointe, Checkout, Evervault, Expedia, Fat Zebra, Fiserv, FlexPay, GMO, PaymentsOS, PCI Vault, ProcessOut, Rewards Network, Shift4, SoftBank, Spreedly, TabaPay, TokenEx, VGS, Worldpay, Xsolla + own PCI token vault.

## Restricted API Keys

`forwarding_request_write` + `forwarding_request_read`.

## Sources

- [[source-stripe-vault-and-forward]] — ForwardingRequest API, replacement fields, wallet support, processor list, PGP key
- [[source-stripe-forwarding-third-party]] — Payment Element multiprocessor integration (paymentMethodCreation: 'manual' flow)
- [[source-stripe-forwarding-token-vault]] — own token vault requirements, PCI, CVC rules, webhook updates
