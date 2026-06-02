---
title: "Buy Now, Pay Later (Stripe)"
type: concept
category: technology
tags: [stripe, bnpl, buy-now-pay-later, klarna, affirm, afterpay, installments, payments]
---

## Definition

Stripe supports 11 buy now, pay later (BNPL) payment methods. Merchants are paid immediately and in full; customers pay nothing or a portion at purchase time and repay in installments. All BNPL methods require a redirect.

## Supported Methods

| Method | API enum | Countries | Transaction limits | Notable |
| --- | --- | --- | --- | --- |
| Affirm | `affirm` | US, CA | $50–$30k | Subscriptions, Terminal |
| Afterpay/Clearpay | `afterpay_clearpay` | AU, CA, NZ, UK, US | $1–$4k | — |
| Alma | `alma` | — | — | — |
| Billie | `billie` | — | — | setup_future_usage |
| Klarna | `klarna` | 22 countries | $10+ | SetupIntents, Express Checkout, setup_future_usage, Subscriptions |
| Kriya | `kriya` | — | — | setup_future_usage |
| Mondu | `mondu` | — | — | setup_future_usage |
| Scalapay | `scalapay` | — | — | — |
| SeQura | `sequra` | — | — | setup_future_usage |
| Sunbit | `sunbit` | — | — | No manual capture |
| Zip | `zip` | AU, US | AU: 0.01–50k AUD; US: $35–$1.5k | No manual capture, no setup_future_usage |

**Meses sin intereses** (Mexico): credit card installments 3–24 months; min 100 MXN/month.

## API Support

All BNPL methods support:

- PaymentIntents ✓
- Redirect required ✓

**Manual capture**: Affirm, Afterpay, Alma, Billie, Klarna, Kriya, Mondu, SeQura ✓ (Sunbit, Zip ✗)

**SetupIntents**: Klarna only

**setup_future_usage**: Billie, Klarna, Kriya, Mondu, SeQura

**Express Checkout Element**: Klarna only (no `setup_future_usage` when using ECE)

## Affirm Details

**Domestic only** — customer country must equal merchant country. Buyer country determined by shipping address → geocoded IP.

**Financing packages**: Standard (default) and Enhanced (more 0% APR tiers). Configurable in Dashboard; platforms excluded from 0% APR plans.

**Refunds**: up to 120 days; async processing (`refund.updated`/`refund.failed` webhooks); no fee credits returned.

**Disputes**: no time limit for customer to file; 30-day resolution; 15-day merchant evidence window; Affirm covers fraud losses.

**Prohibited**: B2B, home improvement, titled goods (cars/boats), professional services, NFTs, pre-orders.

**Connect**: requires `affirm_payments` capability + correct MCC.

**Integration notes**: 12-hour expiry for `requires_action` PaymentIntents. `affirm_checkout_canceled` error can't distinguish user cancel from Affirm loan rejection. Shipping address in `payment_intent_data[shipping]` helps loan acceptance. Always offer fallback payment methods (Affirm has higher decline rates).

## Afterpay / Clearpay Details

**US rebrand**: Afterpay → Cash App Afterpay (no integration changes needed). UK name: Clearpay.

**Domestic only** across 5 countries. Transaction limits: AU $4k AUD, CA $2k CAD, NZ $4k NZD, UK £1.2k GBP, US $4k USD.

**US tiers**: Pay in 4 ($1–$399.99), Pay in 4 + monthly ($400–$2k), monthly only ($2k.01–$4k). All other markets: Pay in 4 only.

**Disputes**: 120-day customer window; 14-day merchant evidence; 30-day decision. Afterpay covers fraud.

**Refunds**: 120-day window; async.

**Prohibited**: alcohol, bars, donations, pre-orders, NFTs, B2B.

**Integration notes**: 3-hour expiry for `requires_action` PaymentIntents (vs Affirm's 12 hours). `billing_details` required for manual PaymentIntent path. Shipping optional but improves auth rates.

## Alma Details

**Coverage**: FR, IT, ES, NL, BE, LU. EUR only. 50–5,000 EUR. Pay in 2, 3, or 4 (interest-free; first installment may be higher based on credit). Payout T+3.

**Refunds**: 180-day window; async (up to 5 min).

**Disputes**: 120-day customer window; 14-day merchant evidence; 25-day Alma decision. Must maintain low fraud/dispute rates or risk losing access.

**Connect**: online marketplaces only (e.g., Deliveroo/ManoMano) — NOT platforms onboarding other businesses (e.g., Shopify). Requires Dashboard onboarding request.

**Prohibited**: sole proprietorships, B2B, education, professional services, transportation, travel, telecom/utilities, veterinary.

**Required customer terms**: merchants must add 4 clauses to general terms of sale (Alma T&Cs, non-approval may cancel purchase, 14-day withdrawal right).

**Integration notes**: **1-hour expiry** for `requires_action` PaymentIntents (shortest of all BNPL methods). `return_url` required. Desktop auth via QR code (expires 1h, refreshable up to 20 times). Manual capture: 7-day window.

## Billie Details

**B2B only** — Pay in 30 days. 11 European countries. Multi-currency: EUR, SEK, NOK, DKK, GBP, CHF. No stated maximum; minimum 0.01 EUR.

**Include `line_items`** in integration to improve approval rates.

**Disputes**: 12-day merchant evidence window (shortest of BNPL methods). Types: fraud, double payments, amount discrepancy.

**Refunds**: 180-day window; async (up to 5 min).

**Connect**: `billie_payments` capability required on both platform AND connected accounts. Statement descriptor: direct/`on_behalf_of` → connected account; destination/SCT → platform.

**Prohibited**: gambling, country clubs, adult content, financial institutions, crypto, postal services (govt), precious metals/jewelry.

**Integration notes**: Payment terms 7–120 days (not just 30). `return_url` required. Manual capture: 7-day window. `line_items` data improves approval rates.

## Kriya Details

**B2B only** — UK only, GBP only. **No Connect support** — only BNPL method without it.

**Disputes**: 12-day evidence window.

**Refunds**: 180-day window; async (up to 5 min).

**Prohibited** (~36 categories, most extensive of any BNPL): travel agencies, hotels, airlines, insurance, gambling, crypto, advertising, drugs, financial institutions, political/religious organizations, charities, and many more.

**Integration notes**: `return_url` required. Manual capture: 7-day window.

## Zip Details

**Consumer BNPL** — AU and US. AUD/USD. **Connect supported**. **No manual capture**.

**Three products**: Zip Pay (AU, up to $1k AUD, flexible repayment), Zip Money (AU, $1k-$50k AUD, up to 36-month interest-free), Zip Pay In 4 (US, $35-$1.5k USD, 4 installments over 6 weeks).

**Disputes**: 180-day customer window. Unique: customer must contact merchant first — **14-day direct resolution** before escalating to Zip. Zip covers fraud losses.

**Refunds**: 180-day window.

**Additional requirements**: delivery within 60 days; retain records 18 months; no surcharging. US: goods must be in US; no gift cards.

**Integration notes**: `return_url` required. No manual capture. Checkout recommended — Direct API uses `stripe.confirmZipPayment()` which is **deprecated** (Stripe may end support).

## Sunbit Details

**Consumer BNPL** — US only, USD only. Pay in 3, 6, 12, or 18 monthly installments. **Connect supported** (`sunbit_payments` capability). **No manual capture**.

**Transaction limits**: min $60, max ~$20,000.

**Disputes**: 12-day evidence window.

**Refunds**: 180-day window; async (up to 5 min).

**Prohibited categories**: ~175 (general retail, services, digital goods, restaurants, travel, healthcare — very broad).

**Additional requirements**: no surcharging; financed amount ≤ price of goods delivered.

**Integration notes**: `return_url` required. No manual capture. $60–$20k enforced in Checkout Session.

## SeQura Details

**Consumer BNPL** — Spain (ES) only, EUR only. Pay in 3 interest-free or up to 12 installments. **No Connect support**.

**Transaction limits**: min €29. No stated maximum.

**Disputes**: 12-day evidence window.

**Refunds**: 180-day window; async (up to 5 min).

**Prohibited categories**: ~160+ categories — the most extensive prohibited list of any payment method on Stripe. Includes restaurants, doctors, legal services, marketplaces, digital goods, bakeries, and many everyday categories.

**Integration notes**: Payment terms 7–120 days (flexible, not fixed installments). `return_url` required. Manual capture: 7-day window.

## Scalapay Details

**Consumer BNPL** — Pay in 3 or 4 installments. **EUR only** across all 28 merchant countries (including US, AU, CA, SG). **No Connect support**.

**Transaction limits**: min €5, max ~€5,000.

**Allowed categories**: "At discretion of Scalapay" — no published list; approval-based (vs other B2B BNPL's long prohibited lists).

**Disputes**: 12-day evidence window.

**Refunds**: **90-day** window (shorter than Billie/Kriya/Mondu's 180 days); async (up to 5 min).

**Integration notes**: `return_url` required. Manual capture: 7-day window. Checkout path limited to 8 EU countries (IT, FR, ES, DE, NL, BE, IE, FI) despite 28-country merchant base.

## Payment on Invoice Details

**Consumer BNPL for Germany/Austria** (not B2B). EUR only. DE merchant accounts only.

**14-day customer payment terms** — Stripe sends branded invoice to customer after approval. Merchant paid immediately (immediate notification).

**Risk-based approval**: buyer provides name, email, address, date of birth; risk assessment determines approval.

**Payout timing**: T+2 minimum. Connect: Yes. Manual capture: Yes.

## Mondu Details

**B2B only** — Pay in 30 days. EU/UK, 14 merchant countries. Multi-currency: EUR, CHF, GBP. **No Connect support**.

**Maximum**: ~€20,000 EUR. No stated minimum.

**Disputes**: 12-day evidence window.

**Refunds**: 180-day window; async (up to 5 min).

**Prohibited** (~90 categories, most extensive of any payment method): transportation, cleaning/repair services, gambling, healthcare, government services, chemicals, fuel, utilities, crypto, pawn shops, timeshares, and many more.

**Integration notes**: `return_url` required. Manual capture: 7-day window. EUR only for Checkout integration path.

## Klarna Details

**Coverage**: 23 customer countries, 32 merchant countries, 13 currencies. Broadest BNPL on Stripe. **Klarna takes loss liability** if customer can't repay.

**No B2B** — explicitly prohibited. Also prohibited: charities and political organizations.

**UK FCA**: must use Klarna-approved messaging for BNPL advertising — non-compliance can result in **criminal charges**. PMME auto-handles this.

**Termination**: Klarna can terminate for prohibited categories or high dispute rates.

**AU DDO**: active promoters of Pay in 4 in Australia are "distributors" — must follow TMD, report under-18 purchases and harm complaints.

**4 payment options**: Pay in full (immediate, most countries), Pay later (30 days, ~20 countries), Pay in 3 or 4 (interest-free installments), Financing (up to 36 months, AT/CA/DE/FI/GB/NO/SE/US).

**Recurring payments**: Pay in full, Pay later, Pay in 3 or 4 support subscriptions (country restrictions apply). Not available with `setup_future_usage`.

**Cross-border**: EEA ↔ EEA/CH/UK allowed in customer's local currency. Non-EEA (AU, CA, NZ, US) must sell domestically.

**Refunds**: 180-day window; 5-7 business days. Partial refunds spread evenly across remaining installments. Blocked during active disputes.

**Disputes**: 180-day window (longest BNPL). Two-stage: Inquiry (21 days, no evidence, resolve directly) → Chargeback (evidence accepted, fee reversed if merchant wins). Fraud disputes skip inquiry. Evidence deadline: 12 days standard, **5 days for fraud**. One round of evidence only. `charge.dispute.funds_withdrawn` webhook marks escalation.

**Connect**: all charge types. `klarna_payments` capability for Express/Custom accounts.

**Integration notes**: Prefill billing details via `payment_method_options.klarna` to improve conversion. Manual capture supported. Test with amount `3500` (local currency) to exercise all options except Financing.

**Conversion tips**: Place Express Checkout Element early. Add Payment Method Messaging on product pages. Pass payment line items (Checkout does this automatically) and optional shipping/billing address to improve Klarna fraud scoring.

**Supplementary purchase data** (public preview, API header `2025-11-17.preview`): pass `payment_method_options.klarna.supplementary_purchase_data` with vertical-specific data (events, insurance, vouchers, train, bus, ferry, organized trips, marketplace sellers) to improve acceptance rates and fraud assessment. No fee impact; no validation feedback.

**Recurring/save**: Use SetupIntent or Checkout `mode: 'setup'` to save. Subscription `reference` must be identical across setup and all renewals — mismatch causes error. Send `payment_method_options.klarna.subscriptions` to unlock Pay in 3/4 for subscriptions. For on-demand, pass `klarna.on_demand` metadata to improve underwriting. Listen for `mandate.updated` webhook to handle Klarna-side revocations.

## Affirm Repayment Options

Pay in 4 interest-free installments or monthly payments up to 36 months. Max credit limit $20k USD/CAD; transactions up to $30k require customer down payment.

## Integration

Use Dynamic Payment Methods (enabled by default) via Checkout, Payment Element, or hosted Invoice page. No individual integration required per method. **Payment Method Messaging Element** (PMME) recommended for on-site BNPL messaging — dynamically shows relevant options. The legacy `affirmMessage` Element (Affirm-only) is deprecated in the latest Stripe.js.

## Sources

- [[source-stripe-bnpl-overview]] — product/API/transaction support matrices for 11 BNPL methods
- [[source-stripe-affirm]] — Affirm deep-dive: financing packages, payment tiers, refunds, disputes, prohibited categories, Connect requirements
- [[source-stripe-affirm-accept-payment]] — Affirm integration: 3 paths, Checkout constraints, 12-hour expiry, error codes, shipping tip
- [[source-stripe-affirm-messaging]] — Legacy affirmMessage Element (deprecated); use Payment Method Messaging Element instead
- [[source-stripe-afterpay-clearpay]] — Afterpay/Clearpay: Cash App rebrand, country limits, US installment tiers, dispute/refund windows, prohibited categories
- [[source-stripe-afterpay-clearpay-accept-payment]] — Afterpay integration: 3-hour expiry, billing_details required, 3 paths, shipping tip
- [[source-stripe-afterpay-clearpay-messaging]] — Legacy afterpayClearpayMessage Element (deprecated); auto-localizes to Clearpay for UK locale
- [[source-stripe-alma]] — Alma: EUR only, T+3 payout, marketplace-only Connect, 25-day dispute, required customer terms
- [[source-stripe-alma-accept-payment]] — Alma integration: 1-hour expiry, QR code desktop auth (20 refreshes), return_url required, 7-day manual capture
- [[source-stripe-billie]] — Billie: B2B Pay-in-30, multi-currency EU, 12-day dispute window, billie_payments capability
- [[source-stripe-billie-accept-payment]] — Billie integration: 7-120 day terms, return_url required, 7-day manual capture, line_items tip
- [[source-stripe-klarna]] — Klarna: 4 payment options, 23 countries, cross-border rules, loss liability, refund mechanics, Connect
- [[source-stripe-klarna-accept-payment]] — Klarna integration: billing prefill, manual capture, per-country test data (23 countries), iOS webview
- [[source-stripe-klarna-set-up-future-payments]] — Klarna save/recurring: subscription reference consistency, on_demand metadata, mandate revocation
- [[source-stripe-klarna-best-practices]] — Klarna conversion: Express Checkout placement, PMME on product pages, line items, shipping/billing for fraud
- [[source-stripe-klarna-compliance]] — Klarna compliance: prohibited categories, UK FCA criminal risk, termination rights, AU DDO
- [[source-stripe-klarna-disputes]] — Klarna disputes: 180-day window, inquiry→chargeback 2-stage, fee model, 5-day fraud evidence, 23-country test triggers
- [[source-stripe-klarna-supplementary-data]] — Klarna supplementary data (preview): 8 verticals, acceptance/fraud improvement, update semantics
- [[source-stripe-kriya]] — Kriya: B2B UK-only, no Connect, most extensive prohibited list (~36 categories), 12-day dispute window
- [[source-stripe-kriya-accept-payment]] — Kriya integration: return_url required, 7-day manual capture
- [[source-stripe-mondu]] — Mondu: B2B Pay-in-30, 14 EU/UK countries, multi-currency, no Connect, ~90 prohibited categories
- [[source-stripe-mondu-accept-payment]] — Mondu integration: return_url required, 7-day manual capture, EUR-only Checkout path
- [[source-stripe-payment-on-invoice]] — Payment on invoice: consumer BNPL DE/AT, 14-day terms, risk-based, branded invoice, T+2 payout
- [[source-stripe-scalapay]] — Scalapay: consumer BNPL, EUR-only (all 28 countries), 90-day refund window, approval-based categories
- [[source-stripe-scalapay-accept-payment]] — Scalapay integration: return_url required, 7-day capture, Checkout limited to 8 EU countries
- [[source-stripe-sequra]] — SeQura: consumer BNPL Spain-only, Pay in 3/12, most extensive prohibited list (~160+ categories)
- [[source-stripe-sequra-accept-payment]] — SeQura integration: 7-120 day terms, return_url required, 7-day manual capture
- [[source-stripe-sunbit]] — Sunbit: US-only, 3/6/12/18-month installments, Connect supported, no manual capture, $60-$20k
- [[source-stripe-sunbit-accept-payment]] — Sunbit integration: return_url required, no manual capture, $60-$20k Checkout enforcement
- [[source-stripe-zip]] — Zip: AU+US, 3 products (Zip Pay/Money/Pay-in-4), 14-day direct resolution, 180-day disputes/refunds
- [[source-stripe-zip-accept-payment]] — Zip integration: return_url required, no manual capture, Direct API deprecated (confirmZipPayment)
