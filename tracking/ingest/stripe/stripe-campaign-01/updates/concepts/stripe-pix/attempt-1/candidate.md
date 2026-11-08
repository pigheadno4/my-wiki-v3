---
title: "Stripe Pix (Brazil)"
type: concept
category: framework
tags: [stripe, pix, pix-automatico, brazil, brl, subscriptions, payment-methods, mandate, qr-code, setup-intents]
---

## Overview

Pix is Brazil's instant payment system. The 2026-05-13 Stripe Pix subscription guide uses **Pix Automático**, a customer-authorized mandate for recurring charges, and illustrates a 20 BRL monthly price. It says a Brazilian Pix-enabled bank account is needed for its live example. These captures do not establish universal merchant, country or currency eligibility; the 2026-11-07 page is only a variant index. See [[source-stripe-subscriptions-pix]].

## Pix Automático

Pix Automático is a mandate-based extension of Pix for recurring payments. The customer authorizes a mandate in their banking app; later charges can be automatic within the mandate's conditions, but can fail or the mandate can be revoked.

**Example mandate fields (2026-05-13 guide)**:
- `payment_method_options.pix.mandate_options.amount` — the example's mandate amount. A higher amount may accommodate a future upgrade without returning on-session, but charges above the mandate or a customer-set limit can fail.
- `payment_method_options.pix.mandate_options.payment_schedule` — the example's monthly schedule; a more frequent new billing interval can fail. The older direct Subscriptions API prose makes mandate options optional and its example omits this field. Pix charging is limited to once per specified mandate cycle in that guide.

## Customer fields in the May 2026 example forms

| Field | Example form input |
|---|---|
| `name` | Full name; marked required in the SetupIntents and Subscriptions API example forms |
| `email` | Email; marked required in those example forms |
| `tax_id` | CPF (individual) or CNPJ (business); marked required in those example forms. The guide states a government requirement for cross-border transactions, not every Pix buyer. |

## Subscription integration paths

### Checkout — 2026-05-13 guide example

The 2026-11-07 page only links to a Checkout variant; its request body is unread in this comparison. The code below is the retained May example, not a verified current recipe.

```js
stripe.checkout.sessions.create({
  payment_method_types: ['pix'],
  payment_method_options: {
    pix: { mandate_options: { amount: 2000, payment_schedule: 'monthly' } }
  },
  mode: 'subscription', ...
})
```

### SetupIntents

In the 2026-05-13 SetupIntents example, `stripe.confirmPixSetup` and banking-app authorization can make the **SetupIntent** `succeeded` and attach its PaymentMethod; this is setup without an initial payment. Create a subscription with that `default_payment_method` and check its separate payment outcome. The return page verifies SetupIntent status, not invoice payment.

### Subscriptions API

In the 2026-05-13 Subscriptions API example, create an initially `incomplete` subscription with `default_incomplete`; mandate options are optional in that variant's prose. Confirm the first-invoice PaymentIntent with Pix and verify its status on return. The guide describes activation and saving the default PaymentMethod **after successful payment**, not from displaying or scanning the QR alone.

## QR code display options

`stripe.confirmPixSetup` auto-handles QR display. Or use `handleActions: false` to get `next_action.pix_display_qr_code`:
- `data` — EMV string ("copy and paste")
- `image_url_svg` / `image_url_png` — QR code images
- `expires_at` — expiry timestamp
- `hosted_instructions_url` — Stripe-hosted page URL

## Mandate revocation

Customer can revoke in their banking app at any time → Stripe fires `mandate.updated` → bring customer back on-session to create a new mandate.

## Testing

- Tax ID: `000.000.000-00`
- In sandbox: "Simulate scan" → test approval/expiry page
- Email controls behavior: `succeed_immediately@test.com`, `expire_immediately@test.com`, etc. (6 email patterns)

## Native iOS evidence

`stripe-ios@26.12.1` adds Pix bindings and announces PaymentSheet support. Retained code opens hosted instructions and uses polling; it does not establish every native SetupIntent, recurring-payment or merchant-eligibility scenario. Do not transfer the web subscription recipe above to native iOS solely from these bindings.

Failed/non-success polling deadlines report canceled. The redirect-return path can also cancel a still-pending Pix Intent; this is a code-path risk, not device-tested behavior or proof that no bank payment occurred. See [[stripe-ios-sdk]], [[source-github-stripe-ios]] and [[changelog-github-stripe-ios]] for version-qualified behavior and server-verification boundaries.

## Native Android `23.22.0` Evidence

Release notes announce Pix PaymentIntent and SetupIntent support in PaymentSheet. Compiled API adds PaymentMethod.Type.Pix, createPix overloads and StripeIntent.NextActionType.DisplayPixDetails. These declarations do not establish required customer fields, QR presentation, polling, mandate persistence or a complete native subscription flow: the model/request and PaymentSheet implementations are excluded. Do not transfer the web subscription recipe above solely from these bindings. See [[source-github-stripe-android]] and [[changelog-github-stripe-android]].

## Sources

- [[source-github-stripe-android]] - native 23.22.0 bindings and PaymentSheet release announcements with explicit implementation limits

- [[source-stripe-subscriptions-pix]] — 2026-11-07 Pix subscription variant index and retained 2026-05-13 combined Checkout, SetupIntents and Subscriptions API guide; mandate, payment and sandbox conditions are dated

> [!warning] Contradiction
> Earlier concept wording treated both mandate options as universal requirements, CPF/CNPJ as universally government-required, and a QR scan as sufficient for direct API activation. The May guide itself says direct API mandate options are optional, limits the stated tax-ID rule to cross-border transactions, and activates after successful payment. The November index does not resolve current variant rules; see [[source-stripe-subscriptions-pix]].
