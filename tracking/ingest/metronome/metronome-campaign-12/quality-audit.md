# Metronome Campaign 12 Selective-Ingest Pilot Quality Audit

Final verdict: `revise_routing_rule`

The independently approved Custom Fields overview is promoted, but the create-key audit disproved the pilot's initial `raw_reference` classification. This pilot does not authorize cross-provider rollout.

## Classification outcomes

| Job | Initial disposition | Final disposition | Evidence |
| --- | --- | --- | --- |
| `create-custom-field-key` | `raw_reference` | `source_required` | `attempts/create-custom-field-key/attempt-1/audit.json`; the complete audit found required request fields, uniqueness failure behavior, invoice propagation, and supported managed entities that are durable API-contract facts. |
| `delete-custom-field-key` | `semantic_triage` | `source_required` | `attempts/delete-custom-field-key/attempt-1/decision.json` and `attempts/delete-custom-field-key/attempt-1/review.json`; worker and reviewer independently selected `source_required`. |

The exact classification miss is that a mechanical-looking create endpoint was routed as navigation-only even though it is the sole evidence for required request fields and durable failure and propagation behavior.

## Complete-read accounting

Five complete reads were performed:

1. Overview source-generation read, recorded in `attempts/custom-fields-overview/attempt-2/receipt.json`.
2. Independent complete overview review, recorded in `attempts/custom-fields-overview/attempt-1/review.json`.
3. Create-key raw-reference audit, recorded in `attempts/create-custom-field-key/attempt-1/audit.json`.
4. Delete-key semantic-triage worker read, recorded in `attempts/delete-custom-field-key/attempt-1/decision.json`.
5. Independent delete-key decision review, recorded in `attempts/delete-custom-field-key/attempt-1/review.json`.

Source retry reads: 0. The overview attempt-2 review was a targeted unchanged-hash review with `complete_raw_read: false`, so it did not add a complete read.

The raw bodies for `list-custom-field-keys`, `set-custom-field-values`, and `delete-custom-fields` were not read. They remain navigation-only links in this pilot.

## Overview promotion and evidence separation

- Approved candidate: `attempts/custom-fields-overview/attempt-2/candidate.md`
- Canonical source: `wiki/sources/metronome/source-metronome-api-reference-custom-fields.md`
- Candidate/source SHA-256: `8b8db7bea73988382636df09542e6dee6d79943f74bf024953c193f3c9679828`
- Byte identity: pass (`cmp` exit 0).
- Factual evidence: only `metronome/api-reference/custom-fields-2026-07-13.md` appears in `raw_files` and `## Raw Sources`.
- Navigation evidence: all five endpoint snapshots appear only under `## Related raw API references`, and every entry is labelled `raw reference; not summarized`.
- Source boundary: pass. The overview source contains no endpoint method, request/response schema, or endpoint-specific behavior derived from the navigation-only pages.
- Concept boundary: pass. `metronome-custom-fields.md` uses overview facts only and explicitly delegates endpoint methods, schemas, and behavior to complete reads of the relevant API references.

## Fixed query results

### 1. Overview role

- Query: `What are Metronome Custom Fields and what role does the overview document establish?`
- Answer: Metronome Custom Fields attach metadata such as foreign keys and descriptors to platform objects so Metronome entities can be related to records in external systems. The overview establishes their cross-system context, supported object examples, persistence, uniqueness boundary, and product-to-invoice-line propagation; it does not establish endpoint schemas or methods.
- Evidence route: `wiki/sources/metronome/source-metronome-api-reference-custom-fields.md`
- Verdict: pass.

### 2. Create-key request fields

- Query: `What exact request fields are needed to create a custom-field key?`
- Answer: The request requires `entity`, `key`, and `enforce_uniqueness`. `entity` uses the ManagedEntity schema, `key` is a string, and `enforce_uniqueness` is a boolean.
- Evidence route: supplied prior-complete-read evidence at `/private/tmp/metronome-campaign-12/query-audit/create-key.json`, grounded in `raw/metronome/api-reference/custom-fields/create-a-custom-field-key-2026-07-13.md`.
- Raw reread performed for query: no.
- Verdict: pass.

### 3. Delete-key effect on existing values

- Query: `What happens to existing values when a custom-field key is deleted?`
- Answer: Existing values for that key on entity instances are no longer accessible once the key is deleted.
- Evidence route: supplied prior-complete-read evidence at `/private/tmp/metronome-campaign-12/query-audit/delete-key.json`, grounded in `raw/metronome/api-reference/custom-fields/delete-a-custom-field-key-2026-07-13.md`.
- Raw reread performed for query: no.
- Verdict: pass.

Query total: 3 pass, 0 partial, 0 fail.

## Derived coverage

- Raw documentation pages: 225
- Source summaries: 91
- Raw pages without source summaries: 134

## Close validation

- `python3 scripts/validate_wiki.py wiki/sources/metronome/source-metronome-api-reference-custom-fields.md wiki/concepts/metronome/metronome-custom-fields.md wiki/companies/metronome.md` — pass: `validate_wiki: OK (3 file(s) checked, no issues)`.
- `python3 scripts/validate_metronome_capsule.py` — pass: `225 raw, 91 sources, 134 raw pages without source summaries`; no structural error.
- `python3 -m unittest discover -s tests` — pass: 639 tests ran in 112.029 seconds, `OK`.

The original Task 6 close set ran once, and no failing check required a rerun. After the evidence-label correction, targeted source validation passed and the final integration check reran all 639 tests in 111.731 seconds, `OK`.

## Bounded next decision

Before another small Metronome sample, revise only the initial routing rule so an endpoint page that is the sole evidence for required request fields or durable failure or propagation semantics enters `semantic_triage` instead of defaulting to `raw_reference`. Re-test that one correction on another bounded sample. Do not write a cross-provider routing registry or migration plan unless a later pilot produces an approving verdict.
