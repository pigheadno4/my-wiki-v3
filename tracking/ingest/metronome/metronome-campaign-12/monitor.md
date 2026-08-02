# Metronome Campaign 12 Selective-Ingest Pilot Monitor

Coordinator-owned execution monitor for the approved exact manifest.

Pilot state: running
Started at: 2026-08-02T13:55:23Z
Completed at: pending
Complete raw reads: 5
Canonical sources promoted: 0

## State vocabulary

`pending` -> `running` -> `candidate_ready`/`reviewing` -> `approved`/`failed`

## Task states

| Job | Pilot action | State | Agent | Reviewer | Last event |
| --- | --- | --- | --- | --- | --- |
| `custom-fields-overview` | `generate_source` | `approved` | `/root/c12_overview_worker` | `/root/c12_overview_reviewer` | attempt 2 targeted review approved |
| `create-custom-field-key` | `audit_raw_reference` | `approved` | `/root/c12_create_auditor` | n/a | audit validated; pilot miss recorded (source_required) |
| `delete-custom-field-key` | `review_triage` | `approved` | `/root/c12_delete_triage` | `/root/c12_delete_reviewer` | final disposition source_required; reviewer agrees with worker |
