# GitHub Major-Track Audit - 2026-10-16

## Scope and Evidence

Read remote tags for all 47 enabled release-tracked repositories (56 configured
tracks before this fix). No remote checks failed. Commit-tracked and disabled
repositories are outside this audit. Stable here means an exact semantic tag
without a prerelease suffix, not independent proof of a published package.
Package-qualified tags are matched by package namespace; plain tags are eligible
only for single-package semantic-tag repositories.

Eight repositories had stable tags above their highest configured major. The
remaining 39 had no such tags at the time of this check. This is not a claim that
their retained minor/patch versions or default-branch knowledge are current.

## Findings and Disposition

| Repository | Previous highest major | Untracked stable tags | Disposition |
| --- | --- | --- | --- |
| paypal/paypal-android | 2 | 3.0.0, 3.1.0 | v3 track and paths corrected; both releases collected, awaiting ingest approval |
| paypal/paypal-ios | 2 | 3.0.0, 3.1.0, 3.1.1 | Keep gated: Sources/PayPalWebPayments and Demo/Demo/PayPalWebPayments no longer exist |
| stripe/stripe-php | 21 | v22.0.0 | Add package:stripe-php@22; configured roots/includes exist |
| stripe/stripe-node | 22 | v23.0.0 | Add package:stripe@23; configured roots/includes exist |
| stripe/stripe-js | 9 | v10.0.0, v10.1.0 | Add package:@stripe/stripe-js@10; configured roots/includes exist |
| stripe/react-stripe-js | 6 | v7.0.0 | Add package:@stripe/react-stripe-js@7; configured roots/includes exist |
| stripe/stripe-terminal-ios | 5 | 6.0.0 | Keep gated: required Example/Podfile and Example/Podfile.lock no longer exist |
| stripe/stripe-terminal-android | 5 | 6.0.0 | Add package:stripeterminal@6; configured roots/includes exist |

File-tree checks used the first new-major tag at these exact commits:

| Repository | Commit |
| --- | --- |
| paypal/paypal-android | 3540adff974abdc20371d66fe47748e4c5174592 |
| paypal/paypal-ios | fc69f404fa68b2c7336a684296543a67e0e809d5 |
| stripe/stripe-php | c4c1f658483e717519935222e47af224ef4a508b |
| stripe/stripe-node | fe645f63d645011aca38dff9e245c1cf7b9ae60e |
| stripe/stripe-js | 857e6cd8e0f308e0f685fa1d3eb9c7e5fcb5b784 |
| stripe/react-stripe-js | 3b42f3d838c5f2279e719a4faac93b617c7e83af |
| stripe/stripe-terminal-ios | 79cfb3225553a7a5cceb8325f1c1f9087f792128 |
| stripe/stripe-terminal-android | 0829be9e77842bc12a6ba56d64fd152b53506025 |

Tree metadata was retrieved from each repository's GitHub git/trees endpoint
with recursive=1 and checked for truncation. Path existence is a readiness check,
not a full capsule/content/budget validation. Collection retains those checks.

## Shared Protection

Routine future checks inspect newer stable majors before filtering by configured
tracks. An untracked major returns needs_manual_review, lists package-qualified
versions and marks the collection index manual-review. No snapshot or ingest work
item is created by detection. Dry runs share this guard; explicit historical
release requests remain available. Older tracks and immutable raw are preserved.

## Remaining Work

Review PayPal iOS v3's renamed source/demo paths before enabling that track. Review
Stripe Terminal iOS 6's changed dependency/example layout before enabling v6.
Collect new releases separately and review packets before serial ingestion.

## Initial Guard Verification

- Seven new regression tests pass: native plain tags, package-specific ceilings,
  unrelated/prerelease tags, unchanged evidence, dry-run behavior, historical
  requests and collection-index manual-review action.
- Live future checks for the three gated repositories returned
  needs_manual_review, with zero snapshot paths and zero new work-item IDs.
- Full suite: 808 tests, 806 pass; two existing failures remain:
  test_adyen_postman_has_reviewed_checkout_terminal_policy (30 vs 40 packet files)
  and test_paypal_messages_ios_uses_the_reviewed_release_capsule (v2 track omitted
  from the old expectation).
- GitHub validation retains the same ten existing packet errors: five packet
  budget failures plus the corresponding five invalid-packet errors. No pending
  ingest items were created. git diff --check passes.

## Approved PayPal Android Follow-Up

The active capsule now requires PayPalPayments instead of PayPalWebPayments,
including its implementation, API declarations, build file and manifest. The
v2 track and immutable evidence remain; historical policy hash
`c0376ccf1e8e394e33bec22aef38f271f05c325a7eec066831e934634894cfc5`
is registered for validation of old packets. A fresh historical-layout recollection
that cannot satisfy the active v3 paths still requires manual policy review.

`version.properties` is now retained and classified as build configuration. Its
classifier regression failed before the narrow filename correction and passed
afterwards; all 61 ingest-packet tests pass.

| Release | Exact commit | Retained files | UTF-8 bytes | Suggested mode | State |
| --- | --- | --- | --- | --- | --- |
| paypal-android@3.0.0 | 3540adff974abdc20371d66fe47748e4c5174592 | 278 | 682258 | Full | awaiting_approval |
| paypal-android@3.1.0 | d100313f2247b512cedf6080bb7b6ecaada26d42 | 277 | 683872 | Delta | awaiting_approval |

Work items: `github-fda0a37813212896f0ec` and
`github-fce7ee241c398cc73695`, respectively. Both packets have zero recorded
evidence gaps and zero unclassified changes. The 3.1.0 retained comparison has
17 modified, one removed and 260 unchanged paths. The first attempt stopped
because version.properties was unclassified; after correction the same immutable
snapshot was reused and its work item recovered through the explicit retry flow.
No ingestion, canonical wiki edits, commit or push is included in this follow-up.

Final follow-up verification: 809 tests, 807 pass, with the same two pre-existing
registry expectation failures named above. GitHub validation reports the same ten
unrelated packet errors, no PayPal Android errors, and two pending ingest items.
Existing v2 raw and cumulative source/changelog files have no tracked diff.

## Approved Serial Ingest Completion

The follow-up above describes collection-time state. Subsequently, user approval
authorized full ingest of `paypal-android@3.0.0`, followed by delta ingest of
`paypal-android@3.1.0`. Both work items are now `ingested` as of 2026-10-16.
All 278 retained 3.0.0 files and all 17 changed retained 3.1.0 files were read
fully, with affected prior code; generated inventories and duplicated diffs
were mechanically verified under separate explicit reading exceptions.

Version-qualified additions preserve all v1/v2 knowledge. The 3.0.0 baseline
documents required merchant ID, session-first PayPalClient, app-switch/return
routing and migration cautions. The 3.1.0 delta resolves restricted TokenType
and card-vault demo initialization, forwards BN code into session eligibility,
and records demo user-action cleanup and Magnes namespace changes. Binary,
variant-source and runtime evidence limits remain explicit in the cumulative
source and changelog. Six typed wiki pages and whitespace checks pass; global
GitHub validation retains the same ten unrelated errors, none for Android.

## PayPal iOS v3 Path Review - 2026-10-16

Review only: no registry activation, accepted raw collection, work-item creation
or wiki ingestion. Remote annotated tags were peeled to these exact commits;
GitHub recursive trees were checked for truncation.

| Release | Exact commit | Proposed files | Tree-reported bytes |
| --- | --- | --- | --- |
| paypal-ios@3.0.0 | fc69f404fa68b2c7336a684296543a67e0e809d5 | 162 | 375722 |
| paypal-ios@3.1.0 | 67e4a9635f8e3ff829221c6d64573590937d1a2f | 162 | 376418 |
| paypal-ios@3.1.1 | de98414f5cf74dc3db2239a4828b4760ef391d20 | 162 | 378154 |

Proposed policy change: replace `Sources/PayPalWebPayments` with
`Sources/PayPalPayments` and `Demo/Demo/PayPalWebPayments` with
`Demo/Demo/PayPalPayments`; include `v3_MIGRATION_GUIDE.md`. All other required
roots and explicit includes exist at all three tags. Explicit PaymentButtons
includes cover every Swift source under that target at 3.1.1. The 3.0.0 package
manifest declares the renamed PayPalPayments target; its migration guide adds
required merchantID and optional partner bnCode to CoreConfig.

No snapshot-budget increase is indicated: 162 candidates are below 300 files,
largest candidate is 41987 bytes versus 512000, aggregate is below 2000000.
These metadata checks do not replace collection's UTF-8, hashing, secret scanning,
classification and packet-budget checks. The Magnes binary remains excluded.
Preserve the v2 track and register historical policy hash
`83c96e9b6452b55a6036f327ebe0f35ceae4ba08d63de33e56680ef556b93d21`
when approving the active v3 policy. Recollecting an old layout under the new
active roots still requires policy review, as for Android.

Recommended next approval: apply these bounded registry/test changes, add
`package:paypal-ios@3` with all-stable backfill/future, and collect 3.0.0, 3.1.0
and 3.1.1. Stop at packet review; recommend full 3.0.0 then assess each later
delta from collected evidence. No ingest or publication is authorized by this
path review alone.

## Approved PayPal iOS Collection - 2026-10-16

Applied only the reviewed iOS registry changes and a regression test, preserving
v2 and its historical policy hash. The new test failed before the registry edit
and passes afterwards. Discovery selected exactly the three approved releases.
The partial-clone blob lookup was slow; a bounded-size refetch hydrated the four
comparison tags in temporary storage, allowing collection to finish without
changing the collector or accepted evidence.

| Release | Files / bytes | Retained changes from prior | Work item | State |
| --- | --- | --- | --- | --- |
| paypal-ios@3.0.0 | 162 / 375722 | 31 added, 45 modified, 14 removed, 6 renamed, 80 unchanged | github-28bbeeaf63ba759b78ef | awaiting_approval |
| paypal-ios@3.1.0 | 162 / 376418 | 11 modified, 151 unchanged | github-5cce6532a34ea07a94ef | awaiting_approval |
| paypal-ios@3.1.1 | 162 / 378154 | 9 modified, 153 unchanged | github-85652bd08413a3ffc568 | awaiting_approval |

Pre-ingest findings from retained release notes, comparisons and selected complete
source/build files; this is not a completed full-capsule ingest review:

- `3.0.0` renames the PayPal module/client/results/funding enum, replaces request
  objects with session-first ID-based checkout/vault, requires merchantID in
  CoreConfig, renames Environment to CoreEnvironment and adds structured phone
  identity. Public PayPalSessionType exposes checkout/vaultWithoutPurchase,
  unlike Android's public TokenType. Recommend full historical ingest.
- The `3.1.1` cumulative changelog explicitly marks `3.0.0` unsupported, advising
  `3.1.0` instead. It also retrospectively rearranges entries under `3.1.0`;
  preserve original release-note records and exact code boundaries rather than
  copying the later changelog's attribution over earlier history.
- `3.1.0` raises the deployment target from iOS 14 to 16 in both SPM and CocoaPods,
  fixes hardcoded PAY to honor CONTINUE/PAY/COMMIT, removes the installed-app helper,
  and replaces the bundled risk framework with paypal/paypal-risk-ios exact 5.6.0
  (PayPalRisk product/pod). The session API now sends paypalNativeAppInstalled=true
  optimistically; that field is not proof of an installed app. Recommend full
  rather than the script's delta suggestion because platform compatibility and
  dependency packaging change. Dependency implementation is not collected here.
- `3.1.1` forwards CoreConfig.bnCode into encoded session experimentation context,
  adds persisted demo BN-code configuration, and changes CardClient only in
  formatting in the bounded comparison. Recommend delta, subject to complete
  assigned reading during approved ingest.

Raw snapshots: `raw/github/paypal/paypal-ios/snapshots/2026-10-16-fc69f40/`,
`2026-10-16-67e4a96/` and `2026-10-16-de98414/`. Release records and comparison/
packet files are linked from generated `tracking/github/status.md`. All 486 new
snapshot file hashes/sizes plus release-note, packet and comparison hashes pass;
each packet records zero evidence gaps and zero unclassified changes. These
counts do not imply that excluded binary/dependency implementation is known.

Full suite: 810 tests, 808 pass; the same Adyen Postman packet-limit and PayPal
Messages iOS v2-track expectation failures remain. Global GitHub validation has
the same ten unrelated structural errors, none for PayPal iOS, and three pending
items. Whitespace checks pass. Existing iOS source/changelog/concept pages are
byte-unchanged. No ingest approval/claim, canonical wiki edits, commit or push.
Next approval: serial full 3.0.0, full 3.1.0, then delta 3.1.1; preserve older
knowledge and annotate 3.0.0's later unsupported status.

## Approved PayPal iOS Serial Ingest - 2026-10-16

The preceding collection section records the pre-ingest state. The user then
approved full 3.0.0, full 3.1.0 and delta 3.1.1 in that order, with mechanical
verification of generated manifests/inventories/duplicated diffs only. Each
full cycle read all 162 current retained files; the delta read all nine changed
files plus affected prior code and cumulative wiki context. Each cycle completed
concept audit, additive source/changelog, company/concepts, contradiction review,
catalog/log updates and focused validation before advancing to the next item.

The wiki now preserves v1/v2 and all three v3 releases, including 3.0.0's
session/API migration and action defect, 3.1.0's iOS 16/risk dependency/action and
routing changes, and 3.1.1's BN forwarding and later unsupported-3.0.0 notice.
The absent invalid-action error, return binding, browser URL construction and
demo BN Clear limitations remain explicitly version-qualified static findings.
External risk implementation and successful payment behavior remain unverified.

Six typed wiki pages validate; all 486 new snapshot file hashes/sizes pass;
new evidence targets, catalog uniqueness, unchanged source_count and preservation
of older source/changelog sections were checked. Global validation retains the
ten unrelated pre-existing packet errors. No commit or push authorized for this
round. Next: report findings and request scoped commit/push approval.
