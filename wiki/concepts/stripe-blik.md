---
title: "BLIK (Stripe)"
type: concept
category: technology
tags: [stripe, blik, poland, pln, bank-debit, authenticated, disputes]
---

## Definition

BLIK is Poland's dominant online payment method. Customers generate a 6-digit code from their banking app and enter it at checkout — no redirect needed. API enum: `blik`. Customer-initiated (customer authenticates each payment), immediate notification.

**Currency**: PLN only. **Customers**: Poland only. **Business**: 37 countries.

## Payment Flow

1. Customer selects BLIK at checkout
2. Opens banking app → generates 6-digit code (valid 2 minutes)
3. Enters code in checkout form
4. Bank sends push notification to customer's phone
5. Customer approves in banking app (60-second window, typically <10 seconds)
6. Immediate payment confirmation

**No redirect** — BLIK is unique among bank redirects in that it doesn't require leaving the checkout page.

## Key Properties

- **Confirmation**: Customer-initiated, immediate notification
- **Recurring**: Private preview
- **Deferred intent**: Client-side confirmation only (private preview)
- **ECE + Mobile Payment Element**: Not supported
- **Refunds**: Full and partial; immediate or within hours depending on bank

## Disputes

- Customers can dispute for fraud, double payment, or order/amount mismatch
- Stripe notifies via email, Dashboard, `charge.dispute.created` webhook
- Must submit evidence within **12 calendar days**
- BLIK adjudicates: merchant win → funds returned; customer win → charge becomes permanent

## Connect

- `blik_payments` capability required on platform and connected accounts
- Descriptor source: Direct/`on_behalf_of` → connected account; Destination/separate charge → platform

## Integration

**Checkout**: `payment_method_types: ['blik']`, `pln`, payment mode only. Refund/dispute window: 13 months.

**Direct API**: `stripe.confirmBlikPayment()` — **synchronous** (no redirect). Code passed in `payment_method_options.blik.code`. After confirm: `requires_action` + `blik_authorize` next_action → customer has 60s in banking app.

**Sandbox failure simulation**: 10 email patterns covering immediate failures, declines (8s delay), and timeouts (60s delay).

## Sources

- [[source-stripe-blik]] — primary source: payment flow, disputes, refunds, Connect
- [[source-stripe-blik-accept-payment]] — integration guide: Checkout + Direct API + iOS + Android, synchronous confirmBlikPayment, 10 failure patterns
- [[source-stripe-blik-save-during-payment]] — save for recurring: setup_future_usage, max 2000 PLN, not all banks supported, 6 additional test patterns
- [[source-stripe-blik-set-up-payment]] — SetupIntent (no payment): mandate-only authorization, confirmSetup/Direct API, same constraints and test patterns
