---
title: "Stripe Docs — Link in different payment integrations"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-link-payment-integrations-2025.md"
tags: [stripe, link, payment-method-types, card-integration, ic-plus, backup-payment, instant-bank-payments]
---

## Summary

Reference for the two Link integration paths — Link as a payment method vs Link within card integrations. Covers PM type differences, IC+ pricing incompatibility, backup payment source, and fixed API values for non-card Link payments.

## Two Integration Paths

| Path | `payment_method_types` | PM type | When to use |
| --- | --- | --- | --- |
| **Link as PM** (recommended) | `['link']` or dynamic | `link` | Default; dynamic PMs; no IC+ pricing |
| **Link in card integration** | `['card']` only | `card` + wallet=`link` | Need card brand/last 4; IC+ pricing |

## Critical Rules

- **Passing `link` ALWAYS triggers PM path** — even alongside `card`. If you want card integration, pass `card` only.
- **IC+ pricing**: Link as PM uses blended rate; card integration required for IC+ customers.
- **Backup payment source**: only in PM path — if primary fails, Link auto-retries with backup; NOT available in card integration.

## Non-Card Link PMs in Card Integration (e.g., Instant Bank Payments)

Fixed API values (not real card data):

| Field | Fixed Value |
| --- | --- |
| `type` | `card` |
| `brand` | `link` |
| `last4` | `0000` |
| `exp_month/year` | `12/2040` |
| `funding` | `unknown` |
| `display_brand` | `other` |
| `networks.available` | `["link"]` |
| All `checks` | `null` |

Stripe recommends identifying these as "Link" in customer UI rather than rendering the fixed values.

## Related Pages

- [[stripe-link]] — Link concept page (Integration Paths section updated)
- [[stripe-instant-bank-payments]] — Instant Bank Payments (a non-card Link funding method)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-link-payment-integrations-2025]] — verbatim webpage content (87 lines)
