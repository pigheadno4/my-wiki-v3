---
title: "PayPal React Apple Pay: 10.3 to 10.4 Migration Guide"
type: analysis
date_created: 2026-08-30
tags: [paypal, apple-pay, react, javascript-sdk, typescript, migration, github-repository]
---

## Summary

`@paypal/react-paypal-js@10.4.0` adopts `@paypal/paypal-js@11.0.0` and Apple's community TypeScript definitions. This is primarily a compile-time ownership change: PayPal no longer declares a reduced `ApplePaySession` browser global. Merchant validation, PayPal order creation, Apple token confirmation, and server-side capture remain the same.

The migration applies to the package-qualified transition from React `10.3.0` to `10.4.0`. It does not establish merchant enablement, regional availability, or a new Apple Pay payment flow.

## What Changed

| Area | React 10.3 with core 10.1 | React 10.4 with core 11 |
| --- | --- | --- |
| Core dependency | `@paypal/paypal-js ^10.1.0` | `@paypal/paypal-js ^11.0.0` |
| Browser global typing | Reduced declaration shipped by PayPal | Native Apple global typed by `@types/applepayjs` |
| Availability access | `window.ApplePaySession` | Bare `ApplePaySession`, guarded with `typeof` |
| Payment request type | PayPal/custom shape passed directly | Cast to `ApplePayJS.ApplePayPaymentRequest` internally |
| Authorization event | PayPal-defined event shape | `ApplePayJS.ApplePayPaymentAuthorizedEvent` internally |
| Payment lifecycle | Validate, create, confirm, approve, capture | Unchanged |

Core 11 removes the old global declaration because it conflicted with `@types/applepayjs` and entered every `/sdk-v6` consumer's compilation, including projects that did not use Apple Pay.

## Package Upgrade

```bash
npm install @paypal/react-paypal-js@10.4.0 @paypal/paypal-js@11
npm install --save-dev @types/applepayjs
```

Install `@types/applepayjs` when merchant application code references `ApplePaySession` or `ApplePayJS.*`. React's own development dependency does not provide those declarations to consuming applications.

## Availability Check

### Before

```typescript
const isApplePayAvailable =
  typeof window !== "undefined" &&
  !!window.ApplePaySession?.canMakePayments();
```

### After

```typescript
const isApplePayAvailable =
  typeof window !== "undefined" &&
  typeof ApplePaySession !== "undefined" &&
  ApplePaySession.canMakePayments();
```

The `typeof ApplePaySession` guard prevents a reference error when the native global is absent. Do not rely on PayPal to augment the `Window` interface after upgrading to core 11.

> [!warning] Retained sample migration
> The retained v6 React sample uses `window.ApplePaySession` because it was collected with `@paypal/react-paypal-js@10.1.0`. Preserve its checkout lifecycle, but replace that capability check when migrating the sample to React 10.4 and core 11.

## Recommended React Integration

Configure `PayPalProvider` with the required v6 component and an explicit environment:

```tsx
import { PayPalProvider } from "@paypal/react-paypal-js/sdk-v6";

<PayPalProvider
  clientId={clientId}
  environment="sandbox"
  components={["applepay-payments"]}
  pageType="checkout"
>
  <ApplePayCheckout />
</PayPalProvider>;
```

Resolve both browser capability and PayPal transaction eligibility, then render the prebuilt button:

```tsx
import {
  ApplePayOneTimePaymentButton,
  useEligibleMethods,
} from "@paypal/react-paypal-js/sdk-v6";

function ApplePayCheckout() {
  const browserEligible =
    typeof window !== "undefined" &&
    window.location.protocol === "https:" &&
    typeof ApplePaySession !== "undefined" &&
    ApplePaySession.canMakePayments();

  const { eligiblePaymentMethods, error } = useEligibleMethods({
    payload: {
      currencyCode: "USD",
      paymentFlow: "ONE_TIME_PAYMENT",
    },
  });

  const applePayConfig = eligiblePaymentMethods?.isEligible("applepay")
    ? eligiblePaymentMethods.getDetails("applepay").config
    : null;

  if (!browserEligible || error || !applePayConfig) return null;

  return (
    <ApplePayOneTimePaymentButton
      applePayConfig={applePayConfig}
      applePaySessionVersion={4}
      paymentRequest={{
        countryCode: "US",
        currencyCode: "USD",
        requiredBillingContactFields: [
          "name",
          "phone",
          "email",
          "postalAddress",
        ],
        total: {
          label: "Example Store",
          amount: "20.00",
          type: "final",
        },
      }}
      buttonstyle="black"
      type="buy"
      locale="en"
      createOrder={async () => {
        const response = await fetch("/api/orders", { method: "POST" });
        if (!response.ok) throw new Error("Order creation failed");
        const order = await response.json();
        return { orderId: order.id };
      }}
      onApprove={async (data) => {
        const orderId = data.approveApplePayPayment.id;
        const response = await fetch(`/api/orders/${orderId}/capture`, {
          method: "POST",
        });
        if (!response.ok) throw new Error("Order capture failed");
      }}
      onCancel={() => console.log("Apple Pay cancelled")}
      onError={(paymentError) => console.error(paymentError)}
    />
  );
}
```

The amount and currency in `paymentRequest` must match the server-created PayPal order. Order creation and capture remain merchant-server responsibilities.

## Internal Type Difference

React 10.3 modeled the authorization event with PayPal-owned types:

```typescript
applePaySession.onpaymentauthorized = async (event: {
  payment: {
    token: ApplePayPaymentToken;
    billingContact: ApplePayContact;
    shippingContact?: ApplePayContact;
  };
}) => {
  // confirm the PayPal order
};
```

React 10.4 uses Apple's community event type and explicitly bridges its optional billing-contact declaration to PayPal's required confirmation input:

```typescript
applePaySession.onpaymentauthorized = async (
  event: ApplePayJS.ApplePayPaymentAuthorizedEvent,
) => {
  await paypalSession.confirmOrder({
    orderId,
    token: event.payment.token,
    billingContact: event.payment.billingContact as ApplePayContact,
    shippingContact: event.payment.shippingContact,
  });
};
```

React also creates the native session with:

```typescript
new ApplePaySession(
  applePaySessionVersion,
  paymentRequest as ApplePayJS.ApplePayPaymentRequest,
);
```

These casts are internal to the wrapper. Merchants using `ApplePayOneTimePaymentButton` do not need to reproduce them.

## Unchanged Checkout Lifecycle

1. Load the PayPal v6 `applepay-payments` component and the Apple Pay browser SDK.
2. Confirm HTTPS and `ApplePaySession.canMakePayments()`.
3. Call `useEligibleMethods()` and require `isEligible("applepay")`.
4. Start `ApplePaySession` from a buyer click.
5. Complete merchant validation through PayPal.
6. Create the PayPal order on the merchant server.
7. Confirm it with Apple's token and contact data.
8. Complete the Apple Pay sheet and capture on the merchant server.

Domain registration, PayPal account enablement, production onboarding, and Apple Pay availability remain separate prerequisites. Package type support does not prove any of them.

## Migration Checklist

- Upgrade React 10.3 to 10.4 together with core 11.
- Add `@types/applepayjs` when application code references Apple's globals or namespace.
- Replace `window.ApplePaySession` checks with the guarded native global.
- Remove any local workaround that duplicates PayPal's former reduced declaration.
- Keep `applepay-payments`, explicit `environment`, HTTPS, and eligibility checks.
- Preserve server-side order creation and capture.
- Verify that the Apple request amount and PayPal order amount match.
- Test unsupported browsers, cancellation, merchant-validation failure, confirmation failure, and capture failure.

## Sources

- [[source-github-paypal-js]] — package-qualified core 11 and React 10.4 implementation evidence
- [[changelog-github-paypal-js]] — shared-SHA release history and migration boundaries
- [[source-github-v6-web-sdk-sample-integration]] — retained provider, eligibility, button, order, and capture example
- [[source-paypal-apm-apple-pay]] — domain validation, onboarding, and one-time integration requirements
- [[paypal-apple-pay]] — consolidated PayPal Apple Pay constraints and lifecycle
