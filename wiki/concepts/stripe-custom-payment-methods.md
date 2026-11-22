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
| Checkout | November 7, 2026 product matrix lists supported |
| Payment Links | ✗ |
| Express Checkout Element | November 7, 2026 product matrix lists private preview |

The May 8, 2026 product matrix marked both Checkout and Express Checkout Element unsupported. The November product overview links an Express Checkout section, while the separate captured base implementation page lists Checkout Sessions and Payment Intents variants only. The product matrix leaves individual Checkout UI support, account enablement and API parity open. See [[source-stripe-custom-payment-methods]] and [[source-stripe-payment-element-custom-payment-methods]].

## Compliance

**Restricted methods**: crypto payment methods in Indonesia and Thailand are prohibited.

**Marks requirements**: must follow the PM provider's brand guidelines; cannot use one provider's Marks for another; cannot alter Marks without permission.

**Disclaimer highlights** (Stripe's formal position):

- Stripe is **not responsible** for CPM transaction processing (disputes, refunds, settlements, funds flows)
- Merchant is responsible for direct PSP integration, PSP agreement compliance, and correct CPM presentation
- Merchant must immediately remove CPMs if their PSP agreement terminates or Stripe prohibits the method

## Setup Flow

The April 21, 2026 Payment Intents Elements guide starts with a Stripe account and a completed deferred payments integration. See [[source-stripe-payment-element-custom-payment-methods#Payment Intents Elements Setup (April 21, 2026)]].

1. In Dashboard, create the CPM, upload its logo and obtain its `cpmt_` ID.
2. Add it to the `customPaymentMethods` option when initializing Elements.
3. In the deferred form, await `elements.submit()` and handle any submission error before routing by `selectedPaymentMethod`.
4. After external processing, optionally record the actual PSP activity using `paymentRecords.reportPayment(...)`.

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

### Express Checkout Embedded Button (Beta Type Surface)

`@stripe/stripe-js@9.14.0` adds an `expressCheckout` configuration for a `cpmt_` method. It requires `type: 'embedded'` and a render callback for the custom button; an optional destroy callback handles cleanup. Express Checkout availability events can use the custom method ID as a dynamic key.

> [!warning] Versioned availability
> The May 8 product matrix marked Express Checkout Element unsupported. The November 7 product matrix lists private preview and links an Express Checkout section outside the captured base page. The Stripe.js 9.14.0 beta declarations describe the typed configuration and require beta access. Hosted availability and merchant enablement need separate confirmation. See [[source-stripe-custom-payment-methods]] and [[source-github-stripe-js]].

## Routing in the Submit Handler

In the April 21, 2026 deferred Payment Intents Elements implementation, await `elements.submit()` and handle errors before branching on `selectedPaymentMethod`. A matching `cpmt_` routes to the merchant's PSP flow. Other selections follow the Stripe flow. The separate November Stripe.js reference scopes submission to Elements created without an Intent and requires awaiting the result before proceeding. Payment status comes from the PSP. See [[source-stripe-payment-element-custom-payment-methods#Submit Handler Pattern]] and [[raw/stripe-js-elements-submit-2026-11-07|Stripe.js Submit reference]].

## Recording to Stripe (Optional)

The April 2026 Payment Intents Elements, mobile and embedded mobile guides show optional server-side reporting for a payment handled by an external provider. Their examples use `2026-03-25.dahlia` with `invoice_partial_payments_beta=v3`. They create a `custom` PaymentMethod using a Dashboard `cpmt_` type ID, then report the actual processor outcome, timing and external reference with the new `pm_` instance ID. Use `guaranteed` only when the PSP result supports it. See [[source-stripe-payment-element-custom-payment-methods#Recording to Stripe (Optional)]], [[source-stripe-inapp-custom-payment-methods#Optional Server-Side Reporting]] and [[source-stripe-inapp-embedded-custom-payment-methods]].

The November [[raw/stripe-api-payment-record-report-2026-11-07|Report a payment API]] example uses `POST /v1/payment_records/report_payment` with `2026-10-28.endive` and inline `payment_method_details[custom][display_name]`. It supplies no PaymentMethod ID. Its initialized response shows `payment_method: null` and zero guaranteed amount. The separate terminal outcome reporting describes external activity. Payment completion depends on the external PSP’s result. The dated examples leave merchant access and cross-version or embedded SDK compatibility undetermined.

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

- **iOS PaymentSheet and FlowController**: The April 22, 2026 Swift examples use `async -> PaymentSheetResult` with completed, canceled or failed outcomes. The April PaymentSheet example shows the custom-method SPI import. The prose names `failure(error:)` and the examples use `.failed(error:)`. Swift EmbeddedPaymentElement uses `EmbeddedPaymentElementResult`.
- **Android PaymentSheet and FlowController**: The April guide uses `ConfirmCustomPaymentMethodCallback`. PaymentSheet prose names `onCustomPaymentMethodResult()`, while the Kotlin examples and FlowController prose use `handleCustomPaymentMethodResult()`. The Android FlowController guidance calls for a canceled result when exiting without confirming payment.
- **React Native**: `resultHandler` callback with `CustomPaymentMethodResultStatus`

See [[source-stripe-inapp-custom-payment-methods]] for PaymentSheet and FlowController. See [[source-stripe-inapp-embedded-custom-payment-methods]] for the separately documented EmbeddedPaymentElement handlers on iOS, Android and React Native.

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
- [[source-stripe-subscriptions-third-party]] — May 2026 Billing guide for custom payment methods and PaymentRecords with external processors; November 2026 base capture links two variants only
- [[source-github-stripe-js]] — `@stripe/stripe-js@9.14.0` embedded Payment Element and beta Express Checkout Custom Payment Method declarations
