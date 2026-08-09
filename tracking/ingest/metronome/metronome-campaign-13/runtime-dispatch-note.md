# Campaign 13 Runtime Dispatch Note

Date: 2026-08-04

Campaign 13 proved that the CLI custom-agent path can spawn and complete
`gpt-5.6-luna` workers at maximum reasoning effort. It did not prove that Luna
Max is safe for sampled-review production ingest: both independently reviewed
audit candidates require full-source revision, so promotion is held and no new
jobs are being dispatched pending a coordinator decision.

## Runtime evidence

- Native `spawn_agent` still rejects `gpt-5.6-luna`; it exposes Sol and Terra
  overrides only. Luna is available through a CLI parent with a custom role.
- Three simultaneous Sol-low CLI parents with a parent output schema did not
  reach child dispatch within ten minutes. This was a parent-runtime failure,
  not a Luna failure.
- The minimized known-good form used `--enable multi_agent`,
  `--ignore-user-config`, `--strict-config`, no parent output schema, and the
  `luna_ingest_worker` custom role. Parent `019fcd05-c2d5-7ec3-8674-b5772d385cc2`
  spawned child `019fcd06-00c5-73b1-bb0f-f23e115371f9`; child metadata records
  `model = gpt-5.6-luna` and `effort = max`.
- Two parents subsequently ran in parallel and both spawned confirmed Luna Max
  children. Parent event streams still showed empty `wait` receiver lists;
  child session metadata and final result files are the dispatch authority.
- Model-stream disconnects recovered automatically but materially increased
  wall-clock time. Completed pages took roughly five to eleven minutes in this
  run.

## Quality evidence

- `manage-customer-lifecycle` and `create-alert-specifiers` passed deterministic
  worker-result validation and are mechanically approved, but are not promoted.
- Independent Sol review of `provision-a-customer` found a material archival
  semantic error, insufficient quote coverage, missing boundaries, and invalid
  or duplicate concept suggestions. It is queued for a full retry.
- Independent Sol review of `customer-dashboards-and-reporting` found overstated
  invoice-breakdown cardinality and missed contradictions inside the guide's
  illustrative balance and chart pseudocode. It is queued for a full retry.
- Because two audit pages failed, the campaign remains active with promotion
  held. The remaining queued pages were not started, and the failure does not
  trigger full review of every non-audit page automatically.

## Recovery point

Use `monitor.md`, `jobs.json`, and the immutable attempt artifacts as the
coordinator state. Do not interpret an empty parent `wait` receiver list as a
failed dispatch. Before resuming, decide whether to retry the two audit pages
with Luna Max plus their explicit corrections, or end the pilot with a verdict
that independent review cannot yet be removed.
