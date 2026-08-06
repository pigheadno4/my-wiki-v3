# Selective Routing Rule Correction Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Prevent endpoint pages that may uniquely carry durable API semantics from being assigned directly to `raw_reference` without a complete semantic triage read.

**Architecture:** Amend the shared selective-ingest boundary with one narrow metadata-routing exception, then record the Metronome Campaign 12 calibration and its `Create a Custom Field Key` regression example in the provider rule. This is a documentation/rule correction only: no classifier, registry, manifest mutation, corpus reclassification, or new campaign is created.

**Tech Stack:** Markdown rules, repository text checks, existing Metronome capsule validator

## Global Constraints

- Preserve complete English canonical raw collection and the three existing dispositions: `source_required`, `raw_reference`, and `semantic_triage`.
- `semantic_triage` remains a decision gate and may still resolve to `raw_reference`; do not promote every API endpoint.
- Do not change `tracking/ingest/metronome/metronome-campaign-12/manifest.json` or any Campaign 12 evidence.
- Do not build a classifier, routing registry, scheduler, state schema, migration, or new campaign.
- Do not touch unrelated workspace changes, including `CLAUDE copy.md`.

---

### Task 1: Correct the live routing rule and preserve the pilot lesson

**Files:**
- Modify: `rules/ingest.md` (`Selective-ingest routing boundary`)
- Modify: `rules/psp/metronome.md` (after `Campaign 12 selective-ingest pilot authorization`)

**Interfaces:**
- Consumes: the approved routing amendment in `docs/superpowers/specs/2026-08-02-selective-psp-ingest-routing-design.md`
- Produces: one shared cross-provider triage rule and one Metronome-specific regression example

- [x] **Step 1: Add the narrow shared triage trigger**

  In `rules/ingest.md`, after the evidence/navigation boundary and before the promotion paragraph, state that an endpoint must enter `semantic_triage` when metadata cannot rule out that it is the sole authority for any of these durable facts:

  ```text
  required request fields; durable failure or propagation behavior;
  deletion or lifecycle semantics; uniqueness or idempotency constraints;
  state-transition semantics
  ```

  Also state both limits explicitly:

  ```text
  CRUD shape or schema-heavy content alone cannot justify raw_reference.
  Triage may still resolve to raw_reference when a complete read finds no
  unique durable facts that warrant a curated source.
  ```

- [x] **Step 2: Record the Metronome calibration and regression example**

  Add a `## Post-Campaign 12 selective-routing calibration` section to `rules/psp/metronome.md` containing:

  ```text
  verdict = revise_routing_rule
  unsafe old route = Create a Custom Field Key -> raw_reference
  corrected metadata route = Create a Custom Field Key -> semantic_triage
  observed complete-read result = source_required
  ```

  Explain that the sampled page uniquely carried required-field, failure, uniqueness, managed-entity, and invoice-propagation facts. Explicitly preserve the boundaries that this does not promote every endpoint, alter the completed Campaign 12 manifest, reclassify the remaining corpus, create a registry, or authorize another campaign.

- [x] **Step 3: Verify the corrected rule is present and bounded**

  Run:

  ```bash
  rg -n "sole authority|required request fields|durable failure|propagation|uniqueness|idempotency|state-transition|may still resolve to.*raw_reference" rules/ingest.md
  rg -n "Post-Campaign 12|revise_routing_rule|Create a Custom Field Key|semantic_triage|source_required|remaining corpus|new campaign" rules/psp/metronome.md
  ```

  Expected: the common rule contains the durable-fact trigger and the explicit non-promotion limit; the provider rule contains the complete worked regression and scope limits.

- [x] **Step 4: Run scoped repository validation**

  Run:

  ```bash
  git diff --check
  python3 scripts/validate_metronome_capsule.py
  git status --short
  ```

  Expected: `git diff --check` exits 0; the existing Metronome capsule validator passes; only the two intended rule files and this plan are changed, aside from the pre-existing untracked `CLAUDE copy.md`.

- [x] **Step 5: Review the final diff and commit only the rule correction**

  Run:

  ```bash
  git diff -- rules/ingest.md rules/psp/metronome.md docs/superpowers/plans/2026-08-03-selective-routing-rule-correction.md
  git add rules/ingest.md rules/psp/metronome.md docs/superpowers/plans/2026-08-03-selective-routing-rule-correction.md
  git commit -m "docs: correct selective endpoint routing rule"
  ```

  Expected: the commit contains the approved narrow rule correction, the Metronome regression example, and this execution plan only.
