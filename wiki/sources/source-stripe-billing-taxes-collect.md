---
title: "Stripe Billing — Collect Taxes for Recurring Payments"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-billing-taxes-collect-2026.md"
tags: [stripe, billing, subscriptions, tax, stripe-tax, tax-rates, invoices, automatic-tax]
---

## Summary

Guide for collecting taxes on Stripe Billing subscriptions. Two approaches: Stripe Tax (automatic, paid) and Tax Rates (manual, free). Covers full Stripe Tax flow for subscriptions including Elements without Intent, address validation, webhook handling, and Credit Note refunds.

## Two approaches

| Approach | Cost | How it works |
|---|---|---|
| Stripe Tax | Paid (after first registration) | Automatic, integrates with prorations/discounts/trials |
| Tax Rates | Free | Manual fixed rates on subscriptions/invoices |

Third-party options: Avalara, Anrok, Sphere have native Stripe integrations.

## Stripe Tax — subscription flow

### 1. Estimate taxes (preview invoice)

```js
// Before address — use IP
stripe.invoices.createPreview({
  automatic_tax: { enabled: true },
  customer_details: { tax: { ip_address: '{{IP}}' } },
  subscription_details: { items: [{ price: priceId }] }
})
// After address — use full address
```

Check `automatic_tax.status` — if `requires_location_inputs`, address invalid.

### 2. Collect info via Elements (no Intent)

```js
stripe.elements({ mode: 'subscription', currency, amount: total })
// Mount AddressElement + PaymentElement
// Listen to address changes → re-estimate → elements.update({ amount: newTotal })
```

### 3. Submit form

`elements.submit()` → save customer details → create subscription → `stripe.confirmPayment()`

### 4. Update Customer (server)

```js
stripe.customers.update(id, {
  address: { ... },
  tax: { validate_location: 'immediately' }  // fails with customer_tax_location_invalid if bad
})
```

**US note**: rooftop-accurate addresses recommended (adjacent houses may have different tax rates).

### 5. Create subscription

```js
stripe.subscriptions.create({
  automatic_tax: { enabled: true },
  customer: customerId,
  items: [{ price: priceId }],
  payment_behavior: 'default_incomplete',
  payment_settings: { save_default_payment_method: 'on_subscription' },
  expand: ['latest_invoice.confirmation_secret']
})
```

### 6. Webhook: `invoice.finalization_failed`

If `automatic_tax.status=requires_location_inputs` → notify customer to update address → Stripe cannot finalize invoice or collect payment.

### 7. Refunds via Credit Notes

Stripe Tax auto-distributes refund between taxes and net amount. Create Credit Note with `refund_amount` (auto-refund) or `refunds: [{ refund: id }]` (manual). For line-item refunds: preview Credit Note first.

## Tax Rates — subscription flow

- **Item level**: up to 5 tax rates per subscription item (`tax_rates` on item)
- **Subscription level**: `default_tax_rates` — applies to items without item-level rates
- **Cascade**: item rates override subscription rates

Dynamic config: listen to `invoice.created` → edit draft invoice during ~1h window → assign tax rates.

### Checkout

- Fixed: `subscription_data.default_tax_rates` or `line_items.tax_rates`
- Dynamic: `line_items.dynamic_tax_rates` — matches to customer shipping > billing > country
- Cannot mix fixed and dynamic

## Related pages

- [[stripe-tax]] — concept page (updated)
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page
- [[source-metronome-integrations-tax-integrations-stripe-tax]] — Metronome-created Stripe invoice setup and mapping

## Raw Sources

- [[stripe-billing-taxes-collect-2026]] — verbatim Stripe docs webpage (569 lines)
