---
title: "Stripe: Accept an EPS Payment"
type: source
date_ingested: 2026-05-03
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/eps/accept-a-payment"
raw_files:
  - "stripe-eps-accept-payment-2025.md"
tags: [stripe, eps, austria, eur, checkout, ios, android, react-native, elements, bank-redirect]
---

## Overview

[[stripe]] acceptance guide for EPS, an Austrian bank-redirect method. The detailed 2026-05-03 capture covers Checkout, iOS, Android, React Native, and a legacy Elements integration. The 2026-11-07 base-URL capture is a five-variant index only; it does not verify the current content, SDK support, eligibility, or outcomes of the linked variants. See [[stripe-eps]].

## Key takeaways — 2026-05-03 detailed capture

- **Payment identity:** The old guide describes EPS as single-use, with customer bank authentication via redirect and a return to the merchant site. It says EPS use must accord with the EPS Terms of Service. An EPS PaymentMethod cannot be saved to a Customer or reused for another payment (lines 26-28, 1542-1544).
- **Checkout conditions:** The captured compatibility list names Europe, US, CA, NZ, SG, HK, JP, AU, and MX as supported business locations; EUR for supported and presentment currency; payment mode yes; setup and subscription modes no. A Checkout Session needs same-currency, one-time line items, and the manual example uses EUR and adds eps to payment_method_types. Hosted Checkout uses success_url, while the embedded example uses return_url. These are dated guide claims, not a current account eligibility check (lines 30-47, 55-112).
- **Name collection is path-specific:** The iOS, Android, and React Native custom-form sections collect the customer's full name for billing details. The legacy Elements form collects an account holder name. The hosted Checkout section does not instruct the merchant to add a manual name input (lines 49-121, 267-306, 472-480, 678-720, 979-1003, 1129-1156).
- **Server/client boundary:** The native and legacy Elements paths create a EUR PaymentIntent on the server and send its client secret to the client for confirmation. The client secret can complete the charge and the guide says not to log, embed in URLs, or expose it beyond the customer. Checkout instead creates a Checkout Session (lines 69-112, 231-253, 430-452, 636-658, 853-873, 1129-1135).
- **Outcome boundary:** The bank return and its PaymentIntent query parameters let the merchant retrieve and display status; they do not themselves prove success. The captured test path has requires_action to succeeded for authenticated success, or requires_payment_method for a failed test. The guide ties completed payment to payment_intent.succeeded and advises listening for events instead of client callbacks. Its sample Source/Charge JSON includes pending status, not a completed live result (lines 332-336, 532-536, 742-746, 1330-1401, 1475-1528).

## Integration paths and locators — 2026-05-03

- **iOS:** STPPaymentMethodEPSParams and billing name are passed with a PaymentIntent client secret to STPPaymentHandler.confirmPayment; the old capture says its iOS SDK supports iOS 13 or above. See lines 157-159, 231-336.
- **Android:** PaymentMethodCreateParams.createEps(billingDetails) is passed to PaymentLauncher.confirm; the captured Gradle example pins stripe-android 23.5.0. See lines 383-403, 430-536.
- **React Native:** The captured confirmPayment example passes paymentMethodType: 'Eps' and paymentMethodData.billingDetails with the collected name. In the dated StripeProvider sample, urlScheme is annotated as required for 3D Secure and bank redirects (lines 623-627), which is material to this EPS bank-redirect path. A separate section headed “Optional: Handle deep linking” describes registering a custom URL scheme, forwarding returns through handleURLCallback, and says universal links are unsupported for that return setup (lines 768-828). Keep the sample's bank-redirect scheme note alongside the optional handler section; neither passage establishes the same setup for Checkout, iOS, Android, or every React Native payment path. See lines 623-627, 636-720, 768-828.
- **Elements, legacy in the old capture:** The epsBank Element and EpsBankElement examples use stripe.confirmEpsPayment with account holder billing name and return_url. The old guide explicitly says epsBank is unavailable in the latest Stripe.js and recommends Payment Element; the November index does not show whether its linked Elements variant retains this implementation. See lines 830-835, 953-973, 979-1025, 1129-1156.
- **Optional manual redirect in the old Elements section:** Server-side PaymentIntent confirmation with return_url and optional bank leads to requires_action and next_action.redirect_to_url; the customer is sent to that URL and later returns. The documented pending sample is not success. See lines 1447-1540. The old bank-values table is at lines 1593-1623; it is not a verified current list.

## Related

- [[stripe-eps]] — EPS concept and reciprocal source route.
- [[source-stripe-eps]] — method overview and broader properties.

## Raw Sources

- [[raw/stripe-eps-accept-payment-2025|EPS acceptance detailed capture, 2026-05-03]] — dated integration and state evidence.

## Related raw API references

- [[raw/stripe-payments-eps-accept-a-payment-2026-11-07|EPS acceptance variant index, 2026-11-07]] — navigation only: Checkout, Elements, iOS, Android, and React Native. Linked variant bodies were not in this pin.
