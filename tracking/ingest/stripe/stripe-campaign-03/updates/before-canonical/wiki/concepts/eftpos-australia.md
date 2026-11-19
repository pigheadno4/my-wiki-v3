---
title: "eftpos Australia"
type: concept
category: standard
tags: [eftpos, australia, local-card-network, co-branded, debit, aud, least-cost-routing]
---

## Definition

eftpos is Australia's local debit card network. More than 90% of eftpos cards are co-branded with Visa or Mastercard. Stripe processes them per Australia's least cost routing (LCR) requirements.

**Currency**: AUD only. **Country**: AU only. **Card type**: debit and prepaid.

## Key Properties

- **No manual capture**: hold/delayed capture always routes to Visa/MC (international scheme)
- **Default routing**: eftpos is the default for non-hold payments; Stripe may route to Visa/MC for technical/authorization rate reasons
- **eftpos-only cards** ("proprietary eftpos cards"): in-person only — cannot be used online
- Detect network: `charge.payment_method_details.card.network` → `"eftpos_au"`

## Excluded MCCs

Not available for: massage parlors (7297), financial institution cash disbursements (6010), financial institution merchandise/services (6012), foreign currency/money orders (6051), remote stored value load (6530), stored value card purchase (6540), wires/money orders (4829).

## Disclosure Requirement

Merchants must notify customers that dual-network debit payments may be routed through the debit (eftpos) network regardless of the card logo displayed:
- Single payment: notify before checkout completion
- New recurring: notify at setup time
- Existing recurring: notify in advance of future transactions

## Integration

No additional code changes needed if already accepting card payments. Contact Stripe support to opt out of eftpos as the default network.

## Product Support

Connect, Checkout, Payment Links, Subscriptions, Invoicing, Elements (not Express Checkout), Terminal (AU-specific regional requirements).

## Sources

- [[source-stripe-eftpos-australia]] — primary source: properties, routing logic, MCCs, disclosure requirements
