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

## Commercial Billings measure

For Metronome's own consumption pricing, Billings are the total value of invoices generated through Metronome whether invoiced automatically or manually. The stated exclusions are current-period finalized invoices voided before Metronome invoices the platform customer, non-production draft invoices used for testing or demonstration, and zero-dollar invoices used to track free-trial credits. The source does not define currency aggregation, tax, discounts, refunds, or other adjustments. [[source-metronome-guides-platform-configuration-metronome-pricing-model]]

The architecture guide orders invoice generation as usage receipt, billable-metric quantity calculation, contract pricing with base-rate-card overrides, and customer-facing invoice generation. It separately describes event-time alert evaluation, on-demand API-backed views, and cycle-close invoice finalization and delivery. The first two contexts do not establish that an invoice is finalized, and the page gives no latency, delivery, collection, retry, or failure-state guarantees.

The customer-controls guide distinguishes two alert calculations: `spend_threshold_reached` uses usage-based spend before credit and commit drawdown, while `invoice_total_reached` evaluates the amount after drawdown and can be limited to usage invoices. These are threshold-evaluation semantics, not evidence that an invoice is finalized, delivered, collected, paid, or immutable.

## Event-based invoice preview

Metronome exposes `POST /v1/customers/{customer_id}/previewEvents` to calculate draft invoices from supplied usage events and the customer's current contract configuration before those events are processed. The request can replace historical usage or merge with it, and the response returns draft invoice records with totals and line items. Contracts using SQL billable metrics are excluded from this preview capability.

The cost-preview guide clarifies that Preview Events simulates invoice impact without processing or billing the proposed events. Its calculation can include tiered pricing, commit and credit coverage, free allotments, and multiple products. `merge` includes existing billing-period usage; `replace` ignores existing usage. Multiple active contracts return separate draft-invoice-shaped results.

These results are previews, not finalized, delivered, collectible, or documented as persisted invoices. The guide limits the endpoint to 8 RPS per client and returns HTTP 400 when SQL billable metrics are present on the customer invoice being evaluated. Its worked response is structurally illustrative: a request for 100 compute hours produces quantity 10, unit price 4900, line-item total 0, and invoice total 49000 without reconciling the quantity or arithmetic.

## Dashboard lifecycle overview

The dashboard quickstart describes a draft invoice accumulating usage during the billing period, followed by a 24-hour grace period before finalization. With a billing provider connected, it says the invoice is pushed within approximately one hour after finalization. Payment collection and paid or failed status remain the billing provider's responsibility.

## Credit and commit application

For a product rated in a custom pricing unit, Metronome first burns down applicable credits and prepaid commits with access schedules in that unit. If no applicable matching balance remains, the invoice receives a conversion line item that calculates the residual cost in the rate card's fiat currency; the converted fiat amount becomes the total due in the example. This does not establish conversion formula direction, precision, rounding, tax, finalization, delivery, collection, or payment-success behavior.

### Credit, correction, and re-bill state boundaries

For incorrect usage on a current-period `DRAFT` invoice, the credit-memo guide directs the merchant to send a negative quantity or value matching the affected product's billable metric. For a previous-period `finalized` invoice, Metronome says usage events cannot be corrected or adjusted; the documented alternatives are a future credit or an external A/R credit memo. When the whole invoice is wrong, the guide separately gives a credit-and-rebill sequence of negative usage, corrected usage, voiding, and regeneration. A Metronome void does not void a downstream invoice, and historical usage submission is limited to 34 days; older re-bills remain entirely in the invoicing and A/R system.

> [!warning] Documentation ambiguity
> The finalized-period example prohibits usage-event correction for finalized invoices, while the following re-bill sequence instructs readers to negate and replace usage before voiding without stating the starting invoice state or reconciling that order with finalized-invoice immutability. Verify state preconditions and operation order before implementation.

Credits and commits apply at invoice line-item level. Covered usage, its negative application line, and uncovered overage remain separate so product-level precommitted and overage spend stays attributable. A commit can record an invoiced amount without sending a downstream invoice, and scheduled commit charges can be consolidated onto a usage statement when the contract enables that behavior.

Commit edits appear immediately on draft invoices, while finalized invoices remain unchanged unless voided and regenerated. Invoice-schedule items tied to finalized invoices cannot be removed or updated, and a voided invoice's schedule item still cannot be removed. An access-schedule segment applied to a finalized invoice can be removed only after voiding that invoice.

A credit or commit ledger has one deduction entry for each invoice that consumes that balance. The deduction's effective timestamp is always the end of the usage invoice's service period, and Metronome says that timestamp can support balance views including or excluding pending charges. This does not make the ledger timestamp an invoice creation, finalization, delivery, collection, or payment timestamp, and the guide does not define how `pending` maps to invoice states.

## Threshold payment flow

Prepaid balance thresholds can gate release of a recharge commit on payment. Stripe gating can use a Stripe Billing invoice or a direct PaymentIntent. On a failed payment, the guide says the threshold configuration is disabled and a voided invoice should appear in both Metronome and Stripe; there is no automatic retry. An external payment gate leaves collection to the integrator, which must explicitly release or cancel the pending commit.

Spend-threshold billing is separate from prepaid-balance recharge: accumulated contract spend reaching `threshold_amount` triggers a payment attempt, and the configured commit product determines what appears on the incremental invoice. Stripe payment can use a Billing invoice or PaymentIntent; an external gate leaves collection to the integrator, which releases or cancels the commit afterward. The page does not define invoice finalization, payment retry, pending-commit invoice state, threshold denomination, or whether an ungated failure changes customer access.

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

### India card e-mandates

For Indian-card invoices, the documented flow collects the card on-session and confirms a Stripe SetupIntent, then waits for the mandate to become active. Threshold recharges use a sporadic interval and maximum amount; subscriptions and recurring fees use their recurrence cadence and a fixed amount when known or maximum when variable. A mandate may remain pending for up to 30 minutes; an inactive mandate is unusable and requires new customer authorization.

The contract stores the Stripe mandate ID in a custom field mapped to `invoice.payment_settings.default_mandate`. Invoices sent to Stripe attempt to attach the mandate, but attachment is not a payment-success guarantee. Stripe can issue `invoice.payment_action_required`; no response or an inactive mandate enters the normal failure flow.

Stripe owns mandate creation and lifecycle. Metronome returns the custom-field value and maps it into invoice delivery but exposes no mandate-management API. The page requires SetupIntent setup for this integration because it characterizes all charges, including the first, as off-session. The integrator must update or replace the mandate in Stripe and act before retrying.

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

- [[source-metronome-guides-pricing-packaging-make-pricing-changes-use-currency-custompricingunits]] — custom-unit balance drawdown, conversion-line-item fallback, and fiat total-due boundary
- [[source-metronome-guides-invoices-invoice-optimization-issue-credit-memos]] — future credits, external A/R credit memos, draft versus finalized correction, void-and-regenerate re-billing, and refund ownership

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
- [[source-metronome-guides-customers-billing-optimize-customer-experience-india-e-mandates]] — Indian-card Stripe mandate creation, activation, invoice mapping, customer action, and ownership boundaries
- [[source-metronome-guides-customers-billing-optimize-customer-experience-set-customer-spend-control]] — incremental spend-threshold invoicing, Stripe payment choices, and external outcome flow
- [[source-metronome-guides-customers-billing-optimize-customer-experience-preview-event-cost]] — contract-aware cost simulation, merge/replace semantics, multi-contract draft results, performance limit, and SQL-metric exclusion
- [[source-metronome-guides-customers-billing-optimize-customer-experience-customer-controls]] — pre-drawdown spend versus post-drawdown usage-invoice alert calculation
- [[source-metronome-guides-customers-billing-optimize-customer-experience-get-remaining-balance]] — per-invoice balance deductions, service-period effective timestamps, and pending-charge display boundary
