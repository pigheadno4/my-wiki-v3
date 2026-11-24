---
title: "Stripe Vault and Forward API"
type: concept
category: technology
tags: [stripe, vault-and-forward, multiprocessor, card-forwarding, pci, adyen, braintree, worldpay]
---

## Overview

Vault and Forward stores card details in Stripe’s PCI-compliant vault and forwards them to configured destinations. The November 7, 2026 general guide directs businesses with a dedicated Stripe account team to request access through that team. The earlier general guide and separate November specialist guides direct readers to Stripe support. See [[source-stripe-vault-and-forward]].

## Use Cases

- Use Payment Element across multiple processors
- Use Stripe as primary card vault across processors
- Route to own PCI-compliant token vault

## ForwardingRequest Flow

1. Collect card details → PaymentMethod created (stored in Stripe vault)
2. Create `ForwardingRequest` with: `payment_method`, `url`, `request.body` (blank card fields), `replacements`
3. Stripe inserts card data into body and forwards to destination
4. Inspect both the Forwarding API response and destination result. The general [[source-stripe-vault-and-forward]] guide says a response received from the destination yields forwarding HTTP 200 even when the destination returns 400, with its response/error in the body. The own-vault guide instead says the API returns the same status, while its concrete example also shows vault 400 yielding API 200; preserve that wording tension. The third-party processor example separately checks `response_details.status` and catches request errors. Neither API 200 nor a forwarded response proves vault token creation, processor authorization, capture or settlement. See [[source-stripe-forwarding-third-party]] and [[source-stripe-forwarding-token-vault]].

## Replacement Fields

| Use case | Fields |
| --- | --- |
| Standard cards + Google Pay FPAN | `card_number`, `card_expiry`, `card_cvc`, `cardholder_name` |
| Google Pay DPAN / Apple Pay DPAN | `network_token_number`, `network_token_cryptogram`, `network_token_expiry`, `network_token_electronic_commerce_indicator` |

## Key Rules

- Placeholder values must match destination JSON type (`""` string, `0` numeric)
- CVC expires with time or forwarding use. SetupIntent confirmation can consume it, so it may need to be recollected if the destination requires it.
- **Link payments excluded** from forwarding
- Use separate Stripe and destination idempotency keys. Use a fresh Stripe key when changing the body or headers. The guide recommends a fresh Stripe key for retries after an error reaching the destination.
- Third-party API keys: encrypt with Stripe's PGP key before sharing; Stripe stores only hashed+encrypted versions

## Wallet Support

- **Apple Pay**: The May 2026 guide lists DPAN only. November’s support list also includes MPAN, while its detection and replacement guidance covers DPAN. See [[source-stripe-vault-and-forward#Wallets and replacement fields|dated wallet qualifications]].
- **Google Pay**: FPAN (standard fields) and DPAN (network token fields)
- **Link**: NOT supported

## Configured destinations

See [[source-stripe-vault-and-forward#Configured endpoints and key scope|the dated exact endpoint and country locators]] to check a destination. The [[source-stripe-forwarding-token-vault|configured own-vault guide]] covers the separate in-house tokenization path.

## Restricted API Keys

`forwarding_request_write` is required for creation. `forwarding_request_read` is optional for retrieval and listing.

## Sources

- [[source-stripe-vault-and-forward]] — May and November 2026 general guides for access, configured endpoints, forwarding responses, and dated wallet and key qualifications.
- [[source-stripe-forwarding-third-party]] — May/November 2026 Payment Element multiprocessor guide: manual PaymentMethod creation, server ForwardingRequest, processor-response relay and identified-PCI-data redaction boundary
- [[source-stripe-forwarding-token-vault]] — own token vault requirements, PCI, CVC rules, webhook updates
