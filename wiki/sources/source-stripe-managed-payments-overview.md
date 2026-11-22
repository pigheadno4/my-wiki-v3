---
title: "Managed Payments — Overview"
type: source
date_ingested: 2026-04-23
date_updated: 2026-11-22
original_format: notes
canonical_url: "https://docs.stripe.com/payments/managed-payments"
raw_files:
  - "stripe-payments-managed-payments-2026-11-07.md"
  - "stripe-managed-payments-overview-2025.md"
tags: [stripe, managed-payments, merchant-of-record, tax-compliance, digital-goods, saas, fraud, disputes]
---

## Summary

The April 23 and November 7, 2026 overviews describe Managed Payments as Stripe's merchant-of-record service for eligible digital products such as SaaS, software, and digital content or downloads. Stripe manages covered indirect tax, fraud prevention, disputes, and transaction-level customer support. The separate [[source-stripe-managed-payments-how-it-works]] guide identifies “Sold through Link” as the customer-facing checkout, receipt, and transaction support identity. The seller retains product support.

## Tax coverage and merchant eligibility

The November overview lists sales tax, VAT, and GST coverage for transactions in more than 80 countries. The companion [[source-stripe-managed-payments-tax-compliance]] guide assigns indirect tax compliance on all domestic sales to Japan-based sellers. For Singapore-based sellers the domestic exception covers B2B sales when the buyer identifies the purchase as business at checkout. Sellers remain responsible where Stripe cannot assume tax compliance. The guide identifies Stripe Tax as the compatible solution for those sales and says Stripe Tax calculation has no additional charge on Managed Payments transactions.

The April 22, 2026 [[source-stripe-managed-payments-changelog]] milestone gives a separate figure of 39 countries for merchant general availability, including new support for Australia. The [[source-stripe-managed-payments-eligibility]] guide separately requires a direct integration, Stripe review, a supported business location, and eligible products and transactions. Sell directly to customers, hold the necessary distribution rights, and assign eligible Product tax codes. The digital product itself must be fully automated. A service that involves human intervention, such as live one-to-one coaching, is ineligible. A tax-coverage or general-availability count supplies no individual approval or transaction result.

## November comparison with other Stripe products

| Feature | Managed Payments | Other Stripe products |
| --- | --- | --- |
| Merchant of record | Stripe | Your business |
| Indirect tax compliance | Supported for covered transactions | Available with Stripe Tax |
| Checkout page | Stripe Checkout and Payment Links | Checkout, Elements, hosted invoice page, and Payment Links |
| Subscriptions | Available with Billing | Available with Billing |
| Fraud prevention | Supported | Available with Radar |
| Dispute response | Supported | Available with Payments |
| Transaction-level customer support | Supported | Unsupported in this comparison |
| Platforms | Unsupported | Available with Connect |

The April table left the Managed Payments fraud, dispute, and platform cells blank, and left other-products transaction support blank. April's overview prose already assigned fraud and dispute handling to Stripe and excluded Connect. November makes those labels explicit and lists other-products transaction-level support as unsupported in this comparison. The labels document the comparison's scope.

## Integration paths

- **New Checkout**. Build a [[source-stripe-managed-payments-setup|new Checkout integration]] with Managed Payments enabled.
- **Existing Checkout**. The separate November [[source-stripe-managed-payments-update-checkout|migration guide]] covers a hosted or full embedded Checkout page that creates Checkout Sessions server-side in `payment` or `subscription` mode. It requires API version `2025-03-31.basil` or later, Dashboard enablement, and eligible products. Only new subscriptions purchased through a Managed Payments Checkout Session are eligible for that migration path. Embedded Checkout is different from the unsupported Elements and other advanced embeddable component flows.
- **Payment Links**. Use [[source-stripe-managed-payments-payment-links|Payment Links with Managed Payments]] for eligible digital products.
- **Mobile app payments**. The separate [[source-stripe-managed-payments-mobile|mobile guide]] describes opening Stripe-hosted Checkout in a browser from an iOS app in supported markets, for eligible digital products and subscriptions. It describes an app-to-web path. The overview link gives no native Elements or platform-rollout evidence.

## Unsupported integrations and invoice operations

- Stripe Connect platforms and marketplaces.
- Elements-based embeddable web components and other advanced payment integrations.
- Attaching invoice items on a `Customer` object to a Managed Payments subscription.
- Generating a one-off invoice on a `Customer` object, or generating one for a Managed Payments subscription outside its billing period.
- Creating subscriptions outside Checkout or Payment Links.
- Third-party tax integrations.

Read these restrictions alongside the dated [[source-stripe-managed-payments-changelog]] operations. On April 22, Stripe documented adding Invoice Items or Invoice Line Items in eligible product categories to invoices for Managed Payments subscriptions, and adding eligible Subscription Items to the subscriptions. Those are specific targets. The Customer-object attachment and one-off invoice restrictions still apply.

On October 5, 2026 Stripe documented Pay Invoice support to finalize and attempt payment on a Managed Payments invoice using the payment method already associated with that invoice. The request cannot supply a different method or other payment-related parameters. This is an attempt on an existing invoice. Confirm payment separately and keep this operation distinct from invoice creation or item attachment.

## Related Pages

- [[stripe]] — Stripe company page
- [[stripe-managed-payments]] — concept and dated account, tax, integration, and operation scope
- [[source-stripe-managed-payments-eligibility]] — business and Product eligibility
- [[source-stripe-managed-payments-tax-compliance]] — domestic and cross-border tax predicates
- [[source-stripe-managed-payments-how-it-works]] — Link identity and transaction support
- [[source-stripe-managed-payments-changelog]] — dated invoice operations and availability milestones

## Raw Sources

- [[raw/stripe-payments-managed-payments-2026-11-07]] — complete November 7, 2026 overview
- [[raw/stripe-managed-payments-overview-2025]] — April 23, 2026 historical overview, reformatted from the pasted navigation page
