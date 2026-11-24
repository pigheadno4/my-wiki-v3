---
title: "TWINT (Stripe)"
type: concept
category: technology
tags: [stripe, twint, switzerland, chf, bank-redirect, recurring, disputes, connect]
---

## Definition

TWINT is Switzerland's dominant mobile payment method. Customers authenticate via a TWINT app — either by mobile redirect or by scanning a desktop QR code. API enum: `twint`. Customer-initiated, immediate notification.

**Currency**: CHF. **Customers**: Switzerland. **Business locations**: 35. The November 7, 2026 overview lists approval-required B2C payments from CHF 0.50 to CHF 5,000.

## Two Payment Flows

The November 7, 2026 flow starts at a TWINT-hosted page. On mobile the customer chooses the app. On desktop the customer scans the hosted page’s QR code. The customer authorizes in the app. The May 3, 2026 capture described the merchant website presenting the desktop QR code.

## Key Properties

- **Recurring**: Supported. The May 3, 2026 guide classified TWINT as a bank redirect and the November 7, 2026 guide classifies it under Wallets.
- **Disputes**: Customers file through their bank. May 3, 2026 reported 25–50 per 1,000,000 transactions.
- **Refunds**: Full or partial within 180 days, with multiple partial refunds capped at the original amount.
- **Products**: November lists Checkout, Payment Links, Payment Element, Billing, Invoicing, Customer Portal, Radar, and Connect, and excludes Express Checkout Element, Payment Method Messaging Element, Managed Payments, and Terminal.

## Onboarding Requirements

Must comply *before* requesting access or capability stays `pending`:

- Functional public website (not password-protected)
- Legal notice/T&C displaying: company name/legal form, full address, contact (email or phone)
- CHF prices displayed; Switzerland as shipping destination for physical goods
- TWINT can **suspend or terminate** access for non-compliance

## Connect

`twint_payments` is required. The May 3, 2026 overview names direct charges, destination charges, and separate charges and transfers. The November 7, 2026 overview gives the default name as the connected account for direct charges and charges using `on_behalf_of`, or the platform for destination and separate charges and transfers without `on_behalf_of`. TWINT may choose whether to display a forwarded custom descriptor.

## Integration

**Checkout (May 3, 2026 one-time guide).** Accept in `payment` mode with all line items in `chf`. Enable Dynamic Payment Methods or include `twint` manually. The hosted and embedded examples list `['card', 'twint']` and use `success_url` and `return_url`, respectively. The separate dated setup and hosted subscription guides show their respective Checkout modes. The November cross-method matrix lists support for Checkout under its three-mode default, and the November acceptance and billing selectors provide navigation. See [[source-stripe-twint-accept-payment]] and [[source-stripe-subscriptions-twint]].

**Checkout (setup mode)**: `mode: "setup"`, `payment_method_types: ['twint']` — saves mandate with no payment upfront.

**Elements**: `stripe.confirmSetup()` (setup mode) or `stripe.confirmPayment()` with `setup_future_usage` (payment mode).

**Direct API.** In the May legacy payment route, `stripe.confirmTwintPayment()` handles the redirect with required `return_url`. The optional one-time server route redirects to `next_action.redirect_to_url.url` when the PaymentIntent requires action and the next action type is `redirect_to_url`. The separate setup route uses `stripe.confirmTwintSetup()` client-side. Manual setup and save-during-payment examples include `mandate_data.customer_acceptance.online` with IP address and user agent. The one-time server example omits mandate data. Verify payment status independently of browser return. See [[source-stripe-twint-accept-payment]].

**Saved TWINT return URL (May 2026)**. The guides make `return_url` optional for reuse when TWINT was previously set up via a SetupIntent or a PaymentIntent with `setup_future_usage`. See [[source-stripe-twint-save-during-payment]] and [[source-stripe-twint-set-up-future-payments]].

## Sources

- [[source-stripe-twint]] — May and November overviews covering eligibility, hosted authorization, mandate lifecycle, refunds, disputes, and Connect.
- [[source-stripe-twint-accept-payment]] — May 2026 one-time Checkout and legacy Direct API, with distinct redirect and verification paths. The November index links Checkout, Direct API, iOS and Android.
- [[source-stripe-twint-save-during-payment]] — May 2026 guide and November variant index for initial-payment saving, customer association, mandate verification, and qualified off-session reuse.
- [[source-stripe-twint-set-up-future-payments]] — May 2026 guide to setup without an upfront charge via Checkout, Elements and Direct API, with later reuse and November variant navigation
- [[source-stripe-subscriptions-twint]] — May 2026 subscription examples for Checkout, Setup Intents and Subscriptions API; November 2026 variant index. Direct API examples include mandate_data and return_url; the Checkout example does not. Hosted QR redirects are described for the direct examples.

> [!warning] Contradiction
> The earlier source summary treated mandate_data and return_url as universal TWINT subscription requirements, but the May Checkout example has neither while the direct API examples include both. The November index has no variant bodies, so current requiredness remains unverified; see [[source-stripe-subscriptions-twint]].
