---
title: "Stripe Managed Payments"
type: concept
category: technology
tags: [stripe, managed-payments, merchant-of-record, tax-compliance, digital-goods, saas, fraud, disputes]
---

## Definition

Stripe Managed Payments is Stripe's **merchant of record (MoR)** solution for selling digital products globally. When using Managed Payments, Stripe (not your business) is the legal merchant responsible for indirect tax compliance, fraud prevention, dispute management, and transaction-level customer support.

## Who It's For

Businesses selling digital products:
- SaaS, IaaS, PaaS
- Software (downloadable, subscription)
- Digital media (audiobooks, ebooks, magazines, newspapers, audio/video, images)
- Online courses and training (self-study, on-demand)
- Electronically supplied business/web services (website hosting)

Not suitable for physical goods, professional services, live events, platforms/marketplaces, or Connect integrations.

**Critical**: product must be **fully automated** — human intervention (e.g., live 1-1 coaching) disqualifies it. If Stripe deems ineligible post-approval, you bear indirect tax liability and must stop using Managed Payments for that product.

## Eligibility: Business Locations (39 countries as of April 2026)

**North America**: CA, US

**Europe** (32): AT, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GI, GR, HR, HU, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK

**Asia Pacific**: AU, HK, JP, SG

## Buyer Countries

195+ countries except 9 restricted: China, Russia, Cuba, Iran, North Korea, Syria, Ascension Island, Kosovo, Tristan da Cunha.

## Tax Code Requirement

Must assign an eligible `txcd_` code (60+ available) to each product. Key categories: IaaS/PaaS/SaaS, video games, downloadable software, digital books/magazines/newspapers/audio/video, online courses, website hosting. See [[source-stripe-managed-payments-eligibility]] for full table.

**US note**: business/personal use distinction on tax codes only relevant for US sales.

## Ongoing Performance Requirements

- Low dispute rate required; Stripe can issue refunds within **60 days** to reduce chargebacks
- Stripe applies regional consumer protection requirements (cooling off periods, etc.)

## Tax Coverage Details

**Domestic exceptions** (seller responsible):
- **Japan**: ALL domestic transactions
- **Singapore B2B**: buyer self-identifies as business at checkout

**Cross-border**: ~81 countries across Africa, APAC, Europe (EU + non-EU), LatAm/Caribbean, North America — Stripe handles everything automatically.

**Unsupported countries**: Stripe Tax is the **only compatible tax solution** — third-party providers not supported. Stripe Tax calculation fees are free on Managed Payments transactions.

**Serbia**: cross-border only for sellers NOT VAT-registered in Serbia.

## What Stripe Handles (vs Regular Stripe)

| Responsibility | Managed Payments | Regular Stripe |
| --- | --- | --- |
| Indirect tax (sales tax, VAT, GST) | Stripe (80+ countries) | Your business (optional Stripe Tax) |
| Fraud prevention | Stripe | Your business (optional Radar) |
| Dispute management | Stripe | Your business |
| Transaction-level support | Stripe | Your business |
| Merchant of record | Stripe | Your business |

## Integration Paths

| Path | Notes |
| --- | --- |
| New Checkout integration | Build from scratch with Managed Payments enabled |
| Update existing Checkout | Add Managed Payments to existing integration |
| Payment Links | No-code option with Managed Payments enabled |
| Mobile app payments | Accept payments via mobile app |

## Limitations

**Unsupported**:
- Stripe Connect (platform/marketplace integrations)
- Elements / embeddable web components / advanced integrations
- Invoice items on Customer object attached to Managed Payments subscription
- One-off invoices outside billing period
- Creating subscriptions outside Checkout or Payment Links
- Third-party tax integrations

## Customer Experience: Link as MoR

Customers see **"Sold through Link"** as the merchant — statement shows `LINK.COM* [descriptor]`. Receipts/invoices sent from Link (your Dashboard receipt settings don't apply). Customers manage orders via link.com.

**48-hour support rule**: if Stripe escalates a support request and you don't respond within 48 hours, Stripe may issue a refund without your approval.

**Refund tax note**: refunds include full tax amount to customer, but Stripe retains + remits original sales tax in certain jurisdictions → your account balance reduced by that tax amount.

## Payment Methods (Key Highlights)

Global: Cards, Apple Pay, Google Pay, Link (all plans, no local currency required)
- Klarna: global but **one-time only** with Managed Payments
- Cash App Pay/Afterpay: US only
- Korean methods (Kakao/Naver/Samsung Pay/PAYCO): South Korea only
- UPI: India; Pix: Brazil (no daily subscriptions); Bancontact: Belgium

## Key Distinction from Stripe Tax

Stripe Tax makes *your business* the merchant that collects and remits taxes. Managed Payments makes *Stripe* the merchant — Stripe is the legal entity responsible for tax compliance.

## Key Players

- [[stripe]] — provides the Managed Payments MoR solution

## Sources

- [[source-stripe-managed-payments-overview]] — overview: MoR definition, comparison table, integration paths, unsupported integrations
- [[source-stripe-managed-payments-eligibility]] — eligibility: ~38 supported business countries, 60+ tax codes, 195+ buyer countries (9 restricted), ongoing performance requirements
- [[source-stripe-managed-payments-tax-compliance]] — tax coverage: 80+ countries auto-handled, Japan/Singapore B2B exceptions, Stripe Tax only for unsupported countries (free), Serbia VAT caveat
- [[source-stripe-managed-payments-how-it-works]] — operational details: Link as customer MoR, 48h response rule, refund tax handling, subscription email schedule, payment methods table, data deletion
- [[source-stripe-managed-payments-changelog]] — timeline: GA 2026-04-22 (39 countries), one-time/in-app payments (Sep 2025), Adaptive Pricing + subscription schedules (Feb 2026), Radar support (Aug 2025)
- [[source-stripe-managed-payments-setup]] — Checkout integration: managed_payments.enabled param, API version 2025-03-31.basil required, all-products-eligible rule, tax behavior, webhooks
- [[source-stripe-managed-payments-update-checkout]] — Migration guide: existing subscriptions NOT eligible (new only); unsupported params tables for subscriptions + one-time payments
- [[source-stripe-managed-payments-mobile]] — iOS mobile integration: managed_payments.enabled + origin_context=mobile_app together; MoR alternative to non-MoR app-to-web; Universal Links + Safari
- [[source-stripe-managed-payments-payment-links]] — Payment Links: managed_payments.enabled on paymentLinks.create(), immutable MoR state, iOS app restriction, variable pricing, up to 20 line items
