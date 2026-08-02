# Metronome Campaign 12 Selective-Ingest Pilot Monitor

Coordinator-owned execution monitor for the approved exact manifest.

Pilot state: running
Started at: 2026-08-02T13:55:23Z
Completed at: pending
Complete raw reads: 3
Canonical sources promoted: 0

## State vocabulary

`pending` -> `running` -> `candidate_ready`/`reviewing` -> `approved`/`failed`

## Task states

| Job | Pilot action | State | Agent | Last event |
| --- | --- | --- | --- | --- |
| `custom-fields-overview` | `generate_source` | `candidate_ready` | `/root/c12_overview_worker` | candidate validated; awaiting independent review |
| `create-custom-field-key` | `audit_raw_reference` | `approved` | `/root/c12_create_auditor` | audit validated; pilot miss recorded (source_required) |
| `delete-custom-field-key` | `review_triage` | `candidate_ready` | `/root/c12_delete_triage` | decision validated (source_required); awaiting independent review |
