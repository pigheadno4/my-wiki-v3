# Coordinator stale artifact handoff

The coordinator submitted `/tmp/braintree-c45-worker-49.json` (attempt 1) while the job was running attempt 2. The runtime correctly failed closed with `worker result does not match the job attempt`.

The worker had already supplied a correct attempt-2 candidate at `/tmp/braintree-c45-worker-49-a2.json`, retained here as `corrected-worker-not-submitted.json`. No new semantic problem was found. Recovery uses the existing retry operation for attempt 3, rechecks the unchanged raw hash, and resubmits the corrected candidate with only the attempt number advanced. Independent review remains targeted against the original attempt-1 finding.

Cause: the coordinator's in-memory list retained old role entries because filtering relied on object identity across serialized store loads. The live list was reconciled by role/position/artifact values; no scheduler, runtime schema or repository code was changed.
