---
title: "GitHub: Metronome-Industries/ai"
type: source
date_ingested: 2026-08-15
date_updated: 2026-10-31
original_format: github-repo
raw_files:
  - "github/metronome/ai/snapshots/2026-10-30-0519b4b/manifest.json"
  - "github/metronome/ai/snapshots/2026-08-15-59193aa/manifest.json"
tags: [metronome, ai, agent-skills, usage-based-billing, catalog, contracts, customer-success, stripe-migration, github-repository]
---

## Overview

`Metronome-Industries/ai` contains Metronome-authored skills for AI coding assistants and operational agents. The approved baseline is `main` at exact SHA `59193aabd9c43cca32f320d6f68f5d63d04034d4`, committed on 2026-06-24 and collected on 2026-08-15. It covers integration best practices, catalog and customer provisioning, contract creation, PLG billing, customer-success reviews, and Stripe usage-billing migration.

Repository: <https://github.com/Metronome-Industries/ai>

## Full Additive Update: `default-branch@0519b4b`

Approved full ingest on 2026-10-31, from August baseline `59193aabd9c43cca32f320d6f68f5d63d04034d4` to `0519b4b79908312e9dbfe64c5e4451fefc9aa30d` (upstream commit 2026-10-29; collected 2026-10-30). This is commit-qualified agent-instruction evidence, not a semantic package release, API schema or runtime audit. All original August body sections, quotations and warnings below remain preserved and August-scoped.

The approved focused-reading exception covers all 39 changed/new current documents in full, every affected prior replacement/deletion range with context, and all three removed August scenarios in full. The unchanged LICENSE, generated inventories and duplicated diff were verified mechanically; shared company/index/log context was read by relevant sections. All 79 files across the 39/40-file snapshots passed size, SHA-256 and Git-blob checks. The full-mode assignment remains 90 paths, approximately 1.74 MB; this does not claim a full upstream-repository read or fresh semantic reading of unchanged historical sections.

### Provenance and Nine-Skill Inventory

The capsule has 40 files / 319,917 bytes: four additions, 35 modifications, three removals and one unchanged file versus the retained baseline. It now has nine skills: the seven historical skills plus `metronome-group-keys` and `metronome-token-billing`. The additions also include skills/README.md and .skills-sync.json. All three dogfood scenarios disappeared upstream, but their August raw files and findings remain queryable.

README and contribution guidance now describe skills as generated from private `Metronome-Industries/api`, path docs/skills. The sync record names upstream SHA `41f41b24fc4e1b06568eb4996b3087d7e06ff430`; this is declared provenance, not evidence that the private repository was accessed. Direct skill edits in this public repository are overwritten by later sync. README supplies docs-site skill installation and a machine-readable skills index; references use absolute documentation URLs. Those links are navigation, not evidence that their current remote targets were fetched during ingest. Raw skill instructions were read as evidence, never executed.

### New Group-Key Design Workflow

The dedicated skill requires a confirmed inventory of dimensions, roles and cardinality before creating immutable metrics. It distinguishes pricing, invoice presentation, spend/usage analysis, seats and alerts; dimensions that co-occur need compound coverage. Invoice presentation requires the pricing/presentation union, while independent queries can use standalone keys. Compound scan cost multiplies dimension cardinalities. Roughly 1,000 values prompts support consultation, not a hard platform cap; bounded alert dimensions and populated-but-unqueried compound keys require care.

Its recommended create payload adds an exists=true property filter for every group and aggregation property. These are specific agent recommendations, not an independently verified minimum schema contract. Token Billing prescribes its own ordered compound metric key beginning with model/provider and all approved extra dimensions; do not replace that workflow with the generic skill's standalone-key default. [[metronome-billable-metrics]]

> [!warning] Contradiction: group-key and example completeness
> The same commit's PLG patterns.md:244 says presentation-only dimensions do not need group keys; the dedicated new skill requires compound coverage. Setup and migration text also encourage extra or cost-free unused keys while the new skill warns about populated compound scan cost. Some setup/PLG metric examples omit the property filters that the dedicated skill requires. UNIQUE remains listed as a streaming aggregation in some tables while migration references direct distinct counts to SQL. Preserve these file-specific differences; [[metronome-billable-metrics]] carries the reciprocal warning. They are not proven API behavior or safe standalone snippets.

### New Token-Billing Orchestration

The new skill covers approved commercial plans, model selection, markup, usage dimensions, managed rates, reusable packages, customer provisioning and verification. It distinguishes sandbox from production, requires explicit write approval and keeps resumable non-secret run evidence. Model aliases resolve by exact, case-insensitive then separator-normalized matches; ambiguous matches stop for input. Event and rate model values use canonical catalog id, not application alias or the shorter model label. Catalog prices use currently effective supported rows, excluding future prices and unknown usage types; the approved catalog snapshot is reused for writes.

Managed structure is one shared metric per input/output/cached_input/cached_write token type, one product per model/token type shared across providers, and one flat rate per model/provider/token type. Products price by model/provider, divide quantity by one million and add only approved invoice-breakout keys to presentation_group_key. Analytics-only dimensions remain in the metric, not invoice grouping. A model or dimension change must preserve or deliberately migrate that structure; names alone do not prove reusable object identity.

The skill uses decimal arithmetic: `USD cents per million = USD per token * (1 + markup fraction) * 1,000,000 * 100`. For custom units, divide that result by the API's cents-per-custom-unit conversion. The merchant chooses markup; defaults are proposals, not approval. Ordinary subscriptions/fees, included allocations, prepaid balances and top-ups remain separate from AI-managed products; reusable named plans use packages over a shared managed rate layer.

It distinguishes Stripe credentials for model-catalog access, account-level invoice-delivery connection, customer billing-provider configuration and direct-contract/package routing. A Stripe API key alone does not connect invoice delivery. Metronome owns token metering/rating/entitlements; Stripe is the collection rail, not a second meter, Price or Subscription for the same stream. Existing separate flat-fee subscriptions and deliberately controlled migration parallel runs have their own scopes. Hard stops use an application-owned low-latency entitlement cache reconciled with Metronome, not a second financial ledger or synchronous invoice aggregation.

### Managed Sync, Model Additions and Markup Changes

The skill describes hourly managed sync keyed by ai_managed fields/tags and ai_managed_last_updated_at. It processes eligible catalog rows newer than the watermark only for author prefixes already represented on the card; advances the watermark even with no additions; and skips existing model/token-type/provider rate keys. Thus author opt-in is not retroactive and existing provider prices are not automatically repriced. These statements come from the skill, not inspected scheduler/runtime code, and do not establish feature enablement or supersede the dated private-preview website boundary. [[metronome-token-billing]]

Manual additions and markup edits require explicit proposals with exact environment, schema, rates and effective time. Existing dimensions and untargeted product fields are preserved. Model additions do not reprice existing keys. A markup edit must change both product ai_markup and actual rates; changing one does not complete the other. Whole-card future-default changes are separately chosen. Neither operation advances the managed-sync watermark. Existing product sharing across cards must be surfaced before changes.

Follow-up rates are hour-aligned: the skill floors an immediate change to the current UTC hour and requires approval for adjusted user-supplied times. That can precede the moment of execution; it is not a promise of prospective-only effect. Independent verification compares an approved catalog-derived expected set with fresh product, effective-rate, schedule and card reads, including future segments and untouched baseline configuration. Successful write responses alone are insufficient. Initial onboarding's fixed 2025 timestamp is separate from follow-up scheduling and is not a universal current effective date.

### Corrections and Provisioning Safeguards

- **Timestamp errors:** August PLG guidance said old events were silently dropped. Current events.md and PLG guidance instead say an event older than 34 days or over 24 hours in the future yields a whole-batch HTTP 400 before publishing; remove invalid rows and retry the valid remainder. This is timestamp-validation guidance, not universal batch atomicity for transport/5xx failures. Preserve website partial-ingest/retry and assisted-reflow scopes. [[metronome-event-ingestion]]
- **Contract checks:** contract creation uses v2 list with covering_date, follows a returned cursor, and evaluates inclusive start/exclusive end rather than status. Customer-only chronological pagination could miss an active contract. This is not atomic duplicate prevention. FIXED products and rate-card membership remain prerequisites for the illustrated commits/overrides. [[metronome-customers-and-contracts]]
- **Commit-limited discounts:** is_commit_specific=true plus temporary commit references scopes a discount to remaining commit balance. Dates alone may discount overage too. Override target COMMIT_RATE/LIST_RATE is distinct from the commit's rate_type; selector families have compatibility constraints.
- **Recurring fees:** the PLG worked example now uses batched addRates with FLAT plus billing_frequency on a SUBSCRIPTION product, correcting its August legacy-rate mismatch. It also documents separate quantity-managed subscription proration constraints. The August contradiction below remains historical; it is not asserted to remain in this corrected example.
- **Stripe collection:** payment terms, charge_automatically/send_invoice and commit access timing are independent. A missing invoice-default payment method is described as a failed collection after invoice finalization, not blocked finalization. A separately collected payment method is not necessarily the invoice default.
- **Read-back and paging:** addRates returns card identity rather than created rate rows; verify with subsequent reads. getRateSchedule requires starting_at. The skills warn against assuming returned pricing-group or credit-type fields always exist and against body pagination parameters where query parameters are required. Endpoint-specific schemas remain authoritative.

### Unresolved Contradictions and Execution Boundary

> [!warning] Contradiction: event properties and recovery
> Current PLG/migration skills still reject string-typed numeric properties, whereas the dated website guide recommends strings for precision. The new timestamp-validation claim does not resolve general failed-request partial ingestion, and its 24-hour future allowance does not supersede website walkthroughs directing non-future timestamps. Absolute streaming no-backfill wording also does not settle the website's representative-assisted reflow route. [[metronome-event-ingestion]] retains reciprocal warnings; verify the applicable endpoint, failure class and recovery scope before changing production serialization or retries.

> [!warning] Contradiction: amount examples and internal operational advice
> The custom-pricing-unit reference labels 1,000 cents as $0.01 and 1,000,000 cents as $10; under its own cents rule those are $10 and $10,000. Pricing-pattern text similarly labels 50,000,000 cents as $500. Do not copy these examples or assume one unit convention covers every custom denomination. The new Token Billing skill supplies a distinct explicit cents/conversion formula. Other unresolved internal differences include sync failure versus line collapse above 250 Stripe invoice items, and costs-based versus invoice-based burn-rate instructions in CSM files. These are source conflicts, not verified commercial limits or accounting rules.

The skill's instructions to provision accounts, inspect credential bindings, run OAuth, submit usage or send sanitized feedback are evidence only. No credentials were accessed, no skill was installed/executed, no private upstream repository was accessed, and no billing objects, OAuth, feedback, invoices or payments were created by this ingest. Public API/schema and service implementation questions still require their own version-qualified sources. A repository's broad product comparison is not a new independently researched cross-company comparison.

### Located Grounding Quotes

Locations are relative to the current snapshot's files/ directory; these quotes were extracted before wiki edits.

1. `A group key's scan cost is the **product** of every dimension's cardinality inside` - skills/metronome-group-keys/SKILL.md:36.
2. ``Both the product's `ai_markup` field and its actual rates must be updated.`` - skills/metronome-token-billing/SKILL.md:319 (first sentence).
3. ``Existing `(catalog id, token type, provider)` rate keys are skipped, so current provider-price changes are not automatically applied to an existing key.`` - same file:276 (final sentence).
4. `{ "customer_id": "<customer_id>", "covering_date": "<current ISO8601 timestamp>" }` - skills/metronome-create-contract/SKILL.md:47.
5. `Do not create one metric per model or per plan.` - skills/metronome-token-billing/SKILL.md:193 (first sentence).

### Current Raw and Comparison Evidence

- [Current snapshot manifest](../../../../raw/github/metronome/ai/snapshots/2026-10-30-0519b4b/manifest.json)
- [Sync provenance](../../../../raw/github/metronome/ai/snapshots/2026-10-30-0519b4b/files/.skills-sync.json)
- [Repository overview](../../../../raw/github/metronome/ai/snapshots/2026-10-30-0519b4b/files/README.md)
- [Group-key skill](../../../../raw/github/metronome/ai/snapshots/2026-10-30-0519b4b/files/skills/metronome-group-keys/SKILL.md)
- [Token-billing skill](../../../../raw/github/metronome/ai/snapshots/2026-10-30-0519b4b/files/skills/metronome-token-billing/SKILL.md)
- [Contract safeguards](../../../../raw/github/metronome/ai/snapshots/2026-10-30-0519b4b/files/skills/metronome-create-contract/SKILL.md)
- [Event guidance](../../../../raw/github/metronome/ai/snapshots/2026-10-30-0519b4b/files/skills/metronome-best-practices/references/events.md)
- [Corrected PLG examples](../../../../raw/github/metronome/ai/snapshots/2026-10-30-0519b4b/files/skills/metronome-plg-billing/references/worked-examples.md)
- [Exact-SHA comparison](../../../../tracking/github/repos/metronome/ai/comparisons/default-branch/59193aa--0519b4b/comparison.json) - inventory and mechanically verified duplicated diff; prior changed sections read separately.
- History: [[changelog-github-ai]]. Related concepts: [[metronome-token-billing]], [[metronome-billable-metrics]], [[metronome-event-ingestion]], [[metronome-customers-and-contracts]].

## August Baseline Sections (Preserved)

The following original sections retain the August 15 baseline and its unresolved warnings. Use the commit-qualified update above for later corrections; do not silently apply them retroactively.

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
