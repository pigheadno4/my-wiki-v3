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

### Web Messaging Runtime

The independent `@paypal/messaging-components@1.95.1` package is the browser implementation behind PayPal Credit and Pay Later promotional messaging. It exposes `Messages(options).render(selector)`, defaults to `[data-pp-message]`, merges SDK, JavaScript, and inline `data-pp-*` options, and updates an existing message instance when its amount or style changes. Dynamically inserted message containers and later `data-pp-*` attribute changes are observed and re-rendered.

The message itself is PayPal-served iframe content. Clicking it can open a PayPal-hosted learn-more or application modal; nested-frame contexts fall back to a popup. This is promotional presentment, not checkout execution, and the package does not establish merchant, buyer, country, or transaction eligibility.

At `1.95.1`, the long-term modal filters out non-qualifying offers before display, validates numeric payment counts, and applies explicit country-specific term ordering: ascending for US, ES, IT, and CA, and descending for AT, DE, and FR. The renderer also includes a Venmo logo mapping for PayPal-supplied v2 message content. That asset/rendering support is not evidence that Venmo is a Pay Later product or that the component enables Venmo checkout. See [[source-github-paypal-messaging-components]] and [[changelog-github-paypal-messaging-components]].

For the v6 React web component, `@paypal/react-paypal-js@10.1.2` expands the typed `logo-type` attribute from `MONOGRAM | WORDMARK` to `MONOGRAM | WORDMARK | TEXT`. This is a TypeScript/JSX contract for `<paypal-message>`, not evidence that every older JS SDK messaging integration accepts the same value.

For Braintree integrations, `@paypal/react-paypal-js@10.2.0` adds `useBraintreePayPalMessages()`. The hook asynchronously creates a Messages instance from Braintree's shared `paypalCheckoutV6` object, then exposes readiness, loading, error, and content-fetch state. Returned content can update its amount without a new fetch. An empty failure sentinel is still passed to `<paypal-message>` so the element can collapse while the hook exposes the fetch error.

### Native iOS Messages

The independent `paypal-messages-ios@1.2.0` package renders Pay Later and PayPal Credit promotion in UIKit or through a SwiftUI wrapper. It accepts client ID, environment, amount, placement, preferred offer, buyer country, language/locale, and style context; PayPal's response can still select a generic message. Buyer-country override requires PayPal approval.

An untagged `develop` documentation commit after `1.2.0`, `fdd1868`, changes the native iOS integration policy to Braintree-only: a merchant must have a Braintree account and integrate the Braintree SDK, and PPCP SDK integrations are unsupported. Only `README.md` changed, so this is policy evidence rather than a demonstrated runtime compatibility change or package release.

This package is promotional presentment, not payment execution. Its click opens a learn-more/application modal; checkout still requires a separate payment integration. See [[source-github-paypal-messages-ios]].

### Native Android Messages

The independent `paypal-messages-android@1.3.0` package presents Pay Later and PayPal Credit promotion through `PayPalMessageView`; a Compose wrapper is present but the retained development guide explicitly says the Jetpack view does not currently work. The README also recommends sandbox use until an official release.

A parallel untagged `develop` README commit, `0424354`, documents the same Braintree-only merchant boundary as iOS: a Braintree account and Braintree SDK integration are required, and PPCP SDK integrations are unsupported. Its comparison begins at historical SHA `1d2238c`, not released `1.3.0` SHA `f1aa138`; only documentation changed.

Like iOS, Android Messages is promotional presentment rather than payment execution. The `1.3.0` capsule adds rendered-language analytics and `%bold%` message styling, but also preserves version-qualified callback, environment-update, and shared-state risks. See [[source-github-paypal-messages-android]] and [[changelog-github-paypal-messages-android]].

## Available Countries (beyond US)

Pay Later offerings differ by country — Australia, France, Germany, Italy, Spain, UK each have their own products. Check the Expanded Checkout eligibility page for which countries support Pay Later.

## Relevant Companies

- [[paypal]] — PayPal company overview

## Sources

- [[source-paypal-pay-later]] — Pay Later by country (US, AU, CA, FR, DE): product tables, purchase ranges, eligibility, bilingual support (CA)
- [[source-github-paypal-js]] — package-qualified React v10.1.2 Messages typing and v10.2.0 Braintree Messages hook behavior
- [[source-github-paypal-messaging-components]] — web messaging runtime, PayPal-hosted iframe/modal lifecycle, style and update behavior, and exact `1.95.1` offer-processing fixes
- [[changelog-github-paypal-messaging-components]] — package-qualified web Messaging Components release ledger beginning at `1.95.1`
- [[source-github-paypal-messages-ios]] — native iOS Pay Later and PayPal Credit message configuration, rendering, modal, and lifecycle
- [[source-github-paypal-messages-android]] — native Android message view, modal, callbacks, caching, analytics, availability warning, and `1.3.0` source risks
- [[changelog-github-paypal-messages-android]] — managed Android `1.3.0` release plus cumulative earlier stable context
