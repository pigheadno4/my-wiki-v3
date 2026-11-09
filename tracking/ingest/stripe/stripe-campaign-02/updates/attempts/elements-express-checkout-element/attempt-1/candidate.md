---
title: "Stripe Express Checkout Element"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/elements/express-checkout-element"
raw_files:
  - "stripe-elements-express-checkout-element-2026-11-07.md"
  - "stripe-express-checkout-element-2025.md"
tags: [stripe, elements, express-checkout, apple-pay, google-pay, paypal, link, klarna, amazon-pay, one-click-payments, wallet]
---

## Overview

The Express Checkout Element presents one-click buttons for six built-in methods: Link, Apple Pay, Google Pay, PayPal, Klarna, and Amazon Pay. The November 7, 2026 product page adds a custom-payment-method button route, a more specific browser/webview matrix, and an `availablepaymentmethodschange` availability example. The April 21 capture remains dated historical evidence for its `ready`/`availablePaymentMethods` example. Neither overview names exact Stripe.js/React package versions for the event change, proves that `ready` was removed, or demonstrates a payment completion.

## Availability and setup

Buttons appear only when a method is active, supported, and set up for the actual customer environment. Dashboard activation, browser and currency support, customer wallet setup, and domain registration in **both sandbox and live mode** still matter. Stripe sorts eligible buttons by relevance; merchant country comes from the publishable key, and changing it requires unmounting the Element, updating the key, then remounting. Shipping collection requires creation options. The demo's displayed buttons are only examples, not merchant or device eligibility proof.

The **November** availability pattern is `availablepaymentmethodschange` with a `paymentMethods` payload, or React `onAvailablePaymentMethodsChange={({ paymentMethods }) => ...}`. Use it to decide whether to show a fallback such as Payment Element when no wallet is available, or whether to hide the ECE container until a method is available. The **April** page instead used `ready`, `availablePaymentMethods`, and React `onReady` for that purpose. Preserve the dated API-shape difference; this page does not establish package-version transition, deprecation of `ready` for every purpose, or successful wallet execution. November raw lines 316–377; April raw lines 301–361.

## Browser and webview matrix

The November browser table (raw lines 63–81) lists Firefox desktop Apple Pay as supported **subject to** `paymentMethods.applePay: 'always'` on non-Safari desktop browsers. April's Firefox row said unsupported and its desktop Chromium footnote additionally said macOS-only. The November footnote omits that operating-system condition; omission does not prove Windows/Linux or every desktop OS is eligible. Other browser distinctions remain: Firefox desktop lacks Link and Klarna; Safari Google Pay requires `always`; Chrome on Android lacks Apple Pay; iOS 16+ Firefox/Edge have narrower PayPal/Amazon/Klarna coverage than Chrome. In an iframe, the Apple Pay origin rule and Safari 17+ `allow="payment"` exception remain at November line 77.

| Method | November in-app webview support |
| --- | --- |
| Apple Pay | Eligible iOS webviews, subject to standard Apple Pay requirements |
| Google Pay | Eligible environment **and** no popup required; Android host app must support Payment Request API |
| Link, PayPal, Klarna, Amazon Pay | Marked unsupported |

Webview support is additional to standard browser and method eligibility. The April blanket limited-webview warning is historical. The November page suggests native iOS/Android SDKs for mobile apps; it does not claim that a table check, an availability event, or a mounted button proves a payment will complete. November raw lines 83–96; April raw line 78.

## Button controls and styling

The default layout is a space-dependent grid with overflow when needed; `layout` controls rows/columns/overflow. `buttonType` differs by wallet: Apple Pay has `plain`, `buy`, `check-out`, `subscribe`, `donate`, and others; Google Pay has `plain`, `buy`, `checkout`, `pay`, `subscribe`, and others; PayPal has `paypal`, `checkout`, `buynow`, `pay`; Klarna has `continue`, `pay`; Link and Amazon Pay each have one type. See November raw lines 98–211 for exact lists and example.

Wallet logos and brand colors are controlled by each method. The supported styling controls are button height, border radius through Appearance, and per-method button themes. Apple Pay offers `black`, `white`, `white-outline`; Google Pay `black`, `white`; PayPal `gold`, `blue`, `silver`, `white`, `black`. Klarna themes and compatible theme selection are described at November raw lines 213–299.

For built-in methods, Dashboard activation, `paymentMethodOrder`, layout, and Apple/Google Pay `paymentMethods.*` `never`/`always` can affect display. `always` does **not** override unsupported platform or currency conditions. The page notes Finland and Sweden debit-before-credit presentation rules. November raw lines 301–314.

The November overview says `customPaymentMethods` on `stripe.elements()` can add custom method buttons to the row. A button does not appear if the ID is not a valid Dashboard-configured `cpmt_` ID or `handleRender` throws. The April overview's “can't specify which methods” sentence predates that support. Separately, a versioned `@stripe/stripe-js@9.14.0` beta declaration in [[source-github-stripe-js]] identifies a typed embedded custom-method surface; neither the product page nor that type declaration proves a given account's cohort, production rollout, or successful rendering. November raw lines 55 and 301–312; April raw line 289.

## Related

- [[stripe-express-checkout-element]] — concept, integration routes, and version-qualified notes.
- [[source-stripe-express-checkout-element-accept-payment]] — Checkout Sessions and Payment Intents integration, confirmation and collection details.
- [[source-stripe-express-checkout-element-migration]] — Payment Request Button migration.

## Raw Sources

- [[raw/stripe-elements-express-checkout-element-2026-11-07|November 7, 2026 Express Checkout Element overview]]
- [[raw/stripe-express-checkout-element-2025|April 21, 2026 Express Checkout Element overview]]
