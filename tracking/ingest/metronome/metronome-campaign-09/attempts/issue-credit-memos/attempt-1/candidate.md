---
title: "Issue credit memos"
type: source
date_ingested: 2026-08-01
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/invoices/invoice-optimization/issue-credit-memos"
raw_files:
  - "metronome/guides/invoices/invoice-optimization/issue-credit-memos-2026-07-13.md"
tags: [metronome, credit-memos, credits, invoices, usage-corrections, revenue, refunds]
---

## Overview

This guide separates a Metronome credit applied to future billing from a credit memo that corrects customer accounts receivable (A/R), and then maps correction options to invoice state. Metronome represents usage charges and credit or commitment drawdown on invoices but does not provide the ERP-style credit-memo entity described here; historical A/R adjustments and payment refunds therefore retain explicit external-system ownership.

## Decision boundaries

| Situation | Documented action | Boundary |
| --- | --- | --- |
| Customer accepts relief on later bills | Create a customer-level or contract-specific Metronome credit | This applies value to future billing; it does not alter the past transaction or invoice and the guide does not say it reverses historical revenue. |
| Charges and associated revenue must be fully reversed | Create a credit memo in the system that manages customer A/R | The adjusted customer invoice can differ from the Metronome invoice line. The guide treats the external credit memo as the audit record supporting that difference. |
| Incorrect usage in the current period and invoice is `DRAFT` | Send a negative quantity or value matching the affected product's billable metric | This corrects the draft calculation in Metronome; it is not documented as a payment refund or an A/R credit memo. |
| Incorrect usage belongs to a previous period and invoice is `finalized` | Grant a credit toward future billing or create an external A/R credit memo | Metronome says usage events cannot be corrected or adjusted for a finalized invoice. |
| Entire invoice is incorrect and the usage is still within the historical-ingest window | Negate the incorrect usage, send corrected usage, void the invoice, and regenerate it | Voiding in Metronome does not void a downstream invoice; that step is manual there. Regeneration recalculates from associated usage, and the Stripe integration sends the new invoice to Stripe automatically. |
| Credit and re-bill is more than 34 days in the past | Void, cancel, and regenerate directly in the invoicing and customer-A/R application | The guide presents the external application as the only option because Metronome limits historical usage submission to 34 days. |
| Money already paid must be returned | Use the ERP, CRM, or payment processor according to the merchant's stack | Payment refunds are outside current Metronome functionality and are distinct from future credits, A/R credit memos, and invoice re-rating. |

## Future-billing credits

A future credit can be customer-level, making it available against any existing contract on the account, or contract-specific. The worked API example creates a customer-level credit of `10000` USD cents, uses access-schedule start and end timestamps, and says recurring credits need one separate `schedule_item` for each billing period.

When several credits are active, `priority` determines drawdown order. `credit_type_id` selects the pricing unit or currency; the page identifies the USD ID and says USD values use cents while other supported currencies use whole units. `product_id` controls the product displayed on the invoice, while `applicable_product_ids` narrows which products the credit can cover. Presentation and applicability are therefore separate concerns.

## Historical correction and revenue

For a full reversal of incorrect charges and their associated revenue, the documented path is an external credit memo in the A/R system. The resulting A/R invoice and Metronome invoice line may not match, and the credit memo supplies the audit record for that discrepancy. The guide does not describe the accounting entries, revenue-recognition timing, tax treatment, payment-status changes, or reconciliation automation.

A current-period `DRAFT` invoice has a different correction path: send a new event with a negative value that matches the relevant billable metric. The example negates `token_count` with the string value `"-50"`; it does not establish that the original event is mutated or deleted.

For a previous-period `finalized` invoice, the page instead permits a future credit or external credit memo and explicitly disallows correction or adjustment of usage events for that finalized invoice. Finalization is thus the documented boundary between direct draft re-rating and compensating action.

## Credit-and-rebill flow

When the whole invoice is wrong, the guide gives this order: negate the incorrect usage, submit corrected usage, void the incorrect invoice, then regenerate it. The regenerated invoice is recalculated from associated usage; when the Metronome Stripe integration is used, the guide says the new invoice is sent to Stripe automatically. A Metronome void does not propagate downstream, so the merchant must separately void or cancel the downstream invoice.

The re-bill path is limited by the 34-day historical-usage submission window. Beyond it, the guide directs all voiding, cancellation, and regeneration to the invoicing and customer-A/R application. It does not define whether exactly 34 days is accepted, which clock or time zone sets the cutoff, how partial failures are recovered, whether downstream void and regeneration are idempotent, or how taxes, collected payments, credits already consumed, and revenue records are reconciled.

## Documentation issues and unknowns

> [!warning] Contradictory example dates
> The future-credit prose says to use today's date as the start and a later use-by date as the end, but the JSON starts at `2024-09-01` and ends before `2020-09-30`. Treat those timestamps as invalid illustrative data, not an operable schedule.

> [!warning] Re-bill sequence ambiguity
> The finalized-period example says Metronome does not allow usage-event correction or adjustment for finalized invoices. The next section says to negate and replace usage before voiding and regenerating the incorrect invoice, but does not state that invoice's starting state or explain how the event steps interact with finalized-invoice immutability. Verify the supported sequence and invoice-state preconditions before implementation.

The page also does not specify the create-credit request's full schema, authentication, validation and idempotency behavior; how to create the contract-specific variant; whether a future credit changes recognized revenue; or how external credit memos, downstream invoice state, Metronome invoice state, refunds, and regenerated invoices are transactionally reconciled.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-credits-and-commits]], [[metronome-invoicing]], [[metronome-event-ingestion]], [[metronome-integrations]]
- Related sources: [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]], [[source-metronome-api-reference-usage-ingest-events]], [[source-metronome-integrations-invoice-integrations-stripe]], [[source-metronome-guides-invoices-overview]]

## Raw Sources

- [[raw/metronome/guides/invoices/invoice-optimization/issue-credit-memos-2026-07-13|2026-07-13 snapshot — future credits, historical A/R corrections, invoice-state boundaries, re-billing, and refunds]]
