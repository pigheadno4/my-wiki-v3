---
title: "Pay with Venmo"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-pay-with-venmo.md"
  - "paypal-pay-with-venmo-integrate.md"
  - "paypal-pay-with-venmo-test.md"
  - "paypal-venmo-sdk-v6.md"
tags: [paypal, venmo, checkout, payment-buttons, mobile, qr-code, us-only, javascript-sdk-v6]
---

## Overview

Overview of the Pay with Venmo integration — how to add a Venmo button to an existing PayPal Checkout integration so US buyers can pay with their Venmo wallet.

Source URL: <https://developer.paypal.com/docs/checkout/pay-with-venmo/>

Last updated: 2025-05-08

## Key Takeaways

### What Venmo adds for buyers

- Seamless checkout using any payment method in their Venmo wallet
- Ability to split purchases among friends
- Option to share purchase activity on Venmo's social feed

### Two checkout flows

**Mobile workflow:**

1. Buyer taps Venmo button → device switches to Venmo app
2. Buyer taps Pay in app
3. Buyer is routed back to merchant website

**Desktop browser workflow (QR code):**

1. Buyer clicks Venmo button → QR code is generated on screen
2. Buyer scans QR code using Venmo app (or mobile device camera)
3. Buyer completes payment review in Venmo app
4. Buyer is routed back to merchant website

### Eligibility

- US merchants and US consumers only
- USD only
- JavaScript SDK integration required
- Mobile: Safari (iOS) or Chrome (Android) only
- Desktop: any major browser
- Buyers must have Venmo iOS or Android app installed

### Supported features

| Feature | Supported |
| --- | --- |
| One-time payments | Yes |
| Authorization and capture | Yes |
| Online purchases | Yes |
| Save Venmo during purchase | Yes |
| Shipping module | Yes |
| Multi-seller payments | No |
| Save Venmo for purchase later | No |
| Buy online, pay in store | No |
| Contact module | No |

### Integration

Venmo is **not shown by default** — must add `enable-funding=venmo` as a query parameter to the JS SDK `<script>` tag. Beyond that, no Venmo-specific Buttons config is required:

```javascript
<script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&enable-funding=venmo"></script>
<script>
  paypal.Buttons().render('#paypal-button-container')
</script>
```

**Sandbox testing**: add `buyer-country=US` to the SDK script tag to simulate Venmo (US-only, not shown otherwise in sandbox).

**Placement**: Venmo button appends below any existing vertical button stack — leave room for it on the page.

**Confirmation pages**: use `data.fundingSource` in `onClick` (value: `"venmo"`) to update copy from "PayPal" to "Venmo" on confirmation/notification UIs.

```javascript
paypal.Buttons({
  onClick: (data) => {
    fundingSource = data.fundingSource // "venmo"
  },
})
```

### Sandbox testing

Sandbox differs from production — desktop shows **web login flow**, not QR code. Desktop QR code testing is **unavailable in sandbox**.

| Sandbox context | Experience |
| --- | --- |
| Desktop | Web login flow |
| Mobile + Venmo app installed | App-switch flow |
| Mobile + no Venmo app | Web login flow |

**Error trigger amounts** (any other amount → SUCCESS):

| Amount | Error |
| --- | --- |
| 12.34 | INSUFFICIENT_FUNDS |
| 21.43 | ACCOUNT_CLOSED |
| 11.45 | ACCOUNT_FROZEN |
| 10.23 | SUSPECTED_FRAUD |
| 13.42 | GENERIC_DECLINE |

**Sandbox NOT supported**: vault subsequent purchases, self-service test account creation, post-purchase feed/ledger, settlement, disputes, merchant reporting.

## Raw Sources

- [[paypal-pay-with-venmo]] — verbatim webpage content with eligibility, supported features table, mobile/desktop flow descriptions and screenshots
- [[paypal-pay-with-venmo-integrate]] — integration guide: enable-funding=venmo param, sandbox buyer-country=US, placement note, onClick fundingSource handler
- [[paypal-pay-with-venmo-test]] — sandbox testing: 3 use cases, desktop QR unavailable in sandbox, 5 error trigger amounts, supported/unsupported sandbox features
- [[paypal-venmo-sdk-v6]] — SDK v6 integration (docs.paypal.ai): `<venmo-button>` custom element, `createVenmoOneTimePaymentSession`, `findEligibleMethods`, `"auto"` only presentation mode, US+USD only

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview; Venmo is a PayPal-owned product
- [[paypal-checkout]] — Venmo button surfaces within PayPal Checkout JS SDK integration
