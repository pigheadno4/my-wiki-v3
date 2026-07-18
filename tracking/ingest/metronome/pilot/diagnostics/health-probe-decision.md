# Metronome Luna Health Probe Decision

## Current Decision

**PASS — the replacement Luna health gate is satisfied.**

The replacement `gpt-5.6-luna` / `high` probe used immutable run ID
`luna-health-2026-07-18-02` and the fixed 60-second total cap. Enterprise A/B was not
launched and still requires separate explicit authorization.

### Replacement Evidence

- Receipt: `health-probes/luna-health-2026-07-18-02/model-health-probe-receipt.json`
- First actual model event: 4.438755 seconds
- Model/runtime elapsed: 5.304394 seconds
- Total elapsed through receipt validation: 5.562462 seconds
- Process exit: 0
- Cleanup: passed; no termination was required
- Terminal JSON: valid `{"status":"ok"}`
- Receipt publication: atomic and within the deadline
- Runtime metadata and prospective provenance: complete
- Strict enterprise-gate loader: passed
- Terminal manifest: reconciled, including receipt, progress, events, stderr, outputs,
  and prompt/schema snapshots

The replacement receipt has no failures and remains permanently ineligible for canonical
coverage. Its successful health status authorizes consideration of the separately gated
enterprise diagnostic; it does not itself launch or approve that job.

## Prior Failed Probe — Preserved History

**FAIL at the time — enterprise A/B remained suspended.**

The original live `gpt-5.6-luna` / `high` probe used immutable run ID
`luna-health-2026-07-18-01` and the fixed 60-second total cap. That run was not retried;
the later replacement used a new immutable run ID.

## Evidence

- Receipt: `health-probes/luna-health-2026-07-18-01/model-health-probe-receipt.json`
- Model/runtime elapsed: 2.835972 seconds
- Total elapsed through receipt validation: 3.047448 seconds
- First stdout lifecycle event: 0.094716 seconds
- First actual model event: not observed
- Process exit: 1
- Cleanup: passed; no termination was required
- Terminal JSON: absent and invalid
- Receipt publication: atomic and within the deadline
- Runtime metadata: complete

The event stream contains only `thread.started`, `turn.started`, an error, and
`turn.failed`. The runtime rejected the response schema with HTTP 400 because
`properties.status` declared `const: "ok"` without the required JSON Schema
`type: "string"`. Luna therefore never produced model content.

The failed receipt correctly blocked the gate. The recorded event and stderr hashes
were independently recomputed and match the receipt:

- events: `384eb80b88326ff59c15dc0642c8a52abeae9033350115b729e5083938fbb5a2`
- stderr: `1aa26269eb1cc57f86b235a03cda53c004edb5b1e9fc99d4da4f00843293d721`
- prompt: `11bfc765d2ab0301768991263c5f90acc17c3fa8eade3bffc38c106bd76a2321`
- rejected schema: `857d76db2255ddb1f9dff3cd13f544635f706a0a3771a9b12f5f9bee6514d6b7`

## Follow-up

The schema now explicitly declares `status` as a string, with a regression assertion.
This correction is for a future user-approved run only; it does not change the immutable
failed evidence and does not authorize a second probe or enterprise A/B.
