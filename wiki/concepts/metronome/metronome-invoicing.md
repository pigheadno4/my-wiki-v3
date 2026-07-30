---
title: "Metronome Invoicing"
type: concept
category: technology
tags: [metronome, invoicing, stripe, marketplaces, erp]
---

## Definition

Metronome presents invoicing as a set of distribution-channel options rather than one mandatory delivery path. Its overview identifies native Stripe invoicing, marketplace invoicing for AWS, Azure, and GCP, and ERP-oriented invoicing and revenue workflows.

## Invoicing options

| Option | Documented scope |
| --- | --- |
| Stripe Invoicing | Native Stripe integration that can use Stripe Tax, dunning, and other Stripe product-suite capabilities. |
| Marketplace Invoicing | Out-of-the-box metering and invoice creation for AWS, Azure, and GCP marketplaces, covering all Metronome charge types without a third-party integrator. |
| ERP Invoicing | Out-of-the-box and custom ERP integrations for collection, book-closing, and revenue workflows; the overview highlights NetSuite as a native option. |

## Selection model

The overview emphasizes optionality: organizations can use simpler integrated invoicing, marketplace distribution, or ERP systems according to their contracting and revenue-process needs. It does not define invoice objects, lifecycle states, synchronization details, or integration setup; those require the linked dedicated guides.

## Calculation and timing boundary

The architecture guide orders invoice generation as usage receipt, billable-metric quantity calculation, contract pricing with base-rate-card overrides, and customer-facing invoice generation. It separately describes event-time alert evaluation, on-demand API-backed views, and cycle-close invoice finalization and delivery. The first two contexts do not establish that an invoice is finalized, and the page gives no latency, delivery, collection, retry, or failure-state guarantees.

## Event-based invoice preview

Metronome exposes `POST /v1/customers/{customer_id}/previewEvents` to calculate draft invoices from supplied usage events and the customer's current contract configuration before those events are processed. The request can replace historical usage or merge with it, and the response returns draft invoice records with totals and line items. Contracts using SQL billable metrics are excluded from this preview capability.

## Dashboard lifecycle overview

The dashboard quickstart describes a draft invoice accumulating usage during the billing period, followed by a 24-hour grace period before finalization. With a billing provider connected, it says the invoice is pushed within approximately one hour after finalization. Payment collection and paid or failed status remain the billing provider's responsibility.

## Credit and commit application

Credits and commits apply at invoice line-item level. Covered usage, its negative application line, and uncovered overage remain separate so product-level precommitted and overage spend stays attributable. A commit can record an invoiced amount without sending a downstream invoice, and scheduled commit charges can be consolidated onto a usage statement when the contract enables that behavior.

Commit edits appear immediately on draft invoices, while finalized invoices remain unchanged unless voided and regenerated. Invoice-schedule items tied to finalized invoices cannot be removed or updated, and a voided invoice's schedule item still cannot be removed. An access-schedule segment applied to a finalized invoice can be removed only after voiding that invoice.

## Threshold payment flow

Prepaid balance thresholds can gate release of a recharge commit on payment. Stripe gating can use a Stripe Billing invoice or a direct PaymentIntent. On a failed payment, the guide says the threshold configuration is disabled and a voided invoice should appear in both Metronome and Stripe; there is no automatic retry. An external payment gate leaves collection to the integrator, which must explicitly release or cancel the pending commit.

## PayGo and manual commit payment

The PayGo example configures Stripe with `send_invoice`, which emails payment instructions. It must not be interpreted as automatic card collection; the native Stripe integration states that a default payment method is required for `charge_automatically`, not generally for `send_invoice`.

A separate manual payment-gated commit flow attempts payment for a one-off commit invoice. Success releases the commit; failure voids both associated invoices, creates no commit, and is not automatically retried. A new Metronome API request is required, and this payment retry is distinct from webhook-delivery retries.

## Native Stripe invoice delivery

- Stripe connections are scoped to a Metronome environment; sandbox connects to Stripe test mode.
- Customer billing configuration selects the Stripe customer and collection method. Multi-account customer setup requires `delivery_method_id`; contract creation selects among the customer's configured providers with `billing_provider_configuration_id`, obtained from `/getCustomerBillingProviderConfigurations`.
- Adding Stripe to an existing contract does not send earlier finalized invoices retroactively.
- `charge_automatically` requires a Stripe default payment method. Stripe can wait up to one hour after `invoice.created` before attempting payment, or 72 hours when that webhook delivery fails.
- Account-level settings can leave invoices as drafts, skip invoices below the currency minimum, adjust presentation, or align `effective_at` to the service period. The guide says that alignment is incompatible with Stripe Tax.

Metronome receives Stripe invoice-status changes through webhooks and exposes mapped external status through its invoice API and data export. No external status appears in Metronome when the integration deliberately leaves the Stripe invoice as a draft.

For Stripe Tax, Metronome supplies the linked customer and product mapping, and Stripe calculates tax when the invoice is finalized. Retaining Stripe invoices as drafts defers calculation until manual finalization. Collection method controls what happens after finalization and is independent of whether tax is applied.

## Scheduled provider routing

Scheduled and commit charges can optionally consolidate onto a usage invoice when the exclusive service-period end day matches the scheduled invoice date and the usage invoice has not finalized. Metronome reevaluates this at contract creation and later changes; this does not make the creation-time consolidation setting editable.

A customer-level provider configuration does not itself route an invoice; a contract must select it. The customer-provisioning guide says archiving an attached configuration immediately stops billing to that destination and prevents provisioning a replacement on the active contract. This archival behavior is beta.

A contract can schedule invoice routing among Stripe, NetSuite, and AWS, Azure, or GCP Marketplace. A current-period Stripe or NetSuite correction can reroute a draft invoice, but it does not reroute an invoice already finalized and sent; Metronome states that each invoice is delivered exactly once. Marketplace transitions begin only with the next billing period.

> [!warning] Documentation ambiguity
> The provider-change guide first selects a schedule segment relative to service-period end or `issued~at`, then says each invoice maps by service-period start. It does not reconcile those timing formulations.

## Stripe representation limits

Decimal quantities are moved into descriptions while Stripe line-item quantities become `1`; invoices over 250 line items collapse into one Stripe item. The guide also documents a maximum-charge error and no native Stripe credit-memo support. These transformations mean the Metronome invoice remains the detailed billing record when Stripe representation is compressed.

## Related

- Company: [[metronome]]
- Usage-billing context: [[metronome-usage-based-billing]]
- Related platform: [[stripe]]

## Sources

- [[source-metronome-guides-invoices-overview]] — Stripe, marketplace, and ERP invoicing options
- [[source-metronome-api-reference-invoices-preview-events]] — draft-invoice previews calculated from proposed usage events
- [[source-metronome-integrations-invoice-integrations-stripe]] — Stripe routing, settings, status synchronization, payment timing, and representation limits
- [[source-metronome-guides-get-started-metronome-dashboard-quickstart]] — draft, finalization, provider-delivery, and collection boundary
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]] — balance application, downstream-invoice suppression, and consolidation
- [[source-metronome-api-reference-credits-and-commits-edit-a-commit]] — draft reflection and finalized or voided schedule constraints
- [[source-metronome-guides-customers-billing-optimize-customer-experience-prepaid-balance-thresholds]] — gated recharge, failed-payment invoices, and external release flow
- [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]] — scheduled invoice destinations, draft rerouting, and exactly-once boundary
- [[source-metronome-integrations-tax-integrations-stripe-tax]] — finalization-time tax calculation and collection-method boundary
- [[source-metronome-guides-get-started-how-metronome-works]] — calculation order and separation of evaluation, visibility, and finalization
- [[source-metronome-guides-implement-metronome-core-concepts-provision-contract]] — consolidation conditions and beta provider-attachment timing
- [[source-metronome-guides-implement-metronome-core-concepts-provision-customer]] — customer/contract routing boundary and beta archival
- [[source-metronome-guides-pricing-packaging-billing-model-guides-pay-as-you-go]] — illustrative Stripe `send_invoice` boundary
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-manual-payment-gated-commits]] — manual commit payment, invoice voiding, and retry boundary
