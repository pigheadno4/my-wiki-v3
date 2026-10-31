---
title: "Metronome Token Billing"
type: concept
category: technology
tags: [metronome, token-billing, ai, usage-based-billing, pricing]
---

## Definition

Metronome Token Billing is a private-preview managed workflow for passing LLM-token costs to customers with a markup. Managed AI rate cards create the selected models' billable metrics, products, and rates from configured markups, while token-usage events select rates by model, provider, and token type. [[source-metronome-guides-pricing-packaging-billing-model-guides-token-billing]]

## Pricing and provisioning

- Non-USD fiat is unsupported because the documented provider prices are denominated in USD. A USD-to-custom-unit conversion can instead support credit-denominated plans; that custom unit is not another fiat currency.
- Newly released models are added to a managed rate card at its default markup. Automatic repricing after a provider changes an existing model's price is described only as coming soon.
- The worked plan layers a custom-unit allocation onto the managed rate card through a package, then provisions a customer contract from that package. Its amounts, identifiers, selected models, markup, and allocation are illustrative.

## Event and operational boundary

Token usage uses `event_type: token-billing`, with input, cached-input, output, and cache-write token properties; `model` and `provider` select the applicable rate. The guide instructs operators to verify that the event matched a billable metric, but submission or matching alone does not prove rating, invoicing, collection, or reconciliation.

The guide does not define catalog-update timing, model removal or fallback, rate effective dating, precision or rounding, provider-cost verification, margin guarantees, or recovery after provider-price changes. Its contract-create and ingest examples omit `Idempotency-Key`; this does not override the separate API-wide POST authority, and usage `transaction_id` remains a distinct deduplication mechanism.

## Commit-Qualified Agent Workflow: `0519b4b`

The 2026-10-31 full additive ingest of Metronome's AI skills adds a public-API orchestration playbook, not runtime implementation or a general-availability announcement. It resolves application model aliases to canonical catalog IDs, uses one shared metric per token type, one managed product per model/token type, and provider-specific rates. Rates use decimal USD-per-token calculations converted to cents per million tokens; custom-unit rates additionally divide by the rate card's cents-per-custom-unit conversion. Reusable plans use packages over a shared managed rate layer; ordinary fees and allocations remain separate from AI-managed products. [[source-github-ai]]

The skill describes hourly managed sync with a catalog watermark, author-prefix opt-in and separate default/product markups. Existing model/provider/token-type rate keys are skipped, so this is not automatic repricing of an existing provider rate. Manual model additions and markup edits preserve the watermark, require explicit proposals, retain established dimensions and independently read back products, effective rates and schedules. This is repository guidance, not audited managed-sync implementation. It supplements rather than replaces the separately dated private-preview website evidence above.

Stripe catalog credentials, account-level invoice-delivery connection, customer billing-provider configuration and contract/package routing are distinct prerequisites. Stripe remains collection infrastructure; the skill does not create a second Stripe meter/plan for the same token stream. Hard-stop behavior uses an application-owned low-latency entitlement cache reconciled with Metronome, not a second financial ledger. No credentials, provider APIs, OAuth, feedback submission or controlled usage were executed during wiki ingest. See [[source-github-ai]] and [[changelog-github-ai]].

## Sources

- [[source-github-ai]] - exact-commit token-billing orchestration, managed-sync limits and verification controls; historical baseline retained.

- [[source-metronome-guides-pricing-packaging-billing-model-guides-token-billing]] - private-preview managed AI pricing, custom-unit and package flow, token-event mapping, and model-update boundaries

## Related

- [[metronome-usage-based-billing]]
- [[metronome-products-and-rate-cards]]
- [[metronome-billable-metrics]]
- [[metronome-event-ingestion]]
- [[metronome-currencies-and-custom-pricing-units]]
- [[metronome-packages-and-aliases]]
- [[metronome-api-idempotency]]
