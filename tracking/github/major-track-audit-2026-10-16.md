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
