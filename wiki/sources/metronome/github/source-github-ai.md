---
title: "GitHub: Metronome-Industries/ai"
type: source
date_ingested: 2026-08-15
original_format: github-repo
raw_files:
  - "github/metronome/ai/snapshots/2026-08-15-59193aa/manifest.json"
tags: [metronome, ai, agent-skills, usage-based-billing, catalog, contracts, customer-success, stripe-migration, github-repository]
---

## Overview

`Metronome-Industries/ai` contains Metronome-authored skills for AI coding assistants and operational agents. The approved baseline is `main` at exact SHA `59193aabd9c43cca32f320d6f68f5d63d04034d4`, committed on 2026-06-24 and collected on 2026-08-15. It covers integration best practices, catalog and customer provisioning, contract creation, PLG billing, customer-success reviews, and Stripe usage-billing migration.

Repository: <https://github.com/Metronome-Industries/ai>

## Evidence Boundary

- This is an instruction and example repository, not a runtime SDK, API schema, or service changelog. It proves what these skills tell an agent at the exact SHA; dedicated Metronome documentation and exact SDK/API evidence remain authoritative for request schemas and product behavior.
- The retained capsule contains all seven skill directories and their references, plus three dogfood scenarios. The scenarios define expected agent tasks and checks; they are not production behavior tests or merchant-eligibility evidence.
- Endpoint paths, enums, limits, and operational rules vary within the repository and sometimes conflict with existing documentation. Preserve those conflicts instead of selecting one example as universally correct.
- The repository has no semantic release in this work item. `default-branch@59193aa` is a commit-qualified evidence identity, not a package version.
- The README describes Metronome as "Stripe's usage-based billing platform," and the license names Stripe. This page preserves that repository attribution without using it to infer corporate ownership or product scope beyond the collected evidence.

## Grounding Excerpts

> "This repo contains AI coding assistant skills that encode Metronome best practices, integration patterns, and common pitfalls."
>
> `raw/github/metronome/ai/snapshots/2026-08-15-59193aa/files/README.md:5`

> "Hard dependencies — do not skip ahead. Save every ID returned at each step."
>
> `raw/github/metronome/ai/snapshots/2026-08-15-59193aa/files/skills/metronome-setup-catalog/SKILL.md:31-33`

> "Always use a parallel run (minimum one full billing cycle) before cutting over legacy customers."
>
> `raw/github/metronome/ai/snapshots/2026-08-15-59193aa/files/skills/stripe-to-metronome-migration/SKILL.md:38`

> "Read the relevant reference file before making any API calls or analysis."
>
> `raw/github/metronome/ai/snapshots/2026-08-15-59193aa/files/skills/metronome-csm-reviews/SKILL.md:25`

> "Label any figure derived this way as estimated. Do not present it as a confirmed rate."
>
> `raw/github/metronome/ai/snapshots/2026-08-15-59193aa/files/skills/metronome-csm-reviews/SKILL.md:67`

## Skill Inventory

| Skill | Operational purpose | Important boundary |
| --- | --- | --- |
| `metronome-best-practices` | Events, contracts, rate cards, invoices, credits and Stripe integration | Broad guidance; examples do not replace API schemas |
| `metronome-setup-catalog` | Ordered metric, product, rate-card, customer and contract setup | First-time setup only; explicitly excludes several provider-specific domains |
| `metronome-create-customer` | Preview-and-confirm customer provisioning | Assumes organization-specific Salesforce and Slack custom fields |
| `metronome-create-contract` | Translate signed commercial terms into contracts | Requires human confirmation before writes |
| `metronome-plg-billing` | PLG pricing patterns, diagnostics and blast-radius analysis | Worked examples contain inconsistent rate representations |
| `metronome-csm-reviews` | Read-only anomaly, commit-health, portfolio and renewal analysis | Thresholds are repository policy, not platform guarantees |
| `stripe-to-metronome-migration` | Stripe UBBv1 discovery, mapping, parallel validation and cutover | Migration playbook; exact API and product claims require canonical verification |

## Catalog and Provisioning Workflow

The setup skill imposes a dependency order: create billable metrics, create products, create a rate card, add rates, create a customer, create a contract, and verify through the customer's invoices. It tells the agent to retain every returned ID and to read the relevant reference before making API calls.

The customer and contract skills add a two-step preview-and-confirm control before writes. Customer creation checks names for likely duplicates and collects an ingest alias plus organization-specific Salesforce and Slack fields. Contract creation parses commercial terms, validates referenced catalog objects, previews commits, credits, overrides and schedules, and asks for confirmation. These are agent operating controls, not evidence that all listed fields are universally required by Metronome.

The PLG material organizes catalog decisions around subscription, usage, hybrid, prepaid-credit and freemium patterns. Its diagnostics emphasize checking the complete event-to-invoice chain instead of assuming that accepted events produced billable usage.

## Event and Billing Guidance

The event reference recommends deterministic transaction IDs, batches of up to 100 events, explicit timestamps, retained dimensional properties, and matching billable metrics before production ingest. It warns that unmatched event types can be silently ignored and that over-aggregation removes future pricing and reporting dimensions.

> [!warning] Contradiction: numeric event properties
> The Stripe migration skill says Metronome requires numeric values to be JSON numbers and rejects string-typed numeric values. Existing Metronome implementation guidance recommends string-valued properties to avoid floating-point precision loss, while the API schema allows an object without defining universal value coercion. Treat the migration statement as scoped agent guidance and verify the current endpoint contract before changing an event producer.

> [!warning] Contradiction: rate representation
> The catalog rate-card reference calls `SUBSCRIPTION` rate type deprecated and recommends `FLAT` plus `billing_frequency`, but a PLG worked example uses `rate_type: "SUBSCRIPTION"` with a nested `subscription_rate`. Dedicated rate-card and contract documentation remains authoritative.

The CSM skill defines read-only workflows over customers, contracts, balances, costs and invoices. It applies repository-selected thresholds to finalized periods, distinguishes estimated fallback burn rates, excludes scheduled fees from usage trends, and treats absent or zero billing activity as an investigation prompt rather than an anomaly by itself.

## Stripe-to-Metronome Migration

The migration skill maps Stripe Billing Meters, prices, subscriptions and credit grants into a staged Metronome implementation. Its durable process recommendations are to scope the existing estate, design metrics and catalog mappings, run both systems for at least one complete billing cycle, compare invoice results, migrate remaining credit balances rather than original grants, align cutover to a billing boundary, and retain a rollback plan.

The playbook warns that enabling Metronome auto-recharge during parallel validation can create real charges even when customers are otherwise marked unbillable. This is a high-impact operational claim from an agent skill and requires confirmation against current Metronome documentation and account configuration before execution.

The migration references repeatedly describe Stripe invoice line-item collapse around a 250-item boundary, but characterize the consequence differently. Preserve it as a migration investigation item rather than a universal failure rule until the canonical Stripe integration evidence is reconciled.

## Query Guidance

Use this source for questions about the repository's agent workflows, checklists, task routing, example architectures, and migration methodology. For exact API fields, endpoint paths, enum values, limits, eligibility, or runtime behavior, search the relevant Metronome documentation source and [[source-github-metronome-node]] as appropriate. For update questions, also search [[changelog-github-ai]].

## Related

- Company: [[metronome]]
- Concepts: [[metronome-event-ingestion]], [[metronome-products-and-rate-cards]], [[metronome-customers-and-contracts]], [[metronome-usage-based-billing]], [[metronome-integrations]]
- SDK evidence: [[source-github-metronome-node]]
- History: [[changelog-github-ai]]

## Raw Sources

- Snapshot manifest: `raw/github/metronome/ai/snapshots/2026-08-15-59193aa/manifest.json`
- Repository overview: `raw/github/metronome/ai/snapshots/2026-08-15-59193aa/files/README.md`
- Integration guidance: `raw/github/metronome/ai/snapshots/2026-08-15-59193aa/files/skills/metronome-best-practices/SKILL.md`
- Event guidance: `raw/github/metronome/ai/snapshots/2026-08-15-59193aa/files/skills/metronome-best-practices/references/events.md`
- Catalog setup: `raw/github/metronome/ai/snapshots/2026-08-15-59193aa/files/skills/metronome-setup-catalog/SKILL.md`
- PLG billing: `raw/github/metronome/ai/snapshots/2026-08-15-59193aa/files/skills/metronome-plg-billing/SKILL.md`
- CSM reviews: `raw/github/metronome/ai/snapshots/2026-08-15-59193aa/files/skills/metronome-csm-reviews/SKILL.md`
- Stripe migration: `raw/github/metronome/ai/snapshots/2026-08-15-59193aa/files/skills/stripe-to-metronome-migration/SKILL.md`
- Dogfood scenarios: `raw/github/metronome/ai/snapshots/2026-08-15-59193aa/files/tests/dogfood/scenarios/`
