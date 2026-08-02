# Metronome Campaign 12 Selective-Ingest Pilot Monitor

Coordinator-owned execution monitor for the approved exact manifest.

Pilot state: running
Started at: 2026-08-02T13:55:23Z
Completed at: pending
Complete raw reads: 0
Canonical sources promoted: 0

## State vocabulary

`pending` -> `running` -> `candidate_ready`/`reviewing` -> `approved`/`failed`

## Task states

| Job | Pilot action | State |
| --- | --- | --- |
| `custom-fields-overview` | `generate_source` | `pending` |
| `create-custom-field-key` | `audit_raw_reference` | `pending` |
| `delete-custom-field-key` | `review_triage` | `pending` |
