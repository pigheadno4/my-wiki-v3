---
title: "PayPal Pay Later (US, AU, CA, FR, DE, IT, ES, UK)"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-pay-later-us.md"
  - "paypal-pay-later-au.md"
  - "paypal-pay-later-ca.md"
  - "paypal-pay-later-fr.md"
  - "paypal-pay-later-de.md"
  - "paypal-pay-later-it.md"
  - "paypal-pay-later-es.md"
  - "paypal-pay-later-uk.md"
  - "paypal-pay-later-integrate.md"
  - "paypal-pay-later-advanced-js.md"
  - "paypal-pay-later-analytics.md"
  - "paypal-pay-later-reference.md"
  - "paypal-pay-later-code-samples.md"
  - "paypal-pay-later-upgrade-options.md"
  - "paypal-pay-later-cross-border.md"
  - "paypal-pay-later-overview.md"
  - "paypal-pay-later-analytics-logging.md"
  - "paypal-pay-later-upgrade-v6.md"
tags: [paypal, pay-later, pay-in-4, pay-in-3, pay-monthly, bnpl, us, au, ca, fr, de, it, installments, messaging]
---

## PayPal Pay Later (US)

Overview of PayPal's Pay Later products for US merchants — two BNPL offerings (Pay in 4 and Pay Monthly) that let merchants get paid upfront while buyers pay in installments.

Source URL: <https://developer.paypal.com/docs/checkout/pay-later/us/>

Last updated: 2026-03-06

## Key Takeaways

### Pay Later by country

| Country | Products | Currency | Purchase range | First payment |
| ------- | -------- | -------- | -------------- | ------------- |
| US | Pay in 4, Pay Monthly | USD | $30–$1,500 / $49–$10,000 | 2 weeks after checkout |
| AU | Pay in 4 only | AUD | AUD $1–$1,999.99 | At checkout |
| CA | Pay in 4 only | CAD | CAD $30–$1,500 | At checkout |
| FR | Pay in 4 only | EUR | €30–€2,000 | At checkout; subsequent monthly over 90 days |
| DE | PayPal Ratenzahlung + Pay in 30 | EUR | €99–€10,000 / €1–€2,000 | Monthly / Single in 30 days |

DE unique: two distinct products. **Pay in 30** is a BNPL deferred single payment — the only such product across all countries documented.
| IT | Pay in 3 + Pay in installments | EUR | €30–€2,000 / €120–€5,000 | Monthly |

IT unique: **Pay in 3** (not Pay in 4); two monthly products with distinct purchase ranges.
| UK | Pay in 3 + PayPal Credit | GBP | £20–£3,000 / revolving | Monthly / revolving |

UK unique: only GBP country; **limited availability**; also offers **PayPal Credit** (revolving line, 0% for 4 months on purchases ≥£99).

### Two Pay Later products (US)

| Product | Payments | Schedule | Purchase range |
| ------- | -------- | -------- | -------------- |
| **Pay in 4** | 4 | Biweekly (every 2 weeks) | $30–$1,500 |
| **Pay Monthly** | 3, 6, 12, or 24 | Monthly | $49–$10,000 |

Key difference: Pay in 4 is a short-term no-fee installment; Pay Monthly is a credit product with APR (9.99–35.99%), subject to credit approval, lender is WebBank.

### Merchant gets paid upfront

Despite buyer paying in installments, merchant receives full payment at checkout. No late fees to buyers.

### Eligibility constraints

- US-based PayPal merchant with Business Account
- US-facing website, USD only
- One-time payment integrations only — **Reference Transaction and Recurring Payment integrations are NOT eligible**
- Website Payments Standard (WPS) also excluded
- Cannot modify Pay Later messages with additional marketing content

### Integration paths

- Code it yourself (via JS SDK)
- Commerce platform integration
- Upgrade from existing integration

## Raw Sources

- [[paypal-pay-later-us]] — verbatim webpage content with Pay Later product table, eligibility rules, legal notices
- [[paypal-pay-later-au]] — AU Pay Later: Pay in 4 only, AUD $1–$1,999.99, first payment at transaction time
- [[paypal-pay-later-ca]] — CA Pay Later: Pay in 4 only, CAD $30–$1,500, first payment at checkout, bilingual support (en_CA/fr_CA), stricter content hosting restriction
- [[paypal-pay-later-fr]] — FR Pay Later: Pay in 4 only, €30–€2,000 EUR, monthly payments over 90 days, France-based merchant required
- [[paypal-pay-later-de]] — DE Pay Later: PayPal Ratenzahlung (3–24 monthly, €99–€10K) + Pay in 30 (single deferred payment, €1–€2K, due in 30 days)
- [[paypal-pay-later-it]] — IT Pay Later: Pay in 3 (3 monthly, €30–€2K) + Pay in installments (6/12/24 monthly, €120–€5K)
- [[paypal-pay-later-es]] — ES Pay Later: identical products to IT — Pay in 3 + Pay in installments, same ranges
- [[paypal-pay-later-uk]] — UK Pay Later: Pay in 3 (£20–£3,000 GBP) + PayPal Credit (revolving, 0% 4 months on ≥£99); limited availability
- [[paypal-pay-later-integrate]] — Integration guide: components=messages,buttons; 5 placements (product/cart/payment/home/category); text layout vs flex/banner layout; data-pp-* attributes
- [[paypal-pay-later-advanced-js]] — Advanced JS: paypal.Messages() API, event hooks (onRender/onClick/onApply), namespace, multi-message render, attribute-based auto-update, SPA guidance
- [[paypal-pay-later-analytics]] — Analytics: inline HTML attribute event hooks (data-pp-onrender/onclick/onapply); HTML attributes override JS API
- [[paypal-pay-later-reference]] — Full reference: all config properties, HTML attribute equivalents, style.ratio values, pageType values, contextualComponents, currency codes
- [[paypal-pay-later-code-samples]] — Upgrade options: legacy merchant.js migration, checkout.js coexistence (data-namespace), components=messages vs buttons,messages patterns
- [[paypal-pay-later-upgrade-options]] — Duplicate of code-samples page (different URL, same content); archived for completeness
- [[paypal-pay-later-cross-border]] — Cross-border messaging (limited release): buyerCountry/data-pp-buyercountry, 7 countries, requires PayPal approval, stricter content modification rules
- [[paypal-pay-later-overview]] — Consolidated docs.paypal.ai overview: all 8 countries in one page, product tables, eligibility rules, 14 downloaded screenshots; Canada uses `locale=en_CA`/`fr_CA` and `enable-funding=paylater`; Germany unique: Pay in 30 Days (€1–€2,000) + Ratenzahlung installments
- [[paypal-pay-later-analytics-logging]] — Analytics hooks for Messages SDK v6: `onTemplateReady`, `onContentReady`, `onShow`/`onApply`/`onClose`, `paypal-message-click` DOM event; `content.update({amount})` for dynamic updates
- [[paypal-pay-later-upgrade-v6]] — v5→v6 upgrade: `data-pp-message` div → `<paypal-message>` Lit component; `paypal.Messages()` → `createPayPalMessages()`; `auto-bootstrap` attr eliminates manual JS; clientId or clientToken auth

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — Pay Later is surfaced through PayPal Checkout buttons
- [[recurring-payments]] — note: recurring payment integrations are NOT eligible for Pay Later
