---
title: "Invoice with Stripe"
type: source
date_ingested: 2026-08-30
canonical_url: "https://docs.metronome.com/integrations/invoice-integrations/stripe"
original_format: webpage
raw_files:
  - "metronome/integrations/invoice-integrations/stripe-2026-08-28.md"
  - "metronome/integrations/invoice-integrations/stripe-2026-07-13.md"
tags: [metronome, stripe, invoicing, billing-integration, multi-entity-billing]
---

## Overview

This guide documents Metronome's native Stripe invoice integration: Metronome finalizes its billing record and creates the corresponding Stripe invoice, while Stripe and the selected tax provider perform downstream collection and tax work. It defines connection scope, account and customer identity mapping, contract routing, status observation, recovery signals, and the representation limits operators must account for.

## Query-critical facts

- A Stripe connection is scoped to one Metronome environment and grants Metronome read and write access to the connected Stripe account. Metronome Sandbox connects to Stripe test mode; a production connection and a sandbox connection are separate setup surfaces, and a single Metronome environment can connect to multiple Stripe accounts.
- Integration settings and mapping rules are enforced per Stripe account and environment, not per customer. In a multi-account environment, customer setup must use `delivery_method_id` to select the Stripe account; contract creation selects an existing customer configuration with `billing_provider_configuration_id`. These identifiers are different routing layers.
- Customer configuration maps to a Stripe customer through `stripe_customer_id` and chooses `charge_automatically` or `send_invoice`. Stripe owns the collection action: automatic charge requires a default payment method before finalization, while `send_invoice` emails payment instructions and uses the account-level due-date setting.
- Adding a Stripe configuration to an existing contract is prospective. Metronome does not resend previously finalized invoices; the first delivery is the in-arrears usage invoice for the period in which the configuration was attached, based on attachment time rather than contract start or configuration-creation time.
- Metronome writes `metronome_id` on the Stripe invoice to map it back to the Metronome invoice and can map additional custom fields. Payment-gated commits have a stricter product-identity requirement: every participating product needs a valid mapped `stripe_product_id`, otherwise Stripe cannot construct the line item, payment fails, and the commit is voided.
- Metronome imports Stripe invoice-status changes from Stripe webhooks and exposes mapped external status through invoice reads and data export. Tax calculation occurs on the Stripe invoice: Metronome supplies entity mappings, the selected tax provider calculates tax, and Stripe finalization includes it. A deliberately draft Stripe invoice has no Stripe status in Metronome.
- For `charge_automatically`, Metronome sends the finalized invoice immediately, but this Metronome guide documents a Stripe-side up-to-one-hour wait before its payment attempt and a 72-hour fallback when `invoice.created` delivery fails. Decimal quantities, more than 250 line items, Stripe's documented maximum charge, and credit-memo absence can change or limit the Stripe representation even though the detailed Metronome invoice remains available.

## Material boundaries

- Metronome owns usage rating, its invoice record, routing configuration, and creation of the corresponding Stripe invoice. Stripe owns invoice acceptance, collection method execution, payment timing and retries, and the external payment status; the selected tax provider owns tax calculation. This Metronome guide does not guarantee Stripe acceptance, customer delivery, payment or settlement finality, tax correctness, accounting posting, or end-to-end reconciliation.
- The multi-account contract section says in prose to use `billing_configuration_id`, while its payload uses `billing_provider_configuration_id`. Preserve that documentation ambiguity and follow the dedicated contract schema rather than silently treating the two names as interchangeable. Likewise, the status table labels `invoice.deleted` but links to `invoiceitem.deleted`; verify the external event authority before implementing that deletion mapping.
- `invoice.billing_provider_error` is a Metronome notification for errors sending an invoice to Stripe; operators must trigger their own internal response. Imported external status and `metronome_id` support observation and matching, but neither proves complete delivery, payment finality, settlement, or reconciliation, and this page defines no exhaustive recovery contract for an ambiguous cross-system outcome.
- The Metronome API POST examples remain subject to the separate [[metronome-api-idempotency|API-wide `Idempotency-Key` authority]]. This guide adds no endpoint-specific Metronome retry, concurrency, cached-error, freshness, or ambiguous-failure guarantee. Its Stripe PaymentIntent-confirm workaround is a Stripe API action and must not be conflated with Metronome POST idempotency or a general payment-retry guarantee.

## Raw-detail coverage map

- **Connection and environment setup:** current Developer → Integrations paths, per-environment setup, Stripe test-mode behavior, multiple-account aliases, and the automatic-payment-retry recommendation are in the latest raw page.
- **Account settings and mappings:** due dates, `auto_advance`, minimum-charge skipping, `effective_at`, Stripe Tax incompatibility, line-item presentation, `metronome_id`, custom metadata, product mapping, and payment-gated-commit prerequisites are in the latest raw page.
- **Customer and contract routing:** complete `/customers`, `/setCustomerBillingProviderConfigurations`, and `/contracts/create` examples; collection-method fields; `delivery_method` and ID layers; account enumeration; and the prospective attachment timeline are in the latest raw page. Dedicated API references remain authoritative for exact request schemas and requiredness.
- **Status, tax, payment, and recovery:** the complete Stripe-event mapping table, data-export visibility, draft-status exception, tax-provider matrix and flow, one-hour tax window, automatic-charge timing, 72-hour fallback, PaymentIntent-confirm workaround, and `invoice.billing_provider_error` action signal are in the latest raw page.
- **Stripe representation limits:** decimal-quantity transformation, 250-line-item collapse, maximum-charge error, and lack of native Stripe credit-memo issuance are in the latest raw page; these statements are Metronome's description of the integration, not a complete external-platform guarantee.

## Related

- Companies: [[metronome]], [[stripe]]
- Primary concepts: [[metronome-integrations]], [[metronome-invoicing]], [[metronome-customers-and-contracts]]
- Supporting concepts: [[metronome-custom-fields]], [[metronome-products-and-rate-cards]], [[metronome-credits-and-commits]], [[metronome-webhooks]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-integrations-tax-integrations-stripe-tax]], [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]], [[source-metronome-api-reference-customers-create-a-customer]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/integrations/invoice-integrations/stripe-2026-08-28|2026-08-28 snapshot - current native Stripe invoice routing, identity mapping, status, payment timing, tax flow, recovery signals, and limits]]
- [[raw/metronome/integrations/invoice-integrations/stripe-2026-07-13|2026-07-13 snapshot - prior native Stripe integration setup and behavior]]
