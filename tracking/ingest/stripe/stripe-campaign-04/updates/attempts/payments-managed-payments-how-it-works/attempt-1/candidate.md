---
title: "How Managed Payments Works"
type: source
date_ingested: 2026-04-23
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/managed-payments/how-it-works"
raw_files:
  - "stripe-payments-managed-payments-how-it-works-2026-11-07.md"
  - "stripe-managed-payments-how-it-works-2025.md"
tags: [stripe, managed-payments, merchant-of-record, link, adaptive-pricing, payment-methods, transaction-support, data-deletion]
---

## Summary

Stripe acts as merchant of record for eligible digital goods sold through Checkout or Payment Links. Link is the customer-facing identity at checkout, on receipts, and in transaction support. Stripe handles covered indirect tax, fraud prevention, and disputes. The seller retains product support and responsibility for out-of-coverage tax compliance. The November 7, 2026 guide adds constraints on custom domains and direct API updates to a subscription payment method, and documents changes to renewals, disputes, method support, reports, and processing.

The separate [[source-stripe-managed-payments-setup]] guide requires eligible Products, Dashboard activation, a development environment, and API version `2025-03-31.basil` or later for its Checkout build. The separate [[source-stripe-managed-payments-payment-links]] guide applies that version floor to the Payment Links API and directs merchants to the web Dashboard for the no-code creation path. The operations guide defines no additional API floor.

## Checkout, tax, and Link

- **Covered indirect tax.** Stripe calculates and collects sales tax, VAT, or GST on covered sales to customers in more than 80 countries, then files and remits the tax. Stripe withholds the applicable amount when payment completes. For transactions where Managed Payments does not handle compliance, the seller remains responsible and can use Stripe Tax to calculate taxes at no additional charge. See [[source-stripe-managed-payments-tax-compliance]] for scope.
- **Checkout.** Customers see **Sold through Link** and can sign in to Link, create an account, or pay as a guest. Adaptive Pricing is on by default, subject to the method's local currency and Adaptive Pricing support. The checkout footer shows standardized payment terms and can include merchant terms of service and privacy policy links configured in Checkout settings. The November guide disallows custom domains on Managed Payments checkouts.
- **Statements and receipts.** The statement uses `LINK.COM* [Your statement descriptor]`. Link sends receipts and invoices with PDFs, and sends refund or credit-note notifications. Dashboard receipt settings do not control these notifications.
- **Orders and subscriptions.** Customers use Link order tools to view orders and manage subscriptions, payment methods, and billing addresses. Guests are prompted to create a Link account for these tools. The seller can also offer the Customer Portal or its own subscription management. The guide broadly permits Dashboard or API subscription updates and specifically disallows direct API updates to `subscription.default_payment_method` on subscriptions created by Managed Payments-enabled Checkout Sessions. Customers can update that field through the Customer Portal.
- **Fraud.** Stripe configures fraud rules and maintains blocklists.

## Transaction support and refunds

Link handles payment and subscription support. The seller handles product support and can respond directly or issue refunds. Stripe escalates product-specific questions using the support email under Dashboard Business details. If the seller does not respond within 48 hours after escalation, Stripe may issue a refund without the seller's approval.

Customers can ask Link for a refund. Stripe can issue a refund within 60 days of the original transaction in certain cases. A refund includes the sales tax that the customer paid. Where Stripe is required to retain and remit the original tax on a refunded transaction, the seller's balance is reduced by that amount.

## Subscription emails

Link sends a trial-start confirmation and a trial-ending reminder for trials longer than seven days. The Dashboard trial-ending setting does not affect that reminder. Subscription and email settings can control renewal, expired-card, and failed-payment emails separately from Dashboard receipt settings.

The November 7 capture describes these branches:

- **Upcoming renewals enabled.** Stripe sends an email before every renewal.
- **Upcoming renewals disabled.** Stripe still sends notices before the 6- and 12-month anniversaries for customers in Australia and the United Kingdom, and before the 12-month anniversary elsewhere. The default is 15 days before the anniversary. Configure the lead time under **Subscription and email settings › Upcoming renewal events**, with at least seven days. Shorter timing options for standard renewal reminders do not apply.

The April 23 capture also sends a notice before every renewal when the setting is enabled. With it disabled, April lists the same 6- and 12-month anniversaries for Australia and the UK, and the 12-month anniversary or timing required by local law elsewhere. April also lists 30 days before the next renewal for subscriptions renewing “monthly or less frequently,” or as required by local law, and seven days for subscriptions renewing “less frequently than monthly.” Those cadence bullets overlap. The November guide gives the anniversary schedule above. The captures establish neither a legal change nor treatment of individual existing subscriptions.

## Disputes

The November guide says Stripe uses automated tools and manual review. Stripe may accept a dispute if it expects the seller is unlikely to win. When Stripe counters, it submits evidence without requesting additional evidence from the seller.

- A received dispute incurs a dispute-received fee. Stripe also bills the merchant account for enabled prevention tools.
- Stripe covers the evidence-submission fee when it submits evidence to counter. If a merchant adds evidence in the Dashboard without submitting it, Stripe reviews it and may submit it without charging the evidence-submission fee.
- The merchant can view, accept, or counter in the Dashboard. If the merchant counters directly, the merchant incurs the evidence-submission fee.

The April 23 guide said Smart Disputes automatically submitted evidence for most disputes and merchants could submit evidence manually (April raw line 19). November describes the conditional review and fee workflow at raw lines 93–101. The November wording gives no evidence-submission rate, fee amounts, or means of determining a specific dispute outcome, and does not establish that Smart Disputes was discontinued.

## Payment method availability

The November 7 matrix applies to Managed Payments. Method visibility depends on payment-method settings, customer country, one-time or recurring use, and local presentment. When a method supports Adaptive Pricing, Stripe handles the applicable currency conversion for display.

| Method | Customer countries | One-time | Recurring | Local currency required | Adaptive Pricing |
| --- | --- | --- | --- | --- | --- |
| Cards | Global | Yes | Yes | No | Yes |
| Apple Pay | Global | Yes | Yes | No | Yes |
| Google Pay | Global | Yes | Yes | No | Yes |
| Link | Global | Yes | Yes | No | Yes |
| Klarna | US | Yes | No | Yes | No |
| Cash App Pay | US | Yes | Yes | Yes | No |
| Afterpay | US | Yes | No | Yes | No |
| Korean cards, Kakao Pay, Naver Pay | South Korea | Yes | Yes | Yes | Yes |
| Samsung Pay, PAYCO | South Korea | Yes | No | Yes | Yes |
| UPI | India | Yes | Yes | Yes | No |
| Pix | Brazil | Yes | Yes, except daily subscriptions | Yes | No |
| Bancontact | Belgium | Yes | No | Yes | Yes |

April lists Klarna as global and Bancontact in Belgium as supporting recurring payments (April raw lines 101 and 108). November lists US-only one-time Klarna and one-time Belgium Bancontact (November raw lines 115 and 122). The outside-Managed-Payments Klarna recurring path remains separate. The general Bancontact-to-SEPA flow is also separate from recurring support in this matrix. See [[stripe-managed-payments]] for the paired dates, [[stripe-klarna]] for its separately scoped subscription route, and [[stripe-bancontact]] for the separately scoped generated-SEPA route.

April calls Afterpay “Cash App Afterpay,” with the same documentation link and matrix values. Konbini and WeChat Pay are general local-method examples in both guides and are absent from both Managed Payments matrices. The tabulated conditions give no session-specific display or payment outcome.

## Reports and reconciliation

Filter Managed Payments transactions alongside other transactions in the Dashboard. The November guide says the default `fee` column combines Stripe fees and withheld tax in the **Balance Change from Activity Report**, **Payout Reconciliation Report**, and **Ending Balance Reconciliation Report**.

- `withheld_tax` is an optional column for indirect tax that Stripe withheld and remitted on the seller's behalf.
- `fee_net_of_withheld_tax` is an optional column for Stripe processing fees excluding withheld tax.

For API access, consult Stripe Reports for the fields and report versions available to the request.

## Data deletion and processing

Customers can request deletion of their information for Managed Payments transactions and the associated Link account. Stripe emails the seller when it receives the request, cancels subscriptions sold to the customer through Managed Payments, and removes the customer's data from related objects, including applicable objects on the seller account. The guide names v2 Account, Customer, PaymentMethod, Invoice, PaymentIntent, Subscription, and Charge.

The November guide lists possible payment processors among Stripe's acquiring affiliates: Stripe Payments Company, Stripe Technology Europe, Limited, Stripe Payments Canada, Ltd., Stripe Payments Singapore Pte. Ltd., and Stripe Payments Australia Pty Ltd. These are processing entities. Stripe is the merchant of record and Link is the customer-facing identity. The guide gives no affiliate assignment for a specific account or transaction.

## Related Pages

- [[stripe]] — provider and source catalog
- [[stripe-managed-payments]] — Managed Payments concept and dated method limits
- [[source-stripe-managed-payments-tax-compliance]] — coverage and seller tax responsibilities
- [[source-stripe-managed-payments-eligibility]] — Product and business location eligibility
- [[source-stripe-managed-payments-setup]] — Checkout integration
- [[source-stripe-managed-payments-update-checkout]] — update an existing Checkout integration

## Raw Sources

- [[raw/stripe-payments-managed-payments-how-it-works-2026-11-07]] — complete November 7, 2026 operational guide
- [[raw/stripe-managed-payments-how-it-works-2025]] — complete April 23, 2026 operational guide with its original checkout image
