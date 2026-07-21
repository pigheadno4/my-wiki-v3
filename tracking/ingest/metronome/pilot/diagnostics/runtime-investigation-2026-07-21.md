# Metronome Model Runtime Investigation — 2026-07-21

## Decision

**Keep bulk ingestion and the enterprise comparison suspended.** The failures are not
evidence that Luna or Terra lacks summarization quality. Both models are reaching the
Codex runtime, but the current live path does not complete nontrivial grounded evidence
synthesis under the Metronome worker contract.

The smallest accurate failure boundary is:

> After the prompt and evidence reach the model, a grounded synthesis request can stop
> producing model events and never publish a final response. The same CLI can still
> complete trivial structured responses, including a response constrained by the full
> v3 JSON schema.

The local evidence cannot distinguish a client continuation defect from a remote
inference or routing defect because the CLI emits no terminal service error or request
identifier during the stall.

## Controlled Results

| Probe | Model and input | Contract | Result |
| --- | --- | --- | --- |
| Replacement health probe | Luna/high, fixed prompt | Tiny `{status: ok}` schema | Passed in 4.771208 seconds |
| Enterprise job 1a | Luna/high, staged 88-line page | Current evidence prompt and v3 schema | Read the full raw page, then timed out at 900 seconds |
| Enterprise job 1b | Terra/medium, staged 88-line page | Current evidence prompt and v3 schema | Emitted only lifecycle events, then timed out at 900 seconds |
| Tiny-page staged probe | Terra/medium, staged 23-line page | Current evidence prompt and v3 schema | Read the full page, then timed out at 120 seconds |
| Tiny-page staged probe | Luna/high, staged 23-line page | Current evidence prompt and v3 schema | Read the page twice, then timed out at 120 seconds |
| Tiny-page inline probe | Terra/medium, inline 23-line page | Current evidence prompt and v3 schema | No tool call; timed out at 120 seconds |
| Simple evidence probe | Terra/medium, inline 23-line page | Evidence check and tiny schema | Passed in 8.781218 seconds |
| Full-schema echo probe | Terra/medium, inline explicit object | Full v3 schema without synthesis | Passed and matched exactly in 10.617419 seconds |
| Historical-prompt probe | Terra/medium, staged 23-line page | Pre-hardening evidence prompt and full v3 schema | Timed out at 120 seconds |

The two tiny-page production-worker probes have immutable failed receipts under:

- `runs/runtime-probe-terra-guides-home/terra-guides-home-20260721-01`
- `runs/runtime-probe-luna-guides-home/luna-guides-home-20260721-01`
- `runs/runtime-probe-terra-guides-home/terra-guides-home-inline-20260721-01`

The three narrower exploratory probes are under `diagnostics/runtime-probes/`. They are
runtime-boundary evidence, not canonical ingestion receipts.

## What The Evidence Rules Out

- **Model selection alone:** Luna and Terra reproduce the stall.
- **Raw-page length alone:** both fail on the 23-line corpus minimum.
- **The staged-file tool call alone:** Terra also fails with inline evidence and no tool
  event.
- **The v3 JSON schema alone:** Terra reproduced an explicit object matching the full
  schema in 10.617419 seconds.
- **General model or authentication unavailability:** Terra completed two bounded
  structured probes.
- **The recent prompt-hardening edits alone:** the historical prompt also stalls in the
  current runtime.
- **A deterministic worker timeout or cleanup defect:** every timed-out worker sent
  `SIGTERM`, exited without escalation, closed its pipes, and published a terminal
  receipt.

## Model Registry Observation

The original Luna and Terra attempts logged
`codex_models_manager::manager: failed to refresh available models`. During the targeted
probes, `models_cache.json` was refreshed at process termination. This is correlated
runtime evidence, but it is not a sufficient root cause: the matching Luna tiny-page
probe still failed after the cache had just refreshed, and the passing probes used the
same CLI executable and model registry.

## Operational Consequence

The existing tiny health probe is necessary but not sufficient. It proves only model
reachability and trivial schema output; it does not exercise grounded synthesis. Do not
use it by itself to authorize more full-page jobs.

Before resuming ingestion, add a separate **grounded-synthesis probe** that:

1. uses a short immutable evidence fixture;
2. requires at least one grounded extracted fact, not a fixed echo;
3. has a short timeout and immutable receipt;
4. must pass for the exact model, CLI executable, and runner provenance; and
5. invalidates on CLI, prompt, schema, or runner changes.

Do not increase the 900-second timeout or retry bulk jobs as a workaround. The existing
failures show a lack of forward progress, not merely a slightly slow successful path.
