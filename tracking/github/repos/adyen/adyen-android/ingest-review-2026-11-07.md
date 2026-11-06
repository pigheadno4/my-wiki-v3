# Adyen Android Serial Ingest Review - 2026-11-07

## Authorization and Reading

User approved full additive 5.21.0 followed by full additive 5.22.0, with focused reading and preservation of all history. Publication is not approved. Unrelated shared-file work is preserved. Original snapshots, releases, packets and comparisons are not edited.

Focused reading covers changed authored implementation/build settings, affected prior/dependency code, the five fully read exact-5.21.0 supplemental files, release notes, comparison changes and complete cumulative source/changelog. Unchanged source and generated inventories/duplicated diff content are verified mechanically; this is not a full read of every snapshot file or the whole upstream repository. Shared company/index/log context is read in relevant sections.

## 5.21.0 Grounding Gate (Before Wiki Edits)

Exact SHA: `405b582a7b2060aceac756eae7b6bd3757e0c084`; work item `github-7ed8658609166ae83227`, approved full and claimed. Effective assignment: 1,215 paths / 4,732,844 bytes including canonical supplement attachment.

Five verbatim excerpts:

1. `binding.switchStorePaymentMethod.isChecked = outputData.shouldStorePaymentMethod` - snapshot `2026-11-07-405b582/files/card/src/main/java/com/adyen/checkout/card/internal/ui/view/CardView.kt:756`.
2. `emitError(e as? CheckoutException ?: ComponentException("Native redirect request failed.", e))` - same snapshot, `redirect/src/main/java/com/adyen/checkout/redirect/internal/ui/DefaultRedirectDelegate.kt:198`.
3. `compileOptions.sourceCompatibility = JavaVersion.VERSION_11` - supplement `2026-11-07-405b582-93095740/files/build-logic/convention/src/main/kotlin/JavaConventionPlugin.kt:37`.
4. `jvmToolchain(jvmTarget.majorVersion.toInt())` - same supplemental file, line 44; catalog target 17, separate from Android source/target 11.
5. `distributionUrl=https\://services.gradle.org/distributions/gradle-9.8.0-bin.zip` - same supplement, `gradle/wrapper/gradle-wrapper.properties:3`.

Before edits: all 3,597 files across the baseline and two new snapshots plus five supplemental files pass size, SHA-256 and Git blob identity checks (3,602 total). Changed retained files: 65; unchanged: 1,134. No packet gaps/unclassified changes. Semantic findings and limits are recorded in the collection/supplement reviews, now followed by the separately approved ingest.

## 5.22.0 Grounding Gate (Before This Version's Wiki Edits)

After completing 5.21.0, approved and claimed `github-a2920dfadabf8c5faa3b` as full at SHA `73df6558fa5868a2c14449ac2e0c6379fc349798`. Effective assignment is 1,208 paths / 4,628,525 bytes, including the now-expanded cumulative wiki history. The preflight byte count increased because 5.21.0 was ingested first. Reread both cumulative pages completely before this version's promotion.

Five verbatim excerpts (paths below are within snapshot `2026-11-07-73df655/files/` unless stated):

1. `Devices with Google Play services were already protected by an automatic update from Google.` - release `5.22.0/2026-11-07/release-notes.md:2`. The same line attributes eight compromised intermediates being blocked on devices without Play services to upstream release notes, not independent execution here.
2. `okhttp = "4.12.1"` - `gradle/libs.versions.toml:49`.
3. `context.imageLoader.load(` - `ui-core/src/main/java/com/adyen/checkout/ui/core/internal/util/ImageSaver.kt:101`.
4. `return@withContext Result.failure(CheckoutException("Failed to load image", error))` - same file, line 91.
5. `bitmap.recycle()` - same file, line 77, now in the view-created bitmap path rather than the shared bitmap-saving helper.

Read complete changed image files, complete comparison patch and relevant prior code; read retained DefaultImageLoader/HTTP factory dependencies. Catalog comparison changes only OkHttp/logging pins to 4.12.1. Three modified and 1,196 unchanged retained files; all seven upstream dispositions accounted for, no gaps/unclassified changes. Snapshot identity and unchanged evidence mechanically verified. Exact 5.21.0 supplemental files remain historical evidence at their own SHA, not misattributed to 5.22.0. Certificate blocklist internals remain outside the retained dependency evidence; no device/certificate/payment run.

## Serial Checklist

- 5.21.0: concept-first additive promotion complete; targeted wiki validation passes (five files), whitespace and exact evidence locators pass, all original source/changelog lines remain in order. Item completed as ingested/full before claiming the second release. Source review corrected the enclosing redirect method locator to handleNativeRedirect (the service call is makeNativeRedirect).
- 5.22.0: claimed only after 5.21.0 completed; concept-first additive promotion complete and item completed ingested/full. Targeted wiki validation passes (five files); provider index/root log links and placeholders pass; all original source/changelog lines remain in order, chronological release sections and exact evidence locators pass. No new canonical source pages or source-count edits by these ingests.
- Publication: not authorized; no commit/push.

## Review and Verification Limits

Semantic self-review checks the card output assignment, enclosing handleNativeRedirect method, cancellation helper, supplemental Android-11/tooling-17 distinction, repository versus consumer build requirements, image-cache bitmap ownership, and release-note-only security attribution. All prior source/changelog lines remain; concept baseline is explicitly relabeled historical rather than removed. No cross-company comparison or new concept is warranted by these repository-only updates. Shared campaign changes are untouched.

An offline validator started before the final queue transition observed a transient collection-index mismatch and one pending item while ingest completed. It is not the final verdict; rerun after terminal states is required. The known unrelated baseline is 13 historical packet-budget/ledger errors (six packet rebuild budgets, their six invalid-packet reports, and Adyen PHP 30.1.0 package-qualified ledger mismatch). No unrelated repair is authorized.

Final post-transition offline rerun: exactly the same 13 unrelated historical errors, no Adyen Android/attachment/index errors and zero pending work items. Both approved items are ingested/full; generated collection index accepts `adyen-android@5.22.0`, next action wait, next due 2026-11-14. Scoped wiki validation, exact raw locators, baseline preservation and whitespace checks pass. This is a scoped pass, not global all-green validation. No commit/push was performed; next step is separately approved scoped publication.
