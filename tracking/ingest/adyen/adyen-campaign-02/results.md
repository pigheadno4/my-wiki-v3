# Adyen C02 results

Status: **COMPLETE — local wiki promotion validated**.

- Approved scope: exact 50-page General Docs manifest and provider dispatch authorization, activated by the user's C2 approval on 2026-10-12.
- 50/50 promoted; 47 first-pass full-review approvals, 3 independently approved targeted second attempts, 0 rejected jobs and 0 repeated full reviews.
- 17 concepts touched, 9 new. Adyen source_count 114 (100 website + 14 GitHub).
- 100 fixed queries plus three complete-raw coordinator exemplars. Structural close and typed validation: PASS; 69 typed files. Raw hashes unchanged.
- Two bounded shared reconciliations, with separate semantic approvals; no default third read of every source.
- Models: gpt-6-sol medium workers and gpt-6-sol high independent reviewers; at most ten shared active child slots, coordinator excluded. Delegates were repository-read-only.

## Timing

Runtime started: 2026-10-12T15:34:09Z (2026-10-12 local).
Runtime completed: 2026-10-12T16:06:01Z (2026-10-13 local).
Wall interval: 31.9 minutes. The run crossed local midnight; one reviewer turn failed and was resumed. This is elapsed wall time, not uninterrupted model-active throughput. Existing runtime events, attempt files and promotion timestamps were retained; the event stream has no per-event timestamps, so no invented stage-duration breakdown is reported.

## Evidence

- [Exact manifest](manifest.json), SHA-256 `17afb5bd8400b6cc93a7aa0bf115b91666c890dac36d0fbf2ebed08367e7beca`.
- [Authorization](authorization.md) and [provider dispatch contract](dispatch-contract.md).
- [Fixed retrieval queries](query-audit.md), [exemplars](exemplar-audit.md), [structural close](close-validation.md), [typed validator output](typed-validation.txt).
- [Canonical promotions](promotions.json), [runtime monitor](monitor.md), [Giving reconciliation](giving-reconciliation.md), [Account Updater reconciliation](account-updater-reconciliation.md).

Commit and push remain separately gated. No new campaign execution is implied.
