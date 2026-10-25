# Stripe Terminal iOS: collection review, 2026-10-25

User approved enabling the v6 track while preserving v5, collecting 5.8.1 and
6.0.0, and reviewing their evidence before ingestion. This file records
pre-ingest findings, not completed full/delta reading or wiki promotion.

## Collection state

| Release | Exact commit | Retained files / bytes | Work item | Recommendation |
| --- | --- | --- | --- | --- |
| StripeTerminal@5.8.1 | 00cd46de3ad9a7847c5d8ccb30abcf311a1e26e0 | 235 / 1021255 | github-efe5a0543a98bd570d9c | Delta |
| StripeTerminal@6.0.0 | 79cfb3225553a7a5cceb8325f1c1f9087f792128 | 243 / 1041137 | github-9124967f62dc0a34c4ec | Full additive |

Both work items remain `awaiting_approval`; neither is approved or claimed.
Snapshots and release records are dated 2026-10-25. Existing 5.8.0 raw and wiki
history are unchanged. No canonical wiki edits, upstream builds, reader/payment
tests, commit or push.

## Policy adjustment

- Preserved `package:StripeTerminal@5`, including pinned 5.8.0 and stable future
  collection; added `package:StripeTerminal@6` with all-stable backfill/future.
- Collected 5.8.1 under the original policy, retaining Example/Podfile and
  Example/Podfile.lock. Removed those mandatory includes from the active v6-ready
  capsule because both files are deleted upstream at 6.0.0. Their old evidence
  and deletion comparisons remain available; this is not a claim that all SDK
  CocoaPods distribution was removed.
- Registered historical policy hash
  `c9f5b38c2f72d20733535b2ba321b96373a5af2152cbfbd0e7ab582154263f64`.
  PublicHeaders, all remaining explicit paths, reading selectors, exclusions and
  byte/file budgets are preserved. No collector implementation changes.
- Active policy no longer requires the two old example files for a future v5
  recollection. The accepted 5.8.0/5.8.1 snapshots still retain them.

## Findings: 5.8.1

- From 5.8.0: three modified retained files, 232 unchanged, no added/removed
  paths. Fully read the complete small comparison patch.
- Stripe reports a fix for offline PaymentIntents dropping merchant creation
  parameters, which caused Tap to Pay collection failures for destination charges
  using onBehalfOf. GitHub publication is October 9 UTC; notes label October 8.
- Public-source diff contains only the changelog entry, binary target URL/checksum
  and SCPSDKVersion constant. No exposed payment API change is present in this
  comparison. Proprietary binary implementation was not collected or executed;
  do not present the reported runtime fix as locally reproduced.
- Recommend delta, preserving the existing 5.8.0 baseline.

## Findings: 6.0.0

- Major release, changed capsule policy and broad public API migration warrant
  full additive ingest. Generated queued counts relative to 5.8.1: ten added,
  56 modified, two removed and 177 unchanged retained files. All 243 current
  files remain available; full effective reading follows existing selectors.
- Fully read Package.swift and selected public headers for payment-intent
  creation, SetupIntent collection, shared reader interactions, blocking payment
  interactions and process-refund parameters. These establish public contracts,
  not the proprietary runtime's implementation or successful payments.
- Package.swift raises minimum iOS to 16 and pins the 6.0.0 binary/checksum.
  PaymentIntentParameters documents automatic-async capture as the new default;
  integrations requiring separate capture must explicitly choose manual.
- SetupIntent collection builder requires allowRedisplay on initialization;
  its header documents always/limited and cardholder-consent requirements.
  The example value is not permission to choose always without consent.
- Shared ReaderInteractionDelegate supplies reader-prefixed lifecycle/display
  callbacks. ReaderPaymentInteractionDelegate separately handles blocking
  payment UI, and its header requires application retention until disconnect.
- Refund parameters use ProcessRefundParameters/Builder. Release notes also
  announce PaymentIntent/SetupIntent model changes, removed legacy APIs,
  reader-originated cancellation errors and preview refunds/installments/Swish.
  Those additional areas still require complete assigned reading during ingest;
  preview declarations do not establish merchant access or availability.

## Branch comparison boundary

GitHub's live comparison endpoint reports 5.8.1 versus 6.0.0 as diverged, with
merge base 5.8.0 at c027d6dc2258c774412cb7933cbb959488c16b63. Both branch tips
descend from that baseline; 5.8.1 was published after 6.0.0.

- Maintenance comparison: `comparisons/stripeterminal/5.8.0--5.8.1/`.
- Primary v6 evolution comparison: `comparisons/stripeterminal/5.8.0--6.0.0/`,
  including its separate ad hoc review-packet.json and review-packet.md.
- The immutable queued v6 packet uses the collector's semantic predecessor
  5.8.1. Its `comparisons/stripeterminal/5.8.1--6.0.0/` remains useful as an
  endpoint comparison, not an ancestor transition. Preserve it and read the
  common-baseline comparison in addition during approved v6 ingestion.
- Do not infer whether the closed-source v6 binary contains the 5.8.1 fix from
  semantic version ordering, missing changelog wording, or Git ancestry alone.

## Verification

- Verified sizes, SHA-256 and Git blob identities for all 713 files across the
  original baseline and both new snapshots. Both queued packets report zero
  evidence gaps and zero unclassified changes.
- The targeted Terminal iOS registry test failed before the path adjustment and
  passes afterward. Registry suite: 64 tests, 61 pass; three pre-existing
  expectation failures remain for Adyen Postman, Braintree GraphQL and PayPal
  Messages iOS. These policies and their tests were not changed by this work.
- Offline GitHub validation reports the same 12 unrelated packet errors across
  six other repositories, no Terminal iOS errors, and two pending items.
- Collection hydration reused hash-verified prior raw blobs only in disposable
  Git caches. A selected-object fetch and local cache-clone attempt failed;
  a filtered exact-tag fetch completed and collection succeeded. These attempts
  did not modify accepted raw evidence or the collector implementation.

Next approval: serial delta 5.8.1, then full additive 6.0.0, preserving all v5
knowledge and explicitly reading the additional common-baseline v6 comparison.
