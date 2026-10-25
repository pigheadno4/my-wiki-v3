# Stripe Terminal iOS serial ingest review, 2026-10-25

## Authority and sequence

User approved 5.8.1 delta followed by 6.0.0 additive full ingest, preserving all
v5 knowledge. User then explicitly approved focused reading for both: complete
changed headers/examples, affected prior code, notes, both branch comparisons
and cumulative wiki history; mechanical verification of unchanged files,
historical changelog sections and generated inventories. Full/delta modes are
unchanged by that reading exception. No commit/push approval in this turn.

1. `github-efe5a0543a98bd570d9c`, StripeTerminal@5.8.1,
   `00cd46de3ad9a7847c5d8ccb30abcf311a1e26e0`: delta completed and marked ingested
   before claiming the next item.
2. `github-9124967f62dc0a34c4ec`, StripeTerminal@6.0.0,
   `79cfb3225553a7a5cceb8325f1c1f9087f792128`: additive full reading and wiki
   updates validated, then marked ingested through `complete-ingest`.

## Reading and mechanical checks

- Changed authored v6 headers and examples read completely, including the large
  error/Terminal headers and payment, discovery, reader-management and logging
  controllers. README, package, support policy, release notes and affected prior
  code reviewed. The two removed example Podfiles remain in v5 raw and are
  completely visible in the comparison.
- Read the complete common-baseline 5.8.0 -> 6.0.0 patch and mechanically compared
  it with the 5.8.1 -> 6.0.0 patch, reading all differences. Differences concern
  the prior changelog/version/binary metadata; all other hunks are identical.
- Verified all 713 retained files (235 baseline, 235 maintenance, 243 v6): size,
  SHA-256 and Git blob identity. v6 counts: ten added, 56 modified, two removed,
  177 unchanged. All three raw changelog suffixes from 5.8.0 onward are identical.
- Packet hashes, inventory identities, retained classifications and zero gaps
  checked mechanically. Inventory reading does not establish excluded behavior.
- No claim of reading the whole upstream repository or inspecting/executing its
  proprietary binary. SceneDelegate and example build configuration are excluded;
  no full example launch/build proof. No additional collection or supplement.

## Version findings

### StripeTerminal@5.8.1

Upstream binary fix for offline PaymentIntent creation parameters affecting Tap
to Pay destination charges using onBehalfOf. Only changelog, binary reference
and SDK version constant change publicly. No retained payment API migration.
GitHub publication October 9 UTC versus October 8 in the note. Not locally
reproduced.

### StripeTerminal@6.0.0

- SPM-only publication of new releases and older-version patches; already
  published CocoaPods versions keep working, without future CocoaPods updates.
  README uses stripe-terminal-ios-spm and still documents manual binaries.
- iOS 16 minimum; integrators Xcode 16+/Swift 6+ despite binary build using
  Xcode 27/Swift 6.4. Support table is unchanged through v5; no invented v6 date.
- Client builder automatic-async capture default. Explicit manual for receipt
  tipping, incremental and extended authorization. Reciprocal contradiction for
  the old unqualified synchronous-capture header comment.
- Required consent-bearing SetupIntent configuration; expanded/ID model rename,
  latest Charge APIs, instrument/transaction separation, nullable instrument
  expiry/funding, API-string card fields and removed old helper exports.
- Shared reader lifecycle/display callbacks and separate retained blocking-UI
  delegate. New reader cancellation code versus SDK cancellation; sample's
  error branch still handles only the old code. Generalized low-battery error,
  updated per-collection cancellation and removed deprecated APIs.
- Private-preview no-collection refund still authenticates through connected
  reader; reconcile unknown outcome before creating another refund. Interac
  presence requirements remain. Nullable Refund ID and next-action states.
- Mexico MSI and Swish previews, WisePad 3 confirm-time surcharge support but
  no collect-time surchargeNotice; simulator changes do not mean live offline GA.

5.8.1 and 6.0.0 diverge from 5.8.0. Both comparisons remain unchanged; the absence
of the later maintenance note in v6 does not prove whether its binary has that
fix. Existing source/changelog history is retained rather than overwritten.

## Wiki scope and validation

Concept audit first: Terminal, saving payment details, refunds, tipping,
incremental authorization and extended authorization. Then cumulative source and
changelog, Stripe company/catalog, provider/root logs. No new source pages or
cross-company comparison; Stripe source_count remains 666. Other sessions'
Adyen/BYD changes are untouched.

- `validate_wiki.py`: all ten touched typed pages pass. Provider index and root
  log are untyped navigation/chronology; touched evidence links and catalog
  occurrences checked separately.
- Original source baseline paragraphs and complete old changelog section from
  5.8.0 onward remain preserved. Company/catalog source and history entries are
  unique at their expected locations; all new Markdown evidence targets exist.
- Targeted Terminal iOS registry test: one pass. Collection-index suite: nine
  passes. Registry suite: 64 tests, 61 pass, three existing unrelated expectation
  failures (Adyen Postman packet-files 30 vs 40, Braintree GraphQL 15 vs 20,
  PayPal Messages iOS missing v2 expectation). Not repaired in this scope.
- Global offline GitHub validator: same 12 unrelated structural errors across
  six older packets (six byte-budget rebuild failures and six corresponding
  invalid-packet errors), no Terminal errors. Before completion, one informational
  pending item; final queue inspection confirms both new items ingested.
- `git diff --check`: passes. No upstream build, physical reader or payment
  test. No commit or push.

Next step: user approval for a scoped commit/push of this Terminal collection,
registry adjustment and serial ingest, excluding other sessions' changes.
