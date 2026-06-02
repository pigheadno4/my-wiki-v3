---
title: "Add Custom Payment Methods to the Payment Element"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-payment-element-custom-payment-methods-2025.md"
tags: [stripe, payment-element, custom-payment-methods, cpmt, third-party, payment-records, reporting, xss]
---

## Summary

Integration guide for surfacing third-party payment methods (custom payment methods / CPM) inside the Stripe Payment Element. Transactions are processed outside Stripe but can be recorded to Stripe for unified reporting. The Checkout Sessions API path only offers a stub — the full integration is Payment Intents API only.

## Key Takeaways

- **`cpmt_` IDs**: created in Dashboard → Settings > Payments > Custom Payment Methods
- **Two display types**: `static` (button only) and `embedded` (Preview — renders custom HTML inside the Payment Element)
- **`elements.submit()`**: returns `selectedPaymentMethod`; branch on `cpmt_` ID to route to custom vs Stripe flow
- **Ordering**: CPMs appear last by default; override with `paymentMethodOrder`
- **Recording**: optional — use `paymentMethods.create({ type: 'custom' })` + `paymentRecords.reportPayment(...)` for unified reporting
- **XSS warning**: embedded type — only render trusted content in the container
- **Legal**: merchant responsible for PSP agreement compliance and applicable laws

## Setup Flow

1. **Dashboard**: Settings > Payments > Custom Payment Methods → create CPM, get `cpmt_` ID
2. **Client**: add to `customPaymentMethods` array in `stripe.elements({...})` options
3. **Submit handler**: call `elements.submit()`, check `selectedPaymentMethod`, branch to CPM flow or Stripe flow
4. **Server (optional)**: call `paymentRecords.reportPayment(...)` to record to Stripe

## Display Types

### Static

```js
customPaymentMethods: [{
  id: 'cpmt_....',
  options: { type: 'static', subtitle: 'Optional subtitle' }
}]
```

![Static CPM in Payment Element](../raw/assets/stripe-payment-element-custom-pm-static.png)

Customer selects → merchant routes to their own payment flow or redirect.

### Embedded (Preview)

```js
customPaymentMethods: [{
  id: 'cpmt_....',
  options: {
    type: 'embedded',
    embedded: {
      handleRender: (container) => { /* render into container */ },
      handleDestroy: () => { /* cleanup */ }
    }
  }
}]
```

![Embedded CPM with custom content](../raw/assets/stripe-payment-element-custom-pm-embedded.png)

Use React Portals to integrate `handleRender` container with React state.

## Submit Handler Pattern

```js
const { submitError, selectedPaymentMethod } = await elements.submit();
if (selectedPaymentMethod === 'cpmt_....') {
  // Route to custom payment flow
  const res = await fetch('/process-cpm-payment', { method: 'post' });
} else {
  // Standard Stripe payment flow
}
```

## Recording to Stripe (Optional)

```js
// Create custom PaymentMethod object
const pm = await stripe.paymentMethods.create({ type: 'custom', custom: { type: 'cpmt_....' } });

// Report the payment
await stripe.paymentRecords.reportPayment({
  amount_requested: { value: amount, currency },
  payment_method_details: { payment_method: pm.id },
  processor_details: { type: 'custom', custom: { payment_reference: externalId } },
  outcome: 'guaranteed',
  ...
});
```

Requires beta API version: `2026-03-25.dahlia; invoice_partial_payments_beta=v3`.

## Logo Guidelines

- Transparent background logos: ensure contrast with Payment Element background
- Background fill logos: include rounded corners in file if needed
- Choose variant that scales to 16×16px (typically the standalone mark)

## Related Pages

- [[stripe-custom-payment-methods]] — concept page
- [[stripe-payment-element]] — parent element
- [[stripe-payment-intents]] — required API path for CPM integration
- [[stripe]] — company page

## Raw Sources

- [[stripe-payment-element-custom-payment-methods-2025]] — verbatim integration guide
