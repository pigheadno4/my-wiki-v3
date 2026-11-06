# Adyen Android 5.21.0 Build Supplement Review

## Scope and State

User approved only the five-file exact-SHA build supplement, following the collection review. Collected and fully read all five approved UTF-8 files plus their immutable manifest at SHA `405b582a7b2060aceac756eae7b6bd3757e0c084` (5.21.0). No extra paths, registry/capsule changes, original snapshot/packet edits, ingest approval, wiki edits, build, commit or push.

Supplement: `raw/github/adyen/adyen-android/supplements/2026-11-07-405b582-93095740/manifest.json`; five files / 12,760 bytes. Published and linked its canonical attachment at `tracking/github/repos/adyen/adyen-android/evidence-attachments/github-7ed8658609166ae83227/attachment.json` through the existing attachment API. Both releases remain awaiting_approval with approved_mode null.

## Confirmed Findings

### Android Java Target Remains 11

JavaConventionPlugin explicitly configures Android modules' Java source and target compatibility to `JavaVersion.VERSION_11` (lines 37-38). It separately reads the catalog's JVM target 17 and applies `jvmToolchain(17)` to plain Kotlin JVM projects. Its comments describe AGP's built-in Kotlin target as derived from Android compile options. This is configuration-source evidence, not compiled-artifact inspection.

The convention build separately pins its Java and Kotlin output target to catalog value 17. Therefore the catalog's newly added JVM target must not be summarized as a universal Java 17 Android-library bytecode migration. These files do not independently establish the minimum JDK that must run Gradle/AGP in every consumer application.

### Build Wrapper and Plugin Wiring

- Gradle wrapper properties name `gradle-9.8.0-bin.zip`. This records the upstream repository wrapper; it does not mandate that every consuming application copy that wrapper version or prove that the wrapper was executed successfully.
- The convention build registers `checkout.android.library` to CheckoutAndroidLibraryPlugin and `checkout.java` to JavaConventionPlugin, along with the other project convention plugins. The retained module Gradle files adopt these aliases, so the supplemental implementations close the previously missing wiring evidence for those settings.
- CheckoutAndroidLibraryPlugin applies the Java convention, Android library plugin and project tooling. It sets the Maven/Gradle group to `com.adyen.checkout` for RestrictedApi enforcement, configures compile SDK/min SDK from the retained catalog (36/21), consumer ProGuard rules and the checkout-version BuildConfig field. This is not proof of merchant/device eligibility or a new minimum Android API requirement.
- ProjectExtensions supplies the catalog accessor and shared group constant. No additional source is needed to interpret these specific settings.

### API-Validation Workaround

For non-ignored projects when the root API-validation extension exists, the library convention manually registers Kotlin API build/compare/dump tasks and attaches apiCheck to check. Its comments identify an AGP 9/binary-compatibility-validator incompatibility; the build task filters compiler-generated Compose ComposableSingletons blocks from dumps. Do not equate every changed generated API dump with an authored public API removal, or claim that compatibility tests passed merely because tasks are configured. The excluded API dump contents and other convention implementations were not separately collected or audited here.

## Verification and Full-Mode Preflight

- All five supplement file sizes, SHA-256 and Git blob identities pass. Canonical attachment loading revalidates exact repository/SHA, supplement identity and required files. The attachment adds seven mandatory paths (attachment, manifest and five files).
- Original collection-time packet Markdown/snapshot identities remain unchanged. Pure full-mode reading expansion, without promoting queue state, validates 1,215 effective paths / 4,732,844 bytes for 5.21.0 including the supplement; 5.22.0 expands to 1,208 paths / 4,618,268 bytes.
- Existing cumulative source/changelog remain byte-identical to HEAD. This collection/review has not changed the last ingest date or accepted implementation version. No Kotlin/Android build, device, certificate-rejection or payment run was performed.
- Fresh offline GitHub validation retains the same 13 unrelated historical errors, none for these items or attachment, with two pending items. Scoped whitespace check passes; no global all-green validation claim.
- The remaining security boundary is unchanged: the eMudhra blocking statement comes from Adyen's 5.22.0 release notes; this Android capsule establishes the OkHttp pin/image-loader routing but does not contain that dependency's blocklist internals.

Next recommendation: separately approve full additive ingestion of 5.21.0 followed by 5.22.0, preserving all 5.20.0 history. Recommend a focused-reading exception for both: fully read changed authored code/build settings, the five supplemental files, affected prior/dependency code, release notes/comparisons and cumulative wiki history; mechanically verify unchanged files, generated inventories and duplicated diff content. Full modes remain full and approval boundaries remain separate. No ingest has begun.
