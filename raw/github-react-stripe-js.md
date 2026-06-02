<!-- Repo: https://github.com/stripe/react-stripe-js -->
<!-- Commit SHA: 58e7e27bfc6560db3636791496958e5c6ccda9ee -->
<!-- Date reviewed: 2026-05-08 -->
<!-- Detail directory: raw/github-react-stripe-js/ -->
<!-- Files saved (read directly from these paths):
  raw/github-react-stripe-js/README.md
  raw/github-react-stripe-js/src/index.ts
  raw/github-react-stripe-js/src/types/index.ts
  raw/github-react-stripe-js/src/components/Elements.tsx
  raw/github-react-stripe-js/src/components/createElementComponent.tsx
  raw/github-react-stripe-js/src/components/EmbeddedCheckoutProvider.tsx
  raw/github-react-stripe-js/src/components/EmbeddedCheckout.tsx
  raw/github-react-stripe-js/src/checkout/index.ts
  raw/github-react-stripe-js/src/checkout/components/CheckoutElementsProvider.tsx
  raw/github-react-stripe-js/src/checkout/types/index.ts
  raw/github-react-stripe-js/examples/hooks/9-Payment-Element.js
  raw/github-react-stripe-js/examples/hooks/11-Custom-Checkout.js
-->
<!-- Deep-dive fallback: if a query needs files NOT listed above, re-clone from https://github.com/stripe/react-stripe-js at commit SHA 58e7e27bfc6560db3636791496958e5c6ccda9ee, then save any newly discovered files into raw/github-react-stripe-js/ preserving their repo-relative paths -->

# react-stripe-js — Official React Stripe.js Library

Package: @stripe/react-stripe-js v6.3.0

## What each file covers

| File | What to find there |
| ---- | ------------------ |
| `raw/github-react-stripe-js/README.md` | Installation, quick usage example, Element components list, hooks list, TypeScript usage |
| `raw/github-react-stripe-js/src/index.ts` | All public exports: Elements, useStripe, useElements, ElementsConsumer, all Element components, EmbeddedCheckout* |
| `raw/github-react-stripe-js/src/types/index.ts` | TypeScript types: ElementProps, StripeElementProps, ElementsContextValue, all element option types, hook return types |
| `raw/github-react-stripe-js/src/components/Elements.tsx` | `<Elements>` provider implementation: context setup, stripe/options prop handling, element mounting, immutability enforcement |
| `raw/github-react-stripe-js/src/components/createElementComponent.tsx` | Factory function that creates all Element components (PaymentElement, CardElement, etc.); `useElementsContextWithUseCase` hook |
| `raw/github-react-stripe-js/src/components/EmbeddedCheckoutProvider.tsx` | `<EmbeddedCheckoutProvider>` for embedded Stripe Checkout; `fetchClientSecret` pattern; `onComplete` callback |
| `raw/github-react-stripe-js/src/components/EmbeddedCheckout.tsx` | `<EmbeddedCheckout>` component that mounts the Stripe-hosted embedded checkout UI |
| `raw/github-react-stripe-js/src/checkout/index.ts` | Checkout Sessions path exports: CheckoutElementsProvider, all checkout-specific Element components, useCheckoutElements hook |
| `raw/github-react-stripe-js/src/checkout/components/CheckoutElementsProvider.tsx` | `<CheckoutElementsProvider>` implementation: clientSecret from Checkout Session, checkout state management |
| `raw/github-react-stripe-js/src/checkout/types/index.ts` | Types for Checkout path: CheckoutContextValue, checkout state types |
| `raw/github-react-stripe-js/examples/hooks/9-Payment-Element.js` | Payment Element example with useStripe + useElements hooks; stripe.confirmPayment flow |
| `raw/github-react-stripe-js/examples/hooks/11-Custom-Checkout.js` | Custom Checkout (Checkout Sessions + CheckoutElementsProvider) example; useCheckoutElements usage |
