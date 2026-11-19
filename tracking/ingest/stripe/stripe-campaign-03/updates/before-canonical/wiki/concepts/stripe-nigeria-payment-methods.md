---
title: "Nigerian Payment Methods (Stripe)"
type: concept
category: technology
tags: [stripe, nigeria, naira, local-payment-methods, merchant-of-record, wallets, bank-transfer]
---

## Definition

Stripe enables acceptance of Nigerian local payment methods (Naira cards, bank transfers, and wallets) without a local Nigerian entity, via a **merchant of record** model through a Nigerian partner. See [[stripe-managed-payments]] for the broader MoR framework.

## How It Works

Customers begin checkout on Stripe's page, then are redirected to the Nigerian partner's localized checkout and their local processor. Payment happens there — Stripe acts as the conduit to the MoR partner.

- **No local entity required**: US-based Stripe accounts can accept NGN payments with USD settlement
- **3-day funding** after payment approval
- **VAT**: The MoR partner remits buyer VAT for Nigerian transactions — merchants should include VAT in presentment pricing

## Payment Methods

| Method | One-time | Recurring |
| --- | --- | --- |
| Naira cards | Yes | Yes |
| Naira bank transfer | Yes | Coming soon |
| Naira wallet | Coming soon | No |

## Key Properties

- **Currency**: NGN only
- **Business locations**: US only (USD settlement)
- **Recurring**: Yes (Naira cards)
- **Manual capture**: Yes
- **Connect**: Yes
- **Disputes**: Cannot challenge — funds removed immediately when PSP accepts dispute; merchant must contact customer directly
- **Refunds**: Full + partial, 365-day window; up to 7 calendar days to return status for some transactions

## Integration

Dashboard-driven: enable Naira payment methods in Stripe Dashboard → auto-surfaced in Checkout/Elements/Payment Links. Also available via Payment Intents API.

### Naira Card (`ng_card`)

- **Amount limits**: 500–100,000,000 NGN
- **Modes**: payment + setup + subscription (supports recurring, unlike bank transfer)
- **Checkout**: add `ng_card` to `payment_method_types`; all line items in `ngn`
- **Direct API**: create PaymentIntent with `ng_card` **and** `payment_method_data: { type: 'ng_card' }` at creation; then `stripe.confirmPayment()` with same `payment_method_data.type` + `return_url`
- **Redirect params on return**: `payment_intent` + `payment_intent_client_secret`
- **Testing**: success → `requires_action` → `succeeded`; fail → "Fail test payment" → `requires_payment_method`
- **Post-payment**: `payment_intent.succeeded` webhook

### Naira Card — Save / Recurring (`ng_card`)

**Two save paths**:

- **SetupIntent**: `setupIntents.create({ payment_method_types: ['ng_card'], usage: 'off_session'|'on_session', customer })` → `stripe.confirmNgCardSetup()` with `return_url` + `mandate_data: { customer_acceptance: { type: 'online', online: { infer_from_client: true } } }`
- **PaymentIntent with `setup_future_usage`**: `paymentIntents.create({ ..., setup_future_usage: 'off_session', confirm: true, return_url, mandate_data })` — mandate_data requires explicit `ip_address` + `user_agent`

**Using a saved PM**: new PaymentIntent with `payment_method: '{{ID}}'` + `off_session: true` + `confirm: true`

**Checkout path**: `mode: 'setup'`, `ng_card` in `payment_method_types`; customer authenticates on redirect page → `requires_action` → `succeeded`

**Manual redirect option**: server-side — create with `confirm: true`, check `next_action.type === 'redirect_to_url'`, redirect to `next_action.redirect_to_url.url`

**Detach**: fires `mandate.updated` + `payment_method.detached`; mandate collection (written agreement) required before saving

### Naira Bank Transfer (`ng_bank_transfer`)

- **Amount limits**: 500–100,000,000 NGN
- **Checkout**: add `ng_bank_transfer` to `payment_method_types`; all line items in `ngn`; no setup/subscription mode
- **Direct API**: create PaymentIntent with `ng_bank_transfer` **and** `payment_method_data: { type: 'ng_bank_transfer' }` at creation; then client-side `stripe.confirmPayment()` with same `payment_method_data.type` + `return_url`
- **Redirect params on return**: `payment_intent` + `payment_intent_client_secret`
- **Testing**: success → `requires_action` → `succeeded`; fail → click "Fail test payment" → `requires_payment_method`
- **Post-payment**: `payment_intent.succeeded` webhook

## Sources

- [[source-stripe-local-payment-methods-by-country]] — hub page: Nigeria + South Korea local payment methods
- [[source-stripe-nigeria-payment-methods]] — Nigeria overview: MoR model, Naira cards/bank transfer/wallet, VAT, disputes, refunds
- [[source-stripe-ng-bank-transfer-accept-payment]] — Naira bank transfer integration: ng_bank_transfer, 500–100M NGN limits, confirmPayment(), redirect flow, test modes
- [[source-stripe-ng-card-accept-payment]] — Naira card integration: ng_card, setup+subscription mode, 500–100M NGN limits, confirmPayment(), same redirect flow
- [[source-stripe-ng-card-set-up-future-payments]] — Naira card save/recurring: SetupIntent + confirmNgCardSetup(), PaymentIntent setup_future_usage, off_session reuse, detach events
