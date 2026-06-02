<!-- Repo: https://github.com/stripe/stripe-react-native -->
<!-- Commit SHA: f8ef10d7df0f98f051c92865c8b015dd653c6e44 -->
<!-- Date reviewed: 2026-05-13 -->
<!-- Detail directory: raw/github-stripe-react-native/ -->
<!-- Files saved (read directly from these paths):
  raw/github-stripe-react-native/README.md
  raw/github-stripe-react-native/MIGRATING.md
  raw/github-stripe-react-native/src/index.tsx
  raw/github-stripe-react-native/src/functions.ts
  raw/github-stripe-react-native/src/hooks/useStripe.tsx
  raw/github-stripe-react-native/src/hooks/usePaymentSheet.tsx
  raw/github-stripe-react-native/src/hooks/usePlatformPay.tsx
  raw/github-stripe-react-native/src/components/StripeProvider.tsx
  raw/github-stripe-react-native/src/components/CardField.tsx
  raw/github-stripe-react-native/src/types/PaymentSheet.ts
  raw/github-stripe-react-native/src/types/PaymentMethod.ts
  raw/github-stripe-react-native/src/types/PaymentIntent.ts
  raw/github-stripe-react-native/src/types/PlatformPay.ts
  raw/github-stripe-react-native/src/types/Errors.ts
-->
<!-- Deep-dive fallback: if a query needs files NOT listed above, re-clone from https://github.com/stripe/stripe-react-native at commit f8ef10d7df0f98f051c92865c8b015dd653c6e44, then save any newly discovered files into raw/github-stripe-react-native/ preserving their repo-relative paths -->

## What each file covers

| File | What to find there |
| ---- | ------------------ |
| `raw/github-stripe-react-native/README.md` | Installation (npm/yarn/Expo), platform requirements (Android API 23+, compileSdk 36, Kotlin 2.x), PaymentSheet supported payment methods, Apple Pay setup, recommended usage (not for in-app purchases) |
| `raw/github-stripe-react-native/MIGRATING.md` | Android SDK 36 requirement, legacy Apple/Google Pay API removal (v0.29.0), other breaking changes |
| `raw/github-stripe-react-native/src/index.tsx` | Full public API surface — all hook, component, function, and type exports |
| `raw/github-stripe-react-native/src/functions.ts` | Imperative payment functions: createPaymentMethod, confirmPayment, initPaymentSheet, presentPaymentSheet, confirmPlatformPay*, collectBankAccount*, verifyMicrodeposits*, createRadarSession, etc. |
| `raw/github-stripe-react-native/src/hooks/useStripe.tsx` | `useStripe()` hook — wraps all imperative functions as memoized callbacks |
| `raw/github-stripe-react-native/src/hooks/usePaymentSheet.tsx` | `usePaymentSheet()` hook — initPaymentSheet, presentPaymentSheet, confirmPaymentSheetPayment |
| `raw/github-stripe-react-native/src/hooks/usePlatformPay.tsx` | `usePlatformPay()` hook — Apple Pay / Google Pay: isPlatformPaySupported, confirmPlatformPayPayment, createPlatformPayPaymentMethod, updatePlatformPaySheet |
| `raw/github-stripe-react-native/src/components/StripeProvider.tsx` | `<StripeProvider>` component + `initStripe()` function — SDK initialization, publishable key, merchant ID, Expo partner attribution |
| `raw/github-stripe-react-native/src/components/CardField.tsx` | `<CardField>` component — card number/expiry/CVC inline input, props API |
| `raw/github-stripe-react-native/src/types/PaymentSheet.ts` | PaymentSheet.SetupParams, PresentOptions, appearance customization types |
| `raw/github-stripe-react-native/src/types/PaymentMethod.ts` | PaymentMethod.CreateParams, result types, CollectBankAccountTokenParams |
| `raw/github-stripe-react-native/src/types/PaymentIntent.ts` | PaymentIntent object shape, status enum, ConfirmOptions |
| `raw/github-stripe-react-native/src/types/PlatformPay.ts` | Apple Pay / Google Pay params (CartSummaryItem, PaymentMethodParams, GooglePay config) |
| `raw/github-stripe-react-native/src/types/Errors.ts` | StripeError shape, error codes enum |
