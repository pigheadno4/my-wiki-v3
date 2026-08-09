# Metronome Campaign 13 Selection Review

- Status: **stopped calibration - audit gate failed; no promotion**
- Purpose: isolate the Luna Max sampled-review optimization; selective-ingest routing remains frozen.
- Selection method: the first ten guide pages in the current pending-source queue, preserving path order. This avoids using unapproved semantic classification to choose easy pages.
- Inspection performed: path, source URL, first heading, line count, and SHA-256 only. No complete raw-body read and no ingest occurred.
- Runtime: one coordinator, at most three read-only Luna Max workers, and independent Sol full review for the fixed three-page sample only.
- Promotion gate: no candidate is promoted until all three audit jobs pass.

| # | Job | Lines | Review level | Audit rationale |
| ---: | --- | ---: | --- | --- |
| 1 | `manage-customer-lifecycle` | 260 | `mechanical` | — |
| 2 | `provision-a-customer` | 316 | `independent` | ordinary guide sample |
| 3 | `customer-dashboards-and-reporting` | 711 | `independent` | longest selected page |
| 4 | `create-alert-specifiers` | 254 | `mechanical` | — |
| 5 | `system-notifications` | 388 | `mechanical` | — |
| 6 | `threshold-notifications` | 244 | `independent` | standard-length sample |
| 7 | `api-quickstart` | 435 | `mechanical` | — |
| 8 | `how-invoicing-works` | 244 | `mechanical` | — |
| 9 | `non-monotonically-increasing-metrics` | 213 | `mechanical` | — |
| 10 | `packages-overview` | 193 | `mechanical` | — |

The approval authorized campaign initialization, complete reads of only these ten
raw pages by their assigned workers, and Sol complete-source review of only the
three named audit jobs. It does not authorize selective-routing migration,
other raw reads, or cross-PSP rollout.

## Outcome

- The approved manifest ran on 2026-08-04.
- Two audit candidates received independent complete-source review; both
  required material semantic or grounding corrections.
- Two non-audit candidates passed deterministic validation but were not
  promoted because the audit gate failed.
- Remaining jobs were not dispatched, and no candidate or shared suggestion
  changed the canonical wiki.
- Do not resume this campaign or initialize another `audit_only` campaign.
