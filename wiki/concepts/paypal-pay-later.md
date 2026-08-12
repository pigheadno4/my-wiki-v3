---
title: "PayPal Pay Later"
type: concept
category: technology
tags: [paypal, pay-later, pay-in-4, pay-monthly, bnpl, installments, messaging, us]
---

## PayPal Pay Later

PayPal's buy now, pay later (BNPL) product suite. Merchants receive full payment at checkout; buyers pay in installments. Available in multiple countries — US offerings documented here.

## Products by Country

| Country | Product | Payments | Schedule | Purchase range | APR |
| ------- | ------- | -------- | -------- | -------------- | --- |
| US | Pay in 4 | 4 | Biweekly | $30–$1,500 USD | None |
| US | Pay Monthly | 3/6/12/24 | Monthly | $49–$10,000 USD | 9.99–35.99% |
| AU | Pay in 4 | 4 | Biweekly (1st at checkout) | AUD $1–$1,999.99 | None |
| CA | Pay in 4 | 4 | Biweekly (1st at checkout) | CAD $30–$1,500 | None |
| FR | Pay in 4 | 4 | Monthly over 90 days (1st at checkout) | €30–€2,000 EUR | None |
| DE | PayPal Ratenzahlung | 3/6/12/24 | Monthly | €99–€10,000 EUR | None |
| DE | Pay in 30 | 1 | Single payment within 30 days | €1–€2,000 EUR | None |
| IT | Pay in 3 | 3 | Monthly | €30–€2,000 EUR | None |
| IT | Pay in installments | 6/12/24 | Monthly | €120–€5,000 EUR | None |
| ES | Pay in 3 | 3 | Monthly | €30–€2,000 EUR | None |
| ES | Pay in installments | 6/12/24 | Monthly | €120–€5,000 EUR | None |
| UK | Pay in 3 | 3 | Monthly | £20–£3,000 GBP | None |
| UK | PayPal Credit | Revolving | Revolving | ≥£99 for 0% promo | 0% for 4 months; then standard rate |

US Pay Monthly lender: WebBank. US Pay in 4: PayPal NMLS #910457.

Country differences:

- AU: lower minimum ($1 vs $30 US), higher maximum ($1,999.99 vs $1,500), first payment at checkout
- CA: same range as US but CAD; first payment at checkout; requires bilingual support (`locale=en_CA`/`fr_CA`); stricter — cannot host own Pay Later content
- FR: higher cap (€2,000); payments monthly over 90 days (not biweekly); first payment at checkout
- DE: widest product set — Ratenzahlung (analogous to US Pay Monthly, up to €10K) + Pay in 30 (unique deferred single payment, buyer pays full amount within 30 days)
- IT + ES: identical product set — **Pay in 3** (not Pay in 4) + Pay in installments (6/12/24 months, up to €5,000)
- UK: **limited availability**; only GBP country; Pay in 3 (£20–£3,000, highest cap among Pay in 3 countries) + PayPal Credit (revolving, 0% for 4 months on ≥£99)

## Key Mechanics

- Merchant paid upfront in full — no installment risk to merchant
- No late fees to buyers (Pay in 4)
- Dynamic messaging — shows offer based on cart contents
- Multiple placement points: product pages, cart, checkout

## Eligibility (US)

- US merchant + US-facing website + USD only
- Business Account required
- One-time payment integrations only
- **Not eligible**: Reference Transactions, Recurring Payments, Website Payments Standard

## Integration

Add `messages` to `components` in the JS SDK script tag: `components=messages,buttons`.

**5 placements** with two layout styles:

| Placement | `data-pp-placement` | Layout |
| --------- | ------------------- | ------ |
| Product page | `product` | `text` (logo-type, color, size) |
| Cart | `cart` | `text` |
| Checkout | `payment` | `text` |
| Home page | `home` | `flex` (banner, ratio 8x1 or 20x1) |
| Category page | `category` | `flex` |

Key attributes: `data-pp-message`, `data-pp-amount`, `data-pp-placement`, `data-pp-style-layout`.

For the v6 React web component, `@paypal/react-paypal-js@10.1.2` expands the typed `logo-type` attribute from `MONOGRAM | WORDMARK` to `MONOGRAM | WORDMARK | TEXT`. This is a TypeScript/JSX contract for `<paypal-message>`, not evidence that every older JS SDK messaging integration accepts the same value.

For Braintree integrations, `@paypal/react-paypal-js@10.2.0` adds `useBraintreePayPalMessages()`. The hook asynchronously creates a Messages instance from Braintree's shared `paypalCheckoutV6` object, then exposes readiness, loading, error, and content-fetch state. Returned content can update its amount without a new fetch. An empty failure sentinel is still passed to `<paypal-message>` so the element can collapse while the hook exposes the fetch error.

### Native iOS Messages

The independent `paypal-messages-ios@1.2.0` package renders Pay Later and PayPal Credit promotion in UIKit or through a SwiftUI wrapper. It accepts client ID, environment, amount, placement, preferred offer, buyer country, language/locale, and style context; PayPal's response can still select a generic message. Buyer-country override requires PayPal approval.

This package is promotional presentment, not payment execution. Its click opens a learn-more/application modal; checkout still requires a separate payment integration. See [[source-github-paypal-messages-ios]].

## Available Countries (beyond US)

Pay Later offerings differ by country — Australia, France, Germany, Italy, Spain, UK each have their own products. Check the Expanded Checkout eligibility page for which countries support Pay Later.

## Relevant Companies

- [[paypal]] — PayPal company overview

## Sources

- [[source-paypal-pay-later]] — Pay Later by country (US, AU, CA, FR, DE): product tables, purchase ranges, eligibility, bilingual support (CA)
- [[source-github-paypal-js]] — package-qualified React v10.1.2 Messages typing and v10.2.0 Braintree Messages hook behavior
- [[source-github-paypal-messages-ios]] — native iOS Pay Later and PayPal Credit message configuration, rendering, modal, and lifecycle
