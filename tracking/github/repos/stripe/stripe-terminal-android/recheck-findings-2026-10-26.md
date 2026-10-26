# Stripe Terminal Android collection review, 2026-10-26

## Approval boundary

User approved rechecking this repository, including newer-major detection, and
sharing findings before ingestion. Existing registry already enables stable v5
and v6 tracks. No registry/code changes, ingest approval, next-ingest claim,
canonical wiki edits, commit or push were performed for this recheck.

GitHub's latest release page resolves to 6.0.0. Independent remote tag checks
confirm legacy v-prefixed v5 tags and the unprefixed 6.0.0 tag. The old wiki
baseline remains stripeterminal@5.8.0 at
b3de15b57201df0aa0e0235ccbe8e81bf9abaa8f.

## Collected releases

| Package release | Exact SHA | Retained files / bytes | Work item | Recommended mode |
| --- | --- | --- | --- | --- |
| stripeterminal@5.8.1 | 846d401d1f7bc686a2c12d6def4342471c25a625 | 447 / 3108265 | github-86ab3cb682c630c93e87 | Delta |
| stripeterminal@5.8.2 | abb16f502cbe0fcc82f673c246c86c883a5c2fdc | 447 / 3108387 | github-d40ef200e4b88ce722d2 | Delta |
| stripeterminal@6.0.0 | 0829be9e77842bc12a6ba56d64fd152b53506025 | 450 / 3531009 | github-78ec024faa51ef3d956e | Full additive |

All three remain awaiting_approval. Their collection-time packets assign
61, 61 and 62 reading paths respectively. Approved full mode would expand the
v6 assignment using existing reading selectors; it is not permission to read
only the original collection-time list.

Snapshots and release records are dated 2026-10-26 under
raw/github/stripe/stripe-terminal-android/. Comparisons and packets are under
tracking/github/repos/stripe/stripe-terminal-android/.

## Findings before ingestion

The GitHub release bodies provide dependency versions and point to a mutable
master changelog. Functional findings below instead use the collected exact-SHA
CHANGELOG.md plus retained example diffs. This is collection review, not a claim
of complete assigned ingestion reading or proprietary runtime inspection.

### stripeterminal@5.8.1, changelog date 2026-09-14

- Adds China UnionPay support in Hong Kong for Tap to Pay on Android.
- Relative to 5.8.0, 341 retained files change and 106 remain unchanged. All 337
  changed generated documentation files become byte-identical after replacing
  the new release version string with the old one. Remaining changes are the
  changelog, README dependency examples and two application Gradle versions.
- No retained application implementation change. This is an upstream SDK
  capability announcement, not merchant/device eligibility or payment proof.

### stripeterminal@5.8.2, changelog date 2026-10-02

- Fixes payment failures for China UnionPay cards in Tap to Pay.
- Same 341 modified / 106 unchanged pattern; all 337 documentation differences
  are version-string-only under the same exact comparison. Other changes are
  changelog, README and the Java/Kotlin example dependency versions.
- Recommend delta, preserving the 5.8.1 capability history and 5.8.0 baseline.

### stripeterminal@6.0.0, changelog date 2026-10-07

- Full additive major boundary: 341 modified, eight added, five removed and 101
  unchanged retained files relative to 5.8.2.
- Capture default changes to AutomaticAsync in the SDK-side PaymentIntent
  builder. Explicit Manual remains required for receipt tipping, incremental
  and extended authorization. Retained Java/Kotlin event examples explicitly
  select Manual for extended/incremental authorization.
- Consent moves into CollectSetupIntentConfiguration. Examples initialize its
  builder with AllowRedisplay.ALWAYS; this does not establish actual customer
  consent or justify copying that value blindly.
- Public-model migrations: latestCharge/latestChargeId replace getCharges;
  invoice relationship retrieved server-side; distinct PaymentMethod.CardPresent
  and Charge.CardPresent models, nullable instrument expiry; SetupAttempt model
  renames; nullable Refund ID and renamed ProcessRefundParameters.
- Separate ReaderPaymentInteractionListener handles selection/QR interactions
  through onInteractionRequired and concrete PaymentInteraction callbacks.
  CANCELED_BY_READER is distinct from SDK CANCELED; low-battery errors generalize.
- Removed legacy initialization overload requires LocaleConfig. Java example
  now passes HardcodedLocale("en-US"). Old Tap to Pay location-ID construction
  moves to TapUseCase.Pay; deprecated refund and simulator-update APIs removed.
- Changelog requires compileSdkVersion >=35 and Kotlin 2.3.21 dependencies. This
  is not a minimum-device Android 15 requirement. Tap to Pay adds the
  MODIFY_AUDIO_SETTINGS permission and an upcoming-update-requirements callback.
- Tap to Pay UX types lose Parcelable, DarkMode/colors migrate to Theme/
  colorScheme and the default theme becomes SYSTEM. Session-token expiration
  uses SESSION_EXPIRED rather than the generic connection error.
- No-collection refunds and typed nextAction are private preview; they do not
  establish merchant access or bypass payment-method-specific refund rules.
- MOTO card authorization code requires smart-reader firmware 2.45+ per note.
  Proguard changes and Tap to Pay cancellation fixes are upstream statements,
  not locally built or reproduced SDK behavior.

Do not copy iOS-only v6 features into Android knowledge without Android evidence.
In particular this Android release note does not announce iOS's Mexico MSI or
Swish additions, or an SPM publication policy.

## Collection verification

- All 1,791 files across baseline and three new snapshots pass size, SHA-256
  and Git blob identity checks. Each packet's Markdown hash matches its JSON;
  all three have zero reported evidence gaps and unclassified changes.
- Existing work items are unchanged; exactly three Terminal Android items added.
  Generated repository index refreshed for this recheck; other date-dependent
  or concurrent rows are not authority for additional repository operations.
- Targeted Terminal Android registry test passes. Whitespace check passes.
- Global offline validator reports the same 12 unrelated historical errors:
  six older packet byte-budget rebuild failures and six corresponding invalid
  packet errors. No Terminal Android errors; three informational pending items.
- Partial-clone hydration initially fetched blobs individually. Reused 447
  size/hash/Git-ID verified baseline blobs in the disposable clone, then fetched
  bounded-size blobs for the three selected tags together. Accepted raw and
  collector policy/code were not changed; collection completed normally.

## Next step

Request approval for serial delta 5.8.1, then delta 5.8.2, then full additive
6.0.0. Preserve all prior wiki history. Choose the reading method separately
where the effective assignment is dominated by regenerated documentation or
inventories. Do not auto-approve or begin ingestion from this review.
