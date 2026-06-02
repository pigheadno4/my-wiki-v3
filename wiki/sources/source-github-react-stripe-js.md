---
title: "GitHub — stripe/react-stripe-js (Official React Stripe.js Library)"
type: source
date_ingested: 2026-05-08
original_format: github-repo
raw_files:
  - "github-react-stripe-js.md"
tags: [stripe, react, stripe-elements, elements-provider, hooks, usestripe, useelements, payment-element, embedded-checkout, checkout-sessions, typescript]
---

## Summary

Official React wrapper for Stripe.js (@stripe/react-stripe-js v6.3.0). Provides React components and hooks for both the Payment Intents API path and the Checkout Sessions API path.

## Two Integration Paths

### Payment Intents path (from `@stripe/react-stripe-js`)

```jsx
import {Elements, PaymentElement, useStripe, useElements} from '@stripe/react-stripe-js';

// Root provider
<Elements stripe={stripePromise} options={{clientSecret}}>
  <CheckoutForm />
</Elements>

// In checkout form
const stripe = useStripe();   // Stripe instance
const elements = useElements(); // Elements instance
await stripe.confirmPayment({ elements, confirmParams: { return_url } });
```

**All Element components**: PaymentElement, CardElement, CardNumberElement, CardExpiryElement, CardCvcElement, AddressElement, LinkAuthenticationElement, ExpressCheckoutElement, PaymentMethodMessagingElement, IbanElement, IdealBankElement, etc.

### Checkout Sessions path (from `@stripe/react-stripe-js/checkout`)

```jsx
import {CheckoutElementsProvider, PaymentElement, useCheckoutElements} from '@stripe/react-stripe-js/checkout';

<CheckoutElementsProvider stripe={stripePromise} options={{clientSecret: promise}}>
  <CheckoutForm />
</CheckoutElementsProvider>

// In form
const checkoutState = useCheckoutElements(); // { type: 'loading'|'error'|'success', checkout }
await checkoutState.checkout.confirm();
```

### Embedded Checkout path

```jsx
import {EmbeddedCheckoutProvider, EmbeddedCheckout} from '@stripe/react-stripe-js';

<EmbeddedCheckoutProvider stripe={stripePromise} options={{fetchClientSecret, onComplete}}>
  <EmbeddedCheckout />
</EmbeddedCheckoutProvider>
```

## Key Implementation Details

- `createElementComponent.tsx`: factory for all Element components — wraps underlying Stripe.js element with React lifecycle
- `Elements.tsx`: enforces `stripe` + `options` prop immutability; passes context down to all nested components
- `EmbeddedCheckoutProvider.tsx`: uses `fetchClientSecret` async fn (not direct clientSecret); `onComplete` callback
- `src/index.ts`: authoritative list of all public exports
- `src/types/index.ts`: complete TypeScript types for all props

## Saved Files

| File | Lines | What's there |
| --- | --- | --- |
| `README.md` | 242 | Install, overview, components list, hooks list |
| `src/index.ts` | 198 | All public exports |
| `src/types/index.ts` | 894 | All TypeScript types |
| `src/components/Elements.tsx` | 201 | Elements provider implementation |
| `src/components/createElementComponent.tsx` | 269 | Element component factory |
| `src/components/EmbeddedCheckoutProvider.tsx` | 242 | EmbeddedCheckoutProvider |
| `src/components/EmbeddedCheckout.tsx` | 67 | EmbeddedCheckout component |
| `src/checkout/index.ts` | 76 | Checkout path exports |
| `src/checkout/components/CheckoutElementsProvider.tsx` | 209 | CheckoutElementsProvider |
| `src/checkout/types/index.ts` | 112 | Checkout path types |
| `examples/hooks/9-Payment-Element.js` | 129 | Payment Element + confirmPayment example |
| `examples/hooks/11-Custom-Checkout.js` | 176 | CheckoutElementsProvider + useCheckoutElements example |

## Related Pages

- [[stripe-elements]] — Stripe Elements concept page (updated with React impl details)
- [[stripe-node-sdk]] — Stripe Node.js SDK (server-side counterpart)
- [[source-stripe-react-stripejs]] — React Stripe.js reference docs
- [[stripe]] — Stripe company page

## Raw Sources

- [[github-react-stripe-js]] — stub file pointing to `raw/github-react-stripe-js/` detail directory
