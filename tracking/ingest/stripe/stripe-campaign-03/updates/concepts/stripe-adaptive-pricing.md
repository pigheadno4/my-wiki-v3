---
title: "Stripe Adaptive Pricing"
type: concept
category: technology
tags: [stripe, adaptive-pricing, local-currency, checkout, payment-links, presentment-currency, international, fx]
---

## Stripe Adaptive Pricing

In the 2026-11-07 Checkout Sessions/Elements guide, Stripe says Adaptive Pricing uses machine learning to select a relevant local presentment currency, calculates converted prices and offers an exchange rate guaranteed for 24 hours across more than 150 customer markets. Stripe says the feature can facilitate compliance when presenting supported currencies; merchants remain responsible for applicable price-localization laws, and Stripe requires the Currency Selector Element for this Elements flow. The guide lists no direct additional merchant Adaptive Pricing fee, with a 2–4% customer conversion fee embedded in the presented rate. These are dated guide claims, not a guarantee of a merchant's eligibility or legal compliance. See [[source-stripe-adaptive-pricing-elements]].

## How It Works

1. Customer visits Checkout or Payment Link
2. Stripe ML selects most relevant presentment currency based on customer location
3. Price automatically converted at mid-market rate + 2–4% fee (guaranteed 24h)
4. Customer sees local price; can opt to pay in integration currency instead (avoiding Adaptive Pricing fee)
5. After payment: the November Elements guide distinguishes localized values in the client Elements Session from an API Checkout Session described as retaining integration currency with customer context under `presentment_details`; its testing paragraph conflicts by saying API Checkout Session `currency`, `payment_method_types` and `amount_total` reflect the local currency. Treat the API-object result as unresolved in these captures; see [[source-stripe-adaptive-pricing-elements]].

## Enablement

- **Payment Links**: always enabled, cannot be disabled
- **Checkout (hosted)**: managed in Dashboard → [Adaptive Pricing settings](https://dashboard.stripe.com/settings/adaptive-pricing)
- **Elements (Checkout Sessions API)**: Dashboard OR `adaptive_pricing.enabled` per session; **additionally requires** `adaptivePricing: { allowed: true }` in `initCheckoutElementsSdk` options to mark the integration as ready
- Disabling doesn't affect already-converted sessions or active local-currency subscriptions

## Pricing

| | Cost |
| --- | --- |
| Merchant | 0% additional |
| Customer | 2–4% embedded in exchange rate (Stripe-determined) |

Customer avoids fee by choosing integration currency (but their bank may apply exchange fees).

## Local Payment Methods Unlocked

The 2026-11-07 Checkout Sessions/Elements guide lists 26 methods that require local-currency presentment, six more than its 2026-04-21 list: Alipay · Amazon Pay · Bacs Debit · Bancontact · Bizum · BLIK · EPS · iDEAL · Link · P24 · Pix · South Korean cards · MB WAY · Naver Pay · Kakao Pay · Pay by Bank · PAYCO · PayPal · Revolut Pay · Samsung Pay · Satispay · SEPA Debit · TWINT · WeChat Pay · Klarna (EU+UK only) · UPI. This is a guide list, not a guarantee of availability for each merchant, market or customer. See [[source-stripe-adaptive-pricing-elements]].

> Cross-border subscriptions: only cards, Link, Apple Pay, Google Pay.

## Reporting

`presentment_details` hash added to events when customer pays in local currency:

- `checkout.session.completed` → `presentment_amount` + `presentment_currency`
- `payment_intent.succeeded` → `presentment_amount` + `presentment_currency`
- `customer.subscription.created` → `presentment_currency` (used for future off-session charges)

The April and November Elements guides say in their display sections that the API Checkout Session remains in integration currency with localized customer context under `presentment_details`, while their testing sections say the Checkout Session's `currency`, `payment_method_types` and `amount_total` reflect local currency when local presentment is possible (April raw lines 39, 180; November raw lines 38, 203). The client Elements Session can contain localized amounts. These API Checkout Session statements conflict in the captures; do not assert an unconditional currency or amount value. See [[source-stripe-adaptive-pricing-elements]].

## Testing

Pass `customer_email: 'test+location_XX@example.com'` on session create (replace `XX` with ISO country code, e.g. `FR` for France). For Payment Links, use `prefilled_email` URL parameter.

## Restrictions

The 2026-11-07 Checkout Sessions/Elements guide excludes Elements + Payment Intents API and Checkout Sessions with `capture_method: 'manual'`. A manually fixed local amount in Price `currency_options` overrides Adaptive Pricing for that currency; other currencies may still convert where the feature and Checkout configuration support it. See [[source-stripe-manual-currency-prices]] for the Checkout Session path and localization prerequisites. The integration or price currency must be a settlement currency of the merchant of record, and Indian businesses are supported only if they accept international payments. The 2026-04-21 guide instead said Indian businesses were unsupported and excluded custom amounts; the November restriction list omits custom amounts, so their current applicability is unresolved. These guide conditions do not establish account-specific eligibility. See [[source-stripe-adaptive-pricing-elements]].

## Supported Coverage

150+ countries across 6 regions: North America (23), South America (9), Europe (44), Asia (39), Oceania (5), Africa (38).

## Refunds

Refund in integration currency → Stripe automatically refunds customer in their local currency at the original exchange rate. No extra cost to merchant or customer.

## Sources

- [[source-stripe-adaptive-pricing]] — Full reference: 150+ countries, 20 local PMs, presentment_details, testing, restrictions, pricing, refunds
- [[source-stripe-adaptive-pricing-elements]] — April and November 2026 Checkout Sessions/Elements guide: separate client `adaptivePricing.allowed` and Session/Dashboard enablement, 26 named local methods, conditional India support, selector troubleshooting, unresolved API Checkout Session currency wording, and dated April-only custom-amount restriction.
- [[source-stripe-manual-currency-prices]] — manually fixed Price currency_options on Checkout Sessions override Adaptive Pricing for those currencies; November 2026 adds a customer-configured Account testing option
