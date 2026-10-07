---
title: "GitHub changelog: stripe/stripe-cli"
type: source
date_ingested: 2026-08-14
date_updated: 2026-10-07
original_format: github-repo
raw_files:
  - "github/stripe/stripe-cli/snapshots/2026-10-06-a915fc6/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-eea8a71/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-1090068/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-4a5d9d6/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-d9aaa68/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-c78e4ab/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-150fa3f/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-6056ace/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-07050f2/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-ba4ee1f/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-f5f390b/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-2f3420a/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-53f08e9/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/manifest.json"
  - "github/stripe/stripe-cli/snapshots/2026-08-14-a6f4065/manifest.json"
tags: [stripe, stripe-cli, developer-tools, telemetry, changelog, github-repository]
---

## Overview

Package-qualified retained history for `stripe/stripe-cli`. Durable implementation knowledge belongs in [[source-github-stripe-cli]].

## Initial Baseline — `stripe-cli@1.50.0` (2026-08-13)

| Package | Version | Tag | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `stripe-cli` | `1.50.0` | `v1.50.0` | `a6f40658b99e4142fd63b2e4b560aa9c7ae337b1` | Full |

**Baseline established:** direct and generated API commands, request controls and dry run, fixture execution, synthetic event triggers, webhook and thin-event listening/forwarding, OAuth and account contexts, request-log transport, and telemetry.

**Release-specific change:** the upstream notes contain one item: capture agent host and self-reported agent identifiers in telemetry. The baseline's other capabilities must not be attributed as newly introduced by `1.50.0`.

**Collection exception:** the immutable first snapshot includes 28 Go test files. Future capsules use the corrected policy that excludes Go tests; this policy reduction is not an upstream product change.

**Future comparison rule:** compare package-qualified stable releases against `stripe-cli@1.50.0`. Use delta ingest for bounded command, fixture, webhook, request, authentication, or telemetry changes with complete classified evidence. Use additive full ingest for a major version, broad architecture change, incompatible command or authentication behavior, missing prior evidence, or capsule-policy change. Preserve older-version findings in the cumulative source.

## `stripe-cli@1.50.0` to `stripe-cli@1.50.1` (2026-08-14)

- **Identity:** tag `v1.50.1`, SHA `4a89968de966ca1978eb4c8da558367233769b4c`; collected 2026-10-06, ingested 2026-10-07.
- **Mode:** user-approved additive full, overriding the collector's contained-patch delta recommendation because authentication safeguards and the capsule-policy boundary deserve full treatment. The one-time focused-reading exception covered all 32 added/modified retained files, affected prior code, the full comparison and cumulative wiki history; inventories, 85 unchanged files and 28 excluded prior tests were mechanically verified. Older findings remain intact.
- **OAuth security:** access-service destinations accept only the exact production/QA origin; credential-bearing requests do not follow redirects. Device/reauth browser destinations require HTTPS and the corresponding trusted host.
- **Login:** `--new-session` attempts to revoke the previous stored OAuth refresh token before login. Revocation errors warn and continue; do not claim guaranteed old-session invalidation.
- **Credential resolution:** plugin mode fallback moves from a private request helper to `Profile.ResolveCredentialsForAnyMode`. The fallback behavior is not newly introduced; payment/listener mode controls remain.
- **Errors:** many retained error origins gain categories; trigger failures preserve wrapped causes. The underlying category/analyzer implementation is not retained.
- **Telemetry:** adds `agent_host_raw`; host-mapping changes for Codex TypeScript and Claude Desktop are note-backed, not implementation-audited. Existing telemetry opt-outs remain.
- **Transport:** expands home-relative Unix-socket paths; WebSockets support dev-host socket routing alongside public-host HTTP CONNECT/TLS when both socket and proxy are configured. This is internal developer tooling, not merchant checkout functionality.
- **Other announcements:** feedback command and CoreCLIHelper credential RPC. Their full implementation/contract is outside the capsule and requires pinned supplemental evidence for detailed queries.
- **Migration impact:** noncanonical `--access-base` overrides are rejected; new-session callers must account for attempted revocation. No new checkout API or payment-method capability is established. The 28 absent Go tests are policy exclusions, not upstream deletions.
- **Updated sections:** cumulative source's version `1.50.1` section and evidence boundary, [[stripe-cli]] authentication/tooling guidance, Stripe company and provider catalog. No cross-company comparison or factual contradiction was identified.

### `1.50.1` Evidence

- [Release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.1/2026-10-06/manifest.json)
- [Release notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.1/2026-10-06/release-notes.md)
- [Snapshot manifest](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/manifest.json)
- [Comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.0--1.50.1/comparison.md)
- [OAuth checks](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/files/pkg/login/access_base.go)
- [Login](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/files/pkg/cmd/login.go)
- [Profile helper](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/files/pkg/config/profile.go)
- [Telemetry](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/files/pkg/stripe/analytics_telemetry.go)
- [WebSocket routing](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a89968/files/pkg/websocket/client.go)

## `stripe-cli@1.50.1` to `stripe-cli@1.50.2` (2026-08-19)

- **Identity:** `v1.50.2`, SHA `8348b889fb48c1cf3ed36452ad1885cc195e9330`; collected 2026-10-06, ingested 2026-10-07.
- **Mode/read:** delta; loop-wide user-approved focused reading. All 18 changed retained files and the full comparison read; inventories/hashes and 99 unchanged files checked mechanically; prior history preserved.
- **Updates:** confirmed profile removal (including legacy dotted names), once-per-process dotted-name warnings, reauthorization polling/context summary, and sandbox terminology. Reauthorization compares ID/name/modes, not scopes; unchanged authorization can time out, and timeout/cancel return nil.
- **Migration:** interactive removal asks for confirmation; scripts must supply `--confirm`. Do not interpret deletion as remote revocation or the wording change as an API-mode/schema change.
- **Note-only:** GitHub Actions hardening and upgrade-test retries/Slack notification, outside the capsule.
- **Sections:** source `1.50.2`, concept, company/catalog and log; no cross-company comparison or factual contradiction identified.
- [Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.2/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.2/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.1--1.50.2/comparison.md), [reauth code](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-8348b88/files/pkg/login/oauth_reauth.go).

## `stripe-cli@1.50.2` to `stripe-cli@1.50.3` (2026-08-19)

- **Identity:** `v1.50.3`, SHA `53f08e96b9dfa82bd86670aa34ff50bab60abaac`; collected 2026-10-06, ingested 2026-10-07.
- **Mode/read:** delta with approved focused reading; release/comparison and cumulative pages read, both inventories and all 117 unchanged retained files hash-verified. Historical knowledge preserved.
- **Update:** release-note announcement of `ResolveCredentialsForAnyMode` plugin RPC. Four changed plugin handler/protocol files are policy-excluded. No detailed RPC contract or merchant checkout change is established.
- **Migration/sections:** no retained implementation migration; source announcement/evidence boundary, concept, company/catalog and log updated. No cross-company comparison or factual contradiction identified.
- [Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-53f08e9/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.3/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.3/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.2--1.50.3/comparison.md).

## `stripe-cli@1.50.3` to `stripe-cli@1.50.4` (2026-08-21)

- **Identity:** `v1.50.4`, SHA `2f3420a7e878cd883a04be5ba3d47e47243e1214`; collected 2026-10-06, ingested 2026-10-07.
- **Mode/read:** approved focused delta; 4 changed retained files and complete comparison/cumulative pages read; inventories and 114 unchanged files checked mechanically. Older knowledge preserved.
- **Updates/impact:** OAuth whoami adds optional identity/role and fetched account names. Optional identity failures are ignored, account-fetch errors fail; OAuth bypasses --format json and contradicts the no-network help claim. Provision alias, docs-search rendering, sandbox messaging and plugin hints are note-backed with excluded implementations.
- **Sections:** additive source/changelog, existing concept, company/catalog and log. The whoami help/implementation contradiction is flagged in both source and concept. No cross-company comparison warranted.
- [Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-2f3420a/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.4/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.4/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.3--1.50.4/comparison.md).

## `stripe-cli@1.50.4` to `stripe-cli@1.50.5` (2026-08-24)

- **Identity:** `v1.50.5`, SHA `f5f390bc37295ec9b69b94a0ca1c195448a30042`; collected 2026-10-06, ingested 2026-10-07.
- **Mode/read:** approved focused delta; 1 changed retained files and complete comparison/cumulative pages read; inventories and 117 unchanged files checked mechanically. Older knowledge preserved.
- **Updates/impact:** OAuth login prompt reordered/reformatted; retained auth-flow logic unchanged. Notes announce Codex detection and docs scroll restoration, with implementation gaps explicit. No payment integration migration established.
- **Sections:** additive source/changelog, existing concept, company/catalog and log. No new factual contradiction identified; prior whoami warning preserved. No cross-company comparison warranted.
- [Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-f5f390b/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.5/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.5/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.4--1.50.5/comparison.md).

## `stripe-cli@1.50.5` to `stripe-cli@1.50.6` (2026-08-26)

- **Identity:** `v1.50.6`, SHA `ba4ee1f3a94ee871280cf56724b36e3d0259bc7b`; collected 2026-10-06, ingested 2026-10-07.
- **Mode/read:** approved focused delta; 4 changed retained files and complete comparison/cumulative pages read; inventories and 114 unchanged files checked mechanically. Older knowledge preserved.
- **Updates/impact:** OAuth JSON support added with an auth-specific schema; no-network/universal-key help claims remain inaccurate. Refresh preserves profile metadata. Plugin metadata carries auto_install/machine_uuid; actual installer and preview Data API guidance are excluded. Scripts should distinguish OAuth and API-key output.
- **Sections:** additive source/changelog, existing concept, company/catalog and log. Prior whoami contradiction is version-qualified: JSON support is fixed, help/schema/network mismatch remains. No cross-company comparison warranted.
- [Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-ba4ee1f/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.6/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.6/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.5--1.50.6/comparison.md).

## Comparison Records

- [1.50.0 to 1.50.1 comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.0--1.50.1/comparison.json)
- [1.50.1 to 1.50.2 comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.1--1.50.2/comparison.json)
- [1.50.2 to 1.50.3 comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.2--1.50.3/comparison.json)
- [1.50.3 to 1.50.4 comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.3--1.50.4/comparison.json)
- [1.50.4 to 1.50.5 comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.4--1.50.5/comparison.json)
- [1.50.5 to 1.50.6 comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.5--1.50.6/comparison.json)

## `stripe-cli@1.50.6` to `stripe-cli@1.50.7` (2026-09-01)

- **Identity:** `v1.50.7`, SHA `14c9c5475d3dbcc73414f743f078cb2287de873b`; collected 2026-10-06, ingested 2026-10-07.
- **Mode/read:** user-approved additive full with focused reading (overrides collector delta); 10 changed retained files and complete comparison/cumulative pages read; inventories and 109 unchanged files checked mechanically. Older knowledge preserved.
- **Updates/impact:** Config-v2 migration library and dual-layout compatibility, unchanged keyring identities, new-profile validation, parsed-host base-URL checks, explicit OAuth switch results and listen 429 classification.
- **Sections:** additive source/changelog, existing concept, company/catalog and log. Qualified the stale no-migration comment and excluded orchestration/plugin/reporting evidence. No cross-company comparison warranted.
- [Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-14c9c54/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.7/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.7/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.6--1.50.7/comparison.md), [comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.6--1.50.7/comparison.json).

## `stripe-cli@1.50.7` to `stripe-cli@1.50.8` (2026-09-01)

- **Identity:** `v1.50.8`, SHA `07050f2f66ec753b37d42671b87e29b4bd5e1253`; collected 2026-10-06, ingested 2026-10-07.
- **Mode/read:** approved focused delta; 1 changed retained files and complete comparison/cumulative pages read; inventories and 118 unchanged files checked mechanically. Older knowledge preserved.
- **Updates/impact:** Plugin metadata recognizes minimum-core-version errors and optionally extracts the upgrade floor; installation enforcement is note-backed with excluded implementation.
- **Sections:** additive source/changelog, existing concept, company/catalog and log. No new contradiction identified; prior qualified findings preserved. No cross-company comparison warranted.
- [Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-07050f2/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.8/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.8/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.7--1.50.8/comparison.md), [comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.7--1.50.8/comparison.json).

## `stripe-cli@1.50.8` to `stripe-cli@1.50.9` (2026-09-02)

- **Identity:** `v1.50.9`, SHA `6056ace7517ccb15c74ceac40d9c619a96e72cde`; collected 2026-10-06, ingested 2026-10-07.
- **Mode/read:** approved focused delta; 1 changed retained files and complete comparison/cumulative pages read; inventories and 118 unchanged files checked mechanically. Older knowledge preserved.
- **Updates/impact:** Telemetry delegates installation detection to a shared helper. Docs context headers, pre-run/telemetry restoration and upgrade-command guidance are note-backed with excluded implementation.
- **Sections:** additive source/changelog, existing concept, company/catalog and log. No new contradiction identified; earlier evidence limitations preserved. No cross-company comparison warranted.
- [Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-6056ace/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.9/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.9/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.8--1.50.9/comparison.md), [comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.8--1.50.9/comparison.json).

## `stripe-cli@1.50.9` to `stripe-cli@1.50.10` (2026-09-02)

- **Identity:** `v1.50.10`, SHA `150fa3f95fe7117561f645878b044f888814242e`; collected 2026-10-06, ingested 2026-10-07.
- **Mode/read:** approved focused delta; 0 changed retained files and complete comparison/cumulative pages read; inventories and 119 unchanged files checked mechanically. Older knowledge preserved.
- **Updates/impact:** Release-note announcement of agent report_usage telemetry command; retained capsule unchanged and detailed command behavior outside collection policy.
- **Sections:** additive source/changelog, existing concept, company/catalog and log. No new contradiction identified; an empty retained diff is explicitly not an unchanged-repository claim. No cross-company comparison warranted.
- [Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-150fa3f/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.10/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.10/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.9--1.50.10/comparison.md), [comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.9--1.50.10/comparison.json).

## `stripe-cli@1.50.10` to `stripe-cli@1.50.11` (2026-09-10)

- **Identity:** `v1.50.11`, SHA `c78e4ab82bc58dc816d0fc7edaaeb3792f8e541c`; collected 2026-10-06, ingested 2026-10-07.
- **Mode/read:** user-approved additive full with focused reading (overrides collector delta); 10 changed retained files and complete comparison/cumulative pages read; inventories and 110 unchanged files checked mechanically. Older knowledge preserved.
- **Updates/impact:** Existing-session login now reauthorizes with a separate non-interactive continuation; completion proxy/cancel limits preserved. Shared device poll/save detaches cancellation after token issuance. API default headers advance, preview events added and uninstall steps documented.
- **Sections:** additive source/changelog, existing concept, company/catalog and log. Qualified the scope-change comment against the actual ID/name/mode signature and distinguished current login behavior from historical informational returns. No cross-company comparison warranted.
- [Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c78e4ab/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.11/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.11/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.10--1.50.11/comparison.md), [comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.10--1.50.11/comparison.json).

## `stripe-cli@1.50.11` to `stripe-cli@1.51.0` (2026-09-17)

- **Identity:** `v1.51.0`, SHA `c856abae2df6f8a32c54b1c0e1bbfbf2abdf261f`; collected 2026-10-06, ingested 2026-10-07.
- **Mode/read:** user-approved additive full with focused reading (overrides collector delta); 22 changed retained files and complete comparison/cumulative pages read; inventories and 98 unchanged files checked mechanically. Older knowledge preserved.
- **Updates/impact:** Explicit webhook payload/source selection and incompatible forwarding/wildcard validation; deprecated thin flags preserved. Preferred switch command with JSON/legacy alias; OAuth whoami near-expiry refresh and corrected help. Configured-endpoint errors propagate, role errors gain guidance; removed-command shims and other excluded tooling remain qualified.
- **Sections:** additive source/changelog, existing concept, company/catalog and log. Historical whoami wording correction and recursive-refresh retry-bound contradiction recorded; reauthorization scope/signature warning preserved. No cross-company comparison warranted.
- [Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-c856aba/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.51.0/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.51.0/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.11--1.51.0/comparison.md), [comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.50.11--1.51.0/comparison.json).

## `stripe-cli@1.51.0` to `stripe-cli@1.51.1` (2026-09-21)

- **Identity:** `v1.51.1`, SHA `d9aaa685aae64dbb32ab735c6e1f7d9c765ed8e4`; collected 2026-10-06, ingested 2026-10-07.
- **Mode/read:** user-approved additive full with focused reading (overrides collector delta); 5 changed retained files and complete comparison/cumulative pages read; inventories and 115 unchanged files checked mechanically. Older knowledge preserved.
- **Updates/impact:** Reusable pending-login discovery/resume/single-check helpers; caller-cancel preservation and persisted expiry. Legacy pending files need a fresh login; network-error cleanup, expiry floor and uncoordinated writers are qualified. Reserved-name profile migration and new-v2-file stamping library added.
- **Sections:** additive source/changelog, existing concept, company/catalog and log. Qualified comments against broader error cleanup, local expiry floor and nonexclusive file creation; earlier contradictions preserved. No cross-company comparison warranted.
- [Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-d9aaa68/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.51.1/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.51.1/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.51.0--1.51.1/comparison.md), [comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.51.0--1.51.1/comparison.json).

## `stripe-cli@1.51.1` to `stripe-cli@1.52.0` (2026-09-24)

- **Identity:** `v1.52.0`, SHA `4a5d9d6c1bb2c70b9403f42847bffc918b7ef6da`; collected 2026-10-06, ingested 2026-10-07.
- **Mode/read:** user-approved additive full with focused reading (overrides collector delta); 3 changed retained files and complete comparison/cumulative pages read; inventories and 117 unchanged files checked mechanically. Older knowledge preserved.
- **Updates/impact:** Automatic binary-update entrypoint hooks; updater verification/recovery is note-backed with excluded implementation. Plugin metadata no longer sends machine_uuid; auto_install remains. Grok setup announced.
- **Sections:** additive source/changelog, existing concept, company/catalog and log. Version-qualified the earlier plugin rollout parameter and separated update wiring from unverified internals; historical warnings preserved. No cross-company comparison warranted.
- [Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-4a5d9d6/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.52.0/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.52.0/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.51.1--1.52.0/comparison.md), [comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.51.1--1.52.0/comparison.json).

## `stripe-cli@1.52.0` to `stripe-cli@1.52.1` (2026-09-29)

- **Identity:** `v1.52.1`, SHA `1090068baae4c3d732fd500a9d3dbe4b94bc91a0`; collected 2026-10-06, ingested 2026-10-07.
- **Mode/read:** approved focused delta; 7 changed retained files and complete comparison/cumulative pages read; inventories and 113 unchanged files checked mechanically. Older knowledge preserved.
- **Updates/impact:** Custom request headers with overwrite and output-disclosure limits; Endive/preview defaults and expanded snapshot/thin event names. Backend plugin-update defaults follow local override precedence; config field deletion and removed invocation-time chmod.
- **Sections:** additive source/changelog, existing concept, company/catalog and log. Version-qualified older plugin default-off behavior and recorded custom-header output/precedence limits; prior warnings preserved. No cross-company comparison warranted.
- [Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-1090068/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.52.1/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.52.1/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.52.0--1.52.1/comparison.md), [comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.52.0--1.52.1/comparison.json).

## `stripe-cli@1.52.1` to `stripe-cli@1.52.2` (2026-09-30)

- **Identity:** `v1.52.2`, SHA `eea8a7190796cca941af52fdd36c8eda0291198c`; collected 2026-10-06, ingested 2026-10-07.
- **Mode/read:** approved focused delta; 5 changed retained files and complete comparison/cumulative pages read; inventories and 115 unchanged files checked mechanically. Older knowledge preserved.
- **Updates/impact:** OAuth server-provided user-code-prefilled URLs with validated fresh flows and pending-session fallback; qualified Accounts v1 fixture error guidance. Boolean normalization/OpenAPI announcements retain excluded-implementation boundaries.
- **Sections:** additive source/changelog, existing concept, company/catalog and log. Qualified the fixture guidance as a broad 400-error hint rather than a verified eligibility diagnosis; earlier warnings preserved. No cross-company comparison warranted.
- [Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-eea8a71/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.52.2/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.52.2/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.52.1--1.52.2/comparison.md), [comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.52.1--1.52.2/comparison.json).

## `stripe-cli@1.52.2` to `stripe-cli@1.53.0` (2026-09-30)

- **Identity:** `v1.53.0`, SHA `a915fc6d89c7d301e0135a97c11656894d66e674`; collected 2026-10-06, ingested 2026-10-07.
- **Mode/read:** approved focused delta; 0 changed retained files and complete comparison/cumulative pages read; inventories and 120 unchanged files checked mechanically. Older knowledge preserved.
- **Updates/impact:** Notes announce stripe version --notes; 120 retained files unchanged. Version command/library/tests are excluded upstream changes, so detailed command behavior requires a pinned supplement.
- **Sections:** additive source/changelog, existing concept, company/catalog and log. Qualified the empty comparison upstream list against the packet's four excluded upstream changes; prior warnings preserved. No cross-company comparison warranted.
- [Snapshot](../../../../raw/github/stripe/stripe-cli/snapshots/2026-10-06-a915fc6/manifest.json), [release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.53.0/2026-10-06/manifest.json), [notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.53.0/2026-10-06/release-notes.md), [comparison](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.52.2--1.53.0/comparison.md), [comparison record](../../../../tracking/github/repos/stripe/stripe-cli/comparisons/stripe-cli/1.52.2--1.53.0/comparison.json).

## Baseline Evidence

- [Release record](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.0/2026-08-14/manifest.json)
- [Release notes](../../../../raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.0/2026-08-14/release-notes.md)
- [Snapshot manifest](../../../../raw/github/stripe/stripe-cli/snapshots/2026-08-14-a6f4065/manifest.json)
- [Telemetry implementation](../../../../raw/github/stripe/stripe-cli/snapshots/2026-08-14-a6f4065/files/pkg/stripe/analytics_telemetry.go)
