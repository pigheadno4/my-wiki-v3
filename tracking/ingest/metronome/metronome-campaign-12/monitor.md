# Metronome Campaign 12 Selective-Ingest Pilot Monitor

Coordinator-owned execution monitor for the approved exact manifest.

Pilot state: complete
Started at: 2026-08-02T13:55:23Z
Completed at: 2026-08-02T14:59:33Z
Complete raw reads: 5
Canonical sources promoted: 1
Approved pilot tasks: 3
Unresolved running states: 0
Final verdict: `revise_routing_rule`

## State vocabulary

`pending` -> `running` -> `candidate_ready`/`reviewing` -> `approved`/`failed`; all three task rows are terminal.

## Task states

| Job | Pilot action | State | Agent | Reviewer | Last event |
| --- | --- | --- | --- | --- | --- |
| `custom-fields-overview` | `generate_source` | `approved` | `/root/c12_overview_worker` | `/root/c12_overview_reviewer` | attempt 2 targeted review approved |
| `create-custom-field-key` | `audit_raw_reference` | `approved` | `/root/c12_create_auditor` | n/a | audit validated; pilot miss recorded (source_required) |
| `delete-custom-field-key` | `review_triage` | `approved` | `/root/c12_delete_triage` | `/root/c12_delete_reviewer` | final disposition source_required; reviewer agrees with worker |
