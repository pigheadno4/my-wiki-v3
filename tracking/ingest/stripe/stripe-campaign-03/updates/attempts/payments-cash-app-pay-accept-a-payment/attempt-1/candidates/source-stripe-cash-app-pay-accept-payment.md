---
title: "Stripe: Accept a Cash App Pay Payment"
type: source
date_ingested: 2026-05-07
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/cash-app-pay/accept-a-payment"
raw_files:
  - "stripe-cash-app-pay-accept-payment-2025.md"
tags: [stripe, wallets, cash-app-pay, checkout, elements, direct-api, ios, android, react-native, manual-capture, authentication, qr-code]
---

## Overview

[[stripe]] Cash App Pay acceptance guide. The 2026-05-07 capture contains Checkout, Elements with Checkout Sessions or Payment Intents, Direct API, iOS, Android, and React Native instructions. The 2026-11-07 base-URL capture is a seven-route variant index only. The detailed integration facts below remain dated to May; the newer index does not establish current prerequisites, timing, SDK behavior, eligibility, or payment outcomes. See [[stripe-wallets]].

## Key takeaways — 2026-05-07 detailed capture

- **Checkout:** The captured compatibility section lists US business locations, USD currency/presentment, and payment, setup, and subscription modes. Checkout Sessions need USD line-item Prices; the manual configuration example adds cashapp to payment_method_types. These are dated guide claims, not current account eligibility.
- **Distinct objects and handoffs:** Hosted Checkout creates a Checkout Session. Elements with Checkout Sessions creates a Session on the server and passes its client secret to the front end. Elements with Payment Intents and Direct API create a PaymentIntent on the server, then confirm from the client. The Direct API guide enables cashapp in Dashboard settings. See raw headings at lines 16-56, 134-175, 635-699, and 1247-1294.
- **Authentication and state:** The Payment Intents and Direct API sections describe mobile Cash App redirect and desktop QR authentication. Their 60-minute period is an authentication-session expiry; the desktop QR can be refreshed up to 20 times before the PaymentIntent returns to the guide's stated require_payment_method spelling. Separate failed-payment sections say a requires_action customer must finish within 10 minutes after redirect or the PaymentMethod detaches and the PaymentIntent becomes requires_payment_method. The two historical timing statements have different wording and are not resolved by the November index (lines 1130-1144, 1226-1234, 1404-1416).
- **Manual capture:** The web PaymentIntent and Direct API guides describe capture_method: manual, a seven-day capture window, and requires_capture after authorization; uncaptured intents are canceled. The React Native section also says seven days, but its test section says an uncaptured test manual-capture PaymentIntent auto-expires 60 minutes after authorization. Keep this unresolved historical conflict; do not apply one deadline to every path or mode (lines 1146-1176, 1495-1525, 2446-2476, 2512-2518).
- **Outcome boundary:** The May guide describes sandbox approval/decline controls and says live redirect has no in-app approval choice. It also documents declined or timed-out payments, PaymentIntent status checks after return, and payment_intent.succeeded/payment_failed events. Redirect, QR display, client callback, and that live-mode wording alone do not establish payment success, capture, fulfillment, or settlement (lines 1013-1066, 1194-1198, 1212-1234, 1487-1493).

## Path details and locators — 2026-05-07

- **Direct API:** The ordinary client stripe.confirmCashappPayment example passes payment_method: { type: 'cashapp' } and return_url after server creation of a PaymentIntent. A separate optional handleActions: false manual-redirect example passes payment_method_data: { type: 'cashapp' }, return_url, then inspects requires_action and next_action. The latter parameter is not the ordinary client example. The guide says automatic return_url redirect is mobile-browser only; desktop can redirect after the returned promise resolves (lines 1271-1294, 1384-1402, 1418-1463).
- **Manual next action:** In the optional Direct API branch, mobile_auth_url and desktop QR payloads each have a stated 30-second expiry; retrieve the PaymentIntent for fresh action data. The guide says wait for a webhook outcome or poll PaymentIntent status on the desktop QR page (lines 1465-1493).
- **Mobile SDKs:** The iOS custom-form section uses STPPaymentHandler and an app return URL; the Android custom-form section uses PaymentLauncher. The React Native section uses useConfirmPayment with paymentMethodType CashApp; its iOS-only return setup requires a custom URL scheme and says universal links are unsupported. SDK/version details in these sections are historical examples (lines 1596-1623, 1750-1809, 1927-1973, 2055-2103, 2203-2212, 2347-2355, 2409-2435).

## Related

- [[stripe-wallets]] — Cash App Pay wallet context and reciprocal route.
- [[stripe-cash-app-pay]] — provider concept; subscription and setup flow is separate from accepting a payment.
- [[source-stripe-cash-app-pay]] — method overview and eligibility context.
- [[source-stripe-cash-app-pay-set-up-payment]] — saving for future payments.

## Raw Sources

- [[raw/stripe-cash-app-pay-accept-payment-2025|Cash App Pay acceptance detailed capture, 2026-05-07]] — factual basis for the dated flows and unresolved internal timing conflict.

## Related raw API references

- [[raw/stripe-payments-cash-app-pay-accept-a-payment-2026-11-07|Cash App Pay acceptance variant index, 2026-11-07]] — navigation only: Checkout; Elements with Checkout Sessions or Payment Intents; Direct API; iOS; Android; React Native. Variant bodies were not in this pin.
