---
title: "Stripe — Forward Card Details to Own Token Vault"
type: source
date_ingested: 2026-05-11
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/forwarding-token-vault"
raw_files:
  - "stripe-payments-forwarding-token-vault-2026-11-07.md"
  - "stripe-forwarding-token-vault-2026.md"
tags: [stripe, vault-and-forward, token-vault, pci, own-vault, webhook]
---

## Overview

The 2026-05-11 and 2026-11-07 guides describe a support-gated path for forwarding card details stored in Stripe's vault from a PaymentMethod to an in-house token vault. The merchant creates or obtains a PaymentMethod, then its server creates a ForwardingRequest with that PaymentMethod ID and a configured vault endpoint. Stripe sends card data to the vault; the November diagram additionally states that Stripe redacts identified PCI-sensitive data from the vault response before relaying it to the server (new raw lines 7-24, 26-32; old raw lines 6-21). PaymentMethod creation and request submission do not prove vault token creation or payment success.

## Access and object sequence

- **Access**: Contact Stripe support to request access to the forwarding service; the page does not establish self-serve availability or account eligibility (new raw lines 9-13; old raw lines 8-12).
- **PaymentMethod**: The guide uses the Payment Element to create a PaymentMethod, with direct PaymentMethod creation as an option for a custom frontend. Stripe stores the collected card details in its PCI-compliant vault (new raw lines 26-28; old raw lines 15-17).
- **Server request**: Pass the PaymentMethod ID to the ForwardingRequest endpoint from the server. The November curl and May Node examples use the demo URL, `pm_card_visa`, header authentication, a JSON body with card placeholders, and `card_number`, `card_expiry`, `card_cvc`, and `cardholder_name` replacements (new raw lines 30-46; old raw lines 19-43). The demo endpoint and sample bearer value are test fixtures, not production credentials or proof that an actual vault was reached.

## Token vault requirements

The in-house vault must be PCI compliant and provide a valid PCI Attestation of Compliance to Stripe support, refreshed annually. Its endpoint must use HTTPS, accept and return JSON rather than XML or ISO 8583, and use a single static URL configured for security rather than changing between requests (new raw lines 48-60; old raw lines 45-57).

Authentication uses HTTP header-based schemes, **including** bearer tokens; the guide does not restrict it to bearer alone. Each forwarded call needs the authentication header. Client certificate authentication is unsupported. Additional headers require explicit vault configuration and Stripe support verification, and should not contain sensitive data except the bearer token (new raw lines 62-72; old raw lines 59-69).

## Request body and CVC boundary

The illustrated body has a `card` object with `number`, `exp_month`, `exp_year`, `name`, and `cvc`, plus optional `metadata`; extra metadata passes through without processing. Stripe inserts decrypted values only for fields actually present in the request body. The displayed object includes a comment and is illustrative, not strict parseable JSON despite the November `json` fence (new raw lines 74-105; old raw lines 71-102).

The table describes a 15- or 16-digit PAN, two-digit expiration month, four-digit expiration year, and cardholder name. CVC is available only for the **first API request to Stripe after tokenization**. Stripe removes CVC from its system after a short period, and the vault or merchant must not store it (new raw lines 95-105; old raw lines 92-102). This is not a guarantee that CVC appears in a later ForwardingRequest or card-update forwarding call.

## Response and outcome boundary

The vault need not return a response body. If it does, Stripe returns it to the Forwarding API caller, and the vault should omit sensitive fields. The November diagram describes redaction of **identified** PCI-sensitive response data, without defining exhaustive detection or relaxing the vault's own no-sensitive-response instruction (new raw lines 17-24, 107-109).

> [!warning] Response-code wording
> Both captures say the Forwarding API returns the same response code as the vault, yet their concrete example says an upstream vault `400` produces Forwarding API HTTP `200` with the upstream `400` and error in the body (new raw lines 111-113; old raw lines 108-110). Preserve this tension rather than assuming a universal mapping. An API `200` alone cannot establish vault token creation or card-network payment success; inspect the contained vault outcome.

## Verification and card updates

The guide says to replace the demo endpoint with the configured in-house vault and initiate a ForwardingRequest with a created PaymentMethod to verify the integration. It states a 15-second request timeout. For updated card credentials, listen for relevant Stripe card-update webhooks and call the API again with the updated PaymentMethod; this is a merchant-triggered step, not automatic vault synchronization or a fresh CVC guarantee (new raw lines 115-123; old raw lines 112-120).

## Related Pages

- [[stripe-vault-and-forward]] — Vault and Forward concept and response boundary
- [[stripe]] — Stripe company page
- [[source-stripe-vault-and-forward]] — broader ForwardingRequest API reference
- [[source-stripe-forwarding-third-party]] — separate third-party processor flow

## Raw Sources

- [[raw/stripe-payments-forwarding-token-vault-2026-11-07|Own token vault guide, captured 2026-11-07]] — actor diagram, requirements, request and response boundaries
- [[raw/stripe-forwarding-token-vault-2026|Own token vault guide, captured 2026-05-11]] — prior full guide and Node example
