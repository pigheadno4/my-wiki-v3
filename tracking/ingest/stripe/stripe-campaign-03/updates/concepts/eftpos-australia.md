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

- **General co-branded card routing**: eftpos does not support manual capture. A payment requiring a hold between authorization and capture routes to Visa or Mastercard; other payments generally default to eftpos, subject to transaction type, technical availability and authorization-rate considerations.
- **Apple Pay eftpos exception (2026-11-07)**: When a customer chooses eftpos on a co-branded card in Apple Pay, the eftpos token cannot fall back to Visa or Mastercard; an eftpos Apple Pay payment with manual capture always fails. Use automatic or automatic_async capture for this path. If manual capture is needed for other cards, configure the Payment Element before render to hide eftpos Apple Pay; setting card manual capture afterward can leave an option that fails at confirmation. This does not change the general co-branded hold-routing rule.
- **eftpos-only cards** ("proprietary eftpos cards"): in-person only — cannot be used online
- Detect the processed network on a successful PaymentIntent's Charge: `charge.payment_method_details.card.network` → `"eftpos_au"`.
- The 2026-11-07 Stripe cards table adds eftpos **Apple Pay** wallet support in AUD without manual capture, after the 2026-05-01 table marked eftpos wallets unsupported. This scoped wallet capability is not all-wallet or manual-capture support; see [[source-stripe-cards]] and [[source-stripe-eftpos-australia]].

## Excluded MCCs

Not available for: massage parlors (7297), financial institution cash disbursements (6010), financial institution merchandise/services (6012), foreign currency/money orders (6051), remote stored value load (6530), stored value card purchase (6540), wires/money orders (4829).

## Disclosure Requirement

Merchants must notify customers that dual-network debit payments may be routed through the debit (eftpos) network regardless of the card logo displayed:
- Single payment: notify before checkout completion
- New recurring: notify at setup time
- Existing recurring: notify in advance of future transactions

## Integration

For the general card acceptance route, the guide says an integration already accepting cards can accept eftpos without additional updates; contact Stripe support if eftpos must never be the default network. The separate Apple Pay eftpos route requires an Australian Stripe account, AUD, an allowed business category and Apple Pay enabled in payment-method settings. For an existing iOS Apple Pay integration, its Swift example enables `.eftpos` only for AUD. A successful PaymentIntent's Charge identifies an Apple Pay eftpos result through `card.network: 'eftpos_au'` and `card.wallet.type: 'apple_pay'`; the customer selection or SDK setting alone is not a payment outcome.

## Product Support

Connect, Checkout, Payment Links, Subscriptions, Invoicing, Elements (not Express Checkout), Terminal (AU-specific regional requirements).

## Sources

- [[source-stripe-eftpos-australia]] — 2026-05 and 2026-11 Stripe guides: general eftpos routing and disclosure, plus the later Apple Pay no-fallback and capture conditions
