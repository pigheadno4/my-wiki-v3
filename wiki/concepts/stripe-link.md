---
title: "Stripe Link"
type: concept
category: technology
tags: [stripe, link, digital-wallet, payment-network, instant-bank-payments, klarna, pix, upi, stablecoins, bnpl, recurring]
---

## Definition

Link is Stripe's payment network — a digital wallet and checkout accelerator that saves customers' payment details once and autofills them across all Link-enabled merchants. Beyond card saving, Link automatically surfaces alternative payment methods (Instant Bank Payments, Klarna, Pix, UPI, Stablecoins) for eligible customers with zero merchant integration.

## Integration Paths

Two paths produce different PaymentMethod types:

| Path | PM type | When to use |
| --- | --- | --- |
| **Link as payment method** (recommended) | `link` | Works with dynamic payment methods; no extra config |
| **Link in card-specific integration** | `card` + `card.wallet.type = 'link'` | When you need card brand / last 4 |

**Key rules**:

- Passing `link` in `payment_method_types` ALWAYS triggers PM path — even alongside `card`. Card integration = pass `card` only.
- **IC+ pricing incompatibility**: Link as PM uses blended rate; use card integration if on IC+ pricing.
- **Backup payment source**: only in PM path (auto-retry with backup if primary fails); not in card integration.
- **Non-card Link PMs in card integration** (e.g., IBP): fixed values — brand=`link`, last4=`0000`, exp=`12/2040`, funding=`unknown`; show "Link" label to customers instead of these values.

Dashboard always shows payments as `link` regardless of underlying funding method.

## Funding Methods

Cards, US bank accounts, [[stripe-instant-bank-payments|Instant Bank Payments]] (Link-exclusive — lower cost than cards, guaranteed settlement), Klarna, other BNPLs.

**Immediate confirmation** regardless of funding. Settlement same timeline as cards.

## Core Properties

- **Manual capture**: Yes
- **Recurring**: Yes
- **Disputes**: Yes (process varies by funding method)
- **Refunds**: 5–10 business days
- **Payment Element**: not supported in Thailand or Brazil

## Link Payment Methods (US-only)

Link automatically presents alternative PMs — [[stripe-instant-bank-payments|Instant Bank Payments]], Klarna, Pix, UPI, Stablecoins — with zero integration. Link handles all routing.

**Klarna on Link**: only supported in Payment Links, Stripe Checkout (Hosted), and Payment Element (not other flows). Disable via Link settings ("Pay later with Klarna"). Merchant receives full purchase amount immediately — no waiting for Klarna to collect installments. Test cards: Visa 4242... (installments), Unbranded debit 4687... (financing).

**Pix on Link**: US businesses only; BRL only; 5 BRL–3,000 USD equivalent; one-time + on-session only. Requires buyer name, address, tax identifier. Service provider: Ebanx (statement descriptor shows Ebanx; business name in "Message to payor"). IOF tax 3.5% paid by customer; Stripe/Ebanx handle calculation, disclosures, and receipts.

**Stablecoins on Link**: US businesses only; USD only; 1–10,000 USD; one-time + on-session only. Customer pays with preferred crypto wallet/token/network; Stripe settles in USD — Link guarantees funds. Refunds go to original wallet as stablecoins. Disputes not supported. Testing requires blockchain testnet wallet.

**UPI on Link**: US businesses only; INR only; 1–100,000 INR; one-time + on-session only. Desktop: QR code; mobile: list of UPI apps → redirect. Saved details include virtual payment address. Refunds: up to 60 days, async, up to 7 business days. Disputes: cannot contest — funds removed immediately if bank/PSP accepts.

**5 eligibility filters** per session: business eligibility, presentment currency, transaction limits, customer location, recurring/off-session support.

**Customer flow**:

- New: email → PM selected → Link signup + auth → instant confirmation → details saved cross-merchant
- Returning: auto-detected via email/phone/browser cookie → OTP → autofill saved details + shipping

**Disabling**: must turn off Link entirely (removes accelerated checkout + returning customer benefits). Exception: BNPL methods can be configured individually on Link settings page.

> Enabling a PM outside Link disables its Link interface — customers can't save details for faster checkout.

## Custom Checkout Page (Elements Integration)

Full guide (PaymentIntent): [[source-stripe-add-link-elements-integration]] — React + HTML+JS for all three email strategies, shipping, prefill, manual capture (7-day window), submit.

Full guide (SetupIntent / save-and-reuse): [[source-stripe-link-save-and-reuse]] — same three email strategies + Accounts v2 dual-path + charge-later flow (`off_session: true`).

**Three email strategies**:

1. **Pass email** (recommended if known beforehand): `defaultValues.billingDetails.email` — triggers Link auth at payment step; no shipping collection in this path
2. **Collect in Payment Element**: no code change; Link prompts in-form automatically
3. **LAE path** (use when collecting shipping): Link Auth Element → Address Element → Payment Element

**Same-page prefill update**: `paymentElement.update({ defaultValues: ... })` on `onblur` of form fields.

## Checkout Integration (Hosted Checkout Product)

**Dynamic PMs** (recommended): enable Link in Dashboard → remove `payment_method_types` from code. Note: if using Setup Intents for future card storage, must list manually instead.

**Manual listing**: `payment_method_types: ['card', 'link']` — `card` must be included.

**PM type** on received payment: `payment_method.type = 'link'`. No additional fees vs cards.

**Sandbox OTP codes**: any 6 digits = success; `000001` = invalid; `000002` = expired; `000003` = max attempts exceeded. Treat sandbox Link accounts as public (tied to publishable key).

**Disable**: per payment method configuration in Dashboard; takes a few minutes to propagate.

## Payment Element Integration

**Two options** for adding Link to Payment Element:

1. **Pass email (recommended)**: `elements.create('payment', { defaultValues: { billingDetails: { email } } })` — customer authenticates directly in the payment form; use when email is collected earlier in flow
2. **Collect in Payment Element**: no code change; Link prompts appear automatically in the form

**Prefill tool** (on by default): scans surrounding page for email/phone/name → auto-populates Link login/sign-up fields; values held only in local memory; disabled by local data privacy laws; customers can opt out. Disable in Link settings Dashboard.

**Accelerated sign-up** (on by default): auto-expands Link sign-up fields; configurable in Settings → Payment Methods → Link.

## Invoicing (Hosted Invoice Page)

Zero implementation — enable via Dashboard: Invoice template → Payment methods → Manage → toggle Link on. Compatible with Invoices and Subscriptions APIs. Customers can view, pay, and download invoices at the hosted URL.

## Mobile Payment Element (iOS / Android / React Native)

Enable via: latest Stripe Mobile SDK + Link in Dashboard + dynamic PMs (`automatic_payment_methods`). Prefill via `defaultBillingDetails` (name, email, phone):

- **iOS**: `configuration.defaultBillingDetails.email = ...`
- **Android**: `PaymentSheet.BillingDetails(name, email, phone)` in `PaymentSheet.Configuration`
- **React Native**: `initPaymentSheet({ defaultBillingDetails: { name, email, phone } })`

**Sandbox OTP**: `000000` (differs from web — web accepts any 6 digits)

## Card Element (Deprecated for Link)

> Not recommended — use Link Authentication Element, Express Checkout Element, or Payment Element instead.

Single-line and split (Card Number/Expiry/CVC) forms both supported. Same 90-day auth window. Display requirements: ≥ 350px wide, ≥ 28px tall; popup support required; `Cross-Origin-Opener-Policy: same-origin` blocks Link. Disable via Dashboard or `disableLink: true`. Not supported in India.

**Connect**: direct charges + payment methods on connected accounts + full Dashboard → accounts manage own settings; otherwise platform controls.

## Payment Request Button (Deprecated for Link)

> Stripe no longer recommends the Payment Request Button for Link. Use Link Authentication Element, Express Checkout Element, or Payment Element instead.

If already using it: returning customers get 90-day auth window (any Link-enabled site); no re-auth needed within window. Connect: auto-available; platform manages for platform-processed payments.

## Express Checkout Element

One-click payment buttons for Link, Apple Pay, Google Pay, PayPal, Klarna, and Amazon Pay. Buttons sort dynamically by customer location; new buttons added without frontend changes; reuses existing Elements instance.

```js
stripe.elements({ mode: 'payment', amount, currency }) → create('expressCheckout', options) → mount
```

## Link Authentication Element

Single email input field that serves two purposes: collecting customer email + triggering Link auth for returning users. When a returning Link user enters their email, Stripe autofills saved payment and shipping details.

Key: `loader: 'auto'` on Elements instance; `onChange` event fires on input and autofill; `defaultValues.email` prefill starts auth flow immediately.

**Page order**: Link Authentication Element → Address Element (optional) → Payment Element. Can be on different pages — show only once per checkout flow. Supported PMs for Link signup: credit card, debit card, US bank. Domain registration required.

## Sources

- [[source-stripe-link]] — two PM type paths (link vs card+wallet), Instant Bank Payments exclusive, Thailand/Brazil Payment Element caveat
- [[source-stripe-link-payment-methods]] — Link payment methods (US-only): LPMs, zero integration, 5 eligibility criteria, customer flow, disabling rules
- [[source-stripe-klarna-on-link]] — Klarna on Link: US-only, Payment Links/Checkout/Payment Element only, immediate merchant settlement, test cards
- [[source-stripe-pix-on-link]] — Pix on Link: US/BRL only, 5 BRL–3K USD limit, Ebanx provider, IOF 3.5% customer tax, one-time/on-session only
- [[source-stripe-stablecoins-on-link]] — Stablecoins on Link: US/USD only, 1–10K USD, any crypto wallet/token, USD settlement guaranteed, refunds as stablecoins, no disputes
- [[source-stripe-upi-on-link]] — UPI on Link: US/INR only, 1–100K INR, QR code (desktop)/app redirect (mobile), virtual payment address saved, 60-day refunds, uncontestable disputes
- [[source-stripe-checkout-link]] — Link with Checkout: dynamic vs manual listing, card required, OTP test codes, sandbox warning, Connect, disable per PMC
- [[source-stripe-elements-link]] — Link Auth Element (Elements): page order, multi-page support, React integration, onChange event, supported PMs for signup
- [[source-stripe-express-checkout-link]] — Link in Express Checkout Element: 6 one-click PMs, dynamic button sorting, no frontend changes needed
- [[source-stripe-payment-element-link]] — Link in Payment Element: pass-email vs collect-email options, prefill tool (page scan, local memory only), accelerated sign-up
- [[source-stripe-payment-request-button-link]] — Link in Payment Request Button (deprecated): 90-day auth window, Connect support; use ECE/PE/Auth Element instead
- [[source-stripe-card-element-link]] — Link in Card Element (deprecated): 90-day auth, 350px/28px min, no COOP same-origin, disableLink param, Connect eligibility rules
- [[source-stripe-mobile-payment-element-link]] — Link in Mobile PE: iOS/Android/React Native, defaultBillingDetails prefill syntax, sandbox OTP 000000
- [[source-stripe-invoicing-link]] — Link with Invoicing: Dashboard-only setup, zero code, Hosted Invoice Page, Invoices + Subscriptions APIs
- [[source-stripe-link-payment-integrations]] — Link integration paths: PM vs card-integration decision, IC+ caveat, backup payment source, non-card fixed values
- [[source-stripe-add-link-elements-integration]] — Full custom checkout guide: 3 email strategies (pass/collect/LAE), React+HTML+JS, shipping, prefill, 7-day manual capture, submit flow
- [[source-stripe-link-save-and-reuse]] — SetupIntent save-and-reuse: same 3 strategies + Accounts v2 dual-path, confirmSetup, charge-later with off_session
- [[source-stripe-link-authentication-element]] — Link Authentication Element: dual-purpose email field, onChange event, prefill behavior
