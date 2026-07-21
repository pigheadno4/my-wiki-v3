# Metronome Terra Comparison — Job 1 Sol Review

## Decision

**STOP — no canonical promotion and no job 2 launch.**

Terra produced no candidate to compare with Luna. The current evidence supports a shared
long-job runtime investigation, not a model-quality routing decision.

## Evidence Reviewed

- Complete raw page: `raw/metronome/guides/events/design-usage-events-2026-07-13.md`
- Historical Luna output: `runs/pilot-luna-design-usage-events-shadow/model-output.json`
- Historical Luna receipt: `runs/pilot-luna-design-usage-events-shadow/model-worker-receipt.json`
- Gated Luna failure: `runs/pilot-luna-design-usage-events-shadow/luna-design-usage-events-shadow-20260721-01/model-worker-receipt.json`
- Gated Terra failure: `runs/pilot-terra-design-usage-events/terra-design-usage-events-20260721-01/model-worker-receipt.json`
- Passing health probe: `diagnostics/health-probes/luna-health-2026-07-21-01/model-health-probe-receipt.json`

Both worker receipts pass the deterministic receipt validator, and both terminal artifact
manifests reconcile.

## Runtime Comparison

| Evidence | Furthest observed activity | Result |
| --- | --- | --- |
| Health probe, Luna/high | Model message at 3.591206 seconds | Passed in 4.771208 seconds |
| Job 1a, Luna/high | Read the complete 88-line raw file, then stalled | Timed out at 900 seconds; no output |
| Job 1b, Terra/medium | `thread.started` and `turn.started` only | Timed out at 900 seconds; no output |

Both full-page attempts used the same Codex executable and CLI version
`codex-cli 0.145.0-alpha.27`, the same staged-file delivery mode, the same raw SHA-256,
and the same output-schema SHA-256. Terra never reached the raw-read boundary, while Luna
crossed it before stalling. This rules out a Terra content-quality comparison and points
to the shared long-job runtime or service path as the next investigation boundary. It
does not prove which remote component stopped progressing.

## Full-Raw Grounding Review

The historical Luna candidate is substantively grounded in the raw page:

- Lines 11–17 state the three design principles and CDN scenario.
- Lines 21–39 support backward design, deferred pricing, minimum event fields, and the
  example bytes-summing metric.
- Lines 45–52 support event timing choices, available-system constraints, hourly
  summaries, central customer lookup, and notification cadence.
- Lines 56–78 support sending additional fields and grouping usage by domain.
- Lines 80–88 support regional pricing and the warning that billable metrics are not
  retroactive.

No critical factual omission or unsupported substantive claim was found in the
historical Luna output. It is not canonical-ready: its suggested tags use spaces rather
than kebab-case, and its Related section retains a concept-audit placeholder. A future
successful ingest cycle should audit the existing `metronome-billable-metrics` and
`metronome-usage-based-billing` concepts and decide whether a dedicated
`metronome-usage-events` concept is warranted before creating the source page.

## Acceptance-Gate Result

- Terra output quality: not measurable; no output exists.
- Terra token cost: unavailable because the event stream omitted usage.
- Sol repair count/time: not applicable; there is no Terra candidate to repair.
- Canonical source promotion: blocked.
- Job 2: blocked.

Do not retry either model or change input mode as an untested workaround within this
pilot checkpoint. First investigate why the same long-job runtime stopped progressing at
different model-event boundaries even though the short health probe passed.
