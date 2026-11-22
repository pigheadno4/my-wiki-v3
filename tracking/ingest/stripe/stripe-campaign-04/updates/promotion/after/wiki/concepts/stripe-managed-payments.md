---
title: "Stripe Managed Payments"
type: concept
category: technology
tags: [stripe, managed-payments, merchant-of-record, tax-compliance, digital-goods, saas, fraud, disputes]
---

## Definition

Stripe Managed Payments is Stripe’s **merchant of record (MoR)** solution for eligible digital-product sales. Stripe handles fraud prevention, disputes and transaction-level customer support, and handles indirect taxes on covered sales where required. See the tax-coverage and seller-responsibility exceptions below.

## Who It's For

Businesses selling digital products:
- SaaS, IaaS, PaaS
- Software (downloadable, subscription)
- Digital media (audiobooks, ebooks, magazines, newspapers, audio/video, images)
- Online courses and training (self-study, on-demand)
- Electronically supplied business/web services (website hosting)

Managed Payments excludes physical goods, professional services, live in-person events, Connect platforms, Express accounts, and accounts controlled by a platform. Listed Digital Audio Visual Works codes can cover live-event content distributed as fully automated digital downloads, streams, or bundles. See [[source-stripe-managed-payments-eligibility]] for the specific code definitions.

For each eligible digital product, sell directly to customers, hold the necessary distribution rights and licences, and provide fully automated delivery. Live intervention such as one-to-one coaching disqualifies the service. If Stripe determines that a product is ineligible, the merchant must stop using Managed Payments for it and take responsibility for its indirect tax liability.

## Business Location Eligibility

Stripe reviews business type and geography for direct integrations. The November 7, 2026 [[source-stripe-managed-payments-eligibility]] capture lists 37 business locations.

**North America**: CA, US

**Europe**: AT, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK

**Asia Pacific**: AU, HK, JP, SG

The April 23, 2026 eligibility capture lists 38 entries, including Gibraltar. The [[source-stripe-managed-payments-changelog]] separately reports 39 countries at the April 22 general-availability milestone. November's [[source-stripe-managed-payments-tax-compliance]] capture still lists Gibraltar for cross-border sales to customers there. The dated lists give no effective change date or account-specific treatment.

## Buyer Countries

195+ countries except 9 restricted: China, Russia, Cuba, Iran, North Korea, Syria, Ascension Island, Kosovo, Tristan da Cunha.

## Tax Code Requirement

Assign an eligible `txcd_` code to each Product through the Dashboard or API for sales through Checkout Sessions or Payment Links. Key categories include IaaS, PaaS, SaaS, video games, downloadable software, digital publications and media, online courses, and website hosting. The June 2, 2026 [[source-stripe-managed-payments-changelog|changelog entry]] adds four AIaaS codes. The [[source-stripe-managed-payments-eligibility|eligibility tables]] list 73 codes in April and 76 in November. November omits April’s Website Advertising code (`txcd_10701000`) and excludes data brokering from four specific information-service definitions. Withdrawal timing and grandfathering remain undetermined.

**US note**: business/personal use distinction on tax codes only relevant for US sales.

## Ongoing Performance Requirements

- Maintain a low historical dispute rate and have no prior risk issues. Stripe can issue refunds within **60 days** of purchase in certain cases, including to help reduce chargebacks.
- Stripe applies regional consumer protection requirements (cooling off periods, etc.)

## Tax Coverage Details

**Domestic exceptions** (seller responsible):
- **Japan**: ALL domestic transactions
- **Singapore B2B**: buyer self-identifies as business at checkout

**Cross-border tax coverage** — the April and November guides list 82 destinations, including 27 EU codes and conditional Serbia. The codes describe covered digital-product sales and are separate from seller eligibility. In November, a local volume or sales threshold can result in `taxability_reason: not_subject_to_tax` on a supported transaction while Stripe retains indirect-tax responsibility.

**Seller-responsible taxes** — where Managed Payments cannot assume indirect-tax liability, the seller remains responsible for registration, calculation, collection, filing and remittance. Managed Payments can remain MoR for payments, fraud prevention, disputes and support. Stripe Tax is the sole compatible integrated solution and has no additional calculation fee on Managed Payments transactions. Enable it under Settings → Tax → Integrations and upload the registration on the Tax page to start automatic calculation and collection. Optional partners support registration, filing and remittance through that workflow.

**Serbia**: cross-border only for sellers NOT VAT-registered in Serbia.

## What Stripe Handles (vs Regular Stripe)

| Responsibility | Managed Payments | Regular Stripe |
| --- | --- | --- |
| Indirect tax (sales tax, VAT, GST) | Stripe on covered digital-product sales where required. Seller responsibility applies in the documented exceptions. | Your business (optional Stripe Tax) |
| Fraud prevention | Stripe | Your business (optional Radar) |
| Dispute management | Stripe reviews disputes and may counter or accept. The merchant pays the dispute-received fee and any charges for enabled prevention tools. Stripe covers the evidence-submission fee when it submits evidence. The merchant pays that fee if it counters directly. See [[source-stripe-managed-payments-how-it-works]] for the dated April Smart Disputes guidance and November workflow. | Your business |
| Transaction-level support | Stripe | Your business |
| Merchant of record | Stripe | Your business |

## Integration Paths

| Path | Notes |
| --- | --- |
| New Checkout integration | Build from scratch with Managed Payments enabled |
| Update existing Checkout | Add Managed Payments to existing integration |
| Payment Links | No-code option with Managed Payments enabled |
| Mobile app payments | For eligible iOS external links, create a Checkout Session on the server and open its URL in Safari. The older in-app wording describes the historical changelog entry. See [[source-stripe-managed-payments-mobile]] and [[source-stripe-managed-payments-changelog]]. |

## Limitations

**Unsupported**:
- Stripe Connect (platform/marketplace integrations)
- Checkout Elements (`ui_mode: elements`) and advanced custom integrations. The April and November 2026 [[source-stripe-managed-payments-update-checkout|Managed Payments migration guide]] separately covers eligible existing hosted and embedded Checkout pages in payment or subscription mode. Its examples set `success_url` and omit `ui_mode`. Use the embedded Checkout Session return contract for `embedded_page`.
- Attaching Invoice Items on a `Customer` object to a Managed Payments subscription.
  The April 22, 2026 changelog allows adding eligible Invoice Items and Invoice Line Items directly to invoices for Managed Payments subscriptions.
- Generating one-off invoices on a `Customer` object or outside a subscription’s billing period.
  The October 5 entry allows finalizing and attempting payment on an existing Managed Payments invoice using its associated payment method. Payment overrides and other payment-related parameters are unavailable for that request. See [[source-stripe-managed-payments-changelog]].
- Creating subscriptions outside Checkout or Payment Links
- Third-party tax integrations
- Custom domains on Managed Payments checkouts. Merchant terms of service and privacy policy links can still be configured.

## Customer Experience: Link as MoR

Customers see **“Sold through Link”** as the merchant, and the statement shows `LINK.COM* [descriptor]`. Link sends receipts and invoices, and Dashboard receipt settings do not control those emails. For seller-responsible tax transactions, the invoice displays the seller’s business name and tax details as configured in Invoice Settings. The separate receipt email and PDF carry Sold through Link details. Customers manage orders via link.com.

**48-hour support rule**: if Stripe escalates a support request and you don't respond within 48 hours, Stripe may issue a refund without your approval.

**Refund tax note**: the customer receives the full refund including tax. In certain jurisdictions Stripe must retain and remit the original sales tax, and the seller's balance is reduced by that amount.

Link sends transaction receipts independently of Dashboard receipt settings. Link also sends separate subscription emails. With **Upcoming renewals** enabled, the November guide sends notices before every renewal. With the setting disabled, anniversary notices still apply. See [[source-stripe-managed-payments-how-it-works]] for the country branches, the November 15-day default and seven-day floor, and the April capture's historical cadence wording.

For subscriptions created by Managed Payments-enabled Checkout Sessions, the November guide disallows direct API updates to `subscription.default_payment_method`. Customers can update it through the Customer Portal.

## Payment Methods (Key Highlights)

The November 7, 2026 Managed Payments matrix lists cards, Apple Pay, Google Pay, and Link as global, with one-time and recurring payments and no local currency requirement.
- Klarna: US, one-time only. April listed global one-time support. The separate Klarna recurring Checkout path applies to sessions without Managed Payments.
- Bancontact: Belgium, one-time only. April also listed recurring support. The general generated-SEPA route does not establish Managed Payments recurring support.
- Cash App Pay and Afterpay: US. The listed Korean methods are scoped to South Korea, UPI to India, and Pix to Brazil with no daily subscriptions.

See [[source-stripe-managed-payments-how-it-works]] for both dated matrices, local presentment and Adaptive Pricing columns, and method configuration scope.

## Key Distinction from Stripe Tax

Stripe Tax helps the seller calculate and collect taxes. Managed Payments can take on indirect-tax compliance for covered sales as part of its MoR service. When Stripe cannot assume indirect-tax liability, the seller remains responsible even if Managed Payments still provides MoR and transaction operations.

## Key Players

- [[stripe]] — provides the Managed Payments MoR solution

## Sources

- [[source-stripe-managed-payments-overview]] — April and November 2026 overviews cover Stripe as merchant of record, the fraud/dispute/platform comparison, integration route labels, and restrictions. Linked companion guides document Link's customer-facing identity, the hosted and embedded Checkout migration, iOS-to-browser Checkout, and the dated invoice allowances.
- [[source-stripe-managed-payments-eligibility]] — November 2026 lists 37 merchant business locations and 76 Product tax codes. Covers direct sale, fully automated digital delivery, customer restrictions, and ongoing eligibility.
- [[source-stripe-managed-payments-tax-compliance]] — April and November 2026 tax guidance. Transaction tax coverage exceeds 80 countries. The 39-country April 2026 merchant GA milestone is a separate measure. Japan-based sellers remain responsible for indirect tax on all domestic sales. Singapore-based sellers remain responsible for domestic B2B sales when the customer identifies as a business at checkout. Where Managed Payments cannot assume the tax liability, Stripe Tax is the only compatible solution. Managed Payments transactions incur no additional fee for Stripe Tax calculation. See the dated guide for setup, Serbia VAT scope, and the invoice and receipt identity.
- [[source-stripe-managed-payments-how-it-works]] — April and November 2026 operational captures: Link support, conditional refunds and escalation, renewal-setting branches, dispute fees, dated method matrices, tax reporting, and acquiring affiliates
- [[source-stripe-managed-payments-changelog]] — timeline: GA 2026-04-22 (39 countries), one-time/in-app payments (Sep 2025), Adaptive Pricing + subscription schedules (Feb 2026), Radar support (Aug 2025)
- [[source-stripe-managed-payments-setup]] — New Stripe-hosted Checkout setup, API `2025-03-31.basil` or later. April 23, 2026 requires all purchased products to be eligible for Managed Payments processing. November 7, 2026 calls for product eligibility and documents the per-Session opt-out.
- [[source-stripe-managed-payments-update-checkout]] — April and November 2026 migration guides for hosted or embedded Checkout, with mode-specific removal lists. Subscription migration applies to new subscriptions purchased through a Managed Payments Checkout Session. The older one-time table excludes two future-usage fields. The September 3, 2026 [[source-stripe-managed-payments-changelog|changelog entry]] documents `payment_intent_data.setup_future_usage` and `payment_method_options.{payment_method}.setup_future_usage` for creating a Managed Payments Checkout Session.
- [[source-stripe-managed-payments-mobile]] — April and November 2026 iOS hosted Checkout setup for eligible digital products, with a mapped Customer and paid server fulfillment. See the dated Dashboard terms wording and November-only price and tax display settings.
- [[source-stripe-managed-payments-payment-links]] — April/November 2026 guide to creating and sharing an eligible Managed Payments link. Create a new link to change Managed Payments state. Stripe selects methods dynamically and excludes Connect. A subscription authorizes Managed Payments charges only. Obtain separate customer consent for outside charges.
