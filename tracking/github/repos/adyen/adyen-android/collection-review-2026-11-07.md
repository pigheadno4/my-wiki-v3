# Adyen Android Collection Review - 2026-11-07

## Approval Boundary

User approved the recommended Adyen Android recheck. Existing future-release collection completed without changing registry, capsule or packet budgets. Two stable releases were collected and stopped at awaiting_approval; no approve/claim/ingest command, wiki edit, commit or push. The v6 alpha remains excluded by the existing prerelease policy. Last ingested implementation remains 5.20.0 from 2026-08-01.

## Collected Releases

| Release | Exact SHA | Work Item | Snapshot | Retained Changes | Script Mode |
| --- | --- | --- | --- | --- | --- |
| adyen-android@5.21.0 | 405b582a7b2060aceac756eae7b6bd3757e0c084 | github-7ed8658609166ae83227 | 2026-11-07-405b582 | 65 modified / 1134 unchanged | delta/high |
| adyen-android@5.22.0 | 73df6558fa5868a2c14449ac2e0c6379fc349798 | github-a2920dfadabf8c5faa3b | 2026-11-07-73df655 | 3 modified / 1196 unchanged | full/high, security |

Each snapshot contains 1,199 files. Prior 5.20.0: 3,670,837 bytes; 5.21.0: 3,651,394 bytes; 5.22.0: 3,651,797 bytes. Current collection-time packets assign 74 paths / 1,215,363 bytes and 12 paths / 991,415 bytes respectively, including cumulative wiki context. An approved full mode would expand the effective reading list; collection-time packet counts are not the full-ingest assignment.

## Findings Before Ingestion

### 5.21.0

- Release notes describe preservation of the store-payment-details switch after returning from address lookup. Retained CardView change restores the switch from `outputData.shouldStorePaymentMethod` during the relevant output update.
- Native redirect submission now uses `runSuspendCatching`, serializes the result inside the protected block, and routes failures through the error channel, wrapping a non-CheckoutException as ComponentException. The retained helper rethrows coroutine cancellation; this is not blanket suppression of cancellation or proof that every exception in the app is handled.
- The version catalog advances Adyen 3DS2 2.2.27 -> 2.2.28, Kotlin 1.9.25 -> 2.3.21, Android Gradle Plugin 8.8.1 -> 9.4.1, Retrofit 2.11.0 -> 3.0.0, and numerous AndroidX/Compose/Coroutines/Material pins. It adds `jvm-target = "17"`. These are observed repository build/dependency definitions, not tested merchant build compatibility or a confirmed Android minimum-device change.
- Build files switch to checkout convention plugins and settings adds an included build-logic build. Example card/BACS back handling moves to OnBackPressedDispatcher. Other retained Kotlin changes include lint suppression, whitespace and documentation cleanup rather than a demonstrated public callback contract change.
- Human recommendation: full additive ingest with an explicitly approved focused-reading scope after resolving the build-evidence gap below, rather than the script's delta. The broad toolchain/build migration merits migration treatment, not inference from the minor version alone.

### 5.22.0

- Upstream release notes state protection against eight compromised eMudhra intermediate CA certificates on devices without Google Play services, and say devices with Play services had already received an automatic update. This is an upstream security claim, not independently verified certificate rejection in this review.
- Retained catalog updates OkHttp and its logging pin 4.12.0 -> 4.12.1. The dependency's internal blocklist implementation is outside this repository capsule; no eight-certificate list, CVE, comprehensive TLS guarantee or live device acceptance is inferred.
- ImageSaver replaces URL.openStream-based downloads with the existing shared DefaultImageLoader, which uses OkHttp. Its error wrapping now distinguishes malformed URLs from image-load failure. Bitmap recycling moves to the view-created bitmap path rather than recycling every bitmap in the shared save helper, avoiding that recycling action on a loader-provided cached bitmap.
- Human recommendation: retain the script's full/high security mode, with separately approved focused reading if desired. Preserve all earlier knowledge and keep delegated dependency claims qualified. No Android build, device, certificate-rejection or payment test was run.

## Bounded Missing Build Evidence

The new convention implementations and Gradle wrapper properties are intentional normal-capsule exclusions and are not retained source authority. The generated comparison does not contain their complete contents either. The catalog alone does not establish the effective JVM/toolchain/plugin wiring.

Before making precise migration statements, recommend collecting these five immutable supplemental paths at exact 5.21.0 SHA 405b582a7b2060aceac756eae7b6bd3757e0c084, without changing the original snapshot or future collection policy:

1. build-logic/convention/src/main/kotlin/CheckoutAndroidLibraryPlugin.kt
2. build-logic/convention/src/main/kotlin/JavaConventionPlugin.kt
3. build-logic/convention/src/main/kotlin/com/adyen/checkout/ProjectExtensions.kt
4. build-logic/convention/build.gradle.kts
5. gradle/wrapper/gradle-wrapper.properties

Only their upstream path/disposition is established so far. Do not claim they have been collected or read. Review any further direct dependency gap after these files are available rather than silently broadening the capsule. Original packet-generated gap/unclassified arrays are empty; this human migration-evidence limitation is recorded here, not hidden by that mechanical result.

## Verification and Reading Boundary

- All 3,597 retained file sizes, SHA-256 and Git blob IDs across prior/current snapshots pass. Packet Markdown/snapshot, release-note and comparison Markdown/patch digests pass. Both items remain awaiting_approval with approved_mode null.
- All 203 upstream dispositions in 5.21.0 reconcile (65 retained, 138 excluded); all seven in 5.22.0 reconcile (three retained, four excluded). Zero packet-reported gaps/unclassified changes.
- Review covered both packet Markdown files, parsed JSON metadata/inventories, complete release notes, retained authored/build/catalog diff sections, the complete 5.22.0 patch and changed image files, and the retained image loader, HTTP factory and suspend-catching dependency. This collection review is not a full read of every assigned file, unchanged source or whole upstream repository. Full-ingest reading remains separately gated.
- Offline GitHub validation retains the same 13 unrelated historical errors and reports these two pending items, with no error for this repository. Scoped whitespace check passes. Source/changelog are unchanged.

## Collection Transport Note

The partial clone's lazy per-blob fetch was progressing but slow. Reused 1,199 hash-verified prior raw files as Git objects only inside the collector's temporary clone, then batch-prefetched 29 remaining unique blobs for existing selected roots/include paths across both tags. No raw evidence, collector code, rules, registry, budgets or selected capsule scope was changed. Collection completed successfully; no background process remains.

Follow-up: the user approved the five-file supplement; it was collected, fully read and canonically attached to the 5.21.0 work item. See `supplement-review-2026-11-07.md`. Important resolution: Android Java source/target remains 11; catalog target 17 applies to the convention build/plain Kotlin JVM tooling, not a universal Android-library bytecode change.

Next: obtain separate ingest-mode/reading approval for serial 5.21.0 -> 5.22.0 ingestion. No automatic ingest or publication.
