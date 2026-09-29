# Braintree C20 execution notes

Status: COMPLETE. The exact ten-page manifest was approved and initialized on
2026-09-27. Runtime started `2026-09-27T12:32:02Z` and completed
`2026-09-27T13:18:07Z`: **46m05s wall clock**. Worker, reviewer, promotion and
query-audit windows overlap; journal events do not justify invented per-stage
durations.

The ten fraud-tool and Control Panel security pages held 1,060 file lines.
Eight initial reviews passed. Chargeback Protection needed a narrow correction
to avoid reversing the raw's unusual indemnity wording. Effortless needed the
conditional post-evidence information request. Both passed targeted review;
no extra full-source retry was required. Five fixed query groups passed 20/20.
The Group E gap sweep exposed a direct bypass-support conflict between two
collected Braintree pages; one bounded concept/index warning preserves the
conflict without guessing current behavior.

C20 took **6m37s longer** than C19's 39m28s despite fewer targeted retries.
The record supports only total elapsed time, not a per-stage cause. Keep the
existing bounded quote check and targeted review; do not add another validator
or reporting layer based on one campaign. No new campaign, commit or push
follows from this closure.
