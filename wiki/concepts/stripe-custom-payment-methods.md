---
title: "Stripe Custom Payment Methods"
type: concept
category: technology
tags: [stripe, payment-element, custom-payment-methods, cpmt, third-party, payment-records, reporting]
---

## Definition

Stripe Custom Payment Methods (CPM) allow merchants to surface third-party payment processors inside the Stripe Payment Element. Transactions are processed entirely outside Stripe, but appear alongside Stripe's 50+ built-in payment methods in a unified UI. Merchants can optionally record CPM transactions to Stripe for unified reporting.

## Key Concepts

- **`cpmt_` IDs**: each CPM has a unique ID starting with `cpmt_`, created in the Stripe Dashboard
- **PM type in API**: `type: 'custom'`, with `custom[type]` = the `cpmt_...` ID
- **Type IDs not API-retrievable**: store the `cpmt_` ID in your own database; retrieve it at payment method creation time
- **Processing**: completely outside Stripe — merchant handles the actual transaction with their third-party PSP
- **Recording**: optional — transactions can be reported to Stripe via the Payment Records API
- **50+ presets**: available for common external PMs; or set a custom display name + logo

## Integration Support

| Integration | Supported |
| --- | --- |
| Connect | ✓ |
| Payment Element | ✓ |
| Mobile Payment Element | ✓ |
| Subscriptions | ✓ |
| Invoicing | ✓ |
| Customer Portal | ✓ |
| Checkout | ✗ |
| Payment Links | ✗ |
| Express Checkout Element | ✗ |

## Compliance

**Restricted methods**: crypto payment methods in Indonesia and Thailand are prohibited.

**Marks requirements**: must follow the PM provider's brand guidelines; cannot use one provider's Marks for another; cannot alter Marks without permission.

**Disclaimer highlights** (Stripe's formal position):

- Stripe is **not responsible** for CPM transaction processing (disputes, refunds, settlements, funds flows)
- Merchant is responsible for direct PSP integration, PSP agreement compliance, and correct CPM presentation
- Merchant must immediately remove CPMs if their PSP agreement terminates or Stripe prohibits the method

## Setup Flow

1. **Dashboard**: Settings > Payments > Custom Payment Methods → create CPM, get `cpmt_` ID + upload logo
2. **Client**: add to `customPaymentMethods` array in `stripe.elements({...})` init options
3. **Submit handler**: call `elements.submit()`, branch on `selectedPaymentMethod` to route CPM vs Stripe flow
4. **Server (optional)**: record transaction via `paymentRecords.reportPayment(...)`

## Display Types

### Static

Button-only — clicking routes customer to merchant's own payment flow or redirect.

```js
{ id: 'cpmt_....', options: { type: 'static', subtitle: 'Optional subtitle' } }
```

![Static CPM in Payment Element](../raw/assets/stripe-payment-element-custom-pm-static.png)

### Embedded (Preview)

Renders merchant's custom HTML/UI inside the Payment Element container.

```js
{ id: 'cpmt_....', options: { type: 'embedded', embedded: {
  handleRender: (container) => { /* render into DOM node */ },
  handleDestroy: () => { /* cleanup: remove SDKs, event listeners */ }
}}}
```

![Embedded CPM with custom content](../raw/assets/stripe-payment-element-custom-pm-embedded.png)

> **XSS warning**: only render trusted content in the embedded container. User-supplied or unsanitized markup creates a cross-site scripting vulnerability.

## Routing in the Submit Handler

```js
const { submitError, selectedPaymentMethod } = await elements.submit();
if (selectedPaymentMethod === 'cpmt_....') {
  // Route to third-party payment processor
} else {
  // Standard Stripe confirmPayment flow
}
```

## Recording to Stripe (Optional)

Requires beta API version. Creates a `PaymentMethod` object of type `custom`, then calls `paymentRecords.reportPayment(...)` with amount, currency, processor reference, outcome, and timing.

Enables unified reporting and back-office workflows (receipts, reports) even for off-Stripe transactions.

## Ordering

CPMs appear last in the Payment Element by default. Override with `paymentMethodOrder` on the Payment Element options.

## Logo Guidelines

- Transparent background: ensure contrast against the Payment Element background
- Background fill: include rounded corners in the file if needed
- Must scale cleanly to 16×16px (use standalone logo mark)

## Legal

Merchant is responsible for compliance with their PSP agreement and applicable laws when integrating a third-party payment processor through CPM.

## Mobile Integration (iOS/Android/React Native)

Same `cpmt_` IDs from Dashboard. Platform-specific handler patterns:

- **iOS**: `async -> PaymentSheetResult` (`.completed`/`.canceled`/`.failed`); beta import required
- **Android**: `ConfirmCustomPaymentMethodCallback`; call `CustomPaymentMethodResultHandler.handleCustomPaymentMethodResult()` even on cancel (FlowController)
- **React Native**: `resultHandler` callback with `CustomPaymentMethodResultStatus`

See [[source-stripe-inapp-custom-payment-methods]] for full mobile integration.

## Notable Use Case: PayPal as CPM

Stripe offers a **low-code PayPal CPM adapter** for adding PayPal to Checkout Sessions and hosted Checkout integrations. The adapter is hosted in the merchant's environment and integrates natively with Checkout.

Decision rule:

- PayPal exclusively in supported European countries → use the **standard PayPal payment method**
- Global or non-EU PayPal → use the **PayPal CPM adapter**

## Key Players

- [[stripe]] — provides the Payment Element and optional recording infrastructure

## Sources

- [[source-stripe-payment-element-custom-payment-methods]] — primary reference: setup flow, display types, submit handler, recording pattern, XSS warning
- [[source-stripe-custom-payment-methods]] — overview: PM API type, integration matrix, marks compliance, Indonesia/Thailand restriction, Stripe disclaimer
- [[source-stripe-paypal-custom-payment-method]] — PayPal as CPM: low-code adapter for Checkout, decision rule (EU→standard PM vs global→CPM adapter)
- [[source-stripe-subscriptions-third-party]] — billing with 3rd party processors: custom PM types, payment records API, webhook handler, retry logic, refunds, out-of-band legacy
