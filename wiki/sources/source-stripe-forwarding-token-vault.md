---
title: "Stripe — Forward Card Details to Own Token Vault"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-forwarding-token-vault-2026.md"
tags: [stripe, vault-and-forward, token-vault, pci, own-vault, webhook]
---

## Summary

Guide for routing Stripe-stored cards to your own PCI-compliant token vault. Vault must meet specific API and compliance requirements.

## Token Vault Requirements

- **PCI**: valid Attestation of Compliance required (renew annually)
- **API**: HTTPS + JSON only (no XML/ISO 8583); single static URL; bearer token auth only (no client certificate)
- **Timeout**: 15 seconds

## Request Body Fields

| Field | Notes |
| --- | --- |
| `number` | PAN (15-16 digits) |
| `exp_month` | Two-digit |
| `exp_year` | Four-digit |
| `name` | Cardholder name |
| `cvc` | Available **first call only** — don't store |

## Test Endpoint

`https://forwarding-api-demo.stripedemos.com/tokens` + `pm_card_visa` for testing.

## Webhook Integration

Listen to card update webhooks → call Vault and Forward API to push updated credentials to your vault.

## Related Pages

- [[stripe-vault-and-forward]] — concept page
- [[source-stripe-vault-and-forward]] — ForwardingRequest API reference

## Raw Sources

- [[stripe-forwarding-token-vault-2026]] — verbatim token vault forwarding guide (120 lines)
